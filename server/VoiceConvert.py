# import pyttsx3
# import os
# from common.commondata import CommonData
#
#
# class VoiceCon:
#
#     def __init__(self):
#         self.tts = pyttsx3.init()
#         self.index = 1
#         self.CommonData = CommonData()
#
#     def Convert(self, text):
#         self.tts.setProperty('voice', self.tts.getProperty('voice')[1])
#         name = f"F:/so_code/Graduation Design/rear_end_Python/Voice/answer{self.index}.mp3"
#         self.tts.save_to_file(text, name)
#         self.tts.runAndWait()
#         if os.path.exists(name):
#             self.index += 1
#             return self.CommonData.is_success(name, "成功")
#         else:
#             return self.CommonData.erro_data(300, "文字转语音失败")