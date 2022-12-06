def tuning(val):
    val = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
    i = 0
    check_list = []
    check_list_forward = []
    count = 0
    j  = 0
    checking_lists_values = []
    for i in range(len(val)):

        if i < 3:
            continue
        else:
            j = i
            for j in range(j - 3,i):
                check_list.append(val[j])

            for j in range(i+1,j+5):
                check_list_forward.append(val[j])
                
   
        set_check = list(set(check_list))
        set_check2 = list(set(check_list_forward))
        #print(set_check2)

        if val[i] not in check_list and val[i] not in check_list_forward:
            print(val[i])
            if len(set_check) > 2 and len(set_check2) > 2:
                print(f'val {val[i]} is not in {check_list}')
                print(f'val {val[i]} is not in forward {check_list_forward}')
                break

        #print(check_list)
        #print(check_list_forward)
        check_list = []
        check_list_forward = []

    print(i+1)


    #print(count)

        


    
    #print(val[1722])
            #checking_lists_values.append(set_check)



        
#1722 too low



def main():
    data = []
    content_file = ''
    with open("tuning.txt") as f:
        content_file = f.readline()
    
    content_file = content_file.strip('\n')

    #print(len(content_file))
    content_file = list(content_file)

    count = 0
    input_list = []
    #count_total = 
    tuning(content_file)





if __name__=="__main__":
    main()    