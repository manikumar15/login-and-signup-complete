from django.contrib import admin
from .models import Register,Enquiry,News
import decimal, csv
from django.http import HttpResponse

admin.site.site_header = 'Mani Kumar'

def export_books(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    writer = csv.writer(response)
    writer.writerow(['name','email','password'])
    books = queryset.values_list('name','email','password')
    for book in books:
        writer.writerow(book)
    return response
export_books.short_description = 'Export to csv'
class Registeradmin(admin.ModelAdmin):
    list_display = ('name','email','password')
    list_filter = ('name',)
    search_fields = ('name',)
    actions = ['', export_books]

admin.site.register(Register,Registeradmin)

class Enquiryadmin(admin.ModelAdmin):
    list_display = ('name','email','phone','jobtype')
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Enquiry,Enquiryadmin)

class Newsadmin(admin.ModelAdmin):
    list_display = ('Email',)

admin.site.register(News, Newsadmin)
