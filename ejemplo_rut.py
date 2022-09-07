#    01234567890
rut="123456789-k"
# rut="2222-k"
# quiero obtener el digito verificador.
print(rut[10:11]) # desde el caracter 10 hasta el 111
print(rut[-1])  # el ultimo caracter
print(rut.split('-')[1]) # divido el texto por un "-" y obtengo el segunndo elemento

# quiero obtener el numero sin el digito verificador
rut="     12.345.678-k"
print(rut[0:-2])  # desde la posicion 0, obtengo -2 caract. (quito los 2 carac)
print(rut.split('-')[0])

print(rut.strip().replace('.','').split('-')[0]) # quita espacios al comienzo o al finbal



