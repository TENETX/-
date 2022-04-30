import random


# 栈
class Stack:
    def __init__(self):
        self.__length = 0   # 记录栈内元素数量
        self.__data = []    # 用一个列表来表示栈

    def push(self, x):
        if x == '':
            print("进栈元素不能为空!")
        else:
            self.__data.append(x)
            self.__length += 1

    def pop(self):
        self.__length = len(self.__data)
        if self.__length == 0:
            print("栈已空, 不能pop!")
        else:
            self.__length -= 1
            return self.__data.pop(self.__length)

    def top(self):
        self.__length = len(self.__data)
        if self.__length == 0:
            print("栈已空!")
        else:
            return self.__data[self.__length - 1]

    def toString(self):
        res = ''
        for i in self.__data:
            res += i
        return res

    def empty(self):
        return self.__length == 0


# 文法
class Grammar:
    def __init__(self, file):
        self.grammar = {}  # 文法
        self.First = {}  # first集
        self.Follow = {}  # follow集
        self.Terminater = []  # 终结符列表
        self.tableTerminater = []  # 分析表头
        self.NonTerminater = []  # 非终结符
        self.PredictTable = {}  # 分析表
        self.beginChar = None
        try:
            f = open(file, 'r')
            fir = 1
            for line in f:
                if fir:
                    # 取第一个字符作为开始字符
                    self.beginChar = line[0]
                    fir = 0
                s = line[3:].replace('\n', '')
                a = s.split('|')
                # print(a)
                # 空串处理
                for i in range(len(a)):
                    # 读入问题
                    if a[i] == '蔚':
                        a[i] = ''
                self.grammar[line[0]] = a
        except:
            print("打开文法文件失败")
            raise IOError
        self.getTerAndNonTer()  # 求终结符和非终结符
        self.beginChar = self.NonTerminater[0]
        # 判断左递归
        if self.judgeLeftRecursion():
            print('该文法是左递归文法')
            # 转化为直接左递归
            self.modifyLeftRecusion()
            # 更新终结符和非终结符表
            self.getTerAndNonTer()
        # 求first and follow
        self.getfirst()
        self.getfollow()
        # 判断是否为LL1
        self.judgeLL1()
        # 生成预测分析表
        self.genAnalysisTable()
        # 处理时空串为‘’，所以需要去掉
        if '' in self.Terminater:
            self.Terminater.remove('')
        # 需要加入#
        self.Terminater.append('#')

    # 求终结符和非终结符
    def getTerAndNonTer(self):
        for key in self.grammar.keys():
            if key not in self.NonTerminater:
                self.NonTerminater.append(key)
            for value in self.grammar[key]:
                # 空串也算终结符
                if value == '':
                    if value not in self.Terminater:
                        self.Terminater.append(value)
                for i in value:
                    # 大小写区分终结符和非终结符
                    if not i.isupper():
                        if i not in self.Terminater:
                            self.Terminater.append(i)

    # 判度左递归
    def judgeLeftRecursion(self):
        isRecursion = self.subRecursion(self.grammar)
        # 1.直接左递归
        if isRecursion:
            print('该文法是直接左递归')
        # 2.间接左递归
        else:
            tmpGrammar = self.modify()  # 间接转直接
            isRecursion = self.subRecursion(tmpGrammar)
            if isRecursion:
                print('该文法是间接左递归')
                self.grammar = tmpGrammar
        return isRecursion

    def subRecursion(self, grammar):
        isRecursion = False
        for key in grammar.keys():
            # 一个文法一个文法的判断
            for derivation in grammar[key]:
                if derivation == '':
                    continue
                elif derivation[0] == key:
                    isRecursion = True
                    break
            if isRecursion is True:
                break
        return isRecursion

    # 间接左递归转直接左递归
    def modify(self):
        # 复制一份方便替换
        tmpGrammar = self.grammar.copy()
        tmp2 = self.grammar.copy()
        keys = list(tmpGrammar.keys())
        # 把位置颠倒从后往前判断，这样可以根据位置来消去非终结符
        keys.reverse()
        for i in range(1, len(keys)):
            tmpDe = tmpGrammar[keys[i]].copy()
            toBeMoved = []
            for de in tmp2[keys[i]]:
                # 空串或终结符则跳过
                if de == '' or de[0] in self.Terminater:
                    continue
                else:
                    # 第一个为非终结符，则判断这个推导式
                    for j in range(len(de)):
                        if de[j] in self.Terminater:
                            continue
                        # 如果是非终结符并且这个非终结符还在前面出现过，证明这个非终结符存在间接左递归
                        elif de[j] in self.NonTerminater and i > keys.index(de[j]):
                            for x in tmpGrammar[de[j]]:
                                # 这个终结符中的推导式都加上这时判定的推导式的后面的字符
                                t = x + de[j + 1:]
                                # 加入需要保留的数组
                                if t not in tmpDe:
                                    tmpDe.append(t)
                            # 加入这个推导式
                            toBeMoved.append(de)
            # 删除判定重复的推导式，也就是自身多次递归了
            for moved in toBeMoved:
                if moved in tmpDe:
                    tmpDe.remove(moved)
            # 本次判定的字符的推导式为处理后的
            tmpGrammar[keys[i]] = tmpDe
        return tmpGrammar

    # 消除直接左递归
    def modifyLeftRecusion(self):
        # 随机找一个不存在于非终结符集合里面的大写字母来进行替换
        toBeChoosed = [chr(ord('A') + x) for x in range(26)]
        toBeChoosed = [x for x in toBeChoosed if x not in self.grammar.keys()]
        tmpGrammar = self.grammar.copy()
        for key in tmpGrammar.keys():
            derivation = tmpGrammar[key]
            tmpDe = tmpGrammar[key].copy()
            isModify = False
            toBeMoved = []
            stay = []
            newNT = ''
            for de in derivation:
                if de == '':
                    continue
                # 定位到存在直接左递归的推导式
                if de[0] == key:
                    toBeMoved.append(de)
                    stay.append(de[1:])
                    newNT = random.choice(toBeChoosed)
                    isModify = True
            if isModify:
                # 这些直接左递归的推导式需要删除
                for move in toBeMoved:
                    tmpDe.remove(move)
                # 每个推导式右边加上随机选的字母
                for i in range(len(tmpDe)):
                    tmpDe[i] += newNT
                self.NonTerminater.append(newNT)
                # 新加入的那个字母的推导式
                newDe = [s + newNT for s in stay]
                # 加入空串
                newDe.append('')
                self.grammar[key] = tmpDe
                self.grammar[newNT] = newDe
        occurTimes = {}
        for value in self.grammar.values():
            for t in value:
                for subT in t:
                    if subT == '':
                        continue
                    elif subT in self.NonTerminater:
                        occurTimes[subT] = occurTimes.get(subT, 0) + 1
        # 删除一些不再在文法中起作用的非终结符了
        popKeys = [key for key in self.grammar.keys(
        ) if key not in occurTimes.keys()]
        for k in popKeys:
            self.grammar.pop(k)
            self.NonTerminater.remove(k)

    # 求first集
    def getfirst(self):
        for i in self.NonTerminater:
            self.First[i] = []
        for i in self.Terminater:
            self.First[i] = [i]
        for i in self.NonTerminater:
            # 递归
            self.subFirst(i)

    # 求first集递归
    def subFirst(self, X):
        tmpSize = len(self.First[X])
        # 终结符加入
        if X in self.Terminater and X not in self.First[X]:
            self.First[X].append(X)
        # 非终结符判断
        else:
            for derivation in self.grammar[X]:
                # 空串加入
                if derivation == '':
                    if '' not in self.First[X]:
                        self.First[X].append('')
                # 终结符加入
                elif derivation[0] in self.Terminater:
                    if derivation[0] not in self.First[X]:
                        self.First[X].append(derivation[0])
                # 非终结符则对这个非终结符进行递归
                else:
                    for i in derivation:
                        self.subFirst(i)
            # 推导结束，把推导中递归非终结符的first集加到原本这个非终结符的first集里
            for derivation in self.grammar[X]:
                if derivation == '' or derivation[0] in self.Terminater:
                    continue
                location = -1
                for i in range(len(derivation)):
                    if '' not in self.grammar[derivation[i]]:
                        location = i
                        break
                # 每个非终结符都能推出空串，所有推得的非终结符first集都要加入
                if location == -1:
                    for i in derivation:
                        for j in self.First[i]:
                            if j not in self.First[X]:
                                self.First[X].append(j)
                else:
                    # 加入前面所有能推出空串和第一个不能推出空串的字符的first集
                    for i in range(location + 1):
                        for ele in self.First[derivation[i]]:
                            if ele != '' and ele not in self.First[X]:
                                self.First[X].append(ele)
        # 长度不变就不用再推导了，找齐了
        if len(self.First[X]) == tmpSize:
            return

    # 求follow集
    def getfollow(self):
        for i in self.NonTerminater:
            self.Follow[i] = []
        self.Follow[self.NonTerminater[0]].append('#')
        for i in self.NonTerminater:
            self.Follows(i)

    # follow集
    def Follows(self, X):
        for key in self.grammar.keys():
            for derivation in self.grammar[key]:
                for i in range(len(derivation)):
                    # 找到X位置
                    if X == derivation[i]:
                        # 1.若X是最后一个字符，把Key的follow集加入X的follow集里
                        if i == len(derivation) - 1:
                            for f in self.Follow[key]:
                                if f not in self.Follow[X] and f != '':
                                    self.Follow[X].append(f)
                        # 2.若X后面为一个终结符，把这个终结符加到X的follow集里
                        elif derivation[i + 1] not in self.NonTerminater:
                            if derivation[i + 1] not in self.Follow[X]:
                                self.Follow[X].append(derivation[i + 1])
                        # 3.若X后面有非终结符，把这个非终结符的first集加到X的follow集里
                        elif derivation[i + 1] in self.NonTerminater:
                            for f in self.First[derivation[i + 1]]:
                                if f not in self.Follow[X] and f != '':
                                    self.Follow[X].append(f)
                            # 重要！后面非终结符有可能可以推出空串！
                            if '' in self.First[derivation[i + 1]]:
                                for f in self.Follow[key]:
                                    if f not in self.Follow[X] and f != '':
                                        self.Follow[X].append(f)

    # 判断LL1
    # 1.不含左递归
    # 2.如果α、β均不能推导出ε，则 FIRST(α) ∩ FIRST(β) = ∅。
    # 3.如果 β *═> ε，则 FIRST（A）∩ FOLLOW（A）= Ø
    def judgeLL1(self):
        tmpGrammar = self.grammar.copy()
        isLL1 = True
        # 第二项规则
        for key in tmpGrammar.keys():
            isLL1 = True
            alpha = []
            for i in tmpGrammar[key]:
                if i == '':
                    alpha.append('')
                else:
                    alpha.append(i[0])
            for i in range(len(alpha) - 1):
                for j in range(i + 1, len(alpha)):
                    if self.First[alpha[i]] == self.First[alpha[j]]:
                        isLL1 = False
                        break
                if not isLL1:
                    break
        if not isLL1:
            print('不是LL1文法')
            return
        # 第三项规则
        for key in self.grammar.keys():
            if '' in self.grammar[key]:
                if [x for x in self.First[key] if x in self.Follow[key]] is False:
                    isLL1 = True
                    break
        if isLL1 is False:
            print('不是LL1文法')
        else:
            print('是LL1文法')

    # 求预测分析表
    # 1. 非终结符推到不为空串, 看first集
    # 2. 非终结符推到空串, 看follow集
    def genAnalysisTable(self):
        self.PredictTable = {}
        self.tableTerminater = self.Terminater.copy()
        # 创建表头
        for first in self.First.values():
            for f in first:
                if f not in self.tableTerminater:
                    self.tableTerminater.append(f)
        for follow in self.Follow.values():
            for f in follow:
                if f not in self.tableTerminater:
                    self.tableTerminater.append(f)
        # 去除空串
        if '' in self.tableTerminater:
            self.tableTerminater.remove('')
        # 开始判断
        for nT in self.NonTerminater:
            self.PredictTable[nT] = {}
            for T in self.tableTerminater:
                derivation = self.grammar[nT]
                # 直接推导到这个终结符
                if T in derivation:
                    self.PredictTable[nT][T] = nT + '->' + T
                # first集里有这个终结符
                elif T in self.First[nT]:
                    find = False
                    # 找到对应文法
                    for de in derivation:
                        if T in de:
                            self.PredictTable[nT][T] = nT + '->' + de
                            find = True
                            break
                    # 没有对应的文法
                    if not find:
                        for de in derivation:
                            # 在每个文法的first集里找
                            for subDe in de:
                                if T in self.First[subDe]:
                                    self.PredictTable[nT][T] = nT + '->' + de
                                    find = True
                                    break
                            if find:
                                break
                # first集里没有看follow集
                elif T in self.Follow[nT]:
                    # 若推导式里有空串，就能推出follow集的其他终结符
                    if '' in derivation:
                        for fo in self.Follow[nT]:
                            self.PredictTable[nT][fo] = nT + '->ε'
                    # 否则推不出来
                    else:
                        self.PredictTable[nT][T] = ''
                else:
                    self.PredictTable[nT][T] = ''

    def getPredictTable(self):
        return self.PredictTable

    def getFirst(self):
        return self.First

    def getFollow(self):
        return self.Follow

    def getBeginChar(self):
        return self.beginChar

    def getTerminater(self):
        return self.Terminater

    def getNonTerminater(self):
        return self.NonTerminater


