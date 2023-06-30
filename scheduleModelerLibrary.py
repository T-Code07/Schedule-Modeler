#Task: Want to create a program that will model what my schedule will 
#      look like next school year. It will show me if my shool schedules 
#      are actually viable. Gonna hopefully get it to show how much time 
#      I will have per day for hw. I want it to break down my week.

#      While that is the ultimate goal of this project (ie: this folder), 
#      this specific file is library that my personal model will be created from.
#      This is supposed to be more universal. I haven't really ever created a useful python library before.
#      Here is my opportunity. 


from enum import Enum, unique
import numpy as np

#ML tie-in:  it might be kind of cool to create a ML algorthmn to predict if your scheudle 
#            would be too intense. That would be awesome! Don't think that would be all that 
#            hard either. We'll see though

@unique
class ActivityType(Enum):
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

#To-do:
#   1) why cant access these variables throughout script?
#   2) implement these functions
#   3) how to create a gui interface for this? This would be much more user friendly with a gui.
class ScheduleManager:
    _workHoursPerDay = 12.0
    _workDays = 6
    _activityList = list()
    _classSchedule = list()
    _timeInWeek = _workDays * _workHoursPerDay

    _scheduleVector = np.array((_workDays, 1))

    
    def createScheduleVector():

        #Think I should create numpy array like:
        #(Works days, work hours):
        #[12, 12, 12, 12, 12, 12, 12]

        #This will allow me to keep track of the hours per day and subtract the hours of activity between them.
        #Numpy's great for math stuff afterall.

        #Also, starting off in a numpy array might be nice for future ML capabilities. Maybe pre-processing won't take as long?

        pass

    def addActivity(activityName, activityType, hoursPerSession, frequency, daysOfOccurance, travelTime):
        pass

    def addClass(className, classInClassTime, classEstHw, classSchool, classtravelEST, classDaysOfWeek):
        pass



class Activity:
    _activityName = str()
    _activityType = None
    _hoursPerSessions = float()
    _frequency = float()
    _daysOfOccurances = list()
    _travelTimeEST = float()

    def __init__(self, name, typeA, hoursPerSession, frequency, daysOfOccurance, travelTime):
        self._activityName = name
        self._activityType = typeA
        self._hoursPerSessions = hoursPerSession
        self._frequency = frequency
        self._daysOfOccurances = daysOfOccurance
        self._travelTimeEST = travelTime


class Sport (Activity):
    pass

class Class(Activity):
    
    s_classEstHw = float()
    s_classSchool = str()


    def __init__(self, className, classInClassTime, classEstHw, classSchool, classtravelEST, classDaysOfWeek):

        #initialize normal activity obj:
        self._activityName = className
        self._hoursPerSessions = classInClassTime
        self._frequency = len(classDaysOfWeek)
        self._daysOfOccurances = classDaysOfWeek
        self._travelTimeEST = classtravelEST

        #initialize "class"-specific obj:
        self._activityType = ActivityType.CLASS
        self.s_classSchool = classSchool
        self.s_classEstHw = classEstHw







