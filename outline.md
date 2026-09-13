# Skyrim AE / NGVO Expansion Modlist Implementation Specification

Build a Wabbajack-ready Skyrim AE modlist using the installed current NGVO
Wabbajack list as the visual foundation.

This document defines what to evaluate and add. Do not blindly install every
candidate. Inventory NGVO first, verify exact compatibility, and report anything
that cannot be verified.

## 1. Technical baseline

- Skyrim Special Edition with Anniversary Edition upgrade and AE Creation Club
  content
- Use the exact current Steam AE runtime supported by the installed NGVO build
- Mod Organizer 2
- Wabbajack-first workflow
- New-game-only modlist
- Target hardware:
  - RTX 3080 Ti with 12 GB VRAM
  - Ryzen 7 5800X3D
  - 32 GB RAM
  - Native 4K OLED display
- Performance target:
  - Stable 60 FPS at native 4K
  - 90 FPS is optional, not required

Before making changes, report:

- NGVO Wabbajack version
- Skyrim runtime version
- SKSE version
- Address Library version
- ENB binaries and Cabbage ENB preset version
- Existing UI, gameplay, animation, output, patch, and DLL mods
- Existing plugin count and plugin types
- Existing generated outputs
- Root-folder modifications
- Creation Club content and versions

Do not guess versions, filenames, URLs, Nexus IDs, dependencies, masters,
patches, or FOMOD selections.

## 2. Global visual rules

Preserve NGVO's visual identity wherever possible.

Required:

- Keep Cabbage ENB.
- Preserve NGVO's weather, lighting, textures, meshes, grass, trees, water,
  landscape, city visuals, animations, LOD, DynDOLOD, TexGen, grass cache,
  Nemesis/Pandora output, and synthesis outputs unless a verified compatibility
  change is required.
- Bright, crisp, natural presentation suitable for HDR/OLED.
- Nights and interiors may justify a lantern but must remain readable.
- Prefer restrained Nordic Souls-style presentation over Nolvus-style excess.
- Maintain stable 60 FPS at native 4K.

Do not add:

- Community Shaders alongside Cabbage ENB
- Competing ENBs, weather systems, or lighting systems
- Unreviewed texture, grass, tree, water, city, NPC, or animation stacks
- Excessive particles
- Anime-styled equipment or animations
- Sexualized NPC overhauls or NSFW content
- Extremely dark lighting
- Unpatched city overhauls

Do not regenerate visual outputs until worldspace content is finalized.

## 3. Living-world design principles

The world should feel inhabited without behaving like a continuous event
generator. Living-world systems must support quiet travel, believable routines,
and restrained escalation while preserving NGVO's visual and NPC foundation.

Required outcomes:

- NPCs sleep, eat, work, socialize, seek shelter, and react appropriately to
  time, weather, danger, and location.
- Roads contain travelers, merchants, guards, pilgrims, hunters, faction
  patrols, and occasional hostile or supernatural encounters.
- Cities and inns feel inhabited without becoming overcrowded.
- Travel retains quiet periods.
- Random encounters do not become constant combat or overlapping event chains.
- Dialogue and reactions are varied, contextual, and non-spammy.
- Civilians avoid suicidal behavior during attacks and seek safety where
  supported.
- Quest scenes, aliases, schedules, faction logic, FaceGen, and NGVO NPC
  appearances remain intact.

Implementation preferences:

- Prefer lightweight event-driven, SPID, KID, SKSE, and Base Object Swapper
  implementations over polling-heavy scripts.
- Prefer packages and native faction behavior over broad cloak-based reaction
  stacks.
- Preserve native-4K performance and long-save stability.
- Do not use living-world systems to start the main quest accidentally.
- Respect Skyrim Unbound's Dragonborn, dragon, and main-quest settings.

## 4. NPC schedules and daily behavior

Evaluate and select a single primary NPC schedule framework. AI Overhaul SSE is
the initial candidate. Preserve vanilla and quest-specific packages unless the
framework has a documented replacement and a verified patch.

NPC behavior should cover:

- Work and shop opening/closing
- Meals and food access
- Sleep and wake cycles
- Leisure, socializing, and tavern use
- Weather shelter and sensible travel limits
- Civilian flee, seek-cover, and return-home behavior
- Guard, faction, and quest-specific exceptions

Rules:

- Forward AI packages without forwarding unrelated NPC appearance records.
- Do not forward entire NPC records blindly.
- Preserve FaceGen and NGVO head parts, hair, skin, tint, and appearance data.
- Audit package priority, aliases, sandbox locations, navmesh, and quest scenes
  in xEdit and in-game.
- Do not add a second broad AI schedule overhaul.

## 5. Dialogue and social reactivity

Candidate dialogue layer:

- Relationship Dialogue Overhaul - RDO SE
- Guard Dialogue Overhaul SE
- More to Say
- Misc Dialogue Edits
- More Dialogue Options

Use only compatible, non-duplicative modules. Dialogue must be contextual and
finite rather than a constant ambient notification system.

Rules:

- Audit duplicate topics, conditions, voice types, quest aliases, and scene
  records before selection.
- Avoid cloak-based reaction stacks that generate repetitive commentary.
- Apply cooldowns, conditions, distance limits, and event filters where offered.
- Preserve quest dialogue, faction dialogue, follower commentary, and custom
  follower frameworks.
- Test greeting frequency and repeated comments over 20-to-30-minute sessions.

