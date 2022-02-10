import sys,os
from vendors.atp.player import Player
from vendors.atp.stats import Stats
from vendors.atp.winloss import WinLoss
from vendors.atp.activity import Activity

from extract.website import Website

stats = Stats(last_name = 'djokovic',  year='2021', surface='all')
stats_url = stats.get_player_url()
print(stats_url)    

# df_serve = stats.get_stats_serve()
# print(df_serve)

# df_return = stats.get_stats_return()
# print(df_return)

wl = WinLoss(last_name = 'djokovic')
wl_url = wl.get_player_url()
print(wl_url)    
df_wl = wl.get()
print(df_wl)


act = Activity(last_name = 'djokovic')
act_url = act.get_player_url()
print(act_url)
df_act = act.get()
print(len(df_act))
print(df_act[0])
print(df_act[-1])

