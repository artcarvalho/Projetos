class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0


    def dar_like(self, quantidade = 1):
        self._likes += quantidade

    @property
    def likes(self):
        return self._likes
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, new_name):
        self._nome = new_name.title()

    def __str__(self):
        return "%s - %s - %s" %(self.nome, self.ano, self.likes)

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return "%s - %s - %s min - %s likes "% (self.nome, self.ano, self.duracao, self.likes)
        

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada
        self.episodios = {}

    def __str__(self):
        return "%s - %s - %s Temporadas - %s likes "% (self.nome, self.ano, self.temporada, self.likes)
   
    def definir_eps(self):
        for temporadas in range(1, self.temporada+1):
            eps = int(input("Temporada %s, Episodios: "% temporadas))
            self.episodios[temporadas] = eps

    def ver_eps(self):
        for temporadas in self.episodios.keys():
            print("Temporada %s: %s Eps"%(temporadas,self.episodios[temporadas]))



class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas
    
    def __getitem__(self, item):
        return self.programas[item]

    @property
    def listagem(self):
        return self.programas

    @property
    def tamanho(self):
        return len(self.programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
jumanji = Filme("Jumanji", 2019, 120)
pb = Serie("Peaky blinders", 2020, 5)

#likes
vingadores.dar_like(55)
atlanta.dar_like(99)
jumanji.dar_like(7)
pb.dar_like(15)


lista = [atlanta, vingadores, jumanji, pb]
playlist_madrugada = Playlist("madrugada", lista)

for programas in playlist_madrugada:
    print(programas)