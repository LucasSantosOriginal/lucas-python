
from time import sleep
banner = """

 _     _   _ _____  ___  _____   _____ _   _ _____ ______
| |   | | | /  __ \/ _ \/  ___| |  _  | | | |_   _|___  /
| |   | | | | /  \/ /_\ \ `--.  | | | | | | | | |    / / 
| |   | | | | |   |  _  |`--. \ | | | | | | | | |   / /  
| |___| |_| | \__/| | | /\__/ / \ \/' | |_| |_| |_./ /___
\_____/\___/ \____\_| |_\____/   \_/\_\\___/ \___/\_____/
                                                         
                                                         
                                                                                                                                                                                                                                                                                                                                                               
    """
# print ("Welcome to Lucas Quiz!")
print (banner)
# answer_user é variavel para armazenar a resposta o retorno do input
answer_user = input ("Are You Ready? (Y/N) ")

# estrutura de condicional
# != quer dizer diferente

if answer_user != "Y":
    quit()
    

score = 0
    
print("Starting...")
print("Which of those is a Last of Us character? \n (A) Walter White \n (B) Max \n (C) Franklin \n (D) Abby")
answer_1 = input ("Answer: ")

if answer_1.upper() == "D":
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("Which of those is a rapper? \n (A) Kurt Cobain \n (B) Michael Jackson \n (C) Notorius B.I.G  \n (D) Lana Del Rey")
answer_2 = input ("Answer: ")

if answer_2.upper() == "C":
    print ("Correct!")
    score += 1
else:
    print("Incorrect!")
    
sleep(1)
print (f"Game Over... Points: {score}/2")
sleep(1)
input("Press Enter to exit...")

# toda vez que atualizar o codigo py precisa ' pyinstaller --onefile quiz.py'
