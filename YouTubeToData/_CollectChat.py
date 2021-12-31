# This file will gather chat data and place it in a text file, mostly time stamps
import json
import pytchat
import _GetDataAndStars

class collectChat:
    # Python Constructor
    def __init__(self, link_of_youtube_video, video_id, streamer_name, video_name):
        # Self is like the keyword 'this' in Java/JavaScript
        self.link_of_youtube_video = link_of_youtube_video
        self.video_id = video_id
        self.streamer_name = streamer_name
        self.video_name = video_name
        # Just print the id to show it's in the works
        print("Video ID: {} has started collecting chat data".format(self.video_id))

        # Place the video ID into an instance variable
        self.chat = pytchat.create(video_id)
        # Calls the function that makes use of that video_id
        self.dataCollecter()

    def dataCollecter(self):
        # pytchat is our algorithm that scans YouTube chat
        # while self.chat.is_alive():
        #     for c in self.chat.get().items:
        #         obj = c.json()
        #         obj2 = json.loads(obj)
        #         self.f.write(("{}".format(obj2['elapsedTime']) + "\n"))
        # self.f.close()

        print("Video ID: {} has finished collecting chat data".format(self.video_id))

        self.nameOfSaveFile = self.streamer_name + ":" + self.video_name + "_ChatData.txt"
        print('nameOfSaveFile: {}'.format(self.nameOfSaveFile))


        # _GetDataAndStars.CalculateData(self.data_file_name, self.link_of_youtube_video, self.file_name)
