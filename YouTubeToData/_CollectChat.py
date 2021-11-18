import json
import pytchat
import _GetDataAndStars

class collectChat:
    # constructor
    def __init__(self, link_of_youtube_video, video_id, streamer_name, video_name,file_name):
        self.link_of_youtube_video = link_of_youtube_video
        self.video_id = video_id
        self.streamer_name = streamer_name
        self.video_name = video_name
        self.file_name = file_name


        # We don't want to empty this file out
        # self.f = open(str(self.file_name) + 'ChatData.txt', 'w')  /// self.data_file_name


        self.chat = pytchat.create(video_id)

        self.dataCollecter()

    def dataCollecter(self):

        # while self.chat.is_alive():
        #     for c in self.chat.get().items:
        #         obj = c.json()
        #         obj2 = json.loads(obj)
        #         self.f.write(("{}".format(obj2['elapsedTime']) + "\n"))
        # self.f.close()
        # File, Source, nameOfCommentFile()

        print("Source: {}\n nameOfCommentFile: {}".format(self.link_of_youtube_video, str(self.file_name) + 'ChatData.txt'))
        self.data_file_name = 'watson:MythOrTreatChatData.txt'

        _GetDataAndStars.CalculateData(self.data_file_name, self.link_of_youtube_video, self.file_name)






