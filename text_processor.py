import re, string, operator


class Text_processor:

    def __init__(self):
        self.repeat_words = {}
        self.asc = {}
        self.desc = {}

    def remove_punctuation (self, text ):
        mensaje = text
        mensaje = mensaje.lower()
        mensaje = re.sub('[%s]' % re.escape(string.punctuation), ' ', mensaje)
        mensaje = mensaje.split()
        return mensaje


    def load_file(self,file_name):
        while True:
            try:
                men= open(f'{file_name}.txt')
                return men.read()


            except FileNotFoundError:
                mensaje =" "
                print("Archivo No existe")
                exit()


    def text_charge(self,carga):
        aux = 0
        valor = 0
        for word in carga:
            aux = carga.count(word)
            if word not in self.repeat_words:
                self.repeat_words[word] = aux


    def sort_dic_asc(self):
        dic_sort_asc = sorted(self.repeat_words.items(), key=operator.itemgetter(1), reverse=True)
        self.asc=dic_sort_asc

    def sort_dic_desc(self):
        resultado = sorted(self.repeat_words.items(), key=operator.itemgetter(1))
        self.desc = resultado

    def show_results_asc(self, cantidad):
        print('___________________________________________________________-')
        print(f'{cantidad}  Palabras De Mayor Repeticion a Menor Repeticion')
        print('___________________________________________________________-')
        for word in enumerate(self.asc[0:cantidad]):
            print(word[1][0], self.repeat_words[word[1][0]])

    def show_results_desc(self, cantidad):
        print('___________________________________________________________-')
        print(f'{cantidad}  Palabras De Menor Repeticion a Mayor Repeticion')
        print('___________________________________________________________-')
        for word in enumerate(self.desc[0:cantidad]):
            print(word[1][0], self.repeat_words[word[1][0]])



tp = Text_processor()
file = input("Ingrese Nombre Del Archivo Sin Extension \n")
carga_file = tp.load_file(file)
mensaje = tp.remove_punctuation(carga_file)
print("Procesando Archivo  ")
tp.text_charge(mensaje)
tp.sort_dic_asc()
print("---------------")
tp.sort_dic_desc()
data = input("Ingrese Cantidad De Palabras Repetidas que desea ver \n")
tp.show_results_asc(int(data))
tp.show_results_desc(int(data))