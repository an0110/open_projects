import os
import datetime

_day_week 	= datetime.datetime.today().day
_month_year = datetime.datetime.today().month 

print ("zi:" + str(_day_week))
print ("luna:" + str(_month_year))


# if _day_week >=1 and _day_week <= 3:
	# print ("chirie LOWE")

# if _day_week >=1 and _day_week <= 5:
	# print ("ABONAMENT VVS"

if _day_week >=1 and _day_week <= 10:
	print ("PLATIT INTRETINERE AP 4")

if _day_week >=13 and _day_week <= 16:
	print ("TRANSMIS APA AP 4")
    
if _day_week >=5 and _day_week <= 10: 
	# if _month_year % 2 == 1:
	print ("PLATIT ENEL curent")
	print ("PLATIT RDS")
	print ("PLATIT ORANGE EDY")

if _day_week >=8 and _day_week <= 14:
	print ("TRANSMIS EON")

# if _day_week >=14 and _day_week <= 16:
	# pass
	# print (" --- de adaugat ap 24 si loc parcare 54"
	#print ("CITIT APA"
	# print ("scos bani "
	
# if _day_week >=20 and _day_week <= 25:
	# pass
	# # print ("chirie C24"
		
if _day_week >=20 and _day_week <= 28  :
	print ("se plateste VODAFONE")
	# if _month_year % 2 ==0:
	print ("TRANSMIS ENEL curent")

if _day_week >=15 and _day_week <= 21:
    print ("Transmis EON Pisu")


if _day_week >=23 and _day_week <= 30:
    print ("PLATIT EON")

if _day_week >=24 and _day_week <= 30:
    print ("PLATIT ORANGE Andrei")

# if _day_week >= 25 and _day_week <= 31:
	# print ("INTRETINERE C24"

if _day_week >= 27 and _day_week <= 29:
	print ("se plateste 1Und1")

if _month_year in [5,8,11,2] and _day_week > 5 and _day_week < 15:
    print ("de platit RADIO arf 55,08 €")

elif _day_week < 1:
	print ("really ?")

	
_input = input(" press any key to finish")
print (_input)
print ("abc")