## 6. Random encounters and road activity

Begin with **Extended Encounters** as the encounter foundation.

Additional candidates:

- World Encounter Hostility Fix, if applicable to the target runtime
- Timing is Everything SE
- Ask The Way
- Better Courier or Provincial Courier Service, not both

Selection rules:

- Do not stack multiple broad encounter injectors without a documented overlap
  analysis.
- Use Timing is Everything to delay DLC, dragon, cultist, and other major event
  triggers where appropriate.
- Roads must include travelers, merchants, guards, pilgrims, hunters, faction
  patrols, and occasional hostile or supernatural encounters.
- Preserve quiet road segments and non-combat travel periods.
- Limit encounter frequency and prevent uncontrolled encounter chains.
- Do not allow any encounter system to start the main quest accidentally.
- Better Courier and Provincial Courier are mutually exclusive.

## 7. Patrols and faction presence

Candidate:

- Immersive Patrols SE AE, using small groups and restrained frequency

Faction presence should communicate regional control without turning roads and
towns into permanent battlefields. Patrols must respect Civil War, Open Civil
War, faction quest states, Skyrim Unbound, and city edits.

Rules:

- Use small Immersive Patrols groups and moderate frequency.
- Do not add large Civil War patrol or battle additions without separate
  approval.
- Audit faction ownership, hostility, encounter zones, aliases, navmesh, and
  Open Civil War states.
- Reject persistent town battles and uncontrolled faction escalation.

## 8. Civilian danger responses

Candidate:

- Run For Your Lives, only if AI Overhaul does not sufficiently cover danger
  responses

Civilians should flee, shelter, or remain in protected locations during dragon,
undead, vampire, bandit, and faction attacks. They should not charge enemies,
stand in open streets, or produce repetitive emergency dialogue.

Rules:

- AI Overhaul is tested first; Run For Your Lives is mutually exclusive with a
  functionally equivalent danger-response implementation.
- Preserve essential NPC, quest, alias, and scene behavior.
- Test dragons, vampires, civil-war attacks, town interiors, and return-to-life
  behavior after danger ends.

## 9. Inns and public spaces

Candidate interaction and occupancy systems:

- EVG Conditional Idles
- Conditional Expressions
- Gesture Animation Remix
- Immersive Interactions - Animated Actions
- Use Those Blankets
- Go to Bed
- Sleeping Expanded
- Simply Knock SKSE, if runtime-compatible

Rules:

- Do not stack generic traveler or inn-population mods.
- Use idle, furniture, bed, and animation systems that preserve vanilla and
  quest packages.
- Inns should have believable workers, travelers, meals, music, conversations,
  and sleeping behavior without overcrowding.
- Public spaces should have quiet and busy periods rather than continuous
  ambient activity.
- Audit animation behavior output, furniture markers, ownership, AI packages,
  and script latency.

## 10. Wildlife and ecology

Candidate requiring separate approval:

- SkyTEST
- Broad wildlife overhauls

Wildlife must remain regionally plausible and leave quiet wilderness periods.
Do not add broad wildlife systems until the core living-world stack is stable.
Evaluate spawn density, predator behavior, pathing, leveled lists, encounter
zones, survival interactions, and performance before approval.

### Travel and world details

Travel should provide texture rather than constant interruption. Use signs,
roadside idles, shelters, camps, travelers, courier routes, weather behavior,
and regional faction presence to make movement meaningful without forcing an
encounter every few minutes.

Rules:

- Preserve quiet travel periods in every hold and on long routes.
- Keep road encounters distinct from city population systems.
- Avoid stacking generic traveler, inn-population, courier, and encounter
  injectors.
- Evaluate roadside objects and swapped variants through Base Object Swapper
  where possible rather than persistent scripted placement.
- Re-run DynDOLOD, occlusion, and relevant landscape outputs only after travel,
  city, and worldspace content is final.

### Unified candidate mod manifest

These candidates are inventory and compatibility-review entries, not automatic
installation approvals. Duplicate detection against NGVO and the existing
manifest is required before selection.

Core living-world candidates:

- AI Overhaul SSE
- Relationship Dialogue Overhaul - RDO SE
- Guard Dialogue Overhaul SE
- More to Say
- Misc Dialogue Edits
- More Dialogue Options
- Extended Encounters
- World Encounter Hostility Fix, if applicable to the target runtime
- Timing is Everything SE
- Immersive Patrols SE AE, restrained settings only
- Run For Your Lives, only if AI Overhaul does not sufficiently cover danger
  responses
- EVG Conditional Idles
- Conditional Expressions
- Gesture Animation Remix
- Immersive Interactions - Animated Actions
- Use Those Blankets
- Go to Bed
- Sleeping Expanded
- Dynamic Things Alternative - Base Object Swapper
- Simply Knock SKSE, if runtime-compatible
- Ask The Way
- Better Courier OR Provincial Courier Service, mutually exclusive

Separate approval candidates:

- Immersive World Encounters
- Interesting NPCs
- Citizens of Tamriel
- SkyTEST
- Lawbringer
- Skyrim Realistic Conquering
- Border overhauls
- Large population mods
- Broad wildlife overhauls
- Large Civil War patrol or battle additions

Selection rules:

