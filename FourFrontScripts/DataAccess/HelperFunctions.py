'''
Takes in a string and replaces all months with their corresponding number value
Returns a string containing the original words separated by spaces.
'''
def formatMonths(fullString):
    result = ""
    words = fullString.split()
    for w in words:
        if w == 'JAN' or w == 'JANUARY':
            w = '1'
        elif w == 'FEB' or w == 'FEBRUARY':
            w = '2'
        elif w == 'MAR' or w == 'MARCH':
            w = '3'
        elif w == 'APR' or w == 'APRIL':
            w = '4'
        elif w == 'MAY':
            w = '5'
        elif w == 'JUN' or w == 'JUNE':
            w = '6'
        elif w == 'JUL' or w == 'JULY':
            w = '7'
        elif w == 'AUG' or w == 'AUGUST':
            w = '8'
        elif w == 'SEP' or w == 'SEPTEMBER':
            w = '9'
        elif w == 'OCT' or w == 'OCTOBER':
            w = '10'
        elif w == 'NOV' or w == 'NOVEMBER':
            w = '11'
        elif w == 'DEC' or w == 'DECEMBER':
            w = '12'
            
        result += w
        result += " "
        
    return result
