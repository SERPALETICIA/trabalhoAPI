# APS 01- API REST com Postgres

Integrantes:
Gabriel Martinello
Leticia Serpa 
Vitoria Zanella 

##Dependencias do projeto

''' shell
poetry add fastapi
poetry add sqlmodel
poetry add unicorn
poetry add psycopg2-binary
'''

uvicorn server:app --reload

Olar, eu e a Leh commitamos no git, porém a Vitória que fez boa parte da estrutura do projeto

Então, a senha do meu banco era 123, então eu deixei o comando do docker da seguinte forma:
docker run --name pg-db -p 54322:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=123 -e POSTGRES_DB=oficina -d postgres:14