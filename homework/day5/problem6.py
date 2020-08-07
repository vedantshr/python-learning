class Question:
    def __init__(self, questionId, correctOption, status, score):
        self.questionId = questionId
        self.correctOption = correctOption
        self.status = status
        self.score = score

class QuestionPaper:
    def __init__(self, paperId, questionList):
        self.paperId = paperId
        self.questionList = questionList

    def checkSolutions(self, answeredDict):
        for key in answeredDict:
            for qObject in self.questionList: 
                if key == qObject.questionId:
                    if answeredDict[key] == qObject.correctOption:
                        qObject.status = "Correct"
                        print (qObject.questionId, "\t", qObject.status)
                    else:
                        qObject.status = "Incorrect"
                        print (qObject.questionId, "\t", qObject.status)

    def findResult(self):
        score = 0
        totalscore = 0
        for qObject in self.questionList:
            totalscore = totalscore + qObject.score
            if qObject.status == "Correct":
                score = score + qObject.score
            elif qObject.status == "Incorrect":
                score = score - (qObject.score/10)

        Percentage = (score/totalscore)*100
        if Percentage > 80:
            return "Pass"
        else:
            return "Fail"
    
if __name__ == "__main__":
    noOfQuestions = int(input())
    questionList = []
    for i in range(noOfQuestions):
        questionId = int(input())
        correctOption = int(input())
        score = int(input())
        obj = Question(questionId, correctOption, "", score)
        questionList.append(obj)
    questionPaperObj = QuestionPaper("ETMA122", questionList)
    noOfanswered = int(input())
    answeredDict = {}
    for i in range(noOfanswered):
        QuestionId = int(input())
        optionChosen = int(input())
        answeredDict[QuestionId] = optionChosen
    questionPaperObj.checkSolutions(answeredDict)
    result = questionPaperObj.findResult()
    print (result)



    

