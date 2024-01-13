LIGHT_SPEED = 300_000_000

mass_kg = int(input("Mass in kg: "))

energy = mass_kg * pow(LIGHT_SPEED, 2)

print(f"The energy in Joules is: {energy}")
