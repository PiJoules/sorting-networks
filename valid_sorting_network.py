# Class that receives number of wires, comparators, and list of the comparator-line pairs
class SortingNetworkValidator:

	def __init__(self, wire_count, comparators):
		self.wire_count = wire_count
		self.comparators = comparators
		self.valid_test_cases = []
		self.invalid_test_cases = []

		cases = self.generate_test_cases(wire_count)
		for case in cases:
			if self.network_does_work(case):
				self.valid_test_cases.append(case)
			else:
				self.invalid_test_cases.append(case)

	# Run the test for a given case
	def network_does_work(self, case):
		for comparator in self.comparators:
			n0 = int(comparator[0])
			n1 = int(comparator[1])
			case_n0 = int(case[n0])
			case_n1 = int(case[n1])
			case = case[:n0] + str(min(case_n0,case_n1)) + case[n0+1:]
			case = case[:n1] + str(max(case_n0,case_n1)) + case[n1+1:]

		case = case.lstrip("0").rstrip("1")
		return case == ""

	# Create all 2**N possible sequences of 1s and 0s
	def generate_test_cases(self, N):
		cases = []
		for i in range(2**N):
			cases.append(self.int_to_binary(i,N))
		return cases

	# Take an int and make it a binary string with padded zeroes
	def int_to_binary(self, i, N):
		return "{0:b}".format(i).zfill(N)

	def isValid(self):
		return len(self.invalid_test_cases) == 0