- Begin with Extended Encounters as the encounter foundation.
- Do not stack broad encounter injectors without documented overlap analysis.
- Use only one broad conquest framework.
- Do not stack generic traveler or inn-population mods.
- Use small Immersive Patrols groups and moderate frequency.
- Delay DLC, dragon, cultist, and major event triggers with Timing is Everything
  where appropriate.
- Respect Skyrim Unbound's Dragonborn and dragon settings.
- Do not allow living-world mods to start the main quest accidentally.
- Preserve NGVO appearance and FaceGen while forwarding AI Overhaul packages.
- Do not forward entire NPC records blindly.
- Avoid cloak-based reaction stacks that generate repetitive commentary.
- Defer borders, wildlife overhauls, conquest systems, and population packs
  until the core living-world stack is stable.
- Do not add another survival, follower, horse, auto-loot, or combat-hotkey
  framework.

## 11. Simonrim gameplay foundation

Use Simonrim as the primary gameplay ecosystem.

Add or retain compatible versions of:

1. Adamant - A Perk Overhaul
2. Mysticism - A Magic Overhaul
3. Aetherius - A Race Overhaul
4. Mundus - A Standing Stone Overhaul
5. Pilgrim - A Religion Overhaul
6. Arena - An Encounter Zone Overhaul
7. Blade and Blunt - A Combat Overhaul
8. Apothecary - An Alchemy Overhaul
9. Gourmet - A Cooking Overhaul
10. Thaumaturgy - An Enchanting Overhaul
11. Scion - A Vampire Overhaul
12. Manbeast - A Werewolf Overhaul
13. Artificer - An Artifact Overhaul
14. Sorcerer - A Staff and Scroll Overhaul

Rules:

- Verify each mod's exact version, dependencies, Creation Club support, and
  cross-compatibility.
- Use official Simonrim patches where applicable.
- Do not add Ordinator, Vokrii, Requiem, Reliquary of Myth, Vestige, Zim's
  Immersive Artifacts, Awesome Artifacts, or competing broad overhauls.
- Test warrior, rogue, assassin, archer, mage, spellsword, necromancer,
  vampire, werewolf, bard, merchant, and hybrid builds.

## 12. Artifact visuals

Add:

15. ArteFakes - Unique Artifacts Replacer

Rules:

- ArteFakes provides visual models and model paths.
- Artificer provides gameplay stats, effects, enchantments, keywords, and
  balance.
- Do not add Unique Uniques as a second broad replacer.
- Inspect every overlap between ArteFakes and Artificer in xEdit.
- Create a minimal compatibility patch that forwards:
  - Artificer gameplay data
  - ArteFakes model paths and intentional visual data
- Consider individual artifact model replacers only after this combination is
  stable.

## 13. Magic expansion

Required direction:

- Mysticism remains the core spell package.
- Add substantial magic without stacking multiple giant spell packs.
- Choose exactly one AE-compatible spell-crafting framework.
- Add at most one supplementary spell package after compatibility review.
- Do not install multiple spell-crafting systems.

Research and present candidates before selecting:

- One maintained spell-crafting system compatible with the target runtime,
  Mysticism, Adamant, NGVO, and Wabbajack distribution
- At most one restrained supplementary spell pack compatible with Mysticism

Summoning requirement:

- Permit 2 to 3 active summons without perk investment.
- Balance extra summons through magicka cost, duration, or summon power.
- Implement using the smallest compatible patch or setting possible.
- Do not globally break summon limits for NPCs unless intentionally documented.

Enchanted-weapon requirement:

- Player enchanted weapons should not consume charges.
- Must be compatible with Thaumaturgy, Artificer, Sorcerer, and staves.
- Prefer a maintained runtime-compatible SKSE solution.
- Otherwise create a minimal custom implementation.
- Exclude staves unless deliberately supported.
- Do not overwrite Thaumaturgy enchantment records.
- Report the proposed solution before installing it.

## 14. Combat

Desired combat:

- Modern and responsive
- Strong in first and third person
- Archery, sword-and-shield, and magic must all feel effective
- Moderate leisure-Skyrim difficulty
- Difficulty from tactics, variety, positioning, AI, and modest enemy strength
- No health-sponging

Add or retain:

16. Precision
17. Blade and Blunt
18. Valhalla Combat, only after compatibility review
19. Wait Your Turn, only if compatible and non-redundant

Valhalla rules:

- Determine overlap with Blade and Blunt.
- Disable overlapping or redundant features where configurable.
- Timed blocking or parrying may remain.
- Dodge must be disabled or unbound.
- Avoid excessive stagger, stamina punishment, or invulnerability behavior.
- Do not install Valhalla if its overlap cannot be cleanly configured.

Wait Your Turn rules:

- Install only if it improves group encounters without causing passive enemies,
  script burden, or overlap with another enemy-spacing system.

Do not add:

- Mandatory MCO/ADXP
- Mandatory dodge rolls
- Soulslike combat dependencies
- Punishing injury systems
- Excessive stagger lock
- Bullet-sponge scaling

## 15. Survival, camping, and lanterns

Add or retain:

20. SunHelm Survival

Requirements:

- Hunger
- Thirst
- Fatigue
- Warmth and exposure
- Sleep requirements
- Camping
- Compact survival meters
- Non-spammy notifications
- Meaningful but not tedious survival

Camping:

- Add Campfire only if required by the selected camping solution.
- Prefer avoiding Campfire if SunHelm and a lighter camping solution safely meet
  requirements.
- Use only one needs/survival framework.

Lantern:

