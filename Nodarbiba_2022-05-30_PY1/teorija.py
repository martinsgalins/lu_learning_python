def calculate_bonus(hours, hourly_wage):
    bonus = 0

    if hours > 200 and hourly_wage < 15:
        bonus += 500

    return bonus


class Accounting:
    def __init__(self, person):
        self.person = person

    # Ex. 3
    def calculate_salary(self):
        print(f'From {self.__class__.__name__}')

        bonus = calculate_bonus(
            hours=self.person.hours,
            hourly_wage=self.person.hourly_wage,
        )

        return ((self.person.hourly_wage * self.person.hours) / self.person.years_of_experience) + bonus


class IvarsAccounting:
    def __init__(self, person):
        self.person = person

    # Ex. 3
    def calculate_salary(self):
        print(f'From {self.__class__.__name__}')

        return (self.person.hourly_wage * self.person.hours) * self.person.years_of_experience


def accounting_from(person):
    if person.name == 'Ivars':
        accounting_class = IvarsAccounting

    else:
        accounting_class = Accounting

    return accounting_class(person=person)


class Person:
    def __init__(self, name, years_of_experience, hours, hourly_wage):
        self.name = name
        self.years_of_experience = years_of_experience
        self.hours = hours
        self.hourly_wage = hourly_wage

        self.accounting = accounting_from(person=self)


persons = [
    Person(
        name='Andrew',
        years_of_experience=2,
        hours=2,
        hourly_wage=10,
    ),

    Person(
        name='Olegs',
        years_of_experience=5,
        hours=89,
        hourly_wage=20,
    ),

    Person(
        name='Ivars',
        years_of_experience=10,
        hours=150,
        hourly_wage=50,
    ),
]

for person in persons:
    person_salary = person.accounting.calculate_salary()

    print(person_salary)