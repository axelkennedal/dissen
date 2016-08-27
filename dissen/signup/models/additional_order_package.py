class AdditionalOrderPackage():
    """Describes an additional order."""

    PEOPLE_DAY_PRICE = 300
    PEOPLE_EVENING_PRICE = 500
    DRINK_TICKET_PRICE = 30
    TABLE_PRICE = 300

    people_day = 0
    people_evening = 0
    drink_tickets = 0
    tables = 0

    def __init__(self, people_day, people_evening, drink_tickets, tables):
        self.people_day = people_day
        self.people_evening = people_evening
        self.drink_tickets = drink_tickets
        self.tables = tables

    def calculate_total_price(self):
        return (people_day * PEOPLE_DAY_PRICE) +
        (people_evening * PEOPLE_EVENING_PRICE) +
        (drink_tickets * DRINK_TICKET_PRICE) +
        (tables * TABLE_PRICE)
