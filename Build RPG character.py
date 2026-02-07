full_dot = '●'
empty_dot = '○'
def create_character(name,strength,intelligence,charisma):
    if type(name) !=str:
        return "The character name should be a string"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if type (strength or intelligence or charisma) != int:
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if (strength + intelligence + charisma )< 7:
        return " The character should start with 7 points"
    return ( "/n (name ) /n (STR  strength = full_dot empty_dot = [strength:10]  /n INT intelligence = full_dot empty_dot = [intelligence:10] /n CHA charisma = full_dot empty_dot = [charisma:10] ")
    

    

print (create_character("ren",4,2,1))