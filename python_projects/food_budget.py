# Copy and paste this very simple piece of code into a python terminal to calculate your weekly food expenses. 


def food_budget(goal, grocery, take_out):
# This simple function will return a comment and value based upon 
# a users weekly food budget goal and weekly grocery and takeout expenses.
    if int(grocery) + int(take_out) > int(goal):
        return 'You are over your weekly food budget : $' + str(int(goal) - (int(grocery) + int(take_out)))
    elif int(grocery) + int(take_out) == int(goal):
        return 'You have reached your weekly food budget goal of : $' + str(int(goal))
    else:
        return 'Great job! You are within your weekly food budget : $' + str(int(goal) - (int(grocery) + int(take_out)))


goal = input("Please enter your weekly food budget goal: $ ")
grocery = input("Please enter your grocery expenses for the week: $ ")
take_out = input("Please enter your take out expenses for the week: $ ")


print(food_budget(goal, grocery, take_out))


# This is the beginning of a python engineering project, future iterations 
# will improve on this very simple function. (4/15/24)