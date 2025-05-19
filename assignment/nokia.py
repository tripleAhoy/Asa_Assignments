nokia = True

def main_menu():
	while True:
		print("""
Main menu

1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
		""")
		try:
			choice = int(input("Select an option: "))
		except ValueError:
			print("Invalid input. Please enter a number.")
			continue
		if choice == 99:
			print("Exiting... Goodbye!")
			break
		if choice == 1:
			phone_book_menu()
		elif choice == 2:
			messages_menu()
		elif choice == 3:
			chat_menu()
		elif choice == 4:
			call_register_menu()
		elif choice == 5:
			tones_menu()
		elif choice == 6:
			settings_menu()
		elif choice == 7:
			call_divert_menu()
		elif choice == 8:
			games_menu()
		elif choice == 9:
			calculator()
		elif choice == 10:
			reminders_menu()
		elif choice == 11:
			clock_menu()
		elif choice == 12:
			profiles_menu()
		elif choice == 13:
			sim_services_menu()
		else:
			print("Invalid option. try again.")	

def phone_book_menu():
	while True:
		print("""
Phone book

1. Search
2. Service Nos.
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags
0. Back to Main menu

		""")
		phone_book_choice = int(input('Select an option: '))
		if phone_book_choice == 0:
			break
		elif phone_book_choice == 1:
			search_menu()
		elif phone_book_choice == 2:
			service_nos_menu()
		elif phone_book_choice == 3:
			add_name_menu()
		elif phone_book_choice == 4:
			erase_menu()
		elif phone_book_choice == 5:
			edit_menu()
		elif phone_book_choice == 6:
			assign_tone()
		elif phone_book_choice == 7:
			send_bcard_menu()
		elif phone_book_choice == 8:
			options_menu()
		elif phone_book_choice == 9:
			speed_dials_menu()
		elif phone_book_choice == 10:
			voice_tags_menu()
		else:
			input("Invalid input. Try again.")

def search_menu():
	while True:
		print("""
		Search
		0. back to previous menu
		""")
		search_choice = input('Select option: ')
		if search_choice == "0":
			break
		else:
			print("Invalid option. Try again.")
def service_nos_menu():
	while True:
		print("""
		Service Nos
		0. back to previous menu
		""")
		service_nos_choice = input('Select option: ')
		if service_nos_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def add_name_menu():
	while True:
		print("""
		Add name
		0. back to previous menu
		""")
		add_name_choice = input('Select option: ')
		if add_name_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def erase_menu():
	while True:
		print("""
		Erase
		0. back to previous menu
		""")
		erase_choice = input('Select option: ')
		if erase_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def edit_menu():
	while True:
		print("""
		Edit
		0. back to previous menu
		""")
		edit_choice = input('Select option: ')
		if edit_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def assign_tone_menu():
	while True:
		print("""
		Assign tone
		0. back to previous menu
		""")
		assign_tone_choice = input('Select option: ')
		if assign_tone_choice == "0":
			break
		else:
			print("Invalid option. Try again.")


def send_bcard_menu():
	while True:
		print("""
		Send b'card
		0. Back to previous menu
		""")
		send_bcard_choice = input('Select option: ')
		if send_bcard_choice == "0":
			break
		else:
			print("Invalid option. Try again.")



def speed_dials_menu():
	while True:
		print("""
		Speed dials menu
		0. Back to previous menu
		""")
		speed_dials_choice = input('Select option: ')
		if speed_dials_choice == "0":
			break
		else:
			print("Invalid option. Try again.")


def voice_tags_menu():
	while True:
		print("""
		Voice tags
		0. Back 
		""")
		voice_tags_choice = input('Select option: ')
		if voice_tags_choice == "0":
			break
		else:
			print("Invalid option. Try again.")


def options_menu():
	while True:
		print("""
		Options

		1. Type of view
		2. Memory status
		0. Back
		""")
		options_choice = input("Select option: ")
		if options_choice == 0:
			break
		elif options_choice == 1:
			type_of_view_menu()
		elif options_choice == 2:
			memory_status_menu()		
		else:
			input("Invalid input. Try again.")

