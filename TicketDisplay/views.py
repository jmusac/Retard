from django.shortcuts import render
from .models import Tickets, Objectcustomfieldvalues
from django.db.models import Q
import json
from django.utils.html import strip_tags
from django.http import HttpResponse
import html
from datetime import datetime, date, timedelta
from django.contrib.auth.decorators import login_required
from .queries import *

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
	problem_desc = ''

	last_3_tickets = get_last_3_tickets() # obtaining only "Sluzba za Informatiku" last 3 tickets

	for ticket in last_3_tickets:
		ticket_dict = {'broj_ticketa': ticket.id, 'naslov': ticket.subject, 'prijavitelj': ticket.creator.realname, 'mail': ticket.creator.emailaddress}
		custom_fields = return_custom_field_dict(ticket) #Return dictionary with custom field values for given ticket
		ticket_dict["custom_fields"] = custom_fields
		
		#if ticket.queue.id: #Try-except je za potrebe onih koji ne unose opis problema pa on ostane prazan
		try:
			problem_desc = ticket.transactions_set.all()[1].attachments_set.all()[1].content.decode()[:600]
			problem_desc = html.unescape(problem_desc)
		except:
			problem_desc = "Nije unesen"
		#else:
		if problem_desc == "Nije unesen":
			try:
				problem_desc = ticket.transactions_set.all()[1].attachments_set.first().content.decode()[:600]
				problem_desc = html.unescape(problem_desc)
			except:
				probem_desc = "Nije unesen"
		if problem_desc == "Nije unesen":
			try:
				problem_desc = ticket.transactions_set.all()[2].attachments_set.all[1].content.decode()[:600]
				problem_desc = html.unescape(problem_desc)
			except:
				probem_desc = "Nije unesen"
		if problem_desc == "Nije unesen":
			try:
				problem_desc = ticket.transactions_set.first().attachments_set.first().content.decode()[:600]
				problem_desc = html.unescape(problem_desc)
			except:
				probem_desc = "Nije unesen"

		problem_desc = strip_tags(problem_desc)
		ticket_dict["opis_problema"] = problem_desc

		tickets.append(ticket_dict)

	return tickets

