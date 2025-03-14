def get_cats_info(path):
    try:
        with open(path) as file:
            data = file.readlines()
            infoCats = []
            for cat in data:
                objCat = cat.strip().split(",")

                infoCats.append({"id": objCat[0], "name": objCat[1], "age": objCat[2]})
            print(infoCats)

    except:
        return "Щось не так з файлом"


print(get_cats_info("./get_cats_info/cats.txt"))
