from import_export import import_data_set_to_int

import math
#
#MAIN FUNCTION
#


def cluster(reduced_data_folder_path, delta_t, max_w_m, max_s_m, offset):
    reduced_data = import_data_set_to_int(reduced_data_folder_path)
    clustered_data = []                                                                     
    pos = 0
    
    while pos < len(reduced_data):                                                                                                 #While there is more data in vector, keep producing time clusters
        time_cluster = create_time_cluster(reduced_data, delta_t, pos)                                                             #Create time cluster
        time_cluster_with_spatial_clusters = create_time_cluster_with_spatial_clusters(time_cluster, max_w_m, max_s_m, offset)        #Create spatial clusters within time cluster
        final_cluster = create_final_cluster(time_cluster_with_spatial_clusters)                                                    #Create final cluster, based on cluster type)
        clustered_data.append(final_cluster)                                                                                             #Add time cluster with spatial clusters to cluster vector
        pos = pos + len(time_cluster)                                                                                                #Increase pos in vector by amount of elements inserted in time cluster
        
    return clustered_data




#
#HELPER FUNCTIONS
#




def create_time_cluster(reduced_data, delta_t, pos):
    
    time_cluster_finished = False
    time_elapsed = 0
    time_cluster = []
    
    #insert first datapoint in time cluster (since it will always have at least one datapoint)
    datapoint = reduced_data[pos] 
    time_cluster.append(datapoint)
    pos += 1
    
    while (not time_cluster_finished) and pos < len(reduced_data) and time_elapsed <= delta_t:          #While there is more elements in cleaned data vector and we have not finished time cluster
        
        datapoint = reduced_data[pos]                                     #Our current datapoint
        time_stamp = datapoint[0]                                         #Time_stamp of current datapoint
        time_stamp_prev = reduced_data[pos-1][0]                          #Time_stamp of previous datapoint (does not matter for first datapoint that we compare with last since we will add it anyway)      
        time_diff = time_stamp - time_stamp_prev
                                                                 
        if 0 <= time_diff <= delta_t:                            #Is it within delta_t? (make sure larger than zero so we don't get values from last neutron bunch)
            time_cluster.append(datapoint)
            time_elapsed += time_diff 
            pos += 1 
        else:
            time_cluster_finished = True
        
    
    time_cluster.sort(key=lambda x: x[2])                                 #Sort time cluster by channel number
    
    return time_cluster



def create_time_cluster_with_spatial_clusters(time_cluster, max_w_m, max_s_m, offset) :
    
    pos = 0
    time_cluster_with_spatial_clusters = []
    
    while pos < len(time_cluster):                                                       #While there is more datapoints in time cluster
        spatial_cluster = create_spatial_cluster(time_cluster, pos, max_w_m, max_s_m, offset)        #Create spatial cluster
        time_cluster_with_spatial_clusters.append(spatial_cluster)                       #Append this spatial cluster to our time_cluster_with_spatial_clusters vector
        pos = pos + spatial_cluster[2]                                                #Increase our position by the number of datapoints we inserted into our spatial cluster (that is, multiplicity)
    
    return time_cluster_with_spatial_clusters
 

    
def create_final_cluster(time_cluster_with_spatial_clusters):
    
    quality_factor = get_quality_factor(time_cluster_with_spatial_clusters)
    dig_nbr = time_cluster_with_spatial_clusters[0][0]
    q_tot_wires = sum(spatial_cluster[3] for spatial_cluster in time_cluster_with_spatial_clusters if spatial_cluster[1] == 'w')
    q_tot_strips = sum(spatial_cluster[3] for spatial_cluster in time_cluster_with_spatial_clusters if spatial_cluster[1] == 's')
    m_tot_wires = sum(spatial_cluster[2] for spatial_cluster in time_cluster_with_spatial_clusters if spatial_cluster[1] == 'w')
    m_tot_strips = sum(spatial_cluster[2] for spatial_cluster in time_cluster_with_spatial_clusters if spatial_cluster[1] == 's')
    
    final_cluster = [quality_factor, dig_nbr, q_tot_wires, q_tot_strips, m_tot_wires, m_tot_strips]
    
    if quality_factor == 1:
        x = time_cluster_with_spatial_clusters[0][6]
        y = time_cluster_with_spatial_clusters[1][6]
        t_min_wires = time_cluster_with_spatial_clusters[0][5]
        t_min_strips = time_cluster_with_spatial_clusters[1][5]
        t_diff_wires = time_cluster_with_spatial_clusters[0][8]
        t_diff_strips = time_cluster_with_spatial_clusters[1][8]
        final_cluster.append([x, y])
        final_cluster.append([t_min_wires,t_min_strips])
        final_cluster.append([t_diff_strips,t_diff_wires])
    else:
        final_cluster.append([])
        final_cluster.append([])
        final_cluster.append([])
        
    final_cluster.append([spatial_cluster[7] for spatial_cluster in time_cluster_with_spatial_clusters])    
    
    return final_cluster   
 