def type_of_view_menu():
	while True:
		print("""
		Type of view
		0. Back
		""")
		type_of_view_choice = input('Select option: ')
		if type_of_view_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def memory_status_menu():
	while True:
		print("""
		Memory status
		0. Back
		""")
		memory_status_choice = input('Select option: ')
		if memory_status_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def messages_menu():
	while True:
		print("""
Messages

1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info Services
9. Voice mailbox number
10. Service command editor
0. Back to Main menu
		""")
		messages_choice = input("Select an option: ")
		if messages_choice == "0":
			break
		elif messages_choice == "1":
			write_message_menu()
		elif messages_choice == "2":
			inbox_menu()
		elif messages_choice == "3":
			outbox_menu()
		elif messages_choice == "4":
			picture_messages_menu()
		elif messages_choice == "5":
			templates_menu()
		elif messages_choice == "6":
			smileys_menu()
		elif messages_choice == "7":
			message_settings_menu()
		elif messages_choice == "8":
			info_services_menu()
		elif messages_choice == "9":
			voice_mailbox_number_menu()
		elif messages_choice == "10":
			service_command_editor_menu()
		else:
			input("invalid input. try again")
def write_message_menu():
	while True:
		print("""
		Write message
		0. Back
		""")
		write_message_choice = input('select option:')
		if write_message_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def inbox_menu():
	while True:
		print("""
		Inbox
		0. Back
		""")
		inbox_choice = input('select option:')
		if inbox_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def outbox_menu():
	while True:
		print("""
		Outbox
		0. Back
		""")
		outbox_choice = input('select option:')
		if outbox_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def picture_messages_menu():
	while True:
		print("""
		Picture messages
		0. Back
		""")
		picture_messages_choice = input('select option:')
		if picture_messages_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def templates_menu():
	while True:
		print("""
		Templates
		0. Back
		""")
		templates_choice = input('select option:')
		if templates_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def smileys_menu():
	while True:
		print("""
		Smileys
		0. Back
		""")
		smileys_choice = input('select option:')
		if smileys_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def info_services_menu():
	while True:
		print("""
		Info services
		0. Back
		""")
		info_services_choice = input('select option:')
		if info_services_choice == "0":
			break
		else:
			print("Invalid option. Try again.")
	
def voice_mailbox_number_menu():
	while True:
		print("""
		Voice mailbox number
		0. Back
		""")
		voice_mailbox_number_choice = input('select option:')
		if voice_mailbox_number_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def service_command_editor_menu():
	while True:
		print("""
		Service command editor
		0. Back
		""")
		service_command_editor_choice = input('select option:')
		if service_command_editor_choice == "0":
			break
		else:
			print("Invalid option. Try again.")


def message_settings_menu():
	while True:
		print("""
Message settings

1. Set 1
2. Common
0. Back
		""")
		message_settings_choice = input("Select an option: ")
		if message_settings_choice == "1":
			set1_menu()
		elif message_settings_choice == "2":
			common_menu()
		elif message_settings_choice == "0":
			break
		else:
			print("Invalid input")

def set1_menu():
	while True:
		print("""
		Set 1

		1. Message centre number
		2. Message sent as
		3. Message validity
		0. Back
		""")
		set1_choice = input("Select an option: ")
		if set1_choice == "0":
			break
		elif set1_choice == "1":
			message_centre_number()
		elif set1_choice == "2":
			message_sent_as()
		elif set1_choice == "3":
			message_validity()
		else:
			input("invalid input. try again.")

def message_centre_number():
	while True:
		print("""
		Message centre number
		0. Back
		""")
		message_centre_choice = input("Select an option: ")
		if message_centre_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def message_sent_as():
	while True:
		print("""
		Message sent as
		0. Back
		""")
		message_sent_choice = input("Select an option: ")
		if message_sent_choice == "0":
			break
		else:
			print("Invalid option. Try again.")
def message_validity():
	while True:
		print("""
		Message validity
		0. Back
		""")
		message_validity_choice = input("Select an option: ")
		if message_validity_choice == "0":
			break
		else:
			print("Invalid option. Try again.")


