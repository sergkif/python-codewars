from src import NumberOfPeopleInTheBus, ReplaceWithAlphabetPosition, DecodeTheMorseCode, Dubstep, IQTest, \
    NumberOfTrailingZerosOfFactorial, MaximumSubarraySum, GapInPrimes, StripComments, PerfectPower, IsMyFriendCheating, WeightForWeight

print("Number of people in th bus: ", NumberOfPeopleInTheBus.number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
print("Replace With Alphabet Position: ", ReplaceWithAlphabetPosition.alphabet_position("The sunset sets at twelve o' clock."))
print("Decode The Morse Code: ", DecodeTheMorseCode.decodeMorse('.... . -.--   .--- ..- -.. .'))
print("Decode The Morse Code Advanced: ", DecodeTheMorseCode.decodeMorse(DecodeTheMorseCode.decodeBits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')))
print("Dubstep: ", Dubstep.song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
print("IQ Test: ", IQTest.iq_test("2 4 7 8 10"))
print("Number of trailing zeros of N!: ", NumberOfTrailingZerosOfFactorial.zeros(30))
print("Maximum subarray sum: ", MaximumSubarraySum.max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print("Gap in Primes: ", GapInPrimes.gap(2,100,110))
print("Strip comments: ", StripComments.solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print("Perfect Power: ", PerfectPower.isPP(326940373369))
print("Is my friend cheating: ", IsMyFriendCheating.removNb(26))
print("Weight For Weight: ", WeightForWeight.order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))