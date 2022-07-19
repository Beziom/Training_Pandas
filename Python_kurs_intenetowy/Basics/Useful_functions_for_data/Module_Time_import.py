
import time
import datetime
from datetime import datetime

#time
#Zwracanie czasu w formie krotki - tuple
# time.struct_time(tm_year=2022, tm_mon=5, tm_mday=22, tm_hour=16, tm_min=34, tm_sec=50, tm_wday=6, tm_yday=142, tm_isdst=1)
#timestamp(), #time.asctime(), time.strftime() time.strptime(), time.sleep()
#time.pert_counter() - co ile wykonuje się jakiś kod

#Ilość sekund od 1970
ticks = time.time()
print(ticks) # 1653232488.026348 
print()

#Aktualna data
timeData = time.localtime()
print(timeData) # time.struct_time(tm_year=2022, tm_mon=5, tm_mday=22, tm_hour=17, tm_min=34, tm_sec=48, tm_wday=6, tm_yday=142, tm_isdst=1)
print()

#Odwołanie się do elementó
print(timeData.tm_year) # 2022
print()

#różnica czasu time.localtime(10) o 10 sec od 1970
timeData = time.localtime(10)
print(timeData)
print()

#Przytępna forma daty
result = time.asctime(time.localtime()) # Sun May 22 17:29:49 2022
print(result)
print()

#Zapisanie daty na swoich ("%d/%m/%Y %H:%M:%S") - time.strftime
timeData = time.localtime()
print(time.strftime("%d/%m/%Y %H:%M:%S", timeData)) # 22/05/2022 17:32:01
print()

#odczytanie danych do krotki
timeStr = "17:23:45 08.12.2021"
timeData = time.strptime(timeStr, "%H:%M:%S %d.%m.%Y") # time.struct_time(tm_year=2021, tm_mon=12, tm_mday=8, tm_hour=17, tm_min=23, tm_sec=45, tm_wday=2, tm_yday=342, tm_isdst=-1)
print(timeData)

#Uśpienie wątku (co 0,5 sekundy przez 12 iteracji będzie wyświetlany czas)
i = 0
while i<12:
    time.sleep(0.0000001) # wyświetlanie co 0.5 sec
    print(time.asctime(time.localtime()))
    i += 1

#Jak długo wykonuje się program
tStart = time.perf_counter() # wartość początkowa
time.sleep(0.5) # ile trwał kod
tEnd = time.perf_counter()# wartość końcowa
print("Code took: ", (tEnd - tStart), "seconds") #Code took:  1.2064310000278056 seconds

#czas według DateTime
datetimeObj = datetime.now()
print(datetimeObj) # 2022-05-22 18:18:08.347926

#print(dir(datetimeObj)) - do sprawdzenia funkcji

#wyświetlenie według daty
datetimeObj = datetime(2025, 3,10,22,59,59)
print("date()", datetimeObj.date()) # date() 2025-03-10
print("time()", datetimeObj.time()) # time() 22:59:59
print("timestamp()", datetimeObj.timestamp()) #timestamp() 1741643999.0 
print("today()", datetimeObj.today()) #today() 2022-05-22 18:18:08.350935

#datetimeObj.strftime
print("format: ", datetimeObj.strftime("%H:%M:%S %d.%m.%Y")) # format:  22:59:59 10.03.2025
datetimeObj = datetime.now()
print("format: ", datetimeObj.strftime("%H:%M:%S %d.%m.%Y")) # format:  18:22:29 22.05.2022

#Porównanie dat
datetime1 = datetime(2025,1,1,23,59,59)
datetime2 = datetime(2030,1,1,23,59,59)

print(datetime2 > datetime1)
print(datetime2 < datetime1)

