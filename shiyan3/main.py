class LR1Grammar:

    def __init__(self, filename):
        self.grammar = []  # 表示形式1：每个推导以一个元组表示
        self.grammar2 = {}  # 表示形式2：字典表示推导
        self.NonTerminater = []  # 非终结符
        self.Terminater = []  # 终结符
        self.First = {}  # first集
        self.projectSetFamily = []  # 项目集族,一个项目集是一个列表
        self.actionTable = {}  # action表
        self.GOTOtable = {}  # goto表
        # 一个元组,(T， n， p),T表示一个产生式编号,n表示右边圆点的位置,p表示展望符,是一个列表
        try:
            f = open(filename, 'r')
            for line in f:
                nT = line[0]
                derivation = line[3:].replace('\n', '')
                self.grammar.append((nT, derivation.replace('蔚', 'ε')))
            f.close()
        except:
            raise IOError('文件打开失败!')
        # 求终结符和非终结符
        self.__CalnTandT()
        for nT in self.NonTerminater:
            self.grammar2[nT] = []
        for item in self.grammar:
            self.grammar2[item[0]].append(item[1])
        print('非终结符集合：', self.NonTerminater)
        print('终结符集合:', self.Terminater)
        # 求first集
        self.allFirst()
        # 求项目集
        self.calProjectSetFamily()
        # 求LR表
        self.calActionAndGOTOTable()

    # 计算终结符和非终结符
    def __CalnTandT(self):
        for item in self.grammar:
            if item[0] not in self.NonTerminater:
                self.NonTerminater.append(item[0])
        for item in self.grammar:
            for subDe in item[1]:
                if subDe not in self.NonTerminater \
                        and subDe not in self.Terminater:
                    self.Terminater.append(subDe)

    # 求一个符号的first集
    def allFirst(self):
        for T in self.Terminater:  # 终结符的first集就是他自己
            self.First[T] = [T]
        for nT in self.NonTerminater:  # 先循环给非终结符的first集一个空列表
            self.First[nT] = []
        if 'ε' in self.First.keys():  # 空字不是终结符，得去掉
            self.First.pop('ε')
        for nT in self.NonTerminater:
            derivation = self.grammar2[nT]
            if 'ε' in derivation:   # 空字在推导中，就把空字也加入它的first集中
                self.First[nT].append('ε')
        for item in self.grammar:
            derivation = item[1]
            if derivation == 'ε':
                continue
            if derivation[0] in self.Terminater:
                self.First[item[0]].append(derivation[0])
        # 从最后一个文法开始往前推
        # 这样将非终结符first集进行加入的时候更加的方便
        for i in range(len(self.grammar) - 1, -1, -1):
            if self.grammar[i][1] == 'ε':
                continue
            de = self.grammar[i][1]
            allHaveNone = True
            for subDe in de:
                if subDe in self.NonTerminater:  # 如果一个产生式右边第一个字符是非终结符
                    for f in self.First[subDe]:  # 就把这个非终结符的first集给推出它的非终结符
                        if f not in self.First[self.grammar[i][0]]:
                            self.First[self.grammar[i][0]].append(f)
                    if 'ε' not in self.First[subDe]:
                        allHaveNone = False
                        break
                elif subDe in self.Terminater:  # 产生式中有一个终结符，就退出for
                    break
            # for正常执行完，说明一个产生式右边全是非终结符
            else:
                if allHaveNone:  # 再看这个全部是非终结符的标记是否为真
                    self.First[self.grammar[i][0]].append('ε')

    # 求一个符号串X的first集
    def first(self, X):
        if self.First == {}:
            print('先调用allFirst方法')
            return
        # 符号串，所以默认没有空字，就不用考虑空字
        res = []
        for subX in X:
            if subX in self.NonTerminater:  # 如果字符是非终结符
                res += self.First[subX]
                if 'ε' not in self.First[subX]:  # 如果这个非终结符的first集没有空字，就退出
                    break   # 有空字，就能继续往后看
            elif subX in self.Terminater and subX not in res:  # 终结符就加入结果列表并退出循环
                res.append(subX)
                break
        return res

    # 求文法的项目集族
    def calProjectSetFamily(self):
        # 元组（T，n，p）
        T = 0  # 第一个产生式标号为0
        n = 1  # 第一个项目右边圆点位置是第一个
        p = '#'  # 第一个项目的展望符肯定是#
        I0 = self.__closure([(T, n, p)])  # 先求第一个项目的闭包
        self.projectSetFamily.append(I0)  # 加入项目集族
        allChar = self.NonTerminater + self.Terminater  # 文法的所有符号
        allChar.remove(self.NonTerminater[0])  # 去掉拓广文法的最开始符
        for projectset in self.projectSetFamily:  # 对每个项目集和每个文法，求
            for char in allChar:
                J = self.__J(projectset, char)
                if not J:
                    continue
                tmp = self.__closure(J)
                if tmp not in self.projectSetFamily:
                    self.projectSetFamily.append(tmp)

    # 求一个项目的闭包
    def __closure(self, project):
        # project是一个项目，是一个三个元素的元组
        res = project
        for item in res:
            T = item[0]  # 产生式编号
            n = item[1]  # 右边圆点位置，用来索引圆点右边那个符号
            p = item[2]  # 当前项目item的展望符
            sizeOfProduct = len(self.grammar[T][1])
            if n == sizeOfProduct + 1:  # 如果圆点的位置在产生式的最后，那么就跳过当前这个产生式，看下一个
                continue
            X = self.grammar[T][1][n - 1]  # 索引圆点右边那个符号
            if X in self.NonTerminater:  # 如果X是非终结符
                # 先求这个X后面的符号连接上展望符的first集
                if n == sizeOfProduct:
                    first = p
                else:
                    # 再求展望符
                    first = self.first(self.grammar[T][1][n] + p)
                prods = []    # 求X作为产生式左边的推导的编号
                for i in range(len(self.grammar)):
                    if self.grammar[i][0] == X:
                        prods.append(i)
                # 把不在原项目集中的项目加到当前项目集中
                for prod in prods:
                    for f in first:
                        if (prod, 1, f) not in res:
                            res.append((prod, 1, f))
        return res

    # 求一个项目集J
    def __J(self, Ii, X):
        res = []
        for project in Ii:
            T = project[0]  # 项目的产生式的标号
            n = project[1]  # 右边圆点位置
            p = project[2]  # 项目的展望符
            product = self.grammar[T][1]  # 产生式右边的字符串
            # 遍历这个推导，由于字符串的特性，因此这里用下标的方式来遍历
            for i in range(len(product)):
                if product[i] == X:  # 第i个字符是X，
                    if i == n - 1:  # 如果它在圆点右边，就把它加入res
                        res.append((T, n + 1, p))
        return res

    # 定义Go函数,返回一个项目集在项目集族中的标号
    def __GO(self, Ii, X):
        J = self.__J(self.projectSetFamily[Ii], X)
        closureJ = self.__closure(J)
        res = -1
        for i in range(len(self.projectSetFamily)):
            if closureJ == self.projectSetFamily[i]:
                res = i
                break
        return res

    # 求action表和goto表
    # 规则1：若项目A→α·aβ属于Ik且GO(Ik, a)＝Ij，a为终结符，则置ACTION[k,a] 为“sj”
    # 规则2：若项目A→α·属于Ik，那么，对任何终结符a(或结束符#)，置ACTION[k,a]为 “rj”(假定产生式A→α是文法G‘的第j个产生式)。
    # 规则3：若项目S’→S·属于Ik，则置ACTION[k,#]为 “acc”
    # 规则4：若GO(Ik,A)＝Ij，A为非终结符，则置GOTO[k,A]=j。
    def calActionAndGOTOTable(self):
        statusNum = len(self.projectSetFamily)  # 状态数
        Terminater = self.Terminater.copy()
        Terminater.append('#')
        # 先把所有项目集放到一个列表里
        allProject = []
        for projectSet in self.projectSetFamily:
            allProject += [x for x in projectSet if x not in allProject]
        # 遍历每个项目集
        for k in range(statusNum):
            # 初始，给每个状态一个空字典，通过双重字典来实现两个字符索引
            self.actionTable[k] = {}
            self.GOTOtable[k] = {}
            for T in self.Terminater:
                # 赋空字防止出错
                self.actionTable[k][T] = ''
            self.actionTable[k]['#'] = ''
            for NT in self.NonTerminater:
                self.GOTOtable[k][NT] = ''
        for project in allProject:  # 遍历每个项目
            T = project[0]  # 项目的产生式的标号
            n = project[1]  # 右边圆点位置
            p = project[2]  # 项目的展望符
            sizeOfProduct = len(self.grammar[T][1])
            for k in range(statusNum):
                # 某项目不在某项目集就跳过
                if project not in self.projectSetFamily[k]:
                    continue
                # 执行到这说明该项目在某项目集中
                # 规则3
                if T == 0 and n == 2 and p == '#':
                    self.actionTable[k]['#'] = 'acc'
                else:
                    # 规则2
                    if n == sizeOfProduct + 1:
                        self.actionTable[k][p] = 'r' + str(T)
                        print('action({},{})='.format(k, p), 'r' + str(T))
                    else:
                        # 规则1
                        a = self.grammar[T][1][n - 1]
                        if a in Terminater:
                            j = self.__GO(k, a)
                            if j != -1:
                                self.actionTable[k][a] = 's' + str(j)
                                print('goto({},{})='.format(
                                    k, a), 's' + str(j))
                        # 规则4
                        A = self.grammar[T][0]
                        j = self.__GO(k, A)
                        if j != -1:
                            self.GOTOtable[k][A] = j

    def GetGrammar(self):
        return self.grammar

    def GetGrammar2(self):
        return self.grammar2

    def GetTerminater(self):
        return self.Terminater

    def GetNonTerminater(self):
        return self.NonTerminater

    def GetFirst(self):
        return self.First

    def GetProjectSetFamily(self):
        return self.projectSetFamily

    def GetActionTable(self):
        return self.actionTable

    def GetGOTOtable(self):
        return self.GOTOtable


