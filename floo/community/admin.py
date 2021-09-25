from django.contrib import admin
from .models import Bill, BillComment, TalkRoom_Y, TalkRoom_F, Debate, DebateComment

# Register your models here.
admin.site.register(Bill)
admin.site.register(BillComment)
admin.site.register(TalkRoom_Y)
admin.site.register(TalkRoom_F)
admin.site.register(Debate)
admin.site.register(DebateComment)
