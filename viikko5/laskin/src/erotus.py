class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.miinus(int(self._lue_syote()))

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)