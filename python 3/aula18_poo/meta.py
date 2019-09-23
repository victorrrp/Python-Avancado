'''
EM PYTHON TUDO É UM OBJETO: incluindo classes.
Metaclasses são as 'classes' que criam classes.
type é uma metaclasse??
'''
class Meta(type): #Criando uma metaclasse
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)


        if 'b_fala' not in namespace:
            print(f'Oi, voce precisa criar o metodo b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print('b_fala precisa ser um metodo, não um atributo. ')
        
        return type.__new__(mcs, name, bases, namespace)

class A(metaclass=Meta): #usando a metaclasse
    def fala(self):
        self.b_fala()

class B(A):
    teste = 'Valor'
    
    def b_fala(self):
        print('Oi')

    def sei_la(self):
        pass
