import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "Fix and Stain 1 plate",
    "author": "Leonardo Giordano",
    "created": "2024-08-05T14:28:45.837Z",
    "internalAppBuildDate": "Tue, 03 Feb 2026 18:27:38 GMT",
    "lastModified": "2026-02-09T21:08:32.900Z",
    "protocolDesigner": "8.8.0",
    "source": "Protocol Designer",
}

requirements = {"robotType": "OT-2", "apiLevel": "2.27"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Labware:
    tip_rack_2 = protocol.load_labware(
        "opentrons_96_filtertiprack_200ul",
        location="1",
        namespace="opentrons",
        version=1,
    )
    tip_rack_1 = protocol.load_labware(
        "opentrons_96_filtertiprack_200ul",
        location=protocol_api.OFF_DECK,
        label="Opentrons OT-2 96 Filter Tip Rack 200 µL (3)",
        namespace="opentrons",
        version=1,
    )
    well_plate_1 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="6",
        label="96 3",
        namespace="opentrons",
        version=5,
    )
    reservoir_1 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="2",
        label="reservoir 3",
        namespace="opentrons",
        version=3,
    )
    reservoir_2 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="3",
        label="reservoir 4",
        namespace="opentrons",
        version=3,
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
        wells=["A1"],
        liquid=liquid_3,
        volume=10000,
    )
    reservoir_1.load_liquid(
        wells=["A3", "A4"],
        liquid=liquid_6,
        volume=10000,
    )
    reservoir_1.load_liquid(
        wells=["A7"],
        liquid=liquid_5,
        volume=10000,
    )
    reservoir_1.load_liquid(
        wells=["A9", "A10"],
        liquid=liquid_2,
        volume=10000,
    )
    reservoir_2.load_liquid(
        wells=["A1", "A2"],
        liquid=liquid_2,
        volume=10000,
    )
    reservoir_2.load_liquid(
        wells=["A5"],
        liquid=liquid_4,
        volume=10000,
    )
    reservoir_2.load_liquid(
        wells=["A7"],
        liquid=liquid_7,
        volume=10000,
    )

    # PROTOCOL STEPS

    # Step 1: r methyl p1 (12-7)
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        dest=[reservoir_2["A12"], reservoir_2["A12"], reservoir_2["A12"], reservoir_2["A12"], reservoir_2["A12"], reservoir_2["A12"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
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

    # Step 2: r methyl p1 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        dest=[reservoir_2["A11"], reservoir_2["A11"], reservoir_2["A11"], reservoir_2["A11"], reservoir_2["A11"], reservoir_2["A11"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
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
    pipette_left.drop_tip()

    # Step 3: A MeOH P1 (12-7)
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_1["A1"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"], well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_3",
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

    # Step 4: Pause 30min
    protocol.delay(seconds=1800)

    # Step 5: Pause 30min
    protocol.pause("REMOVE MeOH, dry plate")

    # Step 6: A milk p1 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_6",
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

    # Step 7: A milk p1 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"]],
        dest=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_7",
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

    # Step 8: milk 10 min
    protocol.delay(seconds=360)

    # Step 9: r pbs p2 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        dest=[reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
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

    # Step 10: r pbs p2 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        dest=[reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_10",
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

    # Step 11: Add 1
    protocol.delay(seconds=1)

    # Step 12: a 1*ab p1 (12-7)
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_1["A7"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"], well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
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

    # Step 13: pause 2h
    protocol.delay(seconds=7200, msg="2 H")

    # Step 14: pause
    protocol.pause("REMOVE 1AB")

    # Step 15: A PBS
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
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

    # Step 16: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"]],
        dest=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
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

    # Step 17: R pbs
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        dest=[reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_17",
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

    # Step 18: R pbs
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        dest=[reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_18",
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

    # Step 19: pause
    protocol.delay(seconds=1)

    # Step 20: A 2AB
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_2["A5"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"], well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_20",
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

    # Step 21: pause
    protocol.delay(seconds=3600)

    # Step 22: pause
    protocol.pause("REMOVE 2AB")

    # Step 23: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_2["A1"], reservoir_2["A1"], reservoir_2["A1"], reservoir_2["A1"], reservoir_2["A1"], reservoir_2["A1"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_23",
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

    # Step 24: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_2["A2"], reservoir_2["A2"], reservoir_2["A2"], reservoir_2["A2"], reservoir_2["A2"], reservoir_2["A2"]],
        dest=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_24",
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

    # Step 25: pause
    protocol.pause("REMOVE PBS, tap plate and add TB to reservoir")

    # Step 26: A TB
    pipette_left.distribute_with_liquid_class(
        volume=40,
        source=[reservoir_2["A7"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"], well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_26",
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

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.8.0","data":{"pipetteTiprackAssignments":{"806347f5-d454-4feb-9ba3-2fe5d0376a65":["opentrons/opentrons_96_filtertiprack_200ul/1"]},"dismissedWarnings":{"form":["BELOW_MIN_DISPOSAL_VOLUME"],"timeline":["ASPIRATE_MORE_THAN_WELL_CONTENTS","ASPIRATE_FROM_PRISTINE_WELL"]},"ingredients":{"0":{"displayName":"Methylcellulose","description":null,"displayColor":"#b925ff","liquidGroupId":"0","liquidClass":null},"1":{"displayName":"PBS","description":null,"displayColor":"#9dffd8","liquidGroupId":"1","liquidClass":null},"2":{"displayName":"MeOH","description":null,"displayColor":"#50d5ff","liquidGroupId":"2","liquidClass":null},"3":{"displayName":"2Ab","description":null,"displayColor":"#ff9900","liquidGroupId":"3","liquidClass":null},"4":{"displayName":"1*AB","description":null,"displayColor":"#ff80f5","liquidGroupId":"4","liquidClass":null},"5":{"displayName":"MILK","description":null,"displayColor":"#c2af4eff","liquidGroupId":"5","liquidClass":null},"6":{"displayName":"TB","description":null,"displayColor":"#087aa1ff","liquidGroupId":"6","liquidClass":null}},"ingredLocations":{"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5":{"A1":{"0":{"volume":100}},"B1":{"0":{"volume":100}},"C1":{"0":{"volume":100}},"D1":{"0":{"volume":100}},"E1":{"0":{"volume":100}},"F1":{"0":{"volume":100}},"G1":{"0":{"volume":100}},"H1":{"0":{"volume":100}},"A2":{"0":{"volume":100}},"B2":{"0":{"volume":100}},"C2":{"0":{"volume":100}},"D2":{"0":{"volume":100}},"E2":{"0":{"volume":100}},"F2":{"0":{"volume":100}},"G2":{"0":{"volume":100}},"H2":{"0":{"volume":100}},"A3":{"0":{"volume":100}},"B3":{"0":{"volume":100}},"C3":{"0":{"volume":100}},"D3":{"0":{"volume":100}},"E3":{"0":{"volume":100}},"F3":{"0":{"volume":100}},"G3":{"0":{"volume":100}},"H3":{"0":{"volume":100}},"A4":{"0":{"volume":100}},"B4":{"0":{"volume":100}},"C4":{"0":{"volume":100}},"D4":{"0":{"volume":100}},"E4":{"0":{"volume":100}},"F4":{"0":{"volume":100}},"G4":{"0":{"volume":100}},"H4":{"0":{"volume":100}},"A5":{"0":{"volume":100}},"B5":{"0":{"volume":100}},"C5":{"0":{"volume":100}},"D5":{"0":{"volume":100}},"E5":{"0":{"volume":100}},"F5":{"0":{"volume":100}},"G5":{"0":{"volume":100}},"H5":{"0":{"volume":100}},"A6":{"0":{"volume":100}},"B6":{"0":{"volume":100}},"C6":{"0":{"volume":100}},"D6":{"0":{"volume":100}},"E6":{"0":{"volume":100}},"F6":{"0":{"volume":100}},"G6":{"0":{"volume":100}},"H6":{"0":{"volume":100}},"A7":{"0":{"volume":100}},"B7":{"0":{"volume":100}},"C7":{"0":{"volume":100}},"D7":{"0":{"volume":100}},"E7":{"0":{"volume":100}},"F7":{"0":{"volume":100}},"G7":{"0":{"volume":100}},"H7":{"0":{"volume":100}},"A8":{"0":{"volume":100}},"B8":{"0":{"volume":100}},"C8":{"0":{"volume":100}},"D8":{"0":{"volume":100}},"E8":{"0":{"volume":100}},"F8":{"0":{"volume":100}},"G8":{"0":{"volume":100}},"H8":{"0":{"volume":100}},"A9":{"0":{"volume":100}},"B9":{"0":{"volume":100}},"C9":{"0":{"volume":100}},"D9":{"0":{"volume":100}},"E9":{"0":{"volume":100}},"F9":{"0":{"volume":100}},"G9":{"0":{"volume":100}},"H9":{"0":{"volume":100}},"A10":{"0":{"volume":100}},"B10":{"0":{"volume":100}},"C10":{"0":{"volume":100}},"D10":{"0":{"volume":100}},"E10":{"0":{"volume":100}},"F10":{"0":{"volume":100}},"G10":{"0":{"volume":100}},"H10":{"0":{"volume":100}},"A11":{"0":{"volume":100}},"B11":{"0":{"volume":100}},"C11":{"0":{"volume":100}},"D11":{"0":{"volume":100}},"E11":{"0":{"volume":100}},"F11":{"0":{"volume":100}},"G11":{"0":{"volume":100}},"H11":{"0":{"volume":100}},"A12":{"0":{"volume":100}},"B12":{"0":{"volume":100}},"C12":{"0":{"volume":100}},"D12":{"0":{"volume":100}},"E12":{"0":{"volume":100}},"F12":{"0":{"volume":100}},"G12":{"0":{"volume":100}},"H12":{"0":{"volume":100}}},"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3":{"A1":{"2":{"volume":10000}},"A3":{"5":{"volume":10000}},"A4":{"5":{"volume":10000}},"A7":{"4":{"volume":10000}},"A9":{"1":{"volume":10000}},"A10":{"1":{"volume":10000}}},"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3":{"A1":{"1":{"volume":10000}},"A2":{"1":{"volume":10000}},"A5":{"3":{"volume":10000}},"A7":{"6":{"volume":10000}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"labwareLocationUpdate":{"bb063119-315e-4ac6-b4c7-088a6e688445:opentrons/opentrons_96_filtertiprack_200ul/1":"1","3f275f2a-19a4-4ba1-8219-afd1a3d38c3a:opentrons/opentrons_96_filtertiprack_200ul/1":"offDeck","90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5":"6","33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3":"2","5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3":"3"},"moduleLocationUpdate":{},"pipetteLocationUpdate":{"806347f5-d454-4feb-9ba3-2fe5d0376a65":"left"},"trashBinLocationUpdate":{"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin":"cutout12"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{},"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__","moduleStateUpdate":{}},"5e579d8a-615d-4293-aa23-efe468c6527f":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:30:00","id":"5e579d8a-615d-4293-aa23-efe468c6527f","stepType":"pause","stepName":"Pause 30min","stepDetails":""},"60b29e21-d461-4511-8ffd-50f337667cd4":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"2 H","pauseTemperature":null,"pauseTime":"02:00:00","id":"60b29e21-d461-4511-8ffd-50f337667cd4","stepType":"pause","stepName":"pause 2h","stepDetails":""},"b8042302-fd37-4ad1-b6bd-1cc771c33bc1":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:6:00","id":"b8042302-fd37-4ad1-b6bd-1cc771c33bc1","stepType":"pause","stepName":"milk 10 min","stepDetails":""},"32a1f55d-36ff-478a-b3cd-632b5577be30":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:00:01","id":"32a1f55d-36ff-478a-b3cd-632b5577be30","stepType":"pause","stepName":"Add 1","stepDetails":""},"87235c2b-ea56-456c-8422-ed9b40f2c253":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"REMOVE MeOH, dry plate","pauseTemperature":null,"pauseTime":null,"id":"87235c2b-ea56-456c-8422-ed9b40f2c253","stepType":"pause","stepName":"Pause 30min","stepDetails":""},"469c2ccb-4317-45ef-87ed-9afe7c849c2a":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"REMOVE 1AB","pauseTemperature":null,"pauseTime":null,"id":"469c2ccb-4317-45ef-87ed-9afe7c849c2a","stepType":"pause","stepName":"pause","stepDetails":""},"6831f4cd-0aa0-45c2-bb3a-49c02e518779":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:00:01","id":"6831f4cd-0aa0-45c2-bb3a-49c02e518779","stepType":"pause","stepName":"pause","stepDetails":""},"415e5cef-9ba6-4484-b662-98421f812778":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"01:00:00","id":"415e5cef-9ba6-4484-b662-98421f812778","stepType":"pause","stepName":"pause","stepDetails":""},"45806cd0-1338-4947-974c-fac49754b3fc":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"REMOVE 2AB","pauseTemperature":null,"pauseTime":null,"id":"45806cd0-1338-4947-974c-fac49754b3fc","stepType":"pause","stepName":"pause","stepDetails":""},"b850c02f-4a88-46f1-ba5b-f0719c978a92":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"REMOVE PBS, tap plate and add TB to reservoir","pauseTemperature":null,"pauseTime":null,"id":"b850c02f-4a88-46f1-ba5b-f0719c978a92","stepType":"pause","stepName":"pause","stepDetails":""},"e98cff20-9750-4f35-8f41-afd22bec35cb":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":45,"aspirate_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":2,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r methyl p1 (12-7)","stepDetails":"","id":"e98cff20-9750-4f35-8f41-afd22bec35cb","dispense_touchTip_mmfromTop":null},"52ffc5b1-ac8c-4d03-82fe-da090c29b2e3":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":45,"aspirate_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":2,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r methyl p1 (12-7)","stepDetails":"","id":"52ffc5b1-ac8c-4d03-82fe-da090c29b2e3","dispense_touchTip_mmfromTop":null},"7d306e29-4ffe-4436-a8fd-55f485f1fdd3":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":45,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"A MeOH P1 (12-7)","stepDetails":"","id":"7d306e29-4ffe-4436-a8fd-55f485f1fdd3","dispense_touchTip_mmfromTop":null},"45695b79-bcc7-44b5-a329-2cf8df861591":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A milk p1 (12-7)","stepDetails":"","id":"45695b79-bcc7-44b5-a329-2cf8df861591","dispense_touchTip_mmfromTop":null},"80d9ebad-f5af-416f-87bd-16809c8abf23":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A milk p1 (12-7)","stepDetails":"","id":"80d9ebad-f5af-416f-87bd-16809c8abf23","dispense_touchTip_mmfromTop":null},"02957744-6cb7-43d2-bb57-3e3ddafbd5b1":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r pbs p2 (12-7)","stepDetails":"","id":"02957744-6cb7-43d2-bb57-3e3ddafbd5b1","dispense_touchTip_mmfromTop":null},"6958c417-d868-45d9-bded-d8bf7e723411":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r pbs p2 (12-7)","stepDetails":"","id":"6958c417-d868-45d9-bded-d8bf7e723411","dispense_touchTip_mmfromTop":null},"e4704cad-3712-42d1-b2d1-bddb9749b2a4":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"a 1*ab p1 (12-7)","stepDetails":"","id":"e4704cad-3712-42d1-b2d1-bddb9749b2a4","dispense_touchTip_mmfromTop":null},"8faf1f3e-a3f9-435f-b118-e71fd2d7ef24":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A9"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"8faf1f3e-a3f9-435f-b118-e71fd2d7ef24","dispense_touchTip_mmfromTop":null},"8d7c8848-40a9-43f0-9a5b-fe2152257f85":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"8d7c8848-40a9-43f0-9a5b-fe2152257f85","dispense_touchTip_mmfromTop":null},"f374a329-a282-42a8-86fb-7d1bd25dd933":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"R pbs","stepDetails":"","id":"f374a329-a282-42a8-86fb-7d1bd25dd933","dispense_touchTip_mmfromTop":null},"a1ca55f7-7379-4270-9fba-6d9007e25d14":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"R pbs","stepDetails":"","id":"a1ca55f7-7379-4270-9fba-6d9007e25d14","dispense_touchTip_mmfromTop":null},"075ea641-d5ac-4381-ad71-bfdf7063710e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"A 2AB","stepDetails":"","id":"075ea641-d5ac-4381-ad71-bfdf7063710e","dispense_touchTip_mmfromTop":null},"d490d2e2-2aab-4f10-befc-96294ca25de9":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"d490d2e2-2aab-4f10-befc-96294ca25de9","dispense_touchTip_mmfromTop":null},"4a426d2a-9304-42be-bdf3-319de14f44b5":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"4a426d2a-9304-42be-bdf3-319de14f44b5","dispense_touchTip_mmfromTop":null},"ffd8d4cd-b763-4f80-aa29-e6a874094542":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"40","stepType":"moveLiquid","stepName":"A TB","stepDetails":"","id":"ffd8d4cd-b763-4f80-aa29-e6a874094542","dispense_touchTip_mmfromTop":null}},"orderedStepIds":["e98cff20-9750-4f35-8f41-afd22bec35cb","52ffc5b1-ac8c-4d03-82fe-da090c29b2e3","7d306e29-4ffe-4436-a8fd-55f485f1fdd3","5e579d8a-615d-4293-aa23-efe468c6527f","87235c2b-ea56-456c-8422-ed9b40f2c253","45695b79-bcc7-44b5-a329-2cf8df861591","80d9ebad-f5af-416f-87bd-16809c8abf23","b8042302-fd37-4ad1-b6bd-1cc771c33bc1","02957744-6cb7-43d2-bb57-3e3ddafbd5b1","6958c417-d868-45d9-bded-d8bf7e723411","32a1f55d-36ff-478a-b3cd-632b5577be30","e4704cad-3712-42d1-b2d1-bddb9749b2a4","60b29e21-d461-4511-8ffd-50f337667cd4","469c2ccb-4317-45ef-87ed-9afe7c849c2a","8faf1f3e-a3f9-435f-b118-e71fd2d7ef24","8d7c8848-40a9-43f0-9a5b-fe2152257f85","f374a329-a282-42a8-86fb-7d1bd25dd933","a1ca55f7-7379-4270-9fba-6d9007e25d14","6831f4cd-0aa0-45c2-bb3a-49c02e518779","075ea641-d5ac-4381-ad71-bfdf7063710e","415e5cef-9ba6-4484-b662-98421f812778","45806cd0-1338-4947-974c-fac49754b3fc","d490d2e2-2aab-4f10-befc-96294ca25de9","4a426d2a-9304-42be-bdf3-319de14f44b5","b850c02f-4a88-46f1-ba5b-f0719c978a92","ffd8d4cd-b763-4f80-aa29-e6a874094542"],"pipettes":{"806347f5-d454-4feb-9ba3-2fe5d0376a65":{"pipetteName":"p300_multi_gen2"}},"modules":{},"labware":{"bb063119-315e-4ac6-b4c7-088a6e688445:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"},"3f275f2a-19a4-4ba1-8219-afd1a3d38c3a:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL (3)","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"},"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5":{"displayName":"96 3","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/5"},"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3":{"displayName":"reservoir 3","labwareDefURI":"opentrons/nest_12_reservoir_15ml/3"},"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3":{"displayName":"reservoir 4","labwareDefURI":"opentrons/nest_12_reservoir_15ml/3"}}}},"metadata":{"protocolName":"Fix and Stain 1 plate","author":"Leonardo Giordano","description":"","created":1722868125837,"lastModified":1770671312900,"category":null,"subcategory":null,"tags":[],"source":"Protocol Designer"}}"""