def StackSlove(str, filename):
    result = []
    s1 = Stack()
    s1.push("#")
    for i in str[::-1]:
        s1.push(i)
    g = Grammar(filename)
    beginc = g.getBeginChar()
    PredictTable = g.getPredictTable()
    s2 = Stack()
    s2.push('#')
    s2.push(beginc)
    last = ""
    while s2.empty() is False and s1.empty() is False:
        print(s2.toString() + "," + s1.toString())
        jud = s2.pop()
        if jud in g.getTerminater() and s1.top() in g.getTerminater() and jud != s1.top():
            print("无法使用该分析器进行分析！")
            return [], False
        if jud == s1.top():
            ret = s1.pop()
            if ret == '#':
                result.append([s2.toString(), s1.toString(),
                               "完成", "GETNEXT({})".format(ret)])
            else:
                result.append([s2.toString(), s1.toString(),
                               PredictTable[last][ret], "GETNEXT({})".format(ret)])
        else:
            ret = s1.top()
            nex = PredictTable[jud][ret]
            ss = nex[3:]
            if ss == 'ε':
                result.append([s2.toString(), s1.toString(),
                              PredictTable[jud][ret], "POP"])
            else:
                for i in ss[::-1]:
                    s2.push(i)
                result.append([s2.toString(), s1.toString(
                ), PredictTable[jud][ret], "POP, PUSH({})".format(ss)])
            last = jud
    y = False
    if s1.empty() and s2.empty():
        y = True
    return result, y
