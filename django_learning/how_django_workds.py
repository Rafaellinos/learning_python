"""
        HTTP request ->  url.py
        (forward to appropriate request view)
                          |
model <- read/write -> View -> HTTP response (HTML)
                        |
                    Template.html


components:

URLs : Recebe a requisiçao e manda para a view certa
VIEW: Python function que recebe a requisição e envia de volta ao cliente, além de acessar o model/data
Models: conexão com bd
Templates: html files layout
"""

"""
django-admin startproject <NOME> # iniciar projeto
python3 manage.py startapp main # Cria um app chamado main

python3 manage.py makemigrations # cria arquivo migrations(sql commands). certifique-se se os apps estão em settings.py>INSTALLED_APPS
python3 manage.py migrate # executa os commandos sql
"""

"""
python3 manage.py shell -i ipython # interactive console
### Salva dados no bd
>>> from main.models import Flight
>>> f = Flight(origin="Washington", destination="London", duration=413)
>>> f.save()
>>> f.destination # print destination
>>> Flight.objects.all() # devolve todos os dados no bd
>>> search = Flight.objects.filter(destination=413) # devolve os dados passados pelo filtro
>>> search.__repr__() # Crie o dunder repr
>>> search[0].destination # lembre-se, um query set é uma LISTA!
>>> f = Flight.objects.first() # apenas o primeiro
>>> f.origin

# get values
>>> f = Flight.objects.all()
>>> f.values('destination') # retorna queryset com apenas os dados destination
>>> f.values('destination')[0] # dict out: {'destination': 'Value'} 
"""

"""
db: Tabelas no db são criadas com: <NOME_APP>_<NOME_CLASSE>

related_name = > usado para acessar todos atributos:
>>> airport = Airport
>>> airport.departures.all()
"""
