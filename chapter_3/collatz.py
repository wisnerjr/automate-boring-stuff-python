def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


try:
    print('Enter number:')
    while True:
        num = int(input())
        print(collatz(num))
        if collatz(num) == 1:
            break
except ValueError:
    print('Only integers must be inserted!')
