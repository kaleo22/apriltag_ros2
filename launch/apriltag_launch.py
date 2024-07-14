from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from pathlib import Path
import yaml

def generate_launch_description():
    
    parameters = Path('/cali_ws/src/apriltag_ros2/cfg/tags_36h11.yaml')

    with open(parameters, 'r') as f:
        params = yaml.safe_load(f)['/**']['ros__parameters']
    print(params)
        
        
    apriltagNodeContainer = ComposableNodeContainer(
        name = 'apriltagNode',
        namespace = '',
        package = 'apriltag_ros',
        executable = 'apriltag_node',
        composable_node_descriptions=[
            ComposableNode(
                package='apriltag_ros',
                plugin='',
                name='apriltag',
                parameters=[params])
        ],
        output = 'screen'
    )
    
    
    
    
    
    
    return LaunchDescription(apriltagNodeContainer)