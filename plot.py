import matplotlib.pyplot as plt
from import_export import import_data_set_to_int
from matplotlib.colors import LogNorm

import numpy as np
import pylab as p
import math

import os


def plot_individual_ch_nbrs(red_data_int, w_or_s):
    
    fig = plt.figure()
    if w_or_s == "wires":
        ch0 = [datapoint[3] for datapoint in red_data_int if datapoint[2] == 0]
        ch1to4 = [datapoint[3] for datapoint in red_data_int if 0 < datapoint[2] < 5]
        ch5to19 = [datapoint[3] for datapoint in red_data_int if 4 < datapoint[2] < 20]
        ch20to30 = [datapoint[3] for datapoint in red_data_int if 19 < datapoint[2] < 31]
        ch31 = [datapoint[3] for datapoint in red_data_int if datapoint[2] == 31]
        total_nbr_counts_wires = len(ch0) + len(ch1to4) + len(ch5to19) + len(ch20to30) + len(ch31)
        print(total_nbr_counts_wires)
        plot_vec = [ch0, ch1to4, ch5to19, ch20to30, ch31]
        name_vec = ['ch0', 'ch1to4', 'ch5to19', 'ch20to30', 'ch31']
        for i, vec in enumerate(plot_vec):
            plt.yscale('log')
            plt.xlabel("q")
            plt.ylabel("Counts")
            plt.title("Counts in wires")
            y,binEdges=np.histogram(vec,bins=100)
            bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
            plt.plot(bincenters,y,'.', label = name_vec[i])
        plt.legend(loc='upper right')
        plt.show()
        fig.savefig('/Users/alexanderbackis/Desktop/Examensarbete/Neutron Reflectometry Analysis/Data/plotted_data/' + 'individual_channel_wires' + '.png')
    
    else:
        ch32 = [datapoint[3] for datapoint in red_data_int if datapoint[2] == 32]
        ch33to36 = [datapoint[3] for datapoint in red_data_int if 32 < datapoint[2] < 37]
        ch37to51 = [datapoint[3] for datapoint in red_data_int if 36 < datapoint[2] < 52]
        ch52to62 = [datapoint[3] for datapoint in red_data_int if 51 < datapoint[2] < 63]
        ch63 = [datapoint[3] for datapoint in red_data_int if datapoint[2] == 63]
        total_nbr_counts_strips = len(ch32) + len(ch33to36) + len(ch37to51) + len(ch52to62) + len(ch63)
        print(total_nbr_counts_strips)
        plot_vec = [ch32, ch33to36, ch37to51, ch52to62, ch63]
        name_vec = ['ch32', 'ch33to36', 'ch37to51', 'ch52to62', 'ch63']
        for i, vec in enumerate(plot_vec):
            plt.yscale('log')
            plt.xlabel("q")
            plt.ylabel("Counts")
            plt.title("Counts in strips")
            y,binEdges=np.histogram(vec,bins=100)
            bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
            plt.plot(bincenters,y,'.', label = name_vec[i])
        plt.legend(loc='upper right')
        plt.show()
        fig.savefig('/Users/alexanderbackis/Desktop/Examensarbete/Neutron Reflectometry Analysis/Data/plotted_data/' + 'individual_channel_strips' + '.png')
    
def plot_ch_nbrs_quality_factor1(red_data_int):
    fig = plt.figure()
    ch41to55 = [datapoint[3] for datapoint in red_data_int if 40 < datapoint[2] < 56]
    ch14to19 = [datapoint[3] for datapoint in red_data_int if 13 < datapoint[2] < 20]
    plot_vec = [ch14to19, ch41to55]
    name_vec = ['ch14to19 (wires)', 'ch41to55 (strips)']
    for i, vec in enumerate(plot_vec):
         plt.yscale('log')
         plt.xlabel("q")
         plt.ylabel("Counts")
         plt.title("Counts in strips and wires for quality factor = 1")
         y,binEdges=np.histogram(vec,bins=100)
         bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
         plt.plot(bincenters,y,'.', label = name_vec[i])
    plt.legend(loc='upper right')
    plt.show()
    fig.savefig('/Users/alexanderbackis/Desktop/Examensarbete/Neutron Reflectometry Analysis/Data/plotted_data/' + 'individual_channel_quality_factor_1' + '.png')
    
