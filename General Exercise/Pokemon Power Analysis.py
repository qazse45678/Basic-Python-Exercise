import pprint

f = open('/Users/marylin/Downloads/Python/pokemon.txt')
f_2 = open('/Users/marylin/Downloads/Python/attribute.txt')
d = {}
d_2 = {}
d_2_list = []
pokemon = []
enemy = input('請輸入敵人編號：')
#pokemon_attribute_1 = ''
#pokemon_attribute_2 = ''
result = 0


#d (寶可夢清單)
for line in f:
    line = line.strip('\n')
    line_split = line.split('\t')
    key = line_split[0]
    ch_name = line_split[1]
    en_name = line_split[2]
    attribute_1 = line_split[3]
    
    if len(line_split) == 5:
        attribute_2 = line_split[4]
    else:
        attribute_2 = ''
    
    d[key] = [
            ch_name,
            en_name,
            attribute_1,
            attribute_2
    ]

#d_2 (攻擊屬性清單)
for line in f_2:
    line = line.strip('\n')
    line = line.split('\t')
    key = line[0]
    d_2_list.append(key)
    d_2[key] = []
    for item in range(1, len(line)):
        d_2[key].append(line[item])

#算出相剋倍率，但缺少自動從給定寶可夢名稱抓屬性中文，然後少迴圈自動 run 四隻給定寶可夢

for line in d:
                
    #我方屬性
    pokemon_attribute_1 = d[line][2] # sample: 火
    pokemon_attribute_2 = d[line][3]
            
    #敵方屬性
    enemy_1 = d[enemy][2] # sample: 火
    enemy_2 = d[enemy][3] # sample: 飛行
            
    #我方找敵方 d_2 key
    enemy_index_1 = d_2_list.index(enemy_1) #火是 d_2 的第幾個 key
    enemy_index_2 = d_2_list.index(enemy_2) 
            
    #敵方找我方 d_2 key
    pokemon_index_1 = d_2_list.index(pokemon_attribute_1)
    if pokemon_attribute_2 != '':
        pokemon_index_2 = d_2_list.index(pokemon_attribute_2)
            
    #攻擊敵方相剋倍率
    multiplier_1 = float(d_2[pokemon_attribute_1][enemy_index_1]) * float(d_2[pokemon_attribute_1][enemy_index_2])
    if pokemon_attribute_2 != '':
        multiplier_2 = float(d_2[pokemon_attribute_2][enemy_index_1]) * float(d_2[pokemon_attribute_2][enemy_index_2])
    else:
        multiplier_2 = multiplier_1
    if multiplier_1 == 0 and multiplier_2 == 0:
        max_pokemon = 1
    else:
        max_pokemon = max(multiplier_1, multiplier_2)
            
    #敵方攻擊己方相剋倍率
    multiplier_3 = float(d_2[enemy_1][pokemon_index_1]) * float(d_2[enemy_1][pokemon_index_2])
    if enemy_2 != '':
        multiplier_4 = float(d_2[enemy_2][pokemon_index_1]) * float(d_2[enemy_2][pokemon_index_2])
    else:
        multiplier_4 = multiplier_3
            
    result = (max(multiplier_3, multiplier_4) / max_pokemon)
        
    if result > 1:
        pokemon.append(d[line][0])

pokemon
