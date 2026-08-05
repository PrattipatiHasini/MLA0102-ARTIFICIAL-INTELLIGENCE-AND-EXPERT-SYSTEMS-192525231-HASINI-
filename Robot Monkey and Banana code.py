# Monkey and Banana Problem

def monkey_banana():
    actions = [
        "Monkey moves to the chair.",
        "Monkey pushes the chair below the banana.",
        "Monkey climbs onto the chair.",
        "Monkey reaches for the banana.",
        "Monkey grabs the banana."
    ]

    print("Goal: Get the banana\n")

    for i, action in enumerate(actions, start=1):
        print(f"Step {i}: {action}")

    print("\nGoal Achieved: Monkey successfully got the banana!")

# Run the program
monkey_banana()
