import time
import random
i = 0
ALPHABET = '\nABCDEFGHJKLMNPQRSTUVWXYZ23456789        ^&*RW$^&*Q#^*%'
while i <= 1000000:
    page = ""
    row = "\n"
    num = random.randint(0,200)
    for j in range(200):
        for k in range(1, num+1):
                row += (random.choice(ALPHABET))
        page += row
    print(page)
    print("DEBUG: page %d, lines: %d"%(i,page.count('\n')))
    i += 1
    time.sleep(0.5)
exit()