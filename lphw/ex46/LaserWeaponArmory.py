class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
        You do a dive roll into the Weapon Armory,cr
        the room for more Gothons that might be hiding
        quiet,too quiet.You stand up and run to the the room
        and find the neutron bomb in its condition
        There's a keypad lock on the box and you need get the bomb out.
        If you get the code wrong,the lock closes foreaver and you can't 
        get the code is 3 digits.
        """))
        code = f"{randint(1,9)}{randint(1,9){randint(1,9)}}"
        guess = input("[keypad]>")
        guesses = 0
        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]>")
        if guess == code:
            print(dedent("""
            The container clicks open and the seal br gas out.
            Yuo grab the neutron bomb and ru you can to the bridge where you must
            place right spot
            """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock  buzzes one last time and then you sickening melting sound as the mechanism together.You decide to sit there,and fit Gothons blow up the ship from their ship
            """))
            return 'death'
