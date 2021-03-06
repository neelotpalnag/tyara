"""
Interpreter Codes 
-1: No Relevant Command
0 :
1 : Gmail Data
2 : Weather Current Temperature
3 : Weather Full Data
4 : Book a Cab from Home to Work
5 : Book a Cab from Work to Home
6 : Set an Alarm
7 : Classes Today
8 : Date
9 : Time
10: Lock Down the Speech Recognition
11: Unlock the Speech Recognition
12: Send Emergency Signal

"""
""" This function *Interpret_Text(foo)* accepts the command received from Google Cloud Speech """
def Interpret_Text(command):
    code = -1
    command = command.lower()
    #print(command)
    if ((command.find("gmail") != -1)|(command.find("mails")!=-1)|(command.find("mail")!=-1)|(command.find("mail")!=-1)):
        code = 1
    if (command.find("weather")!=-1):
        if ((command.find("now") != -1) | (command.find("outside")) != -1):
            code = 2
        elif ((command.find("report")) != -1 | (command.find("forecast")) != -1):
            code = 3
        else: code=3
    if (command.find("taxi") != -1) | (command.find("uber")) != -1 | (command.find("ride")) != -1:
        code = 4
        '''if (command.find("home")!=-1&command.find("work")!=-1):
            code = 4
        elif (command.find("work to home") != -1):
            code = 5
        else:
            code = 0'''
    if (command.find("alarm") != -1):
        code = 6
    if (command.find("class") != -1 & command.find("today") != -1):
        code = 7
    if (command.find("date") != -1):
        code = 8
    if (command.find("time") != -1):
        code = 9
    if (command.find("unlock") != -1 & command.find("speech") != -1):
        code = 11
    if(command.find("nothing")!=-1|command.find("bye")!=-1|command.find("close")):
        code = 12
    print(code)
    return code