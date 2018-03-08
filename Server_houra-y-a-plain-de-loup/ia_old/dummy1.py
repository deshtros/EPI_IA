from random import randrange

def lancer():
    fini = False
    old_question = ""
    while not fini:
        qf = open('./1/questions.txt','r')
        question = qf.read()
        qf.close()
        if question != old_question :
            rf = open('./1/reponses.txt','w')
            rf.write(str(randrange(6)))
            rf.close()
            old_question = question
        infof = open('./1/questions.txt','r')
        fini = "Score" in infof
        infof.close()