try:
    f = open('simple.txt','r')
    f.write("Test write to simple text!"
except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")
