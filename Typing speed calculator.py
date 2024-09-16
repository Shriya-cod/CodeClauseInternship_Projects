import time
import difflib
from tkinter import *


window = Tk()
window.geometry("800x2500")
window.title("TYPING SPEED CALCULATOR")

sample_text = "Typing is an act that demands consistency to ensure a perfect typing speed"

def start_test():
    global start_time
    user_input.delete(0, END)
    result_label.config(text="")
    start_time = time.time()


def end_test():
    global start_time
    end_time = time.time()
    time_taken = end_time - start_time
    time_taken_min = time_taken / 60

    user_text = user_input.get()

    if not user_text.strip():
        result_label.config(text="No input detected.")
        return


    words = len(user_text.split())
    wpm = words/time_taken_min if time_taken_min > 0 else 0
    errors = sum(1 for i, c in enumerate(user_text) if i<len(sample_text) and c!=sample_text)
    accuracy = ((len(user_text) - errors)/len(user_text)) * 100 if len(user_text)>0 else 0

    display_results(time_taken, words, wpm, errors, accuracy)
    highlight_errors(user_text, sample_text)

def display_results(time_taken, words, wpm, errors, accuracy):
    print("RESULTS:")
    print(f"Time taken:{round(time_taken), 2}seconds")
    print(f"Words typed:{words}")
    print(f"Typing speed:{round(wpm, 2)}WPM")
    print(f"Errors made:{errors}")
    print(f"Accuracy:{round(accuracy), 2}%")


def highlight_errors(user_text, sample_text):
    result_label.config(text=result_label.cget("text") + "\n\nText Comparison (Errors Highlighted):\n")
    matcher = difflib.SequenceMatcher(None, sample_text, user_text)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'replace':
            result_label.config(text=result_label.cget("text") + f"Incorrect: {user_text[j1:j2]}\n")
        elif tag == 'delete':
            result_label.config(text=result_label.cget("text") + f"Missing: {sample_text[i1:i2]}\n")
        elif tag == 'insert':
            result_label.config(text=result_label.cget("text") + f"Extra: {user_text[j1:j2]}\n")

instruction_label = Label(window, text="Type the following text and press 'End Test' when done:")
instruction_label.pack(pady=10)

sample_text_label = Label(window, text=sample_text, wraplength=500, justify="left")
sample_text_label.pack(pady=30)

user_input = Entry(window, width=100)
user_input.pack(pady=10)

start_button = Button(window, text="START TEST", command=start_test)
start_button.pack(pady=5)

end_button = Button(window, text="END TEST", command=end_test)
end_button.pack(pady=5)

result_label = Label(window, text="", wraplength=500, justify="left")
result_label.pack(pady=30)

# Start the tkinter event loop
window.mainloop()

