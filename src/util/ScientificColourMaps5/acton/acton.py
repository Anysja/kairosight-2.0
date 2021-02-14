# 
#         acton
#                   www.fabiocrameri.ch/visualisation
from matplotlib.colors import LinearSegmentedColormap      
      
cm_data = [[0.18063, 0.12992, 0.30024],      
           [0.18461, 0.13336, 0.30378],      
           [0.18859, 0.13683, 0.30733],      
           [0.19255, 0.14032, 0.3109],      
           [0.19655, 0.14383, 0.31444],      
           [0.20049, 0.14734, 0.31801],      
           [0.20451, 0.15085, 0.32158],      
           [0.20849, 0.15437, 0.32515],      
           [0.2125, 0.15792, 0.32875],      
           [0.21652, 0.16149, 0.33235],      
           [0.22054, 0.165, 0.33593],      
           [0.22453, 0.16858, 0.33954],      
           [0.2286, 0.17214, 0.34314],      
           [0.23263, 0.17571, 0.34675],      
           [0.2367, 0.17931, 0.35037],      
           [0.24074, 0.18289, 0.35398],      
           [0.24481, 0.1865, 0.35762],      
           [0.24893, 0.1901, 0.36124],      
           [0.25303, 0.19373, 0.36487],      
           [0.25715, 0.19734, 0.36852],      
           [0.26128, 0.20094, 0.37216],      
           [0.26543, 0.20461, 0.37581],      
           [0.2696, 0.20823, 0.37946],      
           [0.27378, 0.21188, 0.38312],      
           [0.27798, 0.2155, 0.38677],      
           [0.2822, 0.21915, 0.39043],      
           [0.28642, 0.22281, 0.3941],      
           [0.29069, 0.22646, 0.39777],      
           [0.29496, 0.23008, 0.40143],      
           [0.29928, 0.23373, 0.40509],      
           [0.30359, 0.23742, 0.40876],      
           [0.30794, 0.24104, 0.41244],      
           [0.31231, 0.24467, 0.41609],      
           [0.31673, 0.24835, 0.41976],      
           [0.32115, 0.25198, 0.4234],      
           [0.3256, 0.25561, 0.42707],      
           [0.3301, 0.25925, 0.43071],      
           [0.33462, 0.26286, 0.43435],      
           [0.33916, 0.26647, 0.43799],      
           [0.34371, 0.27008, 0.44162],      
           [0.34832, 0.27367, 0.44523],      
           [0.35296, 0.27725, 0.44884],      
           [0.35764, 0.28079, 0.45243],      
           [0.36233, 0.28434, 0.45599],      
           [0.36706, 0.28787, 0.45956],      
           [0.37182, 0.29139, 0.46309],      
           [0.37663, 0.29486, 0.46662],      
           [0.38146, 0.29832, 0.47012],      
           [0.38631, 0.30175, 0.47358],      
           [0.39123, 0.30517, 0.47703],      
           [0.39615, 0.30855, 0.48045],      
           [0.40112, 0.31187, 0.48384],      
           [0.40611, 0.31519, 0.4872],      
           [0.41112, 0.31845, 0.49052],      
           [0.41617, 0.32167, 0.4938],      
           [0.42124, 0.32485, 0.49704],      
           [0.42634, 0.32799, 0.50023],      
           [0.43147, 0.33107, 0.50338],      
           [0.43661, 0.33412, 0.50649],      
           [0.44178, 0.3371, 0.50955],      
           [0.44695, 0.34002, 0.51254],      
           [0.45215, 0.34289, 0.51548],      
           [0.45735, 0.34567, 0.51838],      
           [0.46256, 0.34842, 0.5212],      
           [0.46779, 0.35109, 0.52396],      
           [0.47301, 0.35368, 0.52667],      
           [0.47824, 0.35622, 0.5293],      
           [0.48346, 0.35866, 0.53186],      
           [0.48868, 0.36105, 0.53435],      
           [0.49389, 0.36336, 0.53678],      
           [0.49909, 0.36559, 0.53912],      
           [0.50428, 0.36773, 0.54138],      
           [0.50944, 0.36981, 0.54359],      
           [0.5146, 0.37179, 0.54572],      
           [0.51971, 0.37371, 0.54776],      
           [0.52482, 0.37553, 0.54973],      
           [0.52989, 0.37729, 0.55162],      
           [0.53494, 0.37895, 0.55343],      
           [0.53995, 0.38054, 0.55517],      
           [0.54493, 0.38204, 0.55684],      
           [0.54988, 0.38348, 0.55842],      
           [0.55479, 0.38482, 0.55995],      
           [0.55967, 0.38609, 0.56139],      
           [0.5645, 0.38729, 0.56277],      
           [0.56929, 0.38842, 0.56407],      
           [0.57405, 0.38948, 0.56529],      
           [0.57878, 0.39046, 0.56647],      
           [0.58346, 0.39139, 0.56758],      
           [0.5881, 0.39224, 0.56862],      
           [0.59272, 0.39303, 0.56961],      
           [0.59728, 0.39377, 0.57054],      
           [0.60181, 0.39446, 0.57142],      
           [0.60631, 0.39509, 0.57225],      
           [0.61079, 0.39568, 0.57304],      
           [0.61522, 0.39621, 0.57377],      
           [0.61963, 0.3967, 0.57446],      
           [0.62402, 0.39717, 0.57513],      
           [0.62837, 0.39761, 0.57577],      
           [0.63271, 0.39801, 0.57637],      
           [0.63703, 0.39839, 0.57694],      
           [0.64132, 0.39875, 0.57749],      
           [0.64562, 0.39909, 0.57803],      
           [0.64991, 0.39943, 0.57856],      
           [0.65419, 0.39978, 0.57909],      
           [0.65846, 0.40013, 0.57961],      
           [0.66275, 0.4005, 0.58013],      
           [0.66704, 0.40088, 0.58066],      
           [0.67134, 0.40128, 0.58121],      
           [0.67566, 0.40171, 0.58178],      
           [0.67999, 0.40218, 0.58238],      
           [0.68435, 0.40272, 0.58301],      
           [0.68875, 0.40332, 0.58369],      
           [0.69317, 0.40397, 0.58441],      
           [0.69762, 0.4047, 0.58519],      
           [0.70211, 0.40553, 0.58603],      
           [0.70665, 0.40645, 0.58693],      
           [0.71122, 0.40747, 0.58792],      
           [0.71583, 0.40861, 0.58898],      
           [0.72047, 0.40989, 0.59014],      
           [0.72516, 0.41129, 0.59141],      
           [0.72988, 0.41285, 0.59277],      
           [0.73462, 0.41455, 0.59423],      
           [0.73939, 0.41642, 0.59581],      
           [0.74417, 0.41844, 0.59751],      
           [0.74895, 0.42065, 0.59933],      
           [0.75373, 0.42302, 0.60126],      
           [0.75848, 0.42558, 0.60332],      
           [0.7632, 0.4283, 0.60549],      
           [0.76786, 0.4312, 0.60779],      
           [0.77246, 0.43425, 0.61018],      
           [0.77698, 0.43747, 0.61269],      
           [0.78138, 0.44082, 0.6153],      
           [0.78567, 0.44434, 0.61799],      
           [0.78982, 0.44795, 0.62078],      
           [0.79382, 0.4517, 0.62362],      
           [0.79765, 0.45553, 0.62652],      
           [0.8013, 0.45945, 0.62948],      
           [0.80476, 0.46342, 0.63248],      
           [0.80802, 0.46745, 0.6355],      
           [0.81107, 0.47152, 0.63854],      
           [0.81391, 0.47561, 0.64158],      
           [0.81654, 0.4797, 0.64462],      
           [0.81895, 0.48377, 0.64766],      
           [0.82115, 0.48786, 0.65067],      
           [0.82315, 0.4919, 0.65366],      
           [0.82494, 0.4959, 0.65662],      
           [0.82655, 0.49987, 0.65954],      
           [0.82796, 0.5038, 0.66243],      
           [0.8292, 0.50768, 0.66527],      
           [0.83027, 0.5115, 0.66808],      
           [0.83119, 0.51528, 0.67085],      
           [0.83196, 0.51901, 0.67357],      
           [0.8326, 0.52267, 0.67625],      
           [0.83311, 0.5263, 0.67889],      
           [0.83351, 0.52987, 0.68149],      
           [0.83381, 0.53339, 0.68406],      
           [0.83402, 0.53689, 0.6866],      
           [0.83415, 0.54032, 0.68911],      
           [0.8342, 0.54373, 0.69158],      
           [0.83418, 0.54711, 0.69403],      
           [0.83411, 0.55045, 0.69646],      
           [0.83399, 0.55377, 0.69886],      
           [0.83382, 0.55707, 0.70125],      
           [0.83362, 0.56035, 0.70362],      
           [0.83339, 0.56361, 0.70598],      
           [0.83314, 0.56685, 0.70832],      
           [0.83287, 0.57008, 0.71065],      
           [0.83258, 0.57331, 0.71297],      
           [0.83229, 0.57653, 0.7153],      
           [0.83199, 0.57975, 0.71761],      
           [0.83169, 0.58295, 0.71992],      
           [0.83139, 0.58617, 0.72222],      
           [0.83109, 0.58938, 0.72453],      
           [0.83081, 0.59261, 0.72684],      
           [0.83053, 0.59583, 0.72915],      
           [0.83027, 0.59907, 0.73146],      
           [0.83003, 0.6023, 0.73378],      
           [0.82981, 0.60555, 0.7361],      
           [0.8296, 0.60882, 0.73843],      
           [0.82942, 0.61209, 0.74076],      
           [0.82927, 0.61537, 0.74311],      
           [0.82914, 0.61868, 0.74545],      
           [0.82904, 0.62198, 0.74781],      
           [0.82896, 0.62531, 0.75017],      
           [0.82892, 0.62865, 0.75254],      
           [0.82891, 0.63201, 0.75493],      
           [0.82893, 0.63538, 0.75732],      
           [0.82898, 0.63877, 0.75971],      
           [0.82907, 0.64218, 0.76212],      
           [0.82919, 0.6456, 0.76455],      
           [0.82935, 0.64904, 0.76697],      
           [0.82954, 0.6525, 0.76941],      
           [0.82977, 0.65598, 0.77186],      
           [0.83003, 0.65947, 0.77432],      
           [0.83034, 0.66298, 0.77679],      
           [0.83068, 0.6665, 0.77927],      
           [0.83106, 0.67005, 0.78176],      
           [0.83147, 0.67361, 0.78426],      
           [0.83193, 0.6772, 0.78677],      
           [0.83241, 0.68078, 0.78929],      
           [0.83294, 0.6844, 0.79181],      
           [0.83351, 0.68803, 0.79435],      
           [0.83411, 0.69168, 0.79689],      
           [0.83474, 0.69534, 0.79945],      
           [0.83542, 0.69901, 0.80201],      
           [0.83613, 0.70271, 0.80459],      
           [0.83687, 0.70642, 0.80717],      
           [0.83765, 0.71014, 0.80975],      
           [0.83846, 0.71388, 0.81235],      
           [0.83931, 0.71764, 0.81495],      
           [0.84019, 0.7214, 0.81757],      
           [0.8411, 0.72519, 0.82018],      
           [0.84205, 0.72897, 0.82282],      
           [0.84302, 0.73278, 0.82545],      
           [0.84402, 0.7366, 0.82809],      
           [0.84505, 0.74043, 0.83074],      
           [0.84611, 0.74427, 0.83339],      
           [0.8472, 0.74813, 0.83605],      
           [0.84831, 0.75199, 0.83871],      
           [0.84946, 0.75587, 0.84139],      
           [0.85062, 0.75975, 0.84406],      
           [0.85181, 0.76365, 0.84674],      
           [0.85302, 0.76755, 0.84943],      
           [0.85425, 0.77147, 0.85212],      
           [0.85551, 0.77539, 0.85482],      
           [0.85678, 0.77932, 0.85752],      
           [0.85807, 0.78327, 0.86023],      
           [0.85939, 0.78722, 0.86294],      
           [0.86072, 0.79117, 0.86565],      
           [0.86207, 0.79514, 0.86837],      
           [0.86343, 0.79911, 0.87109],      
           [0.8648, 0.80309, 0.87381],      
           [0.8662, 0.80708, 0.87654],      
           [0.8676, 0.81107, 0.87927],      
           [0.86903, 0.81506, 0.88201],      
           [0.87045, 0.81906, 0.88475],      
           [0.8719, 0.82308, 0.88749],      
           [0.87334, 0.8271, 0.89023],      
           [0.87481, 0.83112, 0.89298],      
           [0.87628, 0.83514, 0.89573],      
           [0.87776, 0.83917, 0.89848],      
           [0.87924, 0.84321, 0.90124],      
           [0.88073, 0.84725, 0.904],      
           [0.88223, 0.85129, 0.90676],      
           [0.88374, 0.85535, 0.90952],      
           [0.88524, 0.8594, 0.91229],      
           [0.88676, 0.86346, 0.91505],      
           [0.88827, 0.86752, 0.91783],      
           [0.88979, 0.87158, 0.92059],      
           [0.89132, 0.87565, 0.92337],      
           [0.89284, 0.87972, 0.92614],      
           [0.89437, 0.8838, 0.92892],      
           [0.89589, 0.88787, 0.9317],      
           [0.89742, 0.89195, 0.93448],      
           [0.89895, 0.89604, 0.93727],      
           [0.90047, 0.90012, 0.94005]]      
      
acton_map = LinearSegmentedColormap.from_list('acton', cm_data)      
# For use of "viscm view"      
test_cm = acton_map      
      
if __name__ == "__main__":      
    import matplotlib.pyplot as plt      
    import numpy as np      
      
    try:      
        from viscm import viscm      
        viscm(acton_map)      
    except ImportError:      
        print("viscm not found, falling back on simple display")      
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',      
                   cmap=acton_map)      
    plt.show()      
