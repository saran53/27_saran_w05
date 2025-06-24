# รับ parameter
'''def ชื่อฟังก์ชั่น(parameter):'''

def get_name(name):
    '''Show name fron parameter'''
    print(f"Hello !!! : {name}")
    
    def get_name(a,b):
        '''ฟังก์ชั่นบวกเลข'''
        result = a+b 
        return result
    
a = int(input())
b = int(input())
def get_name(a,b):
        '''ฟังก์ชั่นบวกเลข'''
        result = a+b 
        return result


def rect_cal(width, length):
    '''ฟังชั่นหาพื้นที่สี่เหลียมและเส้นกรอบ'''
    area = width * length
    frame = 2 * (width, length)
    return area, frame 

width = 3
length = 10

cal = rect_cal(width,length)
area = width * length
frame = 2 * (width, length)
print(f"พื้นที่สี่เหลี่ยม = {area} เส้นกรอบ = {frame}")
