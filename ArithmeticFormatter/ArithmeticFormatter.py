import operator

def arithmetic_arranger(problems: list, include_solution: bool = False) -> str:
	RESULT_DASHES = "-"
	SUPPORTED_OPERATIONS = {
		"+": operator.add,
		"-": operator.sub
	} 
	MAX_PROBLEMS_NUM = 5

	num_of_problems = len(problems)
	if num_of_problems > MAX_PROBLEMS_NUM:
		return "Error: Too many problems."

	def create_operation_list(probl: str, include_solution: bool):
		"""
		Returns a list containing each line of the operation
		"""
		first_number, operator, second_number = probl.split(" ")
		
		if not (first_number.isdigit() and second_number.isdigit()):
			raise ValueError("Error: Numbers must only contain digits.")
		
		if not(len(first_number) <= 4 and len(second_number) <= 4):
			raise ValueError("Error: Numbers cannot be more than four digits.")

		if operator not in SUPPORTED_OPERATIONS:
			raise ValueError("Error: Operator must be '+' or '-'.")
		
		probl_lines = [
			first_number if int(first_number)>int(second_number) else second_number,
			operator,
			first_number if int(first_number)<int(second_number) else second_number
		]

		# add the dashes
		probl_lines.append(RESULT_DASHES*(len(probl_lines[0])+2))

		# add the result if asked for
		if include_solution:
			result = SUPPORTED_OPERATIONS[operator](int(first_number), int(second_number))
			probl_lines.append(result)

		return probl_lines

	problems_formatted = []
	for prob in problems:
		try:
			problems_formatted.append(create_operation_list(prob, include_solution))
		except Exception as e:
			return e.args[0]


	# Format first row
	first_row = ""
	for prob_num in range(num_of_problems):
		dash_length = len(problems_formatted[prob_num][3])
		first_row += "{:>{dash}}    ".format(
			problems_formatted[prob_num][0],
			dash = dash_length
		)
	first_row = first_row.rstrip(" ")

	# Format second row
	second_row = ""
	for prob_num in range(num_of_problems):
		dash_length = len(problems_formatted[prob_num][3])
		second_row += "{operator} {:>{dash}}    ".format(
			problems_formatted[prob_num][2],
			operator = problems_formatted[prob_num][1],
			dash = dash_length-2
		)
	second_row = second_row.rstrip(" ")

	# Format third row
	third_row = ""
	for prob_num in range(num_of_problems):
		third_row += "{}    ".format(
			problems_formatted[prob_num][3]
		)
	third_row = third_row.rstrip(" ")

	rows = [first_row, second_row, third_row]
	arranged_problems = "\n".join(rows)

	rows = [first_row, second_row, third_row]

	# Format fourth row if asked for
	if include_solution:
		fourth_row = ""
		for prob_num in range(num_of_problems):
			dash_length = len(problems_formatted[prob_num][3])
			fourth_row += "{:>{dash}}    ".format(
				problems_formatted[prob_num][-1],
				dash = dash_length
			)
		fourth_row = fourth_row.rstrip(" ")
		rows.append(fourth_row)

	arranged_problems = "\n".join(rows)

	return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))

