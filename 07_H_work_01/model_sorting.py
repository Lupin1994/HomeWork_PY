def sort_names():
    with open("Worker_list.txt","r+") as file:
        lst_with_Str = file.readline()
        lst_with_list = []
        for line in lst_with_Str:
            temp = line.split(",")
            lst_with_list.append(temp)
        lst_with_list = sorted(lst_with_list,key = lambda x: x[1])
        file.seek(0)
        for worker in lst_with_list:
            file.write(",".join(worker))
        print("Отсортировано")
        


def sort_id():
    with open("Worker_list.txt","r+") as file:
        lst_with_Str = file.readline()
        lst_with_list = []
        for line in lst_with_Str:
            temp = line.split(",")
            lst_with_list.append(temp)
        lst_with_list = sorted(lst_with_list,key = lambda x: x[0])
        file.seek(0)
        for worker in lst_with_list:
            file.write(",".join(worker))
        print("Отсортировано")
        