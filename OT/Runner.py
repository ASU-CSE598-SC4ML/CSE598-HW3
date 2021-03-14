from OT.Alice import Alice
from OT.Bob import Bob


def main():
    alice = Alice(500)
    bob = Bob(600, 114514, 1919810, alice)
    bob.exec_ot()


if __name__ == '__main__':
    main()