- Select one wearable lantern system compatible with:
  - Current runtime
  - NGVO
  - Cabbage ENB
  - SunHelm
  - First and third person
  - Player and follower behavior
- Verify light limits, ENB behavior, equipment-slot usage, animations, and
  performance.
- Do not stack multiple lantern frameworks.

Provide a balanced SunHelm MCM preset and document all settings.

## 16. Economy

Requirements:

- Economy should not be overly harsh.
- Merchants must have substantially more gold.
- Prefer a lightweight merchant-gold solution.
- Consider Trade and Barter only if a broader economy configuration is needed.
- Do not add multiple economy overhauls.

Provide two evaluated options:

1. Simple merchant-gold increase
2. Trade and Barter with a moderate preset

Choose the lowest-conflict solution that meets the requirement.

## 17. Horses

Choose exactly one horse framework after compatibility testing:

Preferred:

21. Convenient Horses

Fallback:

22. Simplest Horses

Required behavior:

- Horse inventory
- Horse recall or recovery
- Follower horse support
- Compatibility with Nether's Follower Framework
- Safe handling of Inigo and Lucien
- Compatibility with optional custom followers
- Compatibility with SunHelm and NGVO
- Stable mounted combat and dismounting

Rules:

- Install exactly one framework.
- Prefer Convenient Horses only if stable with the final setup.
- Otherwise install Simplest Horses.
- Do not force unsupported custom followers into framework management.
- Document MCM settings and known limitations.

## 18. UI and controls

Inventory NGVO before adding anything. Add missing compatible components only.

Add or retain:

23. SkyUI
24. TrueHUD
25. Wheeler - Quick Action Wheel of Skyrim
26. NGVO's existing compatible Quick Loot implementation
27. Compass Navigation Overhaul
28. More Informative Console
29. Better Dialogue Controls
30. Better MessageBox Controls
31. Constructible Object Custom Keyword System
32. Inventory Interface Information Injector
33. iWant Widgets, only if required for the chosen survival meters

Required behavior:

- Minimal exploration HUD
- Enemy health bars shown contextually during combat
- Follower health bars during combat or low health
- Boss bars for major encounters
- Filtered or toggleable compass
- Compact needs and exposure meters
- No floating damage numbers
- No permanent MMO-style widget wall
- UI elements should disappear when unnecessary
- Preserve NGVO's UI skin and layout when possible

## 19. Quality of life

Add or retain compatible versions of:

34. SkyUI SE - Flashing Savegames Fix
35. Stay At The System Page NG
36. Yes I'm Sure
37. Whose Quest Is It Anyway
38. Better Third Person Selection
39. Read Or Take SKSE
40. Remember Lockpick Angle
41. Simple Activate SKSE
42. Unequip Quiver SE
43. Favorite Misc Items
44. Essential Favorites
45. CoMAP

Rules:

- Check NGVO for duplicates and equivalent features.
- Prefer maintained NG/runtime-compatible versions.
- Do not add a second implementation of the same feature.
- Preserve NGVO's map visuals.
- Do not add Atlas Map Markers in this phase.
- Confirm every SKSE DLL against the exact runtime.

## 20. Auto-harvest

Add:

46. Smart Harvest NG AutoLoot

Use it as the only broad auto-harvesting framework.

Initial preset:

- Auto-harvest flora, ingredients, insects, and critters.
- Auto-loot loose gold and keys.
- Allow ammunition with practical quantity limits.
- Apply strict value-to-weight rules to potions and miscellaneous loot.
- Use a radius around 500 to 800 game units.
- Pause around 75 to 80 percent carry capacity or preserve at least 75 free
  carry-weight units where supported.
- Use compact, non-spammy notifications.

Disable automatic collection of:

- Weapons
- Armor
- Clothing
- Books
- Notes
- Food
- Firewood
- Ore
- Ingots
- Clutter
- Owned items
- Containers
- Corpses

Safety rules:

- Never auto-destroy, auto-sell, or silently discard items.
- Do not automatically manipulate unknown unique, scripted, replica,
  collectible, displayable, or quest items.
- Test against LOTD after LOTD is installed.
- Test compatibility with Quick Loot and SunHelm.
- Export and document the final preset.

## 21. Number-key combat sets

Preferred:

47. Serio's Cycle Hotkeys

Install only if compatible with the target runtime. If incompatible, stop and
report maintained alternatives rather than silently substituting.

Do not combine it with AH Hotkeys or another full equipment-set hotkey system.

Configure:

- 1: Sword and shield
- 2: Bow and selected arrows
- 3: Destruction spell and ward
- 4: Destruction spell and healing
- 5: Dual-spell setup
- 6: Summoning setup
- 7: Dagger and utility or invisibility
- 8: Staff and spell
- 9: Lantern or utility setup
- 0: Emergency healing setup

Use Wheeler for potions, powers, lantern alternatives, and less-frequent utility
actions.

Test:

- Left/right hand restoration
- Shields
- Bows and ammunition
- Dual wielding
- Two copies of the same weapon
- Dual spells
- Staves
- Poisons
- Scripted equipment removal
- Mounted behavior
- Vampire Lord transformation
- Werewolf transformation
- Save and reload
- Conflicts with vanilla favorites and Wheeler

## 22. Followers

Add:

48. Nether's Follower Framework
49. Inigo
50. Lucien

Optional only after compatibility testing:

51. Remiel
52. Xelzaz
53. Kaidan 2

