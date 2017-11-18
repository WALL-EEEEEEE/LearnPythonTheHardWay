class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
        The Gothons of Planet Percal #25 have invaded desctoryed your entire crew.You are the last smember and your last mission is too get the neubomb from the Weapons Armory, put it in the br blow the ship up after getting into an escape
        You're running down the central corridor to the Armory when a Gothon jumps out,red scaly skin teeth,and evil clown costume flowing around hfilled body.H's blocking the door to the Armory about to pull a weaon to blast you.
        """))
        action = input(">")
        if action == "shoot!":
            print(dedent("""
            Quick on the draw you yank out your blaste it at the Gothon.His clown costume is flo Your laster hits his costume but misses him.This completely ruins his brand new costume bought him,which makes him fly into an in and blast you repeatly in the face util dead. Then he eats you. 
            """))
            return 'death'
        elif action == "dodge!":
            print(dedent("""
            Like a world class boxer you dodge,weave,slide right as the Gothon's blaster cranks past your head.In the middle of your arti your foot slips and you bang your head on wall and pass out. You wake up shortly afer die as the Gothon stomps on you head
            """))
            return 'death'
        elif action == 'tell a joke':
            print(dedent(
                """
                Lucky for you they make you learn Gothon in the academy.You tell the one Gothon joke Lbhe zbgure vf fb sng, jura fur fvgf nebha
                fur fvgf nebhaq gur ubhfr.The Gothon stop not to laugh,then 
                busts out laughing and While he's laughing you run up and shoot the head putting him down, then  jump through Weapon Armory door.
                """
                ))
            return 'laster_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central corridor'
