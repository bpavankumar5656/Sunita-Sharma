print("Hello Sunitaji,\nGreetings of the Day to you.\nWe Welcome you to Kratins Healthcare and Solutions\nHope you are taking Good care of yourself! ")
print("\nHow could I assist you Today?")
print("Here are the following Tips and Services Provided by us....\nPlease click:-")
print("1.For your Everyday Health Chart.")
print("2.To check Your Body Mass Index(BMI) and know your health condition and Tips Required.")
print("3.To know your Daily Calorie Level Intake.")
print("4.To know whether Health checkup required or not.")
print("5.To know Schedule of your Daily Exercise/Yogasana Schedule.")
print("6.(EMERGENCY)Feeling low or Uncomfortable.")
weight =85
height=180
BMR=(weight%(height**height))

print("Here's your Everyday Health Chart \n1.Wakeup -> 6:00 am Take fresh air and have 2 Glasses of Water")
print("2.Yoga -> 6:30am -7:30am")
print("3.Breakfast -> 8:30 am")
print("4.Lunch -> Balanced Diet ->12:00am")
print("5.walk ->20 min")
print("6.Spent some time for your refreshment ")
print("7.Evening walk")
print("8.Dinner -> 7:30pm")
print("9.Walk -> 30 min")
print("10.Time for Bed->9:30 pm")
print("\n  Always Remember an Apple a Day Keeps Doctor Away\n  Have a Good Day!\n  Thanks for using Kratins Healthcare and Solutions. ")
if((BMR < 18.5)):
    print("You are underweight")
    print("Here are some healthy ways to gain weight when you're underweight:\n"
	            		+ "Eat more frequently. When you're underweight, you may feel full faster\n"
	            		+ "Choose nutrient-rich foods\n"
	            		+ "Try smoothies and shakes\n"
	            		+ "Watch when you drink\n"
	            		+ "Make every bite\n"
	            		+ "Top it off\n"
	            		+ "Have an occasional treat\n"
	            		+ "Exercise.")
elif(BMR < 25):
    print("Your are normal")
elif(BMR < 30):
    print("You are overweight")
    print("You have to Reduce your Daily CALORIE INTAKE\nCut down your SALT\nHave Some CARDIO AND WORKOUT")
else:
    print("You are obese")
    print("You have to : \n" + "Exercise more\n"+ "Move throughout the Day\n" +
	            "Look for support Groups\n"+"Eat less at Night\n"+"Choose right Supplements\n"+"Limit Added Sugar")
    print("n  Always Remember an Apple a Day Keeps Doctor Away\n  Have a Good Day!\n  Thanks for using Kratins Healthcare and Solutions.")

age=int(input())
height1=float(input())
weight1=int(input())
gender=input()
BMR = int(input())
male = bool(())
none = bool(())
light = bool(())
moderately =bool(())
intensely = bool(())
day = input()
m=len(gender)
print("What is your gender? M or F: ")
print(gender)
print("What is your age: ")
print(age)
print("What is your weight(kg): ")
print(weight1)
print("What is your height(cm): ")
print(height1)
s=gender[0]
male = gender == "M"
if(male):
    BMR = ((66 + (6.23 * weight1) + (12.7 * height1) - (6.8 * age)))
else:
    BMR = ((665 + (4.35 * weight1) + (4.7 * height1) - (4.7 * age)))
if(male):
    print("Your BMR is " + str(BMR))
else:
    print("Your BMR is " + str(BMR))
if (None):
    cal =  (BMR * 1.2)
elif (light):
    cal = (BMR * 1.375);
elif (moderately):
    cal = (BMR * 1.55)
elif (intensely):
	cal = (BMR * 1.725)
else:
    cal = (BMR * 1.9)
