""" Implementa um cliente que faz requisições ao servidor (Server)
        pedindo informações sobre os perfis.
"""
from server import ArchiveServer

# instânia do servidor que aceita chamadas de procedimento remoto
server = ArchiveServer()

# executa um conjunto chamadas remotas
# pode ser extendido para fazer o benchmark depois
# 1. listar todas as pessoas formadas em um determinado curso;
software_engineers = server.filter_by(field="education", value="Engenharia de Software")
# 2. listar as habilidades dos perfis que moram em uma determinada cidade;
fortaleza_skills = server.list_skills_by_city(city="Fortaleza")
# 3. acrescentar uma nova experiência em um perfil;
new_experience = "Profesor de curso online de organização pessoal"
email = "KaueCavalcantiCastro@teleworm.us"
server.add_experience(email, new_experience)
# 4. dado o email do perfil, retornar sua experiência;
gabrielly_experience = server.get_experience(email="GabriellySilvaRibeiro@teleworm.us")
# 5. listar todas as informações de todos os perfis;
all_profiles = server.list_profiles()
# 6. dado o email de um perfil, retornar suas informações.
julio_profile = server.get_profile(email="JulioAzevedoSilva@dayrep.com")
