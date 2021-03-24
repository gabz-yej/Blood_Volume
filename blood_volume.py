def Nadler(sex, height, weight):
	if sex == "m":
		BV = 0.3669 * height**3 + 0.03219*weight + 0.6041
	if sex == "f":
		BV = 0.3561 * height**3 + 0.03308*weight + 0.1833
	return round(BV, 3)

def Gilcher(sex, typ, height):
	IBW = height**2 * 22
	if sex == "m":
		if typ == "m":
			BV = IBW * 75 / 1e6 #/1e6 to get [l]
		elif typ == "n":
			BV = IBW * 70 / 1e6
		elif typ == "t":
			BV = IBW * 65 / 1e6
		elif typ == "o":
			BV = IBW * 60 / 1e6

	if sex == "f":
		if typ == "m":
			BV = IBW * 70 / 1e6 #/1e6 to get [l]
		elif typ == "n":
			BV = IBW * 65 / 1e6
		elif typ == "t":
			BV = IBW * 60 / 1e6
		elif typ == "o":
			BV = IBW * 55 / 1e6

	return round(BV, 3)

def TBV(sex, weight):
	if sex == "m":
		return round(weight * 75 / 1000, 3)
	if sex == "f":
		return round(weight * 65 / 1000, 3)

def Hemo(hemo, Nadler):
	hemo = hemo / 0.1 #/0.1 because [g/dl]
	return round(hemo * Nadler, 1)

def HemoEry(MCH, ery, Nadler):
	return round(MCH * ery * Nadler, 1)

print("\nThis is a programme that will estimate blood volume and mass of hemoglobine in your body!\n")
print("There are a few methods that will allow you to get these values:")
print("Nadler method - it requires inputting sex, height and weight")
print("Gilcher method - it requires inputting sex, type of body and weight")
print("TBV method (Total Blood Volume) - it requires inputting sex and weight")
print("\nIf you choose Nadler method you can also estimate mass of hemoglobine.\nIt requires putting hemoglobine or number of erythrocytes and MCH\n")
while(True):
	print("Choose which method of estimating blood volume interests you the most: \n1 - Nadler method \n2 - Gilcher method \n3 - TBV method \n0 - EXIT")
	choice1 = int(input())

	if choice1 == 1:
		print("Input sex: f - female, m - male")
		s = input()
		print("Input height using '.' as a separator [m]")
		h = float(input())
		print("Input weight using '.' as a separator [kg]")
		w = float(input())
		
		print("Blood volume in Nadler method: " + str(Nadler(s, h, w)) + " l")

		print("\nChoose if you want to go back to menu or estimating mass of hemoglobine: \n1 - using hemoglobine, \n2 - using number of erythrocytes and MCH \n0 - EXIT")
		choice2 = int(input())
		if choice2 == 1:
			print("Input hemoglobine value using '.' as a separator [g/dl]")
			hemo = float(input())
			print("Mass of hemoglobine knowing Hemoglobine: " + str(Hemo(hemo, Nadler(s, h, w))) + " g")
		elif choice2 == 2:
			print("Input erythrocytes value using '.' as a separator [mln/ul]")
			e = float(input())
			print("Input MCH value using '.' as a separator [pg]")
			MCH = float(input())
			print("Mass of hemoglobine knowing number of erythrocytes and MCH: " + str(HemoEry(MCH, e, Nadler(s, h, w))) + " g")
		elif choice2 == 0:
			print("")
		else:
			print("Wrong choice")

	elif choice1 == 2:
		print("Input sex: f - female, m - male")
		s = input()
		print("Input your body type: m - muscular, n - normal, t - thin, o - obese")
		t = input()
		print("Input weight using '.' as a separator [kg]")
		w = float(input())

		print("Blood volume in Gilcher method: " + str(Gilcher(s, t, w)) + " l")

	elif choice1 == 3:
		print("Input sex: f - female, m - male")
		s = input()
		print("Input weight using '.' as a separator [kg]")
		w = float(input())

		print("Blood volume in TBV method: " + str(TBV(s, w)) + " l")

	elif choice1 == 0:
		break

	else:
		print("Wrong choice")
