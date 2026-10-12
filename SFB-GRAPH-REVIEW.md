# Graph review: `sec-six-functors-basics` (2026-10-12)

The section was imported on 2026-10-12 from `DerivedCategoryAndSixFunctorsChoice.tex`. Afterwards the blueprint
graph looked much less linear: there were many edges crossing between lines, and some went back into blocks of
earlier sections. This file records why, and what to change. **Suggestions A and B have been applied.** The
redundant-edge list was recomputed against the files first and matched the table exactly.

## Findings

The extra edges have three separate causes.

### 1. Edges added only to silence `[undeclared-edge]` info notices (the import's clean-up step; no mathematical content)

During the import, `lake exe blueprint check` showed 35 `[undeclared-edge]` **info** notices for the new
section. These are not errors; the tree already had 2934 info notices before the import. They were silenced
by declaring every hidden edge one level up, which added:

- **7 edges from the section into blocks of earlier sections.** The `uses` of
  `blueprint/sec-six-functors-basics/_section.md` gained `sk-def-nagata-sketch-data`,
  `sk-prop-nagata-sketch-comp-category`, `sk-thm-nagata-compactification` (Nagata), `sk-thm-p1`,
  `sk-thm-properbasechange` (proper base change), `sk-thm-picard-coherence` and `sk-thm-picard-semicon` (Picard).
  In the collapsed view each one is an arrow from the new section into the middle of an earlier section.
  These are the edges that "map to previous blocks".
- **20 block → section edges in 15 blocks** of the new section (table below). In the whole of the rest of the
  tree only 14 blocks cite a `sec-*` id.

### 2. Real dependencies on earlier sections (from the content; keep)

Block-level `uses` (statement files) that point outside the section:

| Target | Section | Cited by |
|---|---|---|
| `def-weil-pbc-proetale-site` | picard-framework | 8 blocks: sheaf tensor, layer-A pushforward/pullback, layer-A `f_!` and `Rf_!`, pullback from the point, module objects, derived categories, constructible |
| `def-weil-abstract-derived-category` | picard-framework | `sk-def-sfb-derived-categories`, `sk-def-sfb-bounded-constructible` |
| `def-constructible-stratification` | proper-base-change | `sk-def-sfb-constructible` |
| `sk-def-nagata-sketch-data` | nagata-compactification | 7 blocks (the compactification-based `f_!`, `Rf_!`, `Rf^!`, D_cons setting, `Ex_!`) |
| `sk-prop-nagata-sketch-comp-category` | nagata-compactification | `sk-def-sfb-shriek-base-change-morphism` |

Block proof files cite `sk-thm-nagata-compactification` (`sk-def-sfb-dc-setting`) and `sk-thm-properbasechange`
(`sk-thm-sfb-proper-base-change`). The new section sits in 7th position, so these produce long edges back to
sections 1, 3 and 5. That is the same pattern as `sec-smooth-purity`, and it is inherent.

### 3. The section is much denser inside than the others

| Section | Blocks | Block → block edges inside (statement `uses`) | Per block |
|---|---|---|---|
| sec-six-functors-basics | 47 | 173 (207 with block proof files) | 3.7 |
| sec-smooth-purity | 37 | 68 | 1.8 |
| sec-six-functors | 37 | 50 | 1.4 |
| sec-proper-base-change | 11 | 13 | 1.2 |

The import listed every block whose notion a statement or proof mentions, including blocks that are already
reached through another listed block. For example, a block uses both `sk-def-sfb-module-objects` and a block that
itself uses `sk-def-sfb-module-objects`.

## Suggestions

### A. Undo cause 1

- In `blueprint/sec-six-functors-basics/_section.md` set
  `uses = ["sec-nagata-compactification", "sec-picard-framework", "sec-proper-base-change"]`
  (drop the 7 `sk-*` entries).
- Remove the `sec-*` entries from the `uses` of these block statement files
  (`blueprint/sec-six-functors-basics/<block>/_section.md`):

