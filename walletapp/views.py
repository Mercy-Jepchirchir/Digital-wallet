from django.shortcuts import render
from . import models
from . import forms

# Create your views here.
#read what is actually contained in a request
def register_customer(request):
    if request.method == "POST":
        form = forms.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerRegistrationForm()     
    return render(request,'wallet/register_customer.html',
                  {"form":form})
    
    #list for customers
def list_customers(request):
    customers = models.Customer.objects.all()
    return render (request, 'wallet/customers_list.html',
                   {"customers":customers})
    

def register_currency(request):
    if request.method == "POST":
          form = forms.CurrencyRegistrationForm(request.POST)
          if form.is_valid():
              form.save()
              
    else:
        form= forms.CurrencyRegistrationForm()
        return render(request,'wallet/register_currency.html',
                  {"form":form})

def list_currency(request):
    currencys = models.Currency.objects.all()
    return render (request,'wallet/currency_list.html',
                   {"currencys":currencys})
  
    
    
def register_wallet(request):
    if request.method == "POST":
         form = forms.WalletRegistrationForm(request.POST)
         if form.is_valid():
             form.save()
             
    else:
        form = forms.WalletRegistrationForm()
        return render(request,'wallet/register_wallet.html',
                  {"form":form})
        
def list_wallet(request):
    wallets = models.Wallet.objects.all()
    return render (request,'wallet/list_wallet.html',
                   {"wallets":wallets})         
         

def register_account(request):
    if request.method == "POST":
        form = forms.AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = forms.AccountRegistrationForm()
        return render(request,'wallet/register_account.html',
                  {"form":form})
        
def list_account(request):
    accounts = models.Account.objects.all()
    return render (request,'wallet/list_account.html',
                   {"accounts ": accounts}) 
                
def register_transaction(request):
    if form.method == "POST":
        form = forms.TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = forms.TransactionRegistrationForm()
        return render(request,'wallet/register_transactionn.html',
                  {"form":form})

def list_transaction(request):
    transactions = models.Transaction.objects.all()
    return render (request,'wallet/list_transactionn.html',
                   {"transactions ": transactions}) 
 
    
def register_card(request):
    if form.method == "POST":
        form = forms.CardRegistrationForm()
        if form.is_valid():
            form.save()
        
    else:
        form= forms.CardRegistrationForm()
        return render(request,'wallet/register_card.html',
                  {"form":form})

def list_card(request):
    cards = models.Card.objects.all()
    return render (request,'wallet/list_card.html',
                   {"cards ": cards})
    

def register_thirdparty(request):
    if form.method == "POST":
        form = forms.ThirdpartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = forms.ThirdpartyRegistrationForm()
        return render(request,'wallet/register_thirdparty.html',
                  {"form":form})

def list_thirdparty(request):
    thirdpartys = models.ThirdParty.objects.all()
    return render (request,'wallet/list_thirdparty.html',
                   {" thirdpartys ": thirdpartys})
        
        
def register_notification(request):
    if form.method == "POST":
        form = forms.NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = forms.NotificationRegistrationForm()
        return render(request,'wallet/register_notification.html',
                  {"form":form})
        

def list_notification(request):
    notifications = models.Notification.objects.all()
    return render (request,'wallet/list_notification.html',
                   {" notifications": notifications})
   
   
def register_receipt(request):
    if form.method == "POST":
        form = forms.ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save
    
    else:
        form = forms.ReceiptRegistrationForm()
        return render(request,'wallet/register_receipt.html',
                  {"form":form})
        
def list_receipt(request):
    receipts = models.Receipt.objects.all()
    return render (request,'wallet/list_receipt.html',
                   {" receipts": receipts})
        
        
def register_loan(request):
    form.method == "POST"
    form = forms.LoanRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        
    else:
        form = forms.LoanRegistrationForm()
        return render(request,'wallet/register_loan.html',
                  {"form":form})
        
def list_loan(request):
    loans = models.Loan.objects.all()
    return render (request,'wallet/list_loan.html',
                   {"loans": loans})
         
def register_reward(request):
    if form.method == "POST":
        form = forms.RewardsRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    
    else:
        form = forms.RewardsRegistrationForm()
        return render(request,'wallet/register_reward.html',
                  {"form":form})
        
def list_reward(request):
    rewards = models.Reward.objects.all()
    return render (request,'wallet/list_reward.html',
                   {"rewards": rewards })
  

    

    
    

    
    