
#Task: Want to create a program that will model what my schedule will 
#      look like next school year. It will show me if my shool schedules 
#      are actually viable. Gonna hopefully get it to show how much time 
#      I will have per day for hw. I want it to break down my week.

from enum import Enum, unique
import time

#Data format: (name, in-class time, Est HW time)

#School tags: WHA - Wilson Hill Academy, BP - Baptist Prep, ST - STEAM Co-op, OT - other

#There are 84 working hours in a 7 day week with 12 working hours a day.
timeInWeek = 84.0
timeInDay = 12.0

schoolList = ["WHA", "BP", "ST", "OT"]

@unique
class activityType(Enum):
    CLASS = 1
    SPORT = 2
    PROJECT = 3
    JOB = 4
    EXTRACURRICULAR = 5 
    VOLUNTEER = 6
    RELIGIOUS = 7 # for youth and church

SchoolTravelConversions = {
    "WHA" : float(0),
    "BP" : float(20*2),
    "ST" : float(40*2),
}

weekDayHourTracker = {
    "Sun" : timeInDay,
    "Mon" : timeInDay,
    "Tues" : timeInDay,
    "Wed" : timeInDay,
    "Thurs" : timeInDay,
    "Fri" : timeInDay,
    "Sat" : timeInDay
}

classSchedule = list()


class classObj:
    className = str()
    classInClassTime = float()
    classEstHw = float()
    classSchool = str()
    classTravelEST = float()
    classDaysOfWeek = list()

    def __init__(self, className, classInClassTime, classEstHw, classSchool, classtravelEST, classDaysOfWeek):
        self.className = className
        self.classInClassTime = classInClassTime
        self.classEstHw = classEstHw
        self.classSchool = classSchool
        self.classtravelEST = classtravelEST
        self.classDaysOfWeek = classDaysOfWeek



def createWhaClass(className, classEstHW, classDaysOfWeek):
    return classObj(className=className, classInClassTime=3, classEstHw=classEstHW, classSchool="WHA", classtravelEST=0, classDaysOfWeek=classDaysOfWeek)

def createBpClass(className, classEstHW):
    return classObj(className=className, classInClassTime = 1, classEstHw=classEstHW, classSchool="BP", classtravelEST=SchoolTravelConversions["BP"], classDaysOfWeek=5)




def addClass():
    className = input("Class Name: ")
    classInClassTime = float(input("Class Estimated in-class Time: "))
    classEstHw = float(input("Class Estimated HW (hr): "))
    classSchool = input("School (WHA - Wilson Hill Academy, BP - Baptist Prep, ST - STEAM Co-op, OT - other): ").upper()
    classTravelEST = float()
    classDaysOfWeek = input("Class Days (please separate each day by a space. Ex: 'Sun Mon Tues'): ").split()

    while classSchool not in schoolList:
        print("Please input a valid school tag.")
        time.sleep(1)
        classSchool = input("School (WHA - Wilson Hill Academy, BP - Baptist Prep, ST - STEAM Co-op, OT - other): ").upper()


    if classSchool == "OT":
        classTravelEST = float(input("Travel to and fro estimation: "))
    else:
        classTravelEST = SchoolTravelConversions[classSchool]


    newClass = (className, classInClassTime, classEstHw, classSchool, classTravelEST)
    classSchedule.append(newClass)


addClass()


print(classSchedule)


def main():
    print("Hello there! Here is your current schedule next year: ")
    print(classSchedule)

