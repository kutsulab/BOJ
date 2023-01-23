def solution(a, b):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekdays = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    day_sum = sum(days[:a]) + b
    return weekdays[day_sum % 7]
