print("Дано число n в восьмеричной СС состоящие из 5 чисел. Выведите на экран значение этого числа в десятичной системе счисления")
print("Введите пятизначное число в восмеричной сс")
n = int(input())
eight_last = n % 10
n //= 10
ten_last = eight_last * (8**0)
eight_prev = n % 10
n //= 10
ten_prev = eight_prev * (8**1)
eight_third = n % 10
n //= 10
ten_third = eight_third * (8**2)
eight_second = n % 10
n //= 10
ten_second = eight_second * (8**3)
eight_first = n % 10
n //= 10
ten_first = eight_first * (8**4)
sum = ten_last + ten_prev + ten_third + ten_second + ten_first
print("Число в десятичной сс ", sum)