| Block | `sec-*` entries to remove |
|---|---|
| `sk-def-sfb-bounded-constructible` | `sec-picard-framework`, `sec-proper-base-change` |
| `sk-def-sfb-constructible` | `sec-picard-framework`, `sec-proper-base-change` |
| `sk-def-sfb-dc-setting` | `sec-nagata-compactification` |
| `sk-def-sfb-derived-categories` | `sec-picard-framework` |
| `sk-def-sfb-finite-derived-lower-shriek` | `sec-nagata-compactification`, `sec-picard-framework` |
| `sk-def-sfb-finite-lower-shriek` | `sec-nagata-compactification`, `sec-picard-framework` |
| `sk-def-sfb-finite-pushforward-pullback` | `sec-picard-framework` |
| `sk-def-sfb-finite-upper-shriek` | `sec-nagata-compactification` |
| `sk-def-sfb-module-derived-lower-shriek` | `sec-nagata-compactification` |
| `sk-def-sfb-module-lower-shriek` | `sec-nagata-compactification` |
| `sk-def-sfb-module-objects` | `sec-picard-framework` |
| `sk-def-sfb-pullback-from-point` | `sec-nagata-compactification`, `sec-picard-framework` |
| `sk-def-sfb-sheaf-tensor` | `sec-picard-framework` |
| `sk-def-sfb-shriek-base-change-morphism` | `sec-nagata-compactification` |
| `sk-thm-sfb-proper-base-change` | `sec-proper-base-change` |

Cost: about 35 `[undeclared-edge]` info notices come back. They are at info level, like the 2934 already in the tree.

### B. Transitively reduce the block-level edges inside the section (fixes cause 3)

Drop each block → block `uses` entry that is already implied through another block of the section. Treat the
block statement and the block proof as one node when deciding this.

- Only block files change: `<block>/_section.md` and `<block>/<block>.proof.md`.
- **Child nodes keep their exact `uses`**, so the precise dependencies stay recorded one level down.

