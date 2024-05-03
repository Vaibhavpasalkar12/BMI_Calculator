from tkinter import *

def calculate_bmi():
    previous_result = result_display.get('1.0', END)
    if previous_result != '':
        result_display.delete('1.0', END)
    weight_value = float(weight_entry.get())
    height_value = float(height_entry.get())
    bmi = (weight_value / (height_value * height_value))
    new_weight = (height_value * height_value) * 20
    if 0 <= bmi <= 18:
        weight_change = new_weight - weight_value
        category = 'Underweight'
        lose_or_gain = "gain"
        result_display.insert(END, "Your BMI is %s: \n%s\n" % (round(bmi, 2), category))
        result_display.insert(END, "You need to %s weight.\nThe amount of weight you need to %s is %skg." % (lose_or_gain, lose_or_gain, weight_change))
    elif 19 <= bmi <= 24:
        category = str("Your BMI is ") + str(round(bmi, 2)) + str("\nThis is a healthy weight for your height.")
        result_display.insert(END, category)
    elif 25 <= bmi <= 30:
        weight_change = weight_value - new_weight
        lose_or_gain = "lose"
        category = 'Overweight.'
        result_display.insert(END, "Your BMI is %s: \n%s\n" % (round(bmi, 2), category))
        result_display.insert(END, "You need to %s weight.\nThe amount of weight you need to %s is %skg." % (lose_or_gain, lose_or_gain, weight_change))
    elif 30 <= bmi <= 35:
        weight_change = weight_value - new_weight
        lose_or_gain = "lose"
        category = 'Obese Class I (Moderately obese)'
        result_display.insert(END, "Your BMI is %s: \n%s\n" % (round(bmi, 2), category))
        result_display.insert(END, "You need to %s weight.\nThe amount of weight you need to %s is %skg." % (lose_or_gain, lose_or_gain, weight_change))
    elif 35 <= bmi <= 1000:
        weight_change = weight_value - new_weight
        lose_or_gain = "lose"
        category = 'Obese Class II (Severely obese)'
        result_display.insert(END, "Your BMI is %s: \n%s\n" % (round(bmi, 2), category))
        result_display.insert(END, "You need to %s weight.\nThe amount of weight you need to %s is %skg." % (lose_or_gain, lose_or_gain, weight_change))

window = Tk()
window.title("BMI Calculator")
height_label = Label(window, text="Enter your height in meters")
height_label.grid(row=0, column=0)
height_value = StringVar()
height_entry = Entry(window, textvariable=height_value)
height_entry.grid(row=1, column=0)

weight_label = Label(window, text="Enter your weight in kg")
weight_label.grid(row=2, column=0)
weight_value = StringVar()
weight_entry = Entry(window, textvariable=weight_value)
weight_entry.grid(row=3, column=0)

result_display = Text(window, height=10, width=45)
result_display.grid(row=0, column=1, rowspan=4)

calculate_button = Button(window, text="Calculate", height=3, width=30, command=calculate_bmi)
calculate_button.grid(row=4, column=0, columnspan=2)

window.mainloop()
