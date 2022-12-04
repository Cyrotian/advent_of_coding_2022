from itertools import permutations




def rep(val, num=0):
    
    win = 6
    lose = 0
    draw = 3


   #X = Rock
   #Y = paper
   #Z = Scissors

   #A - Rock
   #B - Paper
   #C - Scissors



    X = 1 #lose
    Y = 2 #draw
    Z = 3 #win

    if val[0] == 'A' and val[1] == 'X':
        if num == 1 :
            if val[1] == 'X':
                return lose + Z
        return draw +  X

    elif val[0] == 'A' and val[1] == 'Y':
        if num == 1 :
            if val[1] == 'Y':
                return draw + X
        return win + Y


    elif val[0] == 'A' and val[1] == 'Z':
        if num == 1 :
            if val[1] == 'Z':
                return win + Y
        return lose + Z



    elif val[0] == 'B' and val[1] == 'Y':
        if num == 1 :
            if val[1] == 'Y':
                return draw + Y
        return draw + Y

    elif val[0] == 'B' and val[1] == 'Z':
        if num == 1 :
            if val[1] == 'Z':
                return win + Z
        return win + Z

    elif val[0] == 'B' and val[1] == 'X':
        if num == 1 :
             if val[1] == 'X':
                return lose + X
        return lose + X

    elif val[0] == 'C' and val[1] == 'Z':
        if num == 1 :
            if val[1] == 'Z':
                return win + X
        return draw + Z

    elif val[0] == 'C' and val[1] == 'Y':
        if num == 1 :
            if val[1] == 'Y':
                return draw + Z

        return lose + Y 
    elif val[0] == 'C' and val[1] == 'X':
        if num == 1 :
            if val[1] == 'X':
                return lose + Y
        return win + X
        

    
     

def main():
    holder_list =[]
    score = 0

    with open("rock_paper_scissor.txt") as f:
        content_file = f.readlines()
        for value in content_file:
            holder_list.append(value.splitlines()[0])
    
    for i in range(len(holder_list)):
        curr = list(holder_list[i].strip()) 

        curr = ''.join(curr).split()
        print(curr)

        print(rep(curr,1))
        score += rep(curr,1)


    print(score)
if __name__=="__main__":
    main()    

 ##   holder_list = [['A', 'Y'],['B', 'X'],['C', 'Z'] ]
  ##  score = 0 
##    for i in range(len(holder_list)):
 ##       curr = holder_list[i]
 ##       print(curr)

 ##       print(rep(curr))
  ##      score += rep(curr)
    
 ##   print(score)
