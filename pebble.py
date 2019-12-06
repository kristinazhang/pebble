import argparse
import numpy as np
import openmc
from IPython.display import Image


def get_args():
    parser = argparse.ArgumentParser(
        description=
        "This example script will show you how to use this module :)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "--type",  "-t", type=str, required=True, help="Please choose your lattice type e.g. 'rectanguler' or 'hexagonal' or 'random'!")
    args = parser.parse_args()

    return args

def get_lat(latt):
    if latt == 'rectanguler':
        lattice = openmc.RectLattice()
        lattice.lower_left = (-2.5, -2.5, -2.5)
        lattice.pitch = (0.1987624510891672, 0.1987624510891672, 0.1987624510891672)
        lattice.universes = np.tile(triso_univ, (25, 25, 25))
        lattice.outer = z
    elif latt == 'hexagonal':
        lattice = openmc.HexLattice()
        lattice.center = (0, 0, 0)
        lattice.pitch = [0.2222231760049275, 0.2222231760049275]
        lattice.universes = \
        [
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]],
        [[x]*78,[x]*72,[x]*66,[x]*60,[x]*54,[x]*48,[x]*42,[x]*36,[x]*30,[x]*24,[x]*18,[x]*12,[x]*6,[x]]
        ]
        lattice.outer = z
    elif latt == 'random':
        outer_radius = 455.*1e-4
        centers = openmc.model.pack_spheres(radius=outer_radius, region=-iPebble_r, num_spheres=8335)
        trisos = [openmc.model.TRISO(outer_radius, triso_univ, c) for c in centers]
        lower_left, upper_right = iPebble.region.bounding_box
        shape = (1, 1, 1)
        pitch = (upper_right - lower_left)/shape
        lattice = openmc.model.create_triso_lattice(trisos, lower_left, pitch, shape, iGraphite)

    return lattice


def get_plot(geom):
    p = openmc.Plot.from_geometry(geom)
    p.id = 1
    p.filename = 'PEBBLE_xy_' + str(latt)
    p.origin = [0,0,0]
    p.width = [6,6]
    p.pixels = (300,300)
    p.color_by = 'material'
    p.basis = 'xy'
    p.colors = {
        fuel:'red', 
        buff:'blue',
        iPyC:'yellow', 
        SiC:'green',
        oPyC:'yellow', 
        iGraphite:'cyan', 
       oGraphite:'pink'}

    q = openmc.Plot.from_geometry(geom)
    q.id = 2
    q.filename = 'PEBBLE_yz_' + str(latt)
    q.origin = [0,0,0]
    q.width = [6,6]
    q.pixels = (300,300)
    q.color_by = 'material'
    q.basis = 'yz'
    q.colors = {
        fuel:'red', 
        buff:'blue',
        iPyC:'yellow', 
        SiC:'green',
        oPyC:'yellow', 
        iGraphite:'cyan', 
        oGraphite:'pink'}

    r = openmc.Plot.from_geometry(geom)
    r.id = 3
    r.filename = 'PEBBLE_xz_' + str(latt)
    r.origin = [0,0,0]
    r.width = [6,6]
    r.pixels = (300,300)
    r.color_by = 'material'
    r.basis = 'xz'
    r.colors = {
        fuel:'red', 
        buff:'blue',
        iPyC:'yellow', 
        SiC:'green',
        oPyC:'yellow', 
        iGraphite:'cyan',
        oGraphite:'pink'}

    plot_file = openmc.Plots((p,q,r))
    plot_file.export_to_xml()
    openmc.plot_geometry()

    
fuel = openmc.Material(1,name='fuel')
fuel.set_density('g/cm3', 10.4)
fuel.add_nuclide('O16',  2)
fuel.add_nuclide('U235', 0.17180114)
fuel.add_nuclide('U238', 0.82819886)

buff= openmc.Material(2,name='buffer')
buff.set_density('g/cm3', 1.1)
buff.add_element('C', 1.0)
buff.add_s_alpha_beta('c_Graphite')

iPyC = openmc.Material(3,name='iPyC')
iPyC.set_density('g/cm3', 1.9)
iPyC.add_element('C', 1.0)
iPyC.add_s_alpha_beta('c_Graphite')

SiC = openmc.Material(4,name='SiC')
SiC.set_density('g/cm3', 3.18)
SiC.add_element('C', 0.5)
SiC.add_element('Si', 0.5)

oPyC = openmc.Material(5,name='oPyC')
oPyC.set_density('g/cm3', 1.9)
oPyC.add_element('C', 1.0)
oPyC.add_s_alpha_beta('c_Graphite')

iGraphite = openmc.Material(6,name='iGraphite')
iGraphite.set_density('g/cm3', 1.73)
iGraphite.add_element('C', 1.0)
iGraphite.add_s_alpha_beta('c_Graphite')

oGraphite = openmc.Material(7,name='oGraphite')
oGraphite.set_density('g/cm3', 1.73)
oGraphite.add_element('C', 1.0)
oGraphite.add_s_alpha_beta('c_Graphite')

spheres = [openmc.Sphere(r=r*1e-4)
               for r in [250., 340., 380., 415., 455.]]
cells = [openmc.Cell(fill=fuel,      region=-spheres[0]),
         openmc.Cell(fill=buff,      region=+spheres[0] &-spheres[1]),
         openmc.Cell(fill=iPyC,      region=+spheres[1] &-spheres[2]),
         openmc.Cell(fill=SiC,       region=+spheres[2] &-spheres[3]),
         openmc.Cell(fill=oPyC,      region=+spheres[3] &-spheres[4]),
         openmc.Cell(fill=iGraphite, region=+spheres[4])]

x = triso_univ = openmc.Universe(cells=cells)
iii = [openmc.Cell(fill=iGraphite, region=+spheres[4])]
z = openmc.Universe(cells=iii)
iPebble_r = openmc.Sphere(r=2.5)
iPebble = openmc.Cell(region=-iPebble_r)
 
args = get_args()
latt = args.type

iPebble.fill=get_lat(latt)
oPebble_r = openmc.Sphere(r=3, boundary_type='reflective')
oPebble = openmc.Cell(region=-oPebble_r & +iPebble_r)
oPebble.fill = oGraphite

univ = openmc.Universe(cells=[iPebble, oPebble])

geom = openmc.Geometry(univ)
geom.export_to_xml()

mats = list(geom.get_all_materials().values())
openmc.Materials(mats).export_to_xml()

settings = openmc.Settings()
settings.run_mode = 'plot'
settings.export_to_xml()
    
get_plot(geom)
