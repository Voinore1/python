class Passport:
    def __init__(self, surname, name, patronymic, nationality, gender, passport_number, date_of_creation, expiry_date):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.nationality = nationality
        self.gender = gender
        self.passport_number = passport_number
        self.date_of_creation = date_of_creation
        self.expiry_date = expiry_date

    def display_info(self):
        return (f"Паспортна інформація:\n"
                f"Прізвище: {self.surname}\n"
                f"Ім'я: {self.name}\n"
                f"По батькові: {self.patronymic}\n"
                f"Національність: {self.nationality}\n"
                f"Стать: {self.gender}\n"
                f"Номер паспорта: {self.passport_number}\n"
                f"Дата видачі: {self.date_of_creation}\n"
                f"Дата закінчення терміну дії: {self.expiry_date}")

class ForeightPassport(Passport):
    def __init__(self, surname, name, patronymic, nationality, gender, passport_number, date_of_creation, expiry_date, visa_info):
        super().__init__(surname, name, patronymic, nationality, gender, passport_number, date_of_creation, expiry_date)
        self.visa_info = visa_info

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}\nВізова інформація: {self.visa_info}"


passport = Passport("Іванов", "Іван", "Іванович", "Україна", "Чоловіча", "UA123456", "2000-01-01", "2010-01-01")
print(passport.display_info())

print("////////////////////////////////////////////////////////////////")
foreignPassport = ForeightPassport("Smith", "John", "", "США", "Чоловіча", "US987654", "2000-01-01", "2020-01-01", "Шенгенська віза")
print(foreignPassport.display_info())