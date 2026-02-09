import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "Stain 3 plates",
    "author": "Leo",
    "created": "2024-08-05T14:28:45.837Z",
    "internalAppBuildDate": "Tue, 03 Feb 2026 18:27:38 GMT",
    "lastModified": "2026-02-09T20:43:55.474Z",
    "protocolDesigner": "8.8.0",
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
    reservoir_1 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="2",
        label="reservoir",
        namespace="opentrons",
        version=3,
    )
    well_plate_3 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="8",
        label="96",
        namespace="opentrons",
        version=5,
    )
    well_plate_1 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="9",
        label="96  2",
        namespace="opentrons",
        version=5,
    )
    reservoir_2 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="5",
        label="reservoir 2",
        namespace="opentrons",
        version=3,
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
    well_plate_2 = protocol.load_labware(
        "nest_96_wellplate_200ul_flat",
        location="7",
        label="96 3",
        namespace="opentrons",
        version=5,
    )
    reservoir_3 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="3",
        label="reservoir 3",
        namespace="opentrons",
        version=3,
    )
    reservoir_4 = protocol.load_labware(
        "nest_12_reservoir_15ml",
        location="6",
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
    liquid_8 = protocol.define_liquid(
        "Fixed cells",
        display_color="#9dffc57d",
    )

    # Load Liquids:
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
    reservoir_3.load_liquid(
        wells=["A3", "A4"],
        liquid=liquid_6,
        volume=10000,
    )
    reservoir_3.load_liquid(
        wells=["A7"],
        liquid=liquid_5,
        volume=10000,
    )
    reservoir_3.load_liquid(
        wells=["A9", "A10"],
        liquid=liquid_2,
        volume=10000,
    )
    reservoir_4.load_liquid(
        wells=["A1", "A2"],
        liquid=liquid_2,
        volume=10000,
    )
    reservoir_4.load_liquid(
        wells=["A5"],
        liquid=liquid_4,
        volume=10000,
    )
    reservoir_4.load_liquid(
        wells=["A7"],
        liquid=liquid_7,
        volume=10000,
    )

    # PROTOCOL STEPS

    # Step 1: A milk p1 (12-7)
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"]],
        dest=[well_plate_3["A12"], well_plate_3["A11"], well_plate_3["A10"], well_plate_3["A9"], well_plate_3["A8"], well_plate_3["A7"]],
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
        dest=[well_plate_3["A6"], well_plate_3["A5"], well_plate_3["A4"], well_plate_3["A3"], well_plate_3["A2"], well_plate_3["A1"]],
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
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
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
        dest=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
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

    # Step 5: A milk p1 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_3["A3"], reservoir_3["A3"], reservoir_3["A3"], reservoir_3["A3"], reservoir_3["A3"], reservoir_3["A3"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
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

    # Step 6: A milk p1 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_3["A4"], reservoir_3["A4"], reservoir_3["A4"], reservoir_3["A4"], reservoir_3["A4"], reservoir_3["A4"]],
        dest=[well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
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

    # Step 7: milk 10 min
    protocol.delay(seconds=360)

    # Step 8: r pbs p2 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        dest=[reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"], reservoir_1["A3"]],
        new_tip="never",
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

    # Step 9: r pbs p2 (6-1)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        dest=[reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"], reservoir_1["A4"]],
        new_tip="never",
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

    # Step 10: r pbs p1 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_3["A12"], well_plate_3["A11"], well_plate_3["A10"], well_plate_3["A9"], well_plate_3["A8"], well_plate_3["A7"]],
        dest=[reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"], reservoir_1["A5"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
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

    # Step 11: r pbs p1 (6-1)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_3["A6"], well_plate_3["A5"], well_plate_3["A4"], well_plate_3["A3"], well_plate_3["A2"], well_plate_3["A1"]],
        dest=[reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"], reservoir_1["A6"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_11",
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

    # Step 12: r pbs p2 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"]],
        dest=[reservoir_3["A3"], reservoir_3["A3"], reservoir_3["A3"], reservoir_3["A3"], reservoir_3["A3"], reservoir_3["A3"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_12",
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

    # Step 13: r pbs p2 (12-7)
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        dest=[reservoir_3["A4"], reservoir_3["A4"], reservoir_3["A4"], reservoir_3["A4"], reservoir_3["A4"], reservoir_3["A4"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_13",
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

    # Step 14: Add 1
    protocol.delay(seconds=1)

    # Step 15: a 1*ab p1 (12-7)
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_1["A7"]],
        dest=[well_plate_3["A12"], well_plate_3["A11"], well_plate_3["A10"], well_plate_3["A9"], well_plate_3["A8"], well_plate_3["A7"], well_plate_3["A6"], well_plate_3["A5"], well_plate_3["A4"], well_plate_3["A3"], well_plate_3["A2"], well_plate_3["A1"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_15",
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

    # Step 16: a 1*ab p2 (12-7)
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_1["A8"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"], well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_16",
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

    # Step 17: a 1*ab p1 (12-7)
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_3["A7"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"], well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_17",
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

    # Step 18: pause 2h
    protocol.delay(seconds=7200, msg="2 H")

    # Step 19: pause
    protocol.pause("REMOVE 1AB")

    # Step 20: A PBS
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"]],
        dest=[well_plate_3["A12"], well_plate_3["A11"], well_plate_3["A10"], well_plate_3["A9"], well_plate_3["A8"], well_plate_3["A7"]],
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

    # Step 21: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"]],
        dest=[well_plate_3["A6"], well_plate_3["A5"], well_plate_3["A4"], well_plate_3["A3"], well_plate_3["A2"], well_plate_3["A1"]],
        new_tip="never",
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

    # Step 22: A PBS 2
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        new_tip="never",
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

    # Step 23: A PBS 2
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"]],
        dest=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
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

    # Step 24: R pbs
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_3["A12"], well_plate_3["A11"], well_plate_3["A10"], well_plate_3["A9"], well_plate_3["A8"], well_plate_3["A7"]],
        dest=[reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"], reservoir_1["A9"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_24",
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

    # Step 25: R pbs
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_3["A6"], well_plate_3["A5"], well_plate_3["A4"], well_plate_3["A3"], well_plate_3["A2"], well_plate_3["A1"]],
        dest=[reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"], reservoir_1["A10"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_25",
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

    # Step 26: R pbs
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        dest=[reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"], reservoir_1["A11"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_26",
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

    # Step 27: R pbs
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        dest=[reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"], reservoir_1["A12"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_27",
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

    # Step 28: A PBS
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_3["A9"], reservoir_3["A9"], reservoir_3["A9"], reservoir_3["A9"], reservoir_3["A9"], reservoir_3["A9"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"]],
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

    # Step 29: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_3["A10"], reservoir_3["A10"], reservoir_3["A10"], reservoir_3["A10"], reservoir_3["A10"], reservoir_3["A10"]],
        dest=[well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
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

    # Step 30: R pbs
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"]],
        dest=[reservoir_3["A9"], reservoir_3["A9"], reservoir_3["A9"], reservoir_3["A9"], reservoir_3["A9"], reservoir_3["A9"]],
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

    # Step 31: R pbs
    pipette_left.transfer_with_liquid_class(
        volume=200,
        source=[well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        dest=[reservoir_3["A10"], reservoir_3["A10"], reservoir_3["A10"], reservoir_3["A10"], reservoir_3["A10"], reservoir_3["A10"]],
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

    # Step 32: pause
    protocol.delay(seconds=1)

    # Step 33: A 2AB
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_2["A5"]],
        dest=[well_plate_3["A12"], well_plate_3["A11"], well_plate_3["A10"], well_plate_3["A9"], well_plate_3["A8"], well_plate_3["A7"], well_plate_3["A6"], well_plate_3["A5"], well_plate_3["A4"], well_plate_3["A3"], well_plate_3["A2"], well_plate_3["A1"]],
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

    # Step 34: A 2AB
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_2["A6"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"], well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
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

    # Step 35: A 2AB
    pipette_left.distribute_with_liquid_class(
        volume=100,
        source=[reservoir_4["A5"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"], well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_35",
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

    # Step 36: pause
    protocol.delay(seconds=3600)

    # Step 37: pause
    protocol.pause("REMOVE 2AB")

    # Step 38: A PBS
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_2["A1"], reservoir_2["A1"], reservoir_2["A1"], reservoir_2["A1"], reservoir_2["A1"], reservoir_2["A1"]],
        dest=[well_plate_3["A12"], well_plate_3["A11"], well_plate_3["A10"], well_plate_3["A9"], well_plate_3["A8"], well_plate_3["A7"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_38",
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

    # Step 39: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_2["A2"], reservoir_2["A2"], reservoir_2["A2"], reservoir_2["A2"], reservoir_2["A2"], reservoir_2["A2"]],
        dest=[well_plate_3["A6"], well_plate_3["A5"], well_plate_3["A4"], well_plate_3["A3"], well_plate_3["A2"], well_plate_3["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_39",
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

    # Step 40: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_2["A3"], reservoir_2["A3"], reservoir_2["A3"], reservoir_2["A3"], reservoir_2["A3"], reservoir_2["A3"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_40",
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

    # Step 41: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_2["A4"], reservoir_2["A4"], reservoir_2["A4"], reservoir_2["A4"], reservoir_2["A4"], reservoir_2["A4"]],
        dest=[well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_41",
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

    # Step 42: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_4["A1"], reservoir_4["A1"], reservoir_4["A1"], reservoir_4["A1"], reservoir_4["A1"], reservoir_4["A1"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_42",
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

    # Step 43: A PBS
    pipette_left.transfer_with_liquid_class(
        volume=180,
        source=[reservoir_4["A2"], reservoir_4["A2"], reservoir_4["A2"], reservoir_4["A2"], reservoir_4["A2"], reservoir_4["A2"]],
        dest=[well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_43",
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

    # Step 44: pause
    protocol.pause("REMOVE PBS, tap plate and add TB to reservoir")

    # Step 45: A TB
    pipette_left.configure_nozzle_layout(
        protocol_api.ALL,
        start="A1",
    )
    pipette_left.distribute_with_liquid_class(
        volume=40,
        source=[reservoir_2["A7"]],
        dest=[well_plate_3["A12"], well_plate_3["A11"], well_plate_3["A10"], well_plate_3["A9"], well_plate_3["A8"], well_plate_3["A7"], well_plate_3["A6"], well_plate_3["A5"], well_plate_3["A4"], well_plate_3["A3"], well_plate_3["A2"], well_plate_3["A1"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_45",
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

    # Step 46: A TB
    pipette_left.distribute_with_liquid_class(
        volume=40,
        source=[reservoir_2["A7"]],
        dest=[well_plate_1["A12"], well_plate_1["A11"], well_plate_1["A10"], well_plate_1["A9"], well_plate_1["A8"], well_plate_1["A7"], well_plate_1["A6"], well_plate_1["A5"], well_plate_1["A4"], well_plate_1["A3"], well_plate_1["A2"], well_plate_1["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_46",
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

    # Step 47: A TB
    pipette_left.distribute_with_liquid_class(
        volume=40,
        source=[reservoir_4["A7"]],
        dest=[well_plate_2["A12"], well_plate_2["A11"], well_plate_2["A10"], well_plate_2["A9"], well_plate_2["A8"], well_plate_2["A7"], well_plate_2["A6"], well_plate_2["A5"], well_plate_2["A4"], well_plate_2["A3"], well_plate_2["A2"], well_plate_2["A1"]],
        new_tip="never",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        group_wells=False,
        tip_racks=[tip_rack_1, tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="distribute_step_47",
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

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.8.0","data":{"pipetteTiprackAssignments":{"806347f5-d454-4feb-9ba3-2fe5d0376a65":["opentrons/opentrons_96_filtertiprack_200ul/1"]},"dismissedWarnings":{"form":["BELOW_MIN_DISPOSAL_VOLUME"],"timeline":["ASPIRATE_MORE_THAN_WELL_CONTENTS","ASPIRATE_FROM_PRISTINE_WELL"]},"ingredients":{"0":{"displayName":"Methylcellulose","description":null,"displayColor":"#b925ff","liquidGroupId":"0","liquidClass":null},"1":{"displayName":"PBS","description":null,"displayColor":"#9dffd8","liquidGroupId":"1","liquidClass":null},"2":{"displayName":"MeOH","description":null,"displayColor":"#50d5ff","liquidGroupId":"2","liquidClass":null},"3":{"displayName":"2Ab","description":null,"displayColor":"#ff9900","liquidGroupId":"3","liquidClass":null},"4":{"displayName":"1*AB","description":null,"displayColor":"#ff80f5","liquidGroupId":"4","liquidClass":null},"5":{"displayName":"MILK","description":null,"displayColor":"#c2af4eff","liquidGroupId":"5","liquidClass":null},"6":{"displayName":"TB","description":null,"displayColor":"#087aa1ff","liquidGroupId":"6","liquidClass":null},"7":{"displayName":"Fixed cells","displayColor":"#9dffc57d","description":null,"liquidGroupId":"7"}},"ingredLocations":{"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3":{"A3":{"5":{"volume":10000}},"A4":{"5":{"volume":10000}},"A5":{"5":{"volume":10000}},"A6":{"5":{"volume":10000}},"A7":{"4":{"volume":10000}},"A8":{"4":{"volume":10000}},"A9":{"1":{"volume":10000}},"A10":{"1":{"volume":10000}},"A11":{"1":{"volume":10000}},"A12":{"1":{"volume":10000}}},"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/3":{"A1":{"1":{"volume":10000}},"A2":{"1":{"volume":10000}},"A3":{"1":{"volume":10000}},"A4":{"1":{"volume":10000}},"A5":{"3":{"volume":10000}},"A6":{"3":{"volume":10000}},"A7":{"6":{"volume":10000}}},"adfb4b92-d977-4694-8181-dfd2387673fa:opentrons/opentrons_96_filtertiprack_200ul/1":{},"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3":{"A3":{"5":{"volume":10000}},"A4":{"5":{"volume":10000}},"A7":{"4":{"volume":10000}},"A9":{"1":{"volume":10000}},"A10":{"1":{"volume":10000}}},"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3":{"A1":{"1":{"volume":10000}},"A2":{"1":{"volume":10000}},"A5":{"3":{"volume":10000}},"A7":{"6":{"volume":10000}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"labwareLocationUpdate":{"bb063119-315e-4ac6-b4c7-088a6e688445:opentrons/opentrons_96_filtertiprack_200ul/1":"1","b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3":"2","aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5":"8","72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5":"9","4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/3":"5","adfb4b92-d977-4694-8181-dfd2387673fa:opentrons/opentrons_96_filtertiprack_200ul/1":"4","3f275f2a-19a4-4ba1-8219-afd1a3d38c3a:opentrons/opentrons_96_filtertiprack_200ul/1":"offDeck","90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5":"7","33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3":"3","5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3":"6"},"moduleLocationUpdate":{},"pipetteLocationUpdate":{"806347f5-d454-4feb-9ba3-2fe5d0376a65":"left"},"trashBinLocationUpdate":{"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin":"cutout12"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{},"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__","moduleStateUpdate":{}},"2ceb731e-92ed-4cf4-872c-4d712ec84ce1":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A milk p1 (12-7)","stepDetails":"","id":"2ceb731e-92ed-4cf4-872c-4d712ec84ce1","dispense_touchTip_mmfromTop":null},"49d3ae38-ea8e-403a-bb20-4b1103e0162b":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A milk p1 (6-1)","stepDetails":"","id":"49d3ae38-ea8e-403a-bb20-4b1103e0162b","dispense_touchTip_mmfromTop":null},"d220fa8a-ea43-4887-b7d3-1ee2e996b13a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A5"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r pbs p1 (12-7)","stepDetails":"","id":"d220fa8a-ea43-4887-b7d3-1ee2e996b13a","dispense_touchTip_mmfromTop":null},"0793860d-6e42-4a46-89b0-70e77d0df829":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r pbs p1 (6-1)","stepDetails":"","id":"0793860d-6e42-4a46-89b0-70e77d0df829","dispense_touchTip_mmfromTop":null},"2f64dd5c-ea74-4bad-bf08-ef7f52f5e94e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"a 1*ab p1 (12-7)","stepDetails":"","id":"2f64dd5c-ea74-4bad-bf08-ef7f52f5e94e","dispense_touchTip_mmfromTop":null},"60b29e21-d461-4511-8ffd-50f337667cd4":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"2 H","pauseTemperature":null,"pauseTime":"02:00:00","id":"60b29e21-d461-4511-8ffd-50f337667cd4","stepType":"pause","stepName":"pause 2h","stepDetails":""},"c18f9f3d-2d7e-41c9-891d-e4dd81eebff1":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A milk p2 (12-7)","stepDetails":"","id":"c18f9f3d-2d7e-41c9-891d-e4dd81eebff1","dispense_touchTip_mmfromTop":null},"f714fb9e-ef77-4f15-8380-43fa2e256b11":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A milk p2 (6-1)","stepDetails":"","id":"f714fb9e-ef77-4f15-8380-43fa2e256b11","dispense_touchTip_mmfromTop":null},"b8042302-fd37-4ad1-b6bd-1cc771c33bc1":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:6:00","id":"b8042302-fd37-4ad1-b6bd-1cc771c33bc1","stepType":"pause","stepName":"milk 10 min","stepDetails":""},"32a1f55d-36ff-478a-b3cd-632b5577be30":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:00:01","id":"32a1f55d-36ff-478a-b3cd-632b5577be30","stepType":"pause","stepName":"Add 1","stepDetails":""},"c6484da0-18ce-49b0-ae5b-98aa22510d26":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r pbs p2 (12-7)","stepDetails":"","id":"c6484da0-18ce-49b0-ae5b-98aa22510d26","dispense_touchTip_mmfromTop":null},"731a35dd-aa0d-40f2-8f51-8159c3515a02":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r pbs p2 (6-1)","stepDetails":"","id":"731a35dd-aa0d-40f2-8f51-8159c3515a02","dispense_touchTip_mmfromTop":null},"0f96cd6e-5321-49c0-a987-b90d58eb594a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A8"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"a 1*ab p2 (12-7)","stepDetails":"","id":"0f96cd6e-5321-49c0-a987-b90d58eb594a","dispense_touchTip_mmfromTop":null},"469c2ccb-4317-45ef-87ed-9afe7c849c2a":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"REMOVE 1AB","pauseTemperature":null,"pauseTime":null,"id":"469c2ccb-4317-45ef-87ed-9afe7c849c2a","stepType":"pause","stepName":"pause","stepDetails":""},"17f896cf-f9b8-4cb6-8e41-62bc4586f335":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A9"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"17f896cf-f9b8-4cb6-8e41-62bc4586f335","dispense_touchTip_mmfromTop":null},"ec6ddbcd-5220-438f-9151-23e3c1483c0e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"ec6ddbcd-5220-438f-9151-23e3c1483c0e","dispense_touchTip_mmfromTop":null},"0bea0a5d-5d60-4da4-8a9c-c8b690b0dff4":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"R pbs","stepDetails":"","id":"0bea0a5d-5d60-4da4-8a9c-c8b690b0dff4","dispense_touchTip_mmfromTop":null},"078bf96f-87b6-4e58-8e01-ace4b64e3d54":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A11"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS 2","stepDetails":"","id":"078bf96f-87b6-4e58-8e01-ace4b64e3d54","dispense_touchTip_mmfromTop":null},"a26f3873-489d-4fe5-9710-151872d015cc":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS 2","stepDetails":"","id":"a26f3873-489d-4fe5-9710-151872d015cc","dispense_touchTip_mmfromTop":null},"919f6513-7dfe-49b3-a384-9957d978a1be":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"R pbs","stepDetails":"","id":"919f6513-7dfe-49b3-a384-9957d978a1be","dispense_touchTip_mmfromTop":null},"07ac41ec-152d-4223-9071-51a17bc9bd54":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A11"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"R pbs","stepDetails":"","id":"07ac41ec-152d-4223-9071-51a17bc9bd54","dispense_touchTip_mmfromTop":null},"3de37394-3004-4d95-90e6-efc9240ccade":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"R pbs","stepDetails":"","id":"3de37394-3004-4d95-90e6-efc9240ccade","dispense_touchTip_mmfromTop":null},"6831f4cd-0aa0-45c2-bb3a-49c02e518779":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"00:00:01","id":"6831f4cd-0aa0-45c2-bb3a-49c02e518779","stepType":"pause","stepName":"pause","stepDetails":""},"2a90bf3c-f3a1-472c-9194-d264720fc559":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"A 2AB","stepDetails":"","id":"2a90bf3c-f3a1-472c-9194-d264720fc559","dispense_touchTip_mmfromTop":null},"1dacc88a-29b0-4e6b-8fe3-8002fd1a0f24":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"A 2AB","stepDetails":"","id":"1dacc88a-29b0-4e6b-8fe3-8002fd1a0f24","dispense_touchTip_mmfromTop":null},"415e5cef-9ba6-4484-b662-98421f812778":{"moduleId":null,"pauseAction":"untilTime","pauseMessage":"","pauseTemperature":null,"pauseTime":"01:00:00","id":"415e5cef-9ba6-4484-b662-98421f812778","stepType":"pause","stepName":"pause","stepDetails":""},"45806cd0-1338-4947-974c-fac49754b3fc":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"REMOVE 2AB","pauseTemperature":null,"pauseTime":null,"id":"45806cd0-1338-4947-974c-fac49754b3fc","stepType":"pause","stepName":"pause","stepDetails":""},"0b5680ec-887a-458d-9eda-ca80bb37db6a":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"0b5680ec-887a-458d-9eda-ca80bb37db6a","dispense_touchTip_mmfromTop":null},"b26ea0fa-914b-44b7-b771-e4e22cdba863":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"b26ea0fa-914b-44b7-b771-e4e22cdba863","dispense_touchTip_mmfromTop":null},"c86fe629-66e2-4711-8119-d0cd33bccf38":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"c86fe629-66e2-4711-8119-d0cd33bccf38","dispense_touchTip_mmfromTop":null},"3cdce018-c674-4234-a558-c11e3a7a5592":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"3cdce018-c674-4234-a558-c11e3a7a5592","dispense_touchTip_mmfromTop":null},"b850c02f-4a88-46f1-ba5b-f0719c978a92":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"REMOVE PBS, tap plate and add TB to reservoir","pauseTemperature":null,"pauseTime":null,"id":"b850c02f-4a88-46f1-ba5b-f0719c978a92","stepType":"pause","stepName":"pause","stepDetails":""},"77e800af-5eb9-46a5-bc7a-cd1a5b7ceaf8":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":8,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"40","stepType":"moveLiquid","stepName":"A TB","stepDetails":"","id":"77e800af-5eb9-46a5-bc7a-cd1a5b7ceaf8","dispense_touchTip_mmfromTop":null},"d6cc0380-f2fe-42c4-bc97-13b02699fa4f":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"40","stepType":"moveLiquid","stepName":"A TB","stepDetails":"","id":"d6cc0380-f2fe-42c4-bc97-13b02699fa4f","dispense_touchTip_mmfromTop":null},"45695b79-bcc7-44b5-a329-2cf8df861591":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A milk p1 (12-7)","stepDetails":"","id":"45695b79-bcc7-44b5-a329-2cf8df861591","dispense_touchTip_mmfromTop":null},"80d9ebad-f5af-416f-87bd-16809c8abf23":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A milk p1 (12-7)","stepDetails":"","id":"80d9ebad-f5af-416f-87bd-16809c8abf23","dispense_touchTip_mmfromTop":null},"02957744-6cb7-43d2-bb57-3e3ddafbd5b1":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r pbs p2 (12-7)","stepDetails":"","id":"02957744-6cb7-43d2-bb57-3e3ddafbd5b1","dispense_touchTip_mmfromTop":null},"6958c417-d868-45d9-bded-d8bf7e723411":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"r pbs p2 (12-7)","stepDetails":"","id":"6958c417-d868-45d9-bded-d8bf7e723411","dispense_touchTip_mmfromTop":null},"e4704cad-3712-42d1-b2d1-bddb9749b2a4":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"a 1*ab p1 (12-7)","stepDetails":"","id":"e4704cad-3712-42d1-b2d1-bddb9749b2a4","dispense_touchTip_mmfromTop":null},"8faf1f3e-a3f9-435f-b118-e71fd2d7ef24":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A9"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"8faf1f3e-a3f9-435f-b118-e71fd2d7ef24","dispense_touchTip_mmfromTop":null},"8d7c8848-40a9-43f0-9a5b-fe2152257f85":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A10"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"8d7c8848-40a9-43f0-9a5b-fe2152257f85","dispense_touchTip_mmfromTop":null},"f374a329-a282-42a8-86fb-7d1bd25dd933":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A7","A8","A9","A10","A11","A12"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A9"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"R pbs","stepDetails":"","id":"f374a329-a282-42a8-86fb-7d1bd25dd933","dispense_touchTip_mmfromTop":null},"a1ca55f7-7379-4270-9fba-6d9007e25d14":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":50,"aspirate_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","aspirate_mix_checkbox":false,"aspirate_mix_times":"2","aspirate_mix_volume":"150","aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"r2l","aspirate_wellOrder_second":"t2b","aspirate_wells_grouped":false,"aspirate_wells":["A1","A2","A3","A4","A5","A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":94,"dispense_labware":"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A10"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":"20","dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"200","stepType":"moveLiquid","stepName":"R pbs","stepDetails":"","id":"a1ca55f7-7379-4270-9fba-6d9007e25d14","dispense_touchTip_mmfromTop":null},"075ea641-d5ac-4381-ad71-bfdf7063710e":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"100","stepType":"moveLiquid","stepName":"A 2AB","stepDetails":"","id":"075ea641-d5ac-4381-ad71-bfdf7063710e","dispense_touchTip_mmfromTop":null},"d490d2e2-2aab-4f10-befc-96294ca25de9":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"d490d2e2-2aab-4f10-befc-96294ca25de9","dispense_touchTip_mmfromTop":null},"4a426d2a-9304-42be-bdf3-319de14f44b5":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"single","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"180","stepType":"moveLiquid","stepName":"A PBS","stepDetails":"","id":"4a426d2a-9304-42be-bdf3-319de14f44b5","dispense_touchTip_mmfromTop":null},"ffd8d4cd-b763-4f80-aa29-e6a874094542":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":"20","aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":94,"aspirate_labware":"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A7"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":94,"blowout_location":null,"changeTip":"never","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":"20","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":50,"dispense_labware":"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"r2l","dispense_wellOrder_second":"t2b","dispense_wells":["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":false,"disposalVolume_volume":null,"dropTip_location":"334d7aaa-8d17-48d0-9755-887a4c4df952:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":"ALL","path":"multiDispense","pipette":"806347f5-d454-4feb-9ba3-2fe5d0376a65","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","tip_tracking":"automatic","tiprack_selected":null,"tips_selected":[],"volume":"40","stepType":"moveLiquid","stepName":"A TB","stepDetails":"","id":"ffd8d4cd-b763-4f80-aa29-e6a874094542","dispense_touchTip_mmfromTop":null}},"orderedStepIds":["2ceb731e-92ed-4cf4-872c-4d712ec84ce1","49d3ae38-ea8e-403a-bb20-4b1103e0162b","c18f9f3d-2d7e-41c9-891d-e4dd81eebff1","f714fb9e-ef77-4f15-8380-43fa2e256b11","45695b79-bcc7-44b5-a329-2cf8df861591","80d9ebad-f5af-416f-87bd-16809c8abf23","b8042302-fd37-4ad1-b6bd-1cc771c33bc1","c6484da0-18ce-49b0-ae5b-98aa22510d26","731a35dd-aa0d-40f2-8f51-8159c3515a02","d220fa8a-ea43-4887-b7d3-1ee2e996b13a","0793860d-6e42-4a46-89b0-70e77d0df829","02957744-6cb7-43d2-bb57-3e3ddafbd5b1","6958c417-d868-45d9-bded-d8bf7e723411","32a1f55d-36ff-478a-b3cd-632b5577be30","2f64dd5c-ea74-4bad-bf08-ef7f52f5e94e","0f96cd6e-5321-49c0-a987-b90d58eb594a","e4704cad-3712-42d1-b2d1-bddb9749b2a4","60b29e21-d461-4511-8ffd-50f337667cd4","469c2ccb-4317-45ef-87ed-9afe7c849c2a","17f896cf-f9b8-4cb6-8e41-62bc4586f335","ec6ddbcd-5220-438f-9151-23e3c1483c0e","078bf96f-87b6-4e58-8e01-ace4b64e3d54","a26f3873-489d-4fe5-9710-151872d015cc","0bea0a5d-5d60-4da4-8a9c-c8b690b0dff4","919f6513-7dfe-49b3-a384-9957d978a1be","07ac41ec-152d-4223-9071-51a17bc9bd54","3de37394-3004-4d95-90e6-efc9240ccade","8faf1f3e-a3f9-435f-b118-e71fd2d7ef24","8d7c8848-40a9-43f0-9a5b-fe2152257f85","f374a329-a282-42a8-86fb-7d1bd25dd933","a1ca55f7-7379-4270-9fba-6d9007e25d14","6831f4cd-0aa0-45c2-bb3a-49c02e518779","2a90bf3c-f3a1-472c-9194-d264720fc559","1dacc88a-29b0-4e6b-8fe3-8002fd1a0f24","075ea641-d5ac-4381-ad71-bfdf7063710e","415e5cef-9ba6-4484-b662-98421f812778","45806cd0-1338-4947-974c-fac49754b3fc","0b5680ec-887a-458d-9eda-ca80bb37db6a","b26ea0fa-914b-44b7-b771-e4e22cdba863","c86fe629-66e2-4711-8119-d0cd33bccf38","3cdce018-c674-4234-a558-c11e3a7a5592","d490d2e2-2aab-4f10-befc-96294ca25de9","4a426d2a-9304-42be-bdf3-319de14f44b5","b850c02f-4a88-46f1-ba5b-f0719c978a92","77e800af-5eb9-46a5-bc7a-cd1a5b7ceaf8","d6cc0380-f2fe-42c4-bc97-13b02699fa4f","ffd8d4cd-b763-4f80-aa29-e6a874094542"],"pipettes":{"806347f5-d454-4feb-9ba3-2fe5d0376a65":{"pipetteName":"p300_multi_gen2"}},"modules":{},"labware":{"bb063119-315e-4ac6-b4c7-088a6e688445:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"},"b645cbf3-fc3f-45ac-8b3e-62d8885b0e13:opentrons/nest_12_reservoir_15ml/3":{"displayName":"reservoir","labwareDefURI":"opentrons/nest_12_reservoir_15ml/3"},"aa60830d-b6c5-465f-ac90-76b60464e6a9:opentrons/nest_96_wellplate_200ul_flat/5":{"displayName":"96","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/5"},"72621de0-8459-40fe-b250-8af1d1b575dd:opentrons/nest_96_wellplate_200ul_flat/5":{"displayName":"96  2","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/5"},"4f0ed734-2804-49f3-bf62-70008fb7372a:opentrons/nest_12_reservoir_15ml/3":{"displayName":"reservoir 2","labwareDefURI":"opentrons/nest_12_reservoir_15ml/3"},"adfb4b92-d977-4694-8181-dfd2387673fa:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL (1)","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"},"3f275f2a-19a4-4ba1-8219-afd1a3d38c3a:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL (3)","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"},"90939678-2606-4f9f-a482-6d9d7551b318:opentrons/nest_96_wellplate_200ul_flat/5":{"displayName":"96 3","labwareDefURI":"opentrons/nest_96_wellplate_200ul_flat/5"},"33e593c7-5711-489c-b8c6-47a73e8b7050:opentrons/nest_12_reservoir_15ml/3":{"displayName":"reservoir 3","labwareDefURI":"opentrons/nest_12_reservoir_15ml/3"},"5fa2eb91-ec07-402c-853a-953f9828f389:opentrons/nest_12_reservoir_15ml/3":{"displayName":"reservoir 4","labwareDefURI":"opentrons/nest_12_reservoir_15ml/3"}}}},"metadata":{"protocolName":"Stain 3 plates","author":"Leo","description":"","created":1722868125837,"lastModified":1770669835474,"category":null,"subcategory":null,"tags":[],"source":"Protocol Designer"}}"""
