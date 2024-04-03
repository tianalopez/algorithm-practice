##Problem 1:
##Incorrect Solution:def solution(operations):
    rectangles = []

    def fits(box):
        for rect in rectangles:
            if (box[0] <= rect[0] and box[1] <= rect[1]) or (box[0] <= rect[1] and box[1] <= rect[0]):
                return True
        return False

    results = []
    for op in operations:
        if op[0] == 0:  # Create rectangle
            rectangles.append((op[1], op[2]))
        elif op[0] == 1:  # Check if box fits
            if rectangles:
                results.append(fits((op[1], op[2])) or fits((op[2], op[1])))
            else:
                results.append(True)  # Any box can fit into an empty space

    return results

# Example usage:
operations = [[1,1,1]]
print(solution(operations))  # Output: [True]
