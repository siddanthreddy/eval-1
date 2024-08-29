students = {}
dietplan = [
    {
        "id": "dp1",
        "agility": 8,
        "speed": 9,
        "strength": 10,
        "recommandSport": "cricket"
    },
    {
        "id": "dp2",
        "agility": 7,
        "speed": 10,
        "strength": 10,
        "recommandSport": "football"
    },
    {
        "id": "dp3",
        "agility": 10,
        "speed": 10,
        "strength": 5,
        "recommandSport": "chess"
    },
    {
        "id": "dp4",
        "agility": 5,
        "speed": 5,
        "strength": 10,
        "recommandSport": "javelin throw"
    }
]

def add_students(id, name, classs, height, weight, sport, agility, speed, strength):
    students[id] = {
        "name": name,
        "class": classs,
        "height": height,
        "weight": weight,
        "sport": sport,
        "agility": agility,
        "speed": speed,
        "strength": strength
    }

def get_personalized(agility, speed, strength):
    for dp in dietplan:
        if (dp["agility"] == agility and dp["speed"] == speed and dp["strength"] == strength):
            return {"plan id": dp["id"], "recommended sport": dp["recommandSport"]}
    return None

def add_diet():
    for student_id, student_info in students.items():
        plan = get_personalized(student_info["agility"], student_info["speed"], student_info["strength"])
        if plan:
            print(f"Student: {student_info['name']}, {plan}")
        else:
            print(f"Student: {student_info['name']}, No matching diet plan found.")

add_students(1, "siddanth", 12, 5.7, 60, "cricket", 5, 5, 10)
add_students(2, "reddy", 11, 5.9, 50, "cricket", 8, 9, 10)

add_diet()
