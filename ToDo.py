import os.path
import json


class ToDo:

    def __init__(self, listFile) -> None:
        self.tasks = []
        self.file = listFile
        self.fillList()

    def fillList(self) -> None:
        if os.path.isfile(self.file):
            # read file
            with open(self.file) as json_file:
                self.tasks = json.load(json_file)
        else:
            # make file
            self.__saveList()

    def __saveList(self) -> None:
        json_object = json.dumps(self.tasks, indent=4)
        tasksFile = open(self.file, "w")
        tasksFile.write(json_object)
        tasksFile.close()

    def printList(self) -> None:
        i = 0
        for item in self.tasks:
            if item["completed"]:
                print(str(i) + " - [x] " + item["task"])
            else:
                print(str(i) + " - [] " + item["task"])
            i += 1

    def percentageCompleted(self) -> float:
        total = len(self.tasks)
        if total is 0:
            return 0
        completed = 0
        for task in self.tasks:
            if task["completed"]:
                completed += 1
        return (completed / total) * 100

    def __isDeleteCommand(self, cmd) -> bool:
        if len(cmd.split()) != 2:
            return False
        if cmd.split()[0] == "-" and cmd.split()[1].isdigit():
            return True
        return False

    def __delete(self, id) -> None:
        if id < len(self.tasks) and id >= 0:
            del self.tasks[id]
            print(str(id) + " was removed!")
            self.__saveList()

    def __add(self, task) -> None:
        self.tasks.append({"task": task, "completed": False})
        self.__saveList()

    def __toggleCompleted(self, id) -> None:
        if id < len(self.tasks) and id >= 0:
            self.tasks[id]["completed"] = not self.tasks[id]["completed"]
            self.__saveList()

    def run(self) -> None:
        while True:
            self.printList()
            userInput = input(": ").strip()
            # check for exit command
            if userInput == "exit":
                break
            # check for delete command
            elif self.__isDeleteCommand(userInput):
                delIndex = int(userInput.split()[1])
                self.__delete(delIndex)
            # mark completed
            elif userInput.isdigit():
                self.__toggleCompleted(int(userInput))
            # add to list
            elif userInput:
                self.__add(userInput)
