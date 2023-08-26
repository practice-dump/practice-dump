# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:23:59 2020

@author: TANMEY
DMML assignment 1
"""
import numpy as np
import pandas as pd
#pip install mlxtend run this command when you are using mlxtend library for first time
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import time 



def find_k_frequent_itemset(K,F,file_name):
    start_time=time.time()
    vocab_kos=np.loadtxt("T:/sem2/DMML_DS/assignment/vocab."+file_name+".txt",dtype="str")
    
    words_kos=np.loadtxt("T:/sem2/DMML_DS/assignment/docword."+file_name+".txt/docword."+file_name+".txt",dtype="str",delimiter='\s',skiprows=3)
    
    document_info=np.loadtxt("T:/sem2/DMML_DS/assignment/docword."+file_name+".txt/docword."+file_name+".txt",dtype="str",delimiter='\n',max_rows=3)
    
    number_of_documents=int(document_info[0])
    # number_of_words_in_vocab=int(document_info[1])
    # total_words=int(document_info[2])
    
    document=[]
    for i in range(0,number_of_documents):
        document.append([])
    for temp_0 in words_kos:
        doc_info=temp_0.split(" ")
        doc_id=int(doc_info[0])
        word_id=int(doc_info[1])
        document[doc_id-1].append(vocab_kos[word_id-1])
                
    transaction_encoder=TransactionEncoder()
    sparse_transaction_encoder=transaction_encoder.fit(document).transform(document,sparse=True)
    sparse_df=pd.DataFrame.sparse.from_spmatrix(sparse_transaction_encoder,columns=transaction_encoder.columns_)
    
    frequent_itemsets=apriori(sparse_df, min_support=F, use_colnames=True,verbose=1,low_memory=False,max_len=K)
    frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
    frequent_itemsets_k=frequent_itemsets['itemsets'][frequent_itemsets['length']==K]
    output_list=list(frequent_itemsets_k)
    if len(output_list) ==0:
        print("Dataset doesn't have "+str(K)+" frequent pairs for "+str(F)+" support.Try other values of K and minimum support" )
    else:
        print("Check working directory a csv file has been generated with file_name_K_F")
        df = pd.DataFrame(data={"Frequent Pairs": output_list})
        df.to_csv("./"+str(file_name)+"_"+str(K)+"_"+str(F)+".csv", sep=',',index=False)
            
    end_time=time.time()
    print("Time taken to find "+str(K)+" frequent itemsets for "+str(F)+" Support is " +str(round(end_time-start_time,2))+" seconds")
    return output_list    
    
zetta=find_k_frequent_itemset(3,.15,"kos") 