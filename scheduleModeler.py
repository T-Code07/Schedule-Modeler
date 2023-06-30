
#Task: Want to create a program that will model what my schedule will 
#      look like next school year. It will show me if my shool schedules 
#      are actually viable. Gonna hopefully get it to show how much time 
#      I will have per day for hw. I want it to break down my week.

from enum import Enum, unique
import time

#To-do: figure out how to import the scheduleModelerLibrary
import sched



#School tags: WHA - Wilson Hill Academy, BP - Baptist Prep, ST - STEAM Co-op, OT - other

#There are 84 working hours in a 7 day week with 12 working hours a day.
timeInWeek = 84.0
timeInDay = 12.0

schoolList = ["WHA", "BP", "ST", "OT"]


#ML tie-in:  it might be kind of cool to create a ML algorthmn to predict if your scheudle 
#            would be too intense. That would be awesome! Don't think that would be all that 
#            hard either. We'll see though


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




def createWhaClass(className, classEstHW, classDaysOfWeek):
    return Class(className, 3, classEstHW, "WHA", 0, classDaysOfWeek)

def createBpClass(className, classEstHW):
    return Class(className, 1, classEstHW)



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


#addClass()




def main():
    print("Hello there! Here is your current schedule next year: ")
    print(classSchedule)

main()