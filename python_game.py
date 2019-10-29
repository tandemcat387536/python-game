"""
Autor : Matej Kovár

"""
from random import randint


class Employee:
    def __init__(self, name, born_year, skills):
        self.name = name
        self.born_year = int(born_year)
        self.skills = skills
        self.boss = None
        self.id = int(born_year) + randint(1, 1000)

    def __str__(self):
        print_skills = ""
        comma = False
        for skill in self.skills:
            if comma:
                print_skills += ", " + skill
            else:
                print_skills += skill
            comma = True
        return "Name: {}, Age: {}, Skills: {}".format(self.name, 2018 - self.born_year, print_skills)


class Firm:
    def __init__(self):
        self.employees = []
        self.teams = []

    def print_employees(self, name, s=0):
        self.sort_employees()
        employee = self.which_employee(name)
        if employee is not None:
            print("\t" * s + employee.name, "<" + str(employee.born_year) + ">")
            s += 2
            for emp in self.employees:
                if emp.boss == employee:
                    self.print_employees(emp.name, s)
        else:
            print("Sorry, but we do not know anything about this employee")

    def which_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp

    def sort_employees(self):
        self.employees = sorted(self.employees, key=lambda employee: employee.name)

    def same_leader(self, emp1, emp2):
        return_value = ""
        first_one1 = emp1
        second_one2 = emp2
        emp1 = self.which_employee(emp1)
        emp2 = self.which_employee(emp2)
        if emp1 is not None and emp2 is not None:
            if emp1.boss == emp2.boss:
                return True
            else:
                return False
        else:
            if emp1 is None:
                return_value += "Sorry but we do not know anything about " + str(first_one1) + "\n"
            if emp2 is None:
                return_value += "Sorry but we do not know anything about " + str(second_one2) + "\n"
            return return_value

    def number_of_employees(self, name, counted=False):
        total = 0
        if counted is not True:
            total += 1
        employee = self.which_employee(name)
        if employee is not None:
            for emp in self.employees:
                if emp.boss == employee:
                    total += 1 + self.number_of_employees(emp.name, True)
            return total
        else:
            return "Sorry but we do not know anything about this employee"

    def search_the_oldest_employee(self):
        oldest = 0
        oldest_employee = None
        for employee in self.employees:
            if 2018 - employee.born_year > oldest:
                oldest = 2018 - employee.born_year
                oldest_employee = employee
        return "The oldest member of this firm is " + oldest_employee.name

    def which_team(self, team_name):
        for team in self.teams:
            if team.name == team_name:
                return team

    def team_average_age(self, team_name):
        team = self.which_team(team_name)
        total = 0
        if team is not None:
            for member in team.members:
                total += 2018 - member.born_year
            return "Average age of members of this firm is " + str(total / len(team.members))
        else:
            return "Sorry, but this team does not exist"

    def print_sorted_teams_and_person(self):
        for team in self.teams:
            print(team.name)
            team.members = sorted(team.members, key=lambda m: 2018 - m.born_year, reverse=True)
            for member in team.members:
                print("\t" * 2 + str(member))

    def is_skill_in_team(self, team_name, skill_name):
        team = self.which_team(team_name)
        if team is not None:
            for member in team.members:
                for skill in member.skills:
                    if skill == skill_name:
                        return True
            return False
        else:
            return "Sorry, but you will not find this team in our firm"

    def print_skills(self, skills):
        return_skills = ""
        comma = False
        for count in skills:
            if skills[count] == 0:
                if comma is False:
                    return_skills += count
                else:
                    return_skills += ", " + count
                comma = True
        return return_skills

    def skills_not_in_team(self, skills):
        for team in self.teams:
            list_of_skills = {}
            for skill in skills:
                list_of_skills[skill] = 0
            for member in team.members:
                for skill in member.skills:
                    for s in skills:
                        if skill == s:
                            list_of_skills[s] += 1
            print_skills = self.print_skills(list_of_skills)
            for count in list_of_skills:
                if list_of_skills[count] == 0:
                    print(team.name + " : " + print_skills)
                    break


class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members


def assignment(lines):
    what_to_assign = 0

    for line in lines:
        line = line.strip()
        if "#Zamestnanci" in line:
            what_to_assign = 1
        elif "#Vedouci" in line:
            what_to_assign = 2
        elif "#Tymy" in line:
            what_to_assign = 3
        elif what_to_assign == 1:
            apple.employees.append(assign_employee(line))
        elif what_to_assign == 2:
            assign_boss(line)
        elif what_to_assign == 3:
            apple.teams.append((assign_team(line)))


def assign_employee(line):
    line = line.split(",")
    skills = line[2].split(";")
    employee = Employee(line[0], line[1], skills)
    return employee


def assign_boss(line):
    line = line.split("->")
    employee = apple.which_employee(line[1])
    boss = apple.which_employee(line[0])
    employee.boss = boss


def assign_team(line):
    line = line.split(": ")
    employees = line[1].split(", ")
    list_of_employees = []
    for employee in employees:
        list_of_employees.append(apple.which_employee(employee))
    team = Team(line[0], list_of_employees)
    return team


def read_file(file):
    input_file = open(file, "r")
    lines = input_file.readlines()
    input_file.close()
    assignment(lines)


apple = Firm()
read_file("firm_info.txt")    # reads file "firm_info.txt"

# SEVERAL TESTS FOR DIFFERENT FUNCTIONS
# ----------------------------------------
# apple.print_employees("Elon")
# print(apple.same_leader("Ruth", "Patricia"))
# print(apple.search_the_oldest_employee())
# print(apple.team_average_age("E-shop"))
# apple.print_sorted_teams_and_person()
# print(apple.number_of_employees("Elon"))
# print(apple.is_skill_in_team("E-shop", "css"))
# apple.skills_not_in_team(["support", "js", "html", "python", "manager", "css", "server", "sql", "qa", "test"])
