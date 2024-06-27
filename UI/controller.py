import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._statoScelto = None


    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        self._model.buildGraph(self._view._txtAnno.value)
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato!"))
        nodi = self._model.getNodi()
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumConnesse()} componenti connesse."))
        self._view._txt_result.controls.append(ft.Text("Di seguito il dettaglio sui nodi:"))
        for n in nodi:
            self._view._txt_result.controls.append(ft.Text(f"{n.StateNme} -- {self._model.getNumConfinanti(n)} vicini."))
        self.fillDD()
        self._view.update_page()


    def handleRaggiungibili(self, e):
        self._view._txt_result.controls.clear()
        raggiungibili = self._model.calcolaRaggiungibili(self._statoScelto)
        self._view._txt_result.controls.append(ft.Text(f"A partire da {self._statoScelto.StateNme} si possono raggiungere i seguenti stati:"))
        for r in raggiungibili:
            self._view._txt_result.controls.append(ft.Text(f"{r.StateNme}"))
        self._view.update_page()

    def fillDD(self):
        nodi = self._model.getNodi()
        for n in nodi:
            self._view._ddStato.options.append(ft.dropdown.Option(data=n, text=n.StateNme, on_click=self.readDD))

    def readDD(self, e):
        if e.control.data is None:
            self._statoScelto = None
        else:
            self._statoScelto = e.control.data



