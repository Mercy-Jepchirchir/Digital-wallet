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
    list_display = ( 'balance',)
    search_fields = (' date_created','balance',)
admin.site.register(Wallet,WalletAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('message',)
    search_fields = ('date_created','balance',)
admin.site.register(Transaction,TransactionAdmin)

class cardAdmin(admin.ModelAdmin):
    list_display = ('card_number','expiry_date')
    search_fields = ('card_number','expiry_date')
admin.site.register(Card,cardAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message','date','recipient','title')
    search_fields = ('message','date','recipient','title')
admin.site.register(Notification,NotificationAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_number','date')
    search_fields = ('transaction','receipt_number','date')
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ('loan_id','date','interest_rate','guaranter')
    search_fields = ('loan_id','date','loan_balance','issuer')
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display = ('recipient','points','bonus')
    search_fields = ('date_of_reward ',' points','date',' bonus',' recipient ')
admin.site.register(Reward,RewardAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('country','symbol',)
    search_fields = ('country','symbol',' amount')
admin.site.register(Currency,CurrencyAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display = ('issuer','transaction_amount','date_of_issue','wallet')
    search_fields = ('issuer','transaction_amount','date_of_issue','wallet')
admin.site.register(ThirdParty,ThirdPartyAdmin)




