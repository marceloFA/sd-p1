import Pyro4
from recordclass import asdict

from models import Profile, profile_records


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class ArchiveServer:
    """Classe que implementa o arquivo de perfis
    e os métodos de manipulação de perfis"""

    def __init__(self):
        """ Popula a instânia com os exemplos de perfis criados em profile.py"""        
        self.profiles = profile_records

    def list_profiles(self) -> [Profile]:
        """
        Lista todos os perfis
        Implementa:
            5. listar todas as informações de todos os perfis
        """
        return [asdict(p) for p in self.profiles]

    def filter_by(self, field: str, value: str) -> [Profile]:
        """
        Lista os perfis que tem o valor 'value' no  campo 'field'
        Implementa:
            1. listar todas as pessoas formadas em um determinado curso;
        """
        filter_fn = lambda profile: getattr(profile, field) == value
        query = filter(filter_fn, self.profiles)
        return [asdict(profile) for profile in query]

    def list_skills_by_city(self, city: str) -> [str]:
        """Lista as habilidades dos perfis que moram em uma determinada cidade
        Implementa:
            2. listar as habilidades dos perfis que moram em uma determinada cidade;
        """

        filter_fn = lambda profile: city in self.get_city(profile)
        same_city = list(filter(filter_fn, self.profiles))
        skills = ", ".join([profile.skills for profile in same_city])
        return skills

    def get_profile(self, email: str, as_dict: bool = True) -> Profile:
        """Retorna o objeto do perfil dado como entrada a chave 'email'
        Implementa:
            6. dado o email de um perfil, retornar suas informações.
        """
        filter_fn = lambda profile: profile.email == email
        filtered = filter(filter_fn, self.profiles)
        profile = list(filtered)[0]

        return asdict(profile) if as_dict else profile

    def add_experience(self, email: str, new_experience: str) -> str:
        """Adiciona uma experiência profissional a um perfil
        Implementa:
            3. acrescentar uma nova experiência em um perfil;
        """

        profile = self.get_profile(email, as_dict=False)
        separator = ", "
        # salva a nova experiência ao
        profile.professional_experience += separator + new_experience

    def get_city(self, profile: Profile) -> str:
        """ método auxiliar para ober a cidade do endereço de um perfil"""
        # O endereço é separado por vírgulas, cidade é o segundo item
        return profile.adress.split(",")[2]

    def get_experience(self, email: str) -> str:
        """Retorna a experiência de um perfil
        Implementa:
            # 4. dado o email do perfil, retornar sua experiência;
        """
        profile = self.get_profile(email, as_dict=False)
        return profile.professional_experience


def run_server(nameserver: bool = False):
    """ Expõe o ArchiveServer para chamadas de método remotas """

    endpoints_wrapper = {ArchiveServer: "ArchiveServer"}
    Pyro4.Daemon.serveSimple(
        objects=endpoints_wrapper,
        host=None,
        ns=nameserver
    )


if __name__ == "__main__":
    # executa este código quando o arquivo é executado como script
    run_server()
