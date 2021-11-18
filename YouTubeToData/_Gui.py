import PySimpleGUI as sg
import _CollectChat

class DisplayTheProgram:
    def __init__(self):
        gui_title = 'YouTube comment to data'
        user_display_one = 'YouTube Link?'
        user_display_two = 'nameOfStreamer:VideoName'

        layout = [
            [sg.Text(user_display_one)],
            [sg.Input()],
            [sg.Text(user_display_two)],
            [sg.Input()],
            [sg.Button('Submit')]
        ]

        window = sg.Window(gui_title, layout)
        self.gui(window)


    def gui(self, window):
        try:
            event, userInput = window.read() # Pauses right here

            link_of_youtube_video = userInput[0] # Holds the link of the YouTube video
            video_id = str(userInput[0]).split('=')[1]  # Only grabs the ID :: Needed to collect chat
            file_name = userInput[1] # Grabs nameOfStreamer:VideoName for usage next class

            streamer_name = str(userInput[1]).split(':')[0]
            video_name = str(userInput[1]).split(':')[1]

            window.close()
            # Sending the entire link, just the id, and
            _CollectChat.collectChat(link_of_youtube_video, video_id, streamer_name, video_name, file_name)
            window.close()
        except IndexError:
            print('Did you forget to place "=" or ":"?')
            window.close()