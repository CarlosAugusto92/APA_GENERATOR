import os

# Menu 
def menu_app():

    print("W E L C O M E   T O   A P A  G E N E R A T O R\n")

    print('''  The APA format should be with the next format:\n

           Author names. Year of publication. Title of publication. Edition and editorial.
           for example,
            
            Pérez, C., Morales, L. (2021). Test engineering in electronics manufacturing. 1st ed. Imagine.

    ''')


# Generate the APA format.
def apa_generator(names, year, title, edition, editorial):

    apa_format = ""

    apa_format = "{}. ({}). {}. {}. {}".format(names, year, title, edition, editorial)

    output_file(apa_format)

    return apa_format

# Generate text format in a file.

def output_file(apa_format):
    
    get_path = ""

    dir_list = ""

    path = os.getcwd()
    
    print("The current directory is: {}".format(path))
    
    get_path = input("Please enter the directory under this sentence, where do you want to save this file?:\n")
    
    new_path = os.chdir(get_path)
    
    
    with open("APA_format.txt", "w") as fp:

        fp.write(apa_format)
        
        print("The file was saved in the path: {}".format(os.getcwd()))
        
        dir_list = os.listdir(new_path)

        for file in dir_list:

            print(file)


def main():
    
    author_names = "" 
    
    last_names = ""
    
    title_p = "" 
    
    edition_p = "" 
    
    editorial_p = ""

    year_p = 0 
    
    count = 1
    
    num_authors = 0

    new_names = ""
    
    #Data set for get the apa format.
    apa_data = [ 
        
        author_names, last_names, year_p, 
        title_p, edition_p, editorial_p,
    ]

    print("How many authors are?\n")

    num_authors = int(input())

    while count <= num_authors:

        apa_data[0] = input(f"Enter the name {str(count)} of author: \n")

        apa_data[1] = input(f"Enter the {str(count)} last name: \n")

        new_names = apa_data[0]

        new_names = new_names[:1]

        author_names += "{}, {}".format( apa_data[1], new_names) + " "

        count += 1

    year_p = input("Enter the year of publication: \n")

    title_p = input("Enter the title of publication: \n")

    edition_p = input("Enter the edition of publication: \n")

    editorial_p = input("Enter the editorial of publication: \n")

    print(apa_generator(author_names, year_p, title_p, edition_p, editorial_p))

    if input("Enter any key to out...\n"):

        exit()


if __name__ == "__main__":

    menu_app()

    main()