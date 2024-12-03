from time import sleep
print('''
Quizz Game 2024
[1] Start Game
[2] Close
''')
choice = input(': ')
if choice == '1':
    print('Ok, choose a category')
    print()
    sleep(1)
    print ('''
    [1] Movie
    [2] Music
    [3] History
    ''')
    choice = input ('Enter your answer')

    # MOVIE
    if choice == '1':
        print("""
        1 - What's the name of the actor in the first Spider-Man movie?
        
            [a] 
            [b]
            [c]
            [d]
            
        """)
        if choice == 'a':
            print('Correct!')
elif choice == '2':
    print('Game Over')
