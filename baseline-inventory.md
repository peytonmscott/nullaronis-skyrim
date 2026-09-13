# NGVO Baseline Inventory

Captured from `D:\NullaroniModlist` without modifying the installation.

## Installation

- NGVO package: `NGVO 7.2.1.1` from the Wabbajack log
- Wabbajack: `4.2.3.0`
- MO2: `2.5.2`
- MO2 profile: `Default`
- MO2 game path: `D:\NullaroniModlist\Stock Game`
- Steam source game: `D:\SteamLibrary\steamapps\common\Skyrim Special Edition`
- Modlist manifest: `GhoulifiedReality_@@_NGVO.wabbajack`
- Required runtime: Skyrim AE `1.6.1170`, English Steam edition
- Root handling: Root Builder and Stock Game

## Counts

- Enabled MO2 left-pane entries: 1,413 entries beginning with `+`
- Mod directories: 1,466
- Active plugins: 450 entries beginning with `*` in `plugins.txt`
- Load-order entries: 531, including masters and Creation Club content
- Archives listed by MO2: 171

These counts include separators, outputs, framework files, official masters,
Creation Club content, and generated files where applicable. They are inventory
counts, not a claim that every entry is a gameplay mod.

## Visual Foundation

- Cabbage ENB
- NAT ENB weather plugin and NAT-related compatibility files
- Lux, Lux Orbis, and Lux Via
- Water for ENB and Natural Waterfalls
- Vanaheimr Landscapes and Vanaheimr mines/caves
- Nature of the Wild Lands, Nature of the Mild Lands downscaler, and grass
  systems
- Northern Roads with a large patch collection
- Better Dynamic Snow, parallax mesh/material systems, Terrain Helper, and ERM
- Extensive ENB particle-light and effect-light stack
- Untarnished UI, SkyUI, TrueHUD, moreHUD, STB Widgets, SmoothCam, TDM, and
  extensive OAR/Pandora animation infrastructure
- Extensive city/interior visual edits for Windhelm, Solitude, Riften,
  Markarth, Whiterun, Winterhold, Solstheim, Dawnguard, and other locations

## Generated Outputs

Existing output mods include:

- `NGVO - DynDOLOD Output`
- `NGVO - TexGen Output`
- `NGVO - Grass Cache`
- `NGVO - xLodGen Output`
- `NGVO - Pandora Output`
- `NGVO - Synthesis Output`
- `NGVO - xEdit Output`
- `NGVO - BodySlide Output`
- `PGPatcher_Output`
- `NGVO - MCM and INI Settings`

MO2 custom-overwrite routing sends Pandora, Synthesis, xEdit, and BodySlide
outputs into their named output mods. Do not regenerate them until worldspaces,
quest locations, and the final animation stack are locked.

## Existing Gameplay and Framework Systems

- TDM and related third-person targeting fixes
- FNIS marker plugin, Pandora Behaviour Engine Plus, OAR, AMR, BDI, and Payload
  Interpreter
- XPMSSE, Simple Dual Sheath, Immersive Equipment Displays, HDT-SMP
- TrueHUD, STB Widgets, Oxygen Meter 2, Detection Meter, moreHUD, SkyHUD,
  Inventory Interface Information Injector, and Casting Bar
- Security Overhaul SKSE lock systems
- Dynamic Things Alternative, SPID/KID/FLM, SkyPatcher, Container frameworks,
  and multiple script/DLL utility systems
- No full survival framework currently selected
- No NFF, Inigo, Lucien, Skyrim Unbound Reborn, LOTD, SunHelm, or horse
  management framework detected in the active baseline
- No Simonrim core, Artificer, Sorcerer, or ArteFakes mod directory detected

## Existing Artifact and Staff Visuals

NGVO already contains many artifact/staff model or visual changes, including
Praedy's Staves AIO, weapon animation/replacer files, JS Unique Utopia items,
Chillrend, Rueful Axe, Spellbreaker, Dawnbreaker, Volendrung, Mace of Molag
Bal, Goldbrand, Sanguine Rose, Katria's Bow, and many ENB-light patches.

This makes Artificer plus ArteFakes a high-risk Phase 1 area. Artificer must
own gameplay records, while ArteFakes must own only intentional model/visual
paths. Existing visual records and all relevant NGVO patches require xEdit
review.

## Root and Tooling

- Root Builder plugin is installed in MO2.
- Stock Game is used as the effective game path.
- MO2 custom tools include SKSE, Creation Kit, xEdit, Synthesis, xLODGen,
  TexGen, DynDOLOD, EasyNPC, BodySlide, Pandora, LOOT, PGPatcher, VRAMr, and
  other asset tools.
- MO2 routes generated tools to named output mods as documented in
  `profiles\Default\settings.ini`.

## Baseline Limitations

- Exact individual SKSE DLL version metadata still needs an automated file
  inventory with PE version fields or mod `meta.ini` extraction.
- Exact ENB binary file version must be recorded from the installed Root Builder
  files, not inferred from the archive filename.
- Creation Club plugin versions are runtime/game-source facts and must be
  recorded from the installed Stock Game files.
- No Phase 1 additions have been installed.

## Runtime Verification Update

- `Stock Game\SkyrimSE.exe`: file version `1.6.1170.0`
- `skse64_loader.exe`: file version `0.2.2.6`
- Source Creation Kit: `D:\SteamLibrary\steamapps\common\Skyrim Special Edition\CreationKit.exe`, file version `1.7.99.0`
- Stock Game Creation Kit: not currently present
- Active mod-provided SKSE DLL files discovered: 208, including duplicate
  providers where MO2 conflict rules select one winner

The Wabbajack install completed successfully on 2026-09-13 (~00:25): the final
attempt validated `Missing 0 archives` and ended with `Finished Installation`.
Effective runtime is the Stock Game copy: `SkyrimSE.exe` file version
`1.6.1170.0`, rewritten by the successful run, matching the NGVO README's
`1.6.1170` requirement. The Steam source game has drifted to `1.7.104.0`
(build 24914197); it is bypassed because MO2 launches the Stock Game copy.
The installed Creation Kit reports file version `1.7.99.0` with all support
files present; its files validated as game-file sources. `CreationKit.exe`
is intentionally not deployed into Stock Game (source-only input). Do not
manually copy CK or Papyrus files into Stock Game. Disable Steam auto-updates
for Skyrim so the source copy cannot drift further.

## Post-Install Repair 2026-09-13

The successful Wabbajack run left `Stock Game\Data` without the 159 vanilla
Creation Club files (all `cc*.esm/esl/bsa` pairs) and without the vanilla
`DialogueViews/` and `Source/` folders, because the Steam source game was still
downloading that content while Wabbajack synced Stock Game. The result was a
reproducible `std::invalid_argument / invalid stoull argument` crash ~85s
after launch at the main menu: the plugin list and `Skyrim.ccc` reference 75
CC plugins whose files were absent. Fix applied: byte-identical copy of the
159 missing root files plus `DialogueViews/` (1,795 files) and `Source/`
(14,302 files) from the Steam source `Data` folder into `Stock Game\Data`.
Verified after copy: all 75 `Skyrim.ccc` entries present, root file counts
match (174 = 174). `ShaderCache/` was intentionally not copied (regenerable).