This takes 207 edges down to 69, about 1.5 per block, which is in line with the other sections. Expect more
`[undeclared-edge]` info notices (the children's edges stay, the block edge above them goes). These are harmless.

The edges to drop are listed below. "In" says which file holds the entry. "Already reached via" is one block
listed by the same block through which the target is still reachable. The list was computed on 2026-10-12;
recompute it if the files change before it is applied.

| Block | Redundant entry | In | Already reached via |
|---|---|---|---|
| `sk-def-sfb-base-change-morphism` | `sk-def-sfb-dc-setting` | statement | `sk-def-sfb-dc-restricted-functors` |
| `sk-def-sfb-change-of-scalars` | `sk-def-sfb-module-objects` | statement | `sk-prop-sfb-module-category` |
| `sk-def-sfb-change-of-scalars` | `sk-def-sfb-ring-object` | statement | `sk-def-sfb-module-objects` |
| `sk-def-sfb-coefficient-change` | `sk-def-sfb-condensed-ring` | statement | `sk-def-sfb-coefficient-morphisms` |
| `sk-def-sfb-coefficient-change` | `sk-def-sfb-derived-categories` | statement | `sk-def-sfb-derived-extension-of-scalars` |
| `sk-def-sfb-coefficient-change` | `sk-def-sfb-finite-pushforward-pullback` | statement | `sk-def-sfb-coefficient-morphisms` |
| `sk-def-sfb-coefficient-change` | `sk-def-sfb-module-objects` | statement | `sk-def-sfb-derived-categories` |
| `sk-def-sfb-coefficient-change` | `sk-def-sfb-pullback-from-point` | statement | `sk-def-sfb-coefficient-morphisms` |
| `sk-def-sfb-coefficient-change` | `sk-def-sfb-pullback-from-point-comp` | statement | `sk-def-sfb-coefficient-morphisms` |
| `sk-def-sfb-coefficient-change` | `sk-def-sfb-pulled-back-coefficients` | statement | `sk-def-sfb-coefficient-morphisms` |
| `sk-def-sfb-coefficient-comparisons` | `sk-def-sfb-change-of-scalars` | statement | `sk-def-sfb-coefficient-change` |
| `sk-def-sfb-coefficient-comparisons` | `sk-def-sfb-derived-categories` | statement | `sk-def-sfb-coefficient-change` |
| `sk-def-sfb-coefficient-comparisons` | `sk-def-sfb-derived-extension-of-scalars` | proof | `sk-def-sfb-coefficient-change` |
| `sk-def-sfb-coefficient-comparisons` | `sk-def-sfb-module-derived-pushpull` | statement | `sk-def-sfb-module-derived-lower-shriek` |
| `sk-def-sfb-coefficient-comparisons` | `sk-def-sfb-module-lower-shriek` | statement | `sk-def-sfb-module-derived-lower-shriek` |
| `sk-def-sfb-coefficient-comparisons` | `sk-def-sfb-module-pushforward-pullback` | statement | `sk-def-sfb-module-derived-lower-shriek` |
| `sk-def-sfb-coefficient-comparisons` | `sk-def-sfb-transport` | proof | `sk-def-sfb-module-derived-lower-shriek` |
| `sk-def-sfb-coefficient-comparisons` | `sk-prop-sfb-cartesian-coefficients` | proof | `sk-def-sfb-module-derived-lower-shriek` |
| `sk-def-sfb-coefficient-morphisms` | `sk-def-sfb-finite-pushforward-pullback` | statement | `sk-def-sfb-pullback-from-point-comp` |
| `sk-def-sfb-constructible` | `sk-def-sfb-finite-pushforward-pullback` | statement | `sk-def-sfb-module-objects` |
| `sk-def-sfb-constructible` | `sk-def-sfb-module-objects` | statement | `sk-def-sfb-transport` |
| `sk-def-sfb-constructible` | `sk-def-sfb-ring-object` | statement | `sk-def-sfb-module-objects` |
| `sk-def-sfb-constructible` | `sk-def-sfb-sheaf-tensor` | statement | `sk-def-sfb-finite-pushforward-pullback` |
| `sk-def-sfb-constructible` | `sk-prop-sfb-module-category` | statement | `sk-def-sfb-transport` |
| `sk-def-sfb-dc-lower-shriek` | `sk-def-sfb-dc-setting` | statement | `sk-def-sfb-dc-restricted-functors` |
| `sk-def-sfb-dc-lower-shriek` | `sk-def-sfb-module-derived-lower-shriek` | statement | `sk-def-sfb-dc-restricted-functors` |
| `sk-def-sfb-dc-restricted-functors` | `sk-def-sfb-bounded-constructible` | statement | `sk-def-sfb-dc-setting` |
| `sk-def-sfb-dc-restricted-functors` | `sk-def-sfb-condensed-ring` | statement | `sk-def-sfb-bounded-constructible` |
| `sk-def-sfb-dc-restricted-functors` | `sk-def-sfb-constructible` | proof | `sk-def-sfb-bounded-constructible` |
| `sk-def-sfb-dc-restricted-functors` | `sk-def-sfb-module-derived-pushpull` | statement | `sk-prop-sfb-module-derived-factorization` |
| `sk-def-sfb-dc-restricted-functors` | `sk-def-sfb-module-lower-shriek` | statement | `sk-prop-sfb-module-derived-factorization` |
| `sk-def-sfb-dc-restricted-functors` | `sk-def-sfb-module-pushforward-pullback` | proof | `sk-def-sfb-module-derived-pushpull` |
| `sk-def-sfb-dc-restricted-functors` | `sk-def-sfb-qlbar-condensed` | statement | `sk-thm-sfb-qlbar-two-colimit` |
| `sk-def-sfb-dc-restricted-functors` | `sk-prop-sfb-module-derived-factorization` | statement | `sk-thm-sfb-qlbar-two-colimit` |
| `sk-def-sfb-dc-restricted-functors` | `sk-prop-sfb-module-pullback-exact` | proof | `sk-def-sfb-module-derived-pushpull` |
| `sk-def-sfb-dc-setting` | `sk-def-sfb-condensed-ring` | statement | `sk-def-sfb-bounded-constructible` |
| `sk-def-sfb-dc-setting` | `sk-def-sfb-pulled-back-coefficients` | statement | `sk-def-sfb-bounded-constructible` |
| `sk-def-sfb-dc-upper-shriek` | `sk-def-sfb-condensed-ring` | statement | `sk-def-sfb-dc-lower-shriek` |
| `sk-def-sfb-dc-upper-shriek` | `sk-def-sfb-dc-restricted-functors` | statement | `sk-def-sfb-dc-lower-shriek` |
| `sk-def-sfb-dc-upper-shriek` | `sk-def-sfb-dc-setting` | statement | `sk-def-sfb-dc-lower-shriek` |
| `sk-def-sfb-dc-upper-shriek` | `sk-def-sfb-qlbar-condensed` | statement | `sk-def-sfb-dc-lower-shriek` |
| `sk-def-sfb-dc-upper-shriek` | `sk-thm-sfb-qlbar-two-colimit` | statement | `sk-def-sfb-dc-lower-shriek` |
| `sk-def-sfb-derived-categories` | `sk-def-sfb-module-objects` | statement | `sk-prop-sfb-module-category` |
| `sk-def-sfb-derived-categories` | `sk-def-sfb-pulled-back-coefficients` | statement | `sk-def-sfb-module-objects` |
| `sk-def-sfb-derived-categories` | `sk-def-sfb-sheaf-tensor` | statement | `sk-def-sfb-module-objects` |
| `sk-def-sfb-derived-extension-of-scalars` | `sk-prop-sfb-module-category` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-def-sfb-derived-tensor-hom` | `sk-def-sfb-condensed-ring` | statement | `sk-def-sfb-derived-categories` |
| `sk-def-sfb-derived-tensor-hom` | `sk-def-sfb-pulled-back-coefficients` | statement | `sk-def-sfb-derived-categories` |
| `sk-def-sfb-derived-tensor-hom` | `sk-def-sfb-sheaf-tensor` | statement | `sk-def-sfb-condensed-ring` |
| `sk-def-sfb-derived-tensor-hom` | `sk-prop-sfb-module-category` | statement | `sk-def-sfb-derived-categories` |
| `sk-def-sfb-finite-derived-functors` | `sk-def-sfb-finite-pushforward-pullback` | statement | `sk-def-sfb-derived-categories` |
| `sk-def-sfb-finite-derived-lower-shriek` | `sk-def-sfb-derived-categories` | statement | `sk-def-sfb-finite-derived-functors` |
| `sk-def-sfb-finite-derived-lower-shriek` | `sk-def-sfb-finite-lower-shriek` | statement | `sk-def-sfb-finite-derived-functors` |
| `sk-def-sfb-finite-derived-lower-shriek` | `sk-def-sfb-finite-pushforward-pullback` | statement | `sk-def-sfb-derived-categories` |
| `sk-def-sfb-finite-upper-shriek` | `sk-def-sfb-derived-categories` | statement | `sk-def-sfb-finite-derived-functors` |
| `sk-def-sfb-finite-upper-shriek` | `sk-def-sfb-finite-derived-functors` | statement | `sk-def-sfb-finite-derived-lower-shriek` |
| `sk-def-sfb-finite-upper-shriek` | `sk-def-sfb-finite-pushforward-pullback` | statement | `sk-def-sfb-derived-categories` |
| `sk-def-sfb-module-derived-lower-shriek` | `sk-def-sfb-derived-categories` | statement | `sk-def-sfb-module-derived-pushpull` |
| `sk-def-sfb-module-derived-pushpull` | `sk-def-sfb-module-pushforward-pullback` | statement | `sk-prop-sfb-module-pullback-exact` |
| `sk-def-sfb-module-derived-pushpull` | `sk-prop-sfb-module-category` | statement | `sk-def-sfb-derived-categories` |
| `sk-def-sfb-module-lower-shriek` | `sk-def-sfb-change-of-scalars` | statement | `sk-def-sfb-module-pushforward-pullback` |
| `sk-def-sfb-module-lower-shriek` | `sk-def-sfb-coefficient-morphisms` | statement | `sk-def-sfb-module-pushforward-pullback` |
| `sk-def-sfb-module-lower-shriek` | `sk-def-sfb-finite-pushforward-pullback` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-def-sfb-module-lower-shriek` | `sk-def-sfb-module-objects` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-def-sfb-module-lower-shriek` | `sk-def-sfb-pulled-back-coefficients` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-def-sfb-module-lower-shriek` | `sk-def-sfb-sheaf-tensor` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-def-sfb-module-lower-shriek` | `sk-def-sfb-transport` | statement | `sk-def-sfb-module-pushforward-pullback` |
| `sk-def-sfb-module-lower-shriek` | `sk-prop-sfb-cartesian-coefficients` | proof | `sk-def-sfb-module-pushforward-pullback` |
| `sk-def-sfb-module-lower-shriek` | `sk-prop-sfb-module-category` | proof | `sk-def-sfb-change-of-scalars` |
| `sk-def-sfb-module-objects` | `sk-def-sfb-ring-object` | statement | `sk-def-sfb-pulled-back-coefficients` |
| `sk-def-sfb-module-objects` | `sk-def-sfb-sheaf-tensor` | statement | `sk-def-sfb-pulled-back-coefficients` |
| `sk-def-sfb-module-pushforward-pullback` | `sk-def-sfb-change-of-scalars` | statement | `sk-def-sfb-transport` |
| `sk-def-sfb-module-pushforward-pullback` | `sk-def-sfb-coefficient-morphisms` | statement | `sk-prop-sfb-cartesian-coefficients` |
| `sk-def-sfb-module-pushforward-pullback` | `sk-def-sfb-condensed-ring` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-def-sfb-module-pushforward-pullback` | `sk-def-sfb-finite-pushforward-pullback` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-def-sfb-module-pushforward-pullback` | `sk-def-sfb-module-objects` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-def-sfb-module-pushforward-pullback` | `sk-def-sfb-pulled-back-coefficients` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-def-sfb-module-pushforward-pullback` | `sk-def-sfb-sheaf-tensor` | proof | `sk-def-sfb-change-of-scalars` |
| `sk-def-sfb-module-pushforward-pullback` | `sk-prop-sfb-module-category` | proof | `sk-def-sfb-change-of-scalars` |
| `sk-def-sfb-open-base-change` | `sk-def-sfb-dc-restricted-functors` | statement | `sk-def-sfb-base-change-morphism` |
| `sk-def-sfb-open-base-change` | `sk-def-sfb-dc-setting` | statement | `sk-def-sfb-base-change-morphism` |
| `sk-def-sfb-open-base-change` | `sk-def-sfb-module-pushforward-pullback` | proof | `sk-def-sfb-base-change-morphism` |
| `sk-def-sfb-open-base-change` | `sk-prop-sfb-module-derived-factorization` | proof | `sk-def-sfb-base-change-morphism` |
| `sk-def-sfb-pullback-from-point` | `sk-def-sfb-sheaf-tensor` | statement | `sk-def-sfb-condensed-ring` |
| `sk-def-sfb-pullback-from-point-comp` | `sk-def-sfb-finite-pushforward-pullback` | statement | `sk-def-sfb-pullback-from-point` |
| `sk-def-sfb-pullback-from-point-comp` | `sk-def-sfb-sheaf-tensor` | statement | `sk-def-sfb-finite-pushforward-pullback` |
| `sk-def-sfb-pulled-back-coefficients` | `sk-def-sfb-ring-object` | statement | `sk-def-sfb-pullback-from-point` |
| `sk-def-sfb-qlbar-condensed` | `sk-def-sfb-ring-object` | statement | `sk-def-sfb-condensed-ring` |
| `sk-def-sfb-shriek-base-change-morphism` | `sk-def-sfb-base-change-morphism` | statement | `sk-def-sfb-open-base-change` |
| `sk-def-sfb-shriek-base-change-morphism` | `sk-def-sfb-dc-setting` | statement | `sk-def-sfb-base-change-morphism` |
| `sk-def-sfb-transport` | `sk-def-sfb-module-objects` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-def-sfb-transport` | `sk-def-sfb-ring-object` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-prop-sfb-cartesian-coefficients` | `sk-def-sfb-finite-pushforward-pullback` | statement | `sk-def-sfb-coefficient-morphisms` |
| `sk-prop-sfb-cartesian-coefficients` | `sk-def-sfb-pullback-from-point-comp` | proof | `sk-def-sfb-coefficient-morphisms` |
| `sk-prop-sfb-finite-extension-compatibility` | `sk-def-sfb-change-of-scalars` | statement | `sk-def-sfb-coefficient-change` |
| `sk-prop-sfb-finite-extension-compatibility` | `sk-def-sfb-coefficient-change` | statement | `sk-def-sfb-coefficient-comparisons` |
| `sk-prop-sfb-finite-extension-compatibility` | `sk-def-sfb-condensed-ring` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-prop-sfb-finite-extension-compatibility` | `sk-def-sfb-pullback-from-point` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-prop-sfb-finite-extension-compatibility` | `sk-def-sfb-pulled-back-coefficients` | statement | `sk-def-sfb-change-of-scalars` |
| `sk-prop-sfb-finite-extension-compatibility` | `sk-def-sfb-qlbar-condensed` | statement | `sk-prop-sfb-qlbar-colimit-point` |
| `sk-prop-sfb-finite-extension-compatibility` | `sk-prop-sfb-qlbar-colimit-point` | statement | `sk-prop-sfb-qlbar-colimit-x` |
| `sk-prop-sfb-module-category` | `sk-def-sfb-pulled-back-coefficients` | statement | `sk-def-sfb-module-objects` |
| `sk-prop-sfb-module-category` | `sk-def-sfb-sheaf-tensor` | statement | `sk-def-sfb-module-objects` |
| `sk-prop-sfb-module-derived-factorization` | `sk-def-sfb-change-of-scalars` | statement | `sk-def-sfb-derived-extension-of-scalars` |
| `sk-prop-sfb-module-derived-factorization` | `sk-def-sfb-derived-categories` | statement | `sk-def-sfb-derived-extension-of-scalars` |
| `sk-prop-sfb-module-derived-factorization` | `sk-def-sfb-finite-pushforward-pullback` | proof | `sk-def-sfb-change-of-scalars` |
| `sk-prop-sfb-module-derived-factorization` | `sk-def-sfb-module-pushforward-pullback` | statement | `sk-def-sfb-module-derived-pushpull` |
| `sk-prop-sfb-module-derived-factorization` | `sk-def-sfb-transport` | statement | `sk-def-sfb-module-derived-pushpull` |
| `sk-prop-sfb-module-derived-factorization` | `sk-prop-sfb-module-category` | proof | `sk-def-sfb-change-of-scalars` |
| `sk-prop-sfb-module-derived-factorization` | `sk-prop-sfb-module-pullback-exact` | proof | `sk-def-sfb-module-derived-pushpull` |
| `sk-prop-sfb-module-pullback-exact` | `sk-def-sfb-change-of-scalars` | proof | `sk-def-sfb-module-pushforward-pullback` |
| `sk-prop-sfb-module-pullback-exact` | `sk-def-sfb-finite-pushforward-pullback` | proof | `sk-def-sfb-change-of-scalars` |
| `sk-prop-sfb-module-pullback-exact` | `sk-def-sfb-transport` | proof | `sk-def-sfb-module-pushforward-pullback` |
| `sk-prop-sfb-module-pullback-exact` | `sk-prop-sfb-cartesian-coefficients` | proof | `sk-def-sfb-module-pushforward-pullback` |
| `sk-prop-sfb-module-pullback-exact` | `sk-prop-sfb-module-category` | proof | `sk-def-sfb-change-of-scalars` |
| `sk-prop-sfb-qlbar-colimit-point` | `sk-def-sfb-condensed-ring` | statement | `sk-def-sfb-qlbar-condensed` |
| `sk-prop-sfb-qlbar-colimit-point` | `sk-def-sfb-ring-object` | statement | `sk-def-sfb-condensed-ring` |
| `sk-prop-sfb-qlbar-colimit-x` | `sk-def-sfb-condensed-ring` | statement | `sk-def-sfb-pullback-from-point` |
| `sk-prop-sfb-qlbar-colimit-x` | `sk-def-sfb-pullback-from-point` | proof | `sk-def-sfb-pulled-back-coefficients` |
| `sk-prop-sfb-qlbar-colimit-x` | `sk-def-sfb-qlbar-condensed` | statement | `sk-prop-sfb-qlbar-colimit-point` |
| `sk-thm-sfb-proper-base-change` | `sk-def-sfb-condensed-ring` | statement | `sk-def-sfb-base-change-morphism` |
| `sk-thm-sfb-proper-base-change` | `sk-def-sfb-qlbar-condensed` | statement | `sk-def-sfb-base-change-morphism` |
| `sk-thm-sfb-proper-base-change` | `sk-thm-sfb-qlbar-two-colimit` | proof | `sk-def-sfb-base-change-morphism` |
| `sk-thm-sfb-proper-base-change` | `sk-thm-sfb-rationalization-comparison` | proof | `sk-def-sfb-base-change-morphism` |
| `sk-thm-sfb-qlbar-two-colimit` | `sk-def-sfb-change-of-scalars` | statement | `sk-def-sfb-bounded-constructible` |
| `sk-thm-sfb-qlbar-two-colimit` | `sk-def-sfb-constructible` | proof | `sk-def-sfb-bounded-constructible` |
| `sk-thm-sfb-qlbar-two-colimit` | `sk-def-sfb-derived-categories` | statement | `sk-def-sfb-bounded-constructible` |
| `sk-thm-sfb-qlbar-two-colimit` | `sk-def-sfb-derived-extension-of-scalars` | statement | `sk-prop-sfb-finite-extension-compatibility` |
| `sk-thm-sfb-qlbar-two-colimit` | `sk-prop-sfb-qlbar-colimit-x` | proof | `sk-prop-sfb-finite-extension-compatibility` |
| `sk-thm-sfb-rationalization-comparison` | `sk-def-sfb-condensed-ring` | statement | `sk-def-sfb-bounded-constructible` |
| `sk-thm-sfb-rationalization-comparison` | `sk-def-sfb-constructible` | statement | `sk-def-sfb-bounded-constructible` |
| `sk-thm-sfb-rationalization-comparison` | `sk-def-sfb-pullback-from-point` | statement | `sk-def-sfb-bounded-constructible` |
| `sk-thm-sfb-rationalization-comparison` | `sk-def-sfb-pulled-back-coefficients` | statement | `sk-def-sfb-bounded-constructible` |
| `sk-thm-sfb-rationalization-comparison` | `sk-def-sfb-ring-object` | statement | `sk-def-sfb-bounded-constructible` |
| `sk-thm-sfb-rationalization-comparison` | `sk-prop-sfb-module-category` | statement | `sk-def-sfb-bounded-constructible` |
| `sk-thm-sfb-shriek-base-change` | `sk-def-sfb-condensed-ring` | statement | `sk-def-sfb-open-base-change` |
| `sk-thm-sfb-shriek-base-change` | `sk-def-sfb-open-base-change` | proof | `sk-def-sfb-shriek-base-change-morphism` |
| `sk-thm-sfb-shriek-base-change` | `sk-def-sfb-qlbar-condensed` | statement | `sk-def-sfb-open-base-change` |

### Not touched by A/B

- Cause 2 (the real cross-section dependencies) stays.
- Edges from the new section's children into other sections are real. Most are to
  `def-weil-pbc-proetale-site` and `sk-def-nagata-sketch-data`.
- Nothing outside the section uses it yet. Linking `sec-smooth-purity` / `sec-six-functors` to these basics is
  still an open design step, and it will add edges *into* the section.
