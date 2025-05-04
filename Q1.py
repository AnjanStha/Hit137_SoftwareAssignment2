def check_file():
    try:

        with open('raw_text.txt', 'r') as file:
            return file.read()

    except FileNotFoundError:

        print('File \'raw_text.txt\' not found')
        exit(1)

def check_input(user_input):
    try:
        if user_input.isdigit():
            return int(user_input)
        
        float_number = float(user_input)
        int_number = int(round(float_number, 0))

        print(f'User input {user_input} is converted to integer number: {int_number}\n')

        return int_number
    
    except ValueError:
        print(f'Converting character input \'{user_input}\' to ascii value...\n')
        ascii_value = [ord(ch) for ch in user_input]
        sum_ascii = sum(ascii_value)
        if type(sum_ascii) == int:
            print(f'Character input \'{user_input}\' is converted to: {sum_ascii}\n')
            return sum_ascii
        else:
            print(f'Could not convert \'{user_input}\' to ascii value. Default value is 0\n')
            return 0
        
def text_encryption(msg, first_key, second_key):

    enc_text = ''
    to_shift = 0

    for ch in msg:
        if ch.isupper():

            if ord(ch) >= ord('A') and ord(ch) <= ord('M'):

                to_shift = first_key
                enc_text = enc_text + chr(((ord(ch) - ord('A') - to_shift) % 26) + ord('A'))

            elif ord(ch) >= ord('N') and ord(ch) <= ord('Z'):

                to_shift = second_key ** 2
                enc_text = enc_text + chr(((ord(ch) - ord('A') + to_shift ) % 26) + ord('A'))
        
        elif ch.islower():

            if ord(ch) >= ord('a') and ord(ch) <= ord('m'):

                to_shift = first_key * second_key
                enc_text = enc_text + chr(((ord(ch) - ord('a') + to_shift) % 26) + ord('a'))
            
            elif ord(ch) >= ord('n') and ord(ch) <= ord('z'):

                to_shift = first_key + second_key
                enc_text = enc_text + chr(((ord(ch) - ord('a') - to_shift) % 26) + ord('a'))
        
        else:
            enc_text = enc_text + ch
        
    return enc_text

def main():
    data = None

    data = check_file()
    
    try:
        if data is not None:
            first_key = check_input(input('Enter First key: '))
            second_key = check_input(input('Enter Second key: '))
            # print(first_key, second_key)

            text_to_write = text_encryption(data, first_key, second_key)

            with open('encrypted_text.txt', 'w+') as file:
                print(f'\nWriting encrypted text to \'encrypted_text.txt\'')
                file.write(text_to_write)
                print(f'Done..')

    except Exception as error:
        raise error

if __name__ == '__main__':
    main()