def open_account():
    print("새로운 계좌가 생성됐습니다.")

def deposit(balance, money):
    print(f"입금이 완료됐습니다. 잔액은 {balance+money}원 입니다.")
    return balance + money

def withdraw(balance, money): #출금
    if balance > money:
        print(f"출금 완료. 잔액은 {balance-money}원 입니다.")
        return balance - money        
    else:
        print(f"출금이 완료되지 않았습니다. 잔액은{balance}원 입니다.")
        return balance
    
def withdraw_night(balance, money): #저녁에 출금
    commission = 100 #수수로 100원
    return commission, balance-money-commission


balance = 0
balance = deposit(balance,1000)
# balance = withdraw (balance, 500)
commission, balance = withdraw_night(balance,500)
print(f"수수료는 {commission}원이며, 잔액은 {balance}원 입니다.")

