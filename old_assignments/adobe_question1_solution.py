# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 01:15:16 2020

@author: TANMEY
"""

def mud_height(wall_positions,wall_height):
    pointer=wall_positions[0]
    all_list=[0]*(wall_positions[-1]+1)
    i=1
    max_height=0
    for j in range(0,len(wall_positions)):
        all_list[wall_positions[j]]=wall_height[j]
    while(i< len(wall_positions)):
        if pointer+1==wall_positions[i]:
            pointer=wall_positions[i]
            i+=1
        else:
            pointer+=1
            temp=max(all_list[pointer],all_list[pointer+1])+1
            all_list[pointer+1]=temp
            max_height=max(max_height,temp)
            
    return max_height

wall_positions=[1,2,4]
wall_height=[7,8,15]
            
print(mud_height(wall_positions,wall_height))