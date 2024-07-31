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

    camnum = params.get('camera_number', int)
    containers = []
        
    for i in range(1, camnum):
        container_name = f'apriltagNodeContainer{i}'
        node_name = f'apriltag{i}'
        if i == 1:
            mapping=[
                ('image_rect', f'/peak_cam/image_raw'),  # Remap image_rect to peak_cam/image_raw
                ('camera_info', f'/peak_cam/camera_info'), # Remap camera_info to /peak_cam/camera_info
                ("/tf", f"/tf_{i}")
            ]  
        else:
            mapping=[
                ('image_rect', f'/peak_cam_{i}/image_raw_{i}'),  # Remap image_rect to peak_cam/image_raw
                ('camera_info', f'/peak_cam_{i}/camera_info'), # Remap camera_info to /peak_cam/camera_info
                ("/tf", f"/tf_{i}")
            ]  
        
        container = ComposableNodeContainer(
        name=container_name,
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='apriltag_ros',
                plugin='AprilTagNode',
                name=node_name,
                parameters=[params],
                remappings=mapping
                )
        ],
        output='screen'
        
        )
        containers.append(container)   
    
    
    
    
    
    
    return LaunchDescription(containers)