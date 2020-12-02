import PySimpleGUI as PySG


layout = [[
    PySG.Input("First"),
    ], [
    PySG.Input("Second", readonly=True),
    ], [
    PySG.Input("Third", use_readonly_for_disable=False, disabled=True),
    ], [
    PySG.Text("Fourth"),
    ]]

window = PySG.Window("Window", layout=layout)

while True:
    event, values = window.read()
    if event is None:
        break

window.close()
