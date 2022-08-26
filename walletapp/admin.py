from django.contrib import admin
# Register your models here.
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet,Currency

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age','email', )
    search_fields = ('first_name', 'last_name')
admin. site.register(Customer,CustomerAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'account_number', 'account_balance',)
    search_fields = ('account_name', 'account_number', 'account_balance',)
admin.site.register(Account,AccountAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ( 'balance','amount',)
    search_fields = (' date_created','balance',)
admin.site.register(Wallet,WalletAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ('date_created','balance',)
admin.site.register(Transaction,TransactionAdmin)

class cardAdmin(admin.ModelAdmin):
    list_display = ('card_number','expiry_date')
    search_fields = ('card_number','expiry_date')
admin.site.register(Card,cardAdmin)

class ThirdParty(admin.ModelAdmin):
    list_display = ('issuer',)
admin.site.register(ThirdParty)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(Currency)




