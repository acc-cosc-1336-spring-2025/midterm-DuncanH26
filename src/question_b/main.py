#add import
import question_b

def main():
 while True:

    print('1-find value tax/assessment')
    print('2-quit')

    option = (input('Enter option: '))

    if option == '1':
        value = int(input('Enter a land value: '))
        get_assessment = int(value)
        get_assets = int(value)
        print('The assessed value is', question_b.get_assessment_value(get_assessment))
        print('The tax assets value is', question_b.get_tax_assets(get_assets))
    
        
    elif option == '2':
            print('Program Exiting...')
            break
    
        
main()