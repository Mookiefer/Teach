import PySimpleGUI as PySG

PySG.theme('LightGreen2')

layout = [[
    PySG.Input("First"),
    ], [
    PySG.Input("Second", readonly=True),
    ], [
    PySG.Input("Third", use_readonly_for_disable=False, disabled=True),
    ], [
    PySG.Text("Fourth"),
    ], [
    PySG.Exit(),
    ]]

window = PySG.Window("Window", layout=layout)

while True:
    event, values = window.read()
    if event is PySG.WIN_CLOSED:
        break
    if event == "Exit":
        break

window.close()
