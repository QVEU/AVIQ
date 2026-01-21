import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "Serial Dilution (2plates)",
    "author": "Leonardo Giordano",
    "created": "2024-08-09T15:58:47.925Z",
    "internalAppBuildDate": "Tue, 16 Dec 2025 16:02:03 GMT",
    "lastModified": "2026-01-21T18:42:49.840Z",
    "protocolDesigner": "8.7.1",
    "source": "Protocol Designer",
}

requirements = {"robotType": "OT-2", "apiLevel": "2.27"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Labware:
    tip_rack_1 = protocol.load_labware(
        "opentrons_96_filtertiprack_200ul",
        location="1",
        namespace="opentrons",
        version=1,
    )
    well_plate_2 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="4",
        label="96",
        namespace="opentrons",
        version=5,
    )
    reservoir_1 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="2",
        label="reservoir",
        namespace="opentrons",
        version=3,
    )
    well_plate_3 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="7",
        label="dilution",
        namespace="opentrons",
        version=5,
    )
    well_plate_4 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="5",
        label="96 2",
        namespace="opentrons",
        version=5,
    )
    well_plate_1 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="8",
        label="dillution 2",
        namespace="opentrons",
        version=5,
    )

    # Load Pipettes:
    pipette_left = protocol.load_instrument("p300_multi_gen2", "left")
    pipette_right = protocol.load_instrument("p300_single_gen2", "right")

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "optimem",
        display_color="#ff9900",
    )
    liquid_2 = protocol.define_liquid(
        "virus",
        display_color="#ff4f4f",
    )
    liquid_3 = protocol.define_liquid(
        "Pbs",
        display_color="#9dffd8",
    )
    liquid_4 = protocol.define_liquid(
        "media",
        display_color="#ff80f5",
    )

    # Load Liquids:
    reservoir_1.load_liquid(
        wells=["A1", "A2"],
        liquid=liquid_1,
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
        liquid=liquid_4,
        volume=200,
    )
    well_plate_3.load_liquid(
        wells=[
            "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
            "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"
        ],
        liquid=liquid_2,
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
        liquid=liquid_4,
        volume=200,
    )
    well_plate_1.load_liquid(
        wells=[
            "A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",
            "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"
        ],
        liquid=liquid_2,
        volume=100,
    )

    # PROTOCOL STEPS

    # Step 1: a opti
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.distribute_with_liquid_class(
        volume=90,
        source=[reservoir_1["A1"]],
        dest=[well_plate_3["A12"], well_plate_3["A11"], well_plate_3["A10"], well_plate_3["A9"], well_plate_3["A8"], well_plate_3["A7"], well_plate_3["A6"], well_plate_3["A5"], well_plate_3["A4"], well_plate_3["A3"], well_plate_3["A2"], well_plate_3["A1"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_1",
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
                "multi_dispense": {
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
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 0)],
                },
            }}},
        ),
    )

    # Step 2: a opti
    pipette_left.distribute_with_liquid_class(
        volume=90,
        source=[reservoir_1["A2"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"], well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_2",
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
                "multi_dispense": {
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
                    "conditioning_by_volume": [(0, 0)],
                    "disposal_by_volume": [(0, 0)],
                },
            }}},
        ),
    )

    # Step 3: a virus -2
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_1["A1"]],
        dest=[well_plate_1["A3"]],
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
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 4: a virus -2
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_1["A3"]],
        dest=[well_plate_1["A5"]],
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
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 5: a virus -2
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_1["A5"]],
        dest=[well_plate_1["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_5",
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 6: a virus -2
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_1["A7"]],
        dest=[well_plate_1["A9"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 7: a virus -2
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_1["A9"]],
        dest=[well_plate_1["A11"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 8: a virus -2
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_1["A2"]],
        dest=[well_plate_1["A4"]],
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
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 9: a virus -2
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_1["A4"]],
        dest=[well_plate_1["A6"]],
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
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 10: a virus -2
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_1["A6"]],
        dest=[well_plate_1["A8"]],
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
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 94)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 11: a virus -2
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_1["A8"]],
        dest=[well_plate_1["A10"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_11",
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 12: a virus -2
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_1["A10"]],
        dest=[well_plate_1["A12"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_12",
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 13: pause
    protocol.delay(seconds=1)

    # Step 14: a virus -2
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_3["A1"]],
        dest=[well_plate_3["A3"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_14",
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 15: a virus -3
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_3["A3"]],
        dest=[well_plate_3["A5"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 16: a virus -4
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_3["A5"]],
        dest=[well_plate_3["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 17: a virus -5
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_3["A7"]],
        dest=[well_plate_3["A9"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 18: a virus -6
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_3["A9"]],
        dest=[well_plate_3["A11"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
                },
            }}},
        ),
    )

    # Step 19: a virus -2
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_3["A2"]],
        dest=[well_plate_3["A4"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_19",
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 20: a virus -3
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_3["A4"]],
        dest=[well_plate_3["A6"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_20",
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 21: a virus -4
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_3["A6"]],
        dest=[well_plate_3["A8"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_21",
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 22: a virus -5
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_3["A8"]],
        dest=[well_plate_3["A10"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_22",
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 23: a virus -6
    pipette_left.transfer_with_liquid_class(
        volume=10,
        source=[well_plate_3["A10"]],
        dest=[well_plate_3["A12"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
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
                    "mix": {"enabled": True, "repetitions": 10, "volume": 40},
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

    # Step 24: pause
    protocol.delay(seconds=1)

    # Step 25: pause
    protocol.delay(seconds=1)

    # Step 26: r media 12-7
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"]],
        dest=[reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_26",
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

    # Step 27: r media 12-7
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        dest=[reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_27",
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

    # Step 28: r media 12-7
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_4["A12"], well_plate_4["A11"], well_plate_4["A10"], well_plate_4["A9"], well_plate_4["A8"], well_plate_4["A7"]],
        dest=[reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
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

    # Step 29: r media 12-7
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_4["A6"], well_plate_4["A5"], well_plate_4["A4"], well_plate_4["A3"], well_plate_4["A2"], well_plate_4["A1"]],
        dest=[reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
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

    # Step 30: pause
    protocol.delay(seconds=1)

    # Step 31: a virus
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.transfer_with_liquid_class(
        volume=40,
        source=[well_plate_3["A12"], well_plate_3["A11"], well_plate_3["A10"], well_plate_3["A9"], well_plate_3["A8"], well_plate_3["A7"], well_plate_3["A6"], well_plate_3["A5"], well_plate_3["A4"], well_plate_3["A3"], well_plate_3["A2"], well_plate_3["A1"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"], well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
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

    # Step 32: a virus
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.transfer_with_liquid_class(
        volume=40,
        source=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"], well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        dest=[well_plate_4["A12"], well_plate_4["A11"], well_plate_4["A10"], well_plate_4["A9"], well_plate_4["A8"], well_plate_4["A7"], well_plate_4["A6"], well_plate_4["A5"], well_plate_4["A4"], well_plate_4["A3"], well_plate_4["A2"], well_plate_4["A1"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_32",
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
    pipette_left.drop_tip()

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.7.0","data":{"pipetteTiprackAssignments":{"358becf5-7d09-4bc8-b8af-fdada6fde6b3":["opentrons/opentrons_96_filtertiprack_200ul/1"],"f2d3d83c-9af8-42e5-ad6f-7e1f2ab0f2e5":["opentrons/opentrons_96_filtertiprack_200ul/1"]},"dismissedWarnings":{"form":["BELOW_PIPETTE_MINIMUM_VOLUME","TIP_POSITIONED_LOW_IN_TUBE","BELOW_MIN_DISPOSAL_VOLUME"],"timeline":["ASPIRATE_MORE_THAN_WELL_CONTENTS","ASPIRATE_FROM_PRISTINE_WELL"]},"ingredients":{"0":{"displayName":"optimem","description":null,"displayColor":"#ff9900","liquidGroupId":"0","liquidClass":null},"1":{"displayName":"virus","description":null,"displayColor":"#ff4f4f","liquidGroupId":"1","liquidClass":null},"2":{"displayName":"Pbs","description":null,"displayColor":"#9dffd8","liquidGroupId":"2","liquidClass":null},"3":{"displayName":"media","description":null,"displayColor":"#ff80f5","liquidGroupId":"3","liquidClass":null}},"ingredLocations":{"4da13a5d-ef01-47e2-9888-d3a165ebde75:opentrons/nest_12_reservoir_15ml/3":{"A1":{"0":{"volume":10000}},"A2":{"0":{"volume":10000}}},"445ed8b9-817e-474d-981b-62f48bb83f69:opentrons/nest_96_wellplate_200ul_flat/5":{"A1":{"3":{"volume":200}},"B1":{"3":{"volume":200}},"C1":{"3":{"volume":200}},"D1":{"3":{"volume":200}},"E1":{"3":{"volume":200}},"F1":{"3":{"volume":200}},"G1":{"3":{"volume":200}},"H1":{"3":{"volume":200}},"A2":{"3":{"volume":200}},"B2":{"3":{"volume":200}},"C2":{"3":{"volume":200}},"D2":{"3":{"volume":200}},"E2":{"3":{"volume":200}},"F2":{"3":{"volume":200}},"G2":{"3":{"volume":200}},"H2":{"3":{"volume":200}},"A3":{"3":{"volume":200}},"B3":{"3":{"volume":200}},"C3":{"3":{"volume":200}},"D3":{"3":{"volume":200}},"E3":{"3":{"volume":200}},"F3":{"3":{"volume":200}},"G3":{"3":{"volume":200}},"H3":{"3":{"volume":200}},"A4":{"3":{"volume":200}},"B4":{"3":{"volume":200}},"C4":{"3":{"volume":200}},"D4":{"3":{"volume":200}},"E4":{"3":{"volume":200}},"F4":{"3":{"volume":200}},"G4":{"3":{"volume":200}},"H4":{"3":{"volume":200}},"A5":{"3":{"volume":200}},"B5":{"3":{"volume":200}},"C5":{"3":{"volume":200}},"D5":{"3":{"volume":200}},"E5":{"3":{"volume":200}},"F5":{"3":{"volume":200}},"G5":{"3":{"volume":200}},"H5":{"3":{"volume":200}},"A6":{"3":{"volume":200}},"B6":{"3":{"volume":200}},"C6":{"3":{"volume":200}},"D6":{"3":{"volume":200}},"E6":{"3":{"volume":200}},"F6":{"3":{"volume":200}},"G6":{"3":{"volume":200}},"H6":{"3":{"volume":200}},"A7":{"3":{"volume":200}},"B7":{"3":{"volume":200}},"C7":{"3":{"volume":200}},"D7":{"3":{"volume":200}},"E7":{"3":{"volume":200}},"F7":{"3":{"volume":200}},"G7":{"3":{"volume":200}},"H7":{"3":{"volume":200}},"A8":{"3":{"volume":200}},"B8":{"3":{"volume":200}},"C8":{"3":{"volume":200}},"D8":{"3":{"volume":200}},"E8":{"3":{"volume":200}},"F8":{"3":{"volume":200}},"G8":{"3":{"volume":200}},"H8":{"3":{"volume":200}},"A9":{"3":{"volume":200}},"B9":{"3":{"volume":200}},"C9":{"3":{"volume":200}},"D9":{"3":{"volume":200}},"E9":{"3":{"volume":200}},"F9":{"3":{"volume":200}},"G9":{"3":{"volume":200}},"H9":{"3":{"volume":200}},"A10":{"3":{"volume":200}},"B10":{"3":{"volume":200}},"C10":{"3":{"volume":200}},"D10":{"3":{"volume":200}},"E10":{"3":{"volume":200}},"F10":{"3":{"volume":200}},"G10":{"3":{"volume":200}},"H10":{"3":{"volume":200}},"A11":{"3":{"volume":200}},"B11":{"3":{"volume":200}},"C11":{"3":{"volume":200}},"D11":{"3":{"volume":200}},"E11":{"3":{"volume":200}},"F11":{"3":{"volume":200}},"G11":{"3":{"volume":200}},"H11":{"3":{"volume":200}},"A12":{"3":{"volume":200}},"B12":{"3":{"volume":200}},"C12":{"3":{"volume":200}},"D12":{"3":{"volume":200}},"E12":{"3":{"volume":200}},"F12":{"3":{"volume":200}},"G12":{"3":{"volume":200}},"H12":{"3":{"volume":200}}},"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5":{"A1":{"1":{"volume":100}},"B1":{"1":{"volume":100}},"C1":{"1":{"volume":100}},"D1":{"1":{"volume":100}},"E1":{"1":{"volume":100}},"F1":{"1":{"volume":100}},"G1":{"1":{"volume":100}},"H1":{"1":{"volume":100}},"A2":{"1":{"volume":100}},"B2":{"1":{"volume":100}},"C2":{"1":{"volume":100}},"D2":{"1":{"volume":100}},"E2":{"1":{"volume":100}},"F2":{"1":{"volume":100}},"G2":{"1":{"volume":100}},"H2":{"1":{"volume":100}}},"f7aa6016-ca85-4898-bff9-148d4be959cf:opentrons/nest_96_wellplate_200ul_flat/5":{"A1":{"3":{"volume":200}},"B1":{"3":{"volume":200}},"C1":{"3":{"volume":200}},"D1":{"3":{"volume":200}},"E1":{"3":{"volume":200}},"F1":{"3":{"volume":200}},"G1":{"3":{"volume":200}},"H1":{"3":{"volume":200}},"A2":{"3":{"volume":200}},"B2":{"3":{"volume":200}},"C2":{"3":{"volume":200}},"D2":{"3":{"volume":200}},"E2":{"3":{"volume":200}},"F2":{"3":{"volume":200}},"G2":{"3":{"volume":200}},"H2":{"3":{"volume":200}},"A3":{"3":{"volume":200}},"B3":{"3":{"volume":200}},"C3":{"3":{"volume":200}},"D3":{"3":{"volume":200}},"E3":{"3":{"volume":200}},"F3":{"3":{"volume":200}},"G3":{"3":{"volume":200}},"H3":{"3":{"volume":200}},"A4":{"3":{"volume":200}},"B4":{"3":{"volume":200}},"C4":{"3":{"volume":200}},"D4":{"3":{"volume":200}},"E4":{"3":{"volume":200}},"F4":{"3":{"volume":200}},"G4":{"3":{"volume":200}},"H4":{"3":{"volume":200}},"A5":{"3":{"volume":200}},"B5":{"3":{"volume":200}},"C5":{"3":{"volume":200}},"D5":{"3":{"volume":200}},"E5":{"3":{"volume":200}},"F5":{"3":{"volume":200}},"G5":{"3":{"volume":200}},"H5":{"3":{"volume":200}},"A6":{"3":{"volume":200}},"B6":{"3":{"volume":200}},"C6":{"3":{"volume":200}},"D6":{"3":{"volume":200}},"E6":{"3":{"volume":200}},"F6":{"3":{"volume":200}},"G6":{"3":{"volume":200}},"H6":{"3":{"volume":200}},"A7":{"3":{"volume":200}},"B7":{"3":{"volume":200}},"C7":{"3":{"volume":200}},"D7":{"3":{"volume":200}},"E7":{"3":{"volume":200}},"F7":{"3":{"volume":200}},"G7":{"3":{"volume":200}},"H7":{"3":{"volume":200}},"A8":{"3":{"volume":200}},"B8":{"3":{"volume":200}},"C8":{"3":{"volume":200}},"D8":{"3":{"volume":200}},"E8":{"3":{"volume":200}},"F8":{"3":{"volume":200}},"G8":{"3":{"volume":200}},"H8":{"3":{"volume":200}},"A9":{"3":{"volume":200}},"B9":{"3":{"volume":200}},"C9":{"3":{"volume":200}},"D9":{"3":{"volume":200}},"E9":{"3":{"volume":200}},"F9":{"3":{"volume":200}},"G9":{"3":{"volume":200}},"H9":{"3":{"volume":200}},"A10":{"3":{"volume":200}},"B10":{"3":{"volume":200}},"C10":{"3":{"volume":200}},"D10":{"3":{"volume":200}},"E10":{"3":{"volume":200}},"F10":{"3":{"volume":200}},"G10":{"3":{"volume":200}},"H10":{"3":{"volume":200}},"A11":{"3":{"volume":200}},"B11":{"3":{"volume":200}},"C11":{"3":{"volume":200}},"D11":{"3":{"volume":200}},"E11":{"3":{"volume":200}},"F11":{"3":{"volume":200}},"G11":{"3":{"volume":200}},"H11":{"3":{"volume":200}},"A12":{"3":{"volume":200}},"B12":{"3":{"volume":200}},"C12":{"3":{"volume":200}},"D12":{"3":{"volume":200}},"E12":{"3":{"volume":200}},"F12":{"3":{"volume":200}},"G12":{"3":{"volume":200}},"H12":{"3":{"volume":200}}},"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5":{"A1":{"1":{"volume":100}},"B1":{"1":{"volume":100}},"C1":{"1":{"volume":100}},"D1":{"1":{"volume":100}},"E1":{"1":{"volume":100}},"F1":{"1":{"volume":100}},"G1":{"1":{"volume":100}},"H1":{"1":{"volume":100}},"A2":{"1":{"volume":100}},"B2":{"1":{"volume":100}},"C2":{"1":{"volume":100}},"D2":{"1":{"volume":100}},"E2":{"1":{"volume":100}},"F2":{"1":{"volume":100}},"G2":{"1":{"volume":100}},"H2":{"1":{"volume":100}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"labwareLocationUpdate":{"8e31dd41-f40c-4d4c-a847-aa62cbe84695:opentrons/opentrons_96_filtertiprack_200ul/1":"1","445ed8b9-817e-474d-981b-62f48bb83f69:opentrons/nest_96_wellplate_200ul_flat/5":"4","4da13a5d-ef01-47e2-9888-d3a165ebde75:opentrons/nest_12_reservoir_15ml/3":"2","60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5":"7","f7aa6016-ca85-4898-bff9-148d4be959cf:opentrons/nest_96_wellplate_200ul_flat/5":"5","03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5":"8"},"moduleLocationUpdate":{},"pipetteLocationUpdate":{"358becf5-7d09-4bc8-b8af-fdada6fde6b3":"left","f2d3d83c-9af8-42e5-ad6f-7e1f2ab0f2e5":"right"},"trashBinLocationUpdate":{"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin":"cutout12"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{},"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__"},"bf798af2-a3ef-411a-97f7-4721425d0e6a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -2","stepDetails":"","id":"bf798af2-a3ef-411a-97f7-4721425d0e6a","dispense_touchTip_mmfromTop":null},"0d903926-6ed6-4a3d-ba98-ec77137c3b94":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -3","stepDetails":"","id":"0d903926-6ed6-4a3d-ba98-ec77137c3b94","dispense_touchTip_mmfromTop":null},"858152a0-2206-4f68-8e81-fcd095e5f0c5":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -4","stepDetails":"","id":"858152a0-2206-4f68-8e81-fcd095e5f0c5","dispense_touchTip_mmfromTop":null},"66aaa38e-6796-4e83-b4a0-1ac3baf21bec":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -5","stepDetails":"","id":"66aaa38e-6796-4e83-b4a0-1ac3baf21bec","dispense_touchTip_mmfromTop":null},"44c546a4-0adf-4136-bc67-ea1e229d2bcb":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A9"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"40","dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -6","stepDetails":"","id":"44c546a4-0adf-4136-bc67-ea1e229d2bcb","dispense_touchTip_mmfromTop":null},"3e9ea8ba-59cf-43ef-ad92-bdcdc2391c81":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -2","stepDetails":"","id":"3e9ea8ba-59cf-43ef-ad92-bdcdc2391c81","dispense_touchTip_mmfromTop":null},"17ae462d-5805-41f9-9338-1165e6047098":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -3","stepDetails":"","id":"17ae462d-5805-41f9-9338-1165e6047098","dispense_touchTip_mmfromTop":null},"83468013-38ba-433a-aeec-5e29b863d342":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -4","stepDetails":"","id":"83468013-38ba-433a-aeec-5e29b863d342","dispense_touchTip_mmfromTop":null},"7580e544-156e-4fa2-aa2a-d0508371c1df":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -5","stepDetails":"","id":"7580e544-156e-4fa2-aa2a-d0508371c1df","dispense_touchTip_mmfromTop":null},"9db25322-3c3a-4799-969c-9b435ab60949":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -6","stepDetails":"","id":"9db25322-3c3a-4799-969c-9b435ab60949","dispense_touchTip_mmfromTop":null},"de855578-88c8-4237-876b-b50ec798c900":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"445ed8b9-817e-474d-981b-62f48bb83f69:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"4da13a5d-ef01-47e2-9888-d3a165ebde75:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r media 12-7","stepDetails":"","id":"de855578-88c8-4237-876b-b50ec798c900","dispense_touchTip_mmfromTop":null},"cfe618d3-fa6b-463f-bd3c-c27aa39f2d32":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"445ed8b9-817e-474d-981b-62f48bb83f69:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"4da13a5d-ef01-47e2-9888-d3a165ebde75:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r media 12-7","stepDetails":"","id":"cfe618d3-fa6b-463f-bd3c-c27aa39f2d32","dispense_touchTip_mmfromTop":null},"a509b01d-b684-4351-987b-b1ea68435e55":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:00:01","id":"a509b01d-b684-4351-987b-b1ea68435e55","stepType":"pause","stepName":"pause","stepDetails":""},"0e3bf1de-ce07-498a-abd1-e186c9c9a603":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4da13a5d-ef01-47e2-9888-d3a165ebde75:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"90","stepType":"moveLiquid","stepName":"a opti","stepDetails":"","id":"0e3bf1de-ce07-498a-abd1-e186c9c9a603","dispense_touchTip_mmfromTop":null},"bb61a72e-3add-4c4f-b7d0-736208f8467a":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:00:01","id":"bb61a72e-3add-4c4f-b7d0-736208f8467a","stepType":"pause","stepName":"pause","stepDetails":""},"f58b1a3e-cce5-45d1-85bb-0b38ce2db18a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"445ed8b9-817e-474d-981b-62f48bb83f69:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"40","stepType":"moveLiquid","stepName":"a virus","stepDetails":"","id":"f58b1a3e-cce5-45d1-85bb-0b38ce2db18a","dispense_touchTip_mmfromTop":null},"dee826a1-7097-47c3-8b5e-eaaf351d7152":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"f7aa6016-ca85-4898-bff9-148d4be959cf:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"4da13a5d-ef01-47e2-9888-d3a165ebde75:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r media 12-7","stepDetails":"","id":"dee826a1-7097-47c3-8b5e-eaaf351d7152","dispense_touchTip_mmfromTop":null},"d2f0b48b-e5a0-46cf-aaee-0cb72f5e8a4f":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"f7aa6016-ca85-4898-bff9-148d4be959cf:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"4da13a5d-ef01-47e2-9888-d3a165ebde75:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r media 12-7","stepDetails":"","id":"d2f0b48b-e5a0-46cf-aaee-0cb72f5e8a4f","dispense_touchTip_mmfromTop":null},"34deff4c-fd75-4ac7-8af5-ea5efa141b4c":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"f7aa6016-ca85-4898-bff9-148d4be959cf:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"40","stepType":"moveLiquid","stepName":"a virus","stepDetails":"","id":"34deff4c-fd75-4ac7-8af5-ea5efa141b4c","dispense_touchTip_mmfromTop":null},"f4b787c9-dd3e-4636-822d-1f9b5d41b038":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4da13a5d-ef01-47e2-9888-d3a165ebde75:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"90","stepType":"moveLiquid","stepName":"a opti","stepDetails":"","id":"f4b787c9-dd3e-4636-822d-1f9b5d41b038","dispense_touchTip_mmfromTop":null},"c0985fcf-3553-4c34-8f98-c99d50178c34":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:00:01","id":"c0985fcf-3553-4c34-8f98-c99d50178c34","stepType":"pause","stepName":"pause","stepDetails":""},"28987327-f165-4f91-86fa-da1919e50965":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -2","stepDetails":"","id":"28987327-f165-4f91-86fa-da1919e50965","dispense_touchTip_mmfromTop":null},"4a980189-8cf7-48c0-bdb9-ba3e1aad3f70":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -2","stepDetails":"","id":"4a980189-8cf7-48c0-bdb9-ba3e1aad3f70","dispense_touchTip_mmfromTop":null},"0058b232-45f8-4906-b83d-a49500cbddc0":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -2","stepDetails":"","id":"0058b232-45f8-4906-b83d-a49500cbddc0","dispense_touchTip_mmfromTop":null},"74f344e3-9d5a-4516-953a-7018f15eb567":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -2","stepDetails":"","id":"74f344e3-9d5a-4516-953a-7018f15eb567","dispense_touchTip_mmfromTop":null},"5e021f4c-5518-4162-a135-66ad9606b549":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A7"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -2","stepDetails":"","id":"5e021f4c-5518-4162-a135-66ad9606b549","dispense_touchTip_mmfromTop":null},"79ea5b81-a54f-45e4-83a0-05e53bc50e3e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A8"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -2","stepDetails":"","id":"79ea5b81-a54f-45e4-83a0-05e53bc50e3e","dispense_touchTip_mmfromTop":null},"1f13ce25-b1ee-4b0b-af33-65e5f99ab679":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -2","stepDetails":"","id":"1f13ce25-b1ee-4b0b-af33-65e5f99ab679","dispense_touchTip_mmfromTop":null},"c35b442b-8d3a-42b8-bbec-96251930ebce":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -2","stepDetails":"","id":"c35b442b-8d3a-42b8-bbec-96251930ebce","dispense_touchTip_mmfromTop":null},"0647d38e-b326-425a-9d3d-08fe36a0d8c9":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A9"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -2","stepDetails":"","id":"0647d38e-b326-425a-9d3d-08fe36a0d8c9","dispense_touchTip_mmfromTop":null},"b1777b7f-42ae-4adf-a1a8-a11781aa6205":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":true,"aspirate_mix_times":"10","aspirate_mix_volume":"40","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"f5c33fa5-18cd-4e82-9dd8-03426e77e1c5:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"358becf5-7d09-4bc8-b8af-fdada6fde6b3","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"10","stepType":"moveLiquid","stepName":"a virus -2","stepDetails":"","id":"b1777b7f-42ae-4adf-a1a8-a11781aa6205","dispense_touchTip_mmfromTop":null},"d36fffb4-2208-4ac9-b300-b9214c7e61bc":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:00:01","id":"d36fffb4-2208-4ac9-b300-b9214c7e61bc","stepType":"pause","stepName":"pause","stepDetails":""}},"orderedStepIds":["0e3bf1de-ce07-498a-abd1-e186c9c9a603","f4b787c9-dd3e-4636-822d-1f9b5d41b038","28987327-f165-4f91-86fa-da1919e50965","0058b232-45f8-4906-b83d-a49500cbddc0","5e021f4c-5518-4162-a135-66ad9606b549","1f13ce25-b1ee-4b0b-af33-65e5f99ab679","0647d38e-b326-425a-9d3d-08fe36a0d8c9","4a980189-8cf7-48c0-bdb9-ba3e1aad3f70","74f344e3-9d5a-4516-953a-7018f15eb567","79ea5b81-a54f-45e4-83a0-05e53bc50e3e","c35b442b-8d3a-42b8-bbec-96251930ebce","b1777b7f-42ae-4adf-a1a8-a11781aa6205","bb61a72e-3add-4c4f-b7d0-736208f8467a","bf798af2-a3ef-411a-97f7-4721425d0e6a","0d903926-6ed6-4a3d-ba98-ec77137c3b94","858152a0-2206-4f68-8e81-fcd095e5f0c5","66aaa38e-6796-4e83-b4a0-1ac3baf21bec","44c546a4-0adf-4136-bc67-ea1e229d2bcb","3e9ea8ba-59cf-43ef-ad92-bdcdc2391c81","17ae462d-5805-41f9-9338-1165e6047098","83468013-38ba-433a-aeec-5e29b863d342","7580e544-156e-4fa2-aa2a-d0508371c1df","9db25322-3c3a-4799-969c-9b435ab60949","d36fffb4-2208-4ac9-b300-b9214c7e61bc","c0985fcf-3553-4c34-8f98-c99d50178c34","de855578-88c8-4237-876b-b50ec798c900","cfe618d3-fa6b-463f-bd3c-c27aa39f2d32","dee826a1-7097-47c3-8b5e-eaaf351d7152","d2f0b48b-e5a0-46cf-aaee-0cb72f5e8a4f","a509b01d-b684-4351-987b-b1ea68435e55","f58b1a3e-cce5-45d1-85bb-0b38ce2db18a","34deff4c-fd75-4ac7-8af5-ea5efa141b4c"],"pipettes":{"358becf5-7d09-4bc8-b8af-fdada6fde6b3":{"pipetteName":"p300_multi_gen2"},"f2d3d83c-9af8-42e5-ad6f-7e1f2ab0f2e5":{"pipetteName":"p300_single_gen2"}},"modules":{},"labware":{"8e31dd41-f40c-4d4c-a847-aa62cbe84695:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"},"445ed8b9-817e-474d-981b-62f48bb83f69:opentrons/nest_96_wellplate_200ul_flat/5":{"displayName":"96","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/5"},"4da13a5d-ef01-47e2-9888-d3a165ebde75:opentrons/nest_12_reservoir_15ml/3":{"displayName":"reservoir","labwareDefURI":"opentrons/nest_12_reservoir_15ml/3"},"60e8b3dd-62a4-417b-ba8e-8990cdb357c5:opentrons/nest_96_wellplate_200ul_flat/5":{"displayName":"dilution","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/5"},"f7aa6016-ca85-4898-bff9-148d4be959cf:opentrons/nest_96_wellplate_200ul_flat/5":{"displayName":"96 2","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/5"},"03b5b287-d93d-4e0b-9fd4-7876fc22dc49:opentrons/nest_96_wellplate_200ul_flat/5":{"displayName":"dillution 2","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/5"}}}},"metadata":{"protocolName":"Serial Dilution (2plates)","author":"Leonardo Giordano","description":"","created":1723219127925,"lastModified":1769020969840,"category":null,"subcategory":null,"tags":[],"source":"Protocol Designer"}}"""
