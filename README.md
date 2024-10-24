# MeshSample
simple toolkit to sample sdf & occ from watertight mesh


## install
```
cd inside_mesh && python setup.py build_ext --inplace
```
install other python dependency

## usage
`python sample --input /path/to/mesh.obj --output /path/to/sample.npy --count 2500000`

- support mesh format: off, obj, glb,
- count: in volume and mesh surface sample points number, so will output 2*count points.
- output file is npy format, and shape is [n,5]: [x,y,z,occ,sdf]

## vis
given sample.npy -> get gt mesh from label data and verify sampling results:`python vis_gt.py `
given sample.npy -> get gt colored-pcd from label data and verify sampling results,support sdf & occ visualization.:`python vis_sdf.py`
## todo
- use cuda-kdtree to optimize performance.