import launch
from launch_ros.actions import Node

def generate_launch_description():
    talker_node = Node(
        package='mypkg',
        executable='talker',
        name='talker_node',
        parameters=[{'talk_rate': 1.0}]
    )
    listener_node = Node(
        package='mypkg',
        executable='listener',
        name='listener_node',
        parameters=[{'message_prefix': 'Listen:'}]
    )
    return launch.LaunchDescription([
        talker_node,
        listener_node
    ])

