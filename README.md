# High-throughput-Flavivirus-Phenotyping

## Automated Focus-Forming Assay (FFA) Workflow on Opentrons OT-2 & Flex

## Overview

This repository contains all automation protocols

The project implements a fully automated focus-forming assay (FFA) workflow for high-throughput viral titration using the Opentrons OT-2 and Opentrons Flex liquid-handling platforms. It standardizes plate setup, serial dilutions, infection, fixation, and staining, and provides reproducible analysis scripts for titer calculation and data visualization.

**QVEU | NIH/NIAID — Methods Paper Companion Repository**

This repository contains Python protocols for running portions (or the full workflow) of our assay on **Opentrons OT-2** and **Opentrons Flex**, plus **R scripts** used for downstream data processing/plots.

The protocols are organized by robot and workflow step:
- **Serial dilution**
- **Fix**
- **Stain**
- **Full protocol**
Each workflow step includes versions for **1–4 plates**.

> [Note] These protocols are intended for research use in a controlled laboratory setting. Always verify deck layout, labware, volumes, and pipetting parameters before running on a live robot.

## Quick Start (Download the Protocols)

### 1)Choose robot
- OT-2
- Flex

### 2)Choose workflow step
-Serial Dilution
- Fix
- Stain
- Full protocol

### 3)Choose plate count (1–4 plates)

Inside each workflow step folder you’ll find plate-count-specific subfolders for 1_plate through 4_plates.

### 4)Download the .py file

Open the folder for your selection and download the Python protocol (.py).

[Tip] Name your downloaded file with date + operator initials (e.g., 2026-02-09_LG_ot2_full_3plates.py) to keep runs traceable.

### Running a Protocol in the Opentrons App (OT-2 or Flex)
Step 1 — Open the Opentrons App

Launch the Opentrons App on your computer.
