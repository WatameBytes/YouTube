import json
import pytchat

class collectChat:
    def __init__(self, source, YouTubeLink, nameOfCommentFile):
        print(nameOfCommentFile)
        self.YouTubeLink = YouTubeLink
        self.nameOfCommentFile = nameOfCommentFile
        print('Hello World')
        self.f = open(str(self.nameOfCommentFile) + 'ChatData.txt', 'w')

        self.chat = pytchat.create(video_id=YouTubeLink)
        self.dataCollecter()

    def dataCollecter(self):

        while self.chat.is_alive():
            for c in self.chat.get().items:
                obj = c.json()
                obj2 = json.loads(obj)
                self.f.write(("{}".format(obj2['elapsedTime']) + "\n"))
        self.f.close()

