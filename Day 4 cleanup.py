def split_value(section1, section2):
    #section1 = '8-9'
    #section2 = '9-93'

    section1_upper = int(section1.split('-')[0])
    section1_lower = int(section1.split('-')[1])

    section2_upper = int(section2.split('-')[0])
    section2_lower = int(section2.split('-')[1])

    count = 0


    ret_count =0 
    start1 = 0
    end1 = 0
    start2 = 0
    end2 = 0


    if (section1_lower - section1_upper) > (section2_lower - section2_upper):
        start1 = section1_upper
        end1 = section1_lower
        start2 = section2_upper
        end2 = section2_lower
    else:
        start2 = section1_upper
        end2 = section1_lower
        start1 = section2_upper
        end1 = section2_lower

    for i in range(start1, end1+1):
        for j in range(start2, end2+1):
            #print(j)
            if j == i:
                count = count + 1
                break
               
    if count >= 1:
        return 1
    else:
        return 0


def main():
    holder_list =[]
    score = 0
    

    with open("cleanup.txt") as f:
        content_file = f.readlines()
        for value in content_file:
            holder_list.append(value.splitlines()[0])

    for i in range(len(holder_list)):
        curr = list(holder_list[i].strip()) 
        curr = ''.join(curr).split(',')
        score = score + split_value(curr[0], curr[1])
    print(score)

if __name__=="__main__":
    main()    