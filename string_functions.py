def say_hello(name):
    n = str(name)
    return "Hi my name is {}".format(n)
    # takes in a name and returns the string "Hi my name is " plus the name
    # use whichever form of interpolation is most appropriate


def replace_given_substring(str_to_replace, str_to_insert, string):
    return string.replace(str_to_replace, str_to_insert)
    # this function takes three parameters --
    # the first is the substring we would like to replace.
    # the second substring is what we would like to use inplace of the first
    # the third is the actual string which we want to operate on
    # the function should return the new string


def remove_duplicate_punctuation(string):
    filtered = ""
    from string import punctuation
    punc = set(punctuation)
    for k in range(len(string)-1):
        if string[k] not in punc:
            filtered += string[k]
        if string[k] in punc:
            if string[k] != string[k+1]:
                filtered += string[k]
            else:
                filtered += ""
    return filtered + string[-1]
    # should remove all duplicate punctuation marks in a given string
    # i.e. "Hi!!!!!!" should be reformatted to "Hi!"
    # i.e. "Hello..... My name is Terrance!! How are you???" -> "Hello. My name is Terrance! How are you?"


def atdotcom(x):
    if "@" and ".com" in x:
        return True
    else:
        return False
    
def nospchx(x):
    wo_spchx = []
    special_chx = ['*','~','#','$','%','&','(',')','\`','\"',':',';','/','>','<', '!']
    for chx in x:
        if chx not in special_chx:
            wo_spchx.append(chx)
    return wo_spchx

def validate_email_format(email):
    if atdotcom(email) == True and nospchx(email) == list(email):
        return True
    else:
        return False
    # make sure the email contains an @ symbol and a .com
    # return True if format passes tests, return False otherwise


def anonymize_credit_card_number(credit_card_number):
    ccno = credit_card_number
    num_length = len(list(ccno))
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    masked = ""
    for x in ccno[0:(num_length - 4)]:
        if x in digits:
            masked +=  "X"
        else:
            masked += (str(x))
    return masked + ccno[-4:]
        