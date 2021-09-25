from django.contrib import admin
from .models import Bill, BillComment, Debate, DebateComment

# Register your models here.
admin.site.register(Bill)
admin.site.register(BillComment)

admin.site.register(Debate)
admin.site.register(DebateComment)
