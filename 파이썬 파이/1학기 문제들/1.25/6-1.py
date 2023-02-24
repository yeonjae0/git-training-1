def de_identify(id):
    id_re = id.replace('-','')
    return id_re.replace(id_re[6:],'*'*len(id_re[6:]))


print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))