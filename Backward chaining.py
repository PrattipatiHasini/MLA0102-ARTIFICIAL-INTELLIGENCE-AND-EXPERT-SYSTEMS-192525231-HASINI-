# Backward Chaining

facts = {
    "fly",
    "cough"
}

rules = {
    "furry": ["fly", "cough"],
    "rest": ["fly"],
    "doctor_visit": ["furry", "rest"]
}


def backward_chaining(goal, facts, rules, visited=None):

    if visited is None:
        visited = set()

    # If goal is already a fact
    if goal in facts:
        return True

    # Avoid infinite loops
    if goal in visited:
        return False

    visited.add(goal)

    # If no rule can prove the goal
    if goal not in rules:
        return False

    # Check all conditions
    for condition in rules[goal]:
        if not backward_chaining(condition, facts, rules, visited):
            return False

    return True


print("BACKWARD CHAINING")
print("------------------")

goal = input("Enter goal: ").lower()

if backward_chaining(goal, facts, rules):
    print("Goal:", goal, "can be proved from facts.")
else:
    print("Goal:", goal, "cannot be proved from given facts.")
