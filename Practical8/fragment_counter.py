seq= 'ATGCAATCGACTACGATCAATCGAGGGCC'
number=seq.find('GAATTC')
if number>0:
    print(str(number+1)+' fragments will be cut.')
else:
    print('This sequence will not be cut if we applied the EcoRI enzyme to it.\nSo there is only one fragment')