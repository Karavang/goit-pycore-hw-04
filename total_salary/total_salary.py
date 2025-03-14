def total_salary(path):
    try:
        with open(path) as file:
            print(file)
            data = file.readlines()
            salaryArr = []
            for str in data:
                emp = str.strip().split(",")
                salaryArr.append(int(emp[1]))
            file.close()
            return f"Загальна зарплата: {sum(salaryArr)}\nСередня зарплата: {int(sum(salaryArr)/len(salaryArr))}"
    except:
        return "Щось не так з файлом"


print(total_salary("./total_salary/total_salary.txt"))
