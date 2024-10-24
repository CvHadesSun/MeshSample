
import os
import numpy as np
import trimesh
from skimage import measure
from scipy.interpolate import griddata


def sdf2mesh(sdf_dir,out_dir):

    res=256

    sdf = np.load(sdf_dir)
    print(sdf.shape)

    # points = sdf['points']
    # print(points.shape[0])
    # print(points.min(),points.max())
    # sdf_values = sdf['sdf']
    points = sdf[:,:3]
    sdf_values = sdf[:,-1]

    # sdf_values = np.clip(sdf_values,-0.05,0.05)

    grid_x, grid_y, grid_z = np.mgrid[-1:1:384j, -1:1:384j, -1:1:384j]

    # 将 SDF 值插值到规则网格
    grid_sdf = griddata(points, sdf_values, (grid_x, grid_y, grid_z), method='linear', fill_value=1.0)
    # 使用 Marching Cubes 提取等值面 (SDF = 0)
    print(sdf_values.min(), sdf_values.max(), grid_sdf.min(), grid_sdf.max())
    verts, faces, normals, values = measure.marching_cubes(grid_sdf, level=0.0)

    # 使用 trimesh 创建网格
    mesh = trimesh.Trimesh(vertices=verts, faces=faces)

    # 保存网格为 .obj 文件
    mesh.export(out_dir)

sdf2mesh('./test.npy','./gt.obj')