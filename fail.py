# import Tkinter 

#calc grade
# def gpa():
#     UserNum = int(input("please enter your grade using the number system to know your GPA    "))
#     if UserNum >= 93 and UserNum <= 100:
#         return "your GPA is 4.0"
#     elif UserNum >= 90 and UserNum <= 92:
#         return "your GPA is 3.7"
#     elif UserNum >= 87 and UserNum <= 89:
#         return "your GPA is 3.3"
#     elif UserNum >= 83 and UserNum <= 86:
#         return "your GPA is 3.0"
#     elif UserNum >= 80 and UserNum <= 82:
#         return "your GPA is 2.7"
#     elif UserNum >= 77 and UserNum <= 79:
#         return "your GPA is 2.3"
#     elif UserNum >= 73 and UserNum <= 76:
#         return "your GPA is 2.0"
#     elif UserNum >= 70 and UserNum <= 72:
#         return "your GPA is 1.7"
#     elif UserNum >= 67 and UserNum <= 69:
#         return "your GPA is 1.3"
#     elif UserNum >= 65 and UserNum <= 66:
#         return "your GPA is 1.0"
#     elif UserNum <= 65:
#         return "your GPA is 0.0"
#     else:
#         return "something went wrong try again"

# print(gpa())

#preferance 
# def S_L():
#     SL = input("please choose the sciences or the arts  ")

#     if SL == "the sciences" or SL == "sciences":
#         return "go here"
#     elif SL == "the art" or SL == "art":
#         return "go here"
#     else:
#         return "something went wrong try"
    
# print(S_L()) 
    
    #EDIT PLSSSS ^^^^


# options

# fields = [
#     {
#         "chem" : 2.78,
#     },{
#         "math" : 2.90,
#     },{
#         "economics" : 2.95,
#     },{
#         "psychology" : 2.78, 
#     },{
#         "bio" : 3.02,
#     },{
#         "edu" : 3.36,
#     },{
#         "lang" : 3.34,
#     },{
#         "english" : 3.33,
#     },{
#         "music" : 3.30,
#     },{
#         "religion" : 3.22,
#     }
# ]


#output

# import tkinter as tk

# Function to calculate GPA
# def calculate_gpa():
#     UserNum = int(entry_grade.get())
#     gpa_label.config(text=gpa(UserNum))

# GPA Calculator function
# def gpa(UserNum):
#     # Your GPA calculation logic remains the same here
#     UserNum = int(input("please enter your grade using the number system to know your GPA    "))
#     if UserNum >= 93 and UserNum <= 100:
#         return "your GPA is 4.0"
#     elif UserNum >= 90 and UserNum <= 92:
#         return "your GPA is 3.7"
#     elif UserNum >= 87 and UserNum <= 89:
#         return "your GPA is 3.3"
#     elif UserNum >= 83 and UserNum <= 86:
#         return "your GPA is 3.0"
#     elif UserNum >= 80 and UserNum <= 82:
#         return "your GPA is 2.7"
#     elif UserNum >= 77 and UserNum <= 79:
#         return "your GPA is 2.3"
#     elif UserNum >= 73 and UserNum <= 76:
#         return "your GPA is 2.0"
#     elif UserNum >= 70 and UserNum <= 72:
#         return "your GPA is 1.7"
#     elif UserNum >= 67 and UserNum <= 69:
#         return "your GPA is 1.3"
#     elif UserNum >= 65 and UserNum <= 66:
#         return "your GPA is 1.0"
#     elif UserNum <= 65:
#         return "your GPA is 0.0"
#     else:
#         return "something went wrong try again"


# Function to choose between sciences and arts
# def choose_preference():
#     preference = preference_entry.get()
#     if preference.lower() == "sciences":
#         display_fields("sciences")
#     elif preference.lower() == "arts":
#         display_fields("arts")
#     else:
#         fields_label.config(text="Invalid preference. Please enter 'sciences' or 'arts'.")

# Function to display fields/majors
# def display_fields(preference):
#     fields_label.config(text="Fields/Majors available:")
#     for field in fields:
#         for key, value in field.items():
#             if preference in key.lower():
#                 fields_label.config(text=fields_label.cget("text") + f"\n{key} - GPA Requirement: {value}")

