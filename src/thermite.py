from thermite_backend import *
import PySimpleGUI as sg
import time

token_read = get_token_from_ini("config.ini")
print(f"Read token as {token_read}")

layout = [[sg.Text('Message:'), sg.InputText()],
          [sg.Text('ID:'), sg.InputText()],
          [sg.Text('Message 2:'), sg.InputText()],
          [sg.Text('Interval (minutes):'), sg.InputText()],
          
          [],
          [sg.Button('Start'), sg.Button('Quit')]]

# Create the Window
window = sg.Window('Thermite Client', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == 'Quit': break
  if event == 'Start':
    sg.popup("When you close this popup, we will start.")
    while True:
      # TODO: read token from config.ini
      send_request(values[1], token_read, values[0])
      time.sleep(int(values[3])*60)
      send_request(values[1], token_read, values[2]) # 2nd message
      time.sleep(int(values[3])*60) # wait

window.close()