import calendar
from datetime import datetime
from services.birthday_range_service import get_birthdays_in_month


def render_birthday_calendar(book):
    now = datetime.now()
    year = now.year
    month = now.month

    cal = calendar.monthcalendar(year, month)
    birthdays = get_birthdays_in_month(book, month)

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