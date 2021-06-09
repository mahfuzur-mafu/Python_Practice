n=8
while (n>=1):
 roll = int(input("Roll number : "))
 s1 = float(input("Subject1 Marks : "))
 s2 = float(input("Subject2 Marks : "))
 s3 = float(input("Subject3 Marks : "))
 res = s1 + s2 + s3
 avg = res / 3
 print("Student Roll: %d " % roll)
 print("Total Marks: %.2f" % res)
 print("Average Marks: %.2f" % avg)
 n=n-1