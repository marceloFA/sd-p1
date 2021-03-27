import sys

import Pyro4

from models import profile_deserializer


def client(archive_server_uri: str) -> None:
        """ Simula requisições provindas de um cliente
        por meio de chamadas remotas de procedimento """

        # server = ArchiveServer() agora se torna:
        server = Pyro4.Proxy(archive_server_uri)

        # executa um conjunto chamadas remotas simulando acesso a recursos remotos
        # pode ser extendido para fazer o benchmark depois
        # 1. listar todas as pessoas formadas em um determinado curso;
        response = server.filter_by(field="education", value="Engenharia de Software")
        software_engineers = profile_deserializer(response)
        

        # 2. listar as habilidades dos perfis que moram em uma determinada cidade;
        fortaleza_skills = server.list_skills_by_city(city="Fortaleza")

        # 3. acrescentar uma nova experiência em um perfil;
        new_experience = "Profesor de curso online de organização pessoal"
        email = "KaueCavalcantiCastro@teleworm.us"
        server.add_experience(email, new_experience)
        
        # 4. dado o email do perfil, retornar sua experiência;
        gabrielly_experience = server.get_experience(email="GabriellySilvaRibeiro@teleworm.us")
        print(gabrielly_experience)
        # 5. listar todas as informações de todos os perfis;
        all_profiles = server.list_profiles()
        from pprint import pprint 
        pprint(all_profiles)
        # 6. dado o email de um perfil, retornar suas informações.
        response = server.get_profile(email="JulioAzevedoSilva@dayrep.com")
        julio_profile = profile_deserializer(response)


if __name__ == "__main__":
        client(sys.argv[1])
