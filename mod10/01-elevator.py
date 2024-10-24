class Elevator:
    def __init__(self, bottom_floor: int, top_floor: int):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = 0

    def go_to_floor(self, target_floor: int):
        print(f"You are at currently floor: {e.current_floor}")

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

        print(f"You are at currently floor: {e.current_floor}\n")

    def floor_up(self):
        print(f"Going up - floor {self.current_floor}")

    def floor_down(self):
        print(f"Going down - floor {self.current_floor}")

e = Elevator(0, 5)

e.go_to_floor(5)

e.go_to_floor(0)


