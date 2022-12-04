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
        print(curr)


if __name__=="__main__":
    main()    