import _Gui
import _CollectChat

def main():
    # TODO We have class/instance methods yet we are not treating them as objects...
    # TODO Learn about Pyton constructors and refactor this code
    # Turn all of this data into an object to easily call it and deal with it
    # Remove all the selfs and classes, this isn't needed
    # Just create a data object that we can pass
    # _Gui.DisplayTheProgram()

    link_of_youtube_video = 'https://www.youtube.com/watch?v=VupT9JCJaOY'
    video_id = 'VupT9JCJaOY'
    streamer_name = 'watson'
    video_name = 'MythOrTreat'
    file_name = 'watson:MythOrTreat'
    _CollectChat.collectChat(link_of_youtube_video, video_id, streamer_name, video_name, file_name)

if __name__ == '__main__':
    main()