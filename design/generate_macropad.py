import sys
print(sys.path)
sys.path.append("src/klavgen")
print(sys.path)

from klavgen import *
from klavgen.classes import Key

import cadquery as cq

config = Config(
    case_config=CaseConfig(
        # side_fillet=4,
        # palm_rests_top_fillet=5,
        switch_type=SwitchType.MX,
        case_base_height=18
    ),
    mx_key_config=MXKeyConfig(case_tile_margin=7.5),
    # choc_key_config=ChocKeyConfig(case_tile_margin=7.6),
    # controller_config=ControllerConfig(case_tile_margin=5),
    # usbc_jack_config=USBCJackConfig(case_tile_margin=5)
)

keys : Key = generate_keys_from_kle_json("./keyboard-layout.json")

key: Key
for key in keys:
    print(key)

controller = Controller(x=47.5, y=20)

screw_holes = [  # Clockwise from top left
    ScrewHole(x=-11.4, y=11.0),
    ScrewHole(x=68.15, y=11.0),
    ScrewHole(x=28.575, y=-28.25),
    ScrewHole(x=28.575, y=-47.05),
    ScrewHole(x=-11.5, y=-87.2),
    ScrewHole(x=68.15, y=-87.2),
]

patches = [
    Patch(
        points=[
            (-15, 15),
            (60, 15),
            (60, -90),
            (-15, -90),
        ],
        height=config.case_config.case_base_height,
    )
]

cuts = [
    Cut(
        points=[(57.5, -15), (82, 7), (82, -15)],
        height=config.case_config.case_base_height,
    )
]

# case_extras = [
#     (
#         cq.Workplane("XY")
#         .workplane(offset=-config.case_config.case_base_height)
#         .center(69.75, -4)
#         .circle(5)
#         .extrude(config.case_config.case_base_height)
#     )
# ]

render_and_save_keyboard(keys=keys,
                         config=config,
                         controller=controller,
                         patches=patches,
                        #  cuts=cuts,
                        #  case_extras=case_extras,
                         screw_holes=screw_holes
                         )
