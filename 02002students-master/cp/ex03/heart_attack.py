"""Exercise 3.8: Heart attack."""


def heart_attack(age: int, weight: int, smoker: bool) -> str:
    """Return a string indicating the risk of a person for having heart attack.

    :param age: The age of the person.
    :param weight: The weight of the person in kilograms.
    :param smoker: Does the person smoke cigarettes?
    :return: A string, either "low" or "high", indicating the risk for having heart attack.
    """
    # TODO: Code has been removed from here.
    if age < 18 and weight < 60:
        return "low"
    if age < 18 and weight > 60:
        return "high"
    if 18 <= age <= 30:
        return "low"
    if age > 30 and smoker:
        return "high"
    if age > 30 and not smoker:
        return "low"
    return "error"

if __name__ == "__main__":
    a = int(input("Enter your age: "))
    w = int(input("Enter your weight: "))
    s = input("Are you a smoker (Y/N): ")
    sm = False
    if s == 'Y':
        sm = True
    if s == 'N':
        sm = False
    print(heart_attack(a, w, sm))
