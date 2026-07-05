def total_salary(path):
    try: 
        with open(path, "r", encoding="utf-8") as salaries:
            whole_salary = 0
            all_developers = 0
            for line in salaries:
                part = line.split(",")
                salary = part[1]
                whole_salary += int(salary.strip())
                all_developers += 1
            if all_developers == 0:
                return None    
        average_salary = whole_salary / all_developers
        final_data = (whole_salary, average_salary)
    except FileNotFoundError: 
        return None
    return final_data    
