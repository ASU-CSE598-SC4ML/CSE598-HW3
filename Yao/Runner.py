import crypten

from Yao.Participant import Participant


def main():
    crypten.init()
    participants = Participant()
    participants.perform_comparison()


if __name__ == '__main__':
    main()
