import tkinter as tk






















def IDS():
    pass





























def DFS():
    pass












def BFS():
    pass










walls = []
buttons = []

def showSolveAlgorithms():
    root = tk.Tk()

    button1 = tk.Button(root, text="BFS", name="bfs", command=BFS())
    button1.grid(row=2, column=1, sticky="nsew")

    button2 = tk.Button(root, text="DFS", name="dfs", command=DFS())
    button2.grid(row=2, column=3, sticky="nsew")
    
    button3 = tk.Button(root, text="IDS", name="ids", command=IDS())
    button3.grid(row=3, column=2, sticky="nsew")

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(1, weight=1)

    root.title("select Algorithm")

    root.geometry("200x200")

    root.resizable(0, 0)

    root.mainloop()

def setHereWall(row, col):
    widgetName = "{}, {}".format(row, col)
    if [row, col] not in walls:
        walls.append([row, col])
        for i in buttons:
            if i['title'] == widgetName:
                i['button']['bg'] = 'black'
    else:
        walls.remove([row, col])
        for i in buttons:
            if i['title'] == widgetName:
                i['button']['bg'] = 'white'

    print(walls)


def createArea(size):
    root = tk.Tk()
    for row in range(0, size):
        for col in range(0, size):
            buttonText = str()
            buttonText = "{}, {}".format(row, col)
            button = tk.Button(root, text=buttonText, name=buttonText, fg='black', 
                               command=lambda row=row, col=col: setHereWall(row, col))
            button.grid(row=row, column=col, sticky="nsew")
            buttons.append({"button": button, "title": buttonText})

    nextStepButton = tk.Button(root, text = "Solve!", name="solvation", command=lambda row=size+2, col=0: showSolveAlgorithms())
    nextStepButton.grid(row=size+2, column=0, sticky="nsew")

    root.grid_rowconfigure(size, weight=2)
    root.grid_columnconfigure(size, weight=2)

    root.resizable(False, False)

    root.title("Set Walls Position")

    root.mainloop()

def setSize():

    size = input("enter size of maze: (non number for default size)")

    try:
        createArea(int(size))
    except:
        createArea(10)



if __name__ == "__main__":
    setSize()