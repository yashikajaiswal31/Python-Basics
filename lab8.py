from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target_quantity):
    visited_states = set()
    initial_state = (0, 0)  # Initial state with both jugs empty

    queue = deque([(initial_state, [])])

    while queue:
        current_state, steps = queue.popleft()
        jug1, jug2 = current_state

        if current_state in visited_states:
            continue

        visited_states.add(current_state)

        # Check if the target quantity is achieved
        if jug1 == target_quantity or jug2 == target_quantity:
            print("\nSolution : ")
            print(solution_in_text_format(steps, target_quantity))
            print("Final State:", current_state)
            print("Steps:")
            for step in steps:
                print(step)
            return

        # Fill jug 1
        queue.append(((jug1_capacity, jug2), steps + [f"Fill jug 1"]))

        # Fill jug 2
        queue.append(((jug1, jug2_capacity), steps + [f"Fill jug 2"]))

        # Empty jug 1
        queue.append(((0, jug2), steps + [f"Empty jug 1"]))

        # Empty jug 2
        queue.append(((jug1, 0), steps + [f"Empty jug 2"]))

        # Pour water from jug 1 to jug 2
        pour_amount = min(jug1, jug2_capacity - jug2)
        queue.append(((jug1 - pour_amount, jug2 + pour_amount), steps + [f"Pour from jug 1 to jug 2 ({pour_amount} units)"]))

        # Pour water from jug 2 to jug 1
        pour_amount = min(jug2, jug1_capacity - jug1)
        queue.append(((jug1 + pour_amount, jug2 - pour_amount), steps + [f"Pour from jug 2 to jug 1 ({pour_amount} units)"]))

    print("No solution found.")

def solution_in_text_format(steps, target_quantity):
    text_solution = ""
    for step in steps:
        if "Fill" in step:
            jug = step.split()[2]
            text_solution += f"Final quantity {target_quantity} units is achieved in jug {jug}\n"
            break
        elif "Pour" in step:
            jug = step.split()[-3]
            text_solution += f"Final quantity {target_quantity} units is achieved in jug {jug}\n"
            break
    return text_solution

#user input
jug1_capacity = int(input("Enter Capacity of Jug1: "))
jug2_capacity = int(input("Enter Capacity of Jug2: "))
target_quantity = int(input("Enter Target Capacity: "))

water_jug_problem(jug1_capacity, jug2_capacity, target_quantity)
