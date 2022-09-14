from unicodedata import name
from django.urls import path
from .  import views
# from .views import list_customers, register_thirdparty,register_notification,register_customer,register_currency,register_wallet,register_account,register_transaction,register_card,register_receipt,register_loan,register_reward


urlpatterns = [
    path("register/",views.register_customer,name="registration"),
    path("currency/",views.register_currency,name="currency"),
    path("wallet/",views.register_wallet,name="wallet"),
    path("account/",views.register_account,name="Account"),
    path("transaction/",views.register_transaction, name="transaction"),
    path("card/",views.register_card,name="card"),
    path("thirdparty/",views.register_thirdparty,name="thirdparty"),
    path("notification/",views.register_notification,name="Notification"),
    path("receipt/",views.register_receipt,name="receipt"),
    path("loan/",views.register_loan,name="loan"),
    path("reward/",views.register_reward,name="reward"),
    path("customers/",views.list_customers,name="customers"),
    path("currencys/",views.list_currency,name= "list_currencys"),
    path("wallets/",views.list_wallet,name= "list_wallet"),
    path("accounts/",views.list_account,name="accounts"),
    path("cards/",views.list_card,name="cards"),
    path("loan/",views.list_loan,name="loans"),
    path("notifications/",views.list_notification,name="notifications"),
    path("receipts/",views.list_receipt,name="receipts"),
    path("rewards/",views.list_reward,name="rewards"),
    path("transactions/",views.list_transaction,name="transactions"),
    path("thirdpartys/",views.list_thirdparty,name="thirdpartys"),
    
    
    
]
