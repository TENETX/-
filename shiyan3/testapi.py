from main import LR1Grammar, StackSolve


LR1Grammar = LR1Grammar("LR1.txt")
Sta = StackSolve("i*i+i", LR1Grammar)
