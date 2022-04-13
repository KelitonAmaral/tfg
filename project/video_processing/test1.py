import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# from project.video_processing.lift import Lift
# from project.video_processing.analysis import Analysis

w = 4
h = 3
d = 70
plt.figure(figsize=(w, h), dpi=d)
fig, ax = plt.subplots()
ax.axis([0, 1, 0, 1])

string_path_data = [
(mpath.Path.MOVETO,(0.69150175, 0.30849825)),
(mpath.Path.CURVE3,(0.69230769, 0.30769231)),
(mpath.Path.CURVE3,(0.69356725, 0.30643275)),
(mpath.Path.CURVE3,(0.69483568, 0.30516432)),
(mpath.Path.CURVE3,(0.69575472, 0.30424528)),
(mpath.Path.CURVE3,(0.69503546, 0.30496454)),
(mpath.Path.CURVE3,(0.69267139, 0.30732861)),
(mpath.Path.CURVE3, (0.68831169, 0.31168831)),
(mpath.Path.CURVE3,(0.68309859, 0.31690141)),
(mpath.Path.CURVE3,(0.67674419, 0.32325581)),
(mpath.Path.CURVE3,(0.66781609, 0.33218391)),
(mpath.Path.CURVE3,(0.65873016, 0.34126984)),
(mpath.Path.CURVE3,(0.6506159, 0.3493841)),
(mpath.Path.CURVE3,(0.64238411, 0.35761589)),
(mpath.Path.CURVE3,(0.6343852, 0.3656148)),
(mpath.Path.CURVE3,(0.62700965, 0.37299035)),
(mpath.Path.CURVE3,(0.62010582, 0.37989418))]




# string_path_data = [
#     (mpath.Path.MOVETO, (0, -3)),
#     (mpath.Path.CURVE3, (1, -4)),
#     (mpath.Path.CURVE3, (-1, -5)),
#     (mpath.Path.CURVE3, (0, -6))]


# string_path_data = [
#     (mpath.Path.MOVETO, (0, -3)),
#     (mpath.Path.LINETO, (1, -4)),
#     (mpath.Path.LINETO, (-1, -5)),
#     (mpath.Path.LINETO, (0, -6))]


codes, verts = zip(*string_path_data)
print(verts)
string_path = mpath.Path(verts, codes)
# string_path = mpath.Path(verts, codes=None)
patch = mpatches.PathPatch(string_path, facecolor="none", lw=2)

ax.add_patch(patch)
# plt.savefig("out.png")
plt.show()