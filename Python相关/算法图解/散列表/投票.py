voted = {}

def check_voter(name):
    if voted.get(name):
        print ("Back OFF!")
    else:
        voted[name] = True
        print("LET THEM VOTE!!!!!")

