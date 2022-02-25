import re
# storing data
class SaveX:
    # Constructor
    def __init__(self):
        self.email = list()
        self.ps = list()
        self.dic = list()

    # Save The Email and Password in List
    def savex(self, email, ps):
        self.email.append(email)
        self.ps.append(ps)
        self.dic.append(list((email, ps)))

        r.put_txt(self.dic)  # Calling Method for Saving E-mail and Password in .txt File
        # print(self.dic)

    # Return Forget Password
    def fg(self, email):
        db = self.dic
        t1 = list()
        t2 = list()
        temp = None
        for i in range(len(db)):
            t1.append(db[i][0])
            t2.append(db[i][1])

        # {Checking Whether E-mail is in the .txt File or not} and {If it in File then Password can be Retrieved}
        for i in range(len(t1)):
            if t1[i] == email:
                temp = t2[i]
        print("Password for the Email: {} is \'{}\'\n\n".format(email, temp))

    # Return Whole Data
    def trans(self):
        temp = r.get_txt()
        for i in temp:  # Extracting Data of E-mail and Password from .txt File
            self.dic.append(i)
        return self.dic

    # Save Email and Password in Text File Using File Handling
    def put_txt(self, dic):
        p = open("database.txt", 'a')
        for i in dic:  # Append the New E-mail and Password in .txt File in Separate Line Wise
            for j in i:
                p.write(j + '\n')
        p.close()
        print("Credentials Successfully Stored in Database\n\n")

    # Retrieve Email and Password in Text File Using File Handling
    def get_txt(self):
        file_obj = open("database.txt", 'r')
        x = list()
        lines = file_obj.readlines()  # Read Total No. of lines in the File
        for i in lines:  # Converting Each line to the Element of List
            x.append(i.strip('\n'))
        yy = list()
        for i in range(0, len(x), 2):
            y = list()
            y.append(x[i])  # Converting Couple of lines to List
            y.append(x[i + 1])
            yy.append(y)  # Converting Above Converted List to a List of Lists
            # print(yy)
        file_obj.close()
        return yy


# Define Class for Checking E-mail and Password
class Validation:

    # Constructor
    def __init__(self):
        self.email = None
        self.ps = None
        self.fe = True
        self.fp = True

    # Method for Getting E-mail and Password
    def gett(self):
        print("Enter Email:", end=" ")
        self.email = input()
        print("Enter password:", end=" ")
        self.ps = input()

    # Method for Validating Email and Password
    def check(self):
        rex = r'^\b[A-Za-z0-9]+1[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'  # Regular Expression foe E-mail
        s_symb = ['.', '!', '@', '#', '$', '%', '^', '&', '*']

        if re.fullmatch(rex, self.email):  # Validating Email with Regular Expression
            print("Valid Email\n\n")
            self.fe = True
        else:
            print("Invalid Email\n\n")
            self.fe = False

        # Validating Password Conditions
        if len(self.ps) > 0:
            if (len(self.ps) < 6) and (len(self.ps) > 15):
                print('Length Should in the Range of 5 to 15 Character length\n\n')
                self.fp = False
            if not any(char.isdigit() for char in self.ps):
                print('Password Should have At Least One Numeral\n\n')
                self.fp = False
            if not any(char.isupper() for char in self.ps):
                print('Password Should have At Least One Uppercase Letter\n\n')
                self.fp = False
            if not any(char.islower() for char in self.ps):
                print('Password Should have At Least One Lowercase Letter\n\n')
                self.fp = False
            if not any(char in s_symb for char in self.ps):
                print('Password Should have At Least One of the Symbols ., !, @. #, $, %, ^, &, *\n\n')
                self.fp = False

            if self.fp is True:
                print("Valid Password\n\n")
            else:
                print("Invalid Password\n\n")

        if self.fe is True and self.fp is True:  # Save the Data Only If Both E-mail and Password were Valid
            r.savex(self.email, self.ps)

    # Method for Verify the Email and Password
    def logchk(self, email, ps):
        t = r.trans()  # Calling A Method for Extracting Data of E-mail and Password from .txt File
        for i in range(len(t)):
            if t[i][0] == email:  # Verify Email And Password with the Data E-mail and Password Stored in the .txt File
                if t[i][1] == ps:
                    print("Login Successful\nCredentials Matches with Database\n\n")
                    break
                else:
                    print("Login Failed\nPassword Credential Does Not Match with Database\nEnter Correct Password\n\n")
                    print("Forget Password Chose Option: 3")
                    break
            else:
                print("Email Does not Register\nPlease Register Your Email Using Option 1\n\n")


q = Validation()
r = SaveX()

while True:
    # Select option for below Mentioned Process
    print("Select the Option:\n 1-Registration \n 2-Login \n 3-Forget Password \n 4-Exit\n\n")
    op = int(input())
    if op == 1:  # Registration
        q.gett()  # Calling Method to Get E-mail and Password
        q.check()  # Calling Method for Validating E-mail and Password
    elif op == 2:  # Login
        print("Login\n\n")
        print("Please Enter E-mail\\Username:", end=" ")
        email = input()
        print("Please Enter Password:", end=" ")
        ps = input()
        q.logchk(email, ps)  # Calling Method for Verifying E-mail and Password
    elif op == 3:  # Forget Password
        print("Recovering Password\n\n")
        print("Enter E-mail for Recovery ", end=" ")
        e = input()
        r.fg(e)  # Calling Method for Recovering Password for Corresponding E-mail
    elif op == 4:  # Exit
        break
