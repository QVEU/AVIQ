import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "Fix (4 plates)",
    "author": "Leo",
    "created": "2024-08-05T14:28:45.837Z",
    "lastModified": "2025-11-25T16:42:50.197Z",
    "protocolDesigner": "8.6.3",
    "source": "Protocol Designer",
}

requirements = {"robotType": "OT-2", "apiLevel": "2.26"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Labware:
    tip_rack_1 = protocol.load_labware(
        "opentrons_96_filtertiprack_200ul",
        location="1",
        namespace="opentrons",
        version=1,
    )
    reservoir_1 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="2",
        label="reservoir",
        namespace="opentrons",
        version=2,
    )
    well_plate_3 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="3",
        label="96",
        namespace="opentrons",
        version=4,
    )
    well_plate_1 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="6",
        label="96  2",
        namespace="opentrons",
        version=4,
    )
    tip_rack_2 = protocol.load_labware(
        "opentrons_96_filtertiprack_200ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons OT-2 96 Filter Tip Rack 200 µL (3)",
        namespace="opentrons",
        version=1,
    )
    well_plate_2 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="4",
        label="96 3",
        namespace="opentrons",
        version=4,
    )
    well_plate_4 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="5",
        label="96 3 (1)",
        namespace="opentrons",
        version=4,
    )

    # Load Pipettes:
    pipette_left = protocol.load_instrument("p300_multi_gen2", "left")

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "Methylcellulose",
        display_color="#b925ff",
    )
    liquid_2 = protocol.define_liquid(
        "PBS",
        display_color="#9dffd8",
    )
    liquid_3 = protocol.define_liquid(
        "MeOH",
        display_color="#50d5ff",
    )
    liquid_4 = protocol.define_liquid(
        "2Ab",
        display_color="#ff9900",
    )
    liquid_5 = protocol.define_liquid(
        "1*AB",
        display_color="#ff80f5",
    )
    liquid_6 = protocol.define_liquid(
        "MILK",
        display_color="#c2af4eff",
    )
    liquid_7 = protocol.define_liquid(
        "TB",
        display_color="#087aa1ff",
    )

    # Load Liquids:
    well_plate_3.load_liquid(
        wells=[
            "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
            "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
            "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
            "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
            "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
            "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
            "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
            "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8",
            "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9",
            "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10",
            "A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11",
            "A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12"
        ],
        liquid=liquid_1,
        volume=100,
    )
    reservoir_1.load_liquid(
        wells=["A1", "A2", "A3", "A4"],
        liquid=liquid_3,
        volume=10000,
    )
    well_plate_1.load_liquid(
        wells=[
            "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
            "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
            "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
            "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
            "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
            "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
            "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
            "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8",
            "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9",
            "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10",
            "A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11",
            "A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12"
        ],
        liquid=liquid_1,
        volume=100,
    )
    well_plate_2.load_liquid(
        wells=[
            "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
            "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
            "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
            "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
            "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
            "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
            "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
            "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8",
            "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9",
            "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10",
            "A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11",
            "A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12"
        ],
        liquid=liquid_1,
        volume=100,
    )
    well_plate_4.load_liquid(
        wells=[
            "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
            "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",
            "A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",
            "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",
            "A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",
            "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",
            "A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",
            "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8",
            "A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9",
            "A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10",
            "A11", "B11", "C11", "D11", "E11", "F11", "G11", "H11",
            "A12", "B12", "C12", "D12", "E12", "F12", "G12", "H12"
        ],
        liquid=liquid_1,
        volume=100,
    )

    # PROTOCOL STEPS

    # Step 1: r methyl p1 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_3["A12"], well_plate_3["A11"], well_plate_3["A10"], well_plate_3["A9"], well_plate_3["A8"], well_plate_3["A7"]],
        dest=[reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_1",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 2, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 2: r methyl p1 (6-1)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_3["A6"], well_plate_3["A5"], well_plate_3["A4"], well_plate_3["A3"], well_plate_3["A2"], well_plate_3["A1"]],
        dest=[reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_2",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 2, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 3: r methyl p2 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        dest=[reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_3",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 2, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 4: r methyl p2 (6-1)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        dest=[reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_4",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 2, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 5: A MeOH P1 (12-7)
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_1["A1"]],
        dest=[well_plate_3["A12"], well_plate_3["A11"], well_plate_3["A10"], well_plate_3["A9"], well_plate_3["A8"], well_plate_3["A7"], well_plate_3["A6"], well_plate_3["A5"], well_plate_3["A4"], well_plate_3["A3"], well_plate_3["A2"], well_plate_3["A1"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_5",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 11},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 11},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 0)],
                },
            }}},
        ),
    )

    # Step 6: A MeOH P2 (12-7)
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_1["A2"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"], well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_6",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 11},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 11},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 0)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 7: r methyl p1 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"]],
        dest=[reservoir_1["A8"], reservoir_1["A8"], reservoir_1["A8"], reservoir_1["A8"], reservoir_1["A8"], reservoir_1["A8"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_7",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 2, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 8: r methyl p1 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        dest=[reservoir_1["A7"], reservoir_1["A7"], reservoir_1["A7"], reservoir_1["A7"], reservoir_1["A7"], reservoir_1["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_8",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 2, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 9: r methyl p1 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_4["A12"], well_plate_4["A11"], well_plate_4["A10"], well_plate_4["A9"], well_plate_4["A8"], well_plate_4["A7"]],
        dest=[reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_9",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 2, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )

    # Step 10: r methyl p1 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_4["A6"], well_plate_4["A5"], well_plate_4["A4"], well_plate_4["A3"], well_plate_4["A2"], well_plate_4["A1"]],
        dest=[reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_10",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 2, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 11: A MeOH P1 (12-7)
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_1["A3"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"], well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_11",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 0)],
                },
            }}},
        ),
    )

    # Step 12: A MeOH P1 (12-7)
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_1["A4"]],
        dest=[well_plate_4["A12"], well_plate_4["A11"], well_plate_4["A10"], well_plate_4["A9"], well_plate_4["A8"], well_plate_4["A7"], well_plate_4["A6"], well_plate_4["A5"], well_plate_4["A4"], well_plate_4["A3"], well_plate_4["A2"], well_plate_4["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_12",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
                "multi_dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 45)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 0)],
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.6.0","data":{"pipetteTiprackAssignments":{"806347f5-d454-4feb-9ba3-2fe5d0376a65":["opentrons/opentrons_96_filtertiprack_200ul/1"]},"dismissedWarnings":{"form":["BELOW_MIN_DISPOSAL_VOLUME"],"timeline":["ASPIRATE_MORE_THAN_WELL_CONTENTS","ASPIRATE_FROM_PRISTINE_WELL"]},"ingredients":{"0":{"displayName":"Methylcellulose","description":null,"displayColor":"#b925ff","liquidGroupId":"0","liquidClass":null},"1":{"displayName":"PBS","description":null,"displayColor":"#9dffd8","liquidGroupId":"1","liquidClass":null},"2":{"displayName":"MeOH","description":null,"displayColor":"#50d5ff","liquidGroupId":"2","liquidClass":null},"3":{"displayName":"2Ab","description":null,"displayColor":"#ff9900","liquidGroupId":"3","liquidClass":null},"4":{"displayName":"1*AB","description":null,"displayColor":"#ff80f5","liquidGroupId":"4","liquidClass":null},"5":{"displayName":"MILK","description":null,"displayColor":"#c2af4eff","liquidGroupId":"5","liquidClass":null},"6":{"displayName":"TB","description":null,"displayColor":"#087aa1ff","liquidGroupId":"6","liquidClass":null}},"ingredLocations":{"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4":{"A1":{"0":{"volume":100}},"B1":{"0":{"volume":100}},"C1":{"0":{"volume":100}},"D1":{"0":{"volume":100}},"E1":{"0":{"volume":100}},"F1":{"0":{"volume":100}},"G1":{"0":{"volume":100}},"H1":{"0":{"volume":100}},"A2":{"0":{"volume":100}},"B2":{"0":{"volume":100}},"C2":{"0":{"volume":100}},"D2":{"0":{"volume":100}},"E2":{"0":{"volume":100}},"F2":{"0":{"volume":100}},"G2":{"0":{"volume":100}},"H2":{"0":{"volume":100}},"A3":{"0":{"volume":100}},"B3":{"0":{"volume":100}},"C3":{"0":{"volume":100}},"D3":{"0":{"volume":100}},"E3":{"0":{"volume":100}},"F3":{"0":{"volume":100}},"G3":{"0":{"volume":100}},"H3":{"0":{"volume":100}},"A4":{"0":{"volume":100}},"B4":{"0":{"volume":100}},"C4":{"0":{"volume":100}},"D4":{"0":{"volume":100}},"E4":{"0":{"volume":100}},"F4":{"0":{"volume":100}},"G4":{"0":{"volume":100}},"H4":{"0":{"volume":100}},"A5":{"0":{"volume":100}},"B5":{"0":{"volume":100}},"C5":{"0":{"volume":100}},"D5":{"0":{"volume":100}},"E5":{"0":{"volume":100}},"F5":{"0":{"volume":100}},"G5":{"0":{"volume":100}},"H5":{"0":{"volume":100}},"A6":{"0":{"volume":100}},"B6":{"0":{"volume":100}},"C6":{"0":{"volume":100}},"D6":{"0":{"volume":100}},"E6":{"0":{"volume":100}},"F6":{"0":{"volume":100}},"G6":{"0":{"volume":100}},"H6":{"0":{"volume":100}},"A7":{"0":{"volume":100}},"B7":{"0":{"volume":100}},"C7":{"0":{"volume":100}},"D7":{"0":{"volume":100}},"E7":{"0":{"volume":100}},"F7":{"0":{"volume":100}},"G7":{"0":{"volume":100}},"H7":{"0":{"volume":100}},"A8":{"0":{"volume":100}},"B8":{"0":{"volume":100}},"C8":{"0":{"volume":100}},"D8":{"0":{"volume":100}},"E8":{"0":{"volume":100}},"F8":{"0":{"volume":100}},"G8":{"0":{"volume":100}},"H8":{"0":{"volume":100}},"A9":{"0":{"volume":100}},"B9":{"0":{"volume":100}},"C9":{"0":{"volume":100}},"D9":{"0":{"volume":100}},"E9":{"0":{"volume":100}},"F9":{"0":{"volume":100}},"G9":{"0":{"volume":100}},"H9":{"0":{"volume":100}},"A10":{"0":{"volume":100}},"B10":{"0":{"volume":100}},"C10":{"0":{"volume":100}},"D10":{"0":{"volume":100}},"E10":{"0":{"volume":100}},"F10":{"0":{"volume":100}},"G10":{"0":{"volume":100}},"H10":{"0":{"volume":100}},"A11":{"0":{"volume":100}},"B11":{"0":{"volume":100}},"C11":{"0":{"volume":100}},"D11":{"0":{"volume":100}},"E11":{"0":{"volume":100}},"F11":{"0":{"volume":100}},"G11":{"0":{"volume":100}},"H11":{"0":{"volume":100}},"A12":{"0":{"volume":100}},"B12":{"0":{"volume":100}},"C12":{"0":{"volume":100}},"D12":{"0":{"volume":100}},"E12":{"0":{"volume":100}},"F12":{"0":{"volume":100}},"G12":{"0":{"volume":100}},"H12":{"0":{"volume":100}}},"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2":{"A1":{"2":{"volume":10000}},"A2":{"2":{"volume":10000}},"A3":{"2":{"volume":10000}},"A4":{"2":{"volume":10000}}},"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4":{"A1":{"0":{"volume":100}},"B1":{"0":{"volume":100}},"C1":{"0":{"volume":100}},"D1":{"0":{"volume":100}},"E1":{"0":{"volume":100}},"F1":{"0":{"volume":100}},"G1":{"0":{"volume":100}},"H1":{"0":{"volume":100}},"A2":{"0":{"volume":100}},"B2":{"0":{"volume":100}},"C2":{"0":{"volume":100}},"D2":{"0":{"volume":100}},"E2":{"0":{"volume":100}},"F2":{"0":{"volume":100}},"G2":{"0":{"volume":100}},"H2":{"0":{"volume":100}},"A3":{"0":{"volume":100}},"B3":{"0":{"volume":100}},"C3":{"0":{"volume":100}},"D3":{"0":{"volume":100}},"E3":{"0":{"volume":100}},"F3":{"0":{"volume":100}},"G3":{"0":{"volume":100}},"H3":{"0":{"volume":100}},"A4":{"0":{"volume":100}},"B4":{"0":{"volume":100}},"C4":{"0":{"volume":100}},"D4":{"0":{"volume":100}},"E4":{"0":{"volume":100}},"F4":{"0":{"volume":100}},"G4":{"0":{"volume":100}},"H4":{"0":{"volume":100}},"A5":{"0":{"volume":100}},"B5":{"0":{"volume":100}},"C5":{"0":{"volume":100}},"D5":{"0":{"volume":100}},"E5":{"0":{"volume":100}},"F5":{"0":{"volume":100}},"G5":{"0":{"volume":100}},"H5":{"0":{"volume":100}},"A6":{"0":{"volume":100}},"B6":{"0":{"volume":100}},"C6":{"0":{"volume":100}},"D6":{"0":{"volume":100}},"E6":{"0":{"volume":100}},"F6":{"0":{"volume":100}},"G6":{"0":{"volume":100}},"H6":{"0":{"volume":100}},"A7":{"0":{"volume":100}},"B7":{"0":{"volume":100}},"C7":{"0":{"volume":100}},"D7":{"0":{"volume":100}},"E7":{"0":{"volume":100}},"F7":{"0":{"volume":100}},"G7":{"0":{"volume":100}},"H7":{"0":{"volume":100}},"A8":{"0":{"volume":100}},"B8":{"0":{"volume":100}},"C8":{"0":{"volume":100}},"D8":{"0":{"volume":100}},"E8":{"0":{"volume":100}},"F8":{"0":{"volume":100}},"G8":{"0":{"volume":100}},"H8":{"0":{"volume":100}},"A9":{"0":{"volume":100}},"B9":{"0":{"volume":100}},"C9":{"0":{"volume":100}},"D9":{"0":{"volume":100}},"E9":{"0":{"volume":100}},"F9":{"0":{"volume":100}},"G9":{"0":{"volume":100}},"H9":{"0":{"volume":100}},"A10":{"0":{"volume":100}},"B10":{"0":{"volume":100}},"C10":{"0":{"volume":100}},"D10":{"0":{"volume":100}},"E10":{"0":{"volume":100}},"F10":{"0":{"volume":100}},"G10":{"0":{"volume":100}},"H10":{"0":{"volume":100}},"A11":{"0":{"volume":100}},"B11":{"0":{"volume":100}},"C11":{"0":{"volume":100}},"D11":{"0":{"volume":100}},"E11":{"0":{"volume":100}},"F11":{"0":{"volume":100}},"G11":{"0":{"volume":100}},"H11":{"0":{"volume":100}},"A12":{"0":{"volume":100}},"B12":{"0":{"volume":100}},"C12":{"0":{"volume":100}},"D12":{"0":{"volume":100}},"E12":{"0":{"volume":100}},"F12":{"0":{"volume":100}},"G12":{"0":{"volume":100}},"H12":{"0":{"volume":100}}},"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/4":{"A1":{"0":{"volume":100}},"B1":{"0":{"volume":100}},"C1":{"0":{"volume":100}},"D1":{"0":{"volume":100}},"E1":{"0":{"volume":100}},"F1":{"0":{"volume":100}},"G1":{"0":{"volume":100}},"H1":{"0":{"volume":100}},"A2":{"0":{"volume":100}},"B2":{"0":{"volume":100}},"C2":{"0":{"volume":100}},"D2":{"0":{"volume":100}},"E2":{"0":{"volume":100}},"F2":{"0":{"volume":100}},"G2":{"0":{"volume":100}},"H2":{"0":{"volume":100}},"A3":{"0":{"volume":100}},"B3":{"0":{"volume":100}},"C3":{"0":{"volume":100}},"D3":{"0":{"volume":100}},"E3":{"0":{"volume":100}},"F3":{"0":{"volume":100}},"G3":{"0":{"volume":100}},"H3":{"0":{"volume":100}},"A4":{"0":{"volume":100}},"B4":{"0":{"volume":100}},"C4":{"0":{"volume":100}},"D4":{"0":{"volume":100}},"E4":{"0":{"volume":100}},"F4":{"0":{"volume":100}},"G4":{"0":{"volume":100}},"H4":{"0":{"volume":100}},"A5":{"0":{"volume":100}},"B5":{"0":{"volume":100}},"C5":{"0":{"volume":100}},"D5":{"0":{"volume":100}},"E5":{"0":{"volume":100}},"F5":{"0":{"volume":100}},"G5":{"0":{"volume":100}},"H5":{"0":{"volume":100}},"A6":{"0":{"volume":100}},"B6":{"0":{"volume":100}},"C6":{"0":{"volume":100}},"D6":{"0":{"volume":100}},"E6":{"0":{"volume":100}},"F6":{"0":{"volume":100}},"G6":{"0":{"volume":100}},"H6":{"0":{"volume":100}},"A7":{"0":{"volume":100}},"B7":{"0":{"volume":100}},"C7":{"0":{"volume":100}},"D7":{"0":{"volume":100}},"E7":{"0":{"volume":100}},"F7":{"0":{"volume":100}},"G7":{"0":{"volume":100}},"H7":{"0":{"volume":100}},"A8":{"0":{"volume":100}},"B8":{"0":{"volume":100}},"C8":{"0":{"volume":100}},"D8":{"0":{"volume":100}},"E8":{"0":{"volume":100}},"F8":{"0":{"volume":100}},"G8":{"0":{"volume":100}},"H8":{"0":{"volume":100}},"A9":{"0":{"volume":100}},"B9":{"0":{"volume":100}},"C9":{"0":{"volume":100}},"D9":{"0":{"volume":100}},"E9":{"0":{"volume":100}},"F9":{"0":{"volume":100}},"G9":{"0":{"volume":100}},"H9":{"0":{"volume":100}},"A10":{"0":{"volume":100}},"B10":{"0":{"volume":100}},"C10":{"0":{"volume":100}},"D10":{"0":{"volume":100}},"E10":{"0":{"volume":100}},"F10":{"0":{"volume":100}},"G10":{"0":{"volume":100}},"H10":{"0":{"volume":100}},"A11":{"0":{"volume":100}},"B11":{"0":{"volume":100}},"C11":{"0":{"volume":100}},"D11":{"0":{"volume":100}},"E11":{"0":{"volume":100}},"F11":{"0":{"volume":100}},"G11":{"0":{"volume":100}},"H11":{"0":{"volume":100}},"A12":{"0":{"volume":100}},"B12":{"0":{"volume":100}},"C12":{"0":{"volume":100}},"D12":{"0":{"volume":100}},"E12":{"0":{"volume":100}},"F12":{"0":{"volume":100}},"G12":{"0":{"volume":100}},"H12":{"0":{"volume":100}}},"f63879d6-fbcc-4cfe-89e8-885c5eaa9689:opentrons/nest_96_wellplate_200ul_flat/4":{"A1":{"0":{"volume":100}},"B1":{"0":{"volume":100}},"C1":{"0":{"volume":100}},"D1":{"0":{"volume":100}},"E1":{"0":{"volume":100}},"F1":{"0":{"volume":100}},"G1":{"0":{"volume":100}},"H1":{"0":{"volume":100}},"A2":{"0":{"volume":100}},"B2":{"0":{"volume":100}},"C2":{"0":{"volume":100}},"D2":{"0":{"volume":100}},"E2":{"0":{"volume":100}},"F2":{"0":{"volume":100}},"G2":{"0":{"volume":100}},"H2":{"0":{"volume":100}},"A3":{"0":{"volume":100}},"B3":{"0":{"volume":100}},"C3":{"0":{"volume":100}},"D3":{"0":{"volume":100}},"E3":{"0":{"volume":100}},"F3":{"0":{"volume":100}},"G3":{"0":{"volume":100}},"H3":{"0":{"volume":100}},"A4":{"0":{"volume":100}},"B4":{"0":{"volume":100}},"C4":{"0":{"volume":100}},"D4":{"0":{"volume":100}},"E4":{"0":{"volume":100}},"F4":{"0":{"volume":100}},"G4":{"0":{"volume":100}},"H4":{"0":{"volume":100}},"A5":{"0":{"volume":100}},"B5":{"0":{"volume":100}},"C5":{"0":{"volume":100}},"D5":{"0":{"volume":100}},"E5":{"0":{"volume":100}},"F5":{"0":{"volume":100}},"G5":{"0":{"volume":100}},"H5":{"0":{"volume":100}},"A6":{"0":{"volume":100}},"B6":{"0":{"volume":100}},"C6":{"0":{"volume":100}},"D6":{"0":{"volume":100}},"E6":{"0":{"volume":100}},"F6":{"0":{"volume":100}},"G6":{"0":{"volume":100}},"H6":{"0":{"volume":100}},"A7":{"0":{"volume":100}},"B7":{"0":{"volume":100}},"C7":{"0":{"volume":100}},"D7":{"0":{"volume":100}},"E7":{"0":{"volume":100}},"F7":{"0":{"volume":100}},"G7":{"0":{"volume":100}},"H7":{"0":{"volume":100}},"A8":{"0":{"volume":100}},"B8":{"0":{"volume":100}},"C8":{"0":{"volume":100}},"D8":{"0":{"volume":100}},"E8":{"0":{"volume":100}},"F8":{"0":{"volume":100}},"G8":{"0":{"volume":100}},"H8":{"0":{"volume":100}},"A9":{"0":{"volume":100}},"B9":{"0":{"volume":100}},"C9":{"0":{"volume":100}},"D9":{"0":{"volume":100}},"E9":{"0":{"volume":100}},"F9":{"0":{"volume":100}},"G9":{"0":{"volume":100}},"H9":{"0":{"volume":100}},"A10":{"0":{"volume":100}},"B10":{"0":{"volume":100}},"C10":{"0":{"volume":100}},"D10":{"0":{"volume":100}},"E10":{"0":{"volume":100}},"F10":{"0":{"volume":100}},"G10":{"0":{"volume":100}},"H10":{"0":{"volume":100}},"A11":{"0":{"volume":100}},"B11":{"0":{"volume":100}},"C11":{"0":{"volume":100}},"D11":{"0":{"volume":100}},"E11":{"0":{"volume":100}},"F11":{"0":{"volume":100}},"G11":{"0":{"volume":100}},"H11":{"0":{"volume":100}},"A12":{"0":{"volume":100}},"B12":{"0":{"volume":100}},"C12":{"0":{"volume":100}},"D12":{"0":{"volume":100}},"E12":{"0":{"volume":100}},"F12":{"0":{"volume":100}},"G12":{"0":{"volume":100}},"H12":{"0":{"volume":100}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"labwareLocationUpdate":{"bb063119-315e-4ac6-b4c7-088a6e688445:opentrons/opentrons_96_filtertiprack_200ul/1":"1","b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2":"2","aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4":"3","72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4":"6","3f275f2a-19a4-4ba1-8219-afd1a3d38c3a:opentrons/opentrons_96_filtertiprack_200ul/1":"offDeck","90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/4":"4","f63879d6-fbcc-4cfe-89e8-885c5eaa9689:opentrons/nest_96_wellplate_200ul_flat/4":"5"},"moduleLocationUpdate":{},"pipetteLocationUpdate":{"806347f5-d454-4feb-9ba3-2fe5d0376a65":"left"},"trashBinLocationUpdate":{"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin":"cutout12"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{},"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__"},"4114ac39-5979-49b0-9ac6-3c3237af17b9":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":11,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"100","stepType":"moveLiquid","stepName":"A MeOH P1 (12-7)","stepDetails":"","id":"4114ac39-5979-49b0-9ac6-3c3237af17b9","dispense_touchTip_mmfromTop":null},"e2e4a843-01cf-49eb-b2cc-6e945056705b":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":11,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"100","stepType":"moveLiquid","stepName":"A MeOH P2 (12-7)","stepDetails":"","id":"e2e4a843-01cf-49eb-b2cc-6e945056705b","dispense_touchTip_mmfromTop":null},"5e4c16af-af1f-4e3e-b12d-f619b19e8bc0":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":45,"aspirate_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":2,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"r methyl p1 (12-7)","stepDetails":"","id":"5e4c16af-af1f-4e3e-b12d-f619b19e8bc0","dispense_touchTip_mmfromTop":null},"6acb9cc5-c885-4397-bf96-4804b92c665a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":45,"aspirate_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":2,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"r methyl p2 (12-7)","stepDetails":"","id":"6acb9cc5-c885-4397-bf96-4804b92c665a","dispense_touchTip_mmfromTop":null},"3b235aab-6b78-4b20-ac67-625ea21ea2d8":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":45,"aspirate_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":2,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"r methyl p2 (6-1)","stepDetails":"","id":"3b235aab-6b78-4b20-ac67-625ea21ea2d8","dispense_touchTip_mmfromTop":null},"12938828-4eb0-4d79-9d52-77a2d4d3bfbb":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":45,"aspirate_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":2,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"r methyl p1 (6-1)","stepDetails":"","id":"12938828-4eb0-4d79-9d52-77a2d4d3bfbb","dispense_touchTip_mmfromTop":null},"e98cff20-9750-4f35-8f41-afd22bec35cb":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":45,"aspirate_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":2,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"r methyl p1 (12-7)","stepDetails":"","id":"e98cff20-9750-4f35-8f41-afd22bec35cb","dispense_touchTip_mmfromTop":null},"52ffc5b1-ac8c-4d03-82fe-da090c29b2e3":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":45,"aspirate_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":2,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"r methyl p1 (12-7)","stepDetails":"","id":"52ffc5b1-ac8c-4d03-82fe-da090c29b2e3","dispense_touchTip_mmfromTop":null},"7d306e29-4ffe-4436-a8fd-55f485f1fdd3":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"100","stepType":"moveLiquid","stepName":"A MeOH P1 (12-7)","stepDetails":"","id":"7d306e29-4ffe-4436-a8fd-55f485f1fdd3","dispense_touchTip_mmfromTop":null},"703ea23c-0e51-4c43-a34e-6756ef0c6f0e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":45,"aspirate_labware":"f63879d6-fbcc-4cfe-89e8-885c5eaa9689:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":2,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"r methyl p1 (12-7)","stepDetails":"","id":"703ea23c-0e51-4c43-a34e-6756ef0c6f0e","dispense_touchTip_mmfromTop":null},"b491cef8-b548-47e8-b7f2-6e2d86867059":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":45,"aspirate_labware":"f63879d6-fbcc-4cfe-89e8-885c5eaa9689:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":2,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"r methyl p1 (12-7)","stepDetails":"","id":"b491cef8-b548-47e8-b7f2-6e2d86867059","dispense_touchTip_mmfromTop":null},"31077ece-b6c1-4263-a638-92fec04300e6":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"f63879d6-fbcc-4cfe-89e8-885c5eaa9689:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"100","stepType":"moveLiquid","stepName":"A MeOH P1 (12-7)","stepDetails":"","id":"31077ece-b6c1-4263-a638-92fec04300e6","dispense_touchTip_mmfromTop":null}},"orderedStepIds":["5e4c16af-af1f-4e3e-b12d-f619b19e8bc0","12938828-4eb0-4d79-9d52-77a2d4d3bfbb","6acb9cc5-c885-4397-bf96-4804b92c665a","3b235aab-6b78-4b20-ac67-625ea21ea2d8","4114ac39-5979-49b0-9ac6-3c3237af17b9","e2e4a843-01cf-49eb-b2cc-6e945056705b","e98cff20-9750-4f35-8f41-afd22bec35cb","52ffc5b1-ac8c-4d03-82fe-da090c29b2e3","703ea23c-0e51-4c43-a34e-6756ef0c6f0e","b491cef8-b548-47e8-b7f2-6e2d86867059","7d306e29-4ffe-4436-a8fd-55f485f1fdd3","31077ece-b6c1-4263-a638-92fec04300e6"],"pipettes":{"806347f5-d454-4feb-9ba3-2fe5d0376a65":{"pipetteName":"p300_multi_gen2"}},"modules":{},"labware":{"bb063119-315e-4ac6-b4c7-088a6e688445:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"},"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2":{"displayName":"reservoir","labwareDefURI":"opentrons/nest_12_reservoir_15ml/2"},"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4":{"displayName":"96","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/4"},"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4":{"displayName":"96  2","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/4"},"3f275f2a-19a4-4ba1-8219-afd1a3d38c3a:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL (3)","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"},"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/4":{"displayName":"96 3","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/4"},"f63879d6-fbcc-4cfe-89e8-885c5eaa9689:opentrons/nest_96_wellplate_200ul_flat/4":{"displayName":"96 3 (1)","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/4"}}}},"metadata":{"protocolName":"Fix (4 plates)","author":"Leo","description":"","created":1722868125837,"lastModified":1764088970197,"category":null,"subcategory":null,"tags":[],"source":"Protocol Designer"}}"""
