class Employee:

    def __init__(self, name, dept, age):
        self.name = name
        self.dept = dept
        self.age = age

    def __repr__(self):
        return '{' + self.name + ', ' + self.dept + ', ' + str(self.age) + '}'


if __name__ == '__main__':
    employees = [
        Employee('John', 'IT', 28),
        Employee('Sam', 'Banking', 20),
        Employee('Joe', 'Finance', 25)
    ]

    # sort list by `name` in the natural order
    employees.sort(key=lambda x: x.dept)

    # output: [{Joe, Finance, 25}, {John, IT, 28}, {Sam, Banking, 20}]
    print(employees)

    # sort list by `name` in reverse order
    employees.sort(key=lambda x: x.dept, reverse=True)

    # output: [{Sam, Banking, 20}, {John, IT, 28}, {Joe, Finance, 25}]
    print(employees)