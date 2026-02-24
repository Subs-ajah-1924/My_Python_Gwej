class A:

    def show(self):
        print("Ini adalah show A")
class B(A):

    def show(self):
        print("Ini adalah show B")
class C(A):

    def show(self):
        print("Ini adalah show C")
class D(B,C): #iki bakal njupok method teko urutan ngene :
              #nggolek nek B,tek rak ono nggolek nek C,nek jeh rakno nko lagek di golek nek A
              #dadi nko golek golekane iku dadi koyok bentuk berlian(diamond)
    def __init__(self,name):
        self.name = name

objek = D("Subahehe")
objek.show()
