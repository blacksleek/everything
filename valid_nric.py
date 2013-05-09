import re

def valid_nric(self):
    validation = re.compile("^[sStTfFgG][0-9]{7}[a-zA-Z]$")
    if validation.match(self):
        number = int(self[1] * 2 + self[2] * 7 + self[3] * 6 + self[4] * 5 + self[5] * 4 + self[6] * 3 + self[7] * 2)
        number = number % 11
        number = 11 - number
        if number == 10:
            if self[-1] == "a" or self[-1] == "A":
                return "Valid NRIC."
            else:
                return "Invalid NRIC."
        if number == 9:
            if self[-1] == "b" or self[-1] == "B":
                return "Valid NRIC."
            else:
                return "Invalid NRIC."
        if number == 8:
            if self[-1] == "c" or self[-1] == "C":
                return "Valid NRIC."
            else:
                return "Invalid NRIC."
        if number == 7:
            if self[-1] == "d" or self[-1] == "D":
                return "Valid NRIC."
            else:
                return "Invalid NRIC."
        if number == 6:
            if self[-1] == "e" or self[-1] == "E":
                return "Valid NRIC."
            else:
                return "Invalid NRIC."
        if number == 5:
            if self[-1] == "f" or self[-1] == "F":
                return "Valid NRIC."
            else:
                return "Invalid NRIC."
        if number == 4:
            if self[-1] == "g" or self[-1] == "G":
                return "Valid NRIC."
            else:
                return "Invalid NRIC."
        if number == 3:
            if self[-1] == "h" or self[-1] == "H":
                return "Valid NRIC."
            else:
                return "Invalid NRIC."
        if number == 2:
            if self[-1] == "i" or self[-1] == "I":
                return "Valid NRIC."
            else:
                return "Invalid NRIC."
        if number == 1:
            if self[-1] == "z" or self[-1] == "Z":
                return "Valid NRIC."
            else:
                return "Invalid NRIC."
        if number == 0:
            if self[-1] == "j" or self[-1] == "J":
                return "Valid NRIC."
            else:
                return "Invalid NRIC."
        else:
            return "Invalid NRIC."
            
    else:
        return "Invalid NRIC."

while True:
    nric = input("Enter NRIC: ")
    print(valid_nric(nric))
