from giskardpy_ros.launch_helpers import giskard_launch_description


def generate_launch_description():
    return giskard_launch_description(
        executable="tiago_standalone",
        xacro_package="iai_tiago_description",
        xacro_file="urdf/tiago_from_our_robot.urdf",
        root_links=["map", "map", "torso_lift_link"],
        tip_links=["arm_left_tool_link", "arm_right_tool_link", "head_2_link"],
        rviz=True,
        map_world_tf=True,
<<<<<<< HEAD
    )
=======
    )
>>>>>>> 5a602f7 (Update launch files for tiago_standalone and tiago_velocity executables)
