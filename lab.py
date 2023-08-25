class Process:
    def _init_(self, pid, process_name, start_time, priority):
        self.pid = pid
        self.process_name = process_name
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def _init_(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def sort_by_pid(self):
        self.processes.sort(key=lambda process: process.pid)

    def sort_by_start_time(self):
        self.processes.sort(key=lambda process: process.start_time)

    def sort_by_priority(self):
        priority_order = {"Low": 0, "MID": 1, "High": 2}
        self.processes.sort(key=lambda process: priority_order[process.priority])

    def display_table(self):
        print("P_ID  Process     Start Time  Priority")
        print("--------------------------------------")
        for process in self.processes:
            print(f"{process.pid:<6}{process.process_name:<12}{process.start_time:<12}{process.priority}")

def main():
    flight_table = FlightTable()

    flight_table.add_process(Process("P1", "VSCode", 100, "MID"))
    flight_table.add_process(Process("P23", "Eclipse", 234, "MID"))
    flight_table.add_process(Process("P93", "Chrome", 189, "High"))
    flight_table.add_process(Process("P42", "JDK 9", 9, "High"))
    flight_table.add_process(Process("P9", "CMD", 7, "High"))
    flight_table.add_process(Process("P87", "NotePad", 23, "Low"))

    while True:
        print("\nOptions:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            flight_table.sort_by_pid()
        elif choice == '2':
            flight_table.sort_by_start_time()
        elif choice == '3':
            flight_table.sort_by_priority()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        flight_table.display_table()

if _name_ == "_main_":
    main()
