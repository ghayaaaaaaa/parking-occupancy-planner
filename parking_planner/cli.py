"""Summarize a fictional parking snapshot without sensor access."""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class LotSnapshot:
    lot_id: str
    zone: str
    capacity: int
    occupied: int

    @property
    def available(self) -> int:
        return self.capacity - self.occupied


SAMPLE_SNAPSHOT = (
    LotSnapshot("lot-a", "North", 80, 61),
    LotSnapshot("lot-b", "North", 50, 24),
    LotSnapshot("lot-c", "Central", 70, 63),
    LotSnapshot("lot-d", "South", 45, 18),
)


def summarize(lots: tuple[LotSnapshot, ...]) -> list[dict[str, int | str | float]]:
    if not lots:
        raise ValueError("At least one lot is required.")
    zones: dict[str, list[LotSnapshot]] = defaultdict(list)
    seen_ids: set[str] = set()
    for lot in lots:
        if not lot.lot_id.strip() or not lot.zone.strip():
            raise ValueError("Lot identifiers and zones must not be empty.")
        if lot.lot_id in seen_ids:
            raise ValueError("Lot identifiers must be unique.")
        if lot.capacity <= 0 or not 0 <= lot.occupied <= lot.capacity:
            raise ValueError("Capacity must be positive and occupancy within capacity.")
        seen_ids.add(lot.lot_id)
        zones[lot.zone].append(lot)
    rows = []
    for zone, zone_lots in sorted(zones.items()):
        capacity = sum(lot.capacity for lot in zone_lots)
        available = sum(lot.available for lot in zone_lots)
        rows.append(
            {
                "zone": zone,
                "lots": len(zone_lots),
                "capacity": capacity,
                "available": available,
                "availability_rate": available / capacity,
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize a fictional parking snapshot.")
    parser.parse_args()
    rows = summarize(SAMPLE_SNAPSHOT)
    for row in rows:
        print(
            f"{row['zone']}: {row['available']}/{row['capacity']} available "
            f"across {row['lots']} lots ({row['availability_rate']:.0%})"
        )
    best = max(rows, key=lambda row: (row["availability_rate"], row["available"], row["zone"]))
    print(f"Suggested zone for review: {best['zone']} (synthetic snapshot)")


if __name__ == "__main__":
    main()
