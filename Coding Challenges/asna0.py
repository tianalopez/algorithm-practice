# adds first problem, and correct solution
def solution(n):
    digits = str(n)
    answer = int(digits[0])  # Add the first digit with a positive sign

    for i in range(1, len(digits)):  # Start the loop from index 1
        if i % 2 == 0:
            answer += int(digits[i])
        else:
            answer -= int(digits[i])

    return answer
