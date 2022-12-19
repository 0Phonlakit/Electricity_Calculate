#โปรแกรมสำหรับคำนวณค่าไฟ
class CalculateElectricity:
    def __init__(self) :
        self.num = 0
        self.lise_of_ele = []

    def electric_equipment(self) :
        self.num = int(input("Enter a number of electric equipment : "))  #รับ input ชนิดของเครื่องใช้ไฟฟ้า
        self.lise_of_ele = []
        for i in range (self.num) :
            ele_equipment = input("Enter a electric equipment : ")        #รับ input เป็นชื่อของเครื่องใช้ไฟฟ้า
            num_ele = int(input("Enter a number of electrical : "))       #รับ input เป็นจำนวนของเครื่องใช้ไฟฟ้า
            ele_power = float(input("Enter a electric power (w) : "))     #รับ input เป็นกำลังไฟฟ้าซึ่งมีหน่วยเป็น watt
            time = float(input("Enter a time (hour): "))                  #รับ input เป็นเวลาในหน่วยของชั่วโมง
            self.lise_of_ele.append([ele_equipment, num_ele ,ele_power, time]) #เก็บค่าต่างๆ ไว้เป็น list
        return self.lise_of_ele
    
    def calculate_unit(self) :
        total = 0
        for j in range (self.num) :
            cal_unit = ((float(self.lise_of_ele[j][1]) * float(self.lise_of_ele[j][2]) / 1000) * float(self.lise_of_ele[j][3])) #คำนวณจำนวน Unit ของเครื่องใช้ไฟฟ้า
            total += cal_unit                            #รวม Unit ที่ใช้ไปเป็นเวลา 1 วัน 
        self.total_unit =  total*30                      #รวม Unit ที่ใช้ไปเป็นเวลา 1 เดือน
        return self.total_unit
    
    def electricity_cost(self) :
        period_1 = 3.2484
        period_2 = 4.2218
        period_3 = 4.4217   
        if self.total_unit >= 400 :                             #หาก Unit มีค่ามากกว่าหรือเท่ากับ 400 จะคำนวณค่าไฟที่ใช้ในส่วนนี้
            self.ele_cost = (150 * period_1) + (250 * period_2) + ((self.total_unit - 400) * period_3) 
        elif self.total_unit < 400 : #หาก Unit มีค่าน้อกว่า 400 แต่ไม่เกิน 150 จะคำนวณค่าไฟที่ใช้ในส่วนนี้
            self.ele_cost = (150 * period_1) + ((self.total_unit - 250 ) * period_2)
        elif self.total_unit > 150 :                          #หาก Unit มีค่ามากว่า 150 แต่น้อยกว่า 400 จะคำนวณค่าไฟที่ใช้ในส่วนนี้
            self.ele_cost = (150 * period_1) + ((250 - self.total_unit) * period_2)
        else :                                                    #หาก Unit มีค่าน้อยกว่า 150 จะคำนวณค่าไฟที่ใช้ในส่วนนี้
            self.ele_cost = ((150 - self.total_unit) * period_1)
        return self.ele_cost
    
    def float_time(self) :
        self.ft = 0.9343 
        self.tal_ft = self.total_unit * self.ft    #นำค่า ft * กับ unit เพื่อหาค่า ft ที่ต้องจ่าย
        return self.tal_ft
    
    def electricity_price(self) :
        service_charge = 38.22
        vat = 107/100
        self.cost = ((self.ele_cost + service_charge + (self.tal_ft / 100)) * vat ) #คำนวณค่าไฟโดยนำค่า self.ele_cost + service_charge + self.tal_ft / 100 แล้วไป * vat
        return self.cost

    def total_current(self) :
        system_volt = 220
        self.tal_cur = self.total_unit / system_volt   #หากระแสไฟฟ้าที่ใช้ไปเป็นหน่วย Ampere
        return self.tal_cur
    
    def show_bill(self) :
        print ("________________________________________________")
        print ("|                                              |")
        print ("|               ElectricityBill                |")
        print ("|                                              |")
        print ("________________________________________________")
        print ("|                                              |")
        print ("|  ใช้ไฟฟ้าเป็นจำนวน           : %.2f   Unit   |"%(self.total_unit))
        print ("|  กระแสไฟฟ้าที่ใช้             : %.2f     A     |"%(self.tal_cur))
        print ("|  ค่า ft                    : %.4f  Bath |"%(self.ft))
        print ("|  ค่า ft รวม                 : %.4f  Bath   |"%(self.tal_ft))
        print ("|  ใช้ไฟฟ้าไป                 : %.2f  Bath  |"%(self.ele_cost))
        print ("|                                              |")
        print ("|                                              |")
        print ("|ราคาค่าไฟที่ต้องชำระ (รวม vat) : %.2f   Bath   |"%(self.cost))
        print ("|                                              |")
        print ("| Thank You                                    |")
        print ("________________________________________________")

           
bill = CalculateElectricity()
bill.electric_equipment()
bill.calculate_unit()
bill.electricity_cost()
bill.float_time()
bill.electricity_price()
bill.total_current()
bill.show_bill()

#reference
# https://www.tpe-trading.com/electric-bill/
# https://www.mea.or.th/download/view/304933