# Count the number of Distinct Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits 
#that occur more than once in the input string. The input string can be assumed to contain 
#only alphabets(both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0  # no characters repeats more than once
# "aabbcde" -> 2  # 'a' and 'b'
# "aabBcde" -> 2  # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1  # 'i' occurs six times
# "Indivisibilities" -> 2  # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2  # 'a' and '1'
# "ABBA" -> 2  # 'A' and 'B' each occur twice




def solution(a_string):
    pass


print(solution('abcde'))
















# make the characters lowercase
# return the items in the string that occur more than once





# def solution(a_string):

#     newlist = [letter.lower() for letter in a_string]
#     counter = 0


#     for letter in set(newlist):
#         if a_string.lower().count(letter) > 1:
#             counter +=1 

#     return counter

    


# print(solution('abcde'))
# print(solution('aabbcd12e'))


# def solutionBRIAN(a_string):
#     counts = {}
#     for letter in a_string.lower():
#         if letter in counts:
#             counts[letter] += 1
#         else:
#             counts[letter] = 1
#     total_duplicates = 0
#     for letter, number in counts.items():
#         if number > 1:
#             total_duplicates += 1
#     return total_duplicates

