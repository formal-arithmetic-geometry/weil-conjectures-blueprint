# Lean alignment of the blueprint (from PRs #210–#233)

PRs #210–#216 and #218–#233 by littlebin530 aligned each chapter's layer 2 with the Lean formalisation. #217 is an unrelated blog PR. They rewrote clause texts, added clause proofs and new clauses, and changed `lean` and `uses` tags, all in the generated markdown only. Their reviews are in `LEAN-ALIGNMENT-PR-REVIEW*.md`. This PR takes what is right from them, in the sources, so that a later `scripts/retex.py` run keeps it. It replaces the 23 PRs.

## What is taken

**Clause texts (in `blueprint-layer-2.tex`).**
- **Rule.** A PR's rewrite of a clause or of a block's shared context is taken when it states what the tex states, made precise, or more general, and has no major issue: 245 texts. 7 new clauses are taken too, with their proofs.
- **Hand edits.** Before being taken, rewrites with a minor issue were edited:
  - Lean commentary was removed ("bypassed by the Lean route", Lean names, "mainline").
  - Notation clashes were fixed.
  - The declaration's own conclusion was added back where a rewrite had left it implicit.
- **Consistency check.** Every declaration with a taken clause was checked as a whole: do its clauses still fit together and still state the declaration? That check made 57 corrections and turned back 23 rewrites:
  - 19 because the proof following the clause (from #238) does not cover the rewritten statement;
  - 4 because kept neighbours depend on the old wording.
- **Not taken:**
  - Narrowed, changed or "bypassed" rewrites, which state less than the notes or something else. Their clauses keep the text of the notes.
  - The PRs' 639 clause proofs. #238 gave every clause a proof in the tex, and those stay.
- **Checks.** The tex compiles, with no undefined references. The 11 website macros that the taken texts use are defined in its preamble with `\providecommand`.

**Lean names.**
- **Placement.** Each name sits on the most specific node that states it: a clause rather than its declaration.
- **Totals.** Names on nodes go from 1077 to 1450: 373 new and none removed.
  - 475 clauses carry 678 names.
  - Declarations with a Lean name on themselves or a clause go from 431 to 435 of 541.
- **Names the PRs removed** stay where they were, unless they moved to a clause. Many of these were reviewed by hand in #193, or state the notes exactly.
- **Existence.** Every name exists at the pinned weil-conjectures `f3cad3b`, checked against the `.ilean` files of the built project. One PR name exists only at `08fcdf1` and is left out: `…CondensedRing.boundedConstructible_rightDerivedLowerStar_obj_of_ringChar_ne`.
- **Cycles.** With the Lean facts of #200, the finer placement made 5 cycles. As in #200, names were moved back to their declarations until none remained (6 nodes):
  - `proposition-pro-etale-affines-form-basis--1`: `AlgebraicGeometry.Scheme.AffineProEt.isCoverDense_toProEt`
  - `proposition-multiplication-n--1`: `AlgebraicGeometry.finrankΓ_torsionSubgroupScheme`, `AlgebraicGeometry.surjective_npow_id`
  - `proposition-comparison-etale-derived-category--4`: `AlgebraicGeometry.ProEtale.isIso_rightDerivedLowerStarComparisonPlusBaseChange`
  - `theorem-smooth-purity-all-admissible-coefficients--4`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_smoothOrientation`, `AlgebraicGeometry.ProEtale.CondensedRing.isIso_upperShriekUnitTensorMap_of_smooth`, `AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation`
  - `definition-exceptional-base-change-map--1`: `AlgebraicGeometry.Etale.rightDerivedUpperShriekBaseChangeMap`, `AlgebraicGeometry.ProEtale.CondensedRing.upperShriekBaseChange`
  - `definition-verdier-dual-evaluation--1`: `AlgebraicGeometry.Etale.dualizingComplex`, `AlgebraicGeometry.ProEtale.CondensedRing.dualizingComplex`
- **Record.** `LEAN-MAPPING.md` records the clause names: *aligned* (text taken), *partial* (Lean states a special case of the clause, whose narrower rewrite was not taken) or as before.

**Scripts.**
- `scripts/retex.py` now keeps a clause's `lean` (and the `uses` derived from it) through a regeneration. Before, `layer2bp.py` rewrote every clause and would have dropped them.
- `scripts/lean_uses.py` now treats a clause with Lean names like a declaration. It leaves out arrows between a declaration and its own clauses.

## Per PR

| PR | Chapter | Texts taken | Texts kept | New clauses taken | Nodes with only tag changes | Proofs not taken |
|---|---|---|---|---|---|---|
| #210 | 2 The pro-étale site | 34 | 55 | 0/0 | 68 | 76 |
| #211 | 3 Constructible complexes | 10 | 14 | 1/1 | 18 | 24 |
| #212 | 4 Proper base change | 17 | 40 | 0/1 | 33 | 49 |
| #213 | 5 Construction of f^! | 4 | 33 | 1/1 | 7 | 26 |
| #214 | 6 Constructibility of f^! | 7 | 21 | 0/0 | 9 | 20 |
| #215 | 7 The six operations | 14 | 37 | 0/0 | 15 | 47 |
| #216 | 8 Smooth base change | 5 | 16 | 0/0 | 16 | 21 |
| #218 | 9 Smooth purity | 2 | 19 | 0/0 | 13 | 17 |
| #219 | 10 Verdier and Poincaré duality | 2 | 49 | 0/0 | 19 | 39 |
| #220 | 11 The Lefschetz–Verdier formula | 2 | 13 | 0/0 | 21 | 14 |
| #221 | 12 The trace formula | 16 | 45 | 0/1 | 32 | 53 |
| #222 | 13 Weights | 19 | 9 | 0/0 | 14 | 25 |
| #223 | 14 Purity of real sheaves | 15 | 20 | 0/0 | 26 | 32 |
| #224 | 15 Pure sheaves on curves | 13 | 16 | 0/0 | 17 | 25 |
| #225 | 16 The Fourier transform | 9 | 29 | 0/0 | 18 | 25 |
| #226 | 17 Deligne–Laumon for curves | 4 | 5 | 0/0 | 6 | 9 |
| #227 | 18 Deligne–Laumon in general | 7 | 5 | 0/0 | 11 | 12 |
| #228 | 19 Proof of the Weil conjectures | 2 | 16 | 0/0 | 4 | 16 |
| #229 | A Nagata and Chow | 12 | 13 | 1/1 | 23 | 24 |
| #230 | B Abelian varieties | 7 | 11 | 0/0 | 11 | 15 |
| #231 | C The Picard scheme | 27 | 14 | 0/0 | 13 | 37 |
| #232 | D Torsion sheaves on curves | 11 | 16 | 4/4 | 8 | 26 |
| #233 | F Algebraic groups | 4 | 5 | 0/0 | 3 | 9 |

## Checks

- **`blueprint check`** (tool `c5071e0`, as pinned): 0 errors, 0 warnings, the same as `main`.
- **KaTeX:** 6231 formulas in the changed nodes, 0 errors.
- **`blueprint-layer-2.tex`** compiles with pdflatex, with no errors and no undefined references.
- **Round trip.**
  - Converting each taken text to LaTeX and back with `retex.py` gives the text again, apart from tex macros written out (e.g. `\Ql` becomes `\mathbf Q_\ell`).
  - A fresh `retex.py` run on this branch reproduces `blueprint/` except for `order` values and #238's not yet converted proofs.
  - It keeps the Lean names of all 475 named clauses.

## Follow-up (after #248)

- **#238's clause proofs on the website (item 2 above).**
  - #237 had the converter for them, but it was merged into its base branch `blueprint-lean-arrows` after #200 had reached `main`, so it never got there. Its `scripts/layer2bp.py` is now on `main`, and `blueprint/` is regenerated from `main`'s tex.
  - That adds 938 clause proofs and replaces the 164 old "Justification" proofs.
  - #235's wording of the introduction had been made in the markdown only. It is now in the readable tex, so the regeneration keeps it.
- **The 29 rewrites of items 3 and 4 above.** 26 are now taken, and every new statement and proof was refereed:
  - The 10 technical cases are all taken:
    - The cited equation labels stay on the same displays.
    - The two links to a hidden text node now point to the section "Coefficient sheaves".
    - Six of them have new proofs.
  - Of the 19 turned back for their proofs:
    - 7 are taken with new proofs: `lemma-extremally-disconnected-covers--2`, `lemma-extremally-disconnected-covers--3`, `corollary-evaluation-weakly-contractible-objects--7`, `lemma-lattices-lisse-e-sheaves--2`, `lemma-inverse-image-tensor-product--1`, `lemma-inverse-image-tensor-product--4`, `proposition-properties-trace--3`.
    - 9 are taken in a narrower form that their proof covers: `theorem-bounded-below-cohomology-comparison--2`, `proposition-comparison-immersions--2`, `corollary-finite-quotients-their-transition-maps--2`, `lemma-restriction-geometric-generic-fibre--2`, `lemma-restriction-geometric-generic-fibre--3`, `lemma-reduction-curve-over-normal-base--1`, `theorem-trace-isomorphism-top-degree--2`, `theorem-trace-isomorphism-top-degree--4`, `theorem-trace-isomorphism-top-degree--8`.
    - 3 stay as they were:
      - `proposition-inverting-ell--1`: The rewrite says that F(f)=F(g) implies l^n f = l^n g.
      - `proposition-proper-direct-image-constructible-complexes--4`: The rewrite claims that Rp_* preserves D^b_c with Qbar_l coefficients for an arbitrary separated finite type p, not only a proper one.
      - `theorem-verdier-biduality--1`: The rewrite states biduality over an arbitrary field k.
- **The *partial* clauses (item 5) are kept as they are.**

## Still to do

1. **The arrows.** `uses` are unchanged from `main`. Recomputing them by the rule of #200 needs a `lean-facts.json` covering the 373 new names.
   - With the next CI extraction, run `scripts/lean_uses.py lean-facts.json blueprint --write`.
   - Check for cycles among the new names.
   - Until then, `blueprint check --lean` will report the difference.
2. *(Done, see Follow-up.)* **#238's clause proofs** are in the tex but not yet in `blueprint/`. A full `retex.py` run still reports what the converter does not handle: `\BPProofAnchor`, `\pageref`, `\hyperref` and the provenance lines. Its hidden "text" nodes would show those anchors.
3. *(Done, see Follow-up.)* **Rewrites not applied for technical reasons**, which keep the notes' text:
   - 8 clauses whose text holds a labelled equation that other passages cite (the rewrite would delete the label): `theorem-bounded-below-cohomology-comparison--1`, `proposition-comparison-immersions--1`, `proposition-milnor-sequence--2`, `theorem-finite-etale-covers-proper-henselian--3`, `corollary-open-direct-image-over-field--1`, `theorem-generic-constructibility-base-change-rj--1`, `theorem-generic-constructibility-base-change-rj--2`, `theorem-smooth-base-change-all-admissible--1`.
   - 2 that link to a hidden text node: `lemma-inverse-image-coefficient-sheaves--1`, `lemma-inverse-image-coefficient-sheaves--4`.
4. *(16 done, see Follow-up.)* **The 19 rewrites turned back because their proofs do not cover them**: `lemma-extremally-disconnected-covers--2`, `lemma-extremally-disconnected-covers--3`, `corollary-evaluation-weakly-contractible-objects--7`, `theorem-bounded-below-cohomology-comparison--2`, `proposition-comparison-immersions--2`, `corollary-finite-quotients-their-transition-maps--2`, `lemma-lattices-lisse-e-sheaves--2`, `proposition-inverting-ell--1`, `proposition-proper-direct-image-constructible-complexes--4`, `lemma-inverse-image-tensor-product--1`, `lemma-inverse-image-tensor-product--4`, `lemma-restriction-geometric-generic-fibre--2`, `lemma-restriction-geometric-generic-fibre--3`, `proposition-properties-trace--3`, `lemma-reduction-curve-over-normal-base--1`, `theorem-verdier-biduality--1`, `theorem-trace-isomorphism-top-degree--2`, `theorem-trace-isomorphism-top-degree--4`, `theorem-trace-isomorphism-top-degree--8`. They can be taken once the clause proofs are extended.
5. *(Kept.)* **The 156 *partial* clauses** in `LEAN-MAPPING.md`. Lean states only a special case, so either the Lean statement is generalised or the clause is split.
6. **The weil-conjectures pin.** Moving it to `08fcdf1` or later would allow the one left-out name.
