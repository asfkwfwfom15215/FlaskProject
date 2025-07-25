class Unit:
    def __init__(self, name, hp, damage): #생성자 == 객체가 만들어질때 자동으로 실행되는것
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성됐습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)


#marine1은 객체, marine1은 Unit클래스의 인스턴스

#레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지않음)(스텔스모드)

wraith1 = Unit("레이스", 80, 5)
print(f"유닛이름 : {wraith1.name}, 공격력 {wraith1.damage}")

#마인드 컨트롤 : 상대방 유닛을 내것으로 만드는것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True
#객체에 추가로 변수를 외부에서 만들어서 쓸 수 있다.
#단, 이 clocking변수는 wraith1에는 없는 멤버변수이다.

if wraith2.clocking == True:
    print(f"{wraith2.name} 는 현재 클로킹 상태입니다.")
