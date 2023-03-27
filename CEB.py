unit = int(input('\nEnter number of units in decimal : '))
days = int(input ('enter number of days : '))

if unit <= days:
    charge = 30*unit
    fix_charge = 400
elif unit <= days*2:
    charge = 30*days + 37*(unit-days)
    fix_charge = 550
elif unit <= days*3:
    charge = 42*unit
    fix_charge = 650
elif unit <= days*6:
    charge = 42*days*3 + 50*(unit-days*3)
    fix_charge = 1500
elif unit > days*6:
    charge = 42*days*3 + 50*days*3+75*(unit-days*6)
    fix_charge = 2000

if days>=54:
    fix_charge1 = int(round(fix_charge*(days/30),0))
else:
    fix_charge1 = fix_charge

total_charge = charge + fix_charge1
sscl_tax = round(total_charge*0.02564123,2)

charge1 = '{:,}'.format(charge)+'.00'
fix_charge2 = '{:,}'.format(fix_charge1)+'.00'
total_charge1 = '{:,}'.format(total_charge)+'.00'
sscl_tax1 = '{:,}'.format(sscl_tax)
net_charge = '{:,}'.format(total_charge+sscl_tax)

width = max(len(charge1),len(fix_charge2),len(total_charge1),len(sscl_tax1),len(net_charge))

print(f'\nUnit  Charge : {charge1.rjust(width)}')
print(f'Fix   Charge : {fix_charge2.rjust(width)}')
print(f'total Charge : {total_charge1.rjust(width)}')
print(f'SSCL Tax     : {sscl_tax1.rjust(width)}')
print(f'Net Charge   : {net_charge.rjust(width)}')