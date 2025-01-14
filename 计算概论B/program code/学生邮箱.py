# 打开文件并读取内容
with open('email.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()  # 逐行读取内容到列表中

# 写入模式 ('w' 会覆盖已有内容，'a' 是追加模式)
with open('email-1.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        file.write(line.strip()+'@qq.com'+'\n')