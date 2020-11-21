import dis


# def hello_world(nome):
#     return 'Hello ' + nome + '!'

"""
Out: 
  5           0 LOAD_CONST               1 ('Hello ')
              2 LOAD_FAST                0 (nome)
              4 BINARY_ADD
              6 LOAD_CONST               2 ('!')
              8 BINARY_ADD
             10 RETURN_VALUE

"""

def hello_world(nome):
    return f'Hello {nome} !'

"""

"""

dis.dis(hello_world)
