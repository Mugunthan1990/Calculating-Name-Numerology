
lt = {'a':1, 'q':1,'y':1, 'i':1, 'j' : 1,
      'b':2, 'r':2, 'k':2,
      'g':3, 'c':3, 'l':3, 's':3,
      'd':4, 'm':4,'t':4,
      'e':5, 'h':5, 'n':5, 'x':5,
      'u':6, 'v':6, 'w':6,
      'o':7, 'z':7,
      'f':8, 'p':8
      }
name = input("Enter Your Name: ")
sum = 0
#name = []
sum = 0
for na in name:
    for item in na.lower():
        #print(item)
        sum += lt[item]
    print("{0} =  {1}".format(na,sum))
    sum = 0
