def add_expense(filename):
    category = input("Категория: ")
    amount = float(input("Сумма: "))
    note = input("Комментарий: ")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{category},{amount},{note}\n")

def show_expenses(filename):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            category, amount, note = line.strip().split(",")
            print(f"{category}: {amount} руб. - {note}")

if __name__ == "__main__":
    add_expense("expenses.txt")
    print("\nТекущие расходы:")
    show_expenses("expenses.txt")