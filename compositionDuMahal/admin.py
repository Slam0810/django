from django.contrib import admin
from .models import Produit, Contact, Reservation, Presentation
# Register your models here.

#admin.site.register(Produit)
admin.site.register(Contact)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'contacted')
    readonly_fields = ('created_at', 'contacted')
    def has_add_permission(self, request):
        return False

class PresentationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'fonction', 'metier')

class ProduitAdmin(admin.ModelAdmin):
    list_display =('nom', 'image', 'description','etat', 'caracteristic', 'date')
    list_filter = ('nom',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('nom', 'etat', 'caracteristic')
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Reservation, ReservationAdmin)
