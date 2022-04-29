# usage:
    # from readfile import get_all_data
    # X, y = get_all_data()

def get_all_data():
    import numpy as np
    import pandas as pd
    import math
    
    def load_data(input_file, header):
        X = []
        y = []
        with open(input_file, 'r') as f:
            for line in f.readlines():
                data = [(x) for x in line.split(',')]
                X.append(data[:-1])
                y.append(header) 
    
        X = np.array(X)
        y = np.array(y)
    
        return X, y
    
    all_data = pd.DataFrame()
    all_y = pd.DataFrame()
    
    # str_list = ['auki_aki']
    str_list = ['auki_aki', 'kiinni_aki','auki_simo', 'kiinni_simo']
    
    for folder in range(len(str_list)):
    
        for folder_nro in range(1, 11):
            X_4cams = np.array([[]])
            y_4cams = np.array([[]])
            df = pd.DataFrame()
            
            for file_nro in range(4):
                #print(str_list[folder],'/',folder_nro,'/', file_nro)
                X, y = load_data(f'data/{str_list[folder]}/{folder_nro}/out{file_nro}.txt', str_list[folder] )
                X_4cams=np.append(X_4cams, X, axis = 1)
       
                df = pd.DataFrame(X_4cams.astype(float), columns=[f'c{math.floor(i/X.shape[1])}p{i%X.shape[1]}' for i in range(0, X_4cams.shape[1])])
            y_4cams=np.append(y_4cams, [y], axis=1)
            all_data = pd.concat([all_data, df], axis=0)
            all_y = pd.concat([all_y, pd.DataFrame(y_4cams.T)], axis=0)
     
    # 24*32 = 768 || 768*4 = 3072
    
    all_y.columns=['is_open']
    all_y.replace(to_replace =['auki_aki','auki_simo', 'kiinni_aki', 'kiinni_simo'], 
                                value=[1,1,0,0],inplace=True)
    
    # all_data = kaikkien kameroiden kaikki pikselit. [c0p0] = camera 0, pixel 0
    # all_y = y:n arvot. auki 1 / kiinni 0
    return all_data, all_y;
    