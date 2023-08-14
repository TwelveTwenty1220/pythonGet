
import os



print(os.getcwd())
os.chdir(os.pardir)
print(os.getcwd())
os.chdir('video/ts')
files=os.listdir('猎魔人')
os.chdir('猎魔人')
print(os.getcwd())
for file in files:
    if(file.startswith('0')):
        file=file.split('index.txt')[0]
        command=f'ffmpeg -f concat -safe 0 -i {file}index.txt -c copy ..\\final\\猎魔人{file}.mp4'
        print(command)
        os.system(command)


# for file in files:
#     if file.startswith('f') :
#         continue
#     else:
#         os.chdir(file)
#         file=file.split(' ')[-1]
#         command = f'ffmpeg -f concat -safe 0 -i {file}index.txt -c copy ..\\final\\{file}.mp4'
#         os.system(command)
#         os.chdir(os.pardir)


# files=os.listdir('temp')
# files.remove('final')
# os.chdir('temp')
#
# for file in files :
#     #进入文件夹
#     print(os.getcwd())
#     # for file in files :
#     ok=os.chdir(file)
#     print(os.getcwd())
#
#     command1=f'ffmpeg -f concat -safe 0 -i index.txt -c copy ..\\final\\{file}.mp4'
#     ok1=os.system(command1)
#     print(ok1)
#
#     os.chdir(os.pardir)
#     print(os.getcwd())

