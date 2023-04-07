# For a given list of digits 0 to 9, return a list with the same digits in the same order, but with all 0s paired. Pairing two 0s generates one 0 at the location of the first one.
# input: [0, 1, 0, 2]
# paired: ^ -----^
#     -> [0, 1,   2]
#   kept: ^

# input: [0, 1, 0, 0]
# paired: ^-----^
#     -> [0, 1,    0]
#   kept: ^        ^
# Ex: [1,0,1,0,2,0,0,3,0]) would Output : [1,0,1,2,0,3,0]
# Ex: [1,0,1,0,2,0,0,3,0] would Output:  [1,0,1,2,0,3,0]

# No preference for in-place or out of place


def solution(a_list):
    pass


print(solution([0, 1, 0, 2]))


















# def solution(a_list):
#     output = []
#     countzeros = 0

#     for num in a_list:
#         if num == 0:
#             countzeros +=1
#             if countzeros %2 == 0:
#                 continue
#             else:
#                 output.append(num)

#         else:
#             output.append(num)

#     return output
      


# print(solution([0, 1, 0, 2]))
