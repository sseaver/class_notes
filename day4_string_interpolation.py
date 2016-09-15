# mad lib

mad_lib = """
Dear {name},
I am {action}ing you to {other_action} you
to {action_three} your {noun}.
"""

print(mad_lib.format(name = "Sam", action = "write",
                        other_action = "inform",
                        action_three = "get lost",
                        noun = "face"))

marker_action = "erase"
print ("Markers are difficult to %s" % marker_action)
