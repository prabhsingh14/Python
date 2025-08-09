from django.contrib import admin
from .models import ChaiVarity, ChaiReview, Store, ChaiCertificate

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1

#ModelAdmin means we are customizing the admin interface for the ChaiVarity model
class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
     list_display = ('name', 'location')
     filter_horizontal = ('chai_varieties',)
    
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'issued_to', 'issued_on', 'valid_until')


admin.site.register(ChaiVarity, ChaiVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
