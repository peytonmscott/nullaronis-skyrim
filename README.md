# Nullaroni's Skyrim

Nullaroni's Skyrim is a Skyrim Anniversary Edition modlist built on the NGVO
visual foundation. It is designed for bright, natural native-4K visuals with
Cabbage ENB, enhanced landscapes, cities, lighting, weather, audio, NPCs,
animations, and generated LOD.

The planned expansion adds Simonrim gameplay, survival, combat, followers,
alternate starts, factions, quests, Legacy of the Dragonborn, and a restrained
living world. NPCs should follow believable routines, roads should contain
varied activity without constant combat, and towns should feel inhabited
without becoming overcrowded.

## Current State

The repository currently documents the NGVO baseline. The compiled baseline
package is not stored here because Wabbajack archives, downloaded mod files,
and generated binary outputs should not be committed to GitHub.

- Skyrim AE runtime: `1.6.1170`
- NGVO baseline: `7.2.1.1`
- Wabbajack: `4.2.3.0`
- MO2: `2.5.2`
- Target: stable 60 FPS at native 4K

## Build Order

1. Baseline inventory and runtime verification
2. Simonrim, Artificer, Sorcerer, and ArteFakes
3. Core utility, survival, combat, follower, horse, and alternate-start systems
4. Living-world schedules, dialogue, encounters, patrols, inns, and ecology
5. LOTD, factions, quests, and individually gated new lands
6. Conflict resolution, generated outputs, testing, and Wabbajack packaging

The authoritative specification is `outline.md`. Installation is gated by the
compatibility and testing requirements in that document.

## Repository Contents

- `outline.md`: authoritative modlist specification
- `baseline-inventory.md`: installed NGVO inventory and runtime findings
- `NGVO.compiler_settings`: Wabbajack compiler configuration
- `Nullaronis.webp`: Wabbajack cover image
