import numpy as np
import trimesh
import random
import torch

def vis_sdf(pts,sdf,out_dir):

    color = np.array([0,255,0]).reshape(1,3)

    sdf = sdf.reshape(-1,1)

    pts = pts.reshape(-1,3)

    colors = sdf @ color

    print(colors.min(),colors.max())

    cloud = trimesh.points.PointCloud(pts, colors=colors)

    cloud.export(out_dir)


# np.savez(output_filepath, vol_points=pts_vol_label, surf_points=pts_surface_label)
file_path = "./test.npy"

data = np.load(file_path)

# pts = data['surf_points'][:,:3]
# sdf = data['surf_points'][:,3]
pts = data[:,:3]
sdf = data[:,-1]
print(sdf.min(),sdf.max())

vis_sdf(pts,sdf,'surf_sdf.ply')

