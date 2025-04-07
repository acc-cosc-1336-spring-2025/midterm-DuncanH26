#add import
import question_d

def main():

    Kilometers = int(input('Enter Kilometers: '))
    Minutes = int(input('Enter minutes: '))

    print('The answer in mph is', question_d.get_miles_per_hour(Kilometers, Minutes))

main()