# GUI Setup
# root = tk.Tk()
# root.title("GPA Calculator")

# GPA Calculator
# grade_label = tk.Label(root, text="Enter your grade (0-100):")
# entry_grade = tk.Entry(root)
# calculate_button = tk.Button(root, text="Calculate GPA", command=calculate_gpa)
# gpa_label = tk.Label(root, text="Your GPA will be displayed here.")

# grade_label.pack()
# entry_grade.pack()
# calculate_button.pack()
# gpa_label.pack()

# Choose Preference (Sciences or Arts)
# preference_label = tk.Label(root, text="Enter your preference (sciences/arts):")
# preference_entry = tk.Entry(root)
# choose_button = tk.Button(root, text="Choose Preference", command=choose_preference)
# fields_label = tk.Label(root, text="Fields/Majors available:")

# preference_label.pack()
# preference_entry.pack()
# choose_button.pack()
# fields_label.pack()

# root.mainloop()



# import tkinter as tk

# Function to calculate GPA
# def calculate_gpa():
#     UserNum = int(entry_grade.get())
#     gpa_label.config(text=gpa(UserNum))

# GPA Calculator function
# def gpa(UserNum):
    # Your GPA calculation logic remains the same here
    # UserNum = int(input("please enter your grade using the number system to know your GPA    "))
    # if UserNum >= 93 and UserNum <= 100:
    #     return "your GPA is 4.0"
    # elif UserNum >= 90 and UserNum <= 92:
    #     return "your GPA is 3.7"
    # elif UserNum >= 87 and UserNum <= 89:
    #     return "your GPA is 3.3"
    # elif UserNum >= 83 and UserNum <= 86:
    #     return "your GPA is 3.0"
    # elif UserNum >= 80 and UserNum <= 82:
    #     return "your GPA is 2.7"
    # elif UserNum >= 77 and UserNum <= 79:
    #     return "your GPA is 2.3"
    # elif UserNum >= 73 and UserNum <= 76:
    #     return "your GPA is 2.0"
    # elif UserNum >= 70 and UserNum <= 72:
    #     return "your GPA is 1.7"
    # elif UserNum >= 67 and UserNum <= 69:
    #     return "your GPA is 1.3"
    # elif UserNum >= 65 and UserNum <= 66:
    #     return "your GPA is 1.0"
    # elif UserNum <= 65:
    #     return "your GPA is 0.0"
    # else:
    #     return "something went wrong try again"


# Function to choose between sciences and arts
# def choose_preference():
#     preference = preference_entry.get()
#     if preference.lower() == "sciences":
#         display_available_fields("sciences")
#     elif preference.lower() == "arts":
#         display_available_fields("arts")
#     else:
#         fields_label.config(text="Invalid preference. Please enter 'sciences' or 'arts'.")

# Function to display available fields/majors
# def display_available_fields(preference):
#     UserNum = int(entry_grade.get())
#     fields_label.config(text=f"Fields/Majors available for {preference}:")
#     for field in fields:
#         for key, value in field.items():
#             if preference in key.lower() and UserNum >= value:
#                 fields_label.config(text=fields_label.cget("text") + f"\n{key} - GPA Requirement: {value}")

# GUI Setup
# root = tk.Tk()
# root.title("GPA Calculator")

# GPA Calculator
# grade_label = tk.Label(root, text="Enter your grade (0-100):")
# entry_grade = tk.Entry(root)
# calculate_button = tk.Button(root, text="Calculate GPA", command=calculate_gpa)
# gpa_label = tk.Label(root, text="Your GPA will be displayed here.")

# grade_label.pack()
# entry_grade.pack()
# calculate_button.pack()
# gpa_label.pack()

# Choose Preference (Sciences or Arts)
# preference_label = tk.Label(root, text="Enter your preference (sciences/arts):")
# preference_entry = tk.Entry(root)
# choose_button = tk.Button(root, text="Choose Preference", command=choose_preference)
# fields_label = tk.Label(root, text="Fields/Majors available:")

# preference_label.pack()
# preference_entry.pack()
# choose_button.pack()
# fields_label.pack()

# root.mainloop()

