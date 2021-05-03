name=str(input('Enter the name of the custamer:-->'))
print('The location Code is :-------------------->Angaragatti(alli)')
print('The consummer ID:------------------------->61202071132199')
print("RR NO:------------------------------------>101")
print('Name and Address:------------------------->RAMESHA HUGGER BASAVANNEPPA')
present_reading=int(input("Enter the present reading of the current bill:-->"))
previous_reading=int(input("Enter the prevous reading of the current bill:-->"))
total_number_of_unit=present_reading-previous_reading
print('The total number of the unit used is :------>'+str(total_number_of_unit))
min_charge=float(input('Enter the minimum charge of the electrycity bill:--->'))

print('The amount of the per unit is:--------------->3.85')
amount_per_unit=3.85
total_amount_per_unit=total_number_of_unit*amount_per_unit
print('The total amount for tataly used unit :------>'+str(total_amount_per_unit))
total_amount_pay_by_user_is=total_amount_per_unit+min_charge
print('The total amount(without tax)to pay user:RAMESHA HUGGER BASAVANNEPPA :-->'+str(total_amount_pay_by_user_is))
tax_per_amount=float(input('Enter the tax per amount :-->'))
total_amount_pay_by_user_with_tax=total_amount_pay_by_user_is+total_amount_pay_by_user_is*tax_per_amount/100
extra_amount=float(input('Enter if user pay the extra amount :------------>'))
total_amount_pay=extra_amount+total_amount_pay_by_user_with_tax
print('The total amount pay(with tax) by user RAMESHA HUGGER BASAVANNEPPA:---->'+str(total_amount_pay))
