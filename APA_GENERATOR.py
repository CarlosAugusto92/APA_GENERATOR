# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#Developed by Carlos Augusto Pérez Méndez
#This app is for generate automatically the format of APA bibliography.
#When you give data, authors, edicion, date and title of the books, magazines or some information sources.
#the app will generate the apa bibliography and you just copy the informartion in your report.
#You can give the directory when you want to save the information.
#Structure: Authors, (year of publication). Title of book or magazines, paper between others. Source of information.


import subprocess



def cmd(command):
    subprocess.run(command, shell=True)

def Welcome_to_app():


    cmd('TITLE APA GENERATOR')

    print ('Welcome to APA Generator')
    print ('This app allow you print a format APA reference for books.')
    print('The format is: #Authors, (year of publication). Title of book or magazines, paper between others. Source of information. ')
    print ('For lazies persons ;P')


def get_date ():

    year_date = input()

    return year_date

def APA_Generator(name_of_authors, year_of_publication, Title_of_information, Editorial_information):

    print (name_of_authors,',', year_of_publication,'.', Title_of_information,'.', Editorial_information)


def main():

    Welcome_to_app()

    print("Entry the data for generate the text with APA format")

    print("How many authors are?:")

    i = 1

    num_of_authors = int(input())

    print ("Entry the names of the authors:")

    name_of_authors = [];

    while i <= num_of_authors:



        name_of_authors = name_of_authors + [input()];




        i = i + 1

    #print(name_of_authors) for debug

    print("Entry the date:")

    year_of_publication = get_date ()

    print ("Entry the title information:")
    Title_of_sc = input()

    print ("Entry the editorial:")

    Editorial_information = input()


    #Calling the APA generator


    APA_Generator (name_of_authors, year_of_publication, Title_of_sc, Editorial_information)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    input('Press Enter to exit[ENTER]')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
