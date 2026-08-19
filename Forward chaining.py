# Forward Chaining

facts = {"fever", "cough", "flu"}

rules = [
    ({"fever", "cough"}, "sick"),
    ({"sick"}, "rest"),
    ({"sick", "rest"}, "doctor_visit")
]


def forward_chaining(facts, rules):
    facts = set(facts)
    changed = True

    while changed:
        changed = False

        for conditions, conclusion in rules:
            if conditions.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                changed = True

    return facts


print("FORWARD CHAINING")
print("-----------------")

print("Initial facts:")
for fact in facts:
    print("-", fact)

final_facts = forward_chaining(facts, rules)

print("\nFinal facts:")
for fact in final_facts:
    print("-", fact)
