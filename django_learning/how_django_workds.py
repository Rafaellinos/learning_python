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

EX: 
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'main', # <-----
    ]
    
    class Airport(models.Model):
        ...
        
        Tabela => main_airport/main_flight

related_name = > usado para acessar todos atributos:
>>> airport = Airport
>>> airport.departures.all()

>>> f = Flight.objects.get(pk=1) # get object id == 1
"""

"""
Criar super admin:

python3 manage.py createsuperuser

Resistrar models em admin.py:

admin.site.register(Airport)
admin.site.register(Flight)

Para conseguir criar registro com a 
interface que o django gera.

"""



##########################################3

"""
Django Rest Framework

In [1]: from api_basic.models import Article

In [2]: from api_basic.serializers import ArticleSerializer

In [4]: from rest_framework.renderers import JSONRenderer

In [5]: from rest_framework.parsers import JSONParser

In [6]: a = Article(title = 'Article Title', author='Rafael', email='rafael@email.com')

In [7]: a.title
Out[7]: 'Article Title'

In [8]: a.save()

In [9]: a1 = Article(title = 'Article Title1', author='Rafael2', email='rafael1@email.com')

In [10]: a1.save()

In [11]: serializer = ArticleSerializer(a)

In [12]: serializer
Out[12]: 
ArticleSerializer(<Article: Article Title>):
    title = CharField(max_length=100)
    author = CharField(max_length=100)
    email = EmailField(max_length=100)
    date = DateTimeField()

In [13]: serializer.data
Out[13]: {'title': 'Article Title', 'author': 'Rafael', 'email': 'rafael@email.com', 'date': '2020-11-07T21:24:52.248738Z'}

In [14]: content = JSONRenderer().render(serializer.data)

In [15]: content
Out[15]: b'{"title":"Article Title","author":"Rafael","email":"rafael@email.com","date":"2020-11-07T21:24:52.248738Z"}'

In [16]: serializer = ArticleSerializer(Article.objects.all(), many=True)

In [17]: serializer.data
Out[17]: [OrderedDict([('title', 'Article Title'), ('author', 'Rafael'), ('email', 'rafael@email.com'), ('date', '2020-11-07T21:24:52.248738Z')]), OrderedDict([('title', 'Article Title1'), ('author', 'Rafael2'), ('email', 'rafael1@email.com'), ('date', '2020-11-07T21:25:51.783472Z')])]

"""