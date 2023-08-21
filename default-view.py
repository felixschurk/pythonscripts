# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
scalar_0000vtk = LegacyVTKReader(registrationName='scalar_0000.vtk*', FileNames=['/home/felix/data/juelich/data/scalar_0000.vtk', '/home/felix/data/juelich/data/scalar_0001.vtk', '/home/felix/data/juelich/data/scalar_0002.vtk', '/home/felix/data/juelich/data/scalar_0003.vtk', '/home/felix/data/juelich/data/scalar_0004.vtk', '/home/felix/data/juelich/data/scalar_0005.vtk', '/home/felix/data/juelich/data/scalar_0006.vtk', '/home/felix/data/juelich/data/scalar_0007.vtk', '/home/felix/data/juelich/data/scalar_0008.vtk', '/home/felix/data/juelich/data/scalar_0009.vtk', '/home/felix/data/juelich/data/scalar_0010.vtk', '/home/felix/data/juelich/data/scalar_0011.vtk', '/home/felix/data/juelich/data/scalar_0012.vtk', '/home/felix/data/juelich/data/scalar_0013.vtk', '/home/felix/data/juelich/data/scalar_0014.vtk', '/home/felix/data/juelich/data/scalar_0015.vtk', '/home/felix/data/juelich/data/scalar_0016.vtk', '/home/felix/data/juelich/data/scalar_0017.vtk', '/home/felix/data/juelich/data/scalar_0018.vtk', '/home/felix/data/juelich/data/scalar_0019.vtk', '/home/felix/data/juelich/data/scalar_0020.vtk', '/home/felix/data/juelich/data/scalar_0021.vtk', '/home/felix/data/juelich/data/scalar_0022.vtk', '/home/felix/data/juelich/data/scalar_0023.vtk', '/home/felix/data/juelich/data/scalar_0024.vtk', '/home/felix/data/juelich/data/scalar_0025.vtk', '/home/felix/data/juelich/data/scalar_0026.vtk', '/home/felix/data/juelich/data/scalar_0027.vtk', '/home/felix/data/juelich/data/scalar_0028.vtk', '/home/felix/data/juelich/data/scalar_0029.vtk', '/home/felix/data/juelich/data/scalar_0030.vtk', '/home/felix/data/juelich/data/scalar_0031.vtk', '/home/felix/data/juelich/data/scalar_0032.vtk', '/home/felix/data/juelich/data/scalar_0033.vtk', '/home/felix/data/juelich/data/scalar_0034.vtk', '/home/felix/data/juelich/data/scalar_0035.vtk', '/home/felix/data/juelich/data/scalar_0036.vtk', '/home/felix/data/juelich/data/scalar_0037.vtk', '/home/felix/data/juelich/data/scalar_0038.vtk', '/home/felix/data/juelich/data/scalar_0039.vtk', '/home/felix/data/juelich/data/scalar_0040.vtk', '/home/felix/data/juelich/data/scalar_0041.vtk', '/home/felix/data/juelich/data/scalar_0042.vtk', '/home/felix/data/juelich/data/scalar_0043.vtk', '/home/felix/data/juelich/data/scalar_0044.vtk', '/home/felix/data/juelich/data/scalar_0045.vtk', '/home/felix/data/juelich/data/scalar_0046.vtk', '/home/felix/data/juelich/data/scalar_0047.vtk', '/home/felix/data/juelich/data/scalar_0048.vtk', '/home/felix/data/juelich/data/scalar_0049.vtk', '/home/felix/data/juelich/data/scalar_0050.vtk', '/home/felix/data/juelich/data/scalar_0051.vtk', '/home/felix/data/juelich/data/scalar_0052.vtk', '/home/felix/data/juelich/data/scalar_0053.vtk', '/home/felix/data/juelich/data/scalar_0054.vtk', '/home/felix/data/juelich/data/scalar_0055.vtk', '/home/felix/data/juelich/data/scalar_0056.vtk', '/home/felix/data/juelich/data/scalar_0057.vtk', '/home/felix/data/juelich/data/scalar_0058.vtk', '/home/felix/data/juelich/data/scalar_0059.vtk', '/home/felix/data/juelich/data/scalar_0060.vtk', '/home/felix/data/juelich/data/scalar_0061.vtk', '/home/felix/data/juelich/data/scalar_0062.vtk', '/home/felix/data/juelich/data/scalar_0063.vtk', '/home/felix/data/juelich/data/scalar_0064.vtk', '/home/felix/data/juelich/data/scalar_0065.vtk', '/home/felix/data/juelich/data/scalar_0066.vtk', '/home/felix/data/juelich/data/scalar_0067.vtk', '/home/felix/data/juelich/data/scalar_0068.vtk', '/home/felix/data/juelich/data/scalar_0069.vtk', '/home/felix/data/juelich/data/scalar_0070.vtk', '/home/felix/data/juelich/data/scalar_0071.vtk', '/home/felix/data/juelich/data/scalar_0072.vtk', '/home/felix/data/juelich/data/scalar_0073.vtk', '/home/felix/data/juelich/data/scalar_0074.vtk', '/home/felix/data/juelich/data/scalar_0075.vtk', '/home/felix/data/juelich/data/scalar_0076.vtk', '/home/felix/data/juelich/data/scalar_0077.vtk', '/home/felix/data/juelich/data/scalar_0078.vtk', '/home/felix/data/juelich/data/scalar_0079.vtk', '/home/felix/data/juelich/data/scalar_0080.vtk', '/home/felix/data/juelich/data/scalar_0081.vtk', '/home/felix/data/juelich/data/scalar_0082.vtk', '/home/felix/data/juelich/data/scalar_0083.vtk', '/home/felix/data/juelich/data/scalar_0084.vtk', '/home/felix/data/juelich/data/scalar_0085.vtk', '/home/felix/data/juelich/data/scalar_0086.vtk', '/home/felix/data/juelich/data/scalar_0087.vtk', '/home/felix/data/juelich/data/scalar_0088.vtk', '/home/felix/data/juelich/data/scalar_0089.vtk', '/home/felix/data/juelich/data/scalar_0090.vtk', '/home/felix/data/juelich/data/scalar_0091.vtk', '/home/felix/data/juelich/data/scalar_0092.vtk', '/home/felix/data/juelich/data/scalar_0093.vtk', '/home/felix/data/juelich/data/scalar_0094.vtk', '/home/felix/data/juelich/data/scalar_0095.vtk', '/home/felix/data/juelich/data/scalar_0096.vtk', '/home/felix/data/juelich/data/scalar_0097.vtk', '/home/felix/data/juelich/data/scalar_0098.vtk', '/home/felix/data/juelich/data/scalar_0099.vtk', '/home/felix/data/juelich/data/scalar_0100.vtk', '/home/felix/data/juelich/data/scalar_0101.vtk', '/home/felix/data/juelich/data/scalar_0102.vtk', '/home/felix/data/juelich/data/scalar_0103.vtk', '/home/felix/data/juelich/data/scalar_0104.vtk', '/home/felix/data/juelich/data/scalar_0105.vtk', '/home/felix/data/juelich/data/scalar_0106.vtk', '/home/felix/data/juelich/data/scalar_0107.vtk', '/home/felix/data/juelich/data/scalar_0108.vtk', '/home/felix/data/juelich/data/scalar_0109.vtk', '/home/felix/data/juelich/data/scalar_0110.vtk', '/home/felix/data/juelich/data/scalar_0111.vtk', '/home/felix/data/juelich/data/scalar_0112.vtk', '/home/felix/data/juelich/data/scalar_0113.vtk', '/home/felix/data/juelich/data/scalar_0114.vtk', '/home/felix/data/juelich/data/scalar_0115.vtk', '/home/felix/data/juelich/data/scalar_0116.vtk', '/home/felix/data/juelich/data/scalar_0117.vtk', '/home/felix/data/juelich/data/scalar_0118.vtk', '/home/felix/data/juelich/data/scalar_0119.vtk', '/home/felix/data/juelich/data/scalar_0120.vtk', '/home/felix/data/juelich/data/scalar_0121.vtk', '/home/felix/data/juelich/data/scalar_0122.vtk', '/home/felix/data/juelich/data/scalar_0123.vtk', '/home/felix/data/juelich/data/scalar_0124.vtk', '/home/felix/data/juelich/data/scalar_0125.vtk', '/home/felix/data/juelich/data/scalar_0126.vtk', '/home/felix/data/juelich/data/scalar_0127.vtk', '/home/felix/data/juelich/data/scalar_0128.vtk', '/home/felix/data/juelich/data/scalar_0129.vtk', '/home/felix/data/juelich/data/scalar_0130.vtk', '/home/felix/data/juelich/data/scalar_0131.vtk', '/home/felix/data/juelich/data/scalar_0132.vtk', '/home/felix/data/juelich/data/scalar_0133.vtk', '/home/felix/data/juelich/data/scalar_0134.vtk', '/home/felix/data/juelich/data/scalar_0135.vtk', '/home/felix/data/juelich/data/scalar_0136.vtk', '/home/felix/data/juelich/data/scalar_0137.vtk', '/home/felix/data/juelich/data/scalar_0138.vtk', '/home/felix/data/juelich/data/scalar_0139.vtk', '/home/felix/data/juelich/data/scalar_0140.vtk', '/home/felix/data/juelich/data/scalar_0141.vtk', '/home/felix/data/juelich/data/scalar_0142.vtk', '/home/felix/data/juelich/data/scalar_0143.vtk', '/home/felix/data/juelich/data/scalar_0144.vtk', '/home/felix/data/juelich/data/scalar_0145.vtk', '/home/felix/data/juelich/data/scalar_0146.vtk', '/home/felix/data/juelich/data/scalar_0147.vtk', '/home/felix/data/juelich/data/scalar_0148.vtk', '/home/felix/data/juelich/data/scalar_0149.vtk', '/home/felix/data/juelich/data/scalar_0150.vtk', '/home/felix/data/juelich/data/scalar_0151.vtk', '/home/felix/data/juelich/data/scalar_0152.vtk', '/home/felix/data/juelich/data/scalar_0153.vtk', '/home/felix/data/juelich/data/scalar_0154.vtk', '/home/felix/data/juelich/data/scalar_0155.vtk', '/home/felix/data/juelich/data/scalar_0156.vtk', '/home/felix/data/juelich/data/scalar_0157.vtk', '/home/felix/data/juelich/data/scalar_0158.vtk', '/home/felix/data/juelich/data/scalar_0159.vtk', '/home/felix/data/juelich/data/scalar_0160.vtk', '/home/felix/data/juelich/data/scalar_0161.vtk', '/home/felix/data/juelich/data/scalar_0162.vtk', '/home/felix/data/juelich/data/scalar_0163.vtk', '/home/felix/data/juelich/data/scalar_0164.vtk', '/home/felix/data/juelich/data/scalar_0165.vtk', '/home/felix/data/juelich/data/scalar_0166.vtk', '/home/felix/data/juelich/data/scalar_0167.vtk', '/home/felix/data/juelich/data/scalar_0168.vtk', '/home/felix/data/juelich/data/scalar_0169.vtk', '/home/felix/data/juelich/data/scalar_0170.vtk', '/home/felix/data/juelich/data/scalar_0171.vtk', '/home/felix/data/juelich/data/scalar_0172.vtk', '/home/felix/data/juelich/data/scalar_0173.vtk', '/home/felix/data/juelich/data/scalar_0174.vtk', '/home/felix/data/juelich/data/scalar_0175.vtk', '/home/felix/data/juelich/data/scalar_0176.vtk', '/home/felix/data/juelich/data/scalar_0177.vtk', '/home/felix/data/juelich/data/scalar_0178.vtk', '/home/felix/data/juelich/data/scalar_0179.vtk', '/home/felix/data/juelich/data/scalar_0180.vtk', '/home/felix/data/juelich/data/scalar_0181.vtk', '/home/felix/data/juelich/data/scalar_0182.vtk', '/home/felix/data/juelich/data/scalar_0183.vtk', '/home/felix/data/juelich/data/scalar_0184.vtk', '/home/felix/data/juelich/data/scalar_0185.vtk', '/home/felix/data/juelich/data/scalar_0186.vtk', '/home/felix/data/juelich/data/scalar_0187.vtk', '/home/felix/data/juelich/data/scalar_0188.vtk', '/home/felix/data/juelich/data/scalar_0189.vtk', '/home/felix/data/juelich/data/scalar_0190.vtk', '/home/felix/data/juelich/data/scalar_0191.vtk', '/home/felix/data/juelich/data/scalar_0192.vtk', '/home/felix/data/juelich/data/scalar_0193.vtk', '/home/felix/data/juelich/data/scalar_0194.vtk', '/home/felix/data/juelich/data/scalar_0195.vtk', '/home/felix/data/juelich/data/scalar_0196.vtk', '/home/felix/data/juelich/data/scalar_0197.vtk', '/home/felix/data/juelich/data/scalar_0198.vtk', '/home/felix/data/juelich/data/scalar_0199.vtk', '/home/felix/data/juelich/data/scalar_0200.vtk', '/home/felix/data/juelich/data/scalar_0201.vtk', '/home/felix/data/juelich/data/scalar_0202.vtk', '/home/felix/data/juelich/data/scalar_0203.vtk', '/home/felix/data/juelich/data/scalar_0204.vtk', '/home/felix/data/juelich/data/scalar_0205.vtk', '/home/felix/data/juelich/data/scalar_0206.vtk', '/home/felix/data/juelich/data/scalar_0207.vtk', '/home/felix/data/juelich/data/scalar_0208.vtk', '/home/felix/data/juelich/data/scalar_0209.vtk', '/home/felix/data/juelich/data/scalar_0210.vtk', '/home/felix/data/juelich/data/scalar_0211.vtk', '/home/felix/data/juelich/data/scalar_0212.vtk', '/home/felix/data/juelich/data/scalar_0213.vtk', '/home/felix/data/juelich/data/scalar_0214.vtk', '/home/felix/data/juelich/data/scalar_0215.vtk', '/home/felix/data/juelich/data/scalar_0216.vtk', '/home/felix/data/juelich/data/scalar_0217.vtk', '/home/felix/data/juelich/data/scalar_0218.vtk', '/home/felix/data/juelich/data/scalar_0219.vtk', '/home/felix/data/juelich/data/scalar_0220.vtk', '/home/felix/data/juelich/data/scalar_0221.vtk', '/home/felix/data/juelich/data/scalar_0222.vtk', '/home/felix/data/juelich/data/scalar_0223.vtk', '/home/felix/data/juelich/data/scalar_0224.vtk', '/home/felix/data/juelich/data/scalar_0225.vtk', '/home/felix/data/juelich/data/scalar_0226.vtk', '/home/felix/data/juelich/data/scalar_0227.vtk', '/home/felix/data/juelich/data/scalar_0228.vtk', '/home/felix/data/juelich/data/scalar_0229.vtk', '/home/felix/data/juelich/data/scalar_0230.vtk', '/home/felix/data/juelich/data/scalar_0231.vtk', '/home/felix/data/juelich/data/scalar_0232.vtk', '/home/felix/data/juelich/data/scalar_0233.vtk', '/home/felix/data/juelich/data/scalar_0234.vtk', '/home/felix/data/juelich/data/scalar_0235.vtk', '/home/felix/data/juelich/data/scalar_0236.vtk', '/home/felix/data/juelich/data/scalar_0237.vtk', '/home/felix/data/juelich/data/scalar_0238.vtk', '/home/felix/data/juelich/data/scalar_0239.vtk', '/home/felix/data/juelich/data/scalar_0240.vtk', '/home/felix/data/juelich/data/scalar_0241.vtk', '/home/felix/data/juelich/data/scalar_0242.vtk', '/home/felix/data/juelich/data/scalar_0243.vtk', '/home/felix/data/juelich/data/scalar_0244.vtk', '/home/felix/data/juelich/data/scalar_0245.vtk', '/home/felix/data/juelich/data/scalar_0246.vtk', '/home/felix/data/juelich/data/scalar_0247.vtk', '/home/felix/data/juelich/data/scalar_0248.vtk', '/home/felix/data/juelich/data/scalar_0249.vtk', '/home/felix/data/juelich/data/scalar_0250.vtk', '/home/felix/data/juelich/data/scalar_0251.vtk', '/home/felix/data/juelich/data/scalar_0252.vtk', '/home/felix/data/juelich/data/scalar_0253.vtk', '/home/felix/data/juelich/data/scalar_0254.vtk', '/home/felix/data/juelich/data/scalar_0255.vtk', '/home/felix/data/juelich/data/scalar_0256.vtk', '/home/felix/data/juelich/data/scalar_0257.vtk', '/home/felix/data/juelich/data/scalar_0258.vtk', '/home/felix/data/juelich/data/scalar_0259.vtk', '/home/felix/data/juelich/data/scalar_0260.vtk', '/home/felix/data/juelich/data/scalar_0261.vtk', '/home/felix/data/juelich/data/scalar_0262.vtk', '/home/felix/data/juelich/data/scalar_0263.vtk', '/home/felix/data/juelich/data/scalar_0264.vtk', '/home/felix/data/juelich/data/scalar_0265.vtk', '/home/felix/data/juelich/data/scalar_0266.vtk', '/home/felix/data/juelich/data/scalar_0267.vtk', '/home/felix/data/juelich/data/scalar_0268.vtk', '/home/felix/data/juelich/data/scalar_0269.vtk', '/home/felix/data/juelich/data/scalar_0270.vtk', '/home/felix/data/juelich/data/scalar_0271.vtk', '/home/felix/data/juelich/data/scalar_0272.vtk', '/home/felix/data/juelich/data/scalar_0273.vtk', '/home/felix/data/juelich/data/scalar_0274.vtk', '/home/felix/data/juelich/data/scalar_0275.vtk', '/home/felix/data/juelich/data/scalar_0276.vtk', '/home/felix/data/juelich/data/scalar_0277.vtk', '/home/felix/data/juelich/data/scalar_0278.vtk', '/home/felix/data/juelich/data/scalar_0279.vtk', '/home/felix/data/juelich/data/scalar_0280.vtk', '/home/felix/data/juelich/data/scalar_0281.vtk', '/home/felix/data/juelich/data/scalar_0282.vtk', '/home/felix/data/juelich/data/scalar_0283.vtk', '/home/felix/data/juelich/data/scalar_0284.vtk', '/home/felix/data/juelich/data/scalar_0285.vtk', '/home/felix/data/juelich/data/scalar_0286.vtk', '/home/felix/data/juelich/data/scalar_0287.vtk', '/home/felix/data/juelich/data/scalar_0288.vtk', '/home/felix/data/juelich/data/scalar_0289.vtk', '/home/felix/data/juelich/data/scalar_0290.vtk', '/home/felix/data/juelich/data/scalar_0291.vtk', '/home/felix/data/juelich/data/scalar_0292.vtk', '/home/felix/data/juelich/data/scalar_0293.vtk', '/home/felix/data/juelich/data/scalar_0294.vtk', '/home/felix/data/juelich/data/scalar_0295.vtk', '/home/felix/data/juelich/data/scalar_0296.vtk', '/home/felix/data/juelich/data/scalar_0297.vtk', '/home/felix/data/juelich/data/scalar_0298.vtk', '/home/felix/data/juelich/data/scalar_0299.vtk', '/home/felix/data/juelich/data/scalar_0300.vtk', '/home/felix/data/juelich/data/scalar_0301.vtk', '/home/felix/data/juelich/data/scalar_0302.vtk', '/home/felix/data/juelich/data/scalar_0303.vtk', '/home/felix/data/juelich/data/scalar_0304.vtk', '/home/felix/data/juelich/data/scalar_0305.vtk', '/home/felix/data/juelich/data/scalar_0306.vtk', '/home/felix/data/juelich/data/scalar_0307.vtk', '/home/felix/data/juelich/data/scalar_0308.vtk', '/home/felix/data/juelich/data/scalar_0309.vtk', '/home/felix/data/juelich/data/scalar_0310.vtk', '/home/felix/data/juelich/data/scalar_0311.vtk', '/home/felix/data/juelich/data/scalar_0312.vtk', '/home/felix/data/juelich/data/scalar_0313.vtk', '/home/felix/data/juelich/data/scalar_0314.vtk', '/home/felix/data/juelich/data/scalar_0315.vtk', '/home/felix/data/juelich/data/scalar_0316.vtk', '/home/felix/data/juelich/data/scalar_0317.vtk', '/home/felix/data/juelich/data/scalar_0318.vtk', '/home/felix/data/juelich/data/scalar_0319.vtk', '/home/felix/data/juelich/data/scalar_0320.vtk', '/home/felix/data/juelich/data/scalar_0321.vtk', '/home/felix/data/juelich/data/scalar_0322.vtk', '/home/felix/data/juelich/data/scalar_0323.vtk', '/home/felix/data/juelich/data/scalar_0324.vtk', '/home/felix/data/juelich/data/scalar_0325.vtk', '/home/felix/data/juelich/data/scalar_0326.vtk', '/home/felix/data/juelich/data/scalar_0327.vtk', '/home/felix/data/juelich/data/scalar_0328.vtk', '/home/felix/data/juelich/data/scalar_0329.vtk', '/home/felix/data/juelich/data/scalar_0330.vtk', '/home/felix/data/juelich/data/scalar_0331.vtk', '/home/felix/data/juelich/data/scalar_0332.vtk', '/home/felix/data/juelich/data/scalar_0333.vtk', '/home/felix/data/juelich/data/scalar_0334.vtk', '/home/felix/data/juelich/data/scalar_0335.vtk', '/home/felix/data/juelich/data/scalar_0336.vtk', '/home/felix/data/juelich/data/scalar_0337.vtk', '/home/felix/data/juelich/data/scalar_0338.vtk', '/home/felix/data/juelich/data/scalar_0339.vtk', '/home/felix/data/juelich/data/scalar_0340.vtk', '/home/felix/data/juelich/data/scalar_0341.vtk', '/home/felix/data/juelich/data/scalar_0342.vtk', '/home/felix/data/juelich/data/scalar_0343.vtk', '/home/felix/data/juelich/data/scalar_0344.vtk', '/home/felix/data/juelich/data/scalar_0345.vtk', '/home/felix/data/juelich/data/scalar_0346.vtk', '/home/felix/data/juelich/data/scalar_0347.vtk', '/home/felix/data/juelich/data/scalar_0348.vtk', '/home/felix/data/juelich/data/scalar_0349.vtk', '/home/felix/data/juelich/data/scalar_0350.vtk', '/home/felix/data/juelich/data/scalar_0351.vtk', '/home/felix/data/juelich/data/scalar_0352.vtk', '/home/felix/data/juelich/data/scalar_0353.vtk', '/home/felix/data/juelich/data/scalar_0354.vtk', '/home/felix/data/juelich/data/scalar_0355.vtk', '/home/felix/data/juelich/data/scalar_0356.vtk', '/home/felix/data/juelich/data/scalar_0357.vtk', '/home/felix/data/juelich/data/scalar_0358.vtk', '/home/felix/data/juelich/data/scalar_0359.vtk', '/home/felix/data/juelich/data/scalar_0360.vtk', '/home/felix/data/juelich/data/scalar_0361.vtk', '/home/felix/data/juelich/data/scalar_0362.vtk', '/home/felix/data/juelich/data/scalar_0363.vtk', '/home/felix/data/juelich/data/scalar_0364.vtk', '/home/felix/data/juelich/data/scalar_0365.vtk', '/home/felix/data/juelich/data/scalar_0366.vtk', '/home/felix/data/juelich/data/scalar_0367.vtk', '/home/felix/data/juelich/data/scalar_0368.vtk', '/home/felix/data/juelich/data/scalar_0369.vtk', '/home/felix/data/juelich/data/scalar_0370.vtk', '/home/felix/data/juelich/data/scalar_0371.vtk', '/home/felix/data/juelich/data/scalar_0372.vtk', '/home/felix/data/juelich/data/scalar_0373.vtk', '/home/felix/data/juelich/data/scalar_0374.vtk', '/home/felix/data/juelich/data/scalar_0375.vtk', '/home/felix/data/juelich/data/scalar_0376.vtk', '/home/felix/data/juelich/data/scalar_0377.vtk', '/home/felix/data/juelich/data/scalar_0378.vtk', '/home/felix/data/juelich/data/scalar_0379.vtk', '/home/felix/data/juelich/data/scalar_0380.vtk', '/home/felix/data/juelich/data/scalar_0381.vtk', '/home/felix/data/juelich/data/scalar_0382.vtk', '/home/felix/data/juelich/data/scalar_0383.vtk', '/home/felix/data/juelich/data/scalar_0384.vtk', '/home/felix/data/juelich/data/scalar_0385.vtk', '/home/felix/data/juelich/data/scalar_0386.vtk', '/home/felix/data/juelich/data/scalar_0387.vtk', '/home/felix/data/juelich/data/scalar_0388.vtk', '/home/felix/data/juelich/data/scalar_0389.vtk', '/home/felix/data/juelich/data/scalar_0390.vtk', '/home/felix/data/juelich/data/scalar_0391.vtk', '/home/felix/data/juelich/data/scalar_0392.vtk', '/home/felix/data/juelich/data/scalar_0393.vtk', '/home/felix/data/juelich/data/scalar_0394.vtk', '/home/felix/data/juelich/data/scalar_0395.vtk', '/home/felix/data/juelich/data/scalar_0396.vtk', '/home/felix/data/juelich/data/scalar_0397.vtk', '/home/felix/data/juelich/data/scalar_0398.vtk', '/home/felix/data/juelich/data/scalar_0399.vtk', '/home/felix/data/juelich/data/scalar_0400.vtk'])

