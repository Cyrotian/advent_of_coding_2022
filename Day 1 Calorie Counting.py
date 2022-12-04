
def main():
    holder_list =[]
    with open("input.txt") as f:
        content_file = f.readlines()
        for value in content_file:
            holder_list.append(value.splitlines()[0])

    

    largest  = 0
    sum_val = 0

    cal_count  = []
    check_val = []
    for value in holder_list:

        
        if value == '':
            check_val.append(sum_val)
            
            if largest < sum_val:
                largest = sum_val
            sum_val = 0
                
        else:
            sum_val+= int(value)
            if not largest in cal_count:
                cal_count.append(largest)

    
    #print(sum_val)
    #print(count)
    #cal_count.sort(reverse=True)
    check_val.sort(reverse=True)
    print(sum (check_val[:3]))




if __name__=="__main__":
    main()
