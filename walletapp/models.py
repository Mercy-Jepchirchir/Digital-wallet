# from time import timezone
from django.db import models
from datetime import datetime
# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    address=models.TextField()
    email=models.EmailField(max_length=254)
    phone_number=models.CharField(max_length=13)
    gender=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    GENDER_CHOISES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    nationality = models.CharField(max_length=20,null=True)
    
    
class Currency(models.Model):
    country= models.CharField(max_length=30)
    symbol= models.CharField(max_length=5)
    amount= models.BigIntegerField()
    
    
class Wallet(models.Model):
    balance = models.IntegerField()
    customer = models.ForeignKey("Customer",on_delete=models.CASCADE,related_name='Wallet_customer')
    amount  = models.IntegerField()
    date_created = models.DateTimeField()
    status = models.CharField(max_length=15)
    currency = models.ForeignKey("Currency",on_delete=models.CASCADE,related_name='Wallet_currency')
    history = models.DateTimeField()
    pin = models.IntegerField()
    
class Account(models.Model):
    account_name = models.CharField(max_length=20)
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=20)
    account_balance = models.IntegerField()
    wallet = models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Account_wallet')
    
class Transaction(models.Model):
    message = models.CharField(max_length=100)
    wallet = models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_description = models.CharField(max_length=9)
    transaction_amount = models.BigIntegerField()
    TRANSACTION_CHOICES = (
        ('withdraw','Withdrawal'),
        ('deposit', 'Deposit')
    )
    transaction_charge = models.IntegerField()
    transaction_type = models.CharField(max_length=6)
    receipt = models.ForeignKey("Receipt",on_delete=models.CASCADE,related_name='Transaction_receipt')
    origin_account = models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name='Transaction_origin')
    destination_account = models.ForeignKey("Wallet", on_delete=models.CASCADE,related_name='Transaction_destination')
    
class Card(models.Model):
    card_number= models.IntegerField()
    card_type= models.CharField(max_length=20)
    expiry_date = models.DateField()
    security_code = models.IntegerField()
    date_of_issue = models.DateTimeField()
    pin = models.IntegerField(null=True)
    cardStatus = models.CharField(max_length=50, null=True)
    signature = models.ImageField(null = True)
    wallet= models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Card_wallet')
    account= models.ForeignKey("Account",on_delete=models.CASCADE,related_name='Card_account')
    issuer= models.CharField(max_length=10)
    
class ThirdParty(models.Model):
    account= models.ForeignKey("Account",on_delete=models.CASCADE,related_name='Thirdparty_account')
    transaction_amount= models.BigIntegerField()
    currency = models.ForeignKey("Currency",on_delete=models.CASCADE,related_name='Thirdparty_currency')
    date_of_issue = models.DateTimeField()
    wallet= models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Thirdparty_wallet')
    issuer= models.CharField(max_length=20)
    
class Notification(models.Model):
    STATUS_CHOICE = (
        ('read','read'),
        ('unread','unread'),
    )
    status = models.CharField(max_length=12,choices=STATUS_CHOICE,null=True)
    message= models.CharField(max_length=100)
    date = models.DateTimeField()
    recipient= models.ForeignKey("Customer",on_delete=models.CASCADE,related_name='Thirdparty_recipient')
    title = models.CharField(max_length=20)
    
class Receipt(models.Model):
    receipt_type= models.CharField(max_length = 20)
    date = models.DateTimeField()
    receipt_number= models.IntegerField()
    amount= models.IntegerField()
    receipt_file = models.FileField()
    
class Loan(models.Model):
    loan_id = models.IntegerField()
    date = models.DateTimeField()
    interest_rate = models.IntegerField()
    loan_type = models.CharField(max_length=15)
    loan_balance = models.IntegerField()
    amount = models.IntegerField()
    guaranter = models.CharField(max_length=20)
    issuer = models.CharField(max_length=20)
    wallet = models.ForeignKey("Wallet",on_delete=models.CASCADE,related_name='Loan_wallet')
    
class Reward(models.Model):
    transaction= models.ForeignKey("Transaction",on_delete=models.CASCADE,related_name='Reward_transaction')
    recipient = models.ForeignKey("Customer",on_delete=models.CASCADE,related_name='Reward_recipient')
    date_of_reward = models.DateTimeField()
    points = models.IntegerField() 
    bonus = models.CharField(max_length=25, null=True)


    
    