def StackSolve(strr, Lr):
    terminater = Lr.GetTerminater()
    terminater.append("#")
    actionTable = Lr.GetActionTable()
    GOTOtable = Lr.GetGOTOtable()
    grammar = Lr.GetGrammar()
    print(grammar)
    stackf = "#"
    stacks = strr + "#"
    result = []
    num = 0
    status = ["0"]
    while True:
        try:
            statusnow = int(status[len(status) - 1])
            judgeChar = stacks[0]
            if actionTable[statusnow][judgeChar]:
                nowstatus = "".join(status)
                if actionTable[statusnow][judgeChar][0] == "r":
                    nextstep = int(actionTable[statusnow][judgeChar][1])
                    word = grammar[nextstep][0]
                    changeword = grammar[int(actionTable[statusnow][judgeChar][1])][1]
                    changestatus = str(GOTOtable[int(status[len(status) - len(changeword) - 1])][word])
                    result.append([num + 1, nowstatus, stackf, stacks, "r{}:{}->{},归约,GOTO({}, {})={}".format(
                        actionTable[statusnow][judgeChar][1], word, changeword, status[len(status) - len(changeword)], word, changestatus)])
                    status = status[:len(status) - len(changeword)]
                    stackf = stackf[:len(stackf) - len(changeword)]
                    stackf += word
                    print(stackf)
                    status.append(changestatus)
                elif actionTable[statusnow][judgeChar][0] == "s":
                    result.append([num + 1, nowstatus, stackf, stacks, "action({}, {})=s{},状态{}入栈".format(
                        statusnow, judgeChar, actionTable[statusnow][judgeChar][1], actionTable[statusnow][judgeChar][1])])
                    status.append(actionTable[statusnow][judgeChar][1])
                    stackf += judgeChar
                    stacks = stacks[1:]
                elif actionTable[statusnow][judgeChar] == "acc":
                    result.append([num + 1, nowstatus, stackf, stacks, "分析成功！"])
                    return result
                else:
                    print("出错")
                    return []
                print(result[num])
                num += 1
            else:
                print("出错")
                return []
        except:
            print("出错")
            return []
