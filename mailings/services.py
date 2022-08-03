import imp
from typing import Union
from cases.models import Case
from mailings.mailchimp_services import add_mailchimp_email_with_tag
from mailings.models import CommonMailingList,CaseMailingList


def add_email_to_common_mailchimp_list(email: str):
    #добовляем email в общий лист рассылок
    add_mailchimp_email_with_tag(audience_name='COMMON',
                                 email=email,
                                 tag='COMMON TAG')
    CaseMailingList.objects.get_or_create(email=email)
    
def add_email_to_cases_mailchimp_list(email:str, case_id:Union [int, str]):
    #Добовляет email в лист рассылки по делу
    case = Case.objects.get(pk=case_id)
    add_mailchimp_email_with_tag(audience_name='CASES',
                                 email=email,
                                 tag= f'Case{case.name}')
    CaseMailingList.objects.get_or_create(email=email)