Requirements:

- Easy follow, wait, dismiss, outfit, recovery, teleport, and group commands
- Support large parties technically
- Balance ordinary play around 2 to 3 followers
- Follower mount support where safe
- Stable behavior with chosen horse framework
- Stable behavior with SunHelm, quests, and new lands

Rules:

- Use NFF for vanilla and compatible standard followers.
- Do not import Inigo, Lucien, or another custom-framework follower into NFF
  unless the follower's author explicitly supports it.
- Review each custom follower's own horse and teleport systems.
- Verify commentary and patches for major quest/new-land mods.
- Use only one general follower framework.
- Document NFF MCM settings and follower exclusions.

## 23. Alternate start and roleplay

Add:

54. Skyrim Unbound Reborn

Required configuration capabilities:

- Dragonborn or non-Dragonborn
- Dragons enabled, disabled, or delayed
- Immediate or delayed main quest
- Multiple starting locations and backgrounds
- Configurable gear, gold, spells, and survival supplies
- No forced race, gender, morality, faction, religion, or backstory

Provide documented optional profiles:

- Wanderer
- Ranger
- Mage
- Mercenary
- Thief
- Assassin
- Merchant
- Vampire
- Werewolf
- Custom

Verify interactions with:

- Survival initialization
- LOTD
- Inigo and Lucien
- Main quest triggers
- Dragon spawning
- Civil War
- Dawnguard
- Creation Club quests

## 24. Global quest pacing

Add or retain:

55. At Your Own Pace
56. The Choice Is Yours
57. Curated JaySerpa quest expansions

Rules:

- Inventory exact modules and patches.
- Avoid overlapping dialogue and quest-stage edits.
- Use only modules verified for the final faction setup.
- Install JaySerpa expansions individually, not blindly as an undefined bundle.
- Record every selected module and excluded module.
- Ensure Skyrim Unbound does not conflict with main-quest pacing modules.

## 25. College of Winterhold

Add:

58. Obscure's College of Winterhold
59. College of Winterhold Quest Expansion
60. Compatible At Your Own Pace College module

Goal:

- Believable academic institution
- Better quest pacing
- Useful magical headquarters

Rules:

- Do not add Immersive College of Winterhold or Ultimate College.
- Verify all required patches among Obscure's College, quest expansion, AYOP,
  Mysticism, LOTD, lighting, NPCs, navmesh, and NGVO.
- Audit exterior and interior worldspace/cell conflicts.
- Regenerate LOD only at the final worldspace phase.

## 26. Thieves Guild

Evaluate and add the compatible subset of:

61. Thieves Guild Requirements
62. Brynjolf Has Time for You
63. Following Mercer
64. Thieves Guild For Good Guys
65. Compatible At Your Own Pace Thieves Guild module

Goals:

- Earned progression
- Criminal and morally gray roleplay
- Ethical or reform-minded choices where safely possible

Rules:

- Build a compatibility matrix before installation.
- Do not combine overlapping quest-stage edits without a verified patch.
- Thieves Guild For Good Guys is optional and must be omitted if the patch
  chain is incomplete.
- Do not add Opulent Thieves Guild without a complete verified patch chain.
- Test radiant-job requirements, Mercer transitions, Brynjolf scenes, and
  post-quest states.

## 27. Civil War

Preferred foundation:

66. Open Civil War

Optional only if fully compatible and non-redundant:

67. Civil War Overhaul Redux
68. Serious Civil War Defense

Optional post-war content:

69. The Second Great War

Rules:

- Stability is more important than feature count.
- Open Civil War is the initial preferred choice.
- Do not stack Civil War Overhaul Redux with Open Civil War merely for more
  features.
- Add Serious Civil War Defense only if its quest states and city battles are
  verified against the chosen foundation.
- Treat The Second Great War as separate post-Civil-War content.
- Verify both Imperial and Stormcloak paths.
- Audit Skyrim Unbound, AYOP, city cells, navmesh, NPC AI packages, aliases,
  Civil War quest stages, and LOTD interactions.
- If compatibility is uncertain, reduce the stack to Open Civil War alone.

## 28. Companions

Add compatible versions of:

70. Companions Questline Tweaks
71. Compatible At Your Own Pace Companions module

Requirements:

- Better pacing
- Ability to embrace, reject, or cure lycanthropy
- Integration with Manbeast
- Functional cure path

Rules:

- Verify quest-stage overlap between the two mods.
- Use only compatible modules.
- Test joining, Circle progression, transformations, cure flow, and post-quest
  state.

## 29. Dark Brotherhood

Add or evaluate:

72. Destroy the Dark Brotherhood - Enhanced
73. Penitus Oculatus

Goals:

- Assassin route
- Destroy/justice route
- Reform-oriented roleplay where safely supported

Rules:

- Clearly document mutually exclusive routes.
- Do not force join, destroy, and reform quest states simultaneously.
- Verify whether the two mods are meant to work together and install required
  patches.
- Test every supported path from a separate new game or isolated test save.
- Document the decision point after which paths become unavailable.

## 30. Dawnguard and Volkihar

Add:

74. Dawnguard Arsenal
75. Dawnguard Map Markers

Foundation:

- Scion for vampires
- Manbeast for werewolves

Requirements:

