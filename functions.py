import  re
from data import *

def check_credit_card(number):
    sum = 0
    for i in range(len(number)):
        if (i+1)%2==0:
            result = int(number[i])
        else:
            result = int(number[i]) * 2
            if result > 9: result = result - 9
        sum += result
    return True if sum%10 == 0 else False

def check_national_code(code):
    if not re.search(r'^\d{10}$', code): return False
    check = int(code[9])
    s = sum(int(code[x]) * (10 - x) for x in range(9)) % 11
    return check == s if s < 2 else check + s == 11

def check_payment_getway(link):
    link = link.split("/")[2] if link.startswith("https") or link.startswith("http") else link
    print(link)
    return urls.get(link) if urls.get(link) else False