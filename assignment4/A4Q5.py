#list of lambda functions for weight conversion
converters=[
    lambda x:x*1000, #tons to kilograms
    lambda x:x*1000000,   #tons to grams
    lambda x:x*1000000000,  #tons to milligrams
    lambda x:x*2204.622622  #tons to pounds
]

#input from user in tons
tons=float(input("Enter weight in tons: "))

#applying conversions
kg=converters[0](tons)
gm=converters[1](tons)
mg=converters[2](tons)
lbs=converters[3](tons)

# Output results
print(f"{kg} kg")
print(f"{gm} gm")
print(f"{mg} mg")
print(f"{lbs} lbs")

#main code (command)
