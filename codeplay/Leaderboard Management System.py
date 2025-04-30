import random
def display(l,purpose):
    print('LeaderBoard'.center(30,'-'),'-',purpose)
    for i,val in enumerate(l):
        print(i+1,"-",val)
l=[]
print("Results of your game")
while True:
    print("1.Create a Leaderboard:")
    print("2.Add Multiple Players:")
    print("3.Add a Single Player:")
    print("4.Remove a Player:")
    print("5.Find a Player:")
    print("6.Sort the Leaderboard:")
    print("7.Check the Leaderboard:")
    print("8.Tie Break:")
    print("9.Top Players:")
    print("10.Least Players:")
    print("11.Score Division:")
    print("12.Clear Leaderboard:")
    print("13.Exit:")
    ch=int(input("Enter the choice:"))
    if ch==1:
       n=int(input("Enter the no of players:"))
       l=[random.randint(1,5)*100 for i in range(n)]
       display(l,'Create a Leaderboard')
    elif ch==2:
        n=int(input("Enter how many players you want to add:"))
        new=[random.randint(1,5)*100 for i in range(n)]
        l.extend(new)
        display(l,'Add Multiple Players')
    elif ch==3:
        score=int(input("Enter the score of single player:"))
        l.append(score)
        display(l,'Add a Single Player')
    elif ch==4:
        display(l,'Select the index to remove that player')
        index=int(input("Enter index:"))
        l.pop(index)
        display(l,'Remove a Player')

    elif ch==5:
        index = int(input("Enter the index to find the player: "))
        if 0 <= index < len(l):
         print(f"Player at index {index} has score: {l[index]}")
        else:
         print("Invalid index. Please enter a valid index.")

    elif ch==6:
        print("1.Highest to Lowest")
        print("2.Lowest to Highest")
        op=int(input("enter the choice:"))
        if op==1:
            sorted(l)
            display(l,'Sort the Leaderboard')
        elif op==2:
            k=sorted(l)[::-1]
            display(k,'Sort the Leaderboard')
        else:
            break

    elif ch==7:
        display(l,'Check the Leaderboard')
    elif ch==8:
        print("Tie Break - Players with the same score:")
        found = False
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if l[i] == l[j] and i != j:
                    print(f"Player at index {i} and Player at index {j} have the same score of {l[i]}")
                    found = True
        if not found:
            print("No tie found in the leaderboard.")

    elif ch==9:
        n = int(input("Enter how many top players to display: "))
        top_players = sorted(l, reverse=True)[:n]
        print("Top n Players:")
        for i in range(len(top_players)):
            print(i + 1, "-", top_players[i])

    elif ch==10:
    
        n = int(input("Enter how many least players to display: "))
        least_players = sorted(l)[:n] 
        print("Lowest", n, "Players:")
        for i in range(len(least_players)):
            print(i + 1, "-", least_players[i])

    elif ch == 11:    
        gold = []
        silver = []
        bronze = []

        for score in l:
            if score > 400:
                gold.append(score)
            elif score >= 250:
                silver.append(score)
            else:
                bronze.append(score)

        print("Gold (Above 400):", gold)
        print("Silver (250 to 400):", silver)
        print("Bronze (Below 250):", bronze)

    elif ch==12:
         l = []
         print("Leaderboard cleared successfully!")

    elif ch==13:
    
        print("Exiting... Goodbye!")
        break
    else:
      print("Invalid option")
