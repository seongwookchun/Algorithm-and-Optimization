d_warehouse = {2:{1:{1:1}}}
int_warehouse_size = 100

def gen_seri_multi(nb_seri, idx):
    int_res = 1
    for num in range(idx+1, nb_seri+idx+1):
        int_res *= num
    return int_res

for idx in range(10):
    print(gen_seri_multi(3, idx))


int_target = 10
nb_seri = 2
int_initial = 1*2    # nb_seri = 2, idx = 1
hash1 = int_initial%int_warehouse_size
hash2 = int_initial//int_warehouse_size
int_fivot = d_warehouse[nb_seri][hash1][hash2]
while (int_flag == int_target):
    tmp_obj = gen_seri_multi(nb_seri, idx)
    if tmp_obj > int_fivot:
        int_fivot = tmp_obj
    else:
        idx += 1
        
    print(tmp_obj)



def register(nb_seri, tmp_obj):
    key = nb_seri
    value = tmp_obj

    hash1 = value%int_warehouse_size
    hash2 = value//int_warehouse_size

    if d_warehouse[key][hash1]:
        d_warehouse[key][hash1][hash2] = value
    else:
        d_warehouse[key] = dict()
        d_warehouse[key][hash1] = dict()
        d_warehouse[key][hash1][hash2] = value

