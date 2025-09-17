def dailyTemperatures(temperatures):
    # I’ll start by preparing the result list with zeros; default is 0 when no warmer day exists.
    n = len(temperatures)                       # number of days; I'll reference this a few times
    answer = [0] * n                            # prefill with 0s as required by the problem

    # I'll use a stack to store indices of days waiting for a warmer temperature.
    # The stack will be *monotonically decreasing* by temperature values.
    stack = []                                  # empty at the beginning; holds indices, not values

    # Now I iterate once from left to right; each day either gets pushed or resolves others.
    for i, temp in enumerate(temperatures):
        # While there's someone on the stack and current temp is strictly warmer,
        # I can finalize that person's waiting time.
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()                  # this index 'prev' has found its next warmer day
            answer[prev] = i - prev             # distance between the days

        # After resolving all cooler/equal tops, I still need to track today 'i'
        # because *its* warmer day is unknown yet.
        stack.append(i)

    # Anything left in the stack has no warmer day ahead; answers already 0, so nothing to do.
    return answer

temperatures = [73,74,75,71,69,72,76,73]
              #[ 0, 1, 2, 3, 4, 5, 6, 7]
print(dailyTemperatures(temperatures))