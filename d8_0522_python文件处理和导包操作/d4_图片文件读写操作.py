# 需求；复制pic1.png---得到pic2.png
# 读取pic1.png
img1 = 'D:\Pycharm_workspace\py61\d8_0522_python文件处理和导包操作\pic1.png'
myimg = open(file=img1,mode='rb')
data = myimg.read()
print(data)
myimg.close()

# 写入pic2.png
img2 = 'D:\Pycharm_workspace\py61\d8_0522_python文件处理和导包操作\pic3.png'
# myimg2 = open(file = img2,mode='wb')
# myimg2.write(data)
# myimg2.close()

with open(file = img2,mode='wb') as myimg2:
    myimg2.write(data)