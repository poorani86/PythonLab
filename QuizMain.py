import random
import DisplayQuestion
def quizMain():
    questions=open("E://Python Docs/QuizQuestions.txt","r").read().splitlines()
    score_list = list()
    for i in range(10):
        question=random.choice(questions)#questions.readlines()
        ques,ans=question.split(',')
        score=DisplayQuestion.displayQuestion(ques,ans.strip())
        score_list+=[ques.strip()+','+ans.strip()+','+str(score)]
        questions.remove(question)
    print 'Your score :'
    sum=0
    for i in score_list:
        ques,ans,score=i.split(',')
        print ques+' - '+ans+' - '+score
        sum+=int(score)
    print 'Total Score : '+str(sum)

if __name__=="__main__":
    print ("Hello welcome to WordPathy!! Shall we start the Quiz (Yes/No)??")
    yesno=raw_input()
    if(yesno.upper()=='Y' or yesno.upper=='YES'):
        quizMain()
    else:
        print ("Thank you!!!")
