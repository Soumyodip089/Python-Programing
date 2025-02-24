#4.Write a python program to convert a number entered by the user into its corresponding number in words.

def num_to_words(num):
    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if num < 10:
        return units[num]
    elif num < 20:
        return teens[num-10]
    elif num < 100:
        return tens[num//10] + ('' if num%10==0 else ' ' + units[num%10])
    elif num < 1000:
        return units[num//100] + ' hundred' + ('' if num%100==0 else ' and ' + num_to_words(num%100))
num = int(input("Enter a number: "))
print(num_to_words(num))
