import operator

def arithmetic_arranger(problems: list, include_solution: bool = False) -> str:
	RESULT_DASHES = "------"
	SUPPORTED_OPERATIONS = {
		"+": operator.add,
		"-": operator.sub
	} 
	MAX_PROBLEMS_NUM = 5

	if len(problems) > MAX_PROBLEMS_NUM:
		return "Error: Too many problems."

	def create_operation_str(probl: str, include_solution: bool):
		"""
		Returns a list containing each line of the operation
		"""
		first_number, operator, second_number = probl.split(" ")
		if operator not in SUPPORTED_OPERATIONS:
			raise ValueError("Error: Operator must be '+' or '-'.")
		
		probl_lines = [first_number, operator, second_number]

		# add the dashes
		probl_lines.append(RESULT_DASHES)

		# add the result if asked for
		if include_solution:
			result = SUPPORTED_OPERATIONS[operator](int(first_number), int(second_number))
			probl_lines.append(result)

		return probl_lines

	problems_formatted = []
	for prob in problems:
		try:
			problems_formatted.append(create_operation_str(prob, include_solution))
		except Exception as e:
			return e.args

	arranged_problems = ""

	return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

