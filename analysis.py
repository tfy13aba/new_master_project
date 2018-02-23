
#
#MAIN FUNCTIONS
#

def perform_analysis(loaded_clusters, analysis_type, order_of_digitizers, max_wire_multiplicity, max_strip_multiplicity, quality_factor):
    if analysis_type == '2D':
        result = perform_2D_analysis(loaded_clusters, order_of_digitizers, max_wire_multiplicity, max_strip_multiplicity, quality_factor)
        
    return result

def perform_2D_analysis(loaded_clusters, order_of_digitizers, max_wire_multiplicity, max_strip_multiplicity, quality_factor):
    displacement = create_displacement(order_of_digitizers)
    coordinates = []
    for time_cluster in loaded_clusters:
        wire_displacement = get_displacement(displacement, time_cluster[0][2][1])
        wire_cor = get_center_of_gravity(time_cluster[0][2]) + wire_displacement
        
        strip_displacement = get_displacement(displacement, time_cluster[1][2][1])
        strip_cor = get_center_of_gravity(time_cluster[0][2]) + strip_displacement
        
        coordinates.append([wire_cor, strip_cor])
    






#
#HELPER FUNCTIONS
#

def get_center_of_gravity(spatial_cluster):
    sum = 
    for datapoint in spatial_cluster:
        
    
    
    


def create_displacement(order_of_digitizers):
    displacement_vec = []
    displacement = 0
    for i in order_of_digitizers:
        displacement_vec.append([i, displacement])
        displacement += 32
    return displacement_vec

def get_displacement(displacement, dig_nbr):
    return displacement[displacement.index(dig_nbr), 1]


    
    
    
    
    
    
    
    
    
    