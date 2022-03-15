from netCDF4 import Dataset
import numpy as np
import math

def sin1d( grp ):

    grp_ = grp.createGroup("1d.1")
    nx = 10

    grp_.short = "{0} short description".format( grp_.name )
    grp_.num = 34

    xs = [ x for x in range(nx) ]
    sins = [ math.sin( math.radians(x) ) for x in xs ]

    #add to ncdef

    xdim  = grp_.createDimension( "X_dim", nx )
    xdim_v = grp_.createVariable( "X", 'f', xdim.name )
    xdim_v[:] = xs

    sin_data = grp_.createVariable( "SIN", 'f', xdim.name )
    sin_data[:] = sins
 


def sin1d_2_grp( grp ):

    grp_ = grp.createGroup("1d.2")
    grp_.short = "{0} short description".format( grp_.name )

    grp_.num = 432

    #data
    nx = 10
    ny = nx

    xs = [ x for x in range(nx) ]
    sins = [ math.sin( math.radians(x) ) for x in xs ]
    coss = [ math.cos( math.radians(x) ) for x in xs ]

    #add to ncdef

    xdim  = grp_.createDimension( "X_dim", nx )
    xdim_v = grp_.createVariable( "X", 'f', xdim.name )
    xdim_v[:] = xs

    sin_data = grp_.createVariable( "SIN", 'f', xdim.name )
    sin_data[:] = sins

    cos_data = grp_.createVariable( "COS", 'f', xdim.name )
    cos_data[:] = coss
    

def sin2d( grp ):

    grp_ = grp.createGroup("2d")

    grp_.short = "{0} short description".format( grp_.name )

    grp_.num = 43902

    #data
    nx = 10
    ny = 5

    xs = [ x for x in range(nx) ]
    ys = [ y for y in range(ny) ]

    data = np.zeros( (nx, ny) )

    for i in range(nx):
        for j in range(ny):
            data[i][j] = math.sin( math.radians(i + j) )

    sins = [ math.sin( math.radians(x) ) for x in xs ]

    #add to ncdef

    xdim  = grp_.createDimension( "X_dim", nx )
    ydim  = grp_.createDimension( "Y_dim", ny )

    xdim_v = grp_.createVariable( "X", 'f', xdim.name )
    ydim_v = grp_.createVariable( "Y", 'f', ydim.name )

    xdim_v[:] = xs
    ydim_v[:] = ys

    data_v = grp_.createVariable( "data2d", 'f',( xdim.name, ydim.name) )
    data_v[:] = data

def sin3d( grp ):

    grp_ = grp.createGroup("3d")

    grp_.short = "{0} short description".format( grp_.name )

    grp_.num = 48702

    #data
    nx = 3
    ny = 4
    nz = 5

    xs = [ x for x in range(nx) ]
    ys = [ y for y in range(ny) ]
    zs = [ z for z in range(nz) ]

    data = np.zeros( (nx, ny, nz) )

    for i in range(nx):
        for j in range(ny):
            for k in range( nz ):
                data[i][j][k] = math.sin( math.radians(i + j + k) )


    #add to ncdef

    xdim  = grp_.createDimension( "X_dim", nx )
    ydim  = grp_.createDimension( "Y_dim", ny )
    zdim  = grp_.createDimension( "Z_dim", nz )

    xdim_v = grp_.createVariable( "X", 'f', xdim.name )
    ydim_v = grp_.createVariable( "Y", 'f', ydim.name )
    zdim_v = grp_.createVariable( "Z", 'f', zdim.name )

    xdim_v[:] = xs

    ydim_v[:] = ys

    zdim_v[:] = zs

    data_v = grp_.createVariable( "data", 'f',( xdim.name, ydim.name, zdim.name) )
    data_v[:] = data

   


if '__main__' == __name__:

    rootgrp = Dataset("test.nc", "w", format="NETCDF4")

    rootgrp.version = 1
    rootgrp.long_description = "A long decription"
    rootgrp.short_description = "A short description"

    grp = rootgrp

    sin1d(grp) 

    sin1d_2_grp( grp )

    sin2d(grp)

    sin3d(grp)
