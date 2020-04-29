from django.shortcuts import render
from .models import Tickets, Objectcustomfieldvalues
from django.db.models import Q
from django.core.files import File
import json
from django.utils.html import strip_tags
from django.http import HttpResponse
import html

def home(request):
	tickets = returnTickets()

	context = {
		'tickets': tickets
	}

	return render(request, 'TicketDisplay/home.html', context)

def refresh(request):
	tickets = returnTickets()
	json_string = json.dumps(tickets)

	return HttpResponse(json_string)


def return_custom_field_dict(ticket):
		custom_field_dict = {}
		custom_fields = ticket.objectcustomfieldvalues_set.all()
		for custom_field in custom_fields:
			if custom_field.content is None:
				custom_field.content = 'Nema informacije'
			if "Klinika" in custom_field.customfield.name.strip():
				custom_field.customfield.name = "KZO"
			if "Lokacija" in custom_field.customfield.name.strip():
				custom_field.customfield.name = "Lokacija"
			if "Ime računala" in custom_field.customfield.name.strip():
				custom_field.customfield.name = "Ime računala"
			custom_field_dict.update({custom_field.customfield.name.strip(): custom_field.content.strip()})

		return custom_field_dict

def returnTickets():

	tickets = [] #List of ticket_dict
	ticket_dict = {} #Contains all ticket data
	custom_fields = {} #Dictionary of custom fields
	json_dict = {} #Dict for writing into json file
	top_id = 0 #previous highest ticket
	problem_desc = ''

	last_3_tickets = Tickets.objects.using('ticket-db').filter(Q(queue__id__gt=4 , queue__id__lt=13) | (Q(queue__id=30))
									| (Q(queue__id=32))).order_by('-id')[:3] # obtaining only "Sluzba za Informatiku" last 3 tickets

	with open('TicketDisplay/files/ticket_ids.txt', 'r') as json_file:
		id_s = json.load(json_file)
		json_file.close()

	top_id = id_s["prvi"]

	for ticket in last_3_tickets:
		ticket_dict = {'broj_ticketa': ticket.id, 'naslov': ticket.subject, 'prijavitelj': ticket.creator.realname, 'mail': ticket.creator.emailaddress}
		custom_fields = return_custom_field_dict(ticket) #Return dictionary with custom field values for given ticket
		ticket_dict["custom_fields"] = custom_fields
		
		#if ticket.queue.id: #Try-except je za potrebe onih koji ne unose opis problema pa on ostane prazan
		try:
			problem_desc = ticket.transactions_set.all()[1].attachments_set.all()[1].content.decode()[:800]
			problem_desc = problem_desc = html.unescape(problem_desc)
		except:
			problem_desc = "Nije unesen"
		#else:
		if problem_desc == "Nije unesen":
			try:
				problem_desc = ticket.transactions_set.all()[1].attachments_set.first().content.decode()[:800]
				problem_desc = problem_desc = html.unescape(problem_desc)
			except:
				probem_desc = "Nije unesen"

		problem_desc = strip_tags(problem_desc)
		ticket_dict["opis_problema"] = problem_desc
		if ticket.id > top_id:
			ticket_dict["new"] = True
		else:
			ticket_dict["new"] = False
		tickets.append(ticket_dict)

	json_dict["prvi"] = last_3_tickets[0].id
	json_dict["drugi"] = last_3_tickets[1].id
	json_dict["treci"] = last_3_tickets[2].id

	with open('TicketDisplay/files/ticket_ids.txt','w') as json_file:
		json.dump(json_dict, json_file)
		json_file.close()

	return tickets