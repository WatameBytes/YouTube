import PySimpleGUI as sg
from _CollectChat import collectChat

window = None
layout = None
streamer_video_divider = ':'

def display_The_Program():
    global layout
    global window

    gui_title = 'YouTube comment to data'
    user_display_one = 'YouTube Link?'
    user_display_two = 'nameOfStreamer:VideoName'
    keep_after_submission = True

    layout = [
        [sg.Text(user_display_one)],
        [sg.Input(do_not_clear=keep_after_submission)],
        [sg.Text(user_display_two)],
        [sg.Input(do_not_clear=keep_after_submission)],
        [sg.Button('Submit')]]

    window = sg.Window(gui_title, layout)

def gui():
    try:
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, userInput = window.read()

            if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
                break

            link_of_video = userInput[0]
            if userInput[0] == '':
                raise ValueError("First value can't be empty")

            video_id = str(userInput[0]).split('=')[1] # Grabs the id from the link


            file_name = userInput[1]  # Grabs nameOfStreamer:VideoName for usage next class
            if userInput[1] == '':
                raise ValueError("Second value can't be empty")


            streamer_name = str(userInput[1]).split(streamer_video_divider)[0]

            if not look_for_streamer_videoname_divier(userInput[1]):
                raise ValueError("You forgot to place {}".format(streamer_video_divider))

            video_name = str(userInput[1]).split(':')[1]
            if(video_name == ''):
                raise ValueError("Video name can't be empty")

            collectChat(link_of_video, video_id, streamer_name, video_name)

        window.close()
    except ValueError as error:
        sg.popup_annoying(repr(error))
        gui()
    except IndexError:
        sg.popup_annoying('You forgot to place "="')
        gui()

def look_for_streamer_videoname_divier(s):
    try:
        s.index(streamer_video_divider)
        return True
    except ValueError:
        return False

