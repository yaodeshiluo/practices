# coding=utf-8
d=dict(a=1,b=2,c=3)
try:
    import cpickle as pickle
except ImportError:
    import pickle

s=pickle.dumps(d)

f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()

f=open('dump.txt','rb')
h=pickle.load(f)
f.close()

pickle.loads(pickle.dumps(d))

import json
w=json.dumps(d)
i=json.loads(w)

import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }


s = Student('Bob', 20, 88)
y=json.dumps(s,default=student2dict)
y=json.dumps(s,default=lambda obj:obj.__dict__)
s.__dict__ #属性not callable

from PIL import Image
im=Image.open(r'D:\yao\test.jpeg')
im.show()
w,h =im.size

im.thumbnail((w//2,h//2))

im.save(r'D:\yao\test.jpeg','jpeg')
import pip; print(pip.pep425tags.get_supported())

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')