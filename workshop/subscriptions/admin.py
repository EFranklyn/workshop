from django.contrib import admin

# Register your models here.
from django.utils.timezone import now

from workshop.subscriptions.models import Subscriptions


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'cpf', 'created_at','subscribed_today','paid')
    date_hierarchy = 'created_at'
    search_fields = ('nome', 'email', 'phone', 'cpf', 'create_at')
    list_filter = ('paid', 'created_at')


    actions = ['mark_as_paid']

    def subscribed_today(self,obj):
        return obj.created_at.date() == now().date()

    def mark_as_paid(self,  request, queryset):

        count = queryset.update(paid = True)

        if count == 1:
            msg = '{} Inscrição marcada como paga'

        else:
            msg = ' {} Inscrições marcadas como pagas'

        self.message_user(request,msg.format(count))

    mark_as_paid.short_description = ' Marcar selecionados como Pago'


    subscribed_today.short_description = 'Inscrito hoje'

    subscribed_today.boolean = True

admin.site.register(Subscriptions,SubscriptionModelAdmin)