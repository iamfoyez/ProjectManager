from Project import Project
import os


class ProjectManager:

    def __init__(self, root) -> None:
        self.root = root
        self.projects = []
        self.__listProjects()
        self.run()

    def __listProjects(self):
        for x in os.listdir(self.root):
            if os.path.isfile(self.root + x + "\\proj.json"):
                self.projects.append(Project(self.root + x))

    def printProjects(self):
        i = 0
        for x in self.projects:
            print("ID: " + str(i))
            print(str(x) + "\n")
            i += 1

    def run(self):
        while True:
            self.printProjects()
            cmd = input("Enter the command: ").strip().lower()
            if len(cmd.split()) == 2 and cmd.split()[1].isdigit():
                n = int(cmd.split()[1])
                if cmd.split()[0] == "t" and n >= 0 and n < len(self.projects):
                    self.projects[n].openTodo()
                elif cmd.split()[0] == "o" and n >= 0 and n < len(self.projects):
                    self.projects[n].openProject()
            elif cmd.strip().lower() == "exit":
                break


pm = ProjectManager("D:\\Projects\\")
