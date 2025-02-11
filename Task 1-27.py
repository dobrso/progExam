def textAnalyze():
    specialChars = "{}+=()\"':."
    result = []

    with open("Test 1-27.txt", "r") as inputData:
        lineNum = 0

        for line in inputData:
            lineNum += 1
            count = 0

            for char in line:
                if char in specialChars:
                    count += 1

            result.append((lineNum, count))

    return result

def hashCalculate(data):
    return sum(lineNum * count for lineNum, count in data)

data = textAnalyze()

print(f"Набор: {data}")
print(f"Хэш файла: {hashCalculate(data)}")