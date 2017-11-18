class TheBridge(Scene):
    def enter(self):
        print(dedent("""
        You burst onto the Bridge with the netron des under
        your arm and surprice 5 Gothons who are take control of the
        ship.Each of them has clown costume than the last.They haven't 
        pull weapons out yet,as they see the active bomb arm
        and don't want to set it off.
        """))
        action = input("> ")
        if action == "throw the bomb":
            print(decent("""
            In a panic you throw the bomb at the ground and 
            make a leap for the door.Right as your Gothon shoots
            you right int the back killing you.you die you see another Gothon
            franticall disarm the bomb.You die knowing they will blow up when             when it goes off. 
                """))
            return 'death'
        elif action == "slowly place the bomb":
            print(dedent("""
             You point your blaster at the bomb under the Gothons put their 
             hands up and start You  inch backward to the door,open it,a carefully place the bomb on the floor,po blaster at it.You then jump back through punch
             the close button and blast the lock Gothons can't get out.Now that the bomb you run to the escape pod to get off this
                """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"

