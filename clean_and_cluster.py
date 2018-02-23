
import cluster

#
#MAIN FUNCTIONS
#

def clean_and_cluster(input_folder_path, file_name, t_min, t_max, q_thres, delta_t, cluster_type):
    
    cleaned_data = import_and_clean(input_folder_path, file_name, t_min, t_max, q_thres)    #Import and clean raw data
    clustered_data = []                                                                     
    pos = 0
    
    while pos < len(cleaned_data):                                                                                  #While there is more data in vector, keep producing time clusters
        time_cluster = cluster.create_time_cluster(cleaned_data, delta_t, pos)                                      #Create time cluster
        time_cluster.sort(key=lambda x: x[2])                                                                     #Sort time cluster by channel number
        time_cluster_with_spatial_clusters = cluster.create_time_cluster_with_spatial_clusters(time_cluster)        #Create spatial clusters within time cluster
        final_cluster = cluster.create_final_cluster(time_cluster_with_spatial_clusters, cluster_type)              #Create final cluster, based on cluster type
        if len(final_cluster) > 0:
            clustered_data.append(time_cluster_with_spatial_clusters)                                               #Add time cluster with spatial clusters to cluster vector
        pos = pos + len(time_cluster)                                                                               #Increase pos in vector by amount of elements inserted in time cluster
    return clustered_data

     
def save_to_file(cluster_output_file_path, clustered_data):
    output_file = open(cluster_output_file_path, 'a')
    output_file.write(str(len(clustered_data)) + ' ')                              #Writes how many time clusters are in our file
    for time_cluster in clustered_data:
        write_time_cluster_to_file(output_file, time_cluster)
    output_file.close()    


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
#HELPER FUNCTIONS
#   
    

## SAVE HELP FUNCTIONS ##

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
    
    
    
## LOAD HELP FUNCTIONS ##    
       
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
    
        
    
    
    
    
    
    
    
    
