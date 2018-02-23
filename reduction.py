from import_export import import_data, write_reduced_data_to_file, convert_to_int
import os

#
# MAIN FUNCTION
# 

def reduce_and_save(raw_data_folder_path, reduced_data_folder_path, t_min, t_max, q_thres):
    files_in_folder = os.listdir(raw_data_folder_path)
    for file_name in files_in_folder:
        reduced_raw_data_int = import_and_reduce(raw_data_folder_path, file_name, t_min, t_max, q_thres)
        write_reduced_data_to_file(reduced_data_folder_path, reduced_raw_data_int, t_min, t_max, q_thres)
             
#
# HELPER FUNCTIONS
#
        
def import_and_reduce(raw_data_folder_path, file_name, t_min, t_max, q_thres):
    raw_data = import_data(raw_data_folder_path, file_name)                             #Import data from folderpath + filename, format is a vector, each element a datpoint
    raw_data_int = convert_to_int(raw_data)                                          #Convert values in vector to int
    reduced_raw_data_int = filter_data(raw_data_int, t_min, t_max, q_thres)         #Remove datapoint with to large or low t, and datapoint with too low q_thres
    
    return reduced_raw_data_int           
   
def filter_data(raw_data_int, t_min, t_max, q_thres):
    time_and_energy_filtered = []
    for datapoint in raw_data_int:                                                          #For each datapoint in raw_data
        if not (datapoint[0] < t_min or datapoint[0] > t_max or datapoint[3] < q_thres):           #Does current datapoint have a valid time_stamp and q-value?
            time_and_energy_filtered.append(datapoint)
            
    return time_and_energy_filtered