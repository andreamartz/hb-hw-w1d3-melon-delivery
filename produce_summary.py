def delivery_report(filepath):
    """Print a delivery report.
    
    Takes an input file with delivery data and prints a delivery report.

    Argument:
    filepath: the path to the data file to be read (string)

    There is no return value.
    """

    day = filepath[-5]
    print("***********")
    print(f"Day {day}")
    print("***********")

    # create a file object from the string passed in as the file path
    the_file = open(filepath)

    # Iterate over each line in the file object
    for line in the_file:
        for line in the_file:
            line = line.rstrip()
            words = line.split('|')   # Create a list of strings using the 
                # pipe character ( | ) as a delimiter

            melon, count, amount = words  # unpack the words list into 
                # individual variables

            print(f"Delivered {count} {melon}s for total of ${amount}")
            break

    the_file.close()

delivery_report("um-deliveries-day-1.txt")
delivery_report("um-deliveries-day-2.txt")
delivery_report("um-deliveries-day-3.txt")
