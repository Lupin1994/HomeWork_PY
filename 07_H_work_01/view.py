

def op():
    op = int(input(
        "1-добавить пользователя \n 2-вывести таблицу \n 3-вывести только имя и фамилию \n 4-отсортировать по имени \n 5-отсортировать по id \n 6-выход \n"))
    return op

def add_worker():
    id = int(input())
    name = input()
    lastname = input()
    number = int(input())
    comments = input()
    line = f"{id},{name},{lastname},{number},{comments} \n"
    with open("Worker_list.txt","a") as file:
        file.write(line)
    print("Сохранено")
    
    
def print_table():
    with open("Worker_list.txt","r") as file:
        for line in file.readlines():
            print(line,end=" ")
def print_only_names():
    with open("Worker_list.txt","r") as file:
        for line in file.readlines():
            temp = line.split(",")
            print(f'Name - {temp[1]}, Фамилия - {temp[2]}')