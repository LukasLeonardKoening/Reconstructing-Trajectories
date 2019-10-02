from helper import process_data
import math
import matplotlib.pyplot as plt
import numpy as np

def get_speeds(data_list):
    speeds = [0.0]
    prev_time = data_list[0][0]
    prev_pos = data_list[0][1]
    
    for i in range(1, len(data_list)):
        deltaT = data_list[i][0] - prev_time
        deltaX = data_list[i][1] - prev_pos
        speeds.append(deltaX / deltaT)
        
        prev_time = data_list[i][0]
        prev_pos = data_list[i][1]
    
    return speeds

def get_headings(data_list):
    area_sum = 0.0
    prev_time = data_list[0][0]
    
    integral = [0.0]
    
    for i in range(1, len(data_list)):
        deltaT = data_list[i][0] - prev_time
        area_sum += data_list[i][2] * deltaT
        integral.append(area_sum) # * math.pi / 180)
        
        prev_time = data_list[i][0]
    return integral

def get_x_y(data_list):
    headings = get_headings(data_list)
    speeds = get_speeds(data_list)
    position = [(0,0)]
    
    prev_time = data_list[0][0]
    
    for i in range(1, len(data_list)):
        deltaT = data_list[i][0] - prev_time
        
        distance = deltaT * speeds[i]
        X = position[i-1][0] + math.cos(headings[i]) * distance # * math.pi / 180
        Y = position[i-1][1] + math.sin(headings[i]) * distance
        
        position.append((X,Y))
        
        prev_time = data_list[i][0]
    return position

def show_x_y(data_list):
    positions = get_x_y(data_list)
    X = [positions[i][0] for i in range(len(positions))]
    Y = [positions[i][1] for i in range(len(positions))]
    headings = get_headings(data_list)
    U = np.cos(headings)
    V = np.sin(headings)
    
    plt.quiver(X, Y, U, V, units='width')
    plt.show()

three_quarter_turn_data = process_data("trajectorys.pickle")
show_x_y(three_quarter_turn_data)