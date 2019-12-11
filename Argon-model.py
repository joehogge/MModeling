# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 09:09:42 2019

@author: Joe

Ths code was adapted from:
https://gist.github.com/jhjensen2/71bdb95ca0b12e22fa176c86b46e28b5
    

"""



import numpy as np
import py3Dmol
global trajectory



#class ArgonModel():
    

def get_initial_coordinates():
    x_coord = [np.random.random()*box_width for i in range(n_particles)]
    y_coord = [np.random.random()*box_width for i in range(n_particles)]
    z_coord = [np.random.random()*box_width for i in range(n_particles)]
    
    return x_coord, y_coord, z_coord

def get_initial_velocities():
    x_vel = [2*(np.random.random()-0.5)*box_width for i in range(n_particles)]
    y_vel = [2*(np.random.random()-0.5)*box_width for i in range(n_particles)]
    z_vel = [2*(np.random.random()-0.5)*box_width for i in range(n_particles)]
    
    return x_vel, y_vel, z_vel

def take_step(x_coord, y_coord, z_coord, x_vel, y_vel, z_vel):
    for i in range(n_particles):
        x_coord[i] += x_vel[i]*dt
        y_coord[i] += y_vel[i]*dt
        z_coord[i] += z_vel[i]*dt
        
        if abs(x_coord[i]) > box_width:
            x_vel[i] = -x_vel[i]
            x_coord[i] += x_vel[i]*dt

        if abs(y_coord[i]) > box_width:
            y_vel[i] = -y_vel[i]
            y_coord[i] += y_vel[i]*dt

        if abs(z_coord[i]) > box_width:
            z_vel[i] = -z_vel[i]
            z_coord[i] += z_vel[i]*dt 
            
        return x_coord, y_coord, z_coord, x_vel, y_vel, z_vel

def add_frame(xs, ys, zs, i):
    global trajectory
    
    if i == 0:
        trajectory = ''
    trajectory += str(n_particles) + '\ntitle\n'
    for x, y, z in zip(xs, ys, zs):
        trajectory += ' '.join(['Ar',str(x),str(y),str(z),'0.0\n'])


n_particles = 100
box_width = 10
n_steps = 5000
dt = 0.001

x_coord, y_coord, z_coord = get_initial_coordinates()
x_vel, y_vel, z_vel = get_initial_velocities

for i in range(n_steps):
    x_coord, y_coord, y_coord, x_vel, y_vel, z_vel = take_step(x_coord, y_coord, z_coord, x_vel, y_vel, z_vel)

    if i%10 == 0:
        add_frame(x_coord, y_coord, z_coord, i)

view = py3Dmol.view()
view.addModelAsFrames(trajectory, 'xyz')
view.animate({'loop': 'forward', 'reps': 1})
view.setStyle({'sphere':{'radius': 0.5}})
view.zoomTo()


