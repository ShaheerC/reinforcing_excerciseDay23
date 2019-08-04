classroom_seating = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

def display_seats(seating):
    for row in seating:
        print(row)

def claim_seat(seating):
    for i, row in enumerate(seating):
        for x, name in enumerate(row):
            if name == None:
                response = input(
                    f'Row {i + 1} seat {x + 1} is free.  Do you want to sit there? (y/n) ')
                if response == 'y':
                    response = input('What is your name? ')
                    seating[i][x] = response
                    display_seats(seating)
                    return

display_seats(classroom_seating)
claim_seat(classroom_seating)