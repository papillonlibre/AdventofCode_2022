f = open("day_3_input.txt", "r")

def calculate_priority(item_type):
    if 'a' <= item_type <= 'z':
        return ord(item_type) - ord('a') + 1
    elif 'A' <= item_type <= 'Z':
        return ord(item_type) - ord('A') + 27

def find_common_item_priorities(rucksacks):
    common_item_priorities = []

    for rucksack in rucksacks:
        first_compartment = rucksack[:len(rucksack)//2]
        second_compartment = rucksack[len(rucksack)//2:]

        for item_type in first_compartment:
            if item_type in second_compartment:
                priority = calculate_priority(item_type)
                common_item_priorities.append(priority)
                break

    return common_item_priorities

rucksacks = []
for rucksack in f:
    rucksacks.append(rucksack)

common_item_priorities = find_common_item_priorities(rucksacks)
sum_of_priorities = sum(common_item_priorities)

print(f"Sum of priorities: {sum_of_priorities}")


    