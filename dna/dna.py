import sys
import csv


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py [DATABASE].csv [SEQUENCE].txt")
        sys.exit(1)

    else:
        # Check if files have correct extensions
        db_file = sys.argv[1]
        seq_file = sys.argv[2]
        if not (db_file.endswith(".csv") or not seq_file.endswith(".txt")):
            print("Error: Invalid file types. Expected .csv for database and .txt for sequence.")
            sys.exit(2)

        # Read database and sequence files into variables
        data = []
        subsequence = []
        with open(db_file) as database:
            reader = csv.DictReader(database)
            subsequence = reader.fieldnames[1:]  # Skip the first column which is 'name'
            for value in reader:
                data.append(value)

        # Read DNA sequence file into a variable
        with open(seq_file, "r") as dna_sequence:
            sequence = dna_sequence.read().strip()

        # Find longest match of each STR in DNA sequence
        str_count = {}
        for str in subsequence:
            count = longest_match(sequence, str)
            str_count[str] = count

        # Check data for matching profiles
        is_match = False
        for person in data:
            all_str_valid = True
            for str in subsequence:
                expected_count = int(person[str])  # str count from the database
                actual_count = str_count[str]  # str count from the sequence

                if expected_count != actual_count:
                    all_str_valid = False
                    break

            if all_str_valid:
                print(person["name"])
                is_match = True
                sys.exit(0)

        if not is_match:
            print("No match")
            sys.exit(3)

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