def plot_data_histogram(raw_data_int, name, plot_type):
    index = None
    nbr_bins = 200
    fig = plt.figure()
    if plot_type == "Amplitude":
        index = 3
        plt.hist([datapoint[index] for datapoint in raw_data_int], bins=nbr_bins, range=[-1000,50000])
        plt.title(name)
        plt.xlabel(plot_type)
        plt.ylabel("Counts")
    else:
        index = 0
        plt.hist([datapoint[index] for datapoint in raw_data_int], bins=nbr_bins)
        plt.title(name)
        plt.xlabel("Timestamp")
        plt.ylabel("Counts")
        
    plt.show()
    fig.savefig('/Users/alexanderbackis/Desktop/Examensarbete/Neutron Reflectometry Analysis/Data/plotted_data/' + name + '.png')
    

def plot_cluster_histogram(clusters, name, plot_type):
    nbr_bins = 200
    fig = plt.figure()
    if plot_type == "mw":
        plt.hist([cluster[4] for cluster in clusters if cluster[0] == 1], bins=10, align='mid', range=[0,3])
        plt.title(name)
        plt.xlabel("Multiplicity Wires")
        plt.ylabel("Counts")
        plt.show()
            
    elif plot_type == "ms":
        plt.hist([cluster[5] for cluster in clusters if cluster[0] == 1], bins=10, align='mid', range =[0,4])
        plt.title(name)
        plt.xlabel("Multiplicity Strips")
        plt.ylabel("Counts")
        plt.show()
        
    elif plot_type == "qw_over_qs":
        print(len([cluster[2]/cluster[3] for cluster in clusters if cluster[0] == 1]))
        plt.hist([cluster[2]/cluster[3] for cluster in clusters if cluster[0] == 1], bins=150)
        plt.title(name)
        plt.xlabel("Q-total in wires over Q-total in strips")
        plt.ylabel("Counts")
        plt.show()
    
                
                

    elif plot_type == "mwoms1":
        ms_when_mw_1 = [cluster[5] for cluster in clusters if cluster[0] == 1 and cluster[4] == 1]
        ms_when_mw_2 = [cluster[5] for cluster in clusters if cluster[0] == 1 and cluster[4] == 2]
        
        y,binEdges = np.histogram(ms_when_mw_1,bins=10, range=[0,3])
        bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
        plt.plot(bincenters,[ele/len(ms_when_mw_1) for ele in y],'o', label = 'm_wire = 1')
        
        y,binEdges = np.histogram(ms_when_mw_2,bins=10, range=[0,3])
        bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
        plt.plot(bincenters,[ele/len(ms_when_mw_2) for ele in y],'o', label = 'm_wire = 2')
        
        
        plt.legend(loc='upper right')
        plt.title(name)
        plt.xlabel("Multiplicity in strips")
        plt.ylabel("Fraction")
        plt.show()
    
    elif plot_type == "mwoms2": 
        mw_when_ms_1 = [cluster[4] for cluster in clusters if cluster[0] == 1 and cluster[5] == 1]
        mw_when_ms_2 = [cluster[4] for cluster in clusters if cluster[0] == 1 and cluster[5] == 2]
        mw_when_ms_3 = [cluster[4] for cluster in clusters if cluster[0] == 1 and cluster[5] == 3]
        
        y,binEdges = np.histogram(mw_when_ms_1,bins=10, range=[0,3])
        bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
        plt.plot(bincenters,[ele/len(mw_when_ms_1) for ele in y],'o', label = 'm_strip = 1')
        
        y,binEdges = np.histogram(mw_when_ms_2,bins=10, range=[0,3])
        bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
        plt.plot(bincenters,[ele/len(mw_when_ms_2) for ele in y],'o', label = 'm_strip = 2')
        
        y,binEdges = np.histogram(mw_when_ms_3,bins=10, range=[0,3])
        bincenters = 0.5*(binEdges[1:]+binEdges[:-1])
        plt.plot(bincenters,[ele/len(mw_when_ms_3) for ele in y],'o', label = 'm_strip = 3')
        
        plt.legend(loc='upper right')
        plt.title(name)
        plt.xlabel("Multiplicity in wires")
        plt.ylabel("Fraction")
        plt.show()
        
    
        
    elif plot_type == "qw":
        plt.hist([cluster[2] for cluster in clusters if cluster[0] == 1], bins=nbr_bins,range=[0,45000])
        plt.title(name)
        plt.xlabel("Q-total in wires")
        plt.ylabel("Counts")
        plt.show()
             
    elif plot_type == "qs":
        plt.hist([cluster[3] for cluster in clusters if cluster[0] == 1], bins=150, range=[0,45000])
        plt.title(name)
        plt.xlabel("Q-total in strips")
        plt.ylabel("Counts")
        plt.show()
    
    elif plot_type == "qf":
        plt.hist([cluster[0] for cluster in clusters], bins=10, range=[-0.5,1.5])
        plt.title(name)
        plt.xlabel("Quality factor")
        plt.ylabel("Counts")
        plt.show()
    
    elif plot_type == "qw_and_qs":
        qw = [cluster[2] for cluster in clusters if cluster[0] == 1]
        qs = [cluster[3] for cluster in clusters if cluster[0] == 1]
        plt.hist(qw, nbr_bins, range=[0,45000], alpha = 0.8, label='Q wires')
        plt.hist(qs, nbr_bins, range=[0,45000], alpha = 0.8, label='Q strips') 
        plt.legend(loc='upper right')
        plt.title(name)
        plt.xlabel("Q")
        plt.ylabel("Counts")
        plt.show()
    
    elif plot_type == "2d":
        X = [cluster[6][0] for cluster in clusters if cluster[0] == 1]
        Y = [cluster[6][1] for cluster in clusters if cluster[0] == 1]
        plt.title(name)
        plt.xlabel("wires [mm]")
        plt.ylabel("strips [mm]")
        plt.hist2d(X, Y, bins=100, norm=LogNorm())
        plt.colorbar()
        plt.show()
        
    elif plot_type == "2d_timediff_and_qw_o_qs":
        Tdiff = [cluster[7][1] - cluster[7][0] for cluster in clusters if cluster[0] == 1]
        qw_o_qs = [cluster[2]/cluster[3] for cluster in clusters if cluster[0] == 1]
        plt.title(name)
        plt.xlabel("Timediff")
        plt.ylabel("qw over qs")
        plt.hist2d(qw_o_qs, Tdiff, bins=100, norm=LogNorm())
        plt.colorbar()
        plt.show()
    
    elif plot_type == "bp":
        X = [cluster[6][0] for cluster in clusters if cluster[0] == 1]
        Y = [cluster[6][1] for cluster in clusters if cluster[0] == 1]
        
        plt.subplot(1, 2, 1)
        plt.hist(X,bins=20, log = True, range = [5,25])
        plt.title('Histogram over wires')
        plt.xlabel('wires [mm]')
        plt.ylabel('Counts')

        plt.subplot(1, 2, 2)
        plt.hist(Y,bins=25,log = True, range=[0,130])
        plt.title('Histogram over strips')
        plt.xlabel('strips [mm]')
        plt.ylabel('Counts')
        plt.tight_layout()
        
    elif plot_type == "time":
       
        Tdiff = [cluster[7][1] - cluster[7][0] for cluster in clusters if cluster[0] == 1]
        plt.hist(Tdiff, bins=100, log = True, range=[-200,400])
        plt.title(name)
        plt.xlabel("t_strip - t_wire")
        plt.ylabel("Counts")
        plt.show()
    elif plot_type == "time_strips_and_wires":
        Twire = [cluster[8][0] for cluster in clusters if cluster[0] == 1]
        Tstrip = [cluster[8][1] for cluster in clusters if cluster[0] == 1]
        
        plt.hist(Twire, bins= 50, log = True, range= [0,50])
        plt.title("Time difference between first wire event and last wire event in wirecluster")
        plt.xlabel("Tdiff wire")
        plt.ylabel("Counts")
        plt.show()
        
        plt.title("Time difference between first strip event and last strip event in stripcluster")
        plt.hist(Tstrip, bins= 50, log = True, range= [0,50])
        plt.xlabel("Tdiff strips")
        plt.ylabel("Counts")
        plt.show()
        
    elif plot_type == "ch_nbr_wires":
        wire_ch_nbrs = []
        strip_ch_nbrs = []
        for cluster in clusters:
            if cluster[0] == 1:
                for vec in cluster[9]:
                    for ch in vec:
                        if ch < 32:
                            wire_ch_nbrs.append(ch)
                        else:
                            strip_ch_nbrs.append(ch)
        plt.hist(wire_ch_nbrs, 64, label = 'Channels wires')
        plt.hist(strip_ch_nbrs, 64, label = 'Channels strips')
        plt.legend(loc='upper right')
        plt.title("Distribution of channel numbers for quality factor = 1")
        plt.xlabel("Ch number")
        plt.ylabel("Counts")
        plt.show()
    
    fig.savefig('/Users/alexanderbackis/Desktop/Examensarbete/Neutron Reflectometry Analysis/Data/plotted_data/' + name + '.eps')