- Support Dawnguard and Volkihar routes where safely possible.
- Verify weapon records against Artificer and ArteFakes where relevant.
- Verify locations, map markers, quests, leveled lists, and vampire progression.
- Confirm compatibility with Serana-related changes already in NGVO.
- Do not add another vampire or werewolf overhaul.

## 31. Bards College

Add:

76. Bards Reborn Student of Song

Requirements:

- Support bard roleplay as a meaningful archetype.
- Verify compatibility with Solitude cells, LOTD, city/worldspace edits, NPC
  packages, Skyrim Unbound, and relevant quest expansions.
- Audit navmesh and interior conflicts.
- Document required patches and performance impact.

## 32. Blades and Paarthurnax

Choose exactly one:

77. The Paarthurnax Dilemma
78. Paarthurnax Quest Expansion

Preferred selection method:

- Compare compatibility, player choice, voice implementation, runtime
  requirements, AYOP interaction, Skyrim Unbound interaction, and LOTD patches.
- Choose the lighter, better-supported option.
- Do not install both.
- Keep main-quest changes limited and roleplay-neutral.

## 33. Legacy of the Dragonborn

Add:

79. Legacy of the Dragonborn
80. Legacy of the Dragonborn Patch Hub

Requirements:

- Treat LOTD as a major campaign hub.
- Keep participation roleplay-neutral:
  - Museum or archive
  - Public institution
  - Private collection
  - Optional side activity
- Do not force every character to center their story on the museum.
- Verify the exact LOTD major version and patch-hub version.
- Use only patches matching installed mod versions.
- Re-run the Patch Hub FOMOD whenever the supported mod inventory changes.
- Do not clean plugins unless specifically instructed by the author.

Audit:

- Persistent references
- Displays
- Replicas
- Unique-item records
- Scripts
- Quest aliases
- Safehouse functionality
- Solitude cells
- Excavation sites
- Leveled lists
- Artifact ownership
- Smart Harvest exclusions
- Skyrim Unbound start behavior
- Artifact conflicts among LOTD, Artificer, and ArteFakes

Create custom patches only after official patches are installed.

## 34. Tier 1 quest content

Evaluate and add individually:

81. Wyrmstooth
82. The Forgotten City
83. Missives
84. Headhunter - Bounties Redone
85. Selected JaySerpa quest expansions

Each requires review for:

- Target runtime and AE support
- Exact version
- LOTD Patch Hub support
- NGVO visual compatibility
- Landscape and navmesh conflicts
- LOD requirements
- Quest aliases and overlap
- Follower commentary/support
- Skyrim Unbound compatibility
- Performance
- Wabbajack redistribution/download behavior

Missives and Headhunter:

- Verify whether they overlap in bounty generation.
- Install required integration patches.
- Avoid duplicate rewards or broken radiant objectives.
- Verify new-land board support only where official or maintained patches exist.

## 35. Tier 2 quest and new-land content

Evaluate one at a time after Tier 1 is stable:

86. Beyond Skyrim - Bruma
87. Falskaar
88. VIGILANT
89. Beyond Reach

Do not install all four simultaneously without individual test gates.

For every mod, report:

- Exact supported version
- AE/runtime status
- Dependencies
- LOTD patch availability and exact version match
- Landscape, navmesh, and worldspace conflicts
- LOD requirements
- Voice/add-on requirements
- Follower commentary
- Quest overlap
- Persistent-reference count impact
- Plugin type and master status
- Performance impact
- Wabbajack download and permissions status

Dark, horror, and morally grim content is allowed.

Acceptance gate for each new land:

- Game launches
- New game starts
- Entry quest starts
- Worldspace loads
- Navmesh works
- Followers transition correctly
- Main quest completes
- Return travel works
- LOTD displays function
- No repeatable crash is introduced
- 4K performance remains acceptable

## 36. Conflict-resolution policy

Use official patches before creating custom patches.

For each plugin:

1. Inspect all conflicts in xEdit.
2. Classify conflicts as intentional, benign, unresolved, or patched.
3. Check:
   - Quest records
   - Dialog topics
   - Cells and worldspaces
   - Navmesh
   - NPC records
   - AI packages
   - Leveled lists
   - Items
   - Enchantments
   - Keywords
   - Containers
   - Scripts
   - Persistent references
4. Create the smallest possible custom patch.
5. Do not forward records blindly.
6. Do not compact FormIDs without explicit safety verification.
7. Do not ESL-flag plugins with new cells, interior records, dialogue, scripts,
   facegen constraints, or unsafe FormID assumptions.
8. Document every record changed by the custom patch.

Custom patch priorities:

- Preserve NGVO visual records.
- Preserve Simonrim gameplay balance.
- Preserve Artificer gameplay data.
- Preserve ArteFakes visual paths.
- Preserve LOTD displays and official integration.
- Preserve selected faction quest logic.
- Preserve Skyrim Unbound start logic.
- Preserve official new-land records.

Living-world compatibility matrix must explicitly cover:

- NGVO NPC visuals, FaceGen, animation, and behavior output
- Simonrim and Arena
- Skyrim Unbound Reborn
- SunHelm
- Smart Harvest
- NFF
- Inigo and Lucien
- The selected horse framework
- At Your Own Pace and The Choice Is Yours
- All selected faction overhauls
- Open Civil War
- LOTD
- Missives and Headhunter
- City and interior changes
- Every selected new land
- Synthesis
- DynDOLOD and occlusion
- The exact AE runtime, Address Library, and SKSE version

