########################
# Liam Dullea, Buuthien Hang, Tommy Tang, Eric Mains
# Skimtech- a credit card skimmer detector
#
#
# This file will be for programming the NFC tag and running  the secure CC protocol
#
#       Date:               Revision:
#       5/3/23              Start of file
##########################

# PSEUDO-CODE FROM PAPER
"""
function G(info, ch):
    const khi = hash(bank_key, info)
    result = empty list of bits
    for each of the n bits of ch:
        if the n’th bit of ch is 1:
            append n’th bit of khi to result
    return result


function F(x, iCVV):
    return x XOR iCVV


function H(info, ch, iCVV):
    x = G(info, ch)
    return F(x, iCVV)
"""

# IMPLEMENTATIONS


bank_key = 0


def H(info, ch, iCVV):
    x = G(info, ch)
    return F(x, iCVV)


def F(x, iCVV):
    return bin(x^iCVV)

def G(info, ch):
    i = 0
    khi = bin(hash(bank_key, info))
    result = []
    chBin = bin(ch)
    for n in chBin:
        if n == 1:
            result.append(khi(i))
    return result

if __name__ == '__main__':
    print(F(7,2))


    print("Hello World")