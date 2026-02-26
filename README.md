# Automated Virus Infectivity Quantification

**QVEU | NIH/NIAID — AVIQ Repository**

This repository contains Python protocols for running portions (or the full workflow) of our assay on **Opentrons OT-2** and **Opentrons Flex**, plus **R scripts** used for downstream data processing/plots.

The protocols are organized by robot and workflow step:

- **Serial dilution**
- **Fix**
- **Stain**
- **Full protocol**

Each workflow step includes versions for **1–4 plates**.

> [Note] These protocols are intended for research use in a controlled laboratory setting. Always verify deck layout, labware, volumes, and pipetting parameters before running on a live robot.

## Downloading the Protocols

### 1) Choose robot
- OT-2
- Flex

### 2) Choose workflow step
- Serial Dilution
- Fix
- Stain
- Full protocol

### 3) Choose plate count (1–4 plates)

Inside each workflow step folder you’ll find plate-count-specific subfolders for 1_plate through 4_plates.

### 4) Download the .py file

Open the folder for your selection and download the Python protocol (.py).

> [Tip] Name your downloaded file with date + operator initials (e.g., 2026-02-09_LG_ot2_full_3plates.py) to keep runs traceable.

## Running a Protocol in the Opentrons App (OT-2 or Flex)

### 1) Open the Opentrons App

- Launch the Opentrons App on your computer.

### 2) Connect to the robot

- Power on robot.

- Ensure robot is on the same network (Ethernet/Wi-Fi as appropriate).

- In the Opentrons App, select your robot from the device list.

> [Note] If the robot doesn’t appear, verify network connection and that the robot is fully booted.

### 3) Upload the protocol

- In the Opentrons App, select Protocols.

- Click Upload and choose the .py protocol you downloaded.

### 4) Review the deck layout

- The App will display the deck map / labware placements.

Confirm every item matches your physical setup:

- Plates (type + position)

- Reservoirs

- Tip racks

### 5) Confirm pipettes and calibrations

- Verify installed pipettes match the protocol’s.

- Confirm calibration status:

- Pipette calibration

- Labware offset calibration

- Deck calibration (especially after service/moves)

> [Tip] If you recently swapped pipettes or moved the robot, re-check calibration before running anything with plates!!!

### 6) Start the run

- Load reagents as prompted.

- Click Run.

- Monitor the first ~5 minutes closely.

> [Tip] Most avoidable errors happen early (wrong tip rack, wrong reservoir well, plate flipped orientation, etc.).
