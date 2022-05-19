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

def menu():
    l=Set()
    print("Введите 0, чтобы закончить, или 1, чтобы сделать множество из чисел, или 2, чтобы сделать множество символов")
    while True:
        numb = checkint()
        if numb == 1:
            while True:
                print("введите число, которое хотите добавить")
                add=checkint()
                l.add(add)
                print(l)
                print("Введите 0, чтобы закончить, или любое число,чтобы продолжить")
                numb1 = checkint()
                if numb1 == 0:
                    break
            break
        elif numb == 2:
            while True:
                print("введите символ, который хотите добавить")
                add = str(input())
                l.add(add)
                print(l)
                print("Введите 0, чтобы закончить, или любое число,чтобы продолжить")
                numb1 = checkint()
                if numb1 == 0:
                    break
            break
        elif numb == 0:
            break
        else:
            print("Введена некорректная команда")

def main():
    menu()

if __name__ == '__main__':
    main()