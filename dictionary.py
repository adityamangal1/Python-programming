adi = {"aditya":"mangal","dipanshu":"goyal"}

adi["ankush"] = "chauhan"
adi["rahul"] =  "gaur"
adi[100] = "corrupts"
adi["police"] = "corrupts"
print(adi.items())
print(adi.keys())

del adi["ankush"]
print(adi)
del adi["rahul"]
print(adi)

# adi2 = adi.copy()
# del adi2["ankush"]

# print(adi2)

# del adi["aditya"]
# print(adi)
# del adi["dipanshu"]
# print(adi)
# del adi["ankush"]
# print(adi)


# d1 = {}
# print(type(d1))