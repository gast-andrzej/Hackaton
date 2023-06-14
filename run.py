import Letter.API
import chat.API
from chat import API
from Letter import API

def run():
    while True:
        print("Welcome to the system prepared by Andrzej Gast for Mavoie. \nA system that will make it easier for you to find yourself on the modern labor market \nand build your self-confidence before recruitment interviews :)")
        choicer = input('choose what you are interested in, whether it is: \n1. preparation of a cover letter \nor \n2. trial job interview (enter the appropriate number)\n')
        try:
            int(choicer)
            choice = int(choicer)
            try:
                if choice>0 and choice<3:
                    match int(choicer):
                        case 1:
                            Letter.API.runnex()
                        case 2:
                            chat.API.runnex()
                else:
                    print('Not implement yet')
            except:
                print('Not implement yet')
        except:
            print('Please, write number ;)')