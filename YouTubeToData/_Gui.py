import PySimpleGUI as sg
import _CollectChat

# We don't need class, since we are not going to create instances
class DisplayTheProgram:
    def __init__(self):
        layout = [
            [sg.Text("YouTube Link?")],
            [sg.Input()],
            [sg.Text("nameOfStreamer:VideoName")],
            [sg.Input()],
            [sg.Button('Submit')]
        ]
        window = sg.Window('YouTube comment to data', layout)
        self.gui(window)


    def gui(self, window):
        event, userInput = window.read() # Pauses right here

        source = userInput[0]  # Get the original source to credit
        YouTubeLink = str(userInput[0]).split('=')[1]  # Get the first input and only send the video ID
        nameOfChatFile = userInput[1]

        window.close()
        _CollectChat.collectChat(source, YouTubeLink, nameOfChatFile)
        window.close()