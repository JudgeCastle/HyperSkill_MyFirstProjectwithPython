# put your python code here
num = int(input())
digit_1 = num // 100
digit_2 = (num // 10) % 10
digit_3 = num % 10

sum_of_digits = digit_1 + digit_2 + digit_3

print(sum_of_digits)