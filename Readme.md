
#### Desafio GPI - desenvolvedor

Você foi convidado a realizar um desafio de cadastro de produtos bem simples. Queremos
avaliar sua qualidade de código, padrões REST e criatividade.

[Projeto](contrib/desafiogpi.pdf)


## Tecnologias utilizadas 

*  Projeto  
   Pipenv  
   django 
   django rest framework

* Banco de dados   
  sqllite DEV   
  postgres PROD 

* testes   
  pytest   
  pytest coverage   

* Ambientes Virtuais   
  Docker   
  Docker Compose   

* Deploy   
  Heroku 


## como rodar o projeto 

para rodar o projeto é necessario  gerar as seguintes variaveis de ambiente 
```
ENV WORKERS="1"
ENV DEBUG="True"
ENV LOG_LEVEL="INFO"
ENV ALLOWED_HOSTS="127.0.0.1, .localhost, *"
ENV SECRET_KEY="!8z6x+11-&vp3f+uy37&cur^wv&-l4v5vd+*)2pqzea=)a%++w"
ENV SECRET_KEY="eb*xnd%dbcj*u0q^y75s!mz9)87(_i@vz&i@w4r-pc3rp1duf1"
ENV FILENAME_LOG_GUNICORN="/var/log/app/gunicorn.log"
ENV FILENAME_LOG_APP="/var/log/app/app.log"
```

utilize o gerador em contrib/generete_env.py
`python contrib/generete_env.py`

#### rodando com pipenv 
```
python contrib/generete_env.py
pipenv shell 
pipenv install -d 
make test
python manage createsuperuser
python manage.py runserver 
```


#### rodando com docker
```
docker build -t brasilprev:v1 .
docker container run \  
-e DEBUG="True" \
-e LOG_LEVEL="INFO" \
-e ALLOWED_HOSTS="127.0.0.1, .localhost, *" \
-e SECRET_KEY="eb*xnd%dbcj*u0q^y75s!mz9)87(_i@vz&i@w4r-pc3rp1duf1" \ 
-e FILENAME_LOG_GUNICORN="/var/log/app/gunicorn.log" \
-e FILENAME_LOG_APP="/var/log/app/app.log" \
-p 8000:8000 \  
--name container_brasilprev brasilprev:v1 

ou  

make build run
```

#### rodando com docker-conpose 
```
docker-compose up --build 
```

### urls de acessos

auth/users/
auth/token/login/
auth/users/me/


#### Exemplos utilizando  a API com Curl 

## URL para usuario 

Criando Usuario
$ curl -X POST http://127.0.0.1:8088/auth/users/ --data 'email=email@email.com&password=alpine12'

Obtenha o token 
curl -X POST http://127.0.0.1:8088/auth/token/login/ --data 'email=email@email.com&password=alpine12'

Perfil de Usuario 
curl -LX GET http://127.0.0.1:8088/auth/users/me/ -H 'Authorization: Token b704c9fc3655635646356ac2950269f352ea1139'

Faça o logout 
curl -X POST http://127.0.0.1:8088/auth/token/logout/ -H 'Authorization: Token b704c9fc3655635646356ac2950269f352ea1139'

## URL da API

http://127.0.0.1:8000/pedido