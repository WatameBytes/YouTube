import _Gui
import _CollectChat

def main():
    # _Gui.DisplayTheProgram()
    link_of_youtube_video = 'https://www.youtube.com/watch?v=VupT9JCJaOY'
    video_id = 'VupT9JCJaOY'
    streamer_name = 'watson'
    video_name = 'MythOrTreat'
    file_name = 'watson:MythOrTreat'
    _CollectChat.collectChat(link_of_youtube_video, video_id, streamer_name, video_name, file_name)
    # Test this sync
    # Test this out to see if branch is new
if __name__ == '__main__':
    main()