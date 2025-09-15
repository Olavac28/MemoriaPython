class Livro:
    def __init__(self, titulo, autor, ano):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano

    def getAutor(self):
        return self.__autor

    def getDados(self):
        return f"{self.__titulo}, {self.__autor}, {self.__ano}"
    
class Biblioteca:
    def __init__(self):
        self.__lista = []
    
    def adicionarLivro(self, livro):
        self.__lista.append(livro)

    def listarLivros(self):
        for livro in self.__lista:
            print(livro.getDados())
    
    def procurarPorAutor(self, nome):
        for livro in self.__lista:
            if (livro.getAutor() == nome):
                print(livro.getDados())