## SMALL HELPER FUNCTIONS ##       
        
        
def create_spatial_cluster(time_cluster, pos, max_w_m, max_s_m, offset):
    
    spatial_cluster_finished = False
    multiplicity = 0
    spatial_cluster = []
 
    #Insert first datapoint in our spatial cluster
    datapoint = time_cluster[pos]                                       #Declare our first datapoint
    spatial_cluster.append(datapoint)                                   #Insert it into our spatial_cluster
    dig_nbr = spatial_cluster[0][1]                                     #What is the digitizer number of our spatial_cluster
    w_or_s = is_wire_or_strip(spatial_cluster)                          #Is our spatial cluster with wires or strips?
    multiplicity += 1                                                   #Increase multiplicity by 1
    pos += 1                            
    expect = datapoint[2] + 1                                           #What channel number are we expecting if next event is to be consecutive?
    spatial_cluster_finished = reached_max_multiplicity(w_or_s, multiplicity, max_w_m, max_s_m)     #Checks if we have reached max multiplicity 
  
    #Sees if we can insert more   
    while not spatial_cluster_finished and pos < len(time_cluster):
        
        datapoint = time_cluster[pos]                                   #Declare our current datapoint
        
        if datapoint[2] == expect and datapoint[2] != 32:               #Is our datapoint adjacent to the previous one, and belong to the same cathegory (wires or strips)?
            spatial_cluster.append(datapoint)                           #If so, append to our spatial cluster            
            multiplicity += 1                                           #Increase multiplicity by 1
            pos += 1
            expect = datapoint[2] + 1
            spatial_cluster_finished = reached_max_multiplicity(w_or_s, multiplicity, max_w_m, max_s_m)     #Checks if we have reached max multiplicity
        else:
            spatial_cluster_finished = True                             #If not, set our spatial cluster as finished
    
    #Assigns relevant parameters        
    q_tot = sum([datapoint[3] for datapoint in spatial_cluster])
    q_max = max([datapoint[3] for datapoint in spatial_cluster])
    t_min = min([datapoint[0] for datapoint in spatial_cluster])
    CoG = perform_center_of_gravity(spatial_cluster, offset, w_or_s, dig_nbr)
    ch_nbrs = [datapoint[2] for datapoint in spatial_cluster]
    t_max = max([datapoint[0] for datapoint in spatial_cluster])
    delta_t = t_max - t_min
                           
    spatial_cluster = [dig_nbr, w_or_s, multiplicity, q_tot, q_max, t_min, CoG, ch_nbrs, delta_t]           #Create a spatial cluster in the format: [dig_nbr, w_or_s, multiplicity, q_tot, q_max, t_min, ch_max_or_CoG] 
    
    return spatial_cluster                


def reached_max_multiplicity(w_or_s, multiplicity, max_w_m, max_s_m):
    w_or_s == 'w' and multiplicity
    if w_or_s == 'w' and multiplicity == max_w_m:
        return True
    elif w_or_s == 's' and multiplicity == max_s_m: 
        return True
    else:
        return False
        
        
def is_wire_or_strip(spatial_cluster):
    if spatial_cluster[0][2] < 32:                  #Is channelnumber under 32?
        return 'w'                                  #If so, datapoint is from wire
    else:
        return 's'                                  #If not, datapoint is from strip
      
def perform_center_of_gravity(spatial_cluster, offset, w_or_s, dig_nbr):
    q_tot = sum([datapoint[3] for datapoint in spatial_cluster])
    coordinate_vec = get_coordinates(spatial_cluster, offset, w_or_s, dig_nbr)
    q_times_coordinate_sum = sum([(datapoint[3] * coordinate_vec[i]) for i, datapoint in enumerate(spatial_cluster)])
    ch_CoG = round(float(q_times_coordinate_sum / q_tot), 2)
    return ch_CoG
    
def get_quality_factor(time_cluster_with_spatial_clusters): 
    if len(time_cluster_with_spatial_clusters) == 2 and time_cluster_with_spatial_clusters[0][1] == 'w' and time_cluster_with_spatial_clusters[1][1] == 's':
        return 1
    else:
        return 0

def get_coordinates(spatial_cluster, offset, w_or_s, dig_nbr):
    coordinate_vec = []
    
    if w_or_s == 'w':
        current_offset = offset[[i[0] for i in offset].index(dig_nbr)][1]
        for datapoint in spatial_cluster:
            coordinate = 4 * math.sin(5 * (math.pi/180)) * datapoint[2] + current_offset
            coordinate_vec.append(coordinate)
    else:
        for datapoint in spatial_cluster:
            coordinate = 4 * (datapoint[2]-32)
            coordinate_vec.append(coordinate)
    
    return coordinate_vec






