import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os

# Remove old data
try:
    os.remove("quiz_database.db")
except:
    pass

# Use SQL for the database storage even though we're using Python lol
import sqlite3

# Create database with the five separate tables

class QuizDatabase:
  def __init__(self, db_name="quiz_database.db"):
    self.conn = sqlite3.connect(db_name)
    self.cursor = self.conn.cursor()
    self._create_tables()

  def _create_tables(self):
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS Metals (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT
      )
    """)
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS Fallacies (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT
      )
    """)
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS Sports (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT
      )
    """)
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS Films (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT
      )
    """)
    self.cursor.execute("""
      CREATE TABLE IF NOT EXISTS Celebrities (
        id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT
      )
    """)
    self.conn.commit()


  def add_question(self, table_name, question, answer):
    self.cursor.execute(f"INSERT INTO {table_name} (question, answer) VALUES (?, ?)", (question, answer))
    self.conn.commit()

  def get_questions(self, table_name):
    self.cursor.execute(f"SELECT id, question FROM {table_name}")
    return self.cursor.fetchall()

  def check_answer(self, table_name, question_id, user_answer):
    self.cursor.execute(f"SELECT answer FROM {table_name} WHERE id=?", (question_id,))
    correct_answer = self.cursor.fetchone()
    if correct_answer:
      return user_answer.lower() == correct_answer[0].lower()
    return False

  def close(self):
    self.conn.close()

conn = sqlite3.connect('C:\Guh\quiz_database.db')
cursor = conn.cursor()



class QuizAppMetals:
  def __init__(self, db):
    self.db = db
    self.current_question_id = None
    self.current_table = "Metals"
    self.questions = self.db.get_questions(self.current_table)
    self.question_index = 0

    self.root = tk.Tk()
    self.root.title("Quiz Application")

    self.question_label = tk.Label(self.root, text="")
    self.question_label.pack(pady=10)

    self.answer_entry = tk.Entry(self.root)
    self.answer_entry.pack(pady=10)

    self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
    self.submit_button.pack(pady=10)

    self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
    self.next_button.pack(pady=10)

    self.show_question()

  def show_question(self):
    if self.question_index < len(self.questions):
      self.current_question_id, question_text = self.questions[self.question_index]
      self.question_label.config(text=question_text)
      self.answer_entry.delete(0, tk.END)
    else:
      messagebox.showinfo("Quiz Completed", "You have answered all the questions!")
      self.root.destroy()

  def check_answer(self):
    user_answer = self.answer_entry.get()
    if self.db.check_answer(self.current_table, self.current_question_id, user_answer):
      messagebox.showinfo("Correct", "Your answer is correct!")
    else:
      messagebox.showinfo("Incorrect", )

  def next_question(self):
    self.question_index += 1
    self.show_question()

  def run(self):
    self.root.mainloop()

class QuizAppFallacies:
  def __init__(self, db):
    self.db = db
    self.current_question_id = None
    self.current_table = "Fallacies"
    self.questions = self.db.get_questions(self.current_table)
    self.question_index = 0

    self.root = tk.Tk()
    self.root.title("Quiz Application")

    self.question_label = tk.Label(self.root, text="")
    self.question_label.pack(pady=10)

    self.answer_entry = tk.Entry(self.root)
    self.answer_entry.pack(pady=10)

    self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
    self.submit_button.pack(pady=10)

    self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
    self.next_button.pack(pady=10)

    self.show_question()

  def show_question(self):
    if self.question_index < len(self.questions):
      self.current_question_id, question_text = self.questions[self.question_index]
      self.question_label.config(text=question_text)
      self.answer_entry.delete(0, tk.END)
    else:
      messagebox.showinfo("Quiz Completed", "You have answered all the questions!")
      self.root.destroy()

  def check_answer(self):
    user_answer = self.answer_entry.get()
    if self.db.check_answer(self.current_table, self.current_question_id, user_answer):
      messagebox.showinfo("Correct", "Your answer is correct!")
    else:
      messagebox.showinfo("Incorrect", )

  def next_question(self):
    self.question_index += 1
    self.show_question()

  def run(self):
    self.root.mainloop()

class QuizAppSports:
  def __init__(self, db):
    self.db = db
    self.current_question_id = None
    self.current_table = "Sports"
    self.questions = self.db.get_questions(self.current_table)
    self.question_index = 0

    self.root = tk.Tk()
    self.root.title("Quiz Application")

    self.question_label = tk.Label(self.root, text="")
    self.question_label.pack(pady=10)

    self.answer_entry = tk.Entry(self.root)
    self.answer_entry.pack(pady=10)

    self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
    self.submit_button.pack(pady=10)

    self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
    self.next_button.pack(pady=10)

    self.show_question()

  def show_question(self):
    if self.question_index < len(self.questions):
      self.current_question_id, question_text = self.questions[self.question_index]
      self.question_label.config(text=question_text)
      self.answer_entry.delete(0, tk.END)
    else:
      messagebox.showinfo("Quiz Completed", "You have answered all the questions!")
      self.root.destroy()

  def check_answer(self):
    user_answer = self.answer_entry.get()
    if self.db.check_answer(self.current_table, self.current_question_id, user_answer):
      messagebox.showinfo("Correct", "Your answer is correct!")
    else:
      messagebox.showinfo("Incorrect", )

  def next_question(self):
    self.question_index += 1
    self.show_question()

  def run(self):
    self.root.mainloop()

class QuizAppFilms:
  def __init__(self, db):
    self.db = db
    self.current_question_id = None
    self.current_table = "Films"
    self.questions = self.db.get_questions(self.current_table)
    self.question_index = 0

    self.root = tk.Tk()
    self.root.title("Quiz Application")

    self.question_label = tk.Label(self.root, text="")
    self.question_label.pack(pady=10)

    self.answer_entry = tk.Entry(self.root)
    self.answer_entry.pack(pady=10)

    self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
    self.submit_button.pack(pady=10)

    self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
    self.next_button.pack(pady=10)

    self.show_question()

  def show_question(self):
    if self.question_index < len(self.questions):
      self.current_question_id, question_text = self.questions[self.question_index]
      self.question_label.config(text=question_text)
      self.answer_entry.delete(0, tk.END)
    else:
      messagebox.showinfo("Quiz Completed", "You have answered all the questions!")
      self.root.destroy()

  def check_answer(self):
    user_answer = self.answer_entry.get()
    if self.db.check_answer(self.current_table, self.current_question_id, user_answer):
      messagebox.showinfo("Correct", "Your answer is correct!")
    else:
      messagebox.showinfo("Incorrect", )

  def next_question(self):
    self.question_index += 1
    self.show_question()

  def run(self):
    self.root.mainloop()

class QuizAppCelebrities:
  def __init__(self, db):
    self.db = db
    self.current_question_id = None
    self.current_table = "Celebrities"
    self.questions = self.db.get_questions(self.current_table)
    self.question_index = 0

    self.root = tk.Tk()
    self.root.title("Quiz Application")

    self.question_label = tk.Label(self.root, text="")
    self.question_label.pack(pady=10)

    self.answer_entry = tk.Entry(self.root)
    self.answer_entry.pack(pady=10)

    self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
    self.submit_button.pack(pady=10)

    self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
    self.next_button.pack(pady=10)

    self.show_question()

  def show_question(self):
    if self.question_index < len(self.questions):
      self.current_question_id, question_text = self.questions[self.question_index]
      self.question_label.config(text=question_text)
      self.answer_entry.delete(0, tk.END)
    else:
      messagebox.showinfo("Quiz Completed", "You have answered all the questions!")
      self.root.destroy()

  def check_answer(self):
    user_answer = self.answer_entry.get()
    if self.db.check_answer(self.current_table, self.current_question_id, user_answer):
      messagebox.showinfo("Correct", "Your answer is correct!")
    else:
      messagebox.showinfo("Incorrect", )

  def next_question(self):
    self.question_index += 1
    self.show_question()

  def run(self):
    self.root.mainloop()

