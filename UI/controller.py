import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def handle_mostra_strumenti(self, e):
        """per gestire il click sul pulsante Mostra strumenti"""
        strumenti = self._model.get_strumenti()

        self._view.lista_strumenti.controls.clear()
        if not strumenti:
            self._view.show_alert("Nessuno strumento trovato nel database.")
            self._view.update()
            return

        for strumento in strumenti:
            self._view.lista_strumenti.controls.append(ft.Text(f"{strumento}"))

        self._view.update()

    def handle_cerca_strumenti(self, e):
        """per gestisce il click sul pulsante Cerca per tipo"""
        tipo = self._view.input_tipo_strumento.value.strip()

        if not tipo:
            self._view.show_alert("Inserisci un tipo di strumento valido da cercare.")
            return

        strumenti = self._model.cerca_strumenti_per_tipo(tipo)

        self._view.lista_strumenti_ricerca.controls.clear()
        if not strumenti:
            self._view.show_alert(f"Nessuno strumento trovato per il tipo '{tipo}'.")
            self._view.update()
            return

        for strumento in strumenti:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text(f"{strumento}"))

        self._view.update()