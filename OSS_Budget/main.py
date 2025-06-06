from inspect import stack
from itertools import count
from budget import Budget


def main():
    budget = Budget()
    try:
        limit = int(input("초기 예산 한도를 입력하세요 (원): "))
    except ValueError:
        print("잘못된 한도 금액입니다. 초기 예산은 0원으로 설정됩니다.\n")
        limit = 0 
    
    limit_count = 3

    while True:
        print("==== 간단 가계부 ====")
        print(f"현재 잔액: {limit} ")
        print(f"한도 초과 허용 횟수: {limit_count} (3번 허용)")
        print("0. 초과횟수 초기화")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        choice = input("선택 > ")

        if choice == "0":
            limit_count = 3
            print("한도 초과 허용 횟수가 초기화 되었습니다.\n ")
        

        elif choice == "1": 
            if limit_count == 0: 
                print("더 이상 한도를 초과하여 지출할 수 없습니다. (3번 초과 허용 횟수 소진)\n")
                continue

            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다. 숫자를 입력해주세요.\n")
                continue
            
            new_limit = limit - amount

            if new_limit < 0:
                limit_count -= 1 
                
                print(f"경고: 이번 지출로 잔액이 {new_limit}원이 됩니다. (남은 초과 허용 횟수: {limit_count}번)\n")
                
                if limit_count == 0:
                    print("주의: 한도 초과 허용 횟수를 모두 사용했습니다. 다음 지출부터는 금지됩니다!\n")
        
            budget.add_expense(category, description, amount)
            limit = new_limit
           

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
