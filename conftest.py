""" Configurações dos testes """

def pytest_addoption(parser):
    """ Permite passar o enderço do host como um argumento de linha de comando """
    parser.addoption("--host", action="store")