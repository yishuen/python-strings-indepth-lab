def say_hello(name):
    # takes in a name and returns the string "Hi my name is " plus the name
    # use whichever form of interpolation is most appropriate
    return f"Hi my name is {name}"

def replace_given_substring(str_to_replace, str_to_insert, string):
    # this function takes three parameters --
    # the first is the substring we would like to replace.
    # the second substring is what we would like to use inplace of the first
    # the third is the actual string which we want to operate on
    # the function should return the new string
    return string.replace(str_to_replace, str_to_insert)

def remove_duplicate_punctuation(string):
    # should remove all duplicate punctuation marks in a given string
    # i.e. "Hi!!!!!!" should be reformatted to "Hi!"
    # i.e. "Hello..... My name is Terrance!! How are you???" -> "Hello. My name is Terrance! How are you?"
    string_list = string.split(" ")
    new_string = []
    for word in string_list:
        new_string.append(remove_excess(word))
    return " ".join(new_string)

def remove_excess(word):
    punctuation = [".", "?", "!"]
    for element in punctuation:
        count = word.count(element)
        if count > 1:
            word = word.replace(element, "", (count - 1))
    return word


def validate_email_format(email):
    # should make sure there are no special characters (i.e. *,~,#,$,%,&,(,),`,",',:,;,/,>,<)
    # make sure the email contains an @ symbol and a .com
    # return True if format passes tests, return False otherwise
    if email.count('@') > 1:
        return False
    email_list = email.partition("@")
    email_name = email_list[0]
    email_ending = email_list[2]
    if not special_characters(email_name):
        return False
    elif not email_ending.endswith('.com'):
        return False
    elif email_list[1] != '@':
        return False
    else:
        return True


def special_characters(word):
    chars = ["*", "~", "#", "$", "%", "&", "(", ")", "`", '"', "'", ":", ";", "/", ">", "<"]
    for char in chars:
        if word.count(char) > 0:
            return False
    return True

def anonymize_credit_card_number(credit_card_number):
    # should replace all characters except the last 4 with 'X'
    # return the anonymized credit card number as a string
    # the credit card may have characters that are not numbers (i.e. spaces and dashes, which we would want to keep)
    # i.e. 1234-5678-90-1234 -> XXXX-XXXX-XX-1234
    new_string = ""
    for char in credit_card_number[:-4]:
        if char.isnumeric():
            new_string = new_string + "X"
        else:
            new_string = new_string + char
    return new_string + credit_card_number[-4:]
