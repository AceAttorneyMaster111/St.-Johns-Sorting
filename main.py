#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

def i(question):
	return input(question + " ")

def sort_preceptorials():
	print('Instructions: Follow the prompts. When prompted for single letter answers, "y" is "yes", "n" is "no", "c" is "cancel" (cancel the current operation rather than just the current iteration), and "v" is view, as in view all responses to the current operation. Type ^d (control + d) at any time to exit the program.')
	student_preferences = {} # Key: Student name, value: list of tuples of preceptorials and favorite status.
	preceptorial_max = {} # Key: preceptorials, value: capacity

	# Fill out preceptorial_max
	while True:
		curr_precept = i("Enter a preceptorial.")
		while True:
			try:
				curr_precept_max = int(i("How many students can {:s} hold?".format(curr_precept)))
			except ValueError:
				print("Please print a number.")
			else:
				break
		print("The preceptorial {:s} can fit {:d} students.".format(curr_precept, curr_precept_max))
		correct = i("Is this correct? (y/n)")
		if(correct == "n"):
			continue
		preceptorial_max[curr_precept] = curr_precept_max
		more_precepts = i("You have entered {:d} preceptorials. Would you like to enter more? (y/n/c/v)".format(len(preceptorial_max)))
		if(more_precepts == "c"):
			confirm = i("Just to confirm, you want to clear all preceptorials? (y/n)")
			if(confirm == "y"):
				preceptorial_max = {}
				print("Preceptorials cleared.")
				continue
			more_precepts = i("You have entered {:d} preceptorials. Would you like to enter more? (y/n/v)")
		if(more_precepts == "v"):
			view_precepts = "*" * 20 + "\n"
			for key, value in preceptorial_max.items():
				view_precepts += key + ": can fit " + value + " students\n"
			view_precepts += "*" * 20
			print(view_precepts)
			more_precepts = i("You have entered {:d} preceptorials. Would you like to enter more? (y/n)")
		if(more_precepts == "n"):
			break
			
	# Fill out student_preferences.
	while True:
		curr_student = i("Enter a student name.")
		curr_reqs = []
		while True:
			curr_req = i("Enter a requested preceptorial.")
			req_preferred = 1 if i("Is this request preferred? (y/n)") == "y" else 0
			print("You entered a {:s}preferred preceptorial \"{:s}\".".format("non-" if req_preferred == 0 else "", curr_req))
			correct = i("Is this correct? (y/n)")
			if(correct == "n"):
				continue
			curr_reqs.append((curr_req, req_preferred))
			more_reqs = i("You currently have entered {:s} requests for {:s}. Would you like to enter more? (y/n/c/v)".format(len(curr_reqs), curr_student))
			if(more_reqs == "v"):
				view_reqs = "*" * 20 + "\n"
				for value in curr_reqs:
					view_reqs += value[0] + "- " + ("non-" if value[1] == 0 else "") + "preferred\n"
				view_reqs += "*" * 20
				print(view_reqs)
				more_reqs = i("You currently have entered {:d} requests for {:d}. Would you like to enter more? (y/n/c)?".format(len(curr_reqs), curr_student))
			if(more_reqs == "c"):
				print("Student {:s} canceled.".format(curr_student))
				break
			elif(more_reqs == "n"):
				break
		if(more_reqs == "c"):
			continue
		student_preferences[curr_student] = curr_reqs
		more_students = i("You currently have entered {:d} students. Would you like to enter more? (y/n/c/v)".format(len(student_preferences)))
		if(more_students == "v"):
			view_students = ("*" * 20 + "\n") * 2 + "\n"
			for key, values in student_preferences.items():
				view_students += key + ":\n"
				for value in values:
					view_students += value[0] + "- " + ("non-" if value[1] == 0 else "") + "preferred\n"
				view_students += "\n" + "*" * 20 + "\n" + ("\n" if value != values[-1] else "")
			view_students += ("*" * 20 + "\n") + "\n"
			print(view_students)
			more_students = i("You currently have entered {:d} students. Would you like to enter more? (y/n/c)".format(len(student_preferences)))
		if(more_students == "c"):
			confirm = i("Just to confirm, you want to clear all students? (y/n)")
			if(confirm == "y"):
				student_preferences = {}
				print("Students cleared.")
				continue
			more_students = i("You currently have entered {:d} students. Would you like to enter more? (y/n)".format(len(student_preferences)))
		if(more_students == "n"):
			break