def plot_qw_over_qs(clusters, offset):
        
        w0 = []
        w1to7 = []
        w8to25 = []
        w26to30 = []
        w31 = []
        
        w8to12 = []
        w19to25 = []
        
        w13 = []
        w14 = []
        w15 = []
        w16 = []
        w17 = []
        w18 = []

        for cluster in clusters:
            if cluster[0] == 1:
                ch_nbr = convert_to_ch_nbr(cluster,offset)
                if ch_nbr == 0:
                    w0.append(cluster[2]/cluster[3])
                elif 0 < ch_nbr < 8 :
                    w1to7.append(cluster[2]/cluster[3])
                elif 7 < ch_nbr < 26:               
                    w8to25.append(cluster[2]/cluster[3])
                    if ch_nbr < 13:
                        w8to12.append(cluster[2]/cluster[3])
                    elif ch_nbr == 13:
                        w13.append(cluster[2]/cluster[3])
                    elif ch_nbr == 14:
                        w14.append(cluster[2]/cluster[3])
                    elif ch_nbr == 15:
                        w15.append(cluster[2]/cluster[3])
                    elif ch_nbr == 16:
                        w16.append(cluster[2]/cluster[3])
                    elif ch_nbr == 17:
                        w17.append(cluster[2]/cluster[3])
                    elif ch_nbr == 18:
                        w18.append(cluster[2]/cluster[3])
                    else:
                        w19to25.append(cluster[2]/cluster[3])
                elif 26 < ch_nbr < 31:                
                    w26to30.append(cluster[2]/cluster[3])
                elif ch_nbr == 31:
                    w31.append(cluster[2]/cluster[3])
        print("w0 length:" + str(len(w0)))
        print("w1to7 length:" + str(len(w1to7)))
        print("w8to25 length:" + str(len(w8to25)))
        print("w26to30 length:" + str(len(w26to30)))
        print("w31 length:" + str(len(w31)))
        print(len(w0)+len(w1to7)+len(w8to25)+len(w26to30)+len(w31))
        
        plot_vec = [w0, w1to7, w8to25, w26to30, w31]
        name_vec = ['w0', 'w1to7', 'w8to25', 'w26to30', 'w31']
        bin_vec = [50,40,150,10,10]
        for i, vec in enumerate(plot_vec):
            plt.hist(vec,bin_vec[i])
            plt.title(name_vec[i])
            plt.xlabel("Q")
            plt.ylabel("Counts")
            plt.show()    
        
