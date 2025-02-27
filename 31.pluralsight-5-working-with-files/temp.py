acronym = input('What acronym do you want to add?\n')
definition = input('What is the definition? \n')

with open('31.pluralsight-5-working-with-files/input.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')