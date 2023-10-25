while True:
    val = input("Enter your value (or type 'stop' to quit): ")

    if val != "stop":
        try:
            val = float(val)
            print(val, pow(val, 3))
        except ValueError:
            print("Error: This is not a valid float. Please try again.")
    else:
        break
