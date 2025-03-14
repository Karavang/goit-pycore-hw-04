def get_cats_info(path):
    try:
        with open(path) as file:
            data = file.readlines()
            infoCats = []
            for cat in data:
                objCat = cat.strip().split(",")
                id_val = objCat[0]
                name_candidate = objCat[1].strip() if len(objCat) > 1 else ""
                age_candidate = objCat[2].strip() if len(objCat) > 2 else ""

                if len(objCat) >= 3:
                    name_val = name_candidate if name_candidate else "Немаємо інфи"
                elif len(objCat) == 2:
                    name_val = name_candidate if name_candidate else "Маємо тільки id"
                else:
                    name_val = "Маємо тільки id"

                age_val = (
                    int(age_candidate)
                    if (len(objCat) >= 3 and age_candidate and age_candidate.isdigit())
                    else "Немає інфи"
                )

                infoCats.append(
                    {
                        "id": id_val,
                        "name": name_val,
                        "age": age_val,
                    }
                )

            return infoCats

    except:
        return "Щось не так з файлом"


print(get_cats_info("./get_cats_info/cats.txt"))
