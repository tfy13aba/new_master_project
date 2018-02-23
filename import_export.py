import os

#
#IMPORT
#

## DATA SET ##

def import_data_set_to_int(input_folder_path):
    data_set_int = []
    files_in_folder = os.listdir(input_folder_path)
    for file_name in files_in_folder:
        data_set = import_data(input_folder_path, file_name)
        data_set_int.extend(convert_to_int(data_set))
    return data_set_int

def import_data(input_folder_path, file_name):
        with open(input_folder_path + file_name, 'r') as raw_file:      #Import datafile
            raw_data = raw_file.read().splitlines()                     #Convert to vector, each slot has a string rep. of datapoint
        return raw_data

## CLUSTER SET ##

def import_cluster_from_file(cluster_source_file):
    clustered_data = []
    with open(cluster_source_file, 'r') as raw_file:
       raw_data = raw_file.read().split()
    data_iter = iter(raw_data)
    nbr_time_clusters = int(data_iter.__next__())
    
    for i in range(nbr_time_clusters):
        clustered_data.append(load_time_cluster(data_iter))
        
    return clustered_data


#
#EXPORT
#    

## DATA SET ##

def write_reduced_data_to_file(reduced_data_folder_path, reduced_raw_data_int, t_min, t_max, q_thres):
    filepath = reduced_data_folder_path + 'Reduced_Data(t_min_' + str(t_min) + ',t_max_' + str(t_max) + ',q_threshold_' + str(q_thres) + ')' + '.txt'
    output_file = open(filepath,'a+')
    
    for datapoint in reduced_raw_data_int:
        export_datapoint(output_file, datapoint)
        output_file.write('\n')
        
## CLUSTER SET ##
        
def save_cluster_to_file(cluster_output_file_path, clustered_data):
    output_file = open(cluster_output_file_path, 'a')
    output_file.write(str(len(clustered_data)) + ' ')                              #Writes how many time clusters are in our file
    for time_cluster in clustered_data:
        write_time_cluster_to_file(output_file, time_cluster)
    output_file.close()          
        
     

#
#HELPER FUNCTIONS
#
    
#
#IMPORT
#

## DATA SET ## 
  
def convert_to_int(raw_data):
    raw_data_int = []                                                  
    for datapoint in raw_data:                                                                  
        datapoint = datapoint.split()                                   #Split string rep. of datapoint, one slot per value
        datapoint = [int(i) for i in datapoint]                         #Convert each value in datapoint to int
        raw_data_int.append(datapoint)
    
    return raw_data_int    
    
## CLUSTER SET ##    
    
def load_time_cluster(data_iter):
    time_cluster = []
    nbr_spatial_clusters = int(data_iter.__next__())
    
    for i in range(nbr_spatial_clusters):
        time_cluster.append(load_spatial_cluster(data_iter))
    
    return time_cluster

def load_spatial_cluster(data_iter):
    spatial_cluster = []
    spatial_cluster.append(str(data_iter.__next__()))
    spatial_cluster.append(int(data_iter.__next__()))
    nbr_datapoints = int(data_iter.__next__())
    
    datapoint_collection = []
    for i in range(nbr_datapoints):
        datapoint = []
        for i in range(4):
            datapoint.append(int(data_iter.__next__()))
        datapoint_collection.append(datapoint)    
    
    spatial_cluster.append(datapoint_collection)   
     
    return spatial_cluster
    
#
#EXPORT
#

## DATA SET ## 
    
def export_datapoint(output_file, datapoint):
    for i in range(3):
        output_file.write(str(datapoint[i]) + ' ')
    output_file.write(str(datapoint[3]))  

## CLUSTER SET ##      
        
def write_time_cluster_to_file(output_file, time_cluster):
    output_file.write(str(len(time_cluster)) + ' ')                                 #Writes how many spatial clusters are in our time cluster
    for spatial_cluster in time_cluster:
        write_spatial_cluster_to_file(output_file, spatial_cluster)
    
def write_spatial_cluster_to_file(output_file, spatial_cluster):
    output_file.write(spatial_cluster[0] + ' ')
    output_file.write(str(spatial_cluster[1]) + ' ')
    output_file.write(str(len(spatial_cluster[2])) + ' ')                           #Writes how many datapoints are in our cluster
    for datapoint in spatial_cluster[2]:
        write_datapoint_to_file(output_file, datapoint)

def write_datapoint_to_file(output_file, datapoint):
    for i in datapoint:
        output_file.write(str(i) + " ")








