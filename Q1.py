# Checking raw_text.txt exists or not.
def check_file():
    try:
        # try opening file
        with open('raw_text.txt', 'r') as file:
            # return file content
            return file.read()
    
    except FileNotFoundError:
        # if file not found, the program exit with error.
        print('File \'raw_text.txt\' not found')
        exit(1)

# Checks user input ensuring value return as integer, if not default value 0 is returned.
def check_input(user_input):
    try:
        # return integer value if it is whole number
        if user_input.isdigit():
            return int(user_input)
        
        # converting float to int
        float_number = float(user_input)
        int_number = int(round(float_number, 0))

        print(f'User input {user_input} is converted to integer number: {int_number}\n')

        return int_number
    
    except ValueError:
        # converting words or character to integer value.

        print(f'Converting character input \'{user_input}\' to ascii value...\n')
        ascii_value = [ord(ch) for ch in user_input]
        sum_ascii = sum(ascii_value)
        if type(sum_ascii) == int:
            print(f'Character input \'{user_input}\' is converted to: {sum_ascii}\n')
            return sum_ascii
        else:
            print(f'Could not convert \'{user_input}\' to ascii value. Default value is 0\n')
            return 0

# encrypting text using keys entered by user
def text_encryption(msg, first_key, second_key):

    enc_text = ''
    to_shift = 0

    for ch in msg:
        # check single character is upper case
        if ch.isupper():
            # ch is/between upper case A and M
            if ord(ch) >= ord('A') and ord(ch) <= ord('M'):

                to_shift = first_key
                # shift backward by first entered key
                enc_text = enc_text + chr(((ord(ch) - ord('A') - to_shift) % 26) + ord('A'))

            # ch is/between upper case N and Z
            elif ord(ch) >= ord('N') and ord(ch) <= ord('Z'):

                to_shift = second_key ** 2
                # shift forward 
                enc_text = enc_text + chr(((ord(ch) - ord('A') + to_shift ) % 26) + ord('A'))

        # check single character is lower case
        elif ch.islower():
            # ch is/between lower case a and m
            if ord(ch) >= ord('a') and ord(ch) <= ord('m'):

                to_shift = first_key * second_key
                enc_text = enc_text + chr(((ord(ch) - ord('a') + to_shift) % 26) + ord('a'))

            # ch is/between lower case n and m
            elif ord(ch) >= ord('n') and ord(ch) <= ord('z'):

                to_shift = first_key + second_key
                enc_text = enc_text + chr(((ord(ch) - ord('a') - to_shift) % 26) + ord('a'))

        # space, commas, point as it is in original text
        else:
            enc_text = enc_text + ch
        
    return enc_text

def main():
    data = None

    # set file content to data
    data = check_file()
    
    # continue if data is not empty.
    try:
        if data is not None:
            first_key = check_input(input('Enter First key: '))
            second_key = check_input(input('Enter Second key: '))
        
            # encrypted text 
            text_to_write = text_encryption(data, first_key, second_key)
            # print(text_to_write)

            # creating encrypted_text.txt and writing encrypted text
            with open('encrypted_text.txt', 'w+') as file:
                print(f'\nWriting encrypted text to \'encrypted_text.txt\'')
                file.write(text_to_write)
                print(f'Done..')

    except Exception as error:
        raise error

# runs only if this python file executed.
if __name__ == '__main__':
    main()