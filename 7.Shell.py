import subprocess

while True:
    # Read user input
    user_input = input("$ ")

    # Check if the user wants to exit the shell
    if user_input == "exit":
        print("Exiting shell...")
        break

    # Split the user input into command and arguments
    parts = user_input.split()
    command = parts[0]
    args = parts[1:]

    # Initialize variables for input/output redirection
    input_file = None
    output_file = None

    # Check for input/output redirection
    if '<' in args:
        index = args.index('<')
        input_file = args[index + 1]
        args = args[:index]
    elif '>' in args:
        index = args.index('>')
        output_file = args[index + 1]
        args = args[:index]

    try:
        if input_file:
            with open(input_file, 'r') as f:
                if output_file:
                    with open(output_file, 'w') as o:
                        subprocess.run([command] + args, stdin=f, stdout=o)
                else:
                    subprocess.run([command] + args, stdin=f)
        elif output_file:
            with open(output_file, 'w') as f:
                subprocess.run([command] + args, stdout=f)
        else:
            subprocess.run([command] + args)
    except FileNotFoundError:
        print("Command not found: {}".format(command))