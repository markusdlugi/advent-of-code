with open("input/06.txt") as f:
    groups = [group.splitlines() for group in f.read().split("\n\n")]


# Iterative solution
def solve_old():
    all_ = any_ = 0
    for group in groups:
        all_questions = set()
        any_questions = set()
        for line in group:
            if not any_questions:
                all_questions.update(set(line))
            else:
                all_questions.intersection_update(set(line))
            any_questions.update(set(line))
        all_ += len(all_questions)
        any_ += len(any_questions)

    print(any_)
    print(all_)


# List comprehension magic
print(sum(len(set.union(*map(set, group))) for group in groups))
print(sum(len(set.intersection(*map(set, group))) for group in groups))
