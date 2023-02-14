from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.messaging_response import MessagingResponse

response = MessagingResponse()
msg = response.message()
msg.body("")
# chatbot logic
def bot():

	# user input
	user_msg = request.values.get('Body', '').lower()

	# creating object of MessagingResponse
	response = MessagingResponse()

	# User Query
	q = user_msg + "hello"

	# list to store urls
	result = []

	# searching and storing urls
	for i in search(q, tld='co.in', num=6, stop=6, pause=2):
		result.append(i)

	# displaying result
	msg = response.message(f"--- Results for '{user_msg}' ---")
	for result in search_results:
		msg = response.message(result)

	return str(response)

