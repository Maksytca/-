# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", ...)

disket_mb = 1.44
kolvo_str = 100
kolvo_strok = 50
kolvo_simv = 25
kolvo_bait = 4

disket_bytes1 = disket_mb * 1024 *1024

disket_bytes2 = kolvo_str * kolvo_strok * kolvo_simv * kolvo_bait

boks = disket_bytes1 // disket_bytes2

print("Количество книг(целых), помещающихся на дискету:", boks)


