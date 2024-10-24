class Elevator:
    def __init__(self, bottom_floor: int, top_floor: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = 0

    def go_to_floor(self, target_floor: int):
        print(f"You are currently on floor: {self.current_floor}")

        if target_floor > self.top_floor:
            print(f"Target floor {target_floor} is out of bounds. Moving to floor 5.")
            target_floor = self.top_floor
        elif target_floor < self.bottom_floor:
            print(f"Target floor {target_floor} is out of bounds. Moving to floor 0.")
            target_floor = self.bottom_floor

        while self.current_floor != target_floor:
            if target_floor < self.current_floor:
                self.current_floor -= 1
                self.floor_down()
            elif target_floor > self.current_floor:
                self.current_floor += 1
                self.floor_up()

        print(f"You have arrived at floor: {self.current_floor}\n")

    def floor_up(self):
        print(f"Going up - floor {self.current_floor}")

    def floor_down(self):
        print(f"Going down - floor {self.current_floor}")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.num_elevators = num_elevators
        self.elevators = []

        for _ in range(self.num_elevators):
            self.elevators.append(Elevator(self.bottom_floor, self.top_floor))

    def run_elevator(self, elevator_number, target_floor):
        if 1 <= elevator_number <= self.num_elevators:
            print(f"Elevator {elevator_number} is going to floor {target_floor}.")
            self.elevators[elevator_number - 1].go_to_floor(target_floor)
        else:
            print(
                f"Invalid elevator number: {elevator_number}. Please choose a number between 1 and {self.num_elevators}.")

b = Building(0, 5, 3)
b.run_elevator(2, 2)
b.run_elevator(1, 3)
