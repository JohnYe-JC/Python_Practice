from random import randint
you = 0
cpu = 0
count = 0
while you == cpu:
    if count:
        print('双方打平，重新开始！')
    for i in range(1, 6):
        print('第%d轮'% i)
        print('射门方向:')
        a = int(input())
        b = int(randint(1, 4))
        if a != b:
            you += 1
            print('你得分！')
        else:
            print('你未得分...')
        print('You：%d， ' % you + 'CPU：%d' % cpu)
        print('防守方向:')
        a = input()
        b = randint(1, 4)
        if a != b:
            cpu += 1
            print('电脑得分！')
        else:
            print('电脑未得分...')
        print('You：%d， ' % you + 'CPU：%d' % cpu)
    count += 1
if you > cpu:
    print('You win!')
else:
    print('CPU win!')
