
#def check(number):
#    temp = number
#    printed = number
#    reverse_num = 0
#    while(number > 0):
#        digit = number % 10
#        reverse_num = reverse_num*10+digit
#        number = number // 10
#    if (temp == reverse_num):
#        return(printed)
#    else:
#        return(0)

def palindromes():
    q = 0
    def palindromeCheck(s):
        number_string = str(s)
        check_number = number_string [::-1]
        if number_string == check_number:
            return True
        else:
            return False
    for i in range(100, 1000):
        for a in range(100, 1000):
            b = a * i
            if palindromeCheck(b):
                if b> q:
                    q = b
    print(q)

palindromes()
