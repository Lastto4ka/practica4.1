class Set:
    def __init__(self):
        self.arr = []

    def add(self, a):
        check = True
        for i in range(len(self.arr)):
            if a == self.arr[i]:
                check = False
                break
        if check:
            self.arr.append(a)
            self.arr.sort()

    def __repr__(self):
        return "{0.arr} ".format(self)

def checkint():
    while True:
        try:
           x = int(input())
           return x
        except ValueError:
            print("Введены некорректные данные")
def text():
    print("Введите 0, чтобы закончить, или 1,чтобы добавить число")
def main():
    l=Set()
    while True:
        text()
        numb=checkint()
        if numb == 1:
            print("введите число, которое хотите добавить")
            add=checkint()
            l.add(add)
            print(l)
        elif numb == 0:
            break
        else:
            print("Введена некорректная команда")

if __name__ == '__main__':
    main()