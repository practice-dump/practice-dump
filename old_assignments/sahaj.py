# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:40:58 2020

@author: TANMEY
"""

#sahaj trial1
n=4
dist=[6,8,3]
price=[100,200,400,6]
cheapest_petrol=min(price)
cost=0
remaining_dist=2*(sum(dist))
next_cheap_dist=0
j=0
i=0
count=0
while(price[i]!=cheapest_petrol):
    j=i
    while(price[i+count]>=price[j]):
        count+=1
    temp_dist_array=dist[j:j+count]
    next_cheap_dist=sum(temp_dist_array)
    cost+=price[j]*next_cheap_dist
    remaining_dist-=next_cheap_dist
    i+=count
    count=0
cost+=remaining_dist*cheapest_petrol

print(cost)