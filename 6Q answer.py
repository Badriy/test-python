#mark = 0
#answer = "abaacbb"
#user_answer = input("Entr your answer:")
#for i in range(len(answer)):
#    if(user_answer[i] == answer[i]):
#       mark+=1
#    else:
#        print(i, end=" ")
#print(i+1, "Out of" , len(answer))

#print()


def grade_exam(num_questions, mark_for_each):
    sum_mark = 0
    answer = input("Enter answer for {} Quetion".format(num_questions))
    user_answer = input("Enter our answer:")
    for i in range(len(answer)):
        if(user_answer[i] == answer[i]):
             sum_mark+=mark_for_each
    print(sum_mark, "Out of" , len(answer)*mark_for_each)        
grade_exam(12 , 2)












