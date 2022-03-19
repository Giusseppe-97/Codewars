import re
import os
# Text file for trials
# os.path('path to txt file')
txt = "hello, my name is Peter, I am 26 years old, and I am please to be hearing from you today my dear friend Ana Mc Miller. I am so happy. I got you invitation and I'll be there for sure; therefore I am glad to anounce that I will be having a lot of fun in my visit to California prior to your dog's marriage."

#Regular expressions might help me write this code simplified
split_string = re.split("(?<!\d)[,.;](?!\d)", txt)
print(split_string)

# by_period = txt.split(".")
# if by_period[-1] == "." or "\n": by_period = by_period[0:len(by_period)-1]
# by_word = []
# for element in by_period: 
#     a = element.split()
#     by_word.append(a)
# x=[]
# y=[]
# for i in range(len(by_period)):
#     if len(by_word[i])<25:
#         x.append(by_period[i])
#     else:
#         z = by_period[i]
#         m = z.split(", ")
#         y.append(m)
	

# print(y)
