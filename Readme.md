
#### Desafio GPI - desenvolvedor

Você foi convidado a realizar um desafio de cadastro de produtos bem simples. Queremos
avaliar sua qualidade de código, padrões REST e criatividade.

[Imagem do Projeto](contrib/desafiogpi.pdf)


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

*Criando Usuario*   
`$ curl -X POST http://127.0.0.1:8000/auth/users/ --data 'email=admin@example.com&password=admin42'`

*Obtenha o token*    
`curl -X POST http://127.0.0.1:8000/auth/token/login/ --data 'email=admin@example.com&password=admin42'`

Perfil de Usuario    
`curl -LX GET http://127.0.0.1:8000/auth/users/me/ -H 'Authorization: Token token_retornado_no_resposedo_login'`

*Faça o logout*    
`curl -X POST http://127.0.0.1:8000/auth/token/logout/ -H 'Authorization: Token token_retornado_no_resposedo_login'`

## URL da API

**GET**   

*Pedido*   
`curl -X GET http://127.0.0.1:8000/pedido -H 'Authorization: Token token_retornado_no_resposedo_login'`

*Produto*   
`curl -X GET http://127.0.0.1:8000/produto -H 'Authorization: Token token_retornado_no_resposedo_login'`

*Categoria*   
`curl -X GET http://127.0.0.1:8000/categoria -H 'Authorization: Token token_retornado_no_resposedo_login'`

*Pedido Item*   
`curl -X GET http://127.0.0.1:8000/pedidoitem -H 'Authorization: Token token_retornado_no_resposedo_login'`

**POST** 

*Pedido*   
`curl -X POST http://127.0.0.1:8000/pedido -H 'Authorization: Token token_retornado_no_resposedo_login' \
-data 'sessao=testando&status=0'`   
- *Filtros*    
  sessao   
  client_nome   
  client_pk   

*Produto*   
`curl -X POST http://127.0.0.1:8000/produto -H 'Authorization: Token token_retornado_no_resposedo_login' \
-data 'categoria=1&quantidade=5221&produto=blablabla&descricao=balbalbla+2vezes&preco=0.00'`   
- *Filtros*   
  produto   
  categoria  
  preco__gte  
  preco__lte  
  quantidade__gte   
  quantidade__gte  
 

*Categoria*   
`curl -X POST http://127.0.0.1:8000/categoria -H 'Authorization: Token token_retornado_no_resposedo_login' \
-data 'categoria=categoria'`   
- *Filtros*    
  categoria  

*Pedido Item*   
`curl -X POST http://127.0.0.1:8000/pedidoitem -H 'Authorization: Token token_retornado_no_resposedo_login' \
-data 'quantidade=10&valor=10.00&subtotal=100.00&pedido=1&produto=5'`   
- *Filtros*   
  pedido   
  produto   
  categoria  
  quantidade__gte  
  quantidade__lte  