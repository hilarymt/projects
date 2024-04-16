# This is a simple food_budget function _v1:


def food_budget(goal, grocery, take_out):
    if int(grocery) + int(take_out) > int(goal):
        return 'You are over your weekly food budget : $' + str(int(goal) - (int(grocery) + int(take_out)))
    elif int(grocery) + int(take_out) == int(goal):
        return 'You have reached your weekly food budget goal of : $' + str(int(goal))
    else:
        return 'Great job! You are within your weekly food budget : $' + str(int(goal) - (int(grocery) + int(take_out)))

# The three inputs are weekly food cost goal, weekly grocery costs and weekly takeout costs that
# our input by the user.

# The first statement is the sum of the users weekly grocery and takeout costs, if this
# is less than the weekly goal. The user is told they are within the weekly goal and difference
# of the goal and sum of the grocery and takeout is displayed to user
# The second statement


goal = input("Please enter your weekly food budget goal: $ ")
grocery = input("Please enter your grocery expenses for the week: $ ")
take_out = input("Please enter your take out expenses for the week: $ ")


print(food_budget(goal, grocery, take_out))
