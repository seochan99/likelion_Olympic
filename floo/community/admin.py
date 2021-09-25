from django.contrib import admin
from .models import Bill, BillComment, TalkRoom, Debate, DebateComment

# Register your models here.
admin.site.register(Bill)
admin.site.register(BillComment)
admin.site.register(TalkRoom)
admin.site.register(Debate)
admin.site.register(DebateComment)