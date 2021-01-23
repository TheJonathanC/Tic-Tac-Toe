#MADE BY JONATHAN C.
#ENJOY YOUR TIC-TAC-TOE!


print('Welcome to tic tac toe :: ')

while True:
   
    #FIRST PLAYER
    var1 = input('choose X or O : ')
    if var1 not in 'xXoO':
        print('*'*100)
       
        #CHECKING VALIDITY
        print(f'{var1} is not a valid input : ')
        continue
       
    #SECOND PLAYER
    if var1 in 'xX':
        var2='O'
    elif var1 in 'oO':
        var2='X'
    var1=var1.upper()
    var2=var2.upper()
   
    print('\nA valid input and ')
    print('player 1 you get ',var1)
    print('player 2 you get ',var2)
    break   
#POSITIONS
print("the positions are as follows : ")
one='(1)'
two='(2)'
three='(3)'
four='(4)'
five='(5)'
six='(6)'
seven='(7)'
eight='(8)'
nine='(9)'
print(f'{seven}|{eight}|{nine}\n-----------\n{four}|{five}|{six}\n-----------\n{one}|{two}|{three}')

num=2

one=two=three=four=five=six=seven=eight=nine=' '

while True:
    again='none'
   
    #POSITIONS FOR PLAYER 1
    if num%2==0:
        pos = input(f'choose your position player 1 ({var1}): ')
       
        temp=var1
       
        nottemp=var2 

    #POSITIONS FOR PLAYER 2 ON ODD TURNS
    if num%2!=0:
        pos = input(f'choose your position player 2 ({var2}): ')
        temp=var2
        nottemp=var1
   
    print('*'*100)
   
    #IF THE POSITION IS NOT A DIGIT
    if pos.isdigit()==False:
        print(f'{pos} cannot be accepted as a valid position ')
       
        print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')
        continue
       
    #NOT IN (1-9) RANGE
    if int(pos) not in [1,2,3,4,5,6,7,8,9]:
        print(f'{int(pos)} cannot be accepted as a valid position ')
       
        print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')
        continue
   
    #OUTPUT USING F STRINGS
    if int(pos)==1 :
       
        if one==temp or one==nottemp:
            print(f'this position is already chosen {int(pos)}, plz chose another')
           
            print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')
            continue
  
        one=temp
        print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')

    if int(pos)==2 :
        if two==temp or two==nottemp:
            print(f'this position is already chosen {int(pos)}, plz chose another')
            print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')

            continue
        two=temp
        print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')
        count=1
    if int(pos)==3 :
        if three==temp or three==nottemp:
            print(f'this position is already chosen {int(pos)}, plz chose another')
            print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')

            continue
        three=temp
        print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')
        count=1
    if int(pos)==4 :
        if four==temp or four==nottemp:
            print(f'this position is already chosen {int(pos)}, plz chose another')
            print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')

            continue
        four=temp
        print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')
        count=1
    if int(pos)==5 :
        if five==temp or five==nottemp:
            print(f'this position is already chosen {int(pos)}, plz chose another')
            print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')

            continue
        five=temp
        print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')
        count=1
    if int(pos)==6 :
        if six==temp or six==nottemp:
            print(f'this position is already chosen {int(pos)}, plz chose another')
            print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')

            continue
        six=temp
        print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')
        count=1
    if int(pos)==7 :
        if seven==temp or seven==nottemp:
            print(f'this position is already chosen {int(pos)}, plz chose another')
            print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')

            continue
        seven=temp
        print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')
        count=1
    if int(pos)==8 :
        if eight==temp or eight==nottemp:
            print(f'this position is already chosen {int(pos)}, plz chose another')
            print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')

            continue
        eight=temp
        print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')
        count=1
    if int(pos)==9 :
        if nine==temp or nine==nottemp:
            print(f'this position is already chosen {int(pos)}, plz chose another')
            print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')

            continue
        nine=temp
        print(f' {seven} | {eight} | {nine}\n-----------\n {four} | {five} | {six}\n-----------\n {one} | {two} | {three}')
        count=1
       
    #ASSIGNING M AND N
    m=var1
    n=var2
   
    #GAME RULES 
    if one==two==three==m or four==five==six==m or seven==eight==nine==m or one==five==nine==m or three==five==seven==m or one==four==seven==m or two==five==eight==m or three==six==nine==m:
        print('congrats, player 1 has won : ')
        while True:
            again=input('do you wanna play again yes/no ? ')
            if again.lower()=='yes':
                break
            elif again.lower()=='no':
                break
            else:
                print('please enter yes or no only : ')
                continue
       
               
    if one==two==three==n or four==five==six==n or seven==eight==nine==n or one==five==nine==n or three==five==seven==n or one==four==seven==n or two==five==eight==n or three==six==nine==n:
        print('congrats, player 2 has won : ')
        while True:
            again=input('do you wanna play again yes/no ? ')
            if again.lower()=='yes':
                break
            elif again.lower()=='no':
                break
            else:
                print('please enter yes or no only : ')
                continue
   
    #NUM=10 BCUZ WE INITIALISED NUM =2
    if num==10:
        print('match tied :: ')
        while True:
            again=input('do you wanna play again yes/no ? ')
            if again.lower()=='yes':
                break
            elif again.lower()=='no':
                break
            else:
                print('please enter yes or no only : ')
                continue
           
    if again.lower()=='yes':
            one=two=three=four=five=six=seven=eight=nine=' '
            num=2
            continue
    elif again.lower()=='no':
            break
                     
    #CHANCE
    num+=1     
