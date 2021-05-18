# Load saved model
import kashgari
import os


# titleList=os.listdir("data1/title.predict")
# with open("data1/title.eventtext", "w", encoding='UTF-8') as file1:


def getEventtext(path):
    with open(path, "r", encoding="utf-8") as file:
        while 1:
            title = input("请输入标题:")
            # text=file.readline()
            # title=""
            # for t in text:
            #     print(t)
            #     if t.strip()!=' '.strip():
            #         title+=t
            #     else:
            #         break
            # print(title)
            loaded_model = kashgari.utils.load_model(
                'REVISED_location_WordEmbedding.h5')
            t = loaded_model.predict([[char for char in title]])
            print(t)
            target = ""
            source = ""
            eventtext = ""
            for i in range(len(t[0])):
                if t[0][i] == "B-source":
                    source += " " + title[i]
                if t[0][i] == "I-source":
                    source += title[i]
                if t[0][i] == "B-target":
                    target += " " + title[i]
                if t[0][i] == "I-target":
                    target += title[i]
                if t[0][i] == "B-eventtext":
                    eventtext += " " + title[i]
                if t[0][i] == "I-eventtext":
                    eventtext += title[i]

            print("source:", source)
            print("target:", target)
            print("eventtext:", eventtext)

        file.close()


# getEventtext("test.txt")

class GerAngels:
    yinxiao = ""
    shougan = ""
    chongdian = ""
    waiguan = ""
    paizhao = ""
    pingmu = ""

    def __init__(self):
        self.model = kashgari.utils.load_model(
            'REVISED_location_WordEmbedding.h5')

    def predict(title):
        t = self.model.predict([[char for char in title]])
        res = [char for char in title]
        resIndex = []
        for i in range(len(t[0])):
            resIndex.append(t[0][i])

        # for i in range(len(t[0])):
        #     if t[0][i] == "B-chongdian":
        #         chongdian += " " + title[i]
        #     if t[0][i] == "I-chongdian":
        #         chongdian += title[i]+ " "
        #     if t[0][i] == "B-waiguan":
        #         waiguan += " " + title[i]
        #     if t[0][i] == "I-waiguan":
        #         waiguan += title[i]+ " "
        #     if t[0][i] == "B-paizhao":
        #         paizhao += " " + title[i]
        #     if t[0][i] == "I-paizhao":
        #         paizhao += title[i]+ " "
        #     if t[0][i] == "B-pingmu":
        #         pingmu += title[i]
        #     if t[0][i] == "I-pingmu":
        #         pingmu += title[i]+ " "
        #     if t[0][i] == "B-shougan":
        #         shougan += title[i]
        #     if t[0][i] == "I-shougan":
        #         shougan += title[i] + " "
        #     if t[0][i] == "B-yinxiao":
        #         yinxiao += title[i]
        #     if t[0][i] == "I-yinxiao":
        #         yinxiao += title[i] + " "

        return res, resIndex

        print("外观:", waiguan)
        print("拍照:", paizhao)
        print("屏幕:", pingmu)
        print("音效:", yinxiao)
        print("充电:", chongdian)
        print("手感:", shougan)


# loaded_model = kashgari.utils.load_model('REVISED_location_WordEmbedding.h5')

# while 1:
#     title = input("请输入评论:")
#     # text=file.readline()
#     # title=""
#     # for t in text:
#     #     print(t)
#     #     if t.strip()!=' '.strip():
#     #         title+=t
#     #     else:
#     #         break
#     # print(title)
#     # loaded_model = kashgari.utils.load_model('REVISED_location_WordEmbedding.h5')
#     t = loaded_model.predict([[char for char in title]])
#     print(t)
#     yinxiao = ""
#     shougan = ""
#     chongdian = ""
#     waiguan = ""
#     paizhao = ""
#     pingmu = ""


#     for i in range(len(t[0])):
#         if t[0][i] == "B-chongdian":
#             chongdian += " " + title[i]
#         if t[0][i] == "I-chongdian":
#             chongdian += title[i]+ " "
#         if t[0][i] == "B-waiguan":
#             waiguan += " " + title[i]
#         if t[0][i] == "I-waiguan":
#             waiguan += title[i]+ " "
#         if t[0][i] == "B-paizhao":
#             paizhao += " " + title[i]
#         if t[0][i] == "I-paizhao":
#             paizhao += title[i]+ " "
#         if t[0][i] == "B-pingmu":
#             pingmu += title[i]
#         if t[0][i] == "I-pingmu":
#             pingmu += title[i]+ " "
#         if t[0][i] == "B-shougan":
#             shougan += title[i]
#         if t[0][i] == "I-shougan":
#             shougan += title[i] + " "
#         if t[0][i] == "B-yinxiao":
#             yinxiao += title[i]
#         if t[0][i] == "I-yinxiao":
#             yinxiao += title[i] + " "

#     print("外观:", waiguan)
#     print("拍照:", paizhao)
#     print("屏幕:", pingmu)
#     print("音效:", yinxiao)
#     print("充电:", chongdian)
#     print("手感:", shougan)


# with open("data1/title.predict", "r", encoding='UTF-8') as file:
#     # for title in titleList:
#     while 1:
#         text=file.readline()
#         if len(text)<3:
#             break
#         # text = input('sentence:')
#         t = loaded_model.predict([[char for char in text]])
#         print(t)
#         target = ""
#         source = ""
#         eventtext = ""
#         for i in range(len(t[0])):
#             if t[0][i] == "B-source":
#                 source +=" "+text[i]
#             if t[0][i] == "I-source":
#                 source += text[i]
#             if t[0][i] == "B-target":
#                 target +=" "+text[i]
#             if t[0][i] == "I-target":
#                 target += text[i]
#             if t[0][i] == "B-eventtext":
#                 eventtext +=" "+text[i]
#             if t[0][i] == "I-eventtext":
#                 eventtext += text[i]
#
#         # print("source:",source)
#         # print("target:", target)
#         # print("eventtext:", eventtext)
#         # print(eventtext,file=file1)
#
#         targetlist.append(target)
#         sourcelist.append(source)
#         eventtextlist.append(eventtext)
#
#
# with open("data1/title.source", "w", encoding='UTF-8') as file1:
#     for x in sourcelist:
#         print(x,file=file1)
#
# with open("data1/title.target", "w", encoding='UTF-8') as file1:
#     for x in targetlist:
#         print(x, file=file1)
#
# with open("data1/title.eventtext", "w", encoding='UTF-8') as file1:
#     for x in eventtextlist:
#         print(x, file=file1)
