# ======= IMPORTS =======
import argparse
import random
import os
# ========================


# ===== COMMAND LINE ===== 
parser = argparse.ArgumentParser(description="Get the defaults for the input generator.")

parser.add_argument(
    '--max_coord', type=int, default=10000, help='Maximum coordinate value. Default: 10000'
)

parser.add_argument(
    '--max_size', type=int, default=5000, help='Maximum number of points. Default: 5000'
)

parser.add_argument(
    '--fixed_size', type=int, default=0, help='Fixed number of points. Default: 0 (disabled)'
)

args = vars(parser.parse_args())

# Example args version:
# {
#   "max_size": 5000,       # Highest possible coordinate. Here 5000 implies that none of our coords will go beyond (5000, 5000, 5000. . .)
#   "fixed_size": None      # Highest possible size. Randomly pick and generate a coordinate set that can be from 1-MaxQuant size.
#   "max_coord": None,      # Fixed number of points generated. Manually fix the size of the coordinate set
# }
# ========================


# ==== CONFIGURATIONS ====
MIN_COORD_POINT =   1000                                            # Lowest possible coordinate location
MAX_COORD_POINT =   max(MIN_COORD_POINT+1, abs(args['max_coord']))  # Highest possible coordinate location
MAX_INPUTS      =   abs(args['max_size'])                           # Max number of inputs for random selection
MIN_INPUTS      =   10                                              # Min number of inputs for random selection
FINAL_FILE_NAME =   'input.txt'                                     # Name of the file where coordinate set will be stored

# ========================

# === INPUTS GENERATOR ===
# Input generator of the form where the first line is a random positive integer N
# between 1 - the 32 bit integer limit and the next N lines are the 3d coordinates
# of the cities separated by a space

def random_size_picker():
    N = random.randint(MIN_INPUTS, MAX_INPUTS)
    return N

# ========================


# Output this to a file and call it input.txt
def write_output_to_file():
    code_location = os.path.dirname(os.path.abspath(__file__))
    output_file_path = os.path.join(code_location, FINAL_FILE_NAME)

    N = abs(args['fixed_size']) if args['fixed_size'] else random_size_picker()

    low  = MIN_COORD_POINT
    high = MAX_COORD_POINT
    get_number_between = random.randint



    cord_system = {f"{get_number_between(low, high)} {get_number_between(low, high)} {get_number_between(low, high)}\n" 
                   for _ in range(N)}

    file_lines = [f"{len(cord_system)}\n"]     # Start by outputting total coordinate set size in the first line
    file_lines.extend(cord_system)

    with open(output_file_path, 'w') as file:
        file.writelines(file_lines)

# ===============================


# ======= MAIN EXECUTION =======
write_output_to_file()

# Log the generation
code_location = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(code_location, 'log.txt')

with open(output_file_path, 'a+') as file:
    file.write(f"New Set Generated \n")
# ==============================