@login_required
def dashboard(request):

	current_date = date.today()
	created_tickets = []
	resolved_tickets = []
	created_tickets_big = []
	resolved_tickets_big = []
	day_names = []
	dates = []
	total_new = []
	total_open = []
	total_new_7 = []
	total_open_7 = []
	solver_list = []
	header_data = {}
	rankings = {}
	rankings_hours = {}
	rankings_30 = {}
	rankings_hours_30 = {}
	distribution = {}
	distribution_hours = {}
	distribution_big = {}
	distribution_hours_big ={}


	for i in range(7,0,-1):
		delta = timedelta(days=i-1)
		past_date = current_date - delta

		count = get_created_on_date(past_date).count()
		day_name = html.unescape(past_date.strftime("%A"))
		day_names.append(day_name)
		created_tickets.append(count)

		count =  get_resolved_on_date(past_date).count()
		resolved_tickets.append(count)


	for j in range(30,0,-1):
		delta = timedelta(days=j-1)
		past_date = current_date - delta

		dates.append(past_date.strftime("%d.%m"))
		count = get_created_on_date(past_date).count()
		created_tickets_big.append(count)

		count = get_resolved_on_date(past_date).count()
		resolved_tickets_big.append(count)


	for n in range(7,0,-1):
		delta = timedelta(days=n-1)
		past_date = current_date - delta
		count_total_7 = get_tickets_created_before_resolved_after(past_date).count()
		count_new_7 = get_tickets_created_before_started_after(past_date).count()
		total_new_7.append(count_new_7)
		count_open_7 = count_total_7 - count_new_7
		total_open_7.append(count_open_7)

	for k in range(30,0,-1):
		delta = timedelta(days=k-1)
		past_date = current_date - delta
		count_total = get_tickets_created_before_resolved_after(past_date).count()
		count_new = get_tickets_created_before_started_after(past_date).count()
		total_new.append(count_new)
		count_open = count_total - count_new
		total_open.append(count_open)

	solved_today = get_solved_tickets_today(current_date)
	if(solved_today.count() == 0):
		header_data["today_count"] = 0
		header_data["best_today"] = "No solved tickets"
		header_data["best_today_count"] = 0
	
	else:
		header_data["today_count"] = solved_today.count()
		for ticket in solved_today:
			solver_list.append(ticket.lastupdatedby.realname)
		header_data["best_today"] = max(set(solver_list), key=solver_list.count)
		header_data["best_today_count"] = solver_list.count(header_data["best_today"])

	solver_list=[]

	solved_month = get_solved_tickets_month(current_date)
	header_data["month_count"] = solved_month.count()
	
	for ticket in solved_month:
		solver_list.append(ticket.lastupdatedby.realname)

	header_data["best_month"] = max(set(solver_list), key=solver_list.count)
	header_data["best_month_count"] = solver_list.count(header_data["best_month"])
	
	#Employee ranking card

	#Ranking card - Solved and hours for last 7 days
	delta = timedelta(days=6)
	past_date = current_date - delta

	solved_week = get_solved_tickets_last_x_days(past_date)
	for ticket in solved_week:
		#Counstruct dictionary of employees with number of solved tickets
		if ticket.lastupdatedby.realname not in rankings:
			rankings[ticket.lastupdatedby.realname] = 1
		else:
			rankings[ticket.lastupdatedby.realname] += 1
			
		if ticket.lastupdatedby.realname not in rankings_hours:
			rankings_hours[ticket.lastupdatedby.realname] = ticket.timeworked/60
			rankings_hours[ticket.lastupdatedby.realname] = round(rankings_hours[ticket.lastupdatedby.realname],1)
		else:
			rankings_hours[ticket.lastupdatedby.realname] += ticket.timeworked/60
			rankings_hours[ticket.lastupdatedby.realname] = round(rankings_hours[ticket.lastupdatedby.realname],1)

	rankings = {k: v for k, v in sorted(rankings.items(), reverse=True, key=lambda item: item[1])}
	rankings_hours = {k: v for k, v in sorted(rankings_hours.items(), reverse=True, key=lambda item: item[1])}

	if len(rankings) > 6: #Select only first 6 to display in template
		rankings = dict(list(rankings.items())[0:5])

	if len(rankings_hours) > 6: #Select only first 6 to display in template
		rankings_hours = dict(list(rankings_hours.items())[0:5])

	#Pie Charts
	tickets = get_tickets_current_month(current_date)
	for ticket in tickets:
		label = ticket.queue.name.replace('Služba za informatiku - ','')
		if label not in distribution:
			distribution[label] = 1
		else:
			distribution[label] +=1
		if label not in distribution_hours:
			distribution_hours[label] = ticket.timeworked/60
			distribution_hours[label] = round(distribution_hours[label],1)
		else:
			distribution_hours[label] += ticket.timeworked/60
			distribution_hours[label] = round(distribution_hours[label],1)

	delta = timedelta(days=90)
	past_date = current_date - delta
	tickets = get_tickets_last_3_months(past_date)
	for ticket in tickets:
		label = ticket.queue.name.replace('Služba za informatiku - ','')
		if label not in distribution_big:
			distribution_big[label] = 1
		else:
			distribution_big[label] +=1
		if label not in distribution_hours_big:
			distribution_hours_big[label] = ticket.timeworked/60
			distribution_hours_big[label] = round(distribution_hours_big[label],1)
		else:
			distribution_hours_big[label] += ticket.timeworked/60
			distribution_hours_big[label] = round(distribution_hours_big[label],1)

	#Ranking card - Solved and hours for last 30 days
	delta = timedelta(days=29)
	past_date = current_date - delta
	solved_month = get_solved_tickets_last_x_days(past_date)

	for ticket in solved_month:
		#Counstruct dictionary of employees with number of solved tickets
		if ticket.lastupdatedby.realname not in rankings_30:
			rankings_30[ticket.lastupdatedby.realname] = 1
		else:
			rankings_30[ticket.lastupdatedby.realname] += 1

		if ticket.lastupdatedby.realname not in rankings_hours_30:
			rankings_hours_30[ticket.lastupdatedby.realname] = ticket.timeworked/60
			rankings_hours_30[ticket.lastupdatedby.realname] = round(rankings_hours_30[ticket.lastupdatedby.realname],1)
		else:
			rankings_hours_30[ticket.lastupdatedby.realname] += ticket.timeworked/60
			rankings_hours_30[ticket.lastupdatedby.realname] = round(rankings_hours_30[ticket.lastupdatedby.realname],1)

	rankings_30 = {k: v for k, v in sorted(rankings_30.items(), reverse=True, key=lambda item: item[1])}
	rankings_hours_30 = {k: v for k, v in sorted(rankings_hours_30.items(), reverse=True, key=lambda item: item[1])}

	if len(rankings_30) > 6: #Select only first 6 to display in template
		rankings_30 = dict(list(rankings_30.items())[0:6])

	if len(rankings_hours_30) > 6: #Select only first 6 to display in template
		rankings_hours_30 = dict(list(rankings_hours_30.items())[0:6])

	context = {
		'day_names': day_names,
		'dates': dates,
		'created_7': created_tickets,
		'resolved_7': resolved_tickets,
		'created_30': created_tickets_big,
		'resolved_30': resolved_tickets_big,
		'new': total_new,
		'open': total_open,
		'new_7': total_new_7,
		'open_7': total_open_7,
		'header': header_data,
		'rankings': rankings,
		'rankings_30': rankings_30,
		'rankings_hours': rankings_hours,
		'rankings_hours_30': rankings_hours_30,
		'category': list(distribution.keys()),
		'category_count': list(distribution.values()),
		'hours_category': list(distribution_hours.keys()),
		'hours_count': list(distribution_hours.values()),
		'category_big': list(distribution_big.keys()),
		'category_count_big': list(distribution_big.values()),
		'hours_category_big': list(distribution_hours_big.keys()),
		'hours_count_big': list(distribution_hours_big.values())
	}

	return render(request, 'TicketDisplay/dashboard.html', context)
