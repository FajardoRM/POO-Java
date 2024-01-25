class A:
    def correr(self):
        print("Estoy en A")
        
class B(A):
    def correr(self):
        print("Estoy en B")  
        
class C(A):
    def correr(self):
        print("Estoy en C")   
        
class D(B, C):
    def correr(self):
        print("Estoy en D")    
 
b= B()
b.correr() 
        
d = D()
d.correr()                       