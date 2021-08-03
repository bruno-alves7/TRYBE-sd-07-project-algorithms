def study_schedule(permanence_period, target_time):
    """verifica a quant. que um valor aparece em uma lista de tuplas"""

    count = 0
    for element in permanence_period:
        if (
            not isinstance(element[0], int)
            or not isinstance(element[1], int)
            or not isinstance(target_time, int)
        ):
            return None
        if element[0] <= target_time <= element[1]:
            count += 1

    return count
