import pytest

from server import ArchiveServer
from profile import Profile


software_engineers = [
    Profile(
        email="JulioAzevedoSilva@dayrep.com",
        first_name="Júlio",
        last_name="Azevedo Silva",
        adress="Rua Juruá, 978, Cotia-SP, 06726-385",
        education="Engenharia de Software",
        skills="Microsserviços, Apache Kafka, AWS, Terraform, Kubernetes",
        professional_experience="Estágio manutenção de infra  no UOL, Engenheiro de software na Globo",
    ),
    Profile(
        email="KaueCavalcantiCastro@teleworm.us",
        first_name="Kauê",
        last_name="Cavalcanti Castro",
        adress="Vila Multirão, 457, Fortaleza-CE, 60534-620",
        education="Engenharia de Software",
        skills="SQL, Mongo, AWS, Terraform, Kubernetes",
        professional_experience="Estágio em desenvolviemnto de aplicações de bancos de dados, Egenheiro de software livre",
    ),
]


@pytest.fixture(scope="session")
def server():
    """ Instância usada para os testes """

    return ArchiveServer()


def test_filter_by_software_engineers(server):
    """ Testa ArchiveServer.filter_by """
    field = "education"
    value = "Engenharia de Software"

    assert server.filter_by(field, value) == software_engineers


def test_fortaleza_skills(server):
    """ Testa que pode-se obter as skills de pessas da mesma cidade """
    fortaleza_skills = "Coordenação de times ágeis, Excel, Tableau, Power BI, SQL, Mongo, AWS, Terraform, Kubernetes"

    assert server.list_skills_by_city(city="Fortaleza") == fortaleza_skills


def test_add_experience(server):
    """ Testa que podemos adicionar uma nova experiência """

    kaue = server.profiles[0]
    new_experience = "Professor de curso online de organização pessoal"
    email = "KaueCavalcantiCastro@teleworm.us"
    new_field_value = "Estágio em administração em firma finaceira, estágio em administração em  banco estadual, Professor de curso online de organização pessoal"
    server.add_experience(email, new_experience)

    assert kaue.professional_experience == new_field_value


def test_get_experience(server):
    """ Testa a obtenção da experiência de um perfil """
    gabrielly_professional_exp = server.profiles[3].professional_experience
    response_experience = server.get_experience(
        email="GabriellySilvaRibeiro@teleworm.us"
    )

    assert response_experience == gabrielly_professional_exp


def test_list_profiles(server):
    """ Testa a listagem de todos os perfils """

    assert server.profiles == server.list_profiles()


def test_get_profile(server):
    """ Testa a obtenção de um perfil """
    julio = server.profiles[2]
    julio_response = server.get_profile(email="JulioAzevedoSilva@dayrep.com")

    assert julio == julio_response
