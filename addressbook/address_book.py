"""Container and search logic for contact records."""

from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):
    """Dictionary-like collection of contact records keyed by name."""

    def add_record(self, record):
        """Add a new contact record to the address book."""
        # ✅ Good: only stores the record, no presentation logic here
        self.data[record.name.value] = record

    def find(self, name):
        """Return the record for the given name or None."""
        # ⚠️ Consider normalizing the key on add_record to avoid looping every time
        # e.g., store self.data[record.name.value.lower()] = record
        for key in self.data:
            if key.lower() == name.lower():
                return self.data[key]
        return None

    def delete(self, name):
        """Remove and return the record for the given name, if any."""
        # ✅ Clean, domain logic only
        return self.data.pop(name, None)

    def get_upcoming_birthdays(self):
        """Return contacts with birthdays in the next 7 days.

        Birthdays that fall on a weekend are shifted to the following Monday
        for the congratulation date. The result is a list of dictionaries
        containing contact name and formatted congratulation date.
        """
        today = datetime.today().date()
        upcoming = []

        for record in self.data.values():
            if not record.birthday:
                continue

            birthday = record.birthday.value.date()

            try:
                birthday_this_year = birthday.replace(year=today.year)
            except ValueError:
                # ⚠️ Leap-year handling is okay, but consider moving formatting to a separate layer
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

                # ⚠️ Here you are formatting as string (%d.%m.%Y) inside domain layer
                # Suggestion: return raw date object, let presentation layer format it
                upcoming.append({
                    "name": record.name.value,
                    "congratulation_date": congratulation_date.strftime("%d.%m.%Y")  # <- move formatting out
                })

        return upcoming

    def search(self, query):
        """Search contacts by name, phone number or email substring."""
        results = []

        for record in self.data.values():
            # ✅ Searching logic is fine
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
        """Rename a contact, preserving its record."""
        record = self.find(old_name)
        if not record:
            return None

        # ⚠️ Consider normalizing keys for case-insensitivity
        del self.data[old_name]

        record.name.value = new_name
        self.data[new_name] = record

        return record