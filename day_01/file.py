import time
try:
    with open('test.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print("无法打开指定的文件")


with open('test.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        print(line, end="")
        time.sleep(0.5)