#        plt.hist(w8to15, 100, alpha = 0.8, label='w8to15')
#        plt.hist(w16, 100, alpha = 0.8, label='w16')
#        plt.hist(w17to25, 100, alpha = 0.8, label='w17to25') 
#        plt.legend(loc='upper right')
#        plt.title("Qw over Qs")
#        plt.xlabel("fraction")
#        plt.ylabel("Counts")
#        plt.show()
#        
#        plot_vec_2 = [w8to12,w13,w14,w15,w16,w17,w18,w19to25]
#        name_vec_2 = ['w8to12','w13','w14','w15','w16','w17','w18','w19to25']
#        bin_vec = [30,20,80,150,150,100,50,30]
#        for i, vec in enumerate(plot_vec_2):
#            plt.hist(vec, bin_vec[i], label=name_vec_2[i])
#            plt.legend(loc='upper right')
#            plt.title("Qw over Qs")
#            plt.xlabel("fraction")
#            plt.ylabel("Counts")
#            plt.show()
        
        
        
        
def convert_to_ch_nbr(cluster,offset):
    dig_nbr = cluster[1]
    x = cluster[6][0]
    current_offset = offset[[i[0] for i in offset].index(dig_nbr)][1]
    ch_wire = int(round((x - current_offset)/(4*math.sin(5*(math.pi/180)))))
    
    return ch_wire
    
    
    
    
    
    
        
    
