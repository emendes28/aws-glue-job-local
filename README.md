# Projeto para ajudar no aprendizado do Glue


## Pré Requisitos
### [Python 3](https://www.python.org/downloads/)
### [Docker](https://docs.docker.com/get-docker/)
### [Terraform](https://www.terraform.io/downloads.html)
### [AWS CLI](https://aws.amazon.com/pt/cli/)

*OBS esse projeto é totalmente free e usa tecnologias open source tem os fins de estudo*

Para apontar pra um recurso da AWS pelo CLI execute 
>  aws --endpoint-url=http://localhost:4566 [recurso] [operacao]
Ex:.
>  aws --endpoint-url=http://localhost:4566 s3 list-buckets