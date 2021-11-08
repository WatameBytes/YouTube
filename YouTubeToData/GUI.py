import PySimpleGUI as sg
import collectChat

class GUI:
    def __init__(self):
        self.source = 'null=null'
        layout = [
            [sg.Text("YouTube Link?")],
            [sg.Input()],
            [sg.Text("nameOfStreamer:VideoName")],
            [sg.Input()],
            [sg.Button('Submit')]
        ]
        while True:
            window = sg.Window('YouTube comment to data', layout)

            event, userInput = window.read()

            source = userInput[0]  # Get the original source to credit
            YouTubeLink = str(userInput[0]).split('=')[1]  # Get the first input and only send the video ID

            nameOfCommentFile = userInput[1]
            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                print('I was called')
                collectChat.collectChat()
                break

        window.close()