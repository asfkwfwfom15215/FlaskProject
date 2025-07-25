#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} 유닛이 생성됐습니다.")

    def move(self, location):
        print("지상 유닛 이동")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴됐습니다.")
        

#공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
    
    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

#마린

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    #스팀팩 : 일정 시간 동안 공격 속도를 증가

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10감소)")
        
        else:
            print(f"{self.name} : 체력이 부족해서 스팀팩을 사용하지 않습니다.")


class Tank(AttackUnit):
    #시즈모드 : 더 높은 파워로공격가능 , 이동불가. 지상에고정정
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__("탱크", 200, 30, 50)
        self. set_seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return 
        
        #현재 시즈모드가 아닐 때
        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *= 2
            self.set_seize_mode = True
        
        #현재 시즈모드 일때 
        else:
            print(f"{self.name} : 시즈모드로 해제합니다.")
            self.damage /= 2
            self.set_seize_mode = False

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name, hp, damage)
        Flyable.__init__(self, flying_speed)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__("레이스", 80, 20,5)
        self.clocked = False #클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True:
            print(f"{self.name} : 클로킹 모드를 해제합니다.")
            self.clocked = False
        else:
            print(f"{self.name} : 클로킹 모드 설정합니다.")
            self.clocked = True


