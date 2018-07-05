def displayClues(ans):
    clues = len(ans) / 2
    clue = 0
    end = 1
    temp='*'*len(ans)
    temp_list=list(temp)
    score = 10
    while end != 0:
        #print ('Clue : '+str(clue))
        if clue<clues:
            #print 'clue count : ' + str(clue)
            #print 'total clue : ' + str(clues)
            print 'Which letter you need to know?'
            letter=raw_input()
            if int(letter) > len(ans) or int(letter) < 0 or int(letter)==0:
                print 'Give letter number with in the length of the answer : 1 to '+str(len(ans))
                end=1
                continue
            if temp_list[int(letter)-1] !='*':
                print 'That letter is already given as clue. Choose another letter: '
                end=1
                continue
            if int(letter) == len(ans):
                if temp_list[int(letter)-1] == '*' and temp_list[int(letter)-2] == '*':
                    temp_list[int(letter) - 1] = ans[int(letter) - 1]
                    print ''.join(temp_list)
                    clue += 1
                    score-=2
                else:
                    print 'That letter can not be given as clue. choose another letter: '
                    end=1
                    continue
            elif int(letter) == 1:
                if temp_list[int(letter)-1] == '*' and temp_list[int(letter)] == '*':
                    temp_list[int(letter) - 1] = ans[int(letter) - 1]
                    print ''.join(temp_list)
                    clue += 1
                    score -= 2
                else:
                    print 'That letter can not be given as clue. choose another letter: '
                    end=1
                    continue
            else:
                if temp_list[int(letter)-1] == '*' and temp_list[int(letter)-2] == '*' and temp_list[int(letter)]=='*':
                    temp_list[int(letter)-1]=ans[int(letter)-1]
                    print ''.join(temp_list)
                    clue+=1
                    score -= 2
                else:
                    print 'That letter can not be given as clue. choose another letter: '
                    end=1
                    continue
            print ('Need another clue? (Y/N)')
            choice=raw_input()
            if choice.upper()=='Y':
                end = 1
            else:
                end = 0
        else:
            print 'You have exhausted all the clues'
            end=0
    return score
if __name__=="__main__":
    displayClues('clarity')