def diffWaysToCompute(expression):
    def compute(left, right, op):
        calculation = []
        for l in left:
            for r in right:
                calculation.append(eval(str(l)+op+str(r)))
        return calculation

    if expression.isdigit():
        return [int(expression)] 

    result = []
    for i,v in enumerate(expression):
        if v in ["-","+","*"]:
            left = diffWaysToCompute(expression[:i])
            right = diffWaysToCompute(expression[i+1:])
            result.extend(compute(left, right, v))
    return result