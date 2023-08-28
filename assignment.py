class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def sort_and_print(self, sort_parameter):
        if sort_parameter == 1:
            sorted_employees = sorted(self.employees, key=lambda emp: emp.age)
        elif sort_parameter == 2:
            sorted_employees = sorted(self.employees, key=lambda emp: emp.name)
        elif sort_parameter == 3:
            sorted_employees = sorted(self.employees, key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter")
            return

        for emp in sorted_employees:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    database = EmployeeDatabase()

    database.add_employee(Employee("161E90", "Raman", 41, 56000))
    database.add_employee(Employee("161F91", "Himadri", 38, 67500))
    database.add_employee(Employee("161F99", "Jaya", 51, 82100))
    database.add_employee(Employee("171E20", "Tejas", 30, 55000))
    database.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    sorting_param = int(input())

    database.sort_and_print(sorting_param)
