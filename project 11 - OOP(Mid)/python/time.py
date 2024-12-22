
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.fix()

    def show(self):
        print()
        print(self.hour , " : " , self.minute , " : " , self.second)    
        print()

    def sum(self,other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = Time(h_new,m_new,s_new)
        # result.fix()
        return result

    def sub(self,other):
         s_new = self.second - other.second
         m_new = self.minute - other.minute
         h_new = self.hour - other.hour
         result = Time(h_new,m_new,s_new)
        #  result.fix()
         return result

    def sec_to_time(self, total_seconds):
        houre = total_seconds // 3600
        minute = (total_seconds % 60) // 60
        second = total_seconds %60
        return Time(houre,minute,second)

    def time_to_sec(self):
        return self.hour + 3600 + self.minute + 60 + self.second

    def GMT_to_Tehran(self,houre,minute,second):
        GMT_Time = Time(houre,minute,second)
        Tehran_time = GMT_Time.sum(Time(3,30,0))
        return Tehran_time

    def fix(self):
            if self.second >= 60:
                self.second -= 60
                self.minute += 1
        
            if self.minute >= 60:
                self.minute -= 60
                self.hour += 1

            if self.second < 0:
                 self.second += 60
                 self.minute -= 1

            if self.minute < 0 :
                 self.minute += 60
                 self.hour -= 1



             



t1 = Time(3,5,17)
# t1.show()


t2 = Time(5,223,56)
# t2.show()

total_time = 33332
# currect_time = t2.sec_to_time(total_time)
# currect_time.show()

# t2.show()

seconds = t2.time_to_sec()
# print(f"Total seconds: {seconds}")


t = Time(0, 0, 0)  
tehran_time = t.GMT_to_Tehran(12, 0, 0) 
tehran_time.show() 