print("Your daily calorie needs " +str(cal))
print("\n  Always Remember an Apple a Day Keeps Doctor Away\n  Have a Good Day!\n  Thanks for using Kratins Healthcare and Solutions. ")


    
months=int(input())
print("\n In which month the Last checkup was done(1 to 12)")
chol=int(input())
print("Please Provide your Cholestrol level in mg/dl")
dbp=int(input())
sbp=int(input())
print("Enter your Diastolic and Systolic Blood Pressure (dbp and sbp)in mm Hg")
bm=int(input())
am=int(input())
Monday=input()
Tuesday=input()
Wednesday=input()
Thursday=input()
Friday=input()
Saturday=input()
Sunday=input()
print("Enter your Sugar Levels Before meal and After meal in mg/dl")
if ((months >= 3) and (chol >= 200 or dbp < 80 or sbp > 150 or bm < 70 or bm > 130 or am > 180)):
    print("\nMonths :" + str(months) + "\nCholestrol  level in mg/dl : " + str(chol) + "\nDiastolic and Systolic Blood Pressure in mm Hg \nDiastolic :" + str(dbp) + "\nSystolic :" + str(sbp) + "\nSugar Levels Before meal and After meal in mg/dl : \nBefore meal:" + str(bm) + "\nAfter meal:" + str(am) + "\nYou need to visit the doctor since the readings in the above Performed tests are not within the normal range and your last visit exceeded the time span of 3 Months")     
elif(chol >= 200 or dbp < 80 or sbp > 150 or bm < 70 or bm > 130 or am > 180):
    print("\nCholestrol  level in mg/dl : " + str(chol) + "\nDiastolic and Systolic Blood Pressure in mm Hg \nDiastolic :" + str(dbp) + "\nSystolic :" + str(dbp) + "\nSugar Levels Before meal and After meal in mg/dl : \nBefore meal:" + str(bm)+ "\nAfter meal:" + str(am)+ "\nYou need to visit the doctor since the readings in the above Performed tests are not within the normal range")
elif(months >= 3):
    print("\nYou need to visit the doctor since your last visit exceeded the time span of 3 Months \nMonths :" + str(months) )
print("\n  Always Remember an Apple a Day Keeps Doctor Away\n  Have a Good Day!\n  Thanks for using Kratins Healthcare and Solutions. ")


print("Please select Today's Day option from below list:-")
print("Monday-Press a\nTuesday-Press b\nWednesday-Press c\nThursday-Press d\nFriday-Press e\nSaturday-Press f\nSunday-Press g")

if(day=="a"):
	Day.Monday
elif(day=="b"):
    Day.Tuesday
elif(day=="c"):
	Day.Wednesday
elif(day=="d"):
    Day.Thursday
elif(day=="e"):
    Day.Friday
elif(day=="f"):
    Day.Saturday
elif(day=="g"):
    Day.Sunday
else:
    print("Please press Valid Key")
print("\n  Always Remember An Apple a Day Keeps the Doctor Away\n  Have a Good Day!\n  Thanks for using Kratins Healthcare and Solutions. ")

print("Urgently please call on the Given Contact number:-**********\nPlease be Relax>>>Our Doctor will visit your home within 10-20 minutes ")
print("\n  Always Remember an Apple a Day Keeps Doctor Away\n  Have a Good Day!\n  Thanks for using Kratins Healthcare and Solutions. ")

if Monday:
    print("Monday-You have to do Yoga for Today\n")
    print("i.Mountain Pose\r\n"
    + "\r\n"
	+ "This yoga pose helps with balance and grounding through the feet. \nStand tall with your big toes touching and heels together. Draw your abdominals in and up and relax your shoulders down and back. Breathe five to eight breaths.")
    print("\nii.Tree Pose\r\n"+"\r\n"+ "Excellent for leg and abdominal strength. Good for seniors for balance and concentration. \nStand tall and place one foot on the opposite inner thigh, either above or below the knee. Open the leg to the side, bring your hands to a prayer position and hold for five to eight breaths.")
if Tuesday:
    print("Tuesday-You have to Exercise Today\n")
    print("(a)Abdominal contractions\n"+"**To increase strength in the abdominal muscles**" +
                "\n1)Take a deep breath and tighten your abdominal muscles.\n" +
                "2)Hold for 3 breaths and then release the contraction.\n" +
                "3)Repeat 10 times")
    print("(b)Heel raises\n"+
                "**To strengthen the upper calves**\n" +
                "1)Sitting in a chair, keep your toes and the balls of your feet on the floor and lift your heels.\n" +
                "2)Repeat 20 times.")
    print("(c)Ankle rotations\n"+
                "**To strengthen the calves**\n" +
                "1)Seated in a chair, lift your right foot off the floor and slowly rotate your foot 5 times to the right and then 5 times to the left.\n" +
                "2)Repeat with the left foot")
