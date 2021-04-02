import pytest
import Pyro4

from models import profile_deserializer


@pytest.fixture
def server(pytestconfig):
    """ Configura uma instância do ArchiveServer para realizar os testes """
    host_adress = pytestconfig.getoption("host")
    uri = f"PYRO:ArchiveServer@{host_adress}:1234"

    return Pyro4.Proxy(uri)


def item_1(server):
    response = server.filter_by(field="education", value="Engenharia de Software")
    software_engineers = profile_deserializer(response)


def item_2(server):
    fortaleza_skills = server.list_skills_by_city(city="Fortaleza")


def item_3(server):
    # 3. acrescentar uma nova experiência em um perfil;
    new_experience = "Profesor de curso online de organização pessoal"
    email = "KaueCavalcantiCastro@teleworm.us"
    server.add_experience(email, new_experience)


def item_4(server):
    # 4. dado o email do perfil, retornar sua experiência;
    gabrielly_experience = server.get_experience(
        email="GabriellySilvaRibeiro@teleworm.us"
    )


def item_5(server):
    # 5. listar todas as informações de todos os perfis;
    all_profiles = server.list_profiles()


def item_6(server):
    # 6. dado o email de um perfil, retornar suas informações.
    response = server.get_profile(email="JulioAzevedoSilva@dayrep.com")
    julio_profile = profile_deserializer(response)


# tests


def test_item_1(server, benchmark):
    benchmark.pedantic(
        item_1,
        args=(server,),
        rounds=20,
        iterations=100,
    )


def test_item_2(server, benchmark):
    benchmark.pedantic(
        item_2,
        args=(server,),
        rounds=20,
        iterations=100,
    )


def test_item_3(server, benchmark):
    benchmark.pedantic(
        item_3,
        args=(server,),
        rounds=20,
        iterations=100,
    )


def test_item_4(server, benchmark):
    benchmark.pedantic(
        item_4,
        args=(server,),
        rounds=20,
        iterations=100,
    )


def test_item_5(server, benchmark):
    benchmark.pedantic(
        item_5,
        args=(server,),
        rounds=20,
        iterations=100,
    )


def test_item_6(server, benchmark):
    benchmark.pedantic(
        item_6,
        args=(server,),
        rounds=20,
        iterations=100,
    )
