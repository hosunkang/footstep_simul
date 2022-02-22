import rospy
import time, sys

from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2
    
class footstep:
    def __init__(self):
        rospy.init_node('footstep', anonymous=True)
        self.pcCallback(rospy.wait_for_message('/l515/depth/pointcloud', PointCloud2))

    def pcCallback(self, pc2data):
        temp = pc2.read_points(pc2data, skip_nans=True, field_names=("x", "y", "z"))
        pts = [p for p in temp]
        rospy.loginfo("Number of Points : {}".format(len(pts)))

if __name__=='__main__':
    fs = footstep()
