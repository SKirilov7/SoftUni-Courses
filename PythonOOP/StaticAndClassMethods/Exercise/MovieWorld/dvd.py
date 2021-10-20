MONTHS_AS_NUMBERS = {
    1: 'January',
	2: 'February',
	3: 'March',
	4: 'April',
	5: 'May',
	6: 'June',
	7: 'July',
	8: 'August',
	9: 'September',
	10: 'October',
	11: 'November',
	12: 'December'
}


class DVD:
    def __init__(self,name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False


    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = date.split('.')
        month_string = MONTHS_AS_NUMBERS[int(month)]
        year = int(year)
        return cls(name,id, year,month_string,age_restriction)



