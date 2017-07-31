#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

# Version: 0.0.1

# TODO: Change to accept three and only three precepts per student

def inp(question):
	return input(question + " ")

def sort_preceptorials():
	print('Instructions: Follow the prompts. When prompted for single letter answers, "y" is "yes", "n" is "no", "c" is "cancel" (cancel the current operation rather than just the current iteration), and "v" is view, as in view all responses to the current operation. Type ^d (control + d) at any time to exit the program.')
	student_preferences = {} # Key: Student name, value: list of tuples of preceptorials and favorite status.
	PRECEPT_MAX = 12;
	PRECEPT_MIN = 3;
	students = [] # Student name
	""" TODO: do this
	# Fill out students
	preceptorials = []
	# Fill out preceptorials
	"""
	# Fill out student_preferences.
	while True:
		curr_student = inp("Enter a student name.")
		curr_reqs = []
		while True:
			curr_req = inp("Enter a requested preceptorial.")
			req_preferred = inp("Is this request preferred? (y/n)") == "y" # This will be true or false
			print("You entered a {:s}preferred preceptorial \"{:s}\".".format("non-" if not req_preferred else "", curr_req))
			correct = inp("Is this correct? (y/n)")
			if(correct == "n"):
				continue
			curr_reqs.append((curr_req, req_preferred))
			more_reqs = inp("You currently have entered {:s} requests for {:s}. Would you like to enter more? (y/n/c/v)".format(len(curr_reqs), curr_student))
			if(more_reqs == "v"):
				view_reqs = "*" * 20 + "\n"
				for value in curr_reqs:
					view_reqs += value[0] + "- " + ("non-" if not value[1] else "") + "preferred\n"
				view_reqs += "*" * 20
				print(view_reqs)
				more_reqs = inp("You currently have entered {:d} requests for {:d}. Would you like to enter more? (y/n/c)?".format(len(curr_reqs), curr_student))
			if(more_reqs == "c"):
				print("Student {:s} canceled.".format(curr_student))
				break
			elif(more_reqs == "n"):
				break
		if(more_reqs == "c"):
			continue
		# students.append(curr_student) # deprecated
		student_preferences[curr_student] = curr_reqs
		more_students = inp("You currently have entered {:d} students. Would you like to enter more? (y/n/c/v)".format(len(student_preferences)))
		if(more_students == "v"):
			view_students = ("*" * 20 + "\n") * 2 + "\n"
			for key, values in student_preferences.items():
				view_students += key + ":\n"
				for value in values:
					view_students += value[0] + "- " + ("non-" if value[1] == 0 else "") + "preferred\n"
				view_students += "\n" + "*" * 20 + "\n" + ("\n" if value != values[-1] else "")
			view_students += ("*" * 20 + "\n") + "\n"
			print(view_students)
			more_students = inp("You currently have entered {:d} students. Would you like to enter more? (y/n/c)".format(len(student_preferences)))
		if(more_students == "c"):
			confirm = inp("Just to confirm, you want to clear all students? (y/n)")
			if(confirm == "y"):
				student_preferences = {}
				# students = []
				print("Students cleared.")
				continue
			more_students = inp("You currently have entered {:d} students. Would you like to enter more? (y/n)".format(len(student_preferences)))
		if(more_students == "n"):
			break
	preceptorial_students = {} # Key: preceptorials, value: list of students.
	# Step 1: Put all students into their preferred preceptorials.
