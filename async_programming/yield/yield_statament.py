
def corrotina():
    print('Começou')
    valor = yield
    print(f'Recebi: {valor}')


c = corrotina()
next(c)  # Começou
print(dir(c))
#c.send(10)  # Recebi: 10
# StopIteration