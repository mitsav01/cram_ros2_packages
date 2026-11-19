from giskardpy_ros.launch_helpers import giskard_launch_description


def generate_launch_description():
    return giskard_launch_description(
        executable="tiago_velocity",
        xacro_package="iai_tiago_description",
        xacro_file="urdf/tiago_from_our_robot.urdf",
        root_links=["map", "map"],
        tip_links=[
            "arm_right_tool_link",  
            "arm_left_tool_link",       
        ],
        rviz=True,
    )