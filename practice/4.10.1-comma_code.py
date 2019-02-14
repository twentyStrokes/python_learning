'''
input spam = ['apples', 'bananas', 'tofu', 'cats']
逗号加空格，最后一项加and
output string 'apples, bananas, tofu, and cats'
'''
def comma_code(aa):
    laststr = ''
    for i in range(len(aa)-1):
        laststr += aa[i] + ', ' 
    laststr += 'and ' + aa[-1]
    print(laststr)

spam = ['apples', 'bananas', 'tofu', 'cats']
comma_code(spam)