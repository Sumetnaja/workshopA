# 5.จงเขียนโปรแกรม Python คำนวนหาเงินเดือนสุทธิของพนักงาน แล้วแสดงผลทางหน้าจอ โดยรับค่ารหัสพนักงาน ชื่อพนักงาน 
# และเงินเดือนปกติของพนักงานทางแป้นพิมพ์ ทั้งนี้เงินเดือนสุทธิของพนักงานนั้นจะต้องหักค่าภาษี และเบี้ยประกันสังคมออกจากเงินเดือนปกติเสียก่อน 
# โดยที่พนักงานต้องเสียภาษี 7% ของเงินเดือนปกติ และจ่ายค่าเบี้ยประกันสังคม 500 บาท 
# สูตร เงินเดือนสุทธิ  =  เงินเดือนปกติ  -(เงินเดือนปกติ * 7 / 100) -500

def inputData ( ) :
    employ_num = float( input('ป้อนรหัสพนักงาน : ') )
    employ_name = input('ป้อนชื่อพนักงาน : ')
    employ_money = float( input('ป้อนเงินเดือนปกติ : ') )
    return employ_num, employ_name, employ_money

def calTax ( employ_money ) :
    employ_aftax = employ_money * 7 / 100
    return employ_aftax

def BeaPraGun ( ) :
    PraGun = 500
    return PraGun

def calSutti ( employ_aftax, PraGun ) :
    sutti = employ_aftax - PraGun
    return sutti

def showPaSeeandSutti ( employ_aftax, sutti ) :
    print(f'ภาษีเป็นเงิน : {employ_aftax:.2f} บาท')
    print(f'เงินเดือนสุทธิเป็นเงิน : {sutti:.2f} บาท')

print('----------------------------')
print('-----คำนวณเงินเดือนพนักงาน-----')
print('-----------------------------')
employ_num, employ_name, employ_money = inputData( )
employ_aftax = calTax( employ_money )
PraGun = BeaPraGun( )
sutti = calSutti( employ_aftax, PraGun)
print('----------------------------')
showPaSeeandSutti( employ_aftax, sutti)
print('-----------------------------')