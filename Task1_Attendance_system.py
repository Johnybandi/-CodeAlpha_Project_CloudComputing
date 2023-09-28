import datetime

# Define a class to represent employees or students
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.attendance_records = []

    def mark_attendance(self, in_time, out_time):
        self.attendance_records.append({
            'in_time': in_time,
            'out_time': out_time
        })

# Create a list of employees/students
people = [
    Person(1, "Johny"),
    Person(2, "Esther"),
    Person(3, "Jolly ruth")
]

# Simulate attendance marking
for person in people:
    in_time = datetime.datetime.now()
    out_time = in_time + datetime.timedelta(hours=8)  # Simulating an 8-hour work/school day
    person.mark_attendance(in_time, out_time)

# Calculate hours spent on the premises
for person in people:
    total_hours = sum((record['out_time'] - record['in_time']).total_seconds() / 3600 for record in person.attendance_records)
    print(f"{person.name}: {total_hours:.2f} hours")