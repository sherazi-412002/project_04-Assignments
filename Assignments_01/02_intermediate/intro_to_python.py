
# defining gravity constants
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889 
MARS_GRAVITY = 0.378 
JUPITER_GRAVITY = 2.36 
SATURN_GRAVITY = 1.081 
URANUS_GRAVITY = 0.815 
NEPTUNE_GRAVITY = 1.14 
EARTH_GRAVITY = 1.0


def main():

    print("\nFinding Weight On different planet with respect to earth!")
    print("---------------------------------------------------------")
    earth_weight = int(input("Enter a weight : "))
    while True:
        planet = input("Enter a planet : ").strip().lower()
        gravity_constant = 0
        match planet:
            case "mercury":
                gravity_constant = MERCURY_GRAVITY
            case "venus":
                gravity_constant = VENUS_GRAVITY
            case "mars":
                gravity_constant = MARS_GRAVITY
            case "jupiter":
                gravity_constant = JUPITER_GRAVITY
            case "saturns":
                gravity_constant = SATURN_GRAVITY
            case "uranus":
                gravity_constant = URANUS_GRAVITY
            case "neptune":
                gravity_constant = NEPTUNE_GRAVITY
            case "earth":
                gravity_constant = EARTH_GRAVITY
            case _:
                print("Enter a valid planet name.")

        if gravity_constant != 0:

            planetory_weight = earth_weight * gravity_constant
            rounded_planetory_weight = round(planetory_weight,2)
            print(f"The Equivalent Weight on {planet} is {rounded_planetory_weight}")

            break

        


if __name__ == "__main__":
    main()