from models import Take

class TakeHelper():
    @staticmethod
    def newTake(activity, studentId):
        possScore = activity.itemsList.count(',')+1
        take = Take(studentId=studentId, complete=False, activity=activity, date="2013-12-10 00:00:00", currentQuestion=0, currentScore=0, possibleScore=possScore)
        take.save()
        return take.id