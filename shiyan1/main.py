import os

# 关键字
k = ["do", "for", "if", "printf", "scanf", "then", "while", "end"]
# 分界符
s = [",", ";", "(", ")", "[", "]", "//"]
# 算数运算符
aop = ["+", "-", "*", "/", "++", "--"]
# 关系运算符
rop = ["<", "<=", "=", ">", ">=", "<>"]
# 输出
comeout = ["Error", "关键字", "分界符", "算数运算符", "关系运算符", "常数", "标识符", "浮点数"]
# 结果
result = []


def judge(word):
    # 常数
    if word.isdigit():
        return 5
    if word[0].isdigit():
        for i in range(len(word)):
            if word[i].isdigit() is False:
                if word[i].isdigit() is False and (word[i + 1].isdigit() is False or i == len(word)):
                    return 6
        else:
            return 7
    if word[0] == '-':
        Flag = True
        for i in word:
            if i.isdigit() is False and i != '.' and Flag is False:
                return 0
            if i == '.':
                Flag = False
        return 5
    if word[0] == '/' and word[1] == '/':
        return 1
    if word[0] == '+' and word[1] == '+':
        return 3
    if word[0].isalpha() or word[0] == "_":
        for i in k:
            if word == i:
                return 1
        return 6
    for i in s:
        if word == i:
            return 2
    for i in aop:
        if word == i:
            return 3
    for i in rop:
        if word == i:
            return 4
    return 0


def createbiao(filename):
    if not os.path.exists(filename):
        print("文件打开失败！")
        return
    else:
        b = open(filename)
    global k, s, aop, rop
    k = []
    s = []
    aop = []
    rop = []
    choice = 0
    for line in b:
        for j in comeout:
            if j == b:
                choice = comeout.index(j)
                continue
        if choice == 1:
            k = line.split(" ")
        elif choice == 2:
            s = line.split(" ")
        elif choice == 3:
            aop = line.split(" ")
        elif choice == 4:
            rop = line.split(" ")


def main(filename):
    global result
    row = 1
    col = 1
    getstring = ""
    result = []
    if not os.path.exists(filename):
        print("文件打开失败！")
        return
    else:
        allstring = open(filename)
    for line in allstring:
        for i in line:
            if i == ' ' or i == '\n':
                num = judge(getstring)
                if num:
                    second = "({0}, {1})".format(str(num), getstring)
                else:
                    second = "Error"
                go = [getstring, second, comeout[num], "({0}, {1})".format(str(row), str(col))]
                result.append(go)
                col += 1
                getstring = ""
            else:
                getstring += i
        col = 1
        row += 1
    allstring.close()
