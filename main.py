import time
from datetime import datetime as d
from to_do_class import ToDoList


def display(to_do: ToDoList, svolte: bool,
            un_svolte: bool, prior: bool) -> None:
    if not to_do.get_data():
        print("No activities registered")
    else:
        if svolte and not un_svolte:
            data = to_do.filter_check_actitivities()
        elif not svolte and un_svolte:
            data = to_do.filter_unchecked_activities()
        else:
            data = to_do.get_data()
        if prior:
            data = to_do.filter_priority(data)
        for i, (act, info) in enumerate(data.items(), start=1):
            sign = "[X]" if info["check"] else "[]"
            print(f"{i}. {act} ({info['expiry']}) ({info['priority']}) {sign}")


if __name__ == "__main__":
    li = ToDoList()
    svolte = True
    un_svolte = True
    prior = False
    while True:
        print("=== TO DO LIST ===")
        print()
        display(li, svolte, un_svolte, prior)
        print()
        print("Choose an option:")
        print("1) Add activity")
        print("2) Mark activity as done")
        print("3) Mark activity as to do")
        print("4) Show only done activities")
        print("5) Show only to do activities")
        print("6) Filter by priority (High -> Low)")
        print("7) Show all activities")
        print("8) Delete activity")
        print("9) Quit")
        print()
        inp = input("- ")
        match inp:
            case "1":
                try:
                    nome = input("Name of the activity: ").capitalize()
                    data = input("Deadline (DD/MM/YY): ")
                    priorità = input("Priority level "
                                     "(High-Medium-Low) ").capitalize()
                    data_oggetto = d.strptime(data, "%d/%m/%y").date()
                    li.add_activity(nome, data_oggetto, priorità)
                    print("Activity registered")
                    print()
                except ValueError as e:
                    print(e)
                time.sleep(3)
            case "2":
                try:
                    inp = input("Which activity "
                                "you want to mark as done? ").capitalize()
                    li.check_activity(inp)
                    print("Activity marked")
                    print()
                except ValueError as e:
                    print(e)
                time.sleep(3)
            case "3":
                try:
                    inp = input("Which activity "
                                "you want to mark as to do? ").capitalize()
                    li.uncheck_activity(inp)
                    print("Activity marked")
                    print()
                except ValueError as e:
                    print(e)
                time.sleep(3)
            case "4":
                svolte = True
                un_svolte = False
            case "5":
                svolte = False
                un_svolte = True
            case "6":
                prior = True
            case "7":
                svolte = True
                un_svolte = True
                prior = False
            case "8":
                try:
                    inp = input("Which activity you "
                                "want to delete? ").capitalize()
                    li.delete_activity(inp)
                    print("Activity deleted")
                    print()
                except ValueError as e:
                    print(e)
                time.sleep(3)
            case "9":
                print("Exiting the program...")
                li.save_activities()
                break
            case _:
                print("Pick a valid action")
                print()
                time.sleep(3)
