# Testbench for running the main script
import sys, json
from valid_sorting_network import SortingNetworkValidator

# Variables to pass to the validator
wire_count = 0
comparator_count = 0
comparators = []

# Read from stdin
reading_first_line = True
for line in sys.stdin:
	line_args = line.strip().split()
	if reading_first_line:
		wire_count = int(line_args[0])
		comparator_count = int(line_args[1])
		reading_first_line = False
	else:
		comparators.append(line_args)


snv = SortingNetworkValidator(wire_count, comparators)

# Check values
print wire_count
print json.dumps(comparators)
print snv.isValid()