if Wednesday:
    print("Wednesday-You have to do Yoga Today\n")
    print("i.Bird Dog\r\n"+ "\r\n"+ "Good for abdominals and back support. The health of the spine is extremely important as we age. \nStart by kneeling and stretching one arm forward and the opposite leg back. Imagine you have a tea cup on your back and draw your belly button towards your spine. Stay for a breath and then switch sides. Repeat five times. ")
	#print("nii.Downward Facing Dog\r\n"+ "\r\n"+ "This position is great for joint health, flexibility and all-over body strength. \nStart on your hands and knees, tuck your toes under and lift your hips up and back until your body forms a triangle. Use your core strength and legs to bring the weight back as much as possible. Stay for five to eight breaths, lower yourself down, and repeat two more times. For seniors with wrist issues, try the Forearm Downward Dog instead, putting your forearms flat on the mat.")
    print("\niii.Sphinx\r\n"+ "\r\n"+ "Excellent for upper back strength and preventing forward head syndrome. Sphinx is gentle and really does a great job of opening up the chest and working the rear deltoids. \nLie down on your stomach and place your forearms on the mat, elbows under your shoulders. Press firmly into your arms and draw your shoulder blades together and down your back. Lift your abdominals in and up and stay for five to eight breaths.")		
if Thursday:
    print("Thursday-You have to Exercise Today\n")
    print("(a)Shifting weight\n"+
                "1)Stand with your feet hip-width apart and your weight evenly distributed on both feet.\n" +
                "2)Relax your hands at your sides. You can also do this exercise with a sturdy chair in front of you in case you need to grab it for balance.\n" +
                "3)Shift your weight on to your right side, then lift your left foot a few inches off of the floor.\n" +
                "4)Hold for 10 seconds, eventually working up to 30 seconds.\n" +
                "5)Return to the starting position and repeat with the opposite leg.\n" +
                "6)Repeat 3 times.\n")
    print("(b)Single leg balance\n"+
                "1)Stand with your feet hip-width apart, with your hands on your hips or on the back of a sturdy chair if you need support.\n" +
                "2)Lift your left foot off of the floor, bending at the knee and lifting your heel halfway between the floor and your buttocks.\n" +
                "3)Hold for 10 seconds, eventually working up to 30 seconds.\n" +
                "4)Return to the starting position and repeat with the opposite leg.\n" +
                "5)Repeat 3 times")
if Friday:
    print("Friday-You have to do Yoga Today\n")
    print("i.Cobbler’s Pose\r\n"+ "\r\n"+ "This is a great way for seniors to keep their hips open and massage their feet. \nSit tall and bring the soles of the feet together as you open your knees out to the sides. Fold yourself forward for a deeper stretch but try to prevent rounding too much in the lower back. Hold for five to eight breaths.")
	#print("\nii.Savasana\r\n"+ "\r\n"+ "Savasana resets the nervous system and helps with restoring peace to the body and mind. \nLie on your back in final relaxation. It’s good for seniors to get comfortable with letting go more often throughout the day. Lie down and let the floor support you. Completely relax the muscles and breathe as you lie there and take a deep, restorative break.")
if Saturday:
    print("Saturday-You have to have some Stretching Today\n")
    print("i)Standing Quadriceps Stretch.\n"
				+"ii.)Seated Knee to Chest.\n"
				+ "iii.)Hamstring Stretch.\n"
				+ "iv)Soleus Stretch.\n"
				+ "v)Overhead Side Stretch.\n"
				+ "vi)Shoulder Stretch.\n"
				+ "vii)Tricep Stretch.\n"
				+ "viii)Lunge in a Chair")
    
if Sunday:
    print("It's a Rest day for you Today")