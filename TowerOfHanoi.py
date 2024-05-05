def print_pegs(pegs, n):
    """ Helper function to print the current state of pegs """
    for level in range(n, 0, -1):
        for peg in pegs:
            if len(peg) >= level:
                print(f" {peg[level - 1]} ", end="")
            else:
                print(" | ", end="")
        print()
    print("------------------------")  # Adjust base length dynamically

def move_disk(n, source, target, auxiliary, pegs, total_disks):
    """ Recursive function to move disks """
    if n == 1:
        pegs[target].append(pegs[source].pop())
        print(f"Move disk 1 from {chr(65+source)} to {chr(65+target)}.")
        print_pegs(pegs, total_disks)
        return
    move_disk(n - 1, source, auxiliary, target, pegs, total_disks)
    pegs[target].append(pegs[source].pop())
    print(f"Move disk {n} from {chr(65+source)} to {chr(65+target)}.")
    print_pegs(pegs, total_disks)
    move_disk(n - 1, auxiliary, target, source, pegs, total_disks)

def tower_of_hanoi(n):
    """ Main function to initiate the process """
    pegs = [[] for _ in range(3)]  # Create three pegs
    pegs[0] = list(range(n, 0, -1))  # Place n disks on the first peg
    print("Initial state:")
    print_pegs(pegs, n)
    move_disk(n, 0, 2, 1, pegs, n)

# Example usage:
tower_of_hanoi(4)