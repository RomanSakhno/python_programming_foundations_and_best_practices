import calendar
from datetime import datetime


def render_birthday_calendar(book):
    now = datetime.now()
    year = now.year
    month = now.month

    cal = calendar.monthcalendar(year, month)

    birthdays = {}

    for record in book.data.values():
        if record.birthday:
            bday = record.birthday.value
            if bday.month == month:
                birthdays.setdefault(bday.day, []).append(record.name.value)

    html = f"<h4>🎂 Birthdays in {calendar.month_name[month]}</h4>"
    html += "<table style='width:100%; text-align:center;'>"

    for week in cal:
        html += "<tr>"

        for day in week:
            if day == 0:
                html += "<td></td>"
            else:
                if day in birthdays:
                    names = ", ".join(birthdays[day])

                    html += f"""
                    <td style="
                        background:#ffe0e0;
                        border-radius:6px;
                        padding:6px;
                        font-weight:bold;
                    " title="{names}">
                        {day} 🎂
                    </td>
                    """
                else:
                    html += f"<td>{day}</td>"

        html += "</tr>"

    html += "</table>"

    return html