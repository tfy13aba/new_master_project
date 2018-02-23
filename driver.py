from reduction import reduce_and_save
from plot import plot_data_histogram, plot_cluster_histogram, plot_individual_ch_nbrs, plot_ch_nbrs_quality_factor1, plot_qw_over_qs
from cluster import cluster
from import_export import import_data_set_to_int
#from clean_and_cluster import clean_and_cluster, save_to_file, import_from_file
#from analysis import perform_analysis
#import os


def driver():
    
    ## DEFINE FILE PATHS ##

    raw_data_folder_path = '/Users/alexanderbackis/Desktop/Examensarbete/Neutron Reflectometry Analysis/Data/raw_data_2/'
    reduced_data_folder_path = '/Users/alexanderbackis/Desktop/Examensarbete/Neutron Reflectometry Analysis/Data/reduced_data/'
    cluster_file_path = '/Users/alexanderbackis/Desktop/Examensarbete/Alexander - Analysis Code/test/test_result.txt'
    analysis_file_path = '/Users/alexanderbackis/Desktop/Examensarbete/Neutron Reflectometry Analysis/Data/analysed_data/'

    ## PARAMETERS ##

    # t_min and t_max define the neutron energy E_n spectrum. one unit of time is 16 ns
    t_min = 375000  # lower time threshold, value included
    t_max = 1249950  # upper time threshold, value included
    q_threshold = 3500  # lower charge threshold, value included
    delta_t = 187  # defines time cluster 1 unit = 16ns (total of 3 us)
    order_of_digitizers = [137, 143, 142, 31, 34, 33]  # from bottom to up
    offset = [[137,0],[143,10],[142,20],[31,30],[34,40],[33,50]]
    max_w_m = 2  # wire sub-cluster size threshold, value included
    max_s_m = 3  # strip sub-cluster size threshold, value included

   
    ## PERFORMS DATA REDUCTION AND SAVES TO FILE ##
    
  #  reduce_and_save(raw_data_folder_path, reduced_data_folder_path, t_min, t_max, q_threshold)
    
    
    ## CREATE CLUSTERS ## 
    
    clusters = cluster(reduced_data_folder_path, delta_t, max_w_m, max_s_m, offset)       
    
    ## READ CLUSTER DATA FROM FILE ##
    
  #  loaded_clusters = import_cluster_from_file(cluster_output_file_path)
    
    
    ## PERFORM DATA ANALYSIS ##
    
  #  result = perform_analysis(loaded_clusters, analysis_type, order_of_digitizers, max_wire_multiplicity, max_strip_multiplicity, quality_factor)
    
    
    ## PLOT DATA ##
    
#    raw_data_int = import_data_set_to_int(raw_data_folder_path)
    red_data_int = import_data_set_to_int(reduced_data_folder_path)
##    
###    
#    plot_individual_ch_nbrs(red_data_int, "wires")
#    plot_individual_ch_nbrs(red_data_int, "strips")
#    
##    
#    plot_data_histogram(raw_data_int, "Raw Data PHS - Timestamp", "Timestamp")
#    plot_data_histogram(raw_data_int, "Raw Data PHS - Amplitude", "Amplitude")
####    
    plot_data_histogram(red_data_int, "Reduced Data PHS - Timestamp", "Timestamp")
    plot_data_histogram(red_data_int, "Reduced Data PHS - Amplitude", "Amplitude")
##    
    plot_cluster_histogram(clusters, "Clusters: Histogram - Wire Multiplicity for quality factor = 1", "mw")
    plot_cluster_histogram(clusters, "Clusters: Histogram - Strip Multiplicity for quality factor = 1", "ms")
    #plot_cluster_histogram(clusters, "Clusters: Histogram - Q_wire", "qw")
    #plot_cluster_histogram(clusters, "Clusters: Histogram - Q_strip", "qs")
  #  plot_cluster_histogram(clusters, "Clusters: Histogram - Quality factor", "qf")
    plot_cluster_histogram(clusters, "Clusters: Histogram in 2D for quality factor = 1", "2d")
#    plot_cluster_histogram(clusters, "Clusters: Histogram - Channel numbers used in clusters with quality factor = 1", "ch_nbr_wires")
#    plot_ch_nbrs_quality_factor1(red_data_int)
#    
    plot_cluster_histogram(clusters, "Clusters: Histogram over wires and strips", "bp")
#    plot_cluster_histogram(clusters, "Clusters: Histogram of m_strips for fixed m_wire", "mwoms1")
#    plot_cluster_histogram(clusters, "Clusters: Histogram of m_wires for fixed m_strip", "mwoms2")
    plot_cluster_histogram(clusters, "Clusters: Histogram - Q_wire and Q_strip for quality factor = 1", "qw_and_qs")
    plot_cluster_histogram(clusters, "Clusters: Histogram - Q_wire over Q_strip for quality factor = 1", "qw_over_qs")
    plot_cluster_histogram(clusters, "Timediff between wires and strips for quality factor = 1", "time")
    plot_cluster_histogram(clusters, "Timediff and qw_over_qs for quality factor = 1", "2d_timediff_and_qw_o_qs")
     
    plot_cluster_histogram(clusters, "Timediff for wires and strips for quality factor = 1", "time_strips_and_wires")
    
    plot_qw_over_qs(clusters, offset)
    
    
    
    
    
    
driver()    
    
    