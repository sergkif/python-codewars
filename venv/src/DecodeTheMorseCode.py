MORSE_CODE = { '.-': 'A', '-...': 'B',
                    '-.-.': 'C', '-..': 'D', '.': 'E',
                    '..-.': 'F', '--.': 'G', '....': 'H',
                    '..': 'I', '.---': 'J', '-.-': 'K',
                    '.-..':'L', '--': 'M', '-.': 'N',
                    '---': 'O', '.--.': 'P', '--.-': 'Q',
                    '.-.': 'R', '...': 'S', '-': 'T',
                    '..-': 'U', '...-': 'V', '.--': 'W',
                    '-..-': 'X', '-.--': 'Y', '--..': 'Z',
                    '.----': '1', '..---': '2', '...--': '3',
                    '....-': '4', '.....': '5', '-....': '6',
                    '--...': '7', '---..': '8', '----.': '9',
                    '-----': '0', '--..--': ', ', '.-.-.-': '.',
                    '..--..': '?', '-..-.': '/', '-....-': '-',
                    '-.--.': '(', '-.--.-': ')'}
######## Decode the Morse code
# easier: 6 kyu
# def decodeMorse(morse_code):
#     result = []
#     for morse_code_word in morse_code.split("   "):
#         tmp = ""
#         for morse_code_letter in morse_code_word.split(" "):
#             if(morse_code_letter != "" and morse_code_letter != " "):
#                 tmp += MORSE_CODE[morse_code_letter]
#         result.append(tmp)
#         tmp = ""
#     return " ".join(result).strip()

def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
#
# In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
# The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as .-, letter Q is coded as --.-, and digit 1 is coded as .---- . The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is .... . -.--   .--- ..- -.. . .
# NOTE: Extra spaces before or after the code have no meaning and should be ignored.
#
# In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ...---... . These special codes are treated as single special characters, and usually are transmitted as separate words.
#
# Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.
#
# For example:
#
# decodeMorse('.... . -.--   .--- ..- -.. .')
# #should return "HEY JUDE"
# NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.
#
# The Morse code table is preloaded for you as a dictionary, feel free to use it:
#
# Coffeescript/C++/Go/JavaScript/Julia/PHP/Python/Ruby/TypeScript: MORSE_CODE['.--']
# C#: MorseCode.Get(".--") (returns string)
# Elixir: @morse_codes variable (from use MorseCode.Constants). Ignore the unused variable warning for morse_codes because it's no longer used and kept only for old solutions.
# Elm: MorseCodes.get : Dict String String
# Haskell: morseCodes ! ".--" (Codes are in a Map String String)
# Java: MorseCode.get(".--")
# Kotlin: MorseCode[".--"] ?: "" or MorseCode.getOrDefault(".--", "")
# Rust: self.morse_code
# Scala: morseCodes(".--")
# C: provides parallel arrays, i.e. morse[2] == "-.-" for ascii[2] == "C"
# All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions. In C#, tests will fail if the solution code throws an exception, please keep that in mind. This is mostly because otherwise the engine would simply ignore the tests, resulting in a "valid" solution.

# _________________________________________
# _________________________________________
# _________________________________________
# _________________________________________
# _________________________________________


######## Decode the Morse code, advanced
#
# 4 kyu

def decodeBits(bits):
    bits = bits.strip('0')
    min_len = min([len(s) for s in bits.split('1') + bits.split('0') if s])
    return bits.replace('111' * min_len, '-').replace('1' * min_len, '.').replace('0000000' * min_len, '   ').replace('000' * min_len, ' ').replace('0' * min_len, '')

#Decode the Morse code, advanced
#
# 4 kyu
# In this kata you have to write a Morse code decoder for wired electrical telegraph.
# Electric telegraph is operated on a 2-wire line with a key that, when pressed, connects the wires together, which can be detected on a remote station. The Morse code encodes every character being transmitted as a sequence of "dots" (short presses on the key) and "dashes" (long presses on the key).
#
# When transmitting the Morse code, the international standard specifies that:
#
# "Dot" - is 1 time unit long.
# "Dash" - is 3 time units long.
# Pause between dots and dashes in a character - is 1 time unit long.
# Pause between characters inside a word - is 3 time units long.
# Pause between words - is 7 time units long.
# However, the standard does not specify how long that "time unit" is. And in fact different operators would transmit at different speed. An amateur person may need a few seconds to transmit a single character, a skilled professional can transmit 60 words per minute, and robotic transmitters may go way faster.
#
# For this kata we assume the message receiving is performed automatically by the hardware that checks the line periodically, and if the line is connected (the key at the remote station is down), 1 is recorded, and if the line is not connected (remote key is up), 0 is recorded. After the message is fully received, it gets to you for decoding as a string containing only symbols 0 and 1.
#
# For example, the message HEY JUDE, that is .... . -.--   .--- ..- -.. . may be received as follows:
#
# 1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011
#
# As you may see, this transmission is perfectly accurate according to the standard, and the hardware sampled the line exactly two times per "dot".
#
# That said, your task is to implement two functions:
#
# Function decodeBits(bits), that should find out the transmission rate of the message, correctly decode the message to dots ., dashes - and spaces (one between characters, three between words) and return those as a string. Note that some extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore them. Also if you have trouble discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot.
#
# Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable string.
#
# NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.
#
# The Morse code table is preloaded for you as MORSE_CODE dictionary; in Java MorseCode class is provided; in Haskell the codes are in a Map String String and can be accessed like this: morseCodes ! ".--"; in Racket MORSE-CODE and can be accessed like this: (hash-ref MORSE-CODE ".--"). Feel free to use this preload.
#
# All the test strings would be valid to the point that they could be reliably decoded as described above, so you may skip checking for errors and exceptions, just do your best in figuring out what the message is!
#
# Good luck!