For NPC and behavior conflicts, preserve FaceGen and appearance records first,
then forward only the intended AI packages, factions, keywords, conditions,
dialogue, and scripts. Record every intentional exception.

Use appropriate tooling only where needed:

- xEdit for record conflict resolution
- Synthesis for supported patchers
- Nemesis or Pandora only if the animation stack requires it
- BodySlide only for included assets that require output
- TexGen and DynDOLOD only after worldspaces are final
- Grass-cache generation only if NGVO's setup requires regeneration
- Occlusion generation only when required

## 37. Installation phases and test gates

Phase 0: Baseline
- Install and verify NGVO unchanged.
- Record FPS and frametimes in representative areas.
- Archive current profiles and generated outputs.

Phase 1: Gameplay
- Add Simonrim core, Artificer, and Sorcerer.
- Resolve and test gameplay conflicts.

Phase 2: Utility
- Add UI, QoL, Smart Harvest, hotkeys, survival, lantern, economy, combat, and
  animations.
- Test before continuing.

Phase 3: Character systems
- Add Skyrim Unbound Reborn, NFF, Inigo, Lucien, and exactly one horse system.
- Test start profiles, followers, survival, and mounts.

Phase 4: Living world
- Add the approved core living-world stack after gameplay and utility systems
  are stable.
- Begin with Extended Encounters, AI Overhaul, selected dialogue modules, and
  restrained Immersive Patrols.
- Add only the approved schedule, social, idle, interaction, bed, and travel
  systems.
- Test every major hold before adding faction, conquest, border, wildlife,
  population, or new-land expansion.

Phase 5: LOTD
- Add LOTD and Patch Hub.
- Resolve artifact, Solitude, collection, and auto-loot behavior.
- Start another disposable new game.

Phase 6: Factions
Add and test one group at a time:
- College
- Thieves Guild
- Civil War
- Companions
- Dark Brotherhood
- Dawnguard/Volkihar
- Bards College
- Blades/Paarthurnax

Do not proceed past a faction with unresolved quest-stage or navmesh conflicts.

Phase 7: Tier 1 content
- Add and test one mod at a time.

Phase 8: Tier 2 content
- Add and test one worldspace at a time.

Phase 9: Final conflict resolution
- Complete xEdit conflict review.
- Build minimal custom patches.
- Finalize plugin order.

Phase 10: Generated outputs
Only now regenerate required:
- Behavior output
- Synthesis output
- BodySlide output
- Grass cache
- TexGen
- DynDOLOD
- Occlusion
- Any NGVO-specific patch/output generation

Phase 11: Integrated testing
- Start a clean new game.
- Test all documented character profiles.
- Test faction branches.
- Test transformations.
- Test followers and horses.
- Test survival and lanterns.
- Test artifacts and LOTD displays.
- Test all new lands.
- Profile native-4K performance.

Living-world observation gate:

- Observe every major hold for 20-to-30 minutes in daytime, evening, night,
  clear weather, and adverse weather where practical.
- Cover work, meal, sleep, and leisure schedules.
- Cover shop opening and closing.
- Cover inn population and public-space occupancy.
- Measure greeting frequency and dialogue repetition.
- Test weather reactions.
- Test civilian and guard danger responses.
- Measure road encounter frequency and quiet periods.
- Verify patrol size and faction presence.
- Measure wildlife density.
- Check stuck NPCs and package loops.
- Check navmesh failures.
- Check interrupted quest scenes.
- Check script latency and Papyrus errors.
- Check save growth across repeated travel and saves.
- Record FPS, 1% lows, frametimes, VRAM, and RAM.

Acceptance criteria:

- No dark-face bugs.
- No recurring NPC package loops.
- No repeated comments every few seconds.
- No persistent town battles.
- No uncontrolled encounter chains.
- No broken quest scenes.
- No obvious save bloat.
- No substantial native-4K performance regression.
- Towns feel inhabited but not overcrowded.
- Roads remain capable of being quiet.

Phase 12: Wabbajack preparation
- Pin exact versions and files.
- Separate generated files.
- Identify manual files.
- Verify download sources.
- Review permissions and licensing.
- Produce installation and troubleshooting documentation.

## 38. Performance requirements

Target stable 60 FPS at native 4K on:

- RTX 3080 Ti, 12 GB VRAM
- Ryzen 7 5800X3D
- 32 GB RAM

Benchmark at minimum:

- Riverwood
- Whiterun exterior
- Whiterun city
- Solitude exterior
- Solitude city
- Falkreath forest
- Riften exterior
- Riften city
- College of Winterhold
- Large Civil War battle
- Heavy magic combat
- Three-follower combat
- LOTD museum
- Each new worldspace

Living-world performance cases must also include:

- A busy inn and a quiet inn during different schedule periods
- A city attack with civilian evacuation behavior
- A road with travelers and patrols during a quiet period
- A road during a validated hostile encounter
- A hold with selected wildlife enabled
- Weather shelter and indoor/outdoor transitions
- Extended travel with followers, horse, SunHelm, Smart Harvest, and NFF

Record:

- Average FPS
- 1% low FPS
- Frametime behavior
- VRAM use
- RAM use
- Repeatable stutter
- CPU-limited and GPU-limited locations
- Papyrus latency, active script count, and save-file growth after extended
  travel

If performance falls below target:

