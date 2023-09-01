case_1 = 'markmintel@gmail.com-Ringo'
case_2 = 'markmintel@gmail.com-Ringo@Dingo'
case_3 = 'markmintel@gmail.com-Ringo-Dingo'
case_4 = 'markmintel@gmail.com-Ringo@Dingo-Bingo'

def pk_split(pk):
    split_1 = pk.split('@')
    if len(split_1) == 2:
        split_2 = split_1[1].split('-')
        if len(split_2) == 2:
            email = split_1[0] + '@' + split_2[0]
            pet_name = split_2[1]
        else:
            email = split_1[0] + '@' + split_2[0]
            pet_name = '-'.join(split_2[1:])
    else:
        corrected = '@'.join(split_1[1:])
        split_2 = corrected.split('-')
        if len(split_2) == 2:
            email = split_1[0] + '@' + split_2[0]
            pet_name = split_2[1]
        else:
            email = split_1[0] + '@' + split_2[0]
            pet_name = '-'.join(split_2[1:])
    
    print(f'email: {email}')
    print(f'pet name: {pet_name}')
    return
        

pk_split(case_1)
pk_split(case_2)
pk_split(case_3)
pk_split(case_4)
