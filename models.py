""" Contém o esquema de um perfil e
    exemplos que podem ser usados para os métodos de
    consulta e manipulação de perfis """
from recordclass import recordclass

# Tupla de campos nomeados e mutáveis
# para conter as informações de cada perfil
Profile = recordclass(
    "Profile",
    [
        "email",
        "first_name",
        "last_name",
        "adress",
        "education",
        "skills",
        "professional_experience",
    ],
)

def profile_deserializer(response):
        """ Reconstrói o objeto após a chegada da resposta
        da chamada remota do método. Deve ser usado do lado do cliente """

        if isinstance(response, list):
                return [Profile(**item) for item in response]
        elif isinstance(response, dict):
                return Profile(**response)

# Exemplos de perfis
p1 = Profile(
    email="KaueCavalcantiCastro@teleworm.us",
    first_name="Kauê",
    last_name="Cavalcanti Castro",
    adress="Vila Multirão, 457, Fortaleza-CE, 60534-620",
    education="Administração",
    skills="Coordenação de times ágeis, Excel, Tableau, Power BI",
    professional_experience="Estágio em administração em firma finaceira, estágio em administração em  banco estadual",
)

p2 = Profile(
    email="NicoleSouzaRodrigues@rhyta.com",
    first_name="Nicole",
    last_name="Souza Rodrigues",
    adress="Rua Um, 660, Porto Alegre-RS, 90040-007",
    education="Design de interiores",
    skills="Decoração moderna, decoração rústica, decoração biaxo custo",
    professional_experience="Design de interiores em grande consultoria da área",
)

p3 = Profile(
    email="JulioAzevedoSilva@dayrep.com",
    first_name="Júlio",
    last_name="Azevedo Silva",
    adress="Rua Juruá, 978, Cotia-SP, 06726-385",
    education="Engenharia de Software",
    skills="Microsserviços, Apache Kafka, AWS, Terraform, Kubernetes",
    professional_experience="Estágio manutenção de infra  no UOL, Engenheiro de software na Globo",
)

p4 = Profile(
    email="GabriellySilvaRibeiro@teleworm.us",
    first_name="Gabrielly",
    last_name="Silva Ribeiro",
    adress="Rua Giacondo Bandeira, 1589, Piracicaba-SP, 13401-393",
    education="Engenharia de telecomunicações",
    skills="Implantação de antenas 4G, Monitoramento de serviços de redes móveis",
    professional_experience="Estágio em redes móveis na VIVO, Engenheira de teleocmunicações na VIVO",
)

p5 = Profile(
    email="KaueCavalcantiCastro@teleworm.us",
    first_name="Kauê",
    last_name="Cavalcanti Castro",
    adress="Vila Multirão, 457, Fortaleza-CE, 60534-620",
    education="Engenharia de Software",
    skills="SQL, Mongo, AWS, Terraform, Kubernetes",
    professional_experience="Estágio em desenvolviemnto de aplicações de bancos de dados, Egenheiro de software livre",
)

# Lista de perfis utilizada para construir o arquivo de consulta
profile_records = [p1, p2, p3, p4, p5]
