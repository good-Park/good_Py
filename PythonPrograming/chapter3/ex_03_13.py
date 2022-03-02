a = 0

while a < 10:
    a += 1
    if a == 5: continue   #while 문으로 수행이 이동한다.
    if a == 7: break      #반복문이 강제로 종료된다.
    print(a)
else:
    print('정상 종료하면 수행된다')

print('while 수행 후 %d'%a) 
