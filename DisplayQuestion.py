import DisplayClues
def displayQuestion(ques,answer):
    print (ques)
    print ("*" * (len(answer)))
    print ("Need a clue or Want to answer the question? (1/2) : ")
    score = 0
    choice = raw_input()
    i = 1
    while i != 0:
        if choice == '1':
            #print 'display clues'
            score=DisplayClues.displayClues(answer)
            print('Enter answer : ')
            useranswer = raw_input()
            if useranswer.lower() == answer.lower().strip():
                print('Correct..')
            else:
                print('Wrong answer')
                score = 0
            i = 0
        elif choice == '2':
            print('Enter answer : ')
            useranswer = raw_input()
            if useranswer.lower() == answer.lower().strip():
                print('Correct..')
                score = 10
                i = 0
            else:
                print('Wrong answer')
                score = 0
                i = 0
        else:
            print('Enter 1 or 2 :')
            choice = raw_input()
            i = 1
    return score


if __name__=="__main__":
    score=displayQuestion("color of sky","blue")
    print("your score : "+str(score))

