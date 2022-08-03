import re
from django.http import JsonResponse
from .services import add_email_to_common_mailchimp_list,add_email_to_cases_mailchimp_list

def add_to_common_list_views(request):
    #Веб-сервис,добовляющий email в общий лист рассылки
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'success':False, 'message':'Передайте email'})
    add_email_to_common_mailchimp_list(email=email)
    return JsonResponse({'success':True})

def add_to_case_list_views(request):
    #Веб-сервис добовляющий email в лист рыассылок по канкретному делу
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'success':False,'message':'Передайте email'})
    case_id = request.GET.get('case_id')
    if not case_id:
        return JsonResponse({'success':False, 'message':'Передайте case id'})
    add_email_to_cases_mailchimp_list(email=email,case_id=case_id)
    return JsonResponse({'success':True})
        