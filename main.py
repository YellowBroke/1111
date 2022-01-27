import pandas as pd
import random
import time
import os

file = pd.read_excel('name.xlsx')
# print(file)
count = file.shape[0]
list = file.values.tolist()


def main():
    print('\n正在抽取幸运儿......\n')
    # print(count)
    # print(num)
    time.sleep(1)
    print('-----------------------------\n')
    randomCount = random.randint(1, 10)
    for i in range(randomCount):
        time.sleep(0.5)
        random.seed(random.random())
        num = random.randint(1, count)
        # print(list[num - 1][0])
        print('\r', list[num - 1][0] + "                 ", end='')
    print('\n')
    print('-----------------------------\n')
    input('如需继续抽取幸运同学，请按回车：')
    os.system('cls')
    main()


main()