# get animation scene
animationScene1 = GetAnimationScene()

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
scalar_0000vtkDisplay = Show(scalar_0000vtk, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
scalar_0000vtkDisplay.Representation = 'Outline'
scalar_0000vtkDisplay.ColorArrayName = ['CELLS', '']
scalar_0000vtkDisplay.SelectTCoordArray = 'None'
scalar_0000vtkDisplay.SelectNormalArray = 'None'
scalar_0000vtkDisplay.SelectTangentArray = 'None'
scalar_0000vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
scalar_0000vtkDisplay.SelectOrientationVectors = 'None'
scalar_0000vtkDisplay.ScaleFactor = 2.125
scalar_0000vtkDisplay.SelectScaleArray = 'Rho'
scalar_0000vtkDisplay.GlyphType = 'Arrow'
scalar_0000vtkDisplay.GlyphTableIndexArray = 'Rho'
scalar_0000vtkDisplay.GaussianRadius = 0.10625
scalar_0000vtkDisplay.SetScaleArray = [None, '']
scalar_0000vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
scalar_0000vtkDisplay.OpacityArray = [None, '']
scalar_0000vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
scalar_0000vtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
scalar_0000vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
scalar_0000vtkDisplay.ScalarOpacityUnitDistance = 1.082531754730548
scalar_0000vtkDisplay.OpacityArrayName = ['CELLS', 'Rho']
scalar_0000vtkDisplay.ColorArray2Name = ['CELLS', 'Rho']
scalar_0000vtkDisplay.IsosurfaceValues = [-3.91155743598938]
scalar_0000vtkDisplay.SliceFunction = 'Plane'
scalar_0000vtkDisplay.Slice = 17
scalar_0000vtkDisplay.SelectInputVectors = [None, '']
scalar_0000vtkDisplay.WriteLog = ''

# init the 'Plane' selected for 'SliceFunction'
scalar_0000vtkDisplay.SliceFunction.Origin = [10.0, 10.0, 10.0]

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(registrationName='CellDatatoPointData1', Input=scalar_0000vtk)
cellDatatoPointData1.CellDataArraytoprocess = ['Rho']

# show data in view
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

# hide data in view
Hide(scalar_0000vtk, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=cellDatatoPointData1)
contour1.ContourBy = ['POINTS', 'Rho']
contour1.Isosurfaces = [-3.7940866947174072]
contour1.PointMergeMethod = 'Uniform Binning'

# Properties modified on contour1
contour1.Isosurfaces = [-7.5881733894348145, -7.194059000517193, -6.799944611599571, -6.405830222681949, -6.0117158337643275, -5.617601444846706, -5.223487055929083, -4.829372667011461, -4.43525827809384, -4.041143889176218, -3.647029500258596, -3.2529151113409744, -2.858800722423352, -2.46468633350573, -2.0705719445881083, -1.6764575556704866, -1.2823431667528649, -0.8882287778352431, -0.4941143889176214, -0.09999999999999964]

# show data in view
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'Rho'
rhoLUT = GetColorTransferFunction('Rho')

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'Rho']
contour1Display.LookupTable = rhoLUT
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'Normals'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleArray = 'Rho'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 2.072467178106308
contour1Display.SelectScaleArray = 'Rho'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'Rho'
contour1Display.GaussianRadius = 0.1036233589053154
contour1Display.SetScaleArray = ['POINTS', 'Rho']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'Rho']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'
contour1Display.SelectInputVectors = ['POINTS', 'Normals']
contour1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [-7.194058895111084, 0.0, 0.5, 0.0, -0.10000000149011612, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [-7.194058895111084, 0.0, 0.5, 0.0, -0.10000000149011612, 1.0, 0.5, 0.0]

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'Rho'
rhoPWF = GetOpacityTransferFunction('Rho')

# get 2D transfer function for 'Rho'
rhoTF2D = GetTransferFunction2D('Rho')

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=contour1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'Rho']
clip1.Value = -3.6470294483006

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [10.019999623298645, 9.979163646697998, 9.993813782930374]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [10.019999623298645, 9.979163646697998, 9.993813782930374]

# Properties modified on clip1.ClipType
clip1.ClipType.Normal = [0.0, 0.0, 1.0]

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

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

# hide data in view
Hide(contour1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1339, 737)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-11.610421042126848, 62.873726213447114, 52.34526369106585]
renderView1.CameraFocalPoint = [10.0, 10.0, 10.0]
renderView1.CameraViewUp = [0.12391964781455654, 0.6506575498444777, -0.7491920139162572]
renderView1.CameraParallelScale = 18.40303983041932

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).