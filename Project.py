from ToDo import ToDo
import os
import json


class Project:
    def __init__(self, location) -> None:
        self.location = location
        self.name = ""
        self.description = ""
        self.__readProjectJson()
        self.todo = ToDo(self.location + "\\tasks.json")

    def __readProjectJson(self):
        with open(self.location + "\\proj.json") as json_file:
            data = json.load(json_file)
            self.name = data["Name"]
            self.description = data["Description"]

    def openProject(self):
        os.system("code " + self.location)

    def openTodo(self) -> None:
        self.todo.run()

    def __percentageCompleted(self) -> float:
        return self.todo.percentageCompleted()

    def __str__(self) -> str:
        return "Name: " + self.name + "\nDescription: " + self.description + "\nCompleted: {:.2f}%".format(self.__percentageCompleted())
