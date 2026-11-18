# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    #   ...
    # Restate: find the total using reverse polish notation
    # Plan: go through the whole list taking two indexs being the first and second indexes, next check if the third index
    # is a operator, if it is then do the operator to the two index and put it into another stack, if it is not an operator, 
    # then I would take the first index into another stack and continue until I have looked through the whole original list. 
    # Once I reach the end I would restart the whole process until I get 1 value in the list
    # then return that number to be my answer.
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    
    operators = ["+", "-", "*", "/"]

    while len(tokens) > 1:
        new_list = []
        i = 0

        while i < len(tokens):
            if i + 2 < len(tokens) and tokens[i + 2] in operators:
                num1 = tokens[i]
                num2 = tokens[i + 1]
                op = tokens[i + 2]

                if op == "+":
                    result = int(num1) + int(num2)
                elif op == "-":
                    result = int(num1) - int(num2)
                elif op == "*":
                    result = int(num1) * int(num2)
                else:  # op == "/"
                    result = int(num1) / int(num2)

                new_list.append(result)
                i += 3  # skip the two numbers and the operator

            else:
                new_list.append(tokens[i])
                i += 1

        tokens = new_list

    return tokens[0]


def decode_string(s):
    # Outline:
    #   ...
    # Restate: decode the encoded string by repeating the encoded stuff inside 
    # of the brackets by the amount outside of the brackets like k[encoded]
    # Plan: I would first go backwards looking at the closing bracket and the opening bracket and the number
    # on the left of the opening bracket to get the number of times its repeated and the encode string that needs
    # to be repeated and add that to another list while also not bring any of the brackets and repeating this until I reach the start of the list which would
    # have resulted in me having the code but backwards, so I would flip it and return it to get the 
    # decoded code.

    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    
    queue = []

    for char in s:
        if char != ']':
            queue.append(char)
        else:
            # Get encoded string
            encoded = ""
            while queue and queue[-1] != '[':
                encoded = queue.pop() + encoded

            queue.pop()  # Remove '['

            # Get repeat number
            num = ""
            while queue and queue[-1].isdigit():
                num = queue.pop() + num

            repeated = encoded * int(num)

            # Put decoded part back on queue
            for c in repeated:
                queue.append(c)

    return "".join(queue)


def daily_temperatures(temps):
    # Outline:
    #   ...
    # Restate: Find how many more days it will take for the temperature to greater than that days temperature.
    # Plan: I would first have another stack to store the days it will take for the temperature to increase.
    # Then through the original list, I would take the temperature for that day and move through the whole list until
    # another temp is larger while also keeping track of the amount taken to find that day and put it into the other list,
    # if I can not find a larger number then I would add 0 to the other list, then return the whole list.
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    days_until_warmer = []

    for i in range(len(temps)):
        days = 0
        found = False

        for j in range(i + 1, len(temps)):
            days += 1

            if temps[j] > temps[i]:
                days_until_warmer.append(days)
                found = True
                break

        if not found:
            days_until_warmer.append(0)

    return days_until_warmer


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
   
    # print(eval_rpn(["2", "1", "+", "3", "*"]))    # returns 9    ((2 + 1) * 3)
    # print(eval_rpn(["4", "13", "5", "/", "+"]))   # returns 6    (4 + 13 // 5)
    # print(decode_string("3[a]2[bc]"))   # returns "aaabcbc"
    # print(decode_string("3[a2[c]]"))    # returns "accaccacc"
    # print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))   # returns [1, 1, 4, 2, 1, 1, 0, 0]
    # print(daily_temperatures([30, 40, 50, 60]))                   # returns [1, 1, 1, 0]
    pass


if __name__ == "__main__":
    main()