def common_menu():
	while True:
		print("""
		Common

		1. Delivery reports
		2. Reply via same centre
		3. Character support
		0. Back
		""")
		common_choice = input("Select an option: ")
		if common_choice == "0":
			break
		elif common_choice == "1":
			print("""
				Delivery reports
				0. Back
			""")
			common_choice = input("Select an option: ")
		elif common_choice == "2":
			print("""
				Reply via same centre
				0. Back
			""")
			common_choice = input("Select an option: ")
		elif common_choice == "3":
			print("""
				Character support
				0. Back
			""")
			common_choice = input("Select an option: ")
		else:
			input("invalid input. try again.")
def chat_menu():
	while True:
		print("""
		Chat

		0. Back
		""")
		chat_choice = input("Select an option: ")
		if chat_choice == "0":
			break

def call_register_menu():
	while True:
		print("""
		Call register

		1. Missed calls
		2. Received calls
		3. Dialled numbers
		4. Erase recent call lists
		5. Show call duration
		6. Show call costs
		7. Call cost settings
		8. Prepaid credit
		0. Back to Main menu
		""")
		call_register_choice = input("Select an option: ")
		if call_register_choice == "0":
			break
		elif call_register_choice == "1":
			missed_calls_menu()
		elif call_register_choice == "2":
			received_calls_menu()
		elif call_register_choice == "3":
			dialled_numbers_menu()
		elif call_register_choice == "4":
			erase_recent_call_lists_menu()
		elif call_register_choice == "5":
			show_call_duration_menu()
		elif call_register_choice == "6":
			show_call_costs_menu()
		elif call_register_choice == "7":
			call_cost_settings_menu()
		elif call_register_choice == "8":
			prepaid_credit_menu()
		else:
			input("invalid input. try again.")

def missed_calls_menu():
	print("""
		Missed calls
		0. back
	""")
	missed_calls_choice = input("Select an option: ")
	if missed_calls_choice < "0" or missed_calls_choice > "0":
		print('Invalid number.')
def received_calls_menu():
	print("""
		Received calls
		0. Back
	""")
	recieved_calls_choice = input("Select an option: ")
def dialled_numbers_menu():
	print("""
		Dialled numbers
		0. Back
	""")
	dialled_numbers_choice = input("Select an option: ")
def erase_recent_call_lists_menu():
	print("""
		Erased recent call lists
		0. Back
	""")
	erase_recent_call_lists_choice = input("Select an option: ")
def show_call_duration_menu():
	while True:
		print("""
		Show call duration

		1. Last call duration
		2. All calls' duration
		3. Receieved calls' duration
		4. Dialled calls' duration
		5. Clear timers

		""")
		show_call_duration_choice = input("Select an option: ")

		if show_call_duration_choice == "0":
			break
		if show_call_duration_choice == "1":
			print("""
				Last call duration
				0. Back
			""")
			last_call_duration_choice = input("Select an option: ")
		if show_call_duration_choice == "2":
			print("""
				All calls' duration
				0. Back
			""")
			all_calls_duration_choice = input("Select an option: ")
		if show_call_duration_choice == "3":
			print("""
				Receieved calls' duration
				0. Back
			""")
			receieved_calls_duration_choice = input("Select an option: ")
		if show_call_duration_choice == "4":
			print("""
				Dialled calls' duration
				0. Back
			""")
			dialled_calls_duration_choice = input("Select an option: ")
		if Show_call_duration_choice == "5":
			print("""
				Clear timers
				0. Back
			""")
			clear_timers_choice = input("Select an option: ")
def show_call_costs_menu():
	while True:
		print("""
		Show call costs

		1. Last call cost
		2. All calls' cost
		3. Clear counters
		""")
		show_call_costs_choice = input("Select an option: ")
		if show_call_costs_choice == "0":
			break
		if show_call_costs_choice == "1":
			print("""
				Last call cost
				0. Back
			""")		
			last_call_cost_choice = input("Select an option: ")
		if show_call_costs_choice == "2":
			print("""
				All calls' cost
				0. Back
			""")		
			all_calls_cost_choice = input("Select an option: ")
		if show_call_costs_choice == "3":
			print("""
				Clear counters
				0. Back
			""")		
			clear_counters_choice = input("Select an option: ")
def call_cost_settings_menu():
	while True:
		print("""
		Call cost settings

		1. Call cost limit
		2. Show costs in
		""")
		call_cost_settings_choice = input("Select an option: ")
		if call_cost_settings_choice == "0":
			break		
		elif call_cost_settings_choice == "1":
			print("""
				Call cost limit
				0. Back
			""")
			call_cost_limit_choice = input("Select an option: ")
		elif call_cost_settings_choice == "2":
			print("""
				Show costs in
				0. Back
			""")
			show_costs_in_choice = input("Select an option: ")


