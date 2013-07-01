def is_palindromic(num):
    str_num = str(num)
    if(str_num == str_num[::-1]):
        return True
    else:
        return False

palindromic = []

for i in range(100, 999):
    for x in range(100, 999):
        temp = i * x
        if(is_palindromic(temp)):
            palindromic.append(temp)

print max(palindromic)
        
