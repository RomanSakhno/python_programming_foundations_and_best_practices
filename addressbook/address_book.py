from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        return self.data.pop(name, None)

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming = []

        for record in self.data.values():

            if not record.birthday:
                continue

            birthday = record.birthday.value.date()

            try:
                birthday_this_year = birthday.replace(year=today.year)
            except ValueError:
                birthday_this_year = birthday.replace(
                    year=today.year,
                    month=2,
                    day=28
                )

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            delta = (birthday_this_year - today).days

            if 0 <= delta <= 7:

                congratulation_date = birthday_this_year

                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)

                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)

                upcoming.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
                })

        return upcoming

    def search(self, query):

        results = []

        for record in self.data.values():

            if query.lower() in record.name.value.lower():
                results.append(record)
                continue

            for phone in record.phones:
                if query in phone.value:
                    results.append(record)
                    break

            if record.email and query in record.email.value:
                results.append(record)

        return results

    def rename(self, old_name, new_name):

        record = self.find(old_name)

        if not record:
            return None

        del self.data[old_name]

        record.name.value = new_name

        self.data[new_name] = record

        return record