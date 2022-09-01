from django.urls import path
from .views import register_thirdparty,register_notification,register_customer,register_currency,register_wallet,register_account,register_transaction,register_card,register_receipt,register_loan,register_reward


urlpatterns = [
    path("register/",register_customer,name="registration"),
    path("currency/",register_currency,name="currency"),
    path("wallet/",register_wallet,name="wallet"),
    path("account/",register_account,name="Account"),
    path("transaction/",register_transaction, name="transaction"),
    path("card/",register_card,name="card"),
    path("thirdparty/",register_thirdparty,name="thirdparty"),
    path("notification/",register_notification,name="Notification"),
    path("receipt/",register_receipt,name="receipt"),
    path("loan/",register_loan,name="loan"),
    path("reward/",register_reward,name="reward")
    
    
]
