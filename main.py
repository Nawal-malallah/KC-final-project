import tkinter as tk

def calculate_gpa():
    grades = entry_grades.get().split(",")
    grades = [float(grade.strip()) for grade in grades]

    if GPA_type.get() == "Weighted":
        weights = [float(weight.strip()) for weight in entry_weights.get().split(",")]
        total_weighted_points = sum(grades[i] * weights[i] for i in range(len(grades)))
        total_weight = sum(weights)
        gpa = total_weighted_points / total_weight
    else:
        total_unweighted_points = sum(grades)
        gpa = total_unweighted_points / len(grades)
    
    result_label.config(text=f"Your {GPA_type.get()} GPA is: {gpa:.2f}")

root = tk.Tk()
root.title("GPA Calculator")

GPA_type = tk.StringVar()
GPA_type.set("Weighted")

label_type = tk.Label(root, text="Choose GPA Type:")
radio_weighted = tk.Radiobutton(root, text="Weighted", variable=GPA_type, value="Weighted")
radio_unweighted = tk.Radiobutton(root, text="Unweighted", variable=GPA_type, value="Unweighted")

label_grades = tk.Label(root, text="Enter your grades (comma-separated):")
entry_grades = tk.Entry(root)

label_weights = tk.Label(root, text="Enter weights (comma-separated, for Weighted GPA):")
entry_weights = tk.Entry(root)

calculate_button = tk.Button(root, text="Calculate GPA", command=calculate_gpa)

result_label = tk.Label(root, text="Your GPA will be displayed here.")

label_type.pack()
radio_weighted.pack()
radio_unweighted.pack()
label_grades.pack()
entry_grades.pack()
label_weights.pack()
entry_weights.pack()
calculate_button.pack()
result_label.pack()

root.mainloop()

