project1 = "Intermodal" + " "
project2 = "Coal Unloading" + " "
project3 = "Coal Loading" + " "

command_profiles = ["Command List 1", "Command List 2", "Command List 3"]

command_list_v1 = [  # interactive command
    ["100", project1 + "Reset position"],
    ["101", project1 + "Move Forward"],
    ["102", project1 + "Move Backward"],
    ["103", project1 + "Move Upward"],
    ["104", project1 + "Move Downward"],
    ["105", project1 + "Move Left"],
    ["106", project1 + "Move Right"],

    ["200", project2 + "Reset Position"],
    ["201", project2 + "Rotate 180 CW"],

    ["300", project3 + "Reset Loading Gate"],
    ["301", project3 + "Toggle Loading Gate"],
]

command_list_v2 = [  # freestyle commands
    ["W", "Forward"],
    ["S", "Backward"],
    ["A", "Left"],
    ["D", "Right"]
]

command_list_v3 = [
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""],
    ["", ""]
]
