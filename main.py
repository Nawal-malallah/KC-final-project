import Tkinter 

#calc grade
def gpa():
    UserNum = int(input("please enter your grade using the number system to know your GPA    "))
    if UserNum >= 93 and UserNum <= 100:
        return "your GPA is 4.0"
    elif UserNum >= 90 and UserNum <= 92:
        return "your GPA is 3.7"
    elif UserNum >= 87 and UserNum <= 89:
        return "your GPA is 3.3"
    elif UserNum >= 83 and UserNum <= 86:
        return "your GPA is 3.0"
    elif UserNum >= 80 and UserNum <= 82:
        return "your GPA is 2.7"
    elif UserNum >= 77 and UserNum <= 79:
        return "your GPA is 2.3"
    elif UserNum >= 73 and UserNum <= 76:
        return "your GPA is 2.0"
    elif UserNum >= 70 and UserNum <= 72:
        return "your GPA is 1.7"
    elif UserNum >= 67 and UserNum <= 69:
        return "your GPA is 1.3"
    elif UserNum >= 65 and UserNum <= 66:
        return "your GPA is 1.0"
    elif UserNum <= 65:
        return "your GPA is 0.0"
    else:
        return "something went wrong try again"

print(gpa())

#preferance 
def S_L():
    SL = input("please choose the sciences or the arts  ")

    if SL == "the sciences" or SL == "sciences":
        return "go here"
    elif SL == "the art" or SL == "art":
        return "go here"
    else:
        return "something went wrong try"
    
print(S_L()) 
    
    #EDIT PLSSSS ^^^^


# options

fields = [
    {
        "chem" : 2.78,
    },{
        "math" : 2.90,
    },{
        "economics" : 2.95,
    },{
        "psychology" : 2.78, 
    },{
        "bio" : 3.02,
    },{
        "edu" : 3.36,
    },{
        "lang" : 3.34,
    },{
        "english" : 3.33,
    },{
        "music" : 3.30,
    },{
        "religion" : 3.22,
    }
]






#output