if __name__ == "__main__":
  db = QuizDatabase()

  # Place to add, alter, or delete questions
  db.add_question("Metals", "What is the metal with the highest melting point?", "Tungsten")
  db.add_question("Metals", "How many elements of the periodic table are metals?", "98")
  db.add_question("Metals", "What is the most commonly used metal in dental implants?", "Titanium")
  db.add_question("Metals", "What is the only metal that is liquid at room temp?", "Mercury")
  db.add_question("Metals", "Which common metal was considered pricier than gold in the 1700's?", "Aluminum")
  db.add_question("Metals", "All metals appear metallic (True/False)", "False")
  db.add_question("Metals", "What is the most abundant metal on Earth?", "Iron")
  db.add_question("Metals", "What is the best metallic conductor of electricity?", "Silver")
  db.add_question("Metals", "What is the lightest metal?", "Lithium")
  db.add_question("Metals", "What is the heaviest metal?", "Osmium")
  db.add_question("Fallacies", "Katherine is a bad choice for mayor because she didn’t grow up in this town. ", "Ad hominem")
  db.add_question("Fallacies", "Erin thinks we need to stop using all plastics, right now, to save the planet from climate change.", "Straw man")
  db.add_question("Fallacies", "Losing a tooth can be scary, but have you heard about the Tooth Fairy? ", "Red herring")
  db.add_question("Fallacies", "Must be fairies in the attic because no one's proven otherwise", "Appeal to ignorance")
  db.add_question("Fallacies", "Both times I've had pizza, I've felt bad. Must be allergic.", "Hasty generalization")
  db.add_question("Fallacies", "I’m not enjoying this book, but I bought it, so I have to finish reading it", "Sunk cost")
  db.add_question("Fallacies", "You don’t have enough experience to be the new leader.” “Neither do you!”", "Appeal to hypocrisy")
  db.add_question("Fallacies", "If you don’t support my decision, you were never really my friend.", "False dilemma")
  db.add_question("Fallacies", "You need to stop drinking coffee to be healthy. I read it on a fitness blog. ", "Appeal to authority")
  db.add_question("Fallacies", "While I have a clear plan for the campus budget, my opponent simply wants to throw money at special interest projects", "Equivocation")
  db.add_question("Sports", "What color were the original Wimbledon tennis balls?", "White")
  db.add_question("Sports", "When did the longest tennis match take place?", "2010")
  db.add_question("Sports", "What God was the original Olympics made to worship?", "Zeus")
  db.add_question("Sports", "How many women were competing in the 1920 Olympics?", "65")
  db.add_question("Sports", "What was the sport banned in England in 1457?", "Golf")
  db.add_question("Sports", "What was the original name of Badminton?", "Poona")
  db.add_question("Sports", "What substance are MLB baseballs wiped down in?", "Mud")
  db.add_question("Sports", "Who is the silhouette on the NBA logo?", "Jerry West")
  db.add_question("Sports", "Who holds the record for the most non-stop push-ups?", "Minoru Yoshida")
  db.add_question("Sports", "How many dimples does the average golf ball have?", "336")
  db.add_question("Films", "What is the name of the fictional island where Jurassic Park takes place?", "Isla Nubar")
  db.add_question("Films", "Who was the Millenium Falcon's pilot in Star Wars?", "Han Solo")
  db.add_question("Films", "What is the name of the shark from Jaws?", "Bruce")
  db.add_question("Films", "Who played Jack Dawson in Titanic?", "Leonardo DiCaprio")
  db.add_question("Films", "What is the name of the ring from Lord of the Rings?", "The One Ring")
  db.add_question("Films", "Who is the character played by Al Pacino in The Godfather?", "Michael Corleone")
  db.add_question("Films", "What is the Terminator's famous catchphrase?", "I'll be back")
  db.add_question("Films", "Who played Dorothy in the Wizard of Oz?", "Judy Garland")
  db.add_question("Films", "What is the name of the famous, nonexistent Martin Scorcese film?", "Goncharov")
  db.add_question("Films", "Which iconic line is spoken by Humphrey Bogart in Casablanca?", "Here's looking at you, kid.")
  db.add_question("Celebrities", "Who was Eminem's AA sponsor?", "Elton John")
  db.add_question("Celebrities", "Who was Al Gore's roommate in college?", "Tommy Lee Jones")
  db.add_question("Celebrities", "What sport did Pedro Pascal compete in before becoming an actor?", "Swimming")
  db.add_question("Celebrities", "What job did Michelle Pfeiffer almost pursue?", "Court stenographer")
  db.add_question("Celebrities", "What odd surgery did the Rock recieve?", "Breast reduction")
  db.add_question("Celebrities", "Who convinced Nichelle Nicol to not quit Star Trek?", "MLK")
  db.add_question("Celebrities", "What did Christopher Walken used to do as a job?", "Train lions")
  db.add_question("Celebrities", "What passion does Margot Robbie have in her free time?", "Giving tattoos")
  db.add_question("Celebrities", "Do the actors from Spider Man have spiders named after them (True/False)?", "True")
  db.add_question("Celebrities", "Who is the only band in history to perform in Antarctica?", "Metallica")


top = tk.Tk()
top.title("Quiz Selection")
top.geometry("200x200")

frame = Frame(top)
frame.pack()

def on_button_click():
    selected_option = radio_var.get()
    print("Selected option:", selected_option)
    if(selected_option == "Metals"):
       app1 = QuizAppMetals(db)
       app1.run()
    elif(selected_option == "Fallacies"):
       app2 = QuizAppFallacies(db)
       app2.run()
    elif(selected_option == "Sports"):
       app3 = QuizAppSports(db)
       app3.run()
    elif(selected_option == "Films"):
       app4 = QuizAppFilms(db)
       app4.run()
    elif(selected_option == "Celebrities"):
       app5 = QuizAppCelebrities(db)
       app5.run()
    else:
       print("Dunno how this happened lol")

radio_var = tk.StringVar(value="Metals")

radio_button1 = tk.Radiobutton(top, text="Metals", variable=radio_var, value="Metals")
radio_button1.pack()

radio_button2 = tk.Radiobutton(top, text="Fallacies", variable=radio_var, value="Fallacies")
radio_button2.pack()

radio_button3 = tk.Radiobutton(top, text="Sports", variable=radio_var, value="Sports")
radio_button3.pack()

radio_button4 = tk.Radiobutton(top, text="Films", variable=radio_var, value="Films")
radio_button4.pack()

radio_button5 = tk.Radiobutton(top, text="Celebrities", variable=radio_var, value="Celebrities")
radio_button5.pack()

button = tk.Button(top, text="Submit", command=on_button_click)
button.pack()

top.mainloop()
db.close()