def prepaid_credit_menu():
	print("""
		Prepaid credit
		0. Back
	""")
	prepaid_credit_choice = input("Select an option: ")

def tones_menu():
	while True:
		print("""
		Tones

		1. Ringing tone
		2. Ringing Volume
		3. Incoming call alert
		4. Composer
		5. Message alert tone
		6. Keypad tones
		7. Warning and game tones
		8. Vibrating alert
		9. Screen saver
		0. Back to Main menu
		""")
		tones_choice = input("Select an option: ")
		if tones_choice == "0":
			break
		elif tones_choice == "1":
			print("""
				Ringing tone
				0. Back
			""")
			ringing_tone_choice = input("Select an option: ")
		elif tones_choice == "2":
			print("""
				Ringing volume
				0. Back
			""")
			ringing_volume_choice = input("Select an option: ")
		elif tones_choice == "3":
			print("""
				Incoming call alert
				0. Back
			""")
			incoming_call_choice = input("Select an option: ")
		elif tones_choice == "4":
			print("""
				Composer
				0. Back
			""")
			composer_choice = input("Select an option: ")
		elif tones_choice == "5":
			print("""
				Message alert tones
				0. Back
			""")
			message_alert_choice = input("Select an option: ")
		elif tones_choice == "6":
			print("""
				Keypad tones
				0. Back
			""")
			keypard_tones_choice = input("Select an option: ")
		elif tones_choice == "7":
			print("""
				Warning and game tones
				0. Back
			""")
			warning_game_choice = input("Select an option: ")
		elif tones_choice == "8":
			print("""
				Vibrating alert
				0. Back
			""")
			vibrating_alert_choice = input("Select an option: ")
		elif tones_choice == "9":
			print("""
				Screen saver
				0. Back
			""")
			screen_saver_choice = input("Select an option: ")
		else:
			input("invalid input. try again.")

def settings_menu():
	while True:
		print("""
		Settings

		1. Call settings
		2. Phone settings
		3. Security settings
		4. Restore factory settings
		0. Back to Main menu
		""")
		settings_choice = input("Select an option: ")
		if settings_choice == "0":
			break
		elif settings_choice == "1":
			call_settings_menu()
		elif settings_choice == "2":
			phone_settings_menu()
		elif settings_choice == "3":
			security_settings_menu()
		elif settings_choice == "4":
			print("""
				Restore factory settings
				0. Back
			""")
			restore_factory_choice = input("Select an option: ")
		else:
			input("invalid input. try again.")

def call_settings_menu():
	while True:
		print("""
		Call settings

		1. Automatic dialling
		2. Speed dialling
		3. Call waiting options
		4. Own number sending
		5. Phone line in use
		6. Automatic answer
		0. Back
		""")
		call_settings_choice = input("Select an option: ")
		if call_settings_choice == "0":
			break
		elif call_settings_choice == "1":
			print("""
				Automatic dialling
				0.Back
			""")
			automatic_dialling_choice = input("Select an option: ")
		elif call_settings_choice == "2":
			print("""
				Speed dialling
				0.Back
			""")
			speed_dialling_choice = input("Select an option: ")
		elif call_settings_choice == "3":
			print("""
				Call waiting options
				0.Back
			""")
			call_waiting_options_choice = input("Select an option: ")
		elif call_settings_choice == "4":
			print("""
				Own number sending
				0.Back
			""")
			own_number_sending_choice = input("Select an option: ")
		elif call_settings_choice == "5":
			print("""
				Phone line in use
				0.Back
			""")
			phone_line_in_use_choice = input("Select an option: ")
		elif call_settings_choice == "6":
			print("""
				Automatic answer
				0.Back
			""")
			automatic_answer_choice = input("Select an option: ")

