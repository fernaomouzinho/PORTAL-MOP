from custom.models import Year
from doc.models import Doc, Report, ReportOwner
from django.db.models import Count, Sum, Q
from news.models import News, NewsCat, NewsImage
from main.models import Languague

def front_end(request):
    obj_lang = Languague.objects.all()
    year = Year.objects.all()
    count_report_year = Report.objects.values('date__year').order_by('date__year').annotate(total=Count('id'))
    count_report_own = Report.objects.values('owner__code','owner__name').order_by('owner__code','owner__name').annotate(total=Count('id'))
    count_report_own_year = Report.objects.values('date__year','owner__code').order_by('date__year','owner__code').annotate(total=Count('id'))
    
    all_owner_report = ReportOwner.objects.all()
    
    # News
    newcat = NewsCat.objects.all()
    return dict(obj_lang=obj_lang,year_a=year, count_report_year=count_report_year,count_report_own=count_report_own, all_owner_report=all_owner_report,count_report_own_year=count_report_own_year,newcat=newcat)

