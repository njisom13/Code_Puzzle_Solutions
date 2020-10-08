import sys

numgames = 0
curr_pos = 2

game_input = []

for line in sys.stdin:
    game_input.append(line)


    

def reorder_array(x, starting_ind):

    place_holder = 1
    index_arr = starting_ind
    mid_jar = 0

    if len(x) > 1:

        while index_arr <= len(x) - 1:

            if x[index_arr] % 2 != 0 and x[index_arr - 1] % 2 == 0:

                mid_jar = x[index_arr - 1]
                x[index_arr - 1] = x[index_arr]
                x[index_arr] = mid_jar

                if index_arr > 1:
   
                    reorder_array(x, index_arr - 1)
               
            else:

                index_arr += 1
    
    


def game_winner(x):

    Raze_numbers = []
    Breach_numbers = []

    traverse_index = 0
    while(traverse_index<=len(str(x))-1):
        if(traverse_index%2==0):
            Raze_numbers.append(int(str(x)[traverse_index]))
            traverse_index+=1
        else:
            Breach_numbers.append(int(str(x)[traverse_index]))
            traverse_index+=1
    if(len(Raze_numbers) > 1):
        reorder_array(Raze_numbers,1)
        Raze_numbers.reverse()

    if(len(Breach_numbers) > 1):
        reorder_array(Breach_numbers,1)

    if(len(Raze_numbers)>len(Breach_numbers)):
        if(Raze_numbers[len(Raze_numbers)-1]%2==0):
            print(2)
        else:
            print(1)

    if(len(Breach_numbers)>len(Raze_numbers)):
        if(Breach_numbers[len(Breach_numbers)-1]%2==0):
             print(2)
        else:
             print(1)

    if(len(Breach_numbers)==len(Raze_numbers)):
        if(Breach_numbers[len(Breach_numbers)-1]%2==0):
            print(2)
        else:
            print(1)
        
    

#python method definitions have to go on  bottom
while numgames < int(game_input[0]):
    game_winner(int(game_input[curr_pos]))
    curr_pos+=2
    numgames+=1
    
                           

        

            

    

    
    

   
    
