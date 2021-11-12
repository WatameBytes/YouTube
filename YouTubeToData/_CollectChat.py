import json
import pytchat
import _GetDataAndStars

class collectChat:
    def __init__(self, source, YouTubeLink, nameOfCommentFile):

        self.YouTubeLink = YouTubeLink
        self.nameOfCommentFile = nameOfCommentFile
        self.source = source
        # self.f = open(str(self.nameOfCommentFile) + 'ChatData.txt', 'w')
        self.file = 'watson:GoodnightASMRChatData.txt'

        self.chat = pytchat.create(video_id=YouTubeLink)
        # BREAKS HERE
        self.dataCollecter()

    def dataCollecter(self):

        # while self.chat.is_alive():
        #     for c in self.chat.get().items:
        #         obj = c.json()
        #         obj2 = json.loads(obj)
        #         self.f.write(("{}".format(obj2['elapsedTime']) + "\n"))
        # self.f.close()
        # File, Source, nameOfCommentFile()
        print("File: {}\n Source: {}\n nameOfCommentFile: {}".format(self.file, self.source, self.nameOfCommentFile))
        _GetDataAndStars.CalculateData(self.file, self.source, self.nameOfCommentFile) # Overwrites the text file with data



