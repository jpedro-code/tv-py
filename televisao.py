class Televisao:
    def __init__(self):
        self.ligar = False
        self.canal= 5
    def power(self):
        if self.ligar:
            self.ligar = False
        else:
            self.ligar = True
    def aumenta_canal(self):
        self.canal+=1
    def diminui_canal(self):
        self.canal-=1

if __name__ == '__main__':

    televisao = Televisao()
    televisao.power()
    print(televisao.ligar)
    televisao.aumenta_canal()
    print(televisao.canal)
    televisao.diminui_canal()
    print(televisao.canal)