1. Do not immediately replace NGVO's visual stack.
2. Reduce optional new-land or scripted load.
3. Review LOD settings.
4. Review shadow resolution and ENB effects.
5. Review grass density and distance.
6. Use restrained texture-resolution reductions where visually acceptable.
7. Document every compromise.

## 39. Explicit exclusions

Do not add without a separate approved review:

- Community Shaders
- Another ENB
- Competing weather or lighting systems
- Ordinator
- Vokrii
- Requiem
- Another artifact overhaul
- Another staff/scroll overhaul
- Multiple giant spell packs
- Multiple spell-crafting systems
- Multiple survival frameworks
- Multiple follower frameworks
- Multiple horse frameworks
- Multiple broad auto-loot frameworks
- Multiple combat-loadout frameworks
- Mandatory MCO/ADXP
- Mandatory dodge rolls
- Soulslike dependencies
- Bullet-sponge scaling
- Excessive stagger or injury systems
- Floating damage numbers
- Permanent MMO-style HUD
- Anime-styled or flashy equipment/animations
- Sexualized NPC or NSFW overhauls
- Major main-quest rewrites
- Unpatched city overhauls
- Unreviewed visual replacement stacks
- Opulent Thieves Guild without a complete patch chain
- Immersive College or Ultimate College alongside Obscure's College
- Both Paarthurnax mods
- Atlas Map Markers during the initial build
- Final LOD generation before worldspaces are locked
- Multiple broad encounter injectors without overlap analysis
- Multiple generic traveler or inn-population mods
- Cloak-heavy reaction stacks that create repetitive commentary
- Large population packs without a separate performance and navmesh review
- Broad wildlife overhauls before the core living-world stack is stable
- Border overhauls without separate approval
- Large Civil War patrol or battle additions without separate approval
- A second broad conquest framework
- A second survival, follower, horse, auto-loot, or combat-hotkey framework

## 40. Required output for every mod

For every selected mod, provide:

- Exact mod name
- Author
- Exact version
- Exact filename
- Official/Nexus URL
- Download source
- Archive hash if available
- Plugin names
- Plugin type: ESM, ESP, ESL, or ESP-FE
- Masters
- Dependencies
- Optional files used
- FOMOD selections
- Manual installation steps
- Root versus MO2 installation
- MO2 separator and left-pane position
- Proposed plugin position
- File conflicts
- Record conflicts
- Official patches
- Custom patches
- MCM/configuration settings
- Runtime compatibility
- Test procedure
- Wabbajack download viability
- Permission/licensing concerns
- Acceptance or rejection reason

## 41. Final deliverables

Produce:

1. Exact final mod manifest
2. MO2 left-pane install order
3. Final plugin load order
4. FOMOD selection guide
5. Manual/root-install instructions
6. Compatibility and patch matrix
7. Custom xEdit patch documentation
8. Generated-output instructions and ordering
9. MCM/configuration preset documentation
10. Smart Harvest preset
11. Number-key combat-loadout preset
12. SunHelm preset
13. HUD preset
14. NFF preset
15. Combat preset
16. Horse-framework preset
17. Skyrim Unbound preset
18. LOTD configuration
19. Optional player start-profile guide
20. Integrated testing checklist
21. Living-world schedule, encounter, patrol, civilian-response, and inn preset
22. Known limitations
23. Unresolved-conflict report
24. Native-4K performance report
25. Wabbajack-readiness report
26. Manual-file and version-pinning report
27. Licensing and permissions report

## 42. Immediate task

Do not begin with the whole stack at once.

First produce:

1. NGVO inventory report
2. Duplicate/equivalent-feature report
3. Runtime and SKSE DLL compatibility report
4. Candidate mod manifest with exact versions and URLs
5. Dependency graph
6. Compatibility-risk matrix
7. Phased implementation plan
8. List of decisions that still require approval

Decisions requiring approval before living-world installation:

- Exact AI Overhaul SSE version and whether it is compatible with NGVO FaceGen,
  custom followers, and all selected faction overhauls.
- Exact RDO, Guard Dialogue Overhaul, More to Say, Misc Dialogue Edits, and More
  Dialogue Options modules; these are not assumed to be mutually compatible.
- Whether World Encounter Hostility Fix applies to the exact AE runtime.
- Whether Run For Your Lives adds value beyond AI Overhaul; otherwise exclude it.
- Whether Go to Bed, Sleeping Expanded, Use Those Blankets, and Simply Knock
  can coexist without package, furniture, or script conflicts.
- Selection of Better Courier or Provincial Courier Service; install one only.
- Whether Immersive World Encounters is approved in addition to Extended
  Encounters after overlap analysis.
- Whether Interesting NPCs or Citizens of Tamriel are approved and how their
  dialogue, FaceGen, navmesh, and population impact will be contained.
- Whether SkyTEST, a broad wildlife overhaul, Lawbringer, Skyrim Realistic
  Conquering, a border overhaul, a population mod, or large Civil War patrols
  are approved. Each is independently optional and requires a separate gate.
- Final patrol group size, encounter frequency, dialogue cooldown, inn density,
  wildlife density, and Timing is Everything settings.
- Exact runtime-compatible versions and settings for all SKSE/DLL candidates.

Then implement Phase 1 only:

- Simonrim core
- Artificer
- Sorcerer
- ArteFakes
- Required official compatibility patches
- Minimal custom Artificer/ArteFakes conflict patch if necessary

Stop after Phase 1 testing and report results before proceeding.
