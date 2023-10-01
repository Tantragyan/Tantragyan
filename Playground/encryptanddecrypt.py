original_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.;:'!@#$%^&*()_+~`="
cipher_table = ["@PS%8GEU:7@M0WBX`,W%)&9WIXP(&@~`'3@_#2)T~8, 4F8O+,T$*MX.;" ,
                "(VKK*B;&A,OAGO+6=@(81O8%'2RO:`FPQN*TBG66HGAJ``=KEH.RN6*Q$" ,
                "O+M;ZQ2X2I$LM$P6*P(,6Z UCXK%UN^~ZH.%@,&4.'N``DF)8N*X9A.*(" ,
                "S,BP;&9P44M*=X(DRYU :$*:Y518CBNZQ(;UKGLJ1:OB%7&A&ZEP%JVLK" ,
                "K^I#Q$O)`I@9L;0_`'TKPIQZYM0^'%H1'KW X1_X_',6TUOGTL3 *K$1," , ]
choice = input("Would you like to encrypt or decrypt? ")

def welcome():
    print("Welcome to this very interesting encryption program!")
def encrypt_char(char, cipher_index):
    original_index = original_alphabet.index(char)
    if cipher_index > 4:
        cipher_index = 0
    #print(original_index)
    index = cipher_table[cipher_index][original_index]
    #print(index)
    return index
#encrypt_char("H", 0)
def encrypt(string):
    global encrypted_string
    encrypted_string = ""
    string = string.upper()
    for i in range(len(string)):
        char = string[i]
        encrypted_string = encrypted_string + encrypt_char(char, i)
    print("This is your encrypted string: ",encrypted_string)
#encrypt(usr_input)
def decrypt_char(char, cipher_index):
    table_index = cipher_table[cipher_index].index(char)
    #print(table_index)
    if cipher_index > 4:
        cipher_index = 0
    decrypted_index = original_alphabet[table_index]
    #print(decrypted_index)
    return decrypted_index
#decrypt_char("U", 0)
def decrypt(string):
    global decrypted_string
    decrypted_string = ""
    for i in range(len(string)):
        char = string[i]
        decrypted_string = decrypted_string + decrypt_char(char, i)
    print("This is your decrypted string: ", decrypted_string)
#decrypt(encrypted_string)

if choice == "Encrypt" or choice == "encrypt":
    usr_input = input("Please enter a message that you would like to encrypt: ")
    encrypt(usr_input)
elif choice == "Decrypt" or choice == "decrypt":
    usr_input = input("Please enter a message that you would like to decrypt: ")
    decrypt(usr_input)
else:
    print("bruh")


