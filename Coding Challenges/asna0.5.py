# adds correct solution to coding challenges:
def solution(commands):
    current_directory = "/"

    for command in commands:
        if command == "cd /":
            current_directory = "/"
        elif command == "cd .":
            continue
        elif command == "cd ..":
            if current_directory != "/":
                current_directory = "/".join(current_directory.split("/")[:-1])
                if not current_directory:
                    current_directory = "/"
        else:
            directory = command.split(" ")[1]
            if current_directory == "/":
                current_directory += directory
            else:
                current_directory += "/" + directory
    return current_directory


# Test the function
commands = ["cd ..", "cd .", "cd trash", "cd ..", "cd ."]
print(solution(commands))  # Output should be "/"
