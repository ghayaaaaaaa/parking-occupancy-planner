# Parking Occupancy Planner

A local Python CLI that summarizes fictional parking-lot capacity and identifies zones with available spaces. It uses a static synthetic snapshot and does not connect to cameras, sensors, license plates, or live parking systems.

## Run

Use Python 3.11 or newer from this directory:

```bash
python -m parking_planner
```

## Features

- Validates capacity and occupied-space counts.
- Reports availability by synthetic zone.
- Selects a suggested zone for review using a clear, deterministic rule.
- Uses only Python's standard library.

## Provenance and limits

This AI-assisted portfolio demo is inspired by a parking-occupancy project theme in a folder supplied by Ghaya. No original images, model weights, or datasets are included. The sample is not computer vision and does not represent live availability. No production deployment or model-training claim is made. No open-source license is included.
