import os, time, sys, random
def number():
    os.system('clear')
    os.system('figlet U E 3 E X')
    try:
        os.system('rm -rif Wordlist.txt')
    except:
        pass

    print ('@ue3ex')
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    naw =input('name : ')
    asia = (naw)
    numl = [600, 800, 500, 1000, 700,]
    n = 0
    o = random.choice(numl)
    print('.........') 
    for x in range(o):
        area = random.choice(asia)
        n1 = random.choice(num)
        n2 = random.choice(num)
        n3 = random.choice(num)
        n4 = random.choice(num)
        n5 = random.choice(num)
        n6 = random.choice(num)
        n7 = random.choice(num)
        n8 = random.choice(num)
        zhm =input('chand zhmara la dway bet :')
        if zhm=='1':
           phone = area + n1 
           file = open('Wordlist.txt', 'a')
           file.write(phone + '\n')
           n += 1
           file.close()
           
          elif zhm=='2':
          	phone = area + n1 + n2
              file = open('Wordlist.txt', 'a')
             file.write(phone + '\n')
             n += 1
             file.close()
             
          elif zhm=='3':
          	phone = area + n1 + n2 + n3
              file = open('Wordlist.txt', 'a')
              file.write(phone + '\n')
              n += 1
              file.close()
              
          elif zhm=='4':
          	phone = area + n1 + n2 + n3 + n4
              file = open('Wordlist.txt', 'a')
              file.write(phone + '\n')
              n += 1
              file.close()
          	
          elif zhm=='5':
          	phone = area + n1 + n2 + n3 +n4 +n5
              file = open('Wordlist.txt', 'a')
              file.write(phone + '\n')
              n += 1
              file.close()
              
          elif zhm=='6':
          	phone = area + n1 + n2 + n3 + n4 + n5 + n6
              file = open('Wordlist.txt', 'a')
              file.write(phone + '\n')
              n += 1
              file.close()          

          elif zhm=='7':
          	phone = area + n1 + n2 + n3 + n4 + n5 + n6 + n7
              file = open('Wordlist.txt', 'a')
              file.write(phone + '\n')
              n += 1
              file.close()      


          elif zhm=='8':
          	phone = area + n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
              file = open('Wordlist.txt', 'a')
              file.write(phone + '\n')
              n += 1
              file.close()   


print('done')    
    
number()