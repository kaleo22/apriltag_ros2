from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from pathlib import Path
import yaml

def generate_launch_description():
    
    parameters = Path('/cali_ws/src/apriltag_ros2/cfg/tags_36h11.yaml')

    with open(parameters, 'r') as f:
        params = yaml.safe_load(f)['apriltag']['ros__parameters']
    print(params)
        
        
    apriltagNodeContainer = ComposableNodeContainer(
        name='apriltagNode',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='apriltag_ros',
                plugin='apriltag_ros::AprilTagNode',
                name='apriltag',
                parameters=[params],
                remappings=[
                    ('image_rect', '/peak_cam/image_raw'),  # Remap image_rect to peak_cam/image_raw
                    ('camera_info', '/peak_cam/camera_info')  # Remap camera_info to /peak_cam/camera_info
                ])
        ],
        output='screen'
    )
    
    
    
    
    
    
    return LaunchDescription([apriltagNodeContainer])