def phone_settings_menu():
	while True:
		print("""
		Phone settings

		1. Language
		2. Cell info display
		3. Welcome note
		4. Network selection
		5. Lights
		6. Confirm SIM service actions
		""")
		phone_settings_choice = input("Select an option: ")
		if phone_settings_choice == "0":
			break
		elif phone_settings_choice == "1":
			print("""
				Language
				0. Back
			""")
			language_choice = input("Select an option: ")
		elif phone_settings_choice == "2":
			print("""
				Cell info display
				0. Back
			""")
			cell_info_display_choice = input("Select an option: ")
		elif phone_settings_choice == "3":
			print("""
				Welcome note
				0. Back
			""")
			cell_info_display_choice = input("Select an option: ")
		elif phone_settings_choice == "4":
			print("""
				Network selection
				0. Back
			""")
			cell_info_display_choice = input("Select an option: ")
		elif phone_settings_choice == "5":
			print("""
				Lights
				0. Back
			""")
			Lights_choice = input("Select an option: ")
		elif phone_settings_choice == "6":
			print("""
				Confirm SIM service actions
				0. Back
			""")
			confirm_sim_service_actions_choice = input("Select an option: ")
		else:
			print('Invalid option. Try again.')

def security_settings_menu():
	while True:
		print("""
		Security settings

		1. PIN code request
		2. Call barring service
		3. Fixed dialling
		4. Closed user group
		5. Phone security
		6. Change access settings	
		""")
		security_settings_choice = input("Select an option: ")
		if security_settings_choice == "0":
			break
		elif security_settings_choice == "1":
			print("""
				PIN code request
				0. Back
			""")
			pin_code_choice = input("Select an option: ")
		elif security_settings_choice == "2":
			print("""
				Call barring service
				0. Back
			""")
			call_barring_choice = input("Select an option: ")
		elif security_settings_choice == "3":
			print("""
				Fixed dialling
				0. Back
			""")
			fixed_dialling_choice = input("Select an option: ")
		elif security_settings_choice == "4":
			print("""
				Closed user group
				0. Back
			""")
			closed_user_choice = input("Select an option: ")
		elif security_settings_choice == "5":
			print("""
				Phone security
				0. Back
			""")
			phone_security_choice = input("Select an option: ")
		elif security_settings_choice == "6":
			print("""
				Change access settings
				0. Back
			""")
			change_access_choice = input("Select an option: ")
		else:
			print("Invalid option. Try again.")

def call_divert_menu():
	print("""
		Call divert
		0. Back
	""")
	call_divert_choice = input("Select an option: ")

def games_menu():
	print("""
		Games
		0. Back
	""")
	games_choice = input("Select an option: ")

def calculator():
	print("""
		Calculator
		0. Back
	""")
	calculator_choice = input("Select an option: ")

def reminders_menu():
	print("""
		Reminders
		0. Back
	""")
	reminders_choice = input("Select an option: ")
def clock_menu():
	while True:
		print("""
		Clock

		1. Alarm clock
		2. Clock settings
		3. Date setting
		4. Stopwatch
		5. Countdown timer
		6. Auto update of date and time	
		""")
		clock_choice = input("Select an option: ")
		if clock_choice == "0":
			break
		elif clock_choice == "1":
			print("""
				Alarm clock
				0. Back
			""")
			alarm_clock_choice = input("Select an option: ")
		elif clock_choice == "2":
			print("""
				Clock settings
				0. Back
			""")
			clock_settings_choice = input("Select an option: ")
		elif clock_choice == "3":
			print("""
				Date setting
				0. Back
			""")
			date_setting_choice = input("Select an option: ")
		elif clock_choice == "4":
			print("""
				Stopwatch
				0. Back
			""")
			stopwatch_choice = input("Select an option: ")
		elif clock_choice == "5":
			print("""
				Countdown timer
				0. Back
			""")
			countdown_choice = input("Select an option: ")
		elif clock_choice == "6":
			print("""
				Auto update of date and time
				0. Back
			""")
			auto_update_choice = input("Select an option: ")
		else:
			print("Invalid option. Try again.")

def profiles_menu():
	while True:
		print("""
		Profiles
		0. Back
		""")
		profiles_choice = input("Select an option: ")	
		if profiles_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

def sim_services_menu():
	while True:
		print("""
		SIM services
		0. Back
		""")
		sim_services_choice = input("Select an option: ")
		if sim_services_choice == "0":
			break
		else:
			print("Invalid option. Try again.")

if __name__ == "__main__":
    main_menu()
