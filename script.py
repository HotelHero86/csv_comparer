import numpy as np
import pandas as pd


archidekt_list = "archidekt-collection-export-2026-10-28.csv"
deckstats_list = "collection_202300_1793150063.csv"

df_a = pd.read_csv(archidekt_list)
df_d = pd.read_csv(deckstats_list)

trans_a = df_a[['Quantity','Name','Finish','Edition Code']]
trans_d = df_d[['amount','card_name','is_foil','set_code']]

trans_d['is_foil'] = trans_d['is_foil'].replace({0: 'Normal', 1: 'Foil'})

trans_a = trans_a.rename(columns = {'Quantity':'amount', 'Name' : 'card_name', 'Finish': 'is_foil', 'Edition Code':'set_code' })

print(trans_a.head())
print(trans_d.head())

merged = trans_a.merge(trans_d, how='outer', indicator = True)

only_in_archidekt = merged[merged['_merge'] == 'left_only']
only_in_deckstats = merged[merged['_merge'] == 'right_only']


print(only_in_archidekt.head())
print(only_in_deckstats.head())

only_in_deckstats.to_csv('only_in_deckstats.csv', index = False)
only_in_archidekt.to_csv('only_in_archidekt.csv', index = False)