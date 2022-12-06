
one = ['Q','W','P','S','Z','R','H','D']
two = ['V', 'B','R','W','Q','H','F']
three = ['C','V','S','H']
four = ['H','F','G']
five = ['P','G','J','B','Z']
six = ['Q','T','J','H','W','F','L']
seven = ['Z','T','W','D','L','V','J','N']
eight = ['D','T','Z','C','J','G','H','F']
nine = ['W','P','V','M','B','H']


help_dict = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine,
}



def stacks(values_to_move, from_,  to_):

    move = help_dict[from_][-values_to_move:]
    #move.reverse()
    for val in move:
        help_dict[to_].append(val)
    help_dict[from_] = help_dict[from_][:-values_to_move]

    
def main():
    holder_list =[]
    

    with open("supply.txt") as f:
        content_file = f.readlines()
        for value in content_file:
            holder_list.append(value.splitlines()[0])

    for i in range(len(holder_list)):
        curr = list(holder_list)
        num_to_move = int(curr[i][5:7].strip())

        start = curr[i][11:14].strip()
        if len(start) > 1:
             start = curr[i][12:14].strip()


        end = curr[i][16:].strip()
        if len(end) > 1:
             end = curr[i][17:].strip()
    

        start = int(start)
        end = int(end)
        stacks(num_to_move, start, end)


    for i in range(0, 9):
        print(list(help_dict.values())[i][-1])
if __name__=="__main__":
    main()    