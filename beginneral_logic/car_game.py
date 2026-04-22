def main():
    is_start = False

    while True:
        command = input(">")
        if command.lower() == "help":
            print("- start\n- stop\n- quit")
        elif command.lower() == "start":
            if is_start:
                print("the Car Already Started")
            else:
                is_start = True
                print("Starting the Car")
        elif command.lower() == "stop":
            if is_start:
                print("Stopping the Car")
                is_start = False
            else:
                print("the Car Already Stop")
        elif command.lower() == "quit":
            break
        else:
            print("Wrong Command.")


if __name__ == '__main__':
    main()
