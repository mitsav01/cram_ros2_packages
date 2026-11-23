from giskardpy_ros.launch_helpers import giskard_launch_description


def generate_launch_description():
    return giskard_launch_description(
        executable="tiago_velocity",
        root_links=["base_footprint", "base_footprint", "map"],
        tip_links=[
            "arm_right_tool_link",
            "arm_left_tool_link",
            "base_footprint",
        ],
        rviz=True,
        map_world_tf=False,
    )
