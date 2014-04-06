from Tkinter import *
import spiderlink
# Not using 
class App:

    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.pack()
        self.master = master
        self.foods = spiderlink.Nutrition()

        #self.text = Text (master)
        #calories = spiderlink.find_calories()
        #print(type(calories))

       # self.text.insert(INSERT, calories)
        #self.text.insert(END, "done...")
        #self.text.pack(side=LEFT)

        self.button = Button(
            self.frame, text="QUIT", fg="red", command=self.frame.quit
            )
        self.button.pack(side=LEFT)
        foods = self.foods.get_food()
        for food in foods:
            self.add_food(food)
    def add_food(self, food):
        theFood = Text(self.master)
        foodString = food
        theFood.insert(INSERT, foodString)
        theFood.insert(END, self.foods.get_calorie_from_food(foodString))
        theFood.pack(side=LEFT)
        button = Button(self.frame, text="+", fg="green")
        button.pack()



root = Tk()

app = App(root)

root.mainloop()