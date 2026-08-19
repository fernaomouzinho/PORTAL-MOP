from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from portal.utils import get_roles
from django.db.models.functions import ExtractYear
from django.db.models import Count
from news.models import News,NewsCat
from pub.models import TenderCategory,Tender 
from django.utils.timezone import now
from django.db.models import Count, Sum, Q


@allowed_users(allowed_roles=['sii_admin','portal_admin','portal_media','portal_dna'])
def admin_home(request):
    roles = get_roles(request)
    current_year = now().year
    # TOTAL NEWS
    total_news = News.objects.filter(is_active=True).count()
    this_year_news = News.objects.filter(is_active=True,date__year=current_year).count()
    # TOTAL TENDER
    total_tender = Tender.objects.filter(is_active=True).count()
    this_year_tender = Tender.objects.filter(is_active=True,publish_date__year=current_year).count()
    
    category_summary = (
        NewsCat.objects.annotate(total_news=Count("news",filter=Q(news__is_active=True)),
            total_this_year=Count("news",filter=Q(news__is_active=True,news__date__year=current_year)),
            total_views=Sum("news__hits",filter=Q(news__is_active=True))).order_by("name_tt"))
    
    category_tender = TenderCategory.objects.annotate(
        total=Count("tender"),this_year=Count("tender",filter=Q(tender__datetime__year=current_year)),
        open_total=Count("tender",filter=Q(tender__status="open")),
        closed_total=Count("tender",filter=Q(tender__status="closed")),
        awarded_total=Count("tender", filter=Q(tender__status="awarded")),)
    
    return render(request, 'web_admin/home.html', {
        "roles": roles,
        "title": "Suamario",
        "current_year":current_year,
        "total_news": total_news,
        "this_year_news": this_year_news,
        "total_tender": total_tender,
        "this_year_tender": this_year_tender,
        "category_summary":category_summary,
        "category_tender":category_tender,
    })

def error_404(request, exception):
        data = {}
        return render(request,'web_admin/404.html', data)

def error_500(request):
        data = {}
        return render(request,'web_admin/500.html', data)

