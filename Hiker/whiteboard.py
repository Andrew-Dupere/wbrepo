# Hills & Valleys
# An avid hiker keeps meticulous records of their hikes. During the last hike they took exactly Steps steps. 
# For every step it was noted if it was an uphill, U, or a downhill, D step. Hikes always start and end at sea 
# level and each step up or down represents a 1 unit change in altitude. We define the following terms: 

# A mountain is a sequence of steps uphill, starting with a step up and ending at sea level. 
# A valley is a sequence of steps downhill, start with a step down and ending at sea level. 
# Given the sequence of up and downs steps during a hike, return the number of valleys walked through. If the # of 
# steps does not equal path, return -1

# Example:
# Input: Steps = 8, Path = "DDUUUUDD" 
# Output: 1 
# Explanation: The hiker first enters a valley with 2 down units deep. Then they climb out of it back to sea level 
# and up onto a mountain 2 units high and returns back down to sea level. 

# Example:
# Input: Steps = 12, Path = "UDDDUDUUDDUU" 
# Output: 2
# Explanation: The hiker first walks uphill to a small mountain and back down. Then they climb into a valley 2 steps 
# down, up 1, back down 1, and then returns to sea level with 2 steps up. 
#They then take 2 more steps down into a valley and then back up out of the valley



def solution(steps,path):
    pass

print(solution(12,"UDDDUDUUDDUU"))
















#UD DD UD UU DDUU

# hiker keeps track of steps and notes whether uphill or downhill

# count how many times 'DU' appears? 


# def solution(steps,path):

#     alt = 0
#     check = []
#     valleys = 0

#     # if altitude was negative and we return to sea level
#     for i in path:
#         if i == 'U':
#             alt += 1
#         else:
#             alt -= 1
#         check.append(alt)

    

#     for i in range(len(check)):
        
#         if check[i] == 0 and check[i-1] < 0:
#             valleys += 1             


#     return(valleys)
    

# print(solution(12,"UDDDUDUUDDUU"))

