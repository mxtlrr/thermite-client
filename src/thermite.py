from thermite_backend import *
import PySimpleGUI as sg
import time

layout = [[sg.Text('Message:'), sg.InputText()],
          [sg.Text('ID:'), sg.InputText()],
          [sg.Text('Message 2:'), sg.InputText()],
          [sg.Text('Interval (minutes):'), sg.InputText()],
          
          [],
          [sg.Button('Start'), sg.Button('Quit')]]

# Create the Window
window = sg.Window('Window Title', layout, )
# Event Loop to process "events" and get the "values" of the inputs
while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == 'Quit': break
  if event == 'Start':
    while True:
      # TODO: read token from config.ini
      send_request(values[1], "foo",
                  values[0])
      time.sleep(int(values[3])*60)
      # Send second message
      send_request(values[1], "foo", values[2])
      # Wait again
      time.sleep(int(values[3])*60)

window.close()