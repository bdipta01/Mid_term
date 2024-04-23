class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self) 

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        self.__seats[id] = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def book_seats(self, show_id, seat_info):
        if show_id in self.__seats:
            row, col = seat_info
            if 0<=row and row<=self.rows and 0<=col and col <= self.cols:
                if self.__seats[show_id][row][col] == 0:
                    self.__seats[show_id][row][col] = 1
                    print(f'seat{row}{col} is successfully booked')
                else:
                    print(f'{row}{col} is already booked. Try another one')
            else:
                print(f'Invalid position {row}{col}. Enter valid position')
        else:
            print(f'{show_id} is not available')

    def view_show_list(self):
        for view_show in self.__show_list:
            show_id, show_name, show_time = view_show
            print(f'Running\nMovie ID : {show_id}\nMovie Name : {show_name}\nMovie Time : {show_time}')

    def view_available_seat(self, id):
        if id in self.__seats:
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.__seats[id][row][col] == 0:
                        print(f'Available Seat {row} {col}')
        
        else:
            print(f'{id} This movie not available')


new_hall = Hall(2,2,1)
new_hall.entry_show('01', 'Oppenheimer', 'Sat-5PM')
new_hall.entry_show('02', 'Chernobyl', 'Sun-5PM')


print('Select Option: ')
print('1: Show List')
print('2: Available Seats')
print('3: Book Seat')
print('4: Log Out')

while True:
    option = int(input())

    if option == 1:
        new_hall.view_show_list()

    elif option == 2:
        print(f"Enter movie ID to check the seat")
        movie_ID = input()
        new_hall.view_available_seat(movie_ID)

    elif option == 3:
        print("Enter movie ID, seat, row")
        id = input()
        row = int(input())
        col = int(input())
        new_hall.book_seats(id, (row, col))

    elif option == 4:
        print(f"Exit")
        break