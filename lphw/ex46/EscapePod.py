class EscapePod(Scene):
    def enter(self):
        print(dedent("""
        You run through the ship desperatedly trying 
        the escape pod before the whole ship explodes like hardly
        any Gothons are on the ship, so y clear of interference.You
        get to the chamber escape pods, and now need to pick one to take
        them could be damaged but you don't have time.There's 5pods,which one 
        do you take?
        """))
        good_pod = randint(1,5)
        guess = input("[pod #]>")
        if int(guess) != good_pod:
            print(dedent("""
            You jump into pod {guess} and hit the eject The pod escapes out
            into the void of spac implodes as the bull ruptures,crushing by jam jelly
            """))
            return 'death'
        else:
            print(dedent("""
            You jump into pod {guess} and hit the eje 
            The pod easily slides out into space head planet below.
            As it files to the planet,back and see your ship implode then 
            explode bright star,taking out hte Gothon ship a time.You won!
            """))
            return 'finished'

