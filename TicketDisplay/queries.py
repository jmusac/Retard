from django.db.models import Q
from .models import Tickets, Objectcustomfieldvalues

def get_last_3_tickets():
	#Returns last 3 Sluzba za Informatiku tickets
	tickets = Tickets.objects.using('ticket-db').filter(~Q(status__contains='deleted'),Q(queue__gt=4 , queue__lt=13) | (Q(queue=30))
									| (Q(queue=32))).order_by('-id')[:3]
	return tickets

def get_created_on_date(date):
	#Returns tickets created on date
	tickets = Tickets.objects.using('ticket-db').filter(~Q(status__contains='deleted'), Q(created__date = date), Q(queue__gt=4 , queue__lt=13) 
										| (Q(queue=30)) | (Q(queue=32)))
	return tickets

def get_resolved_on_date(date):
	#Returns tickets resolved on date
	tickets = Tickets.objects.using('ticket-db').filter(~Q(status__contains='deleted'), Q(resolved__date = date), Q(queue__gt=4 , queue__lt=13) 
										| (Q(queue=30)) | (Q(queue=32)))
	return tickets

def get_solved_tickets_today(current_date):
	#Returns QuerySet of solved tickets on current day
	tickets = Tickets.objects.using('ticket-db').filter(~Q(status__contains='deleted'), Q(resolved__date = current_date), Q(queue__gt=4 , queue__lt=13) 
										| (Q(queue=30)) | (Q(queue=32)))
	return tickets


def get_solved_tickets_last_x_days(past_date):
	#Returns QuerySet of solved tickets for last 7 days
	tickets = Tickets.objects.using('ticket-db').filter(~Q(status__contains='deleted'), Q(resolved__date__gte = past_date), Q(queue__gt=4 , queue__lt=13) 
										| (Q(queue=30)) | (Q(queue=32)))
	return tickets


def get_solved_tickets_month(current_date):
	#Returns QuerySet of solved tickets this month
	tickets = Tickets.objects.using('ticket-db').filter(~Q(status__contains='deleted'), Q(resolved__date__month = current_date.month), 
										Q(resolved__date__year = current_date.year), Q(queue__gt=4 , queue__lt=13) 
										| (Q(queue=30)) | (Q(queue=32)))

	return tickets

def get_tickets_current_month(current_date):
	#Returs all tickets created current month
	tickets = Tickets.objects.using('ticket-db').filter(~Q(status__contains='deleted'), Q(created__date__month = current_date.month), 
										Q(created__date__year = current_date.year), Q(queue__gt=4 , queue__lt=13) 
										| (Q(queue=30)) | (Q(queue=32)))
	return tickets

def get_tickets_created_before_resolved_after(past_date):
	#Return all tickets created before date in past and resolved after date in past
	tickets = Tickets.objects.using('ticket-db').filter(~Q(status__contains='deleted'), Q(created__date__lte = past_date), 
										Q(resolved__date='1970-01-01') | Q(resolved__date__gt = past_date), Q(queue__gt=4 , queue__lt=13) 
										| (Q(queue=30)) | (Q(queue=32)))
	return tickets

def get_tickets_created_before_started_after(past_date):
	#Return all tickets created before date in past and started after date in past
	tickets = Tickets.objects.using('ticket-db').filter(~Q(status__contains='deleted'), Q(created__date__lte = past_date), (Q(started__date__gt = past_date) | Q(started__date='1970-01-01')), 
										Q(queue__gt=4 , queue__lt=13) | (Q(queue=30)) | (Q(queue=32)))
	return tickets

def get_tickets_last_3_months(past_date):
	#Return all tickets created in last 3 months
	tickets = Tickets.objects.using('ticket-db').filter(~Q(status__contains='deleted'), Q(created__date__gte = past_date), Q(queue__gt=4 , queue__lt=13) 
										| (Q(queue=30)) | (Q(queue=32)))
	return tickets