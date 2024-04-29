from django.contrib import admin

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display= ('amount', 'description', 'owner', 'category', 'date',)

    
