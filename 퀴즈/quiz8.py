class House:
    #매물 초기화 
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    #매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type\
            , self.price, self.completion_year)
    

h = []
h1 = House("강남", "아파트", "매매", "10억", "2010년년")
h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
h3 = House("송파", "빌라", "월세", "500/50", "2000년")

h.append(h1)
h.append(h2)
h.append(h3)

print(f"총 {len(h)}대의 매물이 있습니다.")
for house in h:
    house.show_detail()





