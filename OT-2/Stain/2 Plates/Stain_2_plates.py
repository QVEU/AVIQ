import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "Stain (2 plates)",
    "author": "Leonardo Giordano",
    "created": "2024-08-05T14:28:45.837Z",
    "lastModified": "2025-11-25T17:27:33.754Z",
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
    well_plate_1 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="5",
        label="96",
        namespace="opentrons",
        version=4,
    )
    well_plate_2 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="6",
        label="96  2",
        namespace="opentrons",
        version=4,
    )
    reservoir_2 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="3",
        label="reservoir 2",
        namespace="opentrons",
        version=2,
    )
    tip_rack_2 = protocol.load_labware(
        "opentrons_96_filtertiprack_200ul",
        location="4",
        label="Opentrons OT-2 96 Filter Tip Rack 200 µL (1)",
        namespace="opentrons",
        version=1,
    )
    tip_rack_3 = protocol.load_labware(
        "opentrons_96_filtertiprack_200ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons OT-2 96 Filter Tip Rack 200 µL (3)",
        namespace="opentrons",
        version=1,
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
    reservoir_1.load_liquid(
        wells=["A1", "A2"],
        liquid=liquid_3,
        volume=10000,
    )
    reservoir_1.load_liquid(
        wells=["A3", "A4", "A5", "A6"],
        liquid=liquid_6,
        volume=10000,
    )
    reservoir_1.load_liquid(
        wells=["A7", "A8"],
        liquid=liquid_5,
        volume=10000,
    )
    reservoir_1.load_liquid(
        wells=["A9", "A10", "A11", "A12"],
        liquid=liquid_2,
        volume=10000,
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
    reservoir_2.load_liquid(
        wells=["A1", "A2", "A3", "A4"],
        liquid=liquid_2,
        volume=10000,
    )
    reservoir_2.load_liquid(
        wells=["A5", "A6"],
        liquid=liquid_4,
        volume=10000,
    )
    reservoir_2.load_liquid(
        wells=["A7"],
        liquid=liquid_7,
        volume=10000,
    )

    # PROTOCOL STEPS

    # Step 1: A milk p1 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_1",
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
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

    # Step 2: A milk p1 (6-1)
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"]],
        dest=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_2",
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
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

    # Step 3: A milk p2 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_3",
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
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

    # Step 4: A milk p2 (6-1)
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"]],
        dest=[well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_4",
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
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

    # Step 5: milk 10 min
    protocol.delay(seconds=360)

    # Step 6: r pbs p2 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"]],
        dest=[reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_6",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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
                    "flow_rate_by_volume": [(0, 94)],
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

    # Step 7: r pbs p2 (6-1)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        dest=[reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_7",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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
                    "flow_rate_by_volume": [(0, 94)],
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

    # Step 8: r pbs p1 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        dest=[reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_8",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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
                    "flow_rate_by_volume": [(0, 94)],
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

    # Step 9: r pbs p1 (6-1)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        dest=[reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_9",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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
                    "flow_rate_by_volume": [(0, 94)],
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

    # Step 10: Add 1
    protocol.delay(seconds=1)

    # Step 11: a 1*ab p1 (12-7)
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_1["A7"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"], well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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

    # Step 12: a 1*ab p2 (12-7)
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_1["A8"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"], well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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

    # Step 13: pause 2h
    protocol.delay(seconds=7200, msg="2 H")

    # Step 14: pause
    protocol.pause("REMOVE 1AB")

    # Step 15: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_15",
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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

    # Step 16: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"]],
        dest=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_16",
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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

    # Step 17: A PBS 2
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_17",
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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

    # Step 18: A PBS 2
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"]],
        dest=[well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_18",
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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

    # Step 19: R pbs
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        dest=[reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_19",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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
                    "flow_rate_by_volume": [(0, 94)],
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

    # Step 20: R pbs
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        dest=[reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_20",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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
                    "flow_rate_by_volume": [(0, 94)],
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

    # Step 21: R pbs
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"]],
        dest=[reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_21",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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
                    "flow_rate_by_volume": [(0, 94)],
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

    # Step 22: R pbs
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        dest=[reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_22",
            properties={"p300_multi_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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
                    "flow_rate_by_volume": [(0, 94)],
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

    # Step 23: pause
    protocol.delay(seconds=1)

    # Step 24: A 2AB
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_2["A5"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"], well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_24",
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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

    # Step 25: A 2AB
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_2["A6"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"], well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_25",
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
                    "flow_rate_by_volume": [(0, 50)],
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
                    "flow_rate_by_volume": [(0, 50)],
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

    # Step 26: pause
    protocol.delay(seconds=3600)

    # Step 27: pause
    protocol.pause("REMOVE 2AB")

    # Step 28: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_2["A1"], reservoir_2["A1"], reservoir_2["A1"], reservoir_2["A1"], reservoir_2["A1"], reservoir_2["A1"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_28",
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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

    # Step 29: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_2["A2"], reservoir_2["A2"], reservoir_2["A2"], reservoir_2["A2"], reservoir_2["A2"], reservoir_2["A2"]],
        dest=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_29",
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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

    # Step 30: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_2["A3"], reservoir_2["A3"], reservoir_2["A3"], reservoir_2["A3"], reservoir_2["A3"], reservoir_2["A3"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_30",
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
                    "flow_rate_by_volume": [(0, 50)],
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

    # Step 31: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_2["A4"], reservoir_2["A4"], reservoir_2["A4"], reservoir_2["A4"], reservoir_2["A4"], reservoir_2["A4"]],
        dest=[well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_31",
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
                    "flow_rate_by_volume": [(0, 50)],
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

    # Step 32: pause
    protocol.pause("REMOVE PBS, tap plate and add TB to reservoir")

    # Step 33: A TB
    pipette_left.distribute_with_liquid_class(
        volume=40,
        source=[reservoir_2["A7"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"], well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_33",
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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
                        "offset": {"x": 0, "y": 0, "z": 8},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 50)],
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

    # Step 34: A TB
    pipette_left.distribute_with_liquid_class(
        volume=40,
        source=[reservoir_2["A7"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"], well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_34",
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
                    "flow_rate_by_volume": [(0, 50)],
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
                    "flow_rate_by_volume": [(0, 50)],
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

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.6.0","data":{"pipetteTiprackAssignments":{"806347f5-d454-4feb-9ba3-2fe5d0376a65":["opentrons/opentrons_96_filtertiprack_200ul/1"]},"dismissedWarnings":{"form":["BELOW_MIN_DISPOSAL_VOLUME"],"timeline":["ASPIRATE_MORE_THAN_WELL_CONTENTS","ASPIRATE_FROM_PRISTINE_WELL"]},"ingredients":{"0":{"displayName":"Methylcellulose","description":null,"displayColor":"#b925ff","liquidGroupId":"0","liquidClass":null},"1":{"displayName":"PBS","description":null,"displayColor":"#9dffd8","liquidGroupId":"1","liquidClass":null},"2":{"displayName":"MeOH","description":null,"displayColor":"#50d5ff","liquidGroupId":"2","liquidClass":null},"3":{"displayName":"2Ab","description":null,"displayColor":"#ff9900","liquidGroupId":"3","liquidClass":null},"4":{"displayName":"1*AB","description":null,"displayColor":"#ff80f5","liquidGroupId":"4","liquidClass":null},"5":{"displayName":"MILK","description":null,"displayColor":"#c2af4eff","liquidGroupId":"5","liquidClass":null},"6":{"displayName":"TB","description":null,"displayColor":"#087aa1ff","liquidGroupId":"6","liquidClass":null}},"ingredLocations":{"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4":{"A1":{"0":{"volume":100}},"B1":{"0":{"volume":100}},"C1":{"0":{"volume":100}},"D1":{"0":{"volume":100}},"E1":{"0":{"volume":100}},"F1":{"0":{"volume":100}},"G1":{"0":{"volume":100}},"H1":{"0":{"volume":100}},"A2":{"0":{"volume":100}},"B2":{"0":{"volume":100}},"C2":{"0":{"volume":100}},"D2":{"0":{"volume":100}},"E2":{"0":{"volume":100}},"F2":{"0":{"volume":100}},"G2":{"0":{"volume":100}},"H2":{"0":{"volume":100}},"A3":{"0":{"volume":100}},"B3":{"0":{"volume":100}},"C3":{"0":{"volume":100}},"D3":{"0":{"volume":100}},"E3":{"0":{"volume":100}},"F3":{"0":{"volume":100}},"G3":{"0":{"volume":100}},"H3":{"0":{"volume":100}},"A4":{"0":{"volume":100}},"B4":{"0":{"volume":100}},"C4":{"0":{"volume":100}},"D4":{"0":{"volume":100}},"E4":{"0":{"volume":100}},"F4":{"0":{"volume":100}},"G4":{"0":{"volume":100}},"H4":{"0":{"volume":100}},"A5":{"0":{"volume":100}},"B5":{"0":{"volume":100}},"C5":{"0":{"volume":100}},"D5":{"0":{"volume":100}},"E5":{"0":{"volume":100}},"F5":{"0":{"volume":100}},"G5":{"0":{"volume":100}},"H5":{"0":{"volume":100}},"A6":{"0":{"volume":100}},"B6":{"0":{"volume":100}},"C6":{"0":{"volume":100}},"D6":{"0":{"volume":100}},"E6":{"0":{"volume":100}},"F6":{"0":{"volume":100}},"G6":{"0":{"volume":100}},"H6":{"0":{"volume":100}},"A7":{"0":{"volume":100}},"B7":{"0":{"volume":100}},"C7":{"0":{"volume":100}},"D7":{"0":{"volume":100}},"E7":{"0":{"volume":100}},"F7":{"0":{"volume":100}},"G7":{"0":{"volume":100}},"H7":{"0":{"volume":100}},"A8":{"0":{"volume":100}},"B8":{"0":{"volume":100}},"C8":{"0":{"volume":100}},"D8":{"0":{"volume":100}},"E8":{"0":{"volume":100}},"F8":{"0":{"volume":100}},"G8":{"0":{"volume":100}},"H8":{"0":{"volume":100}},"A9":{"0":{"volume":100}},"B9":{"0":{"volume":100}},"C9":{"0":{"volume":100}},"D9":{"0":{"volume":100}},"E9":{"0":{"volume":100}},"F9":{"0":{"volume":100}},"G9":{"0":{"volume":100}},"H9":{"0":{"volume":100}},"A10":{"0":{"volume":100}},"B10":{"0":{"volume":100}},"C10":{"0":{"volume":100}},"D10":{"0":{"volume":100}},"E10":{"0":{"volume":100}},"F10":{"0":{"volume":100}},"G10":{"0":{"volume":100}},"H10":{"0":{"volume":100}},"A11":{"0":{"volume":100}},"B11":{"0":{"volume":100}},"C11":{"0":{"volume":100}},"D11":{"0":{"volume":100}},"E11":{"0":{"volume":100}},"F11":{"0":{"volume":100}},"G11":{"0":{"volume":100}},"H11":{"0":{"volume":100}},"A12":{"0":{"volume":100}},"B12":{"0":{"volume":100}},"C12":{"0":{"volume":100}},"D12":{"0":{"volume":100}},"E12":{"0":{"volume":100}},"F12":{"0":{"volume":100}},"G12":{"0":{"volume":100}},"H12":{"0":{"volume":100}}},"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2":{"A1":{"2":{"volume":10000}},"A2":{"2":{"volume":10000}},"A3":{"5":{"volume":10000}},"A4":{"5":{"volume":10000}},"A5":{"5":{"volume":10000}},"A6":{"5":{"volume":10000}},"A7":{"4":{"volume":10000}},"A8":{"4":{"volume":10000}},"A9":{"1":{"volume":10000}},"A10":{"1":{"volume":10000}},"A11":{"1":{"volume":10000}},"A12":{"1":{"volume":10000}}},"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4":{"A1":{"0":{"volume":100}},"B1":{"0":{"volume":100}},"C1":{"0":{"volume":100}},"D1":{"0":{"volume":100}},"E1":{"0":{"volume":100}},"F1":{"0":{"volume":100}},"G1":{"0":{"volume":100}},"H1":{"0":{"volume":100}},"A2":{"0":{"volume":100}},"B2":{"0":{"volume":100}},"C2":{"0":{"volume":100}},"D2":{"0":{"volume":100}},"E2":{"0":{"volume":100}},"F2":{"0":{"volume":100}},"G2":{"0":{"volume":100}},"H2":{"0":{"volume":100}},"A3":{"0":{"volume":100}},"B3":{"0":{"volume":100}},"C3":{"0":{"volume":100}},"D3":{"0":{"volume":100}},"E3":{"0":{"volume":100}},"F3":{"0":{"volume":100}},"G3":{"0":{"volume":100}},"H3":{"0":{"volume":100}},"A4":{"0":{"volume":100}},"B4":{"0":{"volume":100}},"C4":{"0":{"volume":100}},"D4":{"0":{"volume":100}},"E4":{"0":{"volume":100}},"F4":{"0":{"volume":100}},"G4":{"0":{"volume":100}},"H4":{"0":{"volume":100}},"A5":{"0":{"volume":100}},"B5":{"0":{"volume":100}},"C5":{"0":{"volume":100}},"D5":{"0":{"volume":100}},"E5":{"0":{"volume":100}},"F5":{"0":{"volume":100}},"G5":{"0":{"volume":100}},"H5":{"0":{"volume":100}},"A6":{"0":{"volume":100}},"B6":{"0":{"volume":100}},"C6":{"0":{"volume":100}},"D6":{"0":{"volume":100}},"E6":{"0":{"volume":100}},"F6":{"0":{"volume":100}},"G6":{"0":{"volume":100}},"H6":{"0":{"volume":100}},"A7":{"0":{"volume":100}},"B7":{"0":{"volume":100}},"C7":{"0":{"volume":100}},"D7":{"0":{"volume":100}},"E7":{"0":{"volume":100}},"F7":{"0":{"volume":100}},"G7":{"0":{"volume":100}},"H7":{"0":{"volume":100}},"A8":{"0":{"volume":100}},"B8":{"0":{"volume":100}},"C8":{"0":{"volume":100}},"D8":{"0":{"volume":100}},"E8":{"0":{"volume":100}},"F8":{"0":{"volume":100}},"G8":{"0":{"volume":100}},"H8":{"0":{"volume":100}},"A9":{"0":{"volume":100}},"B9":{"0":{"volume":100}},"C9":{"0":{"volume":100}},"D9":{"0":{"volume":100}},"E9":{"0":{"volume":100}},"F9":{"0":{"volume":100}},"G9":{"0":{"volume":100}},"H9":{"0":{"volume":100}},"A10":{"0":{"volume":100}},"B10":{"0":{"volume":100}},"C10":{"0":{"volume":100}},"D10":{"0":{"volume":100}},"E10":{"0":{"volume":100}},"F10":{"0":{"volume":100}},"G10":{"0":{"volume":100}},"H10":{"0":{"volume":100}},"A11":{"0":{"volume":100}},"B11":{"0":{"volume":100}},"C11":{"0":{"volume":100}},"D11":{"0":{"volume":100}},"E11":{"0":{"volume":100}},"F11":{"0":{"volume":100}},"G11":{"0":{"volume":100}},"H11":{"0":{"volume":100}},"A12":{"0":{"volume":100}},"B12":{"0":{"volume":100}},"C12":{"0":{"volume":100}},"D12":{"0":{"volume":100}},"E12":{"0":{"volume":100}},"F12":{"0":{"volume":100}},"G12":{"0":{"volume":100}},"H12":{"0":{"volume":100}}},"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/2":{"A1":{"1":{"volume":10000}},"A2":{"1":{"volume":10000}},"A5":{"3":{"volume":10000}},"A7":{"6":{"volume":10000}},"A3":{"1":{"volume":10000}},"A4":{"1":{"volume":10000}},"A6":{"3":{"volume":10000}}},"adfb4b92-d977-4694-8181-dfd2387673fa:opentrons/opentrons_96_filtertiprack_200ul/1":{}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"labwareLocationUpdate":{"bb063119-315e-4ac6-b4c7-088a6e688445:opentrons/opentrons_96_filtertiprack_200ul/1":"1","b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2":"2","aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4":"5","72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4":"6","4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/2":"3","adfb4b92-d977-4694-8181-dfd2387673fa:opentrons/opentrons_96_filtertiprack_200ul/1":"4","3f275f2a-19a4-4ba1-8219-afd1a3d38c3a:opentrons/opentrons_96_filtertiprack_200ul/1":"offDeck"},"moduleLocationUpdate":{},"pipetteLocationUpdate":{"806347f5-d454-4feb-9ba3-2fe5d0376a65":"left"},"trashBinLocationUpdate":{"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin":"cutout12"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{},"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__"},"2ceb731e-92ed-4cf4-872c-4d712ec84ce1":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"180","stepType":"moveLiquid","stepName":"A milk p1 (12-7)","stepDetails":"","id":"2ceb731e-92ed-4cf4-872c-4d712ec84ce1","dispense_touchTip_mmfromTop":null},"49d3ae38-ea8e-403a-bb20-4b1103e0162b":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"180","stepType":"moveLiquid","stepName":"A milk p1 (6-1)","stepDetails":"","id":"49d3ae38-ea8e-403a-bb20-4b1103e0162b","dispense_touchTip_mmfromTop":null},"d220fa8a-ea43-4887-b7d3-1ee2e996b13a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"r pbs p1 (12-7)","stepDetails":"","id":"d220fa8a-ea43-4887-b7d3-1ee2e996b13a","dispense_touchTip_mmfromTop":null},"0793860d-6e42-4a46-89b0-70e77d0df829":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"r pbs p1 (6-1)","stepDetails":"","id":"0793860d-6e42-4a46-89b0-70e77d0df829","dispense_touchTip_mmfromTop":null},"2f64dd5c-ea74-4bad-bf08-ef7f52f5e94e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"100","stepType":"moveLiquid","stepName":"a 1*ab p1 (12-7)","stepDetails":"","id":"2f64dd5c-ea74-4bad-bf08-ef7f52f5e94e","dispense_touchTip_mmfromTop":null},"60b29e21-d461-4511-8ffd-50f337667cd4":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"2 H","pauseTemperature":null,"pauseTime":"02:00:00","id":"60b29e21-d461-4511-8ffd-50f337667cd4","stepType":"pause","stepName":"pause 2h","stepDetails":""},"c18f9f3d-2d7e-41c9-891d-e4dd81eebff1":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"180","stepType":"moveLiquid","stepName":"A milk p2 (12-7)","stepDetails":"","id":"c18f9f3d-2d7e-41c9-891d-e4dd81eebff1","dispense_touchTip_mmfromTop":null},"f714fb9e-ef77-4f15-8380-43fa2e256b11":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"180","stepType":"moveLiquid","stepName":"A milk p2 (6-1)","stepDetails":"","id":"f714fb9e-ef77-4f15-8380-43fa2e256b11","dispense_touchTip_mmfromTop":null},"b8042302-fd37-4ad1-b6bd-1cc771c33bc1":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:6:00","id":"b8042302-fd37-4ad1-b6bd-1cc771c33bc1","stepType":"pause","stepName":"milk 10 min","stepDetails":""},"32a1f55d-36ff-478a-b3cd-632b5577be30":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:00:01","id":"32a1f55d-36ff-478a-b3cd-632b5577be30","stepType":"pause","stepName":"Add 1","stepDetails":""},"c6484da0-18ce-49b0-ae5b-98aa22510d26":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"r pbs p2 (12-7)","stepDetails":"","id":"c6484da0-18ce-49b0-ae5b-98aa22510d26","dispense_touchTip_mmfromTop":null},"731a35dd-aa0d-40f2-8f51-8159c3515a02":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"r pbs p2 (6-1)","stepDetails":"","id":"731a35dd-aa0d-40f2-8f51-8159c3515a02","dispense_touchTip_mmfromTop":null},"0f96cd6e-5321-49c0-a987-b90d58eb594a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"100","stepType":"moveLiquid","stepName":"a 1*ab p2 (12-7)","stepDetails":"","id":"0f96cd6e-5321-49c0-a987-b90d58eb594a","dispense_touchTip_mmfromTop":null},"469c2ccb-4317-45ef-87ed-9afe7c849c2a":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"REMOVE 1AB","pauseTemperature":null,"pauseTime":null,"id":"469c2ccb-4317-45ef-87ed-9afe7c849c2a","stepType":"pause","stepName":"pause","stepDetails":""},"17f896cf-f9b8-4cb6-8e41-62bc4586f335":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A9"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"17f896cf-f9b8-4cb6-8e41-62bc4586f335","dispense_touchTip_mmfromTop":null},"ec6ddbcd-5220-438f-9151-23e3c1483c0e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"ec6ddbcd-5220-438f-9151-23e3c1483c0e","dispense_touchTip_mmfromTop":null},"0bea0a5d-5d60-4da4-8a9c-c8b690b0dff4":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"R pbs","stepDetails":"","id":"0bea0a5d-5d60-4da4-8a9c-c8b690b0dff4","dispense_touchTip_mmfromTop":null},"078bf96f-87b6-4e58-8e01-ace4b64e3d54":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"180","stepType":"moveLiquid","stepName":"A PBS 2","stepDetails":"","id":"078bf96f-87b6-4e58-8e01-ace4b64e3d54","dispense_touchTip_mmfromTop":null},"a26f3873-489d-4fe5-9710-151872d015cc":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"180","stepType":"moveLiquid","stepName":"A PBS 2","stepDetails":"","id":"a26f3873-489d-4fe5-9710-151872d015cc","dispense_touchTip_mmfromTop":null},"919f6513-7dfe-49b3-a384-9957d978a1be":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"R pbs","stepDetails":"","id":"919f6513-7dfe-49b3-a384-9957d978a1be","dispense_touchTip_mmfromTop":null},"07ac41ec-152d-4223-9071-51a17bc9bd54":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"R pbs","stepDetails":"","id":"07ac41ec-152d-4223-9071-51a17bc9bd54","dispense_touchTip_mmfromTop":null},"3de37394-3004-4d95-90e6-efc9240ccade":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"200","stepType":"moveLiquid","stepName":"R pbs","stepDetails":"","id":"3de37394-3004-4d95-90e6-efc9240ccade","dispense_touchTip_mmfromTop":null},"6831f4cd-0aa0-45c2-bb3a-49c02e518779":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:00:01","id":"6831f4cd-0aa0-45c2-bb3a-49c02e518779","stepType":"pause","stepName":"pause","stepDetails":""},"2a90bf3c-f3a1-472c-9194-d264720fc559":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"100","stepType":"moveLiquid","stepName":"A 2AB","stepDetails":"","id":"2a90bf3c-f3a1-472c-9194-d264720fc559","dispense_touchTip_mmfromTop":null},"1dacc88a-29b0-4e6b-8fe3-8002fd1a0f24":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"100","stepType":"moveLiquid","stepName":"A 2AB","stepDetails":"","id":"1dacc88a-29b0-4e6b-8fe3-8002fd1a0f24","dispense_touchTip_mmfromTop":null},"415e5cef-9ba6-4484-b662-98421f812778":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"01:00:00","id":"415e5cef-9ba6-4484-b662-98421f812778","stepType":"pause","stepName":"pause","stepDetails":""},"45806cd0-1338-4947-974c-fac49754b3fc":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"REMOVE 2AB","pauseTemperature":null,"pauseTime":null,"id":"45806cd0-1338-4947-974c-fac49754b3fc","stepType":"pause","stepName":"pause","stepDetails":""},"0b5680ec-887a-458d-9eda-ca80bb37db6a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"0b5680ec-887a-458d-9eda-ca80bb37db6a","dispense_touchTip_mmfromTop":null},"b26ea0fa-914b-44b7-b771-e4e22cdba863":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"b26ea0fa-914b-44b7-b771-e4e22cdba863","dispense_touchTip_mmfromTop":null},"c86fe629-66e2-4711-8119-d0cd33bccf38":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"c86fe629-66e2-4711-8119-d0cd33bccf38","dispense_touchTip_mmfromTop":null},"3cdce018-c674-4234-a558-c11e3a7a5592":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"3cdce018-c674-4234-a558-c11e3a7a5592","dispense_touchTip_mmfromTop":null},"b850c02f-4a88-46f1-ba5b-f0719c978a92":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"REMOVE PBS, tap plate and add TB to reservoir","pauseTemperature":null,"pauseTime":null,"id":"b850c02f-4a88-46f1-ba5b-f0719c978a92","stepType":"pause","stepName":"pause","stepDetails":""},"77e800af-5eb9-46a5-bc7a-cd1a5b7ceaf8":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"40","stepType":"moveLiquid","stepName":"A TB","stepDetails":"","id":"77e800af-5eb9-46a5-bc7a-cd1a5b7ceaf8","dispense_touchTip_mmfromTop":null},"d6cc0380-f2fe-42c4-bc97-13b02699fa4f":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"40","stepType":"moveLiquid","stepName":"A TB","stepDetails":"","id":"d6cc0380-f2fe-42c4-bc97-13b02699fa4f","dispense_touchTip_mmfromTop":null}},"orderedStepIds":["2ceb731e-92ed-4cf4-872c-4d712ec84ce1","49d3ae38-ea8e-403a-bb20-4b1103e0162b","c18f9f3d-2d7e-41c9-891d-e4dd81eebff1","f714fb9e-ef77-4f15-8380-43fa2e256b11","b8042302-fd37-4ad1-b6bd-1cc771c33bc1","c6484da0-18ce-49b0-ae5b-98aa22510d26","731a35dd-aa0d-40f2-8f51-8159c3515a02","d220fa8a-ea43-4887-b7d3-1ee2e996b13a","0793860d-6e42-4a46-89b0-70e77d0df829","32a1f55d-36ff-478a-b3cd-632b5577be30","2f64dd5c-ea74-4bad-bf08-ef7f52f5e94e","0f96cd6e-5321-49c0-a987-b90d58eb594a","60b29e21-d461-4511-8ffd-50f337667cd4","469c2ccb-4317-45ef-87ed-9afe7c849c2a","17f896cf-f9b8-4cb6-8e41-62bc4586f335","ec6ddbcd-5220-438f-9151-23e3c1483c0e","078bf96f-87b6-4e58-8e01-ace4b64e3d54","a26f3873-489d-4fe5-9710-151872d015cc","0bea0a5d-5d60-4da4-8a9c-c8b690b0dff4","919f6513-7dfe-49b3-a384-9957d978a1be","07ac41ec-152d-4223-9071-51a17bc9bd54","3de37394-3004-4d95-90e6-efc9240ccade","6831f4cd-0aa0-45c2-bb3a-49c02e518779","2a90bf3c-f3a1-472c-9194-d264720fc559","1dacc88a-29b0-4e6b-8fe3-8002fd1a0f24","415e5cef-9ba6-4484-b662-98421f812778","45806cd0-1338-4947-974c-fac49754b3fc","0b5680ec-887a-458d-9eda-ca80bb37db6a","b26ea0fa-914b-44b7-b771-e4e22cdba863","c86fe629-66e2-4711-8119-d0cd33bccf38","3cdce018-c674-4234-a558-c11e3a7a5592","b850c02f-4a88-46f1-ba5b-f0719c978a92","77e800af-5eb9-46a5-bc7a-cd1a5b7ceaf8","d6cc0380-f2fe-42c4-bc97-13b02699fa4f"],"pipettes":{"806347f5-d454-4feb-9ba3-2fe5d0376a65":{"pipetteName":"p300_multi_gen2"}},"modules":{},"labware":{"bb063119-315e-4ac6-b4c7-088a6e688445:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"},"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/2":{"displayName":"reservoir","labwareDefURI":"opentrons/nest_12_reservoir_15ml/2"},"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/4":{"displayName":"96","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/4"},"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/4":{"displayName":"96  2","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/4"},"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/2":{"displayName":"reservoir 2","labwareDefURI":"opentrons/nest_12_reservoir_15ml/2"},"adfb4b92-d977-4694-8181-dfd2387673fa:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL (1)","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"},"3f275f2a-19a4-4ba1-8219-afd1a3d38c3a:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL (3)","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"}}}},"metadata":{"protocolName":"Stain (2 plates)","author":"Leonardo Giordano","description":"","created":1722868125837,"lastModified":1764091653754,"category":null,"subcategory":null,"tags":[],"source":"Protocol Designer"}}"""
