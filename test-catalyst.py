# script-version: 2.0
# Catalyst state generated using paraview version 5.11.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1609, 1036]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [10.0, 10.0, 10.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-39.59832964672915, 42.39680953405328, 49.32194052494263]
renderView1.CameraFocalPoint = [10.0, 10.000000000000007, 10.0]
renderView1.CameraViewUp = [0.44936152270147445, 0.8793265428911884, -0.1576675390891968]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 18.40303983041932

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1609, 1036)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
scalar_0000vtk = LegacyVTKReader(registrationName='scalar_0000.vtk*', FileNames=['/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0000.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0001.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0002.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0003.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0004.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0005.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0006.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0007.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0008.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0009.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0010.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0011.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0012.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0013.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0014.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0015.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0016.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0017.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0018.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0019.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0020.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0021.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0022.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0023.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0024.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0025.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0026.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0027.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0028.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0029.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0030.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0031.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0032.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0033.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0034.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0035.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0036.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0037.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0038.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0039.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0040.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0041.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0042.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0043.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0044.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0045.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0046.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0047.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0048.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0049.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0050.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0051.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0052.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0053.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0054.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0055.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0056.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0057.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0058.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0059.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0060.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0061.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0062.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0063.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0064.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0065.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0066.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0067.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0068.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0069.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0070.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0071.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0072.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0073.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0074.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0075.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0076.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0077.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0078.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0079.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0080.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0081.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0082.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0083.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0084.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0085.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0086.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0087.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0088.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0089.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0090.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0091.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0092.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0093.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0094.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0095.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0096.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0097.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0098.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0099.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0100.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0101.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0102.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0103.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0104.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0105.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0106.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0107.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0108.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0109.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0110.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0111.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0112.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0113.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0114.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0115.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0116.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0117.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0118.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0119.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0120.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0121.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0122.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0123.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0124.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0125.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0126.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0127.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0128.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0129.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0130.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0131.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0132.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0133.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0134.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0135.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0136.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0137.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0138.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0139.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0140.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0141.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0142.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0143.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0144.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0145.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0146.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0147.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0148.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0149.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0150.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0151.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0152.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0153.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0154.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0155.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0156.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0157.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0158.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0159.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0160.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0161.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0162.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0163.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0164.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0165.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0166.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0167.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0168.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0169.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0170.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0171.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0172.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0173.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0174.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0175.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0176.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0177.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0178.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0179.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0180.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0181.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0182.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0183.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0184.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0185.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0186.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0187.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0188.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0189.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0190.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0191.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0192.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0193.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0194.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0195.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0196.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0197.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0198.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0199.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0200.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0201.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0202.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0203.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0204.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0205.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0206.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0207.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0208.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0209.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0210.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0211.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0212.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0213.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0214.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0215.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0216.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0217.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0218.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0219.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0220.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0221.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0222.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0223.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0224.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0225.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0226.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0227.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0228.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0229.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0230.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0231.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0232.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0233.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0234.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0235.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0236.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0237.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0238.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0239.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0240.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0241.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0242.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0243.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0244.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0245.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0246.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0247.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0248.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0249.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0250.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0251.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0252.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0253.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0254.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0255.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0256.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0257.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0258.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0259.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0260.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0261.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0262.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0263.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0264.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0265.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0266.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0267.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0268.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0269.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0270.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0271.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0272.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0273.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0274.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0275.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0276.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0277.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0278.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0279.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0280.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0281.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0282.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0283.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0284.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0285.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0286.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0287.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0288.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0289.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0290.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0291.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0292.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0293.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0294.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0295.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0296.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0297.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0298.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0299.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0300.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0301.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0302.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0303.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0304.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0305.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0306.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0307.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0308.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0309.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0310.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0311.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0312.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0313.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0314.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0315.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0316.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0317.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0318.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0319.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0320.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0321.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0322.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0323.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0324.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0325.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0326.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0327.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0328.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0329.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0330.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0331.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0332.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0333.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0334.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0335.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0336.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0337.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0338.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0339.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0340.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0341.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0342.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0343.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0344.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0345.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0346.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0347.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0348.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0349.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0350.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0351.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0352.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0353.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0354.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0355.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0356.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0357.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0358.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0359.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0360.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0361.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0362.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0363.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0364.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0365.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0366.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0367.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0368.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0369.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0370.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0371.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0372.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0373.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0374.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0375.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0376.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0377.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0378.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0379.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0380.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0381.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0382.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0383.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0384.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0385.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0386.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0387.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0388.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0389.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0390.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0391.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0392.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0393.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0394.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0395.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0396.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0397.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0398.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0399.vtk', '/p/project/ccstma/schurk1/in-situ/ippl/build_2022/alpine/data/scalar_0400.vtk'])

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(registrationName='CellDatatoPointData1', Input=scalar_0000vtk)
cellDatatoPointData1.CellDataArraytoprocess = ['Rho']

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=cellDatatoPointData1)
contour1.ContourBy = ['POINTS', 'Rho']
contour1.Isosurfaces = [-7.5881733894348145, -7.194059000517193, -6.799944611599571, -6.405830222681949, -6.0117158337643275, -5.617601444846706, -5.223487055929083, -4.829372667011461, -4.43525827809384, -4.041143889176218, -3.647029500258596, -3.2529151113409744, -2.858800722423352, -2.46468633350573, -2.0705719445881083, -1.6764575556704866, -1.2823431667528649, -0.8882287778352431, -0.4941143889176214, -0.09999999999999964]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=contour1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'Rho']
clip1.Value = -3.6470294483006

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [10.019999623298645, 9.979163646697998, 9.993813782930374]
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [10.019999623298645, 9.979163646697998, 9.993813782930374]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from cellDatatoPointData1
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
cellDatatoPointData1Display.Representation = 'Outline'
cellDatatoPointData1Display.ColorArrayName = ['POINTS', '']
cellDatatoPointData1Display.SelectTCoordArray = 'None'
cellDatatoPointData1Display.SelectNormalArray = 'None'
cellDatatoPointData1Display.SelectTangentArray = 'None'
cellDatatoPointData1Display.OSPRayScaleArray = 'Rho'
cellDatatoPointData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.SelectOrientationVectors = 'None'
cellDatatoPointData1Display.ScaleFactor = 2.125
cellDatatoPointData1Display.SelectScaleArray = 'Rho'
cellDatatoPointData1Display.GlyphType = 'Arrow'
cellDatatoPointData1Display.GlyphTableIndexArray = 'Rho'
cellDatatoPointData1Display.GaussianRadius = 0.10625
cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'Rho']
cellDatatoPointData1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.OpacityArray = ['POINTS', 'Rho']
cellDatatoPointData1Display.OpacityTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData1Display.PolarAxes = 'PolarAxesRepresentation'
cellDatatoPointData1Display.ScalarOpacityUnitDistance = 1.082531754730548
cellDatatoPointData1Display.OpacityArrayName = ['POINTS', 'Rho']
cellDatatoPointData1Display.ColorArray2Name = ['POINTS', 'Rho']
cellDatatoPointData1Display.IsosurfaceValues = [-3.7940866947174072]
cellDatatoPointData1Display.SliceFunction = 'Plane'
cellDatatoPointData1Display.Slice = 17
cellDatatoPointData1Display.SelectInputVectors = [None, '']
cellDatatoPointData1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cellDatatoPointData1Display.ScaleTransferFunction.Points = [-7.5881733894348145, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cellDatatoPointData1Display.OpacityTransferFunction.Points = [-7.5881733894348145, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
cellDatatoPointData1Display.SliceFunction.Origin = [10.0, 10.0, 10.0]

# show data from clip1
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# get 2D transfer function for 'Rho'
rhoTF2D = GetTransferFunction2D('Rho')

# get color transfer function/color map for 'Rho'
rhoLUT = GetColorTransferFunction('Rho')
rhoLUT.TransferFunction2D = rhoTF2D
rhoLUT.RGBPoints = [-7.194058895111084, 0.231373, 0.298039, 0.752941, -3.6470294483006, 0.865003, 0.865003, 0.865003, -0.10000000149011612, 0.705882, 0.0156863, 0.14902]
rhoLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Rho'
rhoPWF = GetOpacityTransferFunction('Rho')
rhoPWF.Points = [-7.194058895111084, 0.0, 0.5, 0.0, -0.10000000149011612, 1.0, 0.5, 0.0]
rhoPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'Rho']
clip1Display.LookupTable = rhoLUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'Normals'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'Rho'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 1.7960298776626589
clip1Display.SelectScaleArray = 'Rho'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'Rho'
clip1Display.GaussianRadius = 0.08980149388313294
clip1Display.SetScaleArray = ['POINTS', 'Rho']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'Rho']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = rhoPWF
clip1Display.ScalarOpacityUnitDistance = 0.9257296995732877
clip1Display.OpacityArrayName = ['POINTS', 'Rho']
clip1Display.SelectInputVectors = ['POINTS', 'Normals']
clip1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [-7.194058895111084, 0.0, 0.5, 0.0, -0.10000000149011612, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [-7.194058895111084, 0.0, 0.5, 0.0, -0.10000000149011612, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for rhoLUT in view renderView1
rhoLUTColorBar = GetScalarBar(rhoLUT, renderView1)
rhoLUTColorBar.Title = 'Rho'
rhoLUTColorBar.ComponentTitle = ''

# set color bar visibility
rhoLUTColorBar.Visibility = 1

# show color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup extractors
# ----------------------------------------------------------------

# create extractor
pNG1 = CreateExtractor('PNG', renderView1, registrationName='PNG1')
# trace defaults for the extractor.
pNG1.Trigger = 'TimeStep'

# init the 'PNG' selected for 'Writer'
pNG1.Writer.FileName = 'RenderView1_{timestep:06d}{camera}.png'
pNG1.Writer.ImageResolution = [1609, 1036]
pNG1.Writer.Format = 'PNG'

# ----------------------------------------------------------------
# restore active source
SetActiveSource(pNG1)
# ----------------------------------------------------------------

# ------------------------------------------------------------------------------
# Catalyst options
from paraview import catalyst
options = catalyst.Options()
options.GlobalTrigger = 'TimeStep'
options.CatalystLiveTrigger = 'TimeStep'

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    from paraview.simple import SaveExtractsUsingCatalystOptions
    # Code for non in-situ environments; if executing in post-processing
    # i.e. non-Catalyst mode, let's generate extracts using Catalyst options
    SaveExtractsUsingCatalystOptions(options)
