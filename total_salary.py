def total_salary(path):
    file = open(path, "r")
    data = file.readlines()
    salaryArr = []
    for str in data:
        emp = str.strip().split(",")
        salaryArr.append(int(emp[1]))
    file.close()
    return f"Загальна зарплата: {sum(salaryArr)}\nСередня зарплата: {int(sum(salaryArr)/len(salaryArr))}"
    print(salaryArr)


print(total_salary("./total_salary.txt"))
