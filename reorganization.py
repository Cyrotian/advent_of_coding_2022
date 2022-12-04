
def return_val_num(val):
    import string
    alphabet = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    for char in alphabet:
        if val in char:
            return(int(str(ord(char)-96)))

    for char in alphabet_upper:
        if val in char:
            return(int(str(ord(char) - 38)))
    
T=[]

def find_sim_val(val1, val2, val3):
    val_1 = set(val1)

    val_2 = set(val2)

    val_3 = set(val3)

    check_val = val_1.intersection(val_2).intersection(val_3)

    print(return_val_num(list(check_val)[0]))

    ret = return_val_num(list(check_val)[0])

    return ret
    

def get_val(word, lenght, second=0):

    first_half = word[slice(0, lenght //2)]
    second_half = word[slice(lenght //2, lenght)]

    first_half = list(set(first_half))
    second_half = list (set(second_half))

    similer_val = ''
    for i in range(len(first_half)):
        for t in range(len(second_half)):
            if second_half[t] == first_half[i]:
                similer_val = second_half[t]

    
    if second == 1:
        sum = 0
        word1=''
        word2=''
        word3=''
        T.append(word)
        if len(T) == 3:
            word1 = T[0]
            word2 = T[1]
            word3 = T[2] 
            print("___")
            sum += find_sim_val(word1,word2, word3)
            
            T.clear()


    return(sum)


def main():
    sum = 0
    length_of_word = 0
    groupd  = []
    with open("reorganization.txt") as f:
        content_file = f.readlines()

    for value in content_file:
        value = value.splitlines()[0]
        groupd.append(value)
        if len(groupd) == 3:
            for val in groupd:
                length_of_word = len(val)
                sum += get_val(val, length_of_word, second=1)

        if len(groupd) == 3:
            groupd = []
        
    print(sum)
if __name__=="__main__":
    main()