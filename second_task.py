def get_cats_info(path):
    try: 
        with open (path, "r", encoding="utf-8") as cats:
            cats_list = []
            for line in cats:
                cat_data = line.strip().split(",")
                cat_dict = {
                "id": cat_data[0],
                "name": cat_data[1],
                "age": cat_data[2]
            }
                cats_list.append(cat_dict) 
    except FileNotFoundError:
        return None               
    return cats_list