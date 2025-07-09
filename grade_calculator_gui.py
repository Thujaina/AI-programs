import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        name = entry_name.get()
        marks = list(map(float, entry_marks.get().split()))
        total = sum(marks)
        avg = total / len(marks)

        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 40:
            grade = "D"
        else:
            grade = "Fail"

        result = f"Name: {name}\nTotal: {total}\nAverage: {avg:.2f}\nGrade: {grade}"
        messagebox.showinfo("Result", result)
    except Exception as e:
        messagebox.showerror("Error", "Enter valid name and marks (space separated)")

# GUI window
root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("400x250")

tk.Label(root, text="Student Name:").pack(pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.pack()

tk.Label(root, text="Enter Marks (space separated):").pack(pady=5)
entry_marks = tk.Entry(root, width=30)
entry_marks.pack()

tk.Button(root, text="Calculate Grade", command=calculate).pack(pady=20)

root.mainloop()
