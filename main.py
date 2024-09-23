print("Дано число n в восьмеричной СС состоящие из 5 чисел. Выведите на экран значение этого числа в десятичной системе счисления")
print("введите число в восмеричной сс")
n=input()
list_n=[int(x) for x in n]
reversed_list=list(reversed(list_n))
sum=0
for int , val in enumerate (reversed_list):
    sum+=  val*(8**int)
    print(sum)