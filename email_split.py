def pk_split(pk):
    split_1 = pk.split('@')
    split_2 = split_1[1].split('-')

    email = split_1[0] + '@' + split_2[0]
    to_remove = email + '-'
    pet_name = pk.replace(to_remove, '')

    print(f'email: {email}')
    print(f'pet name: {pet_name}')
    return
    
case_1 = 'markmintel@gmail.com-Ringo'
case_2 = 'markmintel@gmail.com-Ringo@Dingo'
case_3 = 'markmintel@gmail.com-Ringo-Dingo'
case_4 = 'markmintel@gmail.com-Ringo@Dingo-Bingo'

pk_split(case_1)
pk_split(case_2)
pk_split(case_3)
pk_split(case_4)
