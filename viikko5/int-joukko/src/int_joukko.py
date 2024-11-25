KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti: int = KAPASITEETTI, kasvatuskoko:int = OLETUSKASVATUS):
        if kapasiteetti < 0:
            raise ValueError("Kapasiteetti ei voi olla negatiivinen")
        if kasvatuskoko < 0:
            raise ValueError("Kasvatuskoko ei voi olla negatiivinen")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lista = self._luo_lista(self.kapasiteetti)
        self.alkioiden_maara = 0

    def kuuluu(self, alkio):
        for indeksi in range(0, self.alkioiden_maara):
            if alkio == self.lista[indeksi]:
                return True

        return False

    def lisaa(self, alkio):
        if self.alkioiden_maara >= self.kapasiteetti:
            uusi_lista = self._luo_lista(self.alkioiden_maara + self.kasvatuskoko)
            self.kopioi_lista(self.lista, uusi_lista)
            self.lista = uusi_lista

        if self.kuuluu(alkio):
            return

        self.lista[self.alkioiden_maara] = alkio
        self.alkioiden_maara += 1

    def poista(self, alkio):
        if not self.kuuluu(alkio):
            return

        alkion_indeksi = self._alkion_indeksi(alkio)

        for indeksi in range(alkion_indeksi, self.alkioiden_maara - 1):
            self.lista[indeksi] = self.lista[indeksi + 1]

        self.alkioiden_maara -= 1

    def _alkion_indeksi(self, alkio):
        for indeksi in range(0, self.alkioiden_maara):
            if alkio == self.lista[indeksi]:
                return indeksi

    def kopioi_lista(self, lista_1, lista_2):
        for indeksi in range(0, len(lista_1)):
            lista_2[indeksi] = lista_1[indeksi]

    def mahtavuus(self):
        return self.alkioiden_maara

    def to_int_list(self):
        int_lista = self._luo_lista(self.alkioiden_maara)

        for indeksi in range(0, len(int_lista)):
            int_lista[indeksi] = self.lista[indeksi]

        return int_lista

    @staticmethod
    def yhdiste(lista_1, lista_2):
        int_joukko = IntJoukko()
        int_lista_1 = lista_1.to_int_list()
        int_lista_2 = lista_2.to_int_list()

        for indeksi in range(0, len(int_lista_1)):
            int_joukko.lisaa(int_lista_1[indeksi])

        for indeksi in range(0, len(int_lista_2)):
            int_joukko.lisaa(int_lista_2[indeksi])

        return int_joukko

    @staticmethod
    def leikkaus(lista_1, lista_2):
        int_joukko = IntJoukko()
        int_lista_1 = lista_1.to_int_list()
        int_lista_2 = lista_2.to_int_list()

        for indeksi_lista_1 in range(0, len(int_lista_1)):
            for indeksi_lista_2 in range(0, len(int_lista_2)):
                if int_lista_1[indeksi_lista_1] != int_lista_2[indeksi_lista_2]:
                    continue

                int_joukko.lisaa(int_lista_2[indeksi_lista_2])

        return int_joukko

    @staticmethod
    def erotus(lista_1, lista_2):
        int_joukko = IntJoukko()
        int_lista_1 = lista_1.to_int_list()
        int_lista_2 = lista_2.to_int_list()

        for indeksi in range(0, len(int_lista_1)):
            int_joukko.lisaa(int_lista_1[indeksi])

        for indeksi in range(0, len(int_lista_2)):
            int_joukko.poista(int_lista_2[indeksi])

        return int_joukko

    def __str__(self):
        if self.alkioiden_maara == 0:
            return "{}"
        elif self.alkioiden_maara == 1:
            return f"{{{self.lista[0]}}}"
        else:
            tuotos = "{"
            for indeksi in range(0, self.alkioiden_maara - 1):
                tuotos += str(self.lista[indeksi])
                tuotos += ", "
            tuotos += f"{str(self.lista[self.alkioiden_maara - 1])}}}"
            return tuotos
