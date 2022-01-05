x=0
while x!=3:
    q1 = input(f"What phrase best describes your personality?\n\t A. Motivated perfectionist\n\t B. Motivated completionist\n\t C. Unmotivated perfectionist\n\t D. Unmotivated Completionist\n(Input your answer)\t")
    if q1.upper() in ["A", "B", "C", "D"]:
        q2 = input("What word best describes your attitude in a stressful situation?\n\tA. Frustrated\n\tB. Collected\n\tC. Nervous\n\tD. Reserved\n(Input your answer)\t")
        if ((q1.upper() in ["A", "B"]) and (q2.upper() in ["B", "D"])):
            print("You're awesome.")
            x+=3
            break
        elif ((q1.upper() in ["C", "D"]) and (q2.upper() in ["A", "C"])):
            print("I can't believe you picked these answers.")
            x+=3
            break
        elif ((q1.upper() in ["A" or "B"]) and (q2.upper() in ["A", "C"])) or ((q1.upper() in ["C", "D"]) and (q2.upper() in ["B", "D"])):
            print("You're a confounding individual.")
            x+=3
            break
        else:
            print("2 The information we received was not on the menu. Please restart the program and try again.")
            x+=3
            break
    else:
        print("1 The information we received was not on the menu. Please restart the program and try again.")
        x+=3
        break
