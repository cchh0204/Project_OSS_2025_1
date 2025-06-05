from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 소득 추가")
        print("3. 지출 목록 보기")
        print("4. 소득 목록 보기")
        print("5. 총 지출 보기")
        print("6. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)
        
        elif choice == "2":
            source = input("소득원 (예:알바, 용돈 등):")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_income(source, description, amount)
        elif choice == "3":
            budget.list_expenses()

        elif choice == "4":
            budget.list_incomes()

        elif choice == "5":
            budget.total_spent()

        elif choice == "6":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
