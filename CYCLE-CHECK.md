# Cycle check of the blueprint

Arrows between declarations: `scripts/lean_uses.py` on the Lean facts of weil-conjectures.merten.dev (site build of main `ec5a392`, facts extracted at weil-conjectures `f3cad3be`). Sketch declarations have arrows to sketch declarations only, clauses (`<id>--<k>`) to clauses only, and a dependency path passing through a name of the other layer is followed. Arrows between chapters, sections and subsections: as on main, drawn from the text (PR #191).

"Main" below is `ec5a392` with its current declaration arrows; "new" is the same with the arrows above.

## How a cycle is read

Blocks are chapters (appendices too), sections and subsections. The order of the blocks is the one their own arrows give: the arrows between chapters, sections and subsections, each lifted to the level looked at (a subsection counts as its section, and so on). A declaration arrow *X uses Y* is **backward** when, at some level, Y's block uses X's block (directly or through other blocks) while X's block does not use Y's: Y comes later, yet X uses it. On the graph that is an arrow from a later block back to an earlier one. A proof counts where its file is (6 proofs sit in a later section than their statement, e.g. Nagata's theorem; their clauses' proofs go with them). Each arrow is listed once, at the coarsest level where it is backward.

## 1. The arrows between blocks

The arrows between chapters, sections and subsections are drawn from the text and are not touched by the declaration arrows. They have **no cycle** at any level, also when the section arrows are counted towards their chapters.

Until the split of section 5 they had one, between Proper base change (chapter 4) and Appendix D: chapter 4 uses Appendix D (`theorem-cohomology-curves` is stated in 4.4 and proved in D), while D.4 Normalization used 4.5 Proper morphisms (the stalk formula and exactness of `lemma-finite-morphisms`). Those two facts now open Appendix D as `lemma-finite-direct-images`, and every block arrow between chapter 4 and Appendix D runs from 4 to D.

## 2. Backward declaration arrows

| level | new | of which the tex cites | main | of which the tex cites |
|---|---|---|---|---|
| chapter | 470 (221 sketch, 249 detail) | 3 | 233 | 2 |
| section | 39 (18 sketch, 21 detail) | 2 | 36 | 2 |
| subsection | 5 (4 sketch, 1 detail) | 0 | 3 | 0 |

"The tex cites" means that the text of X (its statement, its clauses, or their proofs) links to Y or to a clause of Y. For all others the dependency is Lean's alone: the Lean proof goes another way than the tex. Example: in Lean the Brauer-group clause `lemma-cohomology-multiplicative-group--6` (Kummer theory) is proved with `lemma-finite-morphisms-cohomology--2`, which the tex states later, in Normalization; the tex proof does not use it.

The five that the tex cites:

- `proof/corollary-finite-tor-amplitude-under-comparison--1` uses `definition-constructible-sheaves--5` (The pro-étale site, then Constructible complexes): the clause takes the meaning of Tor amplitude from the later definition, a forward reference in the tex.
- `proof/theorem-weight-bound-affine-curve` uses `lemma-finite-quasi-finite-direct-images` (Deligne–Laumon for curves, then in general): the tex says "whose proof is the same computation", a comparison, not a use.
- `lemma-removing-finitely-many-points` uses `theorem-cohomology-curves` (Appendix D, then Proper base change): the lemma is a step of the proof of that theorem and names its assertions (C1)–(C8); it does not use the theorem.
- `theorem-smooth-purity-all-admissible-coefficients--2` and `--9` use `proposition-sp-unique-adjoint--1` (Statement, then ℓ-adic coefficients): the clauses state the designated isomorphism, which is built with the later proposition.

### Chapter level: 470 arrows

| earlier block (uses) | later block (used) | arrows | tex cites |
|---|---|---|---|
| `chap-Construction-of-f` | `chap-The-six-operations-on-Dbctf` | 71 | 0 |
| `chap-Constructibility-of-f` | `chap-Smooth-base-change` | 39 | 0 |
| `chap-Proper-base-change` | `chap-The-six-operations-on-Dbctf` | 30 | 0 |
| `chap-Construction-of-f` | `chap-Constructibility-of-f` | 25 | 0 |
| `chap-Constructibility-of-f` | `chap-The-six-operations-on-Dbctf` | 24 | 0 |
| `chap-Proper-base-change` | `chap-Construction-of-f` | 22 | 0 |
| `chap-The-six-operations-on-Dbctf` | `chap-Smooth-purity` | 18 | 0 |
| `chap-Construction-of-f` | `chap-Smooth-purity` | 16 | 0 |
| `chap-Cohomology-of-torsion-sheaves-on-curves` | `chap-Proper-base-change` | 15 | 1 |
| `chap-Constructible-complexes` | `chap-Proper-base-change` | 15 | 0 |
| `chap-The-pro-etale-site` | `chap-Proper-base-change` | 13 | 0 |
| `chap-Proper-base-change` | `chap-Smooth-base-change` | 12 | 0 |
| `chap-The-Lefschetz-Verdier-formula` | `chap-The-Fourier-transform` | 11 | 0 |
| `chap-Constructible-complexes` | `chap-The-six-operations-on-Dbctf` | 8 | 0 |
| `chap-Proper-base-change` | `chap-Smooth-purity` | 8 | 0 |
| `chap-Constructibility-of-f` | `chap-Smooth-purity` | 8 | 0 |
| `chap-The-Picard-scheme-of-a-curve` | `chap-Proper-base-change` | 7 | 0 |
| `chap-Nagata-compactification-and-Chows-lemma` | `chap-Proper-base-change` | 7 | 0 |
| `chap-The-Deligne-Laumon-theorem-for-curves` | `chap-The-Deligne-Laumon-theorem-in-general` | 7 | 1 |
| `chap-Construction-of-f` | `chap-Smooth-base-change` | 7 | 0 |
| `chap-Verdier-and-Poincare-duality` | `chap-The-trace-formula` | 6 | 0 |
| `chap-Abelian-varieties` | `chap-The-Picard-scheme-of-a-curve` | 6 | 0 |
| `chap-Constructible-complexes` | `chap-Smooth-purity` | 5 | 0 |
| `chap-The-trace-formula` | `chap-The-Fourier-transform` | 5 | 0 |
| `chap-Abelian-varieties` | `chap-Proper-base-change` | 5 | 0 |
| `chap-The-six-operations-on-Dbctf` | `chap-Smooth-base-change` | 5 | 0 |
| `chap-The-pro-etale-site` | `chap-Nagata-compactification-and-Chows-lemma` | 4 | 0 |
| `chap-Cohomology-of-torsion-sheaves-on-curves` | `chap-Purity-of-real-sheaves` | 4 | 0 |
| `chap-Cohomology-of-torsion-sheaves-on-curves` | `chap-Smooth-base-change` | 4 | 0 |
| `chap-Proper-base-change` | `chap-Constructibility-of-f` | 4 | 0 |
| `chap-The-pro-etale-site` | `chap-The-six-operations-on-Dbctf` | 3 | 0 |
| `chap-Nagata-compactification-and-Chows-lemma` | `chap-The-six-operations-on-Dbctf` | 3 | 0 |
| `chap-Nagata-compactification-and-Chows-lemma` | `chap-Constructibility-of-f` | 3 | 0 |
| `chap-Pure-sheaves-on-curves` | `chap-The-Deligne-Laumon-theorem-in-general` | 3 | 0 |
| `chap-The-six-operations-on-Dbctf` | `chap-Verdier-and-Poincare-duality` | 3 | 0 |
| `chap-Smooth-purity` | `chap-The-Fourier-transform` | 3 | 0 |
| `chap-Verdier-and-Poincare-duality` | `chap-Pure-sheaves-on-curves` | 2 | 0 |
| `chap-Verdier-and-Poincare-duality` | `chap-Weights` | 2 | 0 |
| `chap-The-trace-formula` | `chap-The-Deligne-Laumon-theorem-in-general` | 2 | 0 |
| `chap-The-trace-formula` | `chap-Proof-of-the-Weil-conjectures` | 2 | 0 |
| `chap-The-trace-formula` | `chap-Weights` | 2 | 0 |
| `chap-The-Picard-scheme-of-a-curve` | `chap-Smooth-purity` | 2 | 0 |
| `chap-Purity-of-real-sheaves` | `chap-Pure-sheaves-on-curves` | 2 | 0 |
| `chap-Purity-of-real-sheaves` | `chap-The-Deligne-Laumon-theorem-in-general` | 2 | 0 |
| `chap-The-pro-etale-site` | `chap-The-Picard-scheme-of-a-curve` | 2 | 0 |
| `chap-Weights` | `chap-Pure-sheaves-on-curves` | 2 | 0 |
| `chap-Proper-base-change` | `chap-Purity-of-real-sheaves` | 2 | 0 |
| `chap-The-trace-formula` | `chap-Pure-sheaves-on-curves` | 2 | 0 |
| `chap-The-Lefschetz-Verdier-formula` | `chap-The-trace-formula` | 2 | 0 |
| `chap-Algebraic-groups-in-characteristic-zero` | `chap-Purity-of-real-sheaves` | 1 | 0 |
| `chap-The-pro-etale-site` | `chap-Constructible-complexes` | 1 | 1 |
| `chap-Purity-of-real-sheaves` | `chap-Proof-of-the-Weil-conjectures` | 1 | 0 |
| `chap-The-Picard-scheme-of-a-curve` | `chap-Verdier-and-Poincare-duality` | 1 | 0 |
| `chap-Constructible-complexes` | `chap-Verdier-and-Poincare-duality` | 1 | 0 |
| `chap-Verdier-and-Poincare-duality` | `chap-The-Fourier-transform` | 1 | 0 |
| `chap-Nagata-compactification-and-Chows-lemma` | `chap-Smooth-base-change` | 1 | 0 |
| `chap-Construction-of-f` | `chap-Weights` | 1 | 0 |
| `chap-Weights` | `chap-The-Fourier-transform` | 1 | 0 |
| `chap-Smooth-base-change` | `chap-Purity-of-real-sheaves` | 1 | 0 |
| `chap-The-Fourier-transform` | `chap-The-Deligne-Laumon-theorem-in-general` | 1 | 0 |
| `chap-Constructibility-of-f` | `chap-Verdier-and-Poincare-duality` | 1 | 0 |
| `chap-The-trace-formula` | `chap-Purity-of-real-sheaves` | 1 | 0 |
| `chap-Pure-sheaves-on-curves` | `chap-Proof-of-the-Weil-conjectures` | 1 | 0 |
| `chap-The-Picard-scheme-of-a-curve` | `chap-Purity-of-real-sheaves` | 1 | 0 |

<details><summary>All arrows</summary>

- `proof/lemma-triviality-near-fibre` uses `lemma-acyclic-resolutions` (chap-Abelian-varieties → chap-Proper-base-change)
- `proof/proposition-integral-tate-module` uses `lemma-acyclic-resolutions` (chap-Abelian-varieties → chap-Proper-base-change)
- `proof/proposition-multiplication-n` uses `lemma-acyclic-resolutions` (chap-Abelian-varieties → chap-Proper-base-change)
- `proof/proposition-no-frobenius-fixed-vector` uses `lemma-acyclic-resolutions` (chap-Abelian-varieties → chap-Proper-base-change)
- `proof/theorem-theorem-cube` uses `lemma-acyclic-resolutions` (chap-Abelian-varieties → chap-Proper-base-change)
- `proof/lemma-triviality-fibres--2` uses `lemma-coherent-base-change-invertible-sheaves--1` (chap-Abelian-varieties → chap-The-Picard-scheme-of-a-curve)
- `proof/lemma-triviality-near-fibre--1` uses `lemma-coherent-base-change-invertible-sheaves--1` (chap-Abelian-varieties → chap-The-Picard-scheme-of-a-curve)
- `proof/proposition-integral-tate-module--2` uses `corollary-torsion-jacobian-field-extension--1` (chap-Abelian-varieties → chap-The-Picard-scheme-of-a-curve)
- `proof/proposition-integral-tate-module--2` uses `corollary-torsion-jacobian-field-extension--3` (chap-Abelian-varieties → chap-The-Picard-scheme-of-a-curve)
- `proof/proposition-multiplication-n--1` uses `theorem-picard-scheme-jacobian-over-separably--1` (chap-Abelian-varieties → chap-The-Picard-scheme-of-a-curve)
- `proof/proposition-multiplication-n--2` uses `theorem-picard-scheme-jacobian-over-separably--1` (chap-Abelian-varieties → chap-The-Picard-scheme-of-a-curve)
- `lemma-stable-subspaces-center` uses `lemma-normality-geometric-monodromy` (chap-Algebraic-groups-in-characteristic-zero → chap-Purity-of-real-sheaves)
- `lemma-removing-finitely-many-points` uses `theorem-cohomology-curves` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change) — tex cites it
- `proof/lemma-cohomology-multiplicative-group` uses `lemma-acyclic-resolutions` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proof/lemma-cohomology-multiplicative-group` uses `proposition-cohomology-p-1-over-henselian` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proof/lemma-normalization-constant-sheaf` uses `lemma-acyclic-resolutions` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proof/lemma-removing-finitely-many-points` uses `proposition-cohomology-p-1-over-henselian` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proof/lemma-removing-finitely-many-points--1` uses `definition-underived-base-change-map--1` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proof/lemma-removing-finitely-many-points--1` uses `lemma-finite-morphisms--1` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proof/proposition-cohomology-smooth-affine-curve` uses `lemma-acyclic-resolutions` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proof/proposition-cohomology-smooth-affine-curve--2` uses `theorem-cohomology-curves--2` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proof/proposition-p-torsion-smooth-proper-curve` uses `definition-derived-base-change-map` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proof/proposition-p-torsion-smooth-proper-curve` uses `lemma-acyclic-resolutions` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proof/proposition-p-torsion-smooth-proper-curve` uses `lemma-cohomology-modules-underlying-abelian` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proof/proposition-p-torsion-smooth-proper-curve` uses `proposition-cohomology-p-1-over-henselian` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proof/proposition-smooth-proper-curves-torsion-prime` uses `proposition-cohomology-p-1-over-henselian` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proposition-smooth-proper-curves-torsion-prime` uses `lemma-acyclic-resolutions` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Proper-base-change)
- `proof/proposition-cohomology-smooth-affine-curve--2` uses `lemma-proper-smooth-model--1` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Purity-of-real-sheaves)
- `proof/proposition-cohomology-smooth-affine-curve--3` uses `lemma-proper-smooth-model--1` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Purity-of-real-sheaves)
- `proof/proposition-cohomology-smooth-affine-curve--4` uses `lemma-proper-smooth-model--1` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Purity-of-real-sheaves)
- `proof/proposition-p-torsion-smooth-proper-curve--3` uses `lemma-proper-smooth-model--1` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Purity-of-real-sheaves)
- `proof/proposition-p-torsion-smooth-proper-curve` uses `lemma-degree-zero-calculation` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Smooth-base-change)
- `proof/proposition-p-torsion-smooth-proper-curve` uses `lemma-reduction-curve-over-normal-base` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Smooth-base-change)
- `proof/proposition-p-torsion-smooth-proper-curve` uses `lemma-reduction-field` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Smooth-base-change)
- `proof/proposition-p-torsion-smooth-proper-curve` uses `proposition-base-change-larger-algebraically-closed` (chap-Cohomology-of-torsion-sheaves-on-curves → chap-Smooth-base-change)
- `lemma-class-diagonal-projective-line` uses `lemma-degree-zero-calculation` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `lemma-class-diagonal-projective-line` uses `lemma-kunneth-field-coefficients` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `lemma-class-diagonal-projective-line` uses `lemma-reduction-curve-over-normal-base` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `lemma-class-diagonal-projective-line` uses `lemma-reduction-field` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `lemma-class-diagonal-projective-line` uses `proposition-base-change-larger-algebraically-closed` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/corollary-open-direct-image-over-field--2` uses `theorem-smooth-base-change-classical-torsion--1` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/lemma-affine-space-etale-localization` uses `lemma-degree-zero-calculation` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/lemma-affine-space-etale-localization` uses `lemma-kunneth-field-coefficients` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/lemma-affine-space-etale-localization` uses `lemma-reduction-curve-over-normal-base` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/lemma-affine-space-etale-localization` uses `lemma-reduction-field` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/lemma-affine-space-etale-localization` uses `proposition-base-change-larger-algebraically-closed` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/lemma-projection-formula-integral-coefficients` uses `lemma-change-coefficients` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-adjunction-projective-line` uses `lemma-degree-zero-calculation` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-adjunction-projective-line` uses `lemma-reduction-curve-over-normal-base` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-adjunction-projective-line` uses `lemma-reduction-field` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-adjunction-projective-line` uses `proposition-base-change-larger-algebraically-closed` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-exceptional-inverse-image-smooth-morphism` uses `lemma-degree-zero-calculation` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-exceptional-inverse-image-smooth-morphism` uses `lemma-kunneth-field-coefficients` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-exceptional-inverse-image-smooth-morphism` uses `lemma-reduction-curve-over-normal-base` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-exceptional-inverse-image-smooth-morphism` uses `lemma-reduction-field` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-exceptional-inverse-image-smooth-morphism` uses `proposition-base-change-larger-algebraically-closed` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--5` uses `lemma-kunneth-one-identity-factor--1` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--5` uses `theorem-smooth-base-change-classical-torsion--1` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--5` uses `theorem-smooth-base-change-classical-torsion-2--1` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--6` uses `lemma-kunneth-one-identity-factor--1` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--6` uses `theorem-smooth-base-change-classical-torsion--1` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--6` uses `theorem-smooth-base-change-classical-torsion-2--1` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/proposition-projection-formula-rational-coefficients` uses `lemma-change-coefficients` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/theorem-f-shriek-ell-adic-coefficients` uses `lemma-degree-zero-calculation` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/theorem-f-shriek-ell-adic-coefficients` uses `lemma-kunneth-field-coefficients` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/theorem-f-shriek-ell-adic-coefficients` uses `lemma-reduction-curve-over-normal-base` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/theorem-f-shriek-ell-adic-coefficients` uses `lemma-reduction-field` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/theorem-f-shriek-ell-adic-coefficients` uses `proposition-base-change-larger-algebraically-closed` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/theorem-f-shriek-finite-coefficients` uses `lemma-degree-zero-calculation` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/theorem-f-shriek-finite-coefficients` uses `lemma-kunneth-field-coefficients` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/theorem-f-shriek-finite-coefficients` uses `lemma-reduction-curve-over-normal-base` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/theorem-f-shriek-finite-coefficients` uses `lemma-reduction-field` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/theorem-f-shriek-finite-coefficients` uses `proposition-base-change-larger-algebraically-closed` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proposition-adjunction-projective-line` uses `lemma-kunneth-field-coefficients` (chap-Constructibility-of-f → chap-Smooth-base-change)
- `proof/corollary-open-direct-image-over-field--2` uses `proposition-sp-unique-adjoint--1` (chap-Constructibility-of-f → chap-Smooth-purity)
- `proof/lemma-smooth-morphisms-locally-constant-sheaves` uses `definition-relative-dualizing-complex` (chap-Constructibility-of-f → chap-Smooth-purity)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--5` uses `proposition-sp-unique-adjoint--1` (chap-Constructibility-of-f → chap-Smooth-purity)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--6` uses `proposition-sp-unique-adjoint--1` (chap-Constructibility-of-f → chap-Smooth-purity)
- `proof/theorem-f-shriek-ell-adic-coefficients` uses `definition-relative-dualizing-complex` (chap-Constructibility-of-f → chap-Smooth-purity)
- `proof/theorem-f-shriek-finite-coefficients` uses `definition-relative-dualizing-complex` (chap-Constructibility-of-f → chap-Smooth-purity)
- `proof/theorem-generic-constructibility-base-change-rj--2` uses `proposition-sp-unique-adjoint--1` (chap-Constructibility-of-f → chap-Smooth-purity)
- `proposition-exceptional-inverse-image-smooth-morphism` uses `definition-relative-dualizing-complex` (chap-Constructibility-of-f → chap-Smooth-purity)
- `lemma-cohomology-projective-line-trace` uses `proposition-six-operations-change-coefficients` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/lemma-affine-space-etale-localization` uses `proposition-six-operations-change-coefficients` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/lemma-cycle-class-cartier-divisor` uses `proposition-six-operations-change-coefficients` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/lemma-projection-formula-integral-coefficients` uses `proposition-six-operations-change-coefficients` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/lemma-smooth-morphisms-locally-constant-sheaves` uses `proposition-six-operations-change-coefficients` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-direct-image-along-open-immersion` uses `definition-change-of-coefficients-maps` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-direct-image-along-open-immersion` uses `proposition-dctf-x-qbar-2-colimit` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-direct-image-along-open-immersion` uses `proposition-six-operations-change-coefficients` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-exceptional-inverse-image-smooth-morphism` uses `proposition-six-operations-change-coefficients` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--4` uses `definition-change-of-coefficients-maps--6` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--4` uses `proposition-six-operations-change-coefficients--23` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--5` uses `definition-change-of-coefficients-maps--6` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--5` uses `proposition-six-operations-change-coefficients--23` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--6` uses `definition-change-of-coefficients-maps--6` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-exceptional-inverse-image-smooth-morphism--6` uses `proposition-six-operations-change-coefficients--23` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-projection-formula-rational-coefficients` uses `definition-change-of-coefficients-maps` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-projection-formula-rational-coefficients` uses `proposition-dctf-x-qbar-2-colimit` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-projection-formula-rational-coefficients` uses `proposition-six-operations-change-coefficients` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/theorem-f-shriek-ell-adic-coefficients` uses `definition-change-of-coefficients-maps` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/theorem-f-shriek-ell-adic-coefficients` uses `proposition-dctf-x-qbar-2-colimit` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/theorem-f-shriek-ell-adic-coefficients` uses `proposition-six-operations-change-coefficients` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/theorem-f-shriek-finite-coefficients` uses `proposition-six-operations-change-coefficients` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/theorem-generic-constructibility-base-change-rj--2` uses `definition-change-of-coefficients-maps--6` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/theorem-generic-constructibility-base-change-rj--2` uses `proposition-six-operations-change-coefficients--23` (chap-Constructibility-of-f → chap-The-six-operations-on-Dbctf)
- `proof/theorem-generic-constructibility-base-change-rj--2` uses `definition-verdier-dual-evaluation--3` (chap-Constructibility-of-f → chap-Verdier-and-Poincare-duality)
- `proof/corollary-coefficient-heart-b` uses `lemma-acyclic-resolutions` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/lemma-bounds-finite-reductions` uses `lemma-acyclic-resolutions` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/lemma-continuity-ext-out-constructible-complex` uses `lemma-acyclic-resolutions` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/lemma-descent-finite-coefficient-field` uses `lemma-acyclic-resolutions` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/lemma-flat-models-generators` uses `definition-derived-base-change-map` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/lemma-flat-models-generators` uses `lemma-acyclic-resolutions` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/lemma-flat-models-generators` uses `proposition-cohomology-p-1-over-henselian` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/lemma-flat-models-generators` uses `proposition-proper-base-change-degree-zero` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/lemma-flat-models-generators` uses `proposition-proper-base-change-etale-site` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/lemma-flat-models-generators` uses `proposition-proper-base-change-projective-line` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/lemma-flat-models-generators` uses `theorem-proper-base-change-classical-pro` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/lemma-integral-models` uses `lemma-acyclic-resolutions` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/proposition-ctf-equals-bc` uses `lemma-acyclic-resolutions` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/proposition-integral-constructibility-criterion` uses `lemma-acyclic-resolutions` (chap-Constructible-complexes → chap-Proper-base-change)
- `proof/proposition-inverting-ell` uses `lemma-acyclic-resolutions` (chap-Constructible-complexes → chap-Proper-base-change)
- `lemma-constructible-sheaves--7` uses `proposition-sp-unique-adjoint--1` (chap-Constructible-complexes → chap-Smooth-purity)
- `proof/lemma-integral-models--2` uses `proposition-sp-unique-adjoint--1` (chap-Constructible-complexes → chap-Smooth-purity)
- `proof/lemma-lattices-lisse-e-sheaves--2` uses `proposition-sp-unique-adjoint--1` (chap-Constructible-complexes → chap-Smooth-purity)
- `proof/proposition-integral-constructibility-criterion--1` uses `proposition-sp-unique-adjoint--1` (chap-Constructible-complexes → chap-Smooth-purity)
- `proof/proposition-inverting-ell--2` uses `proposition-sp-unique-adjoint--1` (chap-Constructible-complexes → chap-Smooth-purity)
- `lemma-descent-finite-coefficient-field` uses `proposition-dctf-x-qbar-2-colimit` (chap-Constructible-complexes → chap-The-six-operations-on-Dbctf)
- `proof/lemma-continuity-ext-out-constructible-complex` uses `proposition-six-operations-change-coefficients` (chap-Constructible-complexes → chap-The-six-operations-on-Dbctf)
- `proof/lemma-descent-finite-coefficient-field` uses `proposition-six-operations-change-coefficients` (chap-Constructible-complexes → chap-The-six-operations-on-Dbctf)
- `proof/lemma-descent-lisse-qbar-sheaves-finite` uses `proposition-six-operations-change-coefficients` (chap-Constructible-complexes → chap-The-six-operations-on-Dbctf)
- `proof/proposition-inverting-ell` uses `proposition-six-operations-change-coefficients` (chap-Constructible-complexes → chap-The-six-operations-on-Dbctf)
- `proof/proposition-inverting-ell--2` uses `definition-change-of-coefficients-maps--6` (chap-Constructible-complexes → chap-The-six-operations-on-Dbctf)
- `proof/proposition-inverting-ell--2` uses `proposition-six-operations-change-coefficients--23` (chap-Constructible-complexes → chap-The-six-operations-on-Dbctf)
- `proposition-inverting-ell--2` uses `proposition-six-operations-change-coefficients--1` (chap-Constructible-complexes → chap-The-six-operations-on-Dbctf)
- `proof/lemma-integral-models--2` uses `lemma-perfect-complexes-geometric-point--1` (chap-Constructible-complexes → chap-Verdier-and-Poincare-duality)
- `proof/proposition-compactness-finite-coefficients` uses `lemma-extension-across-finite-subset` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-compactness-finite-coefficients` uses `lemma-generic-smooth-open` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-compactness-finite-coefficients` uses `lemma-smooth-morphisms-locally-constant-sheaves` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `definition-exceptional-base-change-finite` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `lemma-extension-across-finite-subset` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `lemma-generic-smooth-open` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `lemma-smooth-morphisms-locally-constant-sheaves` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `proposition-adjunction-projective-line` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-construction-independence-rf-shriek` uses `lemma-extension-across-finite-subset` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-construction-independence-rf-shriek` uses `lemma-generic-smooth-open` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-construction-independence-rf-shriek` uses `lemma-smooth-morphisms-locally-constant-sheaves` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-proper-base-change-localizing-categories` uses `lemma-extension-across-finite-subset` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-proper-base-change-localizing-categories` uses `lemma-generic-smooth-open` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-proper-base-change-localizing-categories` uses `lemma-smooth-morphisms-locally-constant-sheaves` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proposition-composition-base-change-rf-shriek--1` uses `corollary-open-direct-image-over-field--1` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proposition-composition-base-change-rf-shriek--2` uses `corollary-open-direct-image-over-field--1` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proposition-composition-base-change-rf-shriek--3` uses `corollary-open-direct-image-over-field--1` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proposition-composition-base-change-rf-shriek--5` uses `corollary-open-direct-image-over-field--1` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proposition-composition-base-change-rf-shriek--6` uses `corollary-open-direct-image-over-field--1` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proposition-composition-open-restriction-compactifications-f--1` uses `corollary-open-direct-image-over-field--1` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-exceptional-inverse-image-smooth-morphism--5` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proposition-composition-open-restriction-compactifications-f--2` uses `corollary-open-direct-image-over-field--1` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proposition-composition-open-restriction-compactifications-f--2` uses `proposition-exceptional-inverse-image-smooth-morphism--5` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proposition-composition-open-restriction-compactifications-f--4` uses `corollary-open-direct-image-over-field--1` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-exceptional-inverse-image-smooth-morphism--5` (chap-Construction-of-f → chap-Constructibility-of-f)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `lemma-change-coefficients` (chap-Construction-of-f → chap-Smooth-base-change)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `lemma-degree-zero-calculation` (chap-Construction-of-f → chap-Smooth-base-change)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `lemma-kunneth-field-coefficients` (chap-Construction-of-f → chap-Smooth-base-change)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `lemma-reduction-curve-over-normal-base` (chap-Construction-of-f → chap-Smooth-base-change)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `lemma-reduction-field` (chap-Construction-of-f → chap-Smooth-base-change)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `proposition-base-change-larger-algebraically-closed` (chap-Construction-of-f → chap-Smooth-base-change)
- `proof/proposition-proper-base-change-localizing-categories` uses `lemma-change-coefficients` (chap-Construction-of-f → chap-Smooth-base-change)
- `proof/lemma-inverse-image-tensor-product--2` uses `proposition-sp-unique-adjoint--1` (chap-Construction-of-f → chap-Smooth-purity)
- `proof/lemma-inverse-image-tensor-product--3` uses `proposition-sp-unique-adjoint--1` (chap-Construction-of-f → chap-Smooth-purity)
- `proof/lemma-inverse-image-tensor-product--4` uses `proposition-sp-unique-adjoint--1` (chap-Construction-of-f → chap-Smooth-purity)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `definition-relative-dualizing-complex` (chap-Construction-of-f → chap-Smooth-purity)
- `proposition-composition-base-change-rf-shriek--1` uses `proposition-sp-unique-adjoint--1` (chap-Construction-of-f → chap-Smooth-purity)
- `proposition-composition-base-change-rf-shriek--2` uses `proposition-sp-unique-adjoint--1` (chap-Construction-of-f → chap-Smooth-purity)
- `proposition-composition-base-change-rf-shriek--3` uses `proposition-sp-unique-adjoint--1` (chap-Construction-of-f → chap-Smooth-purity)
- `proposition-composition-base-change-rf-shriek--4` uses `proposition-sp-unique-adjoint--1` (chap-Construction-of-f → chap-Smooth-purity)
- `proposition-composition-base-change-rf-shriek--5` uses `proposition-sp-unique-adjoint--1` (chap-Construction-of-f → chap-Smooth-purity)
- `proposition-composition-base-change-rf-shriek--6` uses `proposition-sp-unique-adjoint--1` (chap-Construction-of-f → chap-Smooth-purity)
- `proposition-composition-open-restriction-compactifications-f--1` uses `definition-sp-scalar-extension--2` (chap-Construction-of-f → chap-Smooth-purity)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-sp-unique-adjoint--1` (chap-Construction-of-f → chap-Smooth-purity)
- `proposition-composition-open-restriction-compactifications-f--2` uses `definition-sp-scalar-extension--2` (chap-Construction-of-f → chap-Smooth-purity)
- `proposition-composition-open-restriction-compactifications-f--2` uses `proposition-sp-unique-adjoint--1` (chap-Construction-of-f → chap-Smooth-purity)
- `proposition-composition-open-restriction-compactifications-f--4` uses `definition-sp-scalar-extension--2` (chap-Construction-of-f → chap-Smooth-purity)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-sp-unique-adjoint--1` (chap-Construction-of-f → chap-Smooth-purity)
- `proof/lemma-inverse-image-tensor-product` uses `proposition-six-operations-change-coefficients` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/lemma-inverse-image-tensor-product--2` uses `definition-change-of-coefficients-maps--6` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/lemma-inverse-image-tensor-product--2` uses `proposition-six-operations-change-coefficients--23` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/lemma-uniform-bound-proper-direct-image` uses `definition-change-of-coefficients-maps` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/lemma-uniform-bound-proper-direct-image` uses `proposition-dctf-x-qbar-2-colimit` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/lemma-uniform-bound-proper-direct-image` uses `proposition-six-operations-change-coefficients` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/lemma-uniform-ext-bound` uses `definition-change-of-coefficients-maps` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/lemma-uniform-ext-bound` uses `proposition-six-operations-change-coefficients` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-compactness-finite-coefficients` uses `proposition-six-operations-change-coefficients` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-compactness-proper-direct-image` uses `proposition-six-operations-change-coefficients` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `definition-change-of-coefficients-maps` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `proposition-dctf-x-qbar-2-colimit` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-composition-open-restriction-compactifications-f` uses `proposition-six-operations-change-coefficients` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-construction-independence-rf-shriek` uses `definition-change-of-coefficients-maps` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-construction-independence-rf-shriek` uses `proposition-dctf-x-qbar-2-colimit` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-construction-independence-rf-shriek` uses `proposition-six-operations-change-coefficients` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-ind-constructible-sheaves` uses `proposition-six-operations-change-coefficients` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-base-change-localizing-categories` uses `definition-change-of-coefficients-maps` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-base-change-localizing-categories` uses `proposition-dctf-x-qbar-2-colimit` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-base-change-localizing-categories` uses `proposition-six-operations-change-coefficients` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-extension-zero` uses `definition-change-of-coefficients-maps` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-extension-zero` uses `proposition-dctf-x-qbar-2-colimit` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-extension-zero` uses `proposition-six-operations-change-coefficients` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/theorem-compactness-rational-coefficients` uses `proposition-six-operations-change-coefficients` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--1` uses `definition-change-of-coefficients-maps--6` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--1` uses `proposition-dctf-x-qbar-2-colimit--2` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--1` uses `proposition-six-operations-change-coefficients--1` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--1` uses `proposition-six-operations-change-coefficients--23` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--2` uses `definition-change-of-coefficients-maps--6` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--2` uses `proposition-dctf-x-qbar-2-colimit--2` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--2` uses `proposition-six-operations-change-coefficients--1` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--2` uses `proposition-six-operations-change-coefficients--23` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--3` uses `definition-change-of-coefficients-maps--6` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--3` uses `proposition-dctf-x-qbar-2-colimit--2` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--3` uses `proposition-six-operations-change-coefficients--1` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--3` uses `proposition-six-operations-change-coefficients--23` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--5` uses `definition-change-of-coefficients-maps--6` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--5` uses `proposition-dctf-x-qbar-2-colimit--2` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--5` uses `proposition-six-operations-change-coefficients--1` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--5` uses `proposition-six-operations-change-coefficients--23` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--6` uses `definition-change-of-coefficients-maps--6` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--6` uses `proposition-dctf-x-qbar-2-colimit--2` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--6` uses `proposition-six-operations-change-coefficients--1` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-base-change-rf-shriek--6` uses `proposition-six-operations-change-coefficients--23` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--1` uses `definition-change-of-coefficients-maps--6` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--1` uses `lemma-change-coefficients-exceptional-inverse-image--4` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-dctf-x-qbar-2-colimit--2` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-dctf-x-qbar-2-colimit--3` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-six-operations-change-coefficients--1` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-six-operations-change-coefficients--2` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-six-operations-change-coefficients--23` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-six-operations-change-coefficients--3` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-six-operations-change-coefficients--9` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--2` uses `definition-change-of-coefficients-maps--6` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--2` uses `lemma-change-coefficients-exceptional-inverse-image--4` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--2` uses `proposition-dctf-x-qbar-2-colimit--2` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--2` uses `proposition-dctf-x-qbar-2-colimit--3` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--2` uses `proposition-six-operations-change-coefficients--1` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--2` uses `proposition-six-operations-change-coefficients--2` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--2` uses `proposition-six-operations-change-coefficients--23` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--2` uses `proposition-six-operations-change-coefficients--3` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--2` uses `proposition-six-operations-change-coefficients--9` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--4` uses `definition-change-of-coefficients-maps--6` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--4` uses `lemma-change-coefficients-exceptional-inverse-image--4` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-dctf-x-qbar-2-colimit--2` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-dctf-x-qbar-2-colimit--3` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-six-operations-change-coefficients--1` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-six-operations-change-coefficients--2` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-six-operations-change-coefficients--23` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-six-operations-change-coefficients--3` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-six-operations-change-coefficients--9` (chap-Construction-of-f → chap-The-six-operations-on-Dbctf)
- `proof/lemma-uniform-ext-bound` uses `lemma-global-lattice-normal-scheme` (chap-Construction-of-f → chap-Weights)
- `lemma-passing-schematic-closure` uses `lemma-extension-across-finite-subset` (chap-Nagata-compactification-and-Chows-lemma → chap-Constructibility-of-f)
- `lemma-passing-schematic-closure` uses `lemma-generic-smooth-open` (chap-Nagata-compactification-and-Chows-lemma → chap-Constructibility-of-f)
- `lemma-passing-schematic-closure` uses `lemma-smooth-morphisms-locally-constant-sheaves` (chap-Nagata-compactification-and-Chows-lemma → chap-Constructibility-of-f)
- `lemma-passing-schematic-closure` uses `definition-derived-base-change-map` (chap-Nagata-compactification-and-Chows-lemma → chap-Proper-base-change)
- `lemma-passing-schematic-closure` uses `lemma-acyclic-resolutions` (chap-Nagata-compactification-and-Chows-lemma → chap-Proper-base-change)
- `lemma-passing-schematic-closure` uses `lemma-cohomology-modules-underlying-abelian` (chap-Nagata-compactification-and-Chows-lemma → chap-Proper-base-change)
- `lemma-passing-schematic-closure` uses `lemma-finite-cover-projective-space` (chap-Nagata-compactification-and-Chows-lemma → chap-Proper-base-change)
- `lemma-passing-schematic-closure` uses `proposition-cohomology-p-1-over-henselian` (chap-Nagata-compactification-and-Chows-lemma → chap-Proper-base-change)
- `lemma-passing-schematic-closure` uses `proposition-proper-base-change-projective-line` (chap-Nagata-compactification-and-Chows-lemma → chap-Proper-base-change)
- `lemma-passing-schematic-closure` uses `theorem-proper-base-change-classical-pro` (chap-Nagata-compactification-and-Chows-lemma → chap-Proper-base-change)
- `proof/lemma-passing-schematic-closure` uses `lemma-change-coefficients` (chap-Nagata-compactification-and-Chows-lemma → chap-Smooth-base-change)
- `lemma-passing-schematic-closure` uses `definition-change-of-coefficients-maps` (chap-Nagata-compactification-and-Chows-lemma → chap-The-six-operations-on-Dbctf)
- `lemma-passing-schematic-closure` uses `proposition-dctf-x-qbar-2-colimit` (chap-Nagata-compactification-and-Chows-lemma → chap-The-six-operations-on-Dbctf)
- `lemma-passing-schematic-closure` uses `proposition-six-operations-change-coefficients` (chap-Nagata-compactification-and-Chows-lemma → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--2` uses `corollary-open-direct-image-over-field--1` (chap-Proper-base-change → chap-Constructibility-of-f)
- `proof/proposition-proper-direct-image-constructible-complexes--3` uses `corollary-open-direct-image-over-field--1` (chap-Proper-base-change → chap-Constructibility-of-f)
- `proposition-proper-direct-image-constructible-complexes--12` uses `corollary-open-direct-image-over-field--1` (chap-Proper-base-change → chap-Constructibility-of-f)
- `proposition-proper-direct-image-constructible-complexes--8` uses `corollary-open-direct-image-over-field--1` (chap-Proper-base-change → chap-Constructibility-of-f)
- `proof/proposition-proper-direct-image-constructible-complexes` uses `proposition-construction-independence-rf-shriek` (chap-Proper-base-change → chap-Construction-of-f)
- `proof/proposition-proper-direct-image-constructible-complexes--10` uses `lemma-inverse-image-tensor-product--1` (chap-Proper-base-change → chap-Construction-of-f)
- `proof/proposition-proper-direct-image-constructible-complexes--10` uses `lemma-inverse-image-tensor-product--2` (chap-Proper-base-change → chap-Construction-of-f)
- `proof/proposition-proper-direct-image-constructible-complexes--10` uses `proposition-comparison-etale-derived-category--5` (chap-Proper-base-change → chap-Construction-of-f)
- `proof/proposition-proper-direct-image-constructible-complexes--10` uses `proposition-comparison-etale-derived-category--6` (chap-Proper-base-change → chap-Construction-of-f)
- `proof/proposition-proper-direct-image-constructible-complexes--12` uses `lemma-inverse-image-tensor-product--2` (chap-Proper-base-change → chap-Construction-of-f)
- `proof/proposition-proper-direct-image-constructible-complexes--2` uses `proposition-comparison-etale-derived-category--5` (chap-Proper-base-change → chap-Construction-of-f)
- `proof/proposition-proper-direct-image-constructible-complexes--2` uses `proposition-comparison-etale-derived-category--6` (chap-Proper-base-change → chap-Construction-of-f)
- `proof/proposition-proper-direct-image-constructible-complexes--3` uses `proposition-comparison-etale-derived-category--5` (chap-Proper-base-change → chap-Construction-of-f)
- `proof/proposition-proper-direct-image-constructible-complexes--3` uses `proposition-comparison-etale-derived-category--6` (chap-Proper-base-change → chap-Construction-of-f)
- `proof/proposition-proper-direct-image-constructible-complexes--6` uses `proposition-comparison-etale-derived-category--5` (chap-Proper-base-change → chap-Construction-of-f)
- `proof/proposition-proper-direct-image-constructible-complexes--6` uses `proposition-comparison-etale-derived-category--6` (chap-Proper-base-change → chap-Construction-of-f)
- `proposition-proper-direct-image-constructible-complexes--12` uses `lemma-inverse-image-tensor-product--1` (chap-Proper-base-change → chap-Construction-of-f)
- `proposition-proper-direct-image-constructible-complexes--12` uses `lemma-inverse-image-tensor-product--4` (chap-Proper-base-change → chap-Construction-of-f)
- `proposition-proper-direct-image-constructible-complexes--12` uses `lemma-inverse-image-tensor-product--6` (chap-Proper-base-change → chap-Construction-of-f)
- `proposition-proper-direct-image-constructible-complexes--12` uses `proposition-comparison-etale-derived-category--5` (chap-Proper-base-change → chap-Construction-of-f)
- `proposition-proper-direct-image-constructible-complexes--12` uses `proposition-comparison-etale-derived-category--6` (chap-Proper-base-change → chap-Construction-of-f)
- `proposition-proper-direct-image-constructible-complexes--6` uses `lemma-inverse-image-tensor-product--1` (chap-Proper-base-change → chap-Construction-of-f)
- `proposition-proper-direct-image-constructible-complexes--7` uses `lemma-inverse-image-tensor-product--1` (chap-Proper-base-change → chap-Construction-of-f)
- `proposition-proper-direct-image-constructible-complexes--8` uses `lemma-inverse-image-tensor-product--1` (chap-Proper-base-change → chap-Construction-of-f)
- `proposition-proper-direct-image-constructible-complexes--8` uses `proposition-comparison-etale-derived-category--5` (chap-Proper-base-change → chap-Construction-of-f)
- `proposition-proper-direct-image-constructible-complexes--8` uses `proposition-comparison-etale-derived-category--6` (chap-Proper-base-change → chap-Construction-of-f)
- `proof/theorem-cohomology-curves--2` uses `lemma-proper-smooth-model--1` (chap-Proper-base-change → chap-Purity-of-real-sheaves)
- `proof/theorem-cohomology-curves--8` uses `lemma-proper-smooth-model--1` (chap-Proper-base-change → chap-Purity-of-real-sheaves)
- `proof/lemma-extension-separably-closed-ground-field` uses `lemma-degree-zero-calculation` (chap-Proper-base-change → chap-Smooth-base-change)
- `proof/lemma-extension-separably-closed-ground-field` uses `lemma-reduction-curve-over-normal-base` (chap-Proper-base-change → chap-Smooth-base-change)
- `proof/lemma-extension-separably-closed-ground-field` uses `lemma-reduction-field` (chap-Proper-base-change → chap-Smooth-base-change)
- `proof/lemma-extension-separably-closed-ground-field` uses `proposition-base-change-larger-algebraically-closed` (chap-Proper-base-change → chap-Smooth-base-change)
- `proof/proposition-proper-direct-image-constructible-complexes` uses `lemma-degree-zero-calculation` (chap-Proper-base-change → chap-Smooth-base-change)
- `proof/proposition-proper-direct-image-constructible-complexes` uses `lemma-reduction-curve-over-normal-base` (chap-Proper-base-change → chap-Smooth-base-change)
- `proof/proposition-proper-direct-image-constructible-complexes` uses `lemma-reduction-field` (chap-Proper-base-change → chap-Smooth-base-change)
- `proof/proposition-proper-direct-image-constructible-complexes` uses `proposition-base-change-larger-algebraically-closed` (chap-Proper-base-change → chap-Smooth-base-change)
- `proof/proposition-proper-direct-image-constructible-complexes--12` uses `lemma-change-coefficients--1` (chap-Proper-base-change → chap-Smooth-base-change)
- `proof/proposition-proper-direct-image-constructible-complexes--7` uses `lemma-change-coefficients--1` (chap-Proper-base-change → chap-Smooth-base-change)
- `proof/proposition-proper-direct-image-constructible-complexes--8` uses `lemma-change-coefficients--1` (chap-Proper-base-change → chap-Smooth-base-change)
- `proof/theorem-cohomology-curves--8` uses `theorem-smooth-base-change-classical-torsion--1` (chap-Proper-base-change → chap-Smooth-base-change)
- `proof/corollary-cohomology-geometric-fibres--2` uses `proposition-sp-unique-adjoint--1` (chap-Proper-base-change → chap-Smooth-purity)
- `proof/proposition-proper-base-change-complete-integral--1` uses `proposition-sp-unique-adjoint--1` (chap-Proper-base-change → chap-Smooth-purity)
- `proof/proposition-proper-base-change-projective-line--1` uses `proposition-sp-unique-adjoint--1` (chap-Proper-base-change → chap-Smooth-purity)
- `proof/proposition-proper-direct-image-constructible-complexes--10` uses `definition-sp-scalar-extension--2` (chap-Proper-base-change → chap-Smooth-purity)
- `proof/proposition-proper-direct-image-constructible-complexes--3` uses `proposition-sp-unique-adjoint--1` (chap-Proper-base-change → chap-Smooth-purity)
- `proof/theorem-cohomology-curves--8` uses `proposition-sp-unique-adjoint--1` (chap-Proper-base-change → chap-Smooth-purity)
- `proposition-proper-direct-image-constructible-complexes--12` uses `proposition-sp-unique-adjoint--1` (chap-Proper-base-change → chap-Smooth-purity)
- `proposition-proper-direct-image-constructible-complexes--8` uses `proposition-sp-unique-adjoint--1` (chap-Proper-base-change → chap-Smooth-purity)
- `proof/proposition-proper-direct-image-constructible-complexes` uses `proposition-six-operations-change-coefficients` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--10` uses `proposition-six-operations-change-coefficients--1` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--10` uses `proposition-six-operations-change-coefficients--2` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--10` uses `proposition-six-operations-change-coefficients--3` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--10` uses `proposition-six-operations-change-coefficients--6` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--12` uses `definition-change-of-coefficients-maps--4` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--12` uses `proposition-six-operations-change-coefficients--14` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--12` uses `proposition-six-operations-change-coefficients--2` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--12` uses `proposition-six-operations-change-coefficients--3` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--12` uses `proposition-six-operations-change-coefficients--6` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--3` uses `definition-change-of-coefficients-maps--6` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--3` uses `proposition-six-operations-change-coefficients--23` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--6` uses `definition-change-of-coefficients-maps--4` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--6` uses `proposition-six-operations-change-coefficients--1` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--6` uses `proposition-six-operations-change-coefficients--14` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--6` uses `proposition-six-operations-change-coefficients--2` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--6` uses `proposition-six-operations-change-coefficients--3` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--7` uses `proposition-six-operations-change-coefficients--1` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--7` uses `proposition-six-operations-change-coefficients--14` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--7` uses `proposition-six-operations-change-coefficients--3` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--8` uses `proposition-six-operations-change-coefficients--14` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/proposition-proper-direct-image-constructible-complexes--8` uses `proposition-six-operations-change-coefficients--3` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proposition-proper-direct-image-constructible-complexes--12` uses `definition-change-of-coefficients-maps--6` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proposition-proper-direct-image-constructible-complexes--12` uses `proposition-dctf-x-qbar-2-colimit--2` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proposition-proper-direct-image-constructible-complexes--12` uses `proposition-six-operations-change-coefficients--1` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proposition-proper-direct-image-constructible-complexes--12` uses `proposition-six-operations-change-coefficients--23` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proposition-proper-direct-image-constructible-complexes--8` uses `definition-change-of-coefficients-maps--6` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proposition-proper-direct-image-constructible-complexes--8` uses `proposition-dctf-x-qbar-2-colimit--2` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proposition-proper-direct-image-constructible-complexes--8` uses `proposition-six-operations-change-coefficients--1` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proposition-proper-direct-image-constructible-complexes--8` uses `proposition-six-operations-change-coefficients--23` (chap-Proper-base-change → chap-The-six-operations-on-Dbctf)
- `proof/theorem-weights-sums-squared-traces--1` uses `theorem-weil-conjectures-smooth-proper-schemes--7` (chap-Pure-sheaves-on-curves → chap-Proof-of-the-Weil-conjectures)
- `proof/corollary-unramified-boundary-point` uses `lemma-finite-quasi-finite-direct-images` (chap-Pure-sheaves-on-curves → chap-The-Deligne-Laumon-theorem-in-general)
- `proof/proposition-weights-j-boundary-points` uses `lemma-finite-quasi-finite-direct-images` (chap-Pure-sheaves-on-curves → chap-The-Deligne-Laumon-theorem-in-general)
- `proof/theorem-weights-sums-squared-traces` uses `lemma-finite-quasi-finite-direct-images` (chap-Pure-sheaves-on-curves → chap-The-Deligne-Laumon-theorem-in-general)
- `proof/definition-real-sheaves--2` uses `theorem-weil-conjectures-smooth-proper-schemes--7` (chap-Purity-of-real-sheaves → chap-Proof-of-the-Weil-conjectures)
- `proof/lemma-degree-zero-top-cohomology--3` uses `proposition-twisting-weight-zero-adding-dual--2` (chap-Purity-of-real-sheaves → chap-Pure-sheaves-on-curves)
- `proof/theorem-purity-real-sheaves-curves--1` uses `lemma-cohomological-range-curve--1` (chap-Purity-of-real-sheaves → chap-Pure-sheaves-on-curves)
- `proof/lemma-degree-zero-top-cohomology` uses `lemma-finite-quasi-finite-direct-images` (chap-Purity-of-real-sheaves → chap-The-Deligne-Laumon-theorem-in-general)
- `proof/proposition-bound-largest-determinant-weight` uses `lemma-finite-quasi-finite-direct-images` (chap-Purity-of-real-sheaves → chap-The-Deligne-Laumon-theorem-in-general)
- `proof/proposition-base-change-larger-algebraically-closed--1` uses `lemma-proper-smooth-model--1` (chap-Smooth-base-change → chap-Purity-of-real-sheaves)
- `proposition-compatibility-purity-base-change--4` uses `lemma-kunneth-formula-compact-supports--2` (chap-Smooth-purity → chap-The-Fourier-transform)
- `proposition-compatibility-purity-base-change--4` uses `lemma-kunneth-formula-compact-supports--3` (chap-Smooth-purity → chap-The-Fourier-transform)
- `theorem-smooth-purity-all-admissible-coefficients--9` uses `lemma-kunneth-formula-compact-supports--2` (chap-Smooth-purity → chap-The-Fourier-transform)
- `proof/lemma-finite-generically-etale-map-line` uses `lemma-finite-quasi-finite-direct-images` (chap-The-Deligne-Laumon-theorem-for-curves → chap-The-Deligne-Laumon-theorem-in-general)
- `proof/lemma-fourier-transform-boundary-sequence` uses `lemma-finite-quasi-finite-direct-images` (chap-The-Deligne-Laumon-theorem-for-curves → chap-The-Deligne-Laumon-theorem-in-general)
- `proof/proposition-purity-lisse-part-fourier-transform` uses `lemma-finite-quasi-finite-direct-images` (chap-The-Deligne-Laumon-theorem-for-curves → chap-The-Deligne-Laumon-theorem-in-general)
- `proof/theorem-weight-bound-affine-curve` uses `lemma-finite-quasi-finite-direct-images` (chap-The-Deligne-Laumon-theorem-for-curves → chap-The-Deligne-Laumon-theorem-in-general) — tex cites it
- `proof/theorem-weight-bound-affine-line` uses `lemma-finite-quasi-finite-direct-images` (chap-The-Deligne-Laumon-theorem-for-curves → chap-The-Deligne-Laumon-theorem-in-general)
- `proof/theorem-weight-bound-curve` uses `lemma-finite-quasi-finite-direct-images` (chap-The-Deligne-Laumon-theorem-for-curves → chap-The-Deligne-Laumon-theorem-in-general)
- `proof/theorem-weight-fourier-transform` uses `lemma-finite-quasi-finite-direct-images` (chap-The-Deligne-Laumon-theorem-for-curves → chap-The-Deligne-Laumon-theorem-in-general)
- `proof/proposition-fourier-transform-middle-extension` uses `lemma-finite-quasi-finite-direct-images` (chap-The-Fourier-transform → chap-The-Deligne-Laumon-theorem-in-general)
- `definition-trace-morphism--1` uses `lemma-kunneth-formula-compact-supports--2` (chap-The-Lefschetz-Verdier-formula → chap-The-Fourier-transform)
- `lemma-external-duality-trace-morphism--1` uses `lemma-kunneth-formula-compact-supports--2` (chap-The-Lefschetz-Verdier-formula → chap-The-Fourier-transform)
- `lemma-external-duality-trace-morphism--1` uses `lemma-kunneth-formula-compact-supports--3` (chap-The-Lefschetz-Verdier-formula → chap-The-Fourier-transform)
- `proof/lemma-external-duality-trace-morphism--2` uses `lemma-kunneth-formula-compact-supports--2` (chap-The-Lefschetz-Verdier-formula → chap-The-Fourier-transform)
- `proof/lemma-external-duality-trace-morphism--2` uses `lemma-kunneth-formula-compact-supports--3` (chap-The-Lefschetz-Verdier-formula → chap-The-Fourier-transform)
- `proof/proposition-additivity-trace-classes--2` uses `lemma-kunneth-formula-compact-supports--2` (chap-The-Lefschetz-Verdier-formula → chap-The-Fourier-transform)
- `proof/proposition-additivity-trace-classes--2` uses `lemma-kunneth-formula-compact-supports--3` (chap-The-Lefschetz-Verdier-formula → chap-The-Fourier-transform)
- `proof/theorem-proper-pushforward-lefschetz-verdier--1` uses `lemma-kunneth-formula-compact-supports--2` (chap-The-Lefschetz-Verdier-formula → chap-The-Fourier-transform)
- `proof/theorem-proper-pushforward-lefschetz-verdier--1` uses `lemma-kunneth-formula-compact-supports--3` (chap-The-Lefschetz-Verdier-formula → chap-The-Fourier-transform)
- `proof/theorem-proper-pushforward-lefschetz-verdier--2` uses `lemma-kunneth-formula-compact-supports--2` (chap-The-Lefschetz-Verdier-formula → chap-The-Fourier-transform)
- `proof/theorem-proper-pushforward-lefschetz-verdier--2` uses `lemma-kunneth-formula-compact-supports--3` (chap-The-Lefschetz-Verdier-formula → chap-The-Fourier-transform)
- `proposition-additivity-trace-classes--2` uses `definition-frobenius-correspondences-their-operators--5` (chap-The-Lefschetz-Verdier-formula → chap-The-trace-formula)
- `proposition-additivity-trace-classes--2` uses `definition-frobenius-correspondences-their-operators--6` (chap-The-Lefschetz-Verdier-formula → chap-The-trace-formula)
- `corollary-degree-jacobian` uses `lemma-acyclic-resolutions` (chap-The-Picard-scheme-of-a-curve → chap-Proper-base-change)
- `proof/corollary-torsion-jacobian-field-extension` uses `lemma-acyclic-resolutions` (chap-The-Picard-scheme-of-a-curve → chap-Proper-base-change)
- `proof/lemma-coherent-base-change-invertible-sheaves` uses `lemma-acyclic-resolutions` (chap-The-Picard-scheme-of-a-curve → chap-Proper-base-change)
- `proof/lemma-twisting-h-0-1-h` uses `lemma-acyclic-resolutions` (chap-The-Picard-scheme-of-a-curve → chap-Proper-base-change)
- `proposition-divisors-degree-g-open-chart` uses `lemma-acyclic-resolutions` (chap-The-Picard-scheme-of-a-curve → chap-Proper-base-change)
- `proposition-h-1-curve-tate-module` uses `lemma-acyclic-resolutions` (chap-The-Picard-scheme-of-a-curve → chap-Proper-base-change)
- `theorem-picard-scheme-jacobian-over-separably` uses `lemma-acyclic-resolutions` (chap-The-Picard-scheme-of-a-curve → chap-Proper-base-change)
- `proposition-h-1-curve-tate-module` uses `proposition-kummer-duality-integral-tate-module` (chap-The-Picard-scheme-of-a-curve → chap-Purity-of-real-sheaves)
- `proof/lemma-coherent-base-change-invertible-sheaves--1` uses `proposition-sp-unique-adjoint--1` (chap-The-Picard-scheme-of-a-curve → chap-Smooth-purity)
- `proof/theorem-riemann-roch-coherent-serre-duality--2` uses `proposition-sp-unique-adjoint--1` (chap-The-Picard-scheme-of-a-curve → chap-Smooth-purity)
- `proof/lemma-coherent-base-change-invertible-sheaves--1` uses `lemma-perfect-complexes-geometric-point--1` (chap-The-Picard-scheme-of-a-curve → chap-Verdier-and-Poincare-duality)
- `proof/corollary-finite-tor-amplitude-under-comparison--1` uses `definition-constructible-sheaves--5` (chap-The-pro-etale-site → chap-Constructible-complexes) — tex cites it
- `proof/lemma-uniform-bounds-pro-etale-affines` uses `lemma-affine-covers-dense-intersection` (chap-The-pro-etale-site → chap-Nagata-compactification-and-Chows-lemma)
- `proof/lemma-uniform-bounds-pro-etale-affines` uses `lemma-schematic-closure-uniqueness` (chap-The-pro-etale-site → chap-Nagata-compactification-and-Chows-lemma)
- `proof/lemma-uniform-bounds-pro-etale-affines` uses `proposition-compactifying-union-two-opens` (chap-The-pro-etale-site → chap-Nagata-compactification-and-Chows-lemma)
- `proof/lemma-uniform-bounds-pro-etale-affines` uses `remark-non-noetherian-compactifications` (chap-The-pro-etale-site → chap-Nagata-compactification-and-Chows-lemma)
- `proof/corollary-cohomology-pro-etale-affine` uses `lemma-acyclic-resolutions` (chap-The-pro-etale-site → chap-Proper-base-change)
- `proof/corollary-cohomology-pro-etale-affine` uses `proposition-cohomology-p-1-over-henselian` (chap-The-pro-etale-site → chap-Proper-base-change)
- `proof/lemma-cohomological-dimension-base-field` uses `lemma-acyclic-resolutions` (chap-The-pro-etale-site → chap-Proper-base-change)
- `proof/lemma-cohomological-dimension-base-field` uses `proposition-cohomology-p-1-over-henselian` (chap-The-pro-etale-site → chap-Proper-base-change)
- `proof/lemma-uniform-bounds-pro-etale-affines` uses `definition-derived-base-change-map` (chap-The-pro-etale-site → chap-Proper-base-change)
- `proof/lemma-uniform-bounds-pro-etale-affines` uses `lemma-acyclic-resolutions` (chap-The-pro-etale-site → chap-Proper-base-change)
- `proof/lemma-uniform-bounds-pro-etale-affines` uses `proposition-cohomology-p-1-over-henselian` (chap-The-pro-etale-site → chap-Proper-base-change)
- `proof/lemma-uniform-bounds-pro-etale-affines` uses `proposition-proper-base-change-projective-line` (chap-The-pro-etale-site → chap-Proper-base-change)
- `proof/proposition-unbounded-comparison-finite-coefficients` uses `lemma-acyclic-resolutions` (chap-The-pro-etale-site → chap-Proper-base-change)
- `proof/theorem-bounded-below-cohomology-comparison` uses `lemma-acyclic-resolutions` (chap-The-pro-etale-site → chap-Proper-base-change)
- `proof/theorem-comparison-constructible-sheaves` uses `lemma-acyclic-resolutions` (chap-The-pro-etale-site → chap-Proper-base-change)
- `proof/theorem-comparison-direct-images` uses `lemma-acyclic-resolutions` (chap-The-pro-etale-site → chap-Proper-base-change)
- `proof/theorem-comparison-direct-images` uses `proposition-cohomology-p-1-over-henselian` (chap-The-pro-etale-site → chap-Proper-base-change)
- `proof/lemma-uniform-bounds-pro-etale-affines` uses `corollary-degree-jacobian` (chap-The-pro-etale-site → chap-The-Picard-scheme-of-a-curve)
- `proof/lemma-uniform-bounds-pro-etale-affines` uses `definition-relative-picard-functor` (chap-The-pro-etale-site → chap-The-Picard-scheme-of-a-curve)
- `lemma-inverse-image-coefficient-sheaves` uses `proposition-six-operations-change-coefficients` (chap-The-pro-etale-site → chap-The-six-operations-on-Dbctf)
- `proof/definition-tate-twists--10` uses `definition-change-of-coefficients-maps--6` (chap-The-pro-etale-site → chap-The-six-operations-on-Dbctf)
- `proof/definition-tate-twists--10` uses `proposition-six-operations-change-coefficients--23` (chap-The-pro-etale-site → chap-The-six-operations-on-Dbctf)
- `proof/proposition-six-operations-dctf` uses `lemma-degree-zero-calculation` (chap-The-six-operations-on-Dbctf → chap-Smooth-base-change)
- `proof/proposition-six-operations-dctf` uses `lemma-kunneth-field-coefficients` (chap-The-six-operations-on-Dbctf → chap-Smooth-base-change)
- `proof/proposition-six-operations-dctf` uses `lemma-reduction-curve-over-normal-base` (chap-The-six-operations-on-Dbctf → chap-Smooth-base-change)
- `proof/proposition-six-operations-dctf` uses `lemma-reduction-field` (chap-The-six-operations-on-Dbctf → chap-Smooth-base-change)
- `proof/proposition-six-operations-dctf` uses `proposition-base-change-larger-algebraically-closed` (chap-The-six-operations-on-Dbctf → chap-Smooth-base-change)
- `definition-change-of-coefficients-maps--2` uses `proposition-sp-unique-adjoint--1` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `definition-change-of-coefficients-maps--5` uses `proposition-sp-unique-adjoint--1` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `lemma-change-coefficients-compact-support` uses `definition-sp-scalar-extension` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `lemma-change-coefficients-internal-hom--1` uses `proposition-sp-unique-adjoint--1` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `lemma-extension-scalars-preserves-dctf` uses `definition-sp-scalar-extension` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proof/proposition-dctf-x-qbar-2-colimit--2` uses `proposition-sp-unique-adjoint--1` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proof/proposition-dctf-x-qbar-2-colimit--3` uses `proposition-sp-unique-adjoint--1` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proof/proposition-six-operations-change-coefficients--14` uses `definition-sp-scalar-extension--2` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proof/proposition-six-operations-change-coefficients--2` uses `definition-sp-scalar-extension--2` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proof/proposition-six-operations-change-coefficients--3` uses `definition-sp-scalar-extension--2` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proof/proposition-six-operations-change-coefficients--4` uses `definition-sp-scalar-extension--2` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proposition-six-operations-change-coefficients--15` uses `proposition-sp-unique-adjoint--1` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proposition-six-operations-change-coefficients--4` uses `proposition-sp-unique-adjoint--1` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proposition-six-operations-change-coefficients--5` uses `definition-sp-scalar-extension--2` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proposition-six-operations-change-coefficients--5` uses `proposition-sp-unique-adjoint--1` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proposition-six-operations-change-coefficients--7` uses `proposition-sp-unique-adjoint--1` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proposition-six-operations-change-coefficients--9` uses `definition-sp-scalar-extension--2` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proposition-six-operations-dctf` uses `definition-relative-dualizing-complex` (chap-The-six-operations-on-Dbctf → chap-Smooth-purity)
- `proof/proposition-six-operations-dctf` uses `definition-verdier-dual-evaluation` (chap-The-six-operations-on-Dbctf → chap-Verdier-and-Poincare-duality)
- `proof/proposition-six-operations-dctf` uses `lemma-verdier-duality-preserves-constructibility` (chap-The-six-operations-on-Dbctf → chap-Verdier-and-Poincare-duality)
- `proof/proposition-six-operations-dctf` uses `theorem-verdier-biduality` (chap-The-six-operations-on-Dbctf → chap-Verdier-and-Poincare-duality)
- `proof/corollary-functional-equation` uses `lemma-hankel-rank-rationality` (chap-The-trace-formula → chap-Proof-of-the-Weil-conjectures)
- `proof/corollary-point-counting-zeta-function--7` uses `lemma-hankel-rank-rationality--2` (chap-The-trace-formula → chap-Proof-of-the-Weil-conjectures)
- `proof/theorem-grothendieck-lefschetz-trace-formula--8` uses `proposition-twisting-weight-zero-adding-dual--2` (chap-The-trace-formula → chap-Pure-sheaves-on-curves)
- `proof/theorem-trace-formula-euler-product--5` uses `lemma-cohomological-range-curve--1` (chap-The-trace-formula → chap-Pure-sheaves-on-curves)
- `proof/theorem-trace-formula-euler-product--5` uses `lemma-degree-zero-top-cohomology--4` (chap-The-trace-formula → chap-Purity-of-real-sheaves)
- `proof/corollary-functional-equation` uses `lemma-finite-quasi-finite-direct-images` (chap-The-trace-formula → chap-The-Deligne-Laumon-theorem-in-general)
- `proof/corollary-functional-equation` uses `theorem-pure-lisse-sheaves-over-relative` (chap-The-trace-formula → chap-The-Deligne-Laumon-theorem-in-general)
- `lemma-vanishing-local-term-zero-stalk--1` uses `lemma-kunneth-formula-compact-supports--2` (chap-The-trace-formula → chap-The-Fourier-transform)
- `proof/lemma-vanishing-local-term-zero-stalk--2` uses `lemma-kunneth-formula-compact-supports--2` (chap-The-trace-formula → chap-The-Fourier-transform)
- `proof/proposition-frobenius-local-term-curve--1` uses `lemma-kunneth-formula-compact-supports--2` (chap-The-trace-formula → chap-The-Fourier-transform)
- `proof/proposition-frobenius-local-term-curve--1` uses `lemma-kunneth-formula-compact-supports--3` (chap-The-trace-formula → chap-The-Fourier-transform)
- `proof/theorem-grothendieck-lefschetz-trace-formula--8` uses `lemma-kunneth-formula-compact-supports--2` (chap-The-trace-formula → chap-The-Fourier-transform)
- `proof/corollary-functional-equation` uses `lemma-subobjects-quotients-weil-sheaves` (chap-The-trace-formula → chap-Weights)
- `proof/corollary-functional-equation` uses `proposition-weights-under-usual-operations` (chap-The-trace-formula → chap-Weights)
- `corollary-degreewise-duality-over-fields--1` uses `proposition-twisting-weight-zero-adding-dual--2` (chap-Verdier-and-Poincare-duality → chap-Pure-sheaves-on-curves)
- `proof/corollary-cup-product-pairing--1` uses `proposition-twisting-weight-zero-adding-dual--2` (chap-Verdier-and-Poincare-duality → chap-Pure-sheaves-on-curves)
- `proof/lemma-internal-adjunction-two-exchange-formulas--1` uses `lemma-kunneth-formula-compact-supports--3` (chap-Verdier-and-Poincare-duality → chap-The-Fourier-transform)
- `corollary-cup-product-pairing--1` uses `theorem-grothendieck-lefschetz-trace-formula--6` (chap-Verdier-and-Poincare-duality → chap-The-trace-formula)
- `corollary-degreewise-duality-over-fields--1` uses `theorem-grothendieck-lefschetz-trace-formula--6` (chap-Verdier-and-Poincare-duality → chap-The-trace-formula)
- `definition-frobenius-operator` uses `definition-frobenius-correspondences-their-operators` (chap-Verdier-and-Poincare-duality → chap-The-trace-formula)
- `proof/corollary-cup-product-pairing--1` uses `theorem-trace-formula-euler-product--6` (chap-Verdier-and-Poincare-duality → chap-The-trace-formula)
- `theorem-trace-isomorphism-top-degree--1` uses `theorem-grothendieck-lefschetz-trace-formula--6` (chap-Verdier-and-Poincare-duality → chap-The-trace-formula)
- `theorem-trace-isomorphism-top-degree--8` uses `theorem-grothendieck-lefschetz-trace-formula--6` (chap-Verdier-and-Poincare-duality → chap-The-trace-formula)
- `proof/corollary-cup-product-pairing--1` uses `proposition-weights-under-usual-operations--13` (chap-Verdier-and-Poincare-duality → chap-Weights)
- `proof/corollary-degreewise-duality-over-fields--1` uses `proposition-weights-under-usual-operations--13` (chap-Verdier-and-Poincare-duality → chap-Weights)
- `proof/lemma-weil-sheaves-point-mixed--1` uses `proposition-twisting-weight-zero-adding-dual--2` (chap-Weights → chap-Pure-sheaves-on-curves)
- `proposition-weights-under-usual-operations--12` uses `proposition-twisting-weight-zero-adding-dual--2` (chap-Weights → chap-Pure-sheaves-on-curves)
- `proof/lemma-weil-sheaves-point-mixed--1` uses `lemma-kunneth-formula-compact-supports--2` (chap-Weights → chap-The-Fourier-transform)

</details>

### Section level: 39 arrows

| earlier block (uses) | later block (used) | arrows | tex cites |
|---|---|---|---|
| `sec-Statement` | `sec-ell-adic-coefficients-4` | 8 | 2 |
| `sec-ell-adic-coefficients-5` | `sec-The-function-sheaf-dictionary-2` | 4 | 0 |
| `sec-Sheaves-of-rank-one` | `sec-Determinant-weights` | 3 | 0 |
| `sec-Compactifications` | `sec-Proof-of-Nagatas-theorem` | 2 | 0 |
| `sec-Compactifications` | `sec-Separation-by-blow-ups` | 2 | 0 |
| `sec-Weights-of-middle-extensions` | `sec-Growth-of-squared-traces` | 2 | 0 |
| `sec-Quasi-finite-morphisms-and-curves` | `sec-Proof-of-the-Deligne-Laumon-theorem` | 2 | 0 |
| `sec-Integral-constructible-complexes` | `sec-Integral-models` | 2 | 0 |
| `sec-Frobenius-and-Rf` | `sec-The-function-sheaf-dictionary-2` | 1 | 0 |
| `sec-Affine-bases` | `sec-Weakly-contractible-objects` | 1 | 0 |
| `sec-Coefficient-rings` | `sec-Extension-by-zero-and-completion` | 1 | 0 |
| `sec-Specialization-of-the-trace-class` | `sec-Contracting-correspondences` | 1 | 0 |
| `sec-The-base-change-map` | `sec-Torsion-sheaves-and-acyclicity` | 1 | 0 |
| `sec-Kummer-theory` | `sec-Normalization` | 1 | 0 |
| `sec-Local-terms-on-a-curve` | `sec-Rationality-and-the-functional-equation` | 1 | 0 |
| `sec-Mixedness-of-real-sheaves` | `sec-Proof-of-the-Deligne-Laumon-theorem` | 1 | 0 |
| `sec-Base-change-in-degree-zero` | `sec-Torsion-sheaves-and-acyclicity` | 1 | 0 |
| `sec-Compactness-of-constructible-complexes` | `sec-Direct-image-with-compact-support` | 1 | 0 |
| `sec-Compactness-for-finite-coefficients` | `sec-Direct-image-with-compact-support` | 1 | 0 |
| `sec-Stability-of-Dbctf` | `sec-Change-of-coefficients` | 1 | 0 |
| `sec-ell-adic-coefficients-5` | `sec-Rationality-and-the-functional-equation` | 1 | 0 |
| `sec-Compatibilities` | `sec-Proof-of-smooth-purity` | 1 | 0 |

<details><summary>All arrows</summary>

- `lemma-w-contractible-affines-projective--1` uses `definition-weak-contractibility--1` (sec-Affine-bases → sec-Weakly-contractible-objects)
- `proof/lemma-sections-geometric-fibre` uses `lemma-acyclic-resolutions` (sec-Base-change-in-degree-zero → sec-Torsion-sheaves-and-acyclicity)
- `proof/corollary-finite-quotients-their-transition-maps--2` uses `lemma-reduction-derived-nakayama--1` (sec-Coefficient-rings → sec-Extension-by-zero-and-completion)
- `lemma-passing-schematic-closure` uses `lemma-affine-covers-dense-intersection` (sec-Compactifications → sec-Proof-of-Nagatas-theorem)
- `proof/proposition-dense-compactifications-form-cofiltered-category` uses `lemma-affine-covers-dense-intersection` (sec-Compactifications → sec-Proof-of-Nagatas-theorem)
- `lemma-passing-schematic-closure` uses `proposition-compactifying-union-two-opens` (sec-Compactifications → sec-Separation-by-blow-ups)
- `proof/proposition-dense-compactifications-form-cofiltered-category` uses `proposition-compactifying-union-two-opens` (sec-Compactifications → sec-Separation-by-blow-ups)
- `proof/proposition-compactness-finite-coefficients` uses `proposition-forgetting-supports-composition` (sec-Compactness-for-finite-coefficients → sec-Direct-image-with-compact-support)
- `proof/lemma-uniform-ext-bound` uses `proposition-forgetting-supports-composition` (sec-Compactness-of-constructible-complexes → sec-Direct-image-with-compact-support)
- `proposition-compatibility-purity-composition` uses `corollary-dualizing-complex-smooth-scheme` (sec-Compatibilities → sec-Proof-of-smooth-purity)
- `lemma-additivity-open-subscheme-complement` uses `definition-trace-function` (sec-Frobenius-and-Rf → sec-The-function-sheaf-dictionary-2)
- `proof/proposition-integral-constructibility-criterion` uses `lemma-integral-models` (sec-Integral-constructible-complexes → sec-Integral-models)
- `proof/proposition-integral-constructibility-criterion--1` uses `lemma-integral-models--2` (sec-Integral-constructible-complexes → sec-Integral-models)
- `proof/lemma-cohomology-multiplicative-group--6` uses `lemma-finite-morphisms-cohomology--2` (sec-Kummer-theory → sec-Normalization)
- `proof/lemma-frobenius-fixed-scheme--2` uses `theorem-trace-formula-euler-product--2` (sec-Local-terms-on-a-curve → sec-Rationality-and-the-functional-equation)
- `proof/lemma-mixedness-open-closed--1` uses `lemma-weights-exact-sequence--1` (sec-Mixedness-of-real-sheaves → sec-Proof-of-the-Deligne-Laumon-theorem)
- `proof/lemma-finite-quasi-finite-direct-images--1` uses `lemma-weights-exact-sequence--1` (sec-Quasi-finite-morphisms-and-curves → sec-Proof-of-the-Deligne-Laumon-theorem)
- `proof/lemma-finite-quasi-finite-direct-images--2` uses `lemma-weights-exact-sequence--1` (sec-Quasi-finite-morphisms-and-curves → sec-Proof-of-the-Deligne-Laumon-theorem)
- `corollary-determinant-weights` uses `definition-weil-representation` (sec-Sheaves-of-rank-one → sec-Determinant-weights)
- `corollary-rank-one-weights` uses `definition-weil-representation` (sec-Sheaves-of-rank-one → sec-Determinant-weights)
- `theorem-rank-one-sheaves-have-finite` uses `definition-weil-representation` (sec-Sheaves-of-rank-one → sec-Determinant-weights)
- `proof/corollary-specialization-when-fixed-point-scheme` uses `lemma-normal-cones-contracting-ideals` (sec-Specialization-of-the-trace-class → sec-Contracting-correspondences)
- `proof/proposition-six-operations-dctf` uses `proposition-six-operations-change-coefficients` (sec-Stability-of-Dbctf → sec-Change-of-coefficients)
- `definition-exceptional-base-change-map--1` uses `definition-sp-scalar-extension--2` (sec-Statement → sec-ell-adic-coefficients-4)
- `definition-exceptional-base-change-map--1` uses `proposition-sp-unique-adjoint--1` (sec-Statement → sec-ell-adic-coefficients-4)
- `definition-relative-dualizing-complex--1` uses `definition-sp-scalar-extension--2` (sec-Statement → sec-ell-adic-coefficients-4)
- `definition-relative-dualizing-complex--1` uses `proposition-sp-unique-adjoint--1` (sec-Statement → sec-ell-adic-coefficients-4)
- `theorem-smooth-purity-all-admissible-coefficients--2` uses `definition-sp-scalar-extension--2` (sec-Statement → sec-ell-adic-coefficients-4)
- `theorem-smooth-purity-all-admissible-coefficients--2` uses `proposition-sp-unique-adjoint--1` (sec-Statement → sec-ell-adic-coefficients-4) — tex cites it
- `theorem-smooth-purity-all-admissible-coefficients--9` uses `definition-sp-scalar-extension--2` (sec-Statement → sec-ell-adic-coefficients-4)
- `theorem-smooth-purity-all-admissible-coefficients--9` uses `proposition-sp-unique-adjoint--1` (sec-Statement → sec-ell-adic-coefficients-4) — tex cites it
- `proof/lemma-cohomology-modules-underlying-abelian` uses `lemma-acyclic-resolutions` (sec-The-base-change-map → sec-Torsion-sheaves-and-acyclicity)
- `proof/lemma-extreme-degrees-affine-curve--3` uses `proposition-twisting-weight-zero-adding-dual--2` (sec-Weights-of-middle-extensions → sec-Growth-of-squared-traces)
- `proof/proposition-weights-j-boundary-points--1` uses `proposition-twisting-weight-zero-adding-dual--2` (sec-Weights-of-middle-extensions → sec-Growth-of-squared-traces)
- `proof/theorem-grothendieck-lefschetz-trace-formula--8` uses `theorem-trace-formula-euler-product--1` (sec-ell-adic-coefficients-5 → sec-Rationality-and-the-functional-equation)
- `proof/theorem-grothendieck-lefschetz-trace-formula` uses `proposition-function-sheaf-dictionary` (sec-ell-adic-coefficients-5 → sec-The-function-sheaf-dictionary-2)
- `proof/theorem-grothendieck-lefschetz-trace-formula--8` uses `proposition-function-sheaf-dictionary--1` (sec-ell-adic-coefficients-5 → sec-The-function-sheaf-dictionary-2)
- `theorem-grothendieck-lefschetz-trace-formula` uses `definition-trace-function` (sec-ell-adic-coefficients-5 → sec-The-function-sheaf-dictionary-2)
- `theorem-grothendieck-lefschetz-trace-formula--8` uses `definition-trace-function--1` (sec-ell-adic-coefficients-5 → sec-The-function-sheaf-dictionary-2)

</details>

### Subsection level: 5 arrows

| earlier block (uses) | later block (used) | arrows | tex cites |
|---|---|---|---|
| `subsec-Henselian-pairs-and-curves` | `subsec-Injectives-on-the-closed-fibre` | 2 | 0 |
| `subsec-Coefficient-sheaves` | `subsec-Inverse-image` | 1 | 0 |
| `subsec-Integral-coefficients` | `subsec-Construction-of-Rf` | 1 | 0 |
| `subsec-Base-change-and-composition` | `subsec-The-trace-map` | 1 | 0 |

<details><summary>All arrows</summary>

- `proposition-compatibility-purity-base-change` uses `definition-trace-map` (subsec-Base-change-and-composition → subsec-The-trace-map)
- `proof/definition-tate-twists--10` uses `lemma-inverse-image-coefficient-sheaves--1` (subsec-Coefficient-sheaves → subsec-Inverse-image)
- `proof/lemma-extension-separably-closed-ground-field` uses `proposition-cohomology-p-1-over-henselian` (subsec-Henselian-pairs-and-curves → subsec-Injectives-on-the-closed-fibre)
- `theorem-gabber-affine-proper-base-change` uses `proposition-cohomology-p-1-over-henselian` (subsec-Henselian-pairs-and-curves → subsec-Injectives-on-the-closed-fibre)
- `proof/proposition-compactness-proper-direct-image` uses `proposition-forgetting-supports-composition` (subsec-Integral-coefficients → subsec-Construction-of-Rf)

</details>

## 3. Witnesses of the block arrows (for information)

A block arrow is judged by the text of the block, not by its declarations; this section only lists where the declaration arrows, or the citations, do not show the same dependency.

Of the 649 arrows between chapters, sections and subsections, 389 are witnessed by a declaration arrow (a declaration or proof inside the first block uses a declaration inside the second). **260 are not.** Only 837 of the 1933 declarations and clauses have Lean names, so the Lean arrows cannot witness everything; 192 of the 260 are witnessed by the text instead (something inside the first block links to something inside the second), and **68 are witnessed by neither**. These were judged from the prose; some are right (e.g. Normalization ends by deducing the theorem "from the calculations on smooth curves", i.e. Kummer theory, Affine curves and the Artin–Schreier sequence, without links), others may be wrong.

(The site's `unwitnessed-edge` notes, 65 of them, look only inside one expanded chapter at a time, so they find fewer.)

### Witnessed by neither Lean nor the text

| arrow | Lean names in first / second block |
|---|---|
| `sec-Base-change-for-nearby-cycles` uses `sec-Specialization-to-the-normal-cone` | 4 / 5 |
| `sec-Bounded-below-complexes` uses `sec-The-base-change-map-2` | 2 / 0 |
| `sec-Change-of-base-field` uses `sec-The-induction-hypothesis` | 2 / 0 |
| `sec-Change-of-base-field` uses `sec-Torsion-sheaves` | 2 / 1 |
| `sec-Change-of-coefficients` uses `sec-Proof-of-the-theorem` | 28 / 0 |
| `sec-Chows-lemma` uses `sec-Proof-of-Nagatas-theorem` | 4 / 2 |
| `sec-Compactness-for-finite-coefficients` uses `sec-Continuity-of-Ext` | 5 / 2 |
| `sec-Composition-and-restriction` uses `sec-Brown-representability` | 5 / 2 |
| `sec-Constructibility` uses `sec-Derived-functors` | 9 / 0 |
| `sec-Constructibility` uses `subsec-Condensed-rings` | 9 / 3 |
| `sec-Coordinate-projections` uses `sec-Conventions-2` | 4 / 1 |
| `sec-Correspondences` uses `sec-Existence-and-finiteness-of-f` | 4 / 1 |
| `sec-Degree-zero` uses `sec-The-base-change-map-2` | 2 / 0 |
| `sec-Duality-for-nearby-cycles` uses `sec-Proof-of-smooth-purity` | 4 / 1 |
| `sec-Exchange-formulas` uses `sec-Existence-and-finiteness-of-f` | 14 / 1 |
| `sec-Extension-by-zero-and-completion` uses `sec-Repleteness-and-limits` | 7 / 7 |
| `sec-Extension-by-zero-and-completion` uses `sec-Weakly-contractible-objects` | 7 / 5 |
| `sec-Finite-Tor-amplitude` uses `sec-Integral-constructible-complexes` | 3 / 4 |
| `sec-Finite-coefficients` uses `sec-Unbounded-complexes` | 1 / 4 |
| `sec-Finite-coefficients-2` uses `sec-Continuity-of-Ext` | 2 / 2 |
| `sec-Finite-coefficients-3` uses `sec-The-tensor-product-map` | 4 / 0 |
| `sec-Fourier-inversion` uses `sec-Stability-of-Dbctf` | 6 / 1 |
| `sec-Fourier-inversion` uses `subsec-Construction-of-Rf` | 6 / 13 |
| `sec-Frobenius-and-Poincare-duality` uses `subsec-The-trace-map` | 2 / 3 |
| `sec-Integrality-and-independence-of-ell` uses `sec-Kummer-theory` | 4 / 8 |
| `sec-Integrality-and-independence-of-ell` uses `sec-The-Weil-conjectures` | 4 / 0 |
| `sec-Inverting-ell` uses `sec-Integral-models` | 2 / 3 |
| `sec-Normalization` uses `sec-Affine-curves` | 5 / 4 |
| `sec-Normalization` uses `sec-Kummer-theory` | 5 / 8 |
| `sec-Normalization` uses `sec-The-Artin-Schreier-sequence` | 5 / 7 |
| `sec-Quasi-finite-morphisms-and-curves` uses `sec-Lisse-sheaves-as-representations` | 7 / 2 |
| `sec-Quasi-finite-morphisms-and-curves` uses `sec-The-Deligne-Laumon-theorem-2` | 7 / 2 |
| `sec-Reduction-to-constant-coefficients` uses `sec-Extension-by-zero` | 3 / 2 |
| `sec-Reduction-to-curves` uses `sec-The-induction-hypothesis` | 9 / 0 |
| `sec-Reduction-to-finite-coefficients` uses `sec-Integral-models` | 1 / 3 |
| `sec-Specialization-of-the-trace-class` uses `sec-Trace-classes-and-local-terms` | 4 / 10 |
| `sec-Specialization-to-the-normal-cone` uses `sec-Bounded-below-complexes` | 5 / 2 |
| `sec-Stability-of-Dbctf` uses `sec-Proof-of-the-theorem` | 1 / 0 |
| `sec-Statement` uses `sec-Proof-of-the-theorem` | 8 / 0 |
| `sec-The-Artin-Schreier-sheaf` uses `subsec-Construction-of-Rf` | 8 / 13 |
| `sec-The-Plancherel-formula` uses `sec-Fourier-inversion` | 3 / 6 |
| `sec-The-affine-line` uses `sec-Poincare-duality` | 3 / 5 |
| `sec-The-affine-line` uses `sec-Verdier-biduality` | 3 / 12 |
| `sec-The-base-change-map` uses `sec-Derived-functors` | 10 / 0 |
| `sec-The-exceptional-Kunneth-formula` uses `sec-Proof-of-smooth-purity` | 5 / 1 |
| `sec-The-tensor-product-map` uses `sec-Smooth-morphisms` | 0 / 8 |
| `sec-The-trace-map-of-affine-space` uses `sec-Statement` | 1 / 8 |
| `sec-Torsion-sheaves` uses `sec-The-base-change-map-2` | 1 / 0 |
| `sec-Unbounded-complexes` uses `sec-Conventions` | 4 / 0 |
| `sec-Verdier-biduality` uses `sec-Proof-of-smooth-purity` | 12 / 1 |
| `sec-ell-adic-coefficients-3` uses `sec-The-base-change-map-2` | 4 / 0 |
| `subsec-A-uniform-bound-for-Ext` uses `sec-Descent-to-a-finite-extension` | 1 / 1 |
| `subsec-A-uniform-bound-for-Ext` uses `sec-Integral-models` | 1 / 3 |
| `subsec-Base-change-and-composition` uses `sec-The-tensor-product-map` | 3 / 0 |
| `subsec-Base-change-and-composition` uses `sec-The-trace-map-of-affine-space` | 3 / 1 |
| `subsec-Change-of-finite-coefficients` uses `sec-Smooth-morphisms` | 4 / 8 |
| `subsec-Change-of-finite-coefficients` uses `sec-The-tensor-product-map` | 4 / 0 |
| `subsec-Direct-sums` uses `sec-Weakly-contractible-objects` | 2 / 5 |
| `subsec-Finite-monodromy` uses `sec-Lisse-sheaves-as-representations` | 9 / 2 |
| `subsec-Finiteness-of-f` uses `sec-Continuity-of-Ext` | 2 / 2 |
| `subsec-Henselian-pairs-and-curves` uses `sec-Devissage` | 9 / 0 |
| `subsec-Integral-coefficients` uses `sec-Continuity-of-Ext` | 8 / 2 |
| `subsec-Integral-coefficients-2` uses `sec-The-tensor-product-map` | 0 / 0 |
| `subsec-Representations-and-filtrations` uses `sec-Lisse-sheaves-as-representations` | 4 / 2 |
| `subsec-Tensor-operations` uses `sec-Weil-sheaves-and-weights` | 5 / 25 |
| `subsec-The-local-term-at-a-zero-stalk` uses `sec-The-Kunneth-formula` | 7 / 7 |
| `subsec-The-trace-map` uses `sec-The-trace-map-of-affine-space` | 3 / 1 |
| `subsec-Vanishing-on-a-strictly-local-surface` uses `sec-Proof-of-smooth-purity` | 7 / 1 |

### Witnessed by the text only

<details><summary>192 arrows, each with a citation that witnesses it</summary>

- `sec-Arbitrary-curves` uses `sec-Riemann-Roch-and-Serre-duality`: `proof/lemma-finite-generically-etale-map-line` cites `theorem-riemann-roch-coherent-serre-duality`
- `sec-Arbitrary-curves` uses `sec-The-affine-line`: `proof/theorem-weight-bound-affine-curve` cites `theorem-weight-bound-affine-line`
- `sec-Arbitrary-curves` uses `sec-Weil-sheaves-and-weights`: `proof/theorem-weight-bound-curve` cites `lemma-weil-sheaves-point-mixed`
- `sec-Base-change-for-nearby-cycles` uses `sec-The-exceptional-Kunneth-formula`: `prose-E-16` cites `lemma-external-duality-trace-morphism`
- `sec-Change-of-base-field` uses `sec-Constructible-sheaves`: `proof/proposition-base-change-larger-algebraically-closed` cites `lemma-torsors-under-classical-groups`
- `sec-Change-of-base-field` uses `sec-Direct-images`: `proof/proposition-base-change-larger-algebraically-closed` cites `theorem-comparison-direct-images`
- `sec-Change-of-coefficients` uses `sec-Descent-to-a-finite-extension`: `proof/proposition-dctf-x-qbar-2-colimit` cites `lemma-descent-finite-coefficient-field`
- `sec-Change-of-coefficients` uses `sec-Duality-for-the-projective-line`: `proof/lemma-change-coefficients-exceptional-inverse-image--1` cites `proposition-adjunction-projective-line`
- `sec-Change-of-coefficients` uses `sec-Stability-of-Dbctf`: `proof/proposition-six-operations-change-coefficients--5` cites `proposition-six-operations-dctf`
- `sec-Cohomology-in-top-degree` uses `subsec-The-trace-map`: `theorem-trace-isomorphism-top-degree` cites `definition-trace-map`
- `sec-Compactness-for-finite-coefficients` uses `sec-Constructible-sheaves`: `proof/proposition-compactness-finite-coefficients--1` cites `corollary-finite-tor-amplitude-under-comparison`
- `sec-Compactness-for-finite-coefficients` uses `sec-Finite-coefficients`: `prose-05-18` cites `proposition-proper-direct-image-finite-coefficients`
- `sec-Compactness-for-finite-coefficients` uses `sec-Unbounded-complexes`: `proof/proposition-comparison-etale-derived-category--2` cites `proposition-unbounded-comparison-finite-coefficients`
- `sec-Compactness-of-constructible-complexes` uses `sec-Field-coefficients`: `proof/lemma-uniform-ext-bound` cites `lemma-descent-lisse-qbar-sheaves-finite`
- `sec-Constructible-sheaves` uses `sec-Comparison-with-the-etale-site`: `prose-02-41` cites `corollary-bounded-below-classical-complexes`
- `sec-Constructible-sheaves` uses `sec-Direct-images`: `proof/theorem-comparison-constructible-sheaves` cites `theorem-comparison-direct-images`
- `sec-Continuity-of-Ext` uses `sec-Left-completeness-and-hypercovers`: `proof/lemma-continuity-ext-out-constructible-complex` cites `corollary-continuity-cohomology`
- `sec-Continuous-cohomology` uses `sec-Comparison-with-the-etale-site`: `proof/corollary-continuous-etale-cohomology` cites `theorem-bounded-below-cohomology-comparison`
- `sec-Continuous-cohomology` uses `sec-Repleteness-and-limits`: `proof/proposition-continuous-cohomology-pro-etale-cohomology` cites `proposition-milnor-sequence`
- `sec-Continuous-cohomology` uses `subsec-Coefficient-sheaves`: `prose-02-56` cites `lemma-comparison-completed-coefficients`
- `sec-Conventions-2` uses `sec-Brown-representability`: `prose-06-02` cites `theorem-existence-exceptional-inverse-image`
- `sec-Conventions-2` uses `sec-Compactness-for-finite-coefficients`: `prose-06-02` cites `proposition-comparison-etale-derived-category`
- `sec-Conventions-2` uses `sec-Comparison-with-the-etale-site`: `prose-06-02` cites `theorem-bounded-below-cohomology-comparison`
- `sec-Conventions-2` uses `sec-Constructible-sheaves`: `prose-06-02` cites `corollary-finite-tor-amplitude-under-comparison`
- `sec-Conventions-2` uses `sec-Direct-images`: `prose-06-02` cites `sec-Direct-images`
- `sec-Conventions-2` uses `sec-Unbounded-complexes`: `prose-06-02` cites `proposition-unbounded-comparison-finite-coefficients`
- `sec-Conventions-2` uses `subsec-Construction-of-Rf`: `prose-06-02` cites `proposition-forgetting-supports-composition`
- `sec-Derived-functors` uses `subsec-Inverse-image`: `prose-03-02` cites `lemma-inverse-image-coefficient-sheaves`
- `sec-Descent-to-a-finite-extension` uses `sec-Continuity-of-Ext`: `proof/lemma-descent-finite-coefficient-field` cites `lemma-continuity-ext-out-constructible-complex`
- `sec-Descent-to-the-ground-field` uses `sec-Comparison-with-the-etale-site`: `proof/proposition-h-1-curve-tate-module` cites `theorem-bounded-below-cohomology-comparison`
- `sec-Devissage` uses `sec-Comparison-with-the-etale-site`: `proof/theorem-cohomology-curves/2` cites `theorem-bounded-below-cohomology-comparison`
- `sec-Devissage` uses `sec-Extension-by-zero`: `proof/theorem-cohomology-curves/2` cites `lemma-removing-finitely-many-points`
- `sec-Devissage` uses `sec-Normalization`: `proof/theorem-cohomology-curves/2` cites `lemma-sheaves-finite-support-finite-morphisms`
- `sec-Devissage` uses `sec-Reduction-to-constant-coefficients`: `proof/theorem-cohomology-curves/2` cites `lemma-reduction-unipotent-local-system`
- `sec-Duality-for-nearby-cycles` uses `sec-Verdier-biduality`: `prose-E-21` cites `lemma-restriction-geometric-generic-fibre`
- `sec-Duality-for-the-projective-line` uses `sec-Kummer-theory`: `proof/lemma-cohomology-projective-line-trace` cites `proposition-smooth-proper-curves-torsion-prime`
- `sec-Exchange-formulas` uses `sec-Continuous-cohomology`: `proof/lemma-perfect-complexes-geometric-point` cites `sec-Continuous-cohomology`
- `sec-Exchange-formulas` uses `sec-Stability-of-Dbctf`: `proof/lemma-perfect-complexes-geometric-point--4` cites `proposition-six-operations-dctf`
- `sec-Exchange-formulas` uses `sec-ell-adic-coefficients-2`: `proof/lemma-internal-adjunction-two-exchange-formulas` cites `proposition-projection-formula-rational-coefficients`
- `sec-Existence-and-finiteness-of-f` uses `sec-Finite-Tor-amplitude`: `prose-05-04` cites `proposition-ctf-equals-bc`
- `sec-Extension-by-zero-and-completion` uses `subsec-Coefficient-sheaves`: `proof/lemma-reduction-derived-nakayama--2` cites `corollary-finite-quotients-their-transition-maps`
- `sec-Field-coefficients` uses `sec-Derived-functors`: `prose-03-18` cites `sec-Derived-functors`
- `sec-Finite-coefficients` uses `sec-Constructible-sheaves`: `proof/proposition-proper-direct-image-finite-coefficients` cites `corollary-finite-tor-amplitude-under-comparison`
- `sec-Finite-coefficients` uses `sec-Direct-images`: `proof/proposition-proper-direct-image-finite-coefficients` cites `theorem-comparison-direct-images`
- `sec-Finite-coefficients-2` uses `sec-Brown-representability`: `theorem-f-shriek-finite-coefficients` cites `theorem-existence-exceptional-inverse-image`
- `sec-Finite-coefficients-2` uses `sec-Extension-by-zero-and-completion`: `proof/theorem-f-shriek-finite-coefficients--1` cites `sec-Extension-by-zero-and-completion`
- `sec-Finite-coefficients-2` uses `sec-Finite-coefficients`: `proof/theorem-f-shriek-finite-coefficients--1` cites `proposition-proper-direct-image-finite-coefficients`
- `sec-Finite-coefficients-2` uses `sec-Unbounded-complexes`: `proof/proposition-open-direct-image-preserves-finite` cites `proposition-unbounded-comparison-finite-coefficients`
- `sec-Finite-coefficients-4` uses `sec-Frobenius-correspondences`: `prose-12-19` cites `definition-frobenius-correspondences-their-operators`
- `sec-Finite-coefficients-4` uses `sec-Stability-of-Dbctf`: `proof/theorem-trace-formula-frobenius-correspondence` cites `proposition-six-operations-dctf`
- `sec-Finite-coefficients-4` uses `subsec-The-local-term-at-a-fixed-point`: `prose-12-19` cites `proposition-frobenius-local-term-curve`
- `sec-Frobenius-and-Poincare-duality` uses `sec-Poincare-duality`: `proof/theorem-poincare-duality-frobenius--6` cites `corollary-degreewise-duality-over-fields`
- `sec-Frobenius-and-Poincare-duality` uses `sec-Weil-complexes`: `theorem-poincare-duality-frobenius` cites `definition-weil-structure`
- `sec-Frobenius-and-Rf` uses `sec-Frobenius-correspondences`: `lemma-comparison-via-relative-frobenius--3` cites `definition-frobenius-correspondences-their-operators`
- `sec-Frobenius-and-Rf` uses `sec-Traces-of-perfect-complexes`: `proof/lemma-additivity-open-subscheme-complement` cites `proposition-properties-trace`
- `sec-Generic-base-change` uses `sec-Smooth-morphisms`: `proof/lemma-extension-across-finite-subset` cites `lemma-smooth-morphisms-locally-constant-sheaves`
- `sec-Integral-constructible-complexes` uses `sec-Derived-functors`: `proof/proposition-integral-constructibility-criterion` cites `sec-Derived-functors`
- `sec-Integral-constructible-complexes` uses `sec-Repleteness-and-limits`: `proof/lemma-bounds-finite-reductions--3` cites `proposition-milnor-sequence`
- `sec-Integral-models` uses `sec-Descent-to-a-finite-extension`: `proof/lemma-integral-models--7` cites `lemma-descent-finite-coefficient-field`
- `sec-Integral-models` uses `sec-Field-coefficients`: `proof/lemma-integral-models--2` cites `corollary-coefficient-heart-b`
- `sec-Integral-models` uses `sec-Integral-constructible-complexes`: `proof/lemma-integral-models--5` cites `proposition-integral-constructibility-criterion`
- `sec-Integral-models` uses `sec-Lattices-after-stratification`: `proof/lemma-integral-models--2` cites `lemma-lattices-after-finite-stratification`
- `sec-Integrality-and-independence-of-ell` uses `sec-The-Riemann-hypothesis`: `proof/lemma-reciprocal-roots-zeta--6` cites `corollary-purity-cohomology-smooth-proper-variety`
- `sec-Inverting-ell` uses `sec-Extension-by-zero-and-completion`: `proof/proposition-inverting-ell` cites `proposition-extension-zero-restriction-closed-subscheme`
- `sec-Kummer-theory` uses `sec-Riemann-Roch-and-Serre-duality`: `proof/lemma-cohomology-multiplicative-group` cites `theorem-riemann-roch-coherent-serre-duality`
- `sec-Kummer-theory` uses `sec-Torsion-points`: `proof/proposition-smooth-proper-curves-torsion-prime` cites `corollary-torsion-jacobian-field-extension`
- `sec-Kunneth-formula-for-nearby-cycles` uses `sec-Specialization-to-the-normal-cone`: `prose-E-11` cites `lemma-nearby-cycles-constant-family`
- `sec-Left-completeness-and-hypercovers` uses `sec-Weakly-contractible-objects`: `proof/corollary-continuity-cohomology--1` cites `corollary-evaluation-weakly-contractible-objects`
- `sec-Lisse-sheaves-as-representations` uses `sec-Constructible-sheaves`: `proof/lemma-global-lattice-normal-scheme` cites `theorem-comparison-constructible-sheaves`
- `sec-Lisse-sheaves-as-representations` uses `sec-Field-coefficients`: `proof/lemma-global-lattice-normal-scheme` cites `lemma-lattices-lisse-e-sheaves`
- `sec-Lisse-sheaves-as-representations` uses `sec-Lattices-after-stratification`: `prose-13-09` cites `sec-Lattices-after-stratification`
- `sec-Lisse-sheaves-as-representations` uses `subsec-Coefficient-sheaves`: `proof/lemma-global-lattice-normal-scheme` cites `lemma-comparison-completed-coefficients`
- `sec-Middle-extensions` uses `sec-Perverse-t-exactness`: `proof/proposition-fourier-transform-middle-extension` cites `proposition-fourier-transform-perverse-heart`
- `sec-Middle-extensions` uses `subsec-Representations-and-filtrations`: `proof/lemma-unramified-at-infinity-no-linear-characters` cites `lemma-restriction-normal-subgroup`
- `sec-Mixedness-of-real-sheaves` uses `subsec-Representations-and-filtrations`: `proof/lemma-geometric-constituents-after-constant-extension` cites `lemma-restriction-normal-subgroup`
- `sec-Normalization` uses `sec-Comparison-with-the-etale-site`: `proof/lemma-finite-morphisms-cohomology` cites `theorem-bounded-below-cohomology-comparison`
- `sec-Perverse-sheaves-on-a-curve` uses `sec-Lisse-sheaves-as-representations`: `proof/lemma-largest-punctual-subsheaf` cites `proposition-lattices-representations-normal-scheme`
- `sec-Perverse-t-exactness` uses `sec-Weights-of-middle-extensions`: `proof/proposition-fourier-transform-perverse-heart` cites `lemma-cohomological-range-curve`
- `sec-Poincare-duality` uses `sec-Exchange-formulas`: `proof/theorem-poincare-duality--6` cites `lemma-perfect-complexes-geometric-point`
- `sec-Poincare-duality` uses `sec-Proof-of-smooth-purity`: `proof/theorem-poincare-duality` cites `corollary-dualizing-complex-smooth-scheme`
- `sec-Poincare-duality` uses `sec-Verdier-biduality`: `prose-10-12` cites `corollary-verdier-exchange-formulas`
- `sec-Poincare-duality` uses `subsec-The-trace-map`: `proof/theorem-poincare-duality` cites `definition-trace-map`
- `sec-Pro-etale-complexes` uses `sec-Comparison-with-the-etale-site`: `proof/theorem-proper-base-change-classical-pro` cites `corollary-bounded-below-classical-complexes`
- `sec-Pro-etale-complexes` uses `sec-Direct-images`: `prose-04-35` cites `theorem-comparison-direct-images`
- `sec-Pro-etale-complexes` uses `subsec-Condensed-rings`: `proof/corollary-cohomology-geometric-fibres` cites `proposition-pro-etale-site-separably-closed`
- `sec-Proof-of-smooth-purity` uses `sec-The-trace-map-of-affine-space`: `proof/theorem-smooth-purity-all-admissible-coefficients` cites `sec-The-trace-map-of-affine-space`
- `sec-Proof-of-smooth-purity` uses `subsec-Base-change-and-composition`: `proof/theorem-smooth-purity-all-admissible-coefficients` cites `proposition-compatibility-purity-base-change`
- `sec-Proof-of-smooth-purity` uses `subsec-Change-of-coefficients`: `proof/theorem-smooth-purity-all-admissible-coefficients--9` cites `proposition-compatibility-purity-change-coefficients`
- `sec-Proof-of-smooth-purity` uses `subsec-Integral-coefficients-2`: `proof/theorem-smooth-purity-all-admissible-coefficients--2` cites `proposition-sp-integral-adjunction`
- `sec-Proof-of-smooth-purity` uses `subsec-The-projective-line`: `proof/theorem-smooth-purity-all-admissible-coefficients` cites `proposition-ell-adic-cycle-class-diagonal`
- `sec-Proof-of-the-Deligne-Laumon-theorem` uses `subsec-Construction-of-Rf`: `proof/lemma-weight-bounds-partitions--2` cites `proposition-composition-base-change-rf-shriek`
- `sec-Proof-of-the-theorem` uses `sec-Brown-representability`: `proof/theorem-exceptional-inverse-image--1` cites `lemma-hypotheses-brown-representability`
- `sec-Proof-of-the-theorem` uses `sec-Direct-image-with-compact-support`: `proof/theorem-exceptional-inverse-image--7` cites `proposition-proper-direct-image-extension-zero`
- `sec-Proof-of-the-theorem` uses `sec-Existence-and-finiteness-of-f`: `prose-06-26` cites `theorem-exceptional-inverse-image`
- `sec-Proof-of-the-theorem` uses `sec-Finite-coefficients-2`: `proof/theorem-exceptional-inverse-image--15` cites `theorem-f-shriek-finite-coefficients`
- `sec-Proof-of-the-theorem` uses `subsec-Finiteness-of-f`: `proof/theorem-exceptional-inverse-image--3` cites `theorem-f-shriek-ell-adic-coefficients`
- `sec-Proper-direct-image` uses `sec-Left-completeness-and-hypercovers`: `proof/proposition-proper-direct-image-constructible-complexes--4` cites `corollary-continuity-cohomology`
- `sec-Proper-morphisms` uses `sec-Base-change-in-degree-zero`: `proof/lemma-composition-cancellation` cites `proposition-proper-base-change-degree-zero`
- `sec-Rankins-bound` uses `sec-Rationality-and-the-functional-equation`: `proof/proposition-bound-largest-determinant-weight` cites `theorem-trace-formula-euler-product`
- `sec-Rankins-bound` uses `sec-Weil-sheaves-and-weights`: `proof/proposition-bound-largest-determinant-weight` cites `lemma-filtrations-spectra`
- `sec-Rational-power-series` uses `sec-Rationality-and-the-functional-equation`: `prose-19-06` cites `corollary-point-counting-zeta-function`
- `sec-Rationality-and-the-functional-equation` uses `sec-Frobenius-and-Poincare-duality`: `proof/corollary-functional-equation--7` cites `theorem-poincare-duality-frobenius--8`
- `sec-Rationality-and-the-functional-equation` uses `sec-Traces-of-perfect-complexes`: `proof/lemma-logarithm-determinant` cites `proposition-properties-trace`
- `sec-Reduction-to-constant-coefficients` uses `sec-Constructible-sheaves`: `proof/lemma-reduction-unipotent-local-system` cites `proposition-locally-constant-sheaves-finite-presentation`
- `sec-Reduction-to-finite-coefficients` uses `sec-Extension-by-zero-and-completion`: `proof/proposition-isomorphisms-reduce-finite-coefficients` cites `lemma-reduction-derived-nakayama`
- `sec-Reduction-to-finite-coefficients` uses `sec-Integral-constructible-complexes`: `proof/proposition-isomorphisms-reduce-finite-coefficients` cites `proposition-integral-constructibility-criterion`
- `sec-Relative-affine-curves` uses `sec-Arbitrary-curves`: `proof/theorem-pure-lisse-sheaves-over-relative` cites `theorem-weight-bound-curve`
- `sec-Smooth-morphisms` uses `sec-Constructible-sheaves`: `proof/lemma-smooth-morphisms-locally-constant-sheaves` cites `proposition-locally-constant-sheaves-finite-presentation`
- `sec-Specialization-of-the-trace-class` uses `sec-Duality-for-nearby-cycles`: `prose-E-23` cites `proposition-nearby-cycles-commute-verdier-duality`
- `sec-Specialization-of-the-trace-class` uses `sec-The-exceptional-Kunneth-formula`: `prose-E-23` cites `lemma-external-duality-trace-morphism`
- `sec-Stability-of-Dbctf` uses `sec-Constructibility`: `proof/proposition-six-operations-dctf` cites `definition-constructible-sheaves`
- `sec-Statement` uses `subsec-The-projective-line`: `definition-trace-map-affine-line` cites `proposition-ell-adic-cycle-class-diagonal`
- `sec-The-Artin-Schreier-sequence` uses `sec-Comparison-with-the-etale-site`: `proof/lemma-p-torsion-affine-curve-characteristic` cites `theorem-bounded-below-cohomology-comparison`
- `sec-The-Artin-Schreier-sheaf` uses `subsec-The-trace-map`: `proof/lemma-integral-linear-character` cites `definition-trace-map`
- `sec-The-Kunneth-formula` uses `sec-Bounded-below-complexes`: `proof/lemma-base-change-along-product-projection` cites `theorem-smooth-base-change-classical-torsion-2`
- `sec-The-Kunneth-formula` uses `sec-Stability-of-Dbctf`: `proof/lemma-kunneth-one-identity-factor` cites `proposition-six-operations-dctf`
- `sec-The-Riemann-hypothesis` uses `sec-Frobenius-and-Poincare-duality`: `proof/theorem-purity-higher-direct-images-under` cites `theorem-poincare-duality-frobenius`
- `sec-The-Riemann-hypothesis` uses `sec-Poincare-duality`: `proof/theorem-purity-higher-direct-images-under` cites `corollary-degreewise-duality-over-fields`
- `sec-The-Riemann-hypothesis` uses `sec-Proof-of-the-Deligne-Laumon-theorem`: `prose-19-02` cites `theorem-direct-image-mixed-sheaf`
- `sec-The-affine-line` uses `sec-The-weight-of-the-Fourier-transform`: `prose-17-09` cites `corollary-h-1-c-stalk-fourier`
- `sec-The-base-change-map-2` uses `sec-The-base-change-map`: `prose-08-02` cites `lemma-naturality-pasting-comparison`
- `sec-The-exceptional-Kunneth-formula` uses `sec-Stability-of-Dbctf`: `proof/lemma-external-duality-trace-morphism` cites `proposition-six-operations-dctf`
- `sec-The-function-sheaf-dictionary-2` uses `sec-The-function-sheaf-dictionary`: `prose-12-24` cites `sec-The-function-sheaf-dictionary`
- `sec-The-function-sheaf-dictionary-2` uses `sec-Traces-of-perfect-complexes`: `proof/proposition-function-sheaf-dictionary` cites `proposition-properties-trace`
- `sec-The-induction-hypothesis` uses `sec-Torsion-sheaves`: `prose-08-06` cites `theorem-smooth-base-change-classical-torsion`
- `sec-The-tensor-product-map` uses `sec-Statement`: `prose-09-07` cites `definition-exceptional-base-change-map`
- `sec-The-trace-map-of-affine-space` uses `sec-Compactness-for-finite-coefficients`: `prose-09-09` cites `proposition-comparison-etale-derived-category`
- `sec-The-trace-map-of-affine-space` uses `sec-Conventions-2`: `prose-09-09` cites `sec-Conventions-2`
- `sec-The-trace-map-of-affine-space` uses `sec-Duality-for-the-projective-line`: `prose-09-08` cites `proposition-adjunction-projective-line`
- `sec-Torsion-sheaves` uses `sec-Direct-images`: `prose-08-04` cites `theorem-comparison-direct-images`
- `sec-Unbounded-complexes` uses `sec-Direct-images`: `proof/proposition-unbounded-comparison-finite-coefficients--2` cites `theorem-comparison-direct-images`
- `sec-Verdier-biduality` uses `sec-Left-completeness-and-hypercovers`: `proof/lemma-restriction-geometric-generic-fibre` cites `corollary-continuity-cohomology`
- `sec-Verdier-biduality` uses `sec-Stability-of-Dbctf`: `proof/corollary-verdier-exchange-formulas--2` cites `proposition-six-operations-dctf--15`
- `sec-Weights-of-middle-extensions` uses `sec-Poincare-duality`: `proof/lemma-cohomological-range-curve` cites `corollary-degreewise-duality-over-fields`
- `sec-ell-adic-coefficients` uses `sec-Pro-etale-complexes`: `proof/proposition-proper-base-change-complete-integral` cites `theorem-proper-base-change-classical-pro`
- `sec-ell-adic-coefficients` uses `sec-The-base-change-map`: `proof/lemma-completed-ordinary-base-change--1` cites `definition-pro-etale-base-change-map`
- `sec-ell-adic-coefficients-2` uses `sec-Integral-constructible-complexes`: `proof/proposition-direct-image-along-open-immersion--1` cites `proposition-integral-constructibility-criterion`
- `sec-ell-adic-coefficients-2` uses `sec-Left-completeness-and-hypercovers`: `proof/proposition-ell-adic-cycle-class-diagonal--10` cites `corollary-continuity-cohomology`
- `sec-ell-adic-coefficients-3` uses `sec-Stability-of-Dbctf`: `proof/theorem-smooth-base-change-all-admissible` cites `proposition-six-operations-dctf`
- `sec-ell-adic-coefficients-5` uses `sec-Finite-coefficients-4`: `proof/theorem-grothendieck-lefschetz-trace-formula--1` cites `theorem-trace-formula-frobenius-correspondence`
- `subsec-A-uniform-bound-for-Ext` uses `sec-Lattices-after-stratification`: `prose-05-09` cites `lemma-lattices-after-finite-stratification`
- `subsec-A-uniform-bound-for-Ext` uses `sec-Unbounded-complexes`: `prose-05-07` cites `definition-cohomological-dimension`
- `subsec-Base-change-and-composition` uses `subsec-Integral-coefficients-2`: `prose-09-30` cites `proposition-sp-tower-geometric`
- `subsec-Central-elements` uses `sec-Lie-algebras`: `proof/lemma-identity-component` cites `lemma-stable-subspaces-center`
- `subsec-Change-of-coefficients` uses `sec-Change-of-coefficients`: `proof/proposition-compatibility-purity-change-coefficients--14` cites `proposition-six-operations-change-coefficients`
- `subsec-Change-of-coefficients` uses `subsec-Base-change-and-composition`: `proof/proposition-compatibility-purity-change-coefficients` cites `subsec-Base-change-and-composition`
- `subsec-Change-of-coefficients` uses `subsec-Change-of-finite-coefficients`: `prose-09-34` cites `lemma-sp-reduction`
- `subsec-Change-of-coefficients` uses `subsec-Field-coefficients`: `proof/proposition-compatibility-purity-change-coefficients` cites `subsec-Field-coefficients`
- `subsec-Change-of-coefficients` uses `subsec-Integral-coefficients-2`: `proof/proposition-compatibility-purity-change-coefficients` cites `proposition-sp-tower-geometric`
- `subsec-Change-of-finite-coefficients` uses `sec-Duality-for-the-projective-line`: `proof/lemma-sp-reduction--2` cites `proposition-adjunction-projective-line`
- `subsec-Change-of-finite-coefficients` uses `sec-Finite-Tor-amplitude`: `proof/lemma-sp-reduction` cites `lemma-flat-models-generators`
- `subsec-Change-of-finite-coefficients` uses `sec-Finite-coefficients-3`: `prose-09-20` cites `lemma-section-normal-bundle`
- `subsec-Change-of-finite-coefficients` uses `sec-The-trace-map-of-affine-space`: `prose-09-20` cites `proposition-purity-vector-bundles`
- `subsec-Condensed-rings` uses `sec-Weil-cohomology`: `prose-02-49` cites `sec-Weil-cohomology`
- `subsec-Direct-sums` uses `sec-Field-coefficients`: `proof/lemma-uniform-bound-proper-direct-image` cites `lemma-descent-lisse-qbar-sheaves-finite`
- `subsec-Direct-sums` uses `sec-Lattices-after-stratification`: `proof/lemma-uniform-bound-proper-direct-image` cites `lemma-lattices-after-finite-stratification`
- `subsec-Direct-sums` uses `sec-Proper-direct-image`: `proof/lemma-uniform-bound-proper-direct-image` cites `proposition-proper-direct-image-constructible-complexes`
- `subsec-Direct-sums` uses `sec-Repleteness-and-limits`: `proof/lemma-uniform-bound-proper-direct-image` cites `proposition-milnor-sequence`
- `subsec-Field-coefficients` uses `subsec-Change-of-finite-coefficients`: `prose-09-27` cites `lemma-sp-reduction`
- `subsec-Field-coefficients` uses `subsec-Integral-coefficients-2`: `proof/proposition-sp-rational` cites `proposition-sp-integral-adjunction`
- `subsec-Finite-monodromy` uses `sec-Weil-sheaves-and-weights`: `corollary-rank-one-weights--1` cites `sec-Weil-sheaves-and-weights`
- `subsec-Finiteness-of-f` uses `sec-Finite-coefficients-2`: `proof/theorem-f-shriek-ell-adic-coefficients--1` cites `sec-Finite-coefficients-2`
- `subsec-Finiteness-of-f` uses `sec-Proper-direct-image`: `proof/lemma-projection-formula-integral-coefficients` cites `proposition-proper-direct-image-constructible-complexes`
- `subsec-Finiteness-of-f` uses `subsec-The-projective-line`: `proof/theorem-f-shriek-ell-adic-coefficients--2` cites `proposition-projective-line-rational-coefficients`
- `subsec-Frobenius-invariants` uses `sec-Continuous-cohomology`: `proof/proposition-no-fixed-class-degree-one` cites `proposition-continuous-cohomology-pro-etale-cohomology`
- `subsec-Frobenius-invariants` uses `sec-Left-completeness-and-hypercovers`: `proof/proposition-no-fixed-class-degree-one` cites `corollary-continuity-cohomology`
- `subsec-Frobenius-invariants` uses `sec-Poincare-duality`: `proof/proposition-kummer-duality-integral-tate-module` cites `theorem-poincare-duality`
- `subsec-Frobenius-invariants` uses `subsec-Coefficient-sheaves`: `proof/proposition-no-fixed-class-degree-one` cites `lemma-comparison-completed-coefficients`
- `subsec-Henselian-pairs-and-curves` uses `sec-Comparison-with-the-etale-site`: `theorem-cohomology-curves--7` cites `theorem-bounded-below-cohomology-comparison`
- `subsec-Integral-coefficients` uses `sec-Integral-constructible-complexes`: `proof/lemma-structure-integral-constructible-complexes--2` cites `proposition-local-structure-integral-constructible-complexes`
- `subsec-Integral-coefficients-2` uses `sec-Brown-representability`: `proposition-sp-integral-adjunction` cites `theorem-existence-exceptional-inverse-image`
- `subsec-Integral-coefficients-2` uses `sec-Finite-coefficients-3`: `prose-09-24` cites `lemma-section-normal-bundle`
- `subsec-Integral-coefficients-2` uses `sec-Integral-constructible-complexes`: `proof/proposition-sp-integral-towers--2` cites `proposition-integral-constructibility-criterion`
- `subsec-Integral-coefficients-2` uses `sec-Stability-of-Dbctf`: `prose-09-23` cites `proposition-six-operations-dctf`
- `subsec-Integral-coefficients-2` uses `sec-The-trace-map-of-affine-space`: `proof/proposition-sp-tower-geometric` cites `sec-The-trace-map-of-affine-space`
- `subsec-Integral-coefficients-2` uses `subsec-Change-of-finite-coefficients`: `proposition-sp-tower-geometric--1` cites `lemma-sp-reduction`
- `subsec-Integral-coefficients-2` uses `subsec-Integral-coefficients`: `proof/proposition-sp-integral-towers--1` cites `lemma-structure-integral-constructible-complexes`
- `subsec-Rational-coefficients` uses `sec-Repleteness-and-limits`: `proof/lemma-reduction-finitely-many-degrees` cites `proposition-exact-products`
- `subsec-Representations-and-filtrations` uses `sec-Weil-sheaves-and-weights`: `prose-14-14` cites `example-kummer-extension`
- `subsec-The-local-term-as-a-restriction-map` uses `sec-Frobenius-correspondences`: `prose-12-09` cites `definition-frobenius-correspondences-their-operators`
- `subsec-The-local-term-as-a-restriction-map` uses `sec-The-exceptional-Kunneth-formula`: `proof/lemma-local-term-restriction-map` cites `definition-trace-morphism`
- `subsec-The-local-term-as-a-restriction-map` uses `sec-Trace-classes-and-local-terms`: `lemma-local-term-restriction-map--1` cites `definition-trace-class-local-terms`
- `subsec-The-local-term-at-a-zero-stalk` uses `subsec-The-local-term-as-a-restriction-map`: `lemma-vanishing-local-term-zero-stalk--1` cites `lemma-local-term-restriction-map`
- `subsec-The-projective-line` uses `sec-Brown-representability`: `proposition-projective-line-rational-coefficients` cites `theorem-existence-exceptional-inverse-image`
- `subsec-The-projective-line` uses `sec-Duality-for-the-projective-line`: `proof/proposition-ell-adic-cycle-class-diagonal--3` cites `proposition-adjunction-projective-line`
- `subsec-The-projective-line` uses `sec-Field-coefficients`: `proof/proposition-projection-formula-rational-coefficients` cites `corollary-coefficient-heart-b`
- `subsec-The-projective-line` uses `sec-Left-completeness-and-hypercovers`: `proof/proposition-ell-adic-cycle-class-diagonal--10` cites `corollary-continuity-cohomology`
- `subsec-The-projective-line` uses `sec-Proper-direct-image`: `proof/proposition-projection-formula-rational-coefficients--2` cites `proposition-proper-direct-image-constructible-complexes`
- `subsec-The-projective-line` uses `sec-Repleteness-and-limits`: `proof/proposition-ell-adic-cycle-class-diagonal` cites `proposition-repleteness-pro-etale-topos`
- `subsec-The-projective-line` uses `subsec-Inverse-image`: `proof/proposition-ell-adic-cycle-class-diagonal` cites `lemma-inverse-image-coefficient-sheaves`
- `subsec-The-trace-map` uses `subsec-Base-change-and-composition`: `proof/proposition-transitivity-trace-map` cites `proposition-compatibility-purity-composition`
- `subsec-Vanishing-on-a-strictly-local-surface` uses `sec-Affine-curves`: `proof/lemma-punctured-surface-punctured-curve` cites `proposition-cohomology-smooth-affine-curve`

</details>

## 4. Cycles among declarations

### 4.1: 2 sketch declarations

- `proposition-cohomology-p-1-over-henselian` uses `theorem-gabber-affine-proper-base-change`: `AlgebraicGeometry.Etale.bijective_cohomologyMap_projectiveLine_residueField` (proposition-cohomology-p-1-over-henselian) → `AlgebraicGeometry.Etale.bijective_cohomologyMap_projectiveLine_residueField_zmod` (proposition-cohomology-p-1-over-henselian--1) → `AlgebraicGeometry.Etale.subsingleton_H_projectiveLine_closedFibre_of_injective` (lemma-acyclicity-closed-fibre--1) → `AlgebraicGeometry.Etale.bijective_cohomologyMap_of_henselianRing` (theorem-gabber-affine-proper-base-change)
- `theorem-gabber-affine-proper-base-change` uses `proposition-cohomology-p-1-over-henselian`: `AlgebraicGeometry.Etale.bijective_cohomologyMap_of_henselianRing` (theorem-gabber-affine-proper-base-change) → `AlgebraicGeometry.Etale.cohomologyMap_map` (proposition-cohomology-p-1-over-henselian)

### 4.2: 7 sketch declarations

- `definition-exceptional-base-change-finite` uses `proposition-composition-open-restriction-compactifications-f`: `AlgebraicGeometry.Etale.rightDerivedUpperShriekBaseChangeMap` (definition-exceptional-base-change-finite) → `AlgebraicGeometry.Etale.rightDerivedUpperShriekOfCompactification` (proposition-composition-open-restriction-compactifications-f)
- `definition-relative-dualizing-complex` uses `proposition-composition-open-restriction-compactifications-f`: `AlgebraicGeometry.Etale.dualizingComplex` (definition-relative-dualizing-complex) → `AlgebraicGeometry.Etale.rightDerivedUpperShriekOfCompactification` (proposition-composition-open-restriction-compactifications-f)
- `lemma-change-coefficients` uses `lemma-smooth-morphisms-locally-constant-sheaves`: `AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_integralToPadicAlgCl` (lemma-change-coefficients) → `AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_isOpenImmersion` (corollary-open-direct-image-over-field--1) → `AlgebraicGeometry.Etale.exists_hasConstructibleDirectImageBaseChangeOn` (theorem-generic-constructibility-base-change-rj--2) → `AlgebraicGeometry.Etale.exists_nonempty_open_smooth_directImage_lisse_baseChange` (lemma-smooth-morphisms-locally-constant-sheaves)
- `lemma-class-diagonal-projective-line` uses `definition-exceptional-base-change-finite`: `AlgebraicGeometry.Etale.projectiveLineTrace_diagonal` (lemma-class-diagonal-projective-line) → `AlgebraicGeometry.Etale.rightDerivedUpperShriekBaseChangeMap` (definition-exceptional-base-change-finite)
- `lemma-class-diagonal-projective-line` uses `proposition-composition-open-restriction-compactifications-f`: `AlgebraicGeometry.Etale.projectiveLineTrace_diagonal` (lemma-class-diagonal-projective-line) → `AlgebraicGeometry.Etale.rightDerivedUpperShriekOfCompactification` (proposition-composition-open-restriction-compactifications-f)
- `lemma-smooth-morphisms-locally-constant-sheaves` uses `definition-exceptional-base-change-finite`: `AlgebraicGeometry.Etale.exists_nonempty_open_smooth_directImage_lisse_baseChange` (lemma-smooth-morphisms-locally-constant-sheaves) → `AlgebraicGeometry.Etale.rightDerivedUpperShriekBaseChangeMap` (definition-exceptional-base-change-finite)
- `lemma-smooth-morphisms-locally-constant-sheaves` uses `definition-relative-dualizing-complex`: `AlgebraicGeometry.Etale.exists_nonempty_open_smooth_directImage_lisse_baseChange` (lemma-smooth-morphisms-locally-constant-sheaves) → `AlgebraicGeometry.Etale.dualizingComplex` (definition-relative-dualizing-complex)
- `lemma-smooth-morphisms-locally-constant-sheaves` uses `lemma-class-diagonal-projective-line`: `AlgebraicGeometry.Etale.exists_nonempty_open_smooth_directImage_lisse_baseChange` (lemma-smooth-morphisms-locally-constant-sheaves) → `AlgebraicGeometry.Etale.ordinaryFiniteP1_diagonal_integral` (lemma-class-diagonal-projective-line)
- `lemma-smooth-morphisms-locally-constant-sheaves` uses `proposition-composition-open-restriction-compactifications-f`: `AlgebraicGeometry.Etale.exists_nonempty_open_smooth_directImage_lisse_baseChange` (lemma-smooth-morphisms-locally-constant-sheaves) → `AlgebraicGeometry.Etale.rightDerivedUpperShriekOfCompactification` (proposition-composition-open-restriction-compactifications-f)
- `proposition-adjunction-projective-line` uses `definition-exceptional-base-change-finite`: `AlgebraicGeometry.Etale.exists_projectiveLineAdjunction` (proposition-adjunction-projective-line) → `AlgebraicGeometry.Etale.rightDerivedUpperShriekBaseChangeMap` (definition-exceptional-base-change-finite)
- `proposition-adjunction-projective-line` uses `lemma-class-diagonal-projective-line`: `AlgebraicGeometry.Etale.exists_projectiveLineAdjunction` (proposition-adjunction-projective-line) → `AlgebraicGeometry.Etale.projectiveLineTrace_diagonal` (lemma-class-diagonal-projective-line)
- `proposition-adjunction-projective-line` uses `proposition-composition-open-restriction-compactifications-f`: `AlgebraicGeometry.Etale.exists_projectiveLineAdjunction` (proposition-adjunction-projective-line) → `AlgebraicGeometry.Etale.rightDerivedUpperShriekOfCompactification` (proposition-composition-open-restriction-compactifications-f)
- `proposition-composition-open-restriction-compactifications-f` uses `definition-exceptional-base-change-finite`: `AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructibleUpperShriekOfCompactification` (proposition-composition-open-restriction-compactifications-f) → `AlgebraicGeometry.Etale.exists_dualizingComplex_iso_and_tensor` (proposition-exceptional-inverse-image-smooth-morphism--5) → `AlgebraicGeometry.Etale.rightDerivedUpperShriekBaseChangeMap` (definition-exceptional-base-change-finite)
- `proposition-composition-open-restriction-compactifications-f` uses `definition-relative-dualizing-complex`: `AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructibleUpperShriekOfCompactification` (proposition-composition-open-restriction-compactifications-f) → `AlgebraicGeometry.Etale.dualizingComplex` (definition-relative-dualizing-complex)
- `proposition-composition-open-restriction-compactifications-f` uses `lemma-change-coefficients`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekId` (proposition-composition-open-restriction-compactifications-f) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicAlgCl` (proposition-proper-direct-image-constructible-complexes--8) → `AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_integralToPadicAlgCl` (lemma-change-coefficients)
- `proposition-composition-open-restriction-compactifications-f` uses `lemma-smooth-morphisms-locally-constant-sheaves`: `AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructibleUpperShriekOfCompactification` (proposition-composition-open-restriction-compactifications-f) → `AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_isOpenImmersion` (corollary-open-direct-image-over-field--1) → `AlgebraicGeometry.Etale.exists_hasConstructibleDirectImageBaseChangeOn` (theorem-generic-constructibility-base-change-rj--2) → `AlgebraicGeometry.Etale.exists_nonempty_open_smooth_directImage_lisse_baseChange` (lemma-smooth-morphisms-locally-constant-sheaves)
- `proposition-composition-open-restriction-compactifications-f` uses `proposition-adjunction-projective-line`: `AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructibleUpperShriekOfCompactification` (proposition-composition-open-restriction-compactifications-f) → `AlgebraicGeometry.Etale.exists_dualizingComplex_iso_and_tensor` (proposition-exceptional-inverse-image-smooth-morphism--5) → `AlgebraicGeometry.Etale.exists_projectiveLineAdjunction` (proposition-adjunction-projective-line)

### 4.3: 3 detail nodes

- `corollary-torsion-jacobian-field-extension--1` uses `corollary-torsion-jacobian-field-extension--3`: `AlgebraicGeometry.nonempty_addEquiv_torsionBy` (corollary-torsion-jacobian-field-extension--1) → `AlgebraicGeometry.surjective_npow_points` (corollary-torsion-jacobian-field-extension--3)
- `corollary-torsion-jacobian-field-extension--3` uses `corollary-torsion-jacobian-field-extension--1`: `AlgebraicGeometry.Scheme.surjective_pow_picardZero` (corollary-torsion-jacobian-field-extension--3) → `AlgebraicGeometry.nonempty_addEquiv_torsionBy` (corollary-torsion-jacobian-field-extension--1)
- `corollary-torsion-jacobian-field-extension--3` uses `proposition-integral-tate-module--2`: `AlgebraicGeometry.Scheme.surjective_pow_picardZero` (corollary-torsion-jacobian-field-extension--3) → `AlgebraicGeometry.IsAbelianVariety.nonempty_linearEquiv_tateModule` (proposition-integral-tate-module--2)
- `proposition-integral-tate-module--2` uses `corollary-torsion-jacobian-field-extension--1`: `AlgebraicGeometry.IsAbelianVariety.nonempty_linearEquiv_tateModule` (proposition-integral-tate-module--2) → `AlgebraicGeometry.nonempty_addEquiv_torsionBy` (corollary-torsion-jacobian-field-extension--1)
- `proposition-integral-tate-module--2` uses `corollary-torsion-jacobian-field-extension--3`: `AlgebraicGeometry.IsAbelianVariety.nonempty_linearEquiv_tateModule` (proposition-integral-tate-module--2) → `AlgebraicGeometry.surjective_npow_points` (corollary-torsion-jacobian-field-extension--3)

### 4.4: 17 detail nodes

- `corollary-open-direct-image-over-field--1` uses `theorem-generic-constructibility-base-change-rj--2`: `AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_isOpenImmersion` (corollary-open-direct-image-over-field--1) → `AlgebraicGeometry.Etale.exists_hasConstructibleDirectImageBaseChangeOn` (theorem-generic-constructibility-base-change-rj--2)
- `definition-kunneth-map--1` uses `corollary-open-direct-image-over-field--1`: `AlgebraicGeometry.ProEtale.CondensedRing.prodLowerStarExternalProduct` (definition-kunneth-map--1) → `AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_isOpenImmersion` (corollary-open-direct-image-over-field--1)
- `lemma-change-coefficients-exceptional-inverse-image--4` uses `proposition-proper-direct-image-constructible-complexes--3`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_mateEquiv_boundedConstructibleLowerStarExtendScalarsSubfield` (lemma-change-coefficients-exceptional-inverse-image--4) → `AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--3)
- `lemma-change-coefficients-exceptional-inverse-image--4` uses `proposition-six-operations-change-coefficients--3`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_mateEquiv_boundedConstructibleLowerStarExtendScalarsSubfield` (lemma-change-coefficients-exceptional-inverse-image--4) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_padicSubfieldRingObjMap` (proposition-six-operations-change-coefficients--3)
- `lemma-kunneth-one-identity-factor--1` uses `definition-kunneth-map--1`: `AlgebraicGeometry.Etale.nonempty_iso_externalProduct_rightDerivedLowerStar` (lemma-kunneth-one-identity-factor--1) → `AlgebraicGeometry.Etale.externalProductRightDerivedLowerStarMap` (definition-kunneth-map--1)
- `proposition-composition-base-change-rf-shriek--1` uses `corollary-open-direct-image-over-field--1`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl` (proposition-composition-base-change-rf-shriek--1) → `AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_isOpenImmersion` (corollary-open-direct-image-over-field--1)
- `proposition-composition-base-change-rf-shriek--1` uses `proposition-proper-direct-image-constructible-complexes--2`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicIntegers` (proposition-composition-base-change-rf-shriek--1) → `AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--2)
- `proposition-composition-base-change-rf-shriek--1` uses `proposition-proper-direct-image-constructible-complexes--6`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicIntegers` (proposition-composition-base-change-rf-shriek--1) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicIntegers` (proposition-proper-direct-image-constructible-complexes--6)
- `proposition-composition-base-change-rf-shriek--1` uses `proposition-proper-direct-image-constructible-complexes--8`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl` (proposition-composition-base-change-rf-shriek--1) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicAlgCl` (proposition-proper-direct-image-constructible-complexes--8)
- `proposition-composition-base-change-rf-shriek--4` uses `proposition-proper-direct-image-constructible-complexes--2`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange_padicIntegers` (proposition-composition-base-change-rf-shriek--4) → `AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--2)
- `proposition-composition-base-change-rf-shriek--4` uses `proposition-proper-direct-image-constructible-complexes--3`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange` (proposition-composition-base-change-rf-shriek--4) → `AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--3)
- `proposition-composition-base-change-rf-shriek--4` uses `proposition-proper-direct-image-constructible-complexes--6`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange_padicIntegers` (proposition-composition-base-change-rf-shriek--4) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicIntegers` (proposition-proper-direct-image-constructible-complexes--6)
- `proposition-composition-base-change-rf-shriek--4` uses `proposition-proper-direct-image-constructible-complexes--7`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerShriekBaseChange` (proposition-composition-base-change-rf-shriek--4) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper` (proposition-proper-direct-image-constructible-complexes--7)
- `proposition-composition-open-restriction-compactifications-f--1` uses `corollary-open-direct-image-over-field--1`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekComp_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--1) → `AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_isOpenImmersion` (corollary-open-direct-image-over-field--1)
- `proposition-composition-open-restriction-compactifications-f--1` uses `lemma-change-coefficients-exceptional-inverse-image--4`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekComp_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--1) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_mateEquiv_boundedConstructibleLowerStarExtendScalarsSubfield` (lemma-change-coefficients-exceptional-inverse-image--4)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-composition-base-change-rf-shriek--1`: `AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_comp` (proposition-composition-open-restriction-compactifications-f--1) → `AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerShriek_comp` (proposition-composition-base-change-rf-shriek--1)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-composition-open-restriction-compactifications-f--4`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekComp_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--1) → `AlgebraicGeometry.Etale.rightDerivedUpperShriekIsoOfIsOpenImmersion` (proposition-composition-open-restriction-compactifications-f--4)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-exceptional-inverse-image-smooth-morphism--5`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekComp_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--1) → `AlgebraicGeometry.Etale.exists_dualizingComplex_iso_and_tensor` (proposition-exceptional-inverse-image-smooth-morphism--5)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-proper-direct-image-constructible-complexes--2`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekComp_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--1) → `AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--2)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-proper-direct-image-constructible-complexes--3`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekComp_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--1) → `AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--3)
- `proposition-composition-open-restriction-compactifications-f--1` uses `proposition-six-operations-change-coefficients--3`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekComp_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--1) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_app_padicSubfieldRingObjToPadicAlgCl_of_isGE` (proposition-six-operations-change-coefficients--3)
- `proposition-composition-open-restriction-compactifications-f--4` uses `corollary-open-direct-image-over-field--1`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekIsoUpperStar_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--4) → `AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_isOpenImmersion` (corollary-open-direct-image-over-field--1)
- `proposition-composition-open-restriction-compactifications-f--4` uses `lemma-change-coefficients-exceptional-inverse-image--4`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekIsoUpperStar_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--4) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_mateEquiv_boundedConstructibleLowerStarExtendScalarsSubfield` (lemma-change-coefficients-exceptional-inverse-image--4)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-composition-open-restriction-compactifications-f--1`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekIsoUpperStar_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--4) → `AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_comp` (proposition-composition-open-restriction-compactifications-f--1)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-exceptional-inverse-image-smooth-morphism--5`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekIsoUpperStar_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--4) → `AlgebraicGeometry.Etale.exists_dualizingComplex_iso_and_tensor` (proposition-exceptional-inverse-image-smooth-morphism--5)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-proper-direct-image-constructible-complexes--2`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekIsoUpperStar_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--4) → `AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--2)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-proper-direct-image-constructible-complexes--3`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekIsoUpperStar_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--4) → `AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--3)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-proper-direct-image-constructible-complexes--6`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekIsoUpperStar_padicIntegers` (proposition-composition-open-restriction-compactifications-f--4) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicIntegers` (proposition-proper-direct-image-constructible-complexes--6)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-proper-direct-image-constructible-complexes--8`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekIsoUpperStar_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--4) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicAlgCl` (proposition-proper-direct-image-constructible-complexes--8)
- `proposition-composition-open-restriction-compactifications-f--4` uses `proposition-six-operations-change-coefficients--3`: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleUpperShriekIsoUpperStar_padicAlgCl` (proposition-composition-open-restriction-compactifications-f--4) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_app_padicSubfieldRingObjToPadicAlgCl_of_isGE` (proposition-six-operations-change-coefficients--3)
- `proposition-composition-open-restriction-compactifications-f--5` uses `proposition-composition-base-change-rf-shriek--4`: `AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekBaseChangeMap_of_isOpenImmersion` (proposition-composition-open-restriction-compactifications-f--5) → `AlgebraicGeometry.Etale.isIso_rightDerivedLowerShriekBaseChangeMap` (proposition-composition-base-change-rf-shriek--4)
- `proposition-exceptional-inverse-image-smooth-morphism--5` uses `lemma-kunneth-one-identity-factor--1`: `AlgebraicGeometry.Etale.exists_dualizingComplex_iso_and_tensor` (proposition-exceptional-inverse-image-smooth-morphism--5) → `AlgebraicGeometry.Etale.nonempty_iso_externalProduct_rightDerivedLowerStar` (lemma-kunneth-one-identity-factor--1)
- `proposition-exceptional-inverse-image-smooth-morphism--5` uses `proposition-composition-base-change-rf-shriek--4`: `AlgebraicGeometry.Etale.exists_dualizingComplex_iso_and_tensor` (proposition-exceptional-inverse-image-smooth-morphism--5) → `AlgebraicGeometry.Etale.isIso_rightDerivedLowerShriekBaseChangeMap` (proposition-composition-base-change-rf-shriek--4)
- `proposition-exceptional-inverse-image-smooth-morphism--5` uses `proposition-composition-open-restriction-compactifications-f--5`: `AlgebraicGeometry.Etale.exists_dualizingComplex_iso_and_tensor` (proposition-exceptional-inverse-image-smooth-morphism--5) → `AlgebraicGeometry.Etale.isIso_rightDerivedUpperShriekBaseChangeMap_of_isOpenImmersion` (proposition-composition-open-restriction-compactifications-f--5)
- `proposition-proper-direct-image-constructible-complexes--2` uses `corollary-open-direct-image-over-field--1`: `AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--2) → `AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_isOpenImmersion` (corollary-open-direct-image-over-field--1)
- `proposition-proper-direct-image-constructible-complexes--3` uses `corollary-open-direct-image-over-field--1`: `AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--3) → `AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_isOpenImmersion` (corollary-open-direct-image-over-field--1)
- `proposition-proper-direct-image-constructible-complexes--6` uses `proposition-proper-direct-image-constructible-complexes--2`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicIntegers` (proposition-proper-direct-image-constructible-complexes--6) → `AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--2)
- `proposition-proper-direct-image-constructible-complexes--6` uses `proposition-six-operations-change-coefficients--3`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicIntegers` (proposition-proper-direct-image-constructible-complexes--6) → `AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_derivedReduction_boundedConstructibleBaseChange` (lemma-change-coefficients) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedUpperStarExtendScalarsPushHom_residueField_app` (proposition-six-operations-change-coefficients--3)
- `proposition-proper-direct-image-constructible-complexes--7` uses `proposition-proper-direct-image-constructible-complexes--2`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper` (proposition-proper-direct-image-constructible-complexes--7) → `AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--2)
- `proposition-proper-direct-image-constructible-complexes--7` uses `proposition-proper-direct-image-constructible-complexes--3`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper` (proposition-proper-direct-image-constructible-complexes--7) → `AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--3)
- `proposition-proper-direct-image-constructible-complexes--7` uses `proposition-proper-direct-image-constructible-complexes--6`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper` (proposition-proper-direct-image-constructible-complexes--7) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicIntegers` (proposition-proper-direct-image-constructible-complexes--6)
- `proposition-proper-direct-image-constructible-complexes--7` uses `proposition-six-operations-change-coefficients--3`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper` (proposition-proper-direct-image-constructible-complexes--7) → `AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_integralToRational` (lemma-change-coefficients) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_app_padicIntegers_of_isGE` (proposition-six-operations-change-coefficients--3)
- `proposition-proper-direct-image-constructible-complexes--8` uses `corollary-open-direct-image-over-field--1`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicAlgCl` (proposition-proper-direct-image-constructible-complexes--8) → `AlgebraicGeometry.Etale.boundedConstructible_rightDerivedLowerStar_of_isOpenImmersion` (corollary-open-direct-image-over-field--1)
- `proposition-proper-direct-image-constructible-complexes--8` uses `proposition-proper-direct-image-constructible-complexes--2`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicAlgCl` (proposition-proper-direct-image-constructible-complexes--8) → `AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--2)
- `proposition-proper-direct-image-constructible-complexes--8` uses `proposition-proper-direct-image-constructible-complexes--3`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicAlgCl` (proposition-proper-direct-image-constructible-complexes--8) → `AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_integralToPadicAlgCl` (lemma-change-coefficients) → `AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--3)
- `proposition-proper-direct-image-constructible-complexes--8` uses `proposition-proper-direct-image-constructible-complexes--6`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicAlgCl` (proposition-proper-direct-image-constructible-complexes--8) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicIntegers` (proposition-proper-direct-image-constructible-complexes--6)
- `proposition-proper-direct-image-constructible-complexes--8` uses `proposition-six-operations-change-coefficients--3`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_isProper_padicAlgCl` (proposition-proper-direct-image-constructible-complexes--8) → `AlgebraicGeometry.ProEtale.CondensedRing.nonempty_arrowIso_boundedConstructibleBaseChange_integralToPadicAlgCl` (lemma-change-coefficients) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_app_padicSubfieldRingObjToPadicAlgCl_of_isGE` (proposition-six-operations-change-coefficients--3)
- `proposition-six-operations-change-coefficients--3` uses `proposition-proper-direct-image-constructible-complexes--2`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleLowerStarIntegersModPowReduction'` (proposition-six-operations-change-coefficients--3) → `AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructible_rightDerivedLowerStar_obj` (proposition-proper-direct-image-constructible-complexes--2)
- `theorem-generic-constructibility-base-change-rj--2` uses `proposition-composition-base-change-rf-shriek--4`: `AlgebraicGeometry.Etale.exists_hasConstructibleDirectImageBaseChangeOn` (theorem-generic-constructibility-base-change-rj--2) → `AlgebraicGeometry.Etale.exists_nonempty_open_smooth_directImage_lisse_baseChange` (lemma-smooth-morphisms-locally-constant-sheaves) → `AlgebraicGeometry.Etale.isIso_rightDerivedLowerShriekBaseChangeMap` (proposition-composition-base-change-rf-shriek--4)
- `theorem-generic-constructibility-base-change-rj--2` uses `proposition-composition-open-restriction-compactifications-f--1`: `AlgebraicGeometry.Etale.exists_hasConstructibleDirectImageBaseChangeOn` (theorem-generic-constructibility-base-change-rj--2) → `AlgebraicGeometry.Etale.exists_nonempty_open_smooth_directImage_lisse_baseChange` (lemma-smooth-morphisms-locally-constant-sheaves) → `AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_comp` (proposition-composition-open-restriction-compactifications-f--1)
- `theorem-generic-constructibility-base-change-rj--2` uses `proposition-composition-open-restriction-compactifications-f--4`: `AlgebraicGeometry.Etale.exists_hasConstructibleDirectImageBaseChangeOn` (theorem-generic-constructibility-base-change-rj--2) → `AlgebraicGeometry.Etale.exists_nonempty_open_smooth_directImage_lisse_baseChange` (lemma-smooth-morphisms-locally-constant-sheaves) → `AlgebraicGeometry.Etale.rightDerivedUpperShriekIsoOfIsOpenImmersion` (proposition-composition-open-restriction-compactifications-f--4)

### 4.5: 2 detail nodes

- `lemma-change-coefficients-internal-hom--1` uses `proposition-six-operations-change-coefficients--7`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_constructibleExtendScalars` (lemma-change-coefficients-internal-hom--1) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_derivedExtendScalarsSubfield` (proposition-six-operations-change-coefficients--7)
- `proposition-six-operations-change-coefficients--7` uses `lemma-change-coefficients-internal-hom--1`: `AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_constructibleToPadicAlgCl` (proposition-six-operations-change-coefficients--7) → `AlgebraicGeometry.ProEtale.CondensedRing.isIso_ihomComparison_constructibleExtendScalars` (lemma-change-coefficients-internal-hom--1)

### 4.6: 2 detail nodes

- `corollary-point-counting-zeta-function--4` uses `corollary-point-counting-zeta-function--6`: `AlgebraicGeometry.Scheme.Hom.zetaSeries_eq_tprod` (corollary-point-counting-zeta-function--4) → `AlgebraicGeometry.Scheme.Hom.constantCoeff_zetaSeries` (corollary-point-counting-zeta-function--6)
- `corollary-point-counting-zeta-function--6` uses `corollary-point-counting-zeta-function--4`: `AlgebraicGeometry.Scheme.Hom.exists_int_zetaSeries` (corollary-point-counting-zeta-function--6) → `AlgebraicGeometry.Scheme.Hom.zetaSeries_eq_tprod` (corollary-point-counting-zeta-function--4)


## 5. Lean names moved back

The arrow between Section 4.5 (`sec-Proper-morphisms`) and Section D.4 (`sec-Normalization`) ran backward: `lemma-finite-morphisms--3` (finite base change, 4.5) used `lemma-finite-morphisms-cohomology--1`, `--2` (D.4), because its Lean proof uses `AlgebraicGeometry.Etale.preservesFiniteColimits_lowerStar_of_isFinite` and `AlgebraicGeometry.Etale.isIso_baseChangeMap_of_isFinite`, which #232 had put on those two clauses of D.4. Both are statements on the étale site, exactness of u_* and the underived base change for finite u: they state clause `lemma-finite-morphisms--2` of 4.5 (where they were before #248), not the pro-étale statements of D.4. Moved back, the only arrows between 4.5 and D.4 are D.4 using 4.5, as in the tex (the proof of `lemma-finite-morphisms-cohomology` cites `lemma-finite-morphisms`).

Two more names that the Lean-alignment PRs had put in a later block than the node they state, moved by the same rule:

- `AlgebraicGeometry.WeilComplex.traceFunction`: from `definition-growth-squared-traces--1` (Pure sheaves on curves) to `definition-trace-function--1` (The trace formula), the definition of the trace function of a Weil complex.
- `AlgebraicGeometry.Etale.isPerfect_compactlySupportedGlobalSections`: from `theorem-grothendieck-lefschetz-trace-formula--5` (The trace formula) to `lemma-perfect-complexes-geometric-point--4` (Verdier and Poincaré duality), "RΓ_c(X,K) is perfect"; `--5` there already has the RΓ version.

**Split of `lemma-finite-morphisms`** (both tex files). The stalk formula and the exactness of u_* for finite u are now `lemma-finite-direct-images` (clauses `--1`, `--2`), at the start of Appendix D, after its introduction; it cites nothing in chapter 4. `lemma-finite-morphisms` in 4.5 keeps the base change (clauses `--1` underived, `--2` derived) and takes the stalk formula from the new lemma. `lemma-finite-morphisms-cohomology` (D.4) no longer states that h_* commutes with base change (nothing in D used it), so its clauses are `--1` (exactness) and `--2` (cohomology). Citations of the stalk formula or exactness now point to the new lemma: the proofs of `lemma-finite-morphisms-cohomology`, `lemma-normalization-constant-sheaf`, `lemma-finite-quasi-finite-direct-images`, `lemma-reduction-field` (exactness; base change stays with `lemma-finite-morphisms`), and Example `example-finite-direct-image-double-cover`. Section arrows: `sec-Normalization` no longer uses `sec-Proper-morphisms`; `sec-Proper-morphisms` and `sec-Quasi-finite-morphisms-and-curves` use `chap-Cohomology-of-torsion-sheaves-on-curves` (in place of `sec-Proper-morphisms` for the latter). The Lean names went with their statements.

Left as they are, for a decision:

- `AlgebraicGeometry.ProEtale.mapDerivedCategoryComparisonUpperStarCompUpperStarIso` (g^*ν^* ≅ ν^*g^* on derived categories) is on `proposition-comparison-etale-derived-category--5` (Construction of f^!), which states it. The tex uses it as β_g already in Section 2.9 (`prose-02-37`: "the isomorphism above"), but no earlier declaration states it for derived categories; before #248 it was on `proposition-comparison-immersions`, which is about immersions only. 6 chapter-level backward arrows.
- `AlgebraicGeometry.ProEtale.mapDerivedCategoryOpenImmersionLowerShriekComparisonUpperStarIso` (ν^*j_! ≅ j_!ν^* on derived categories) is on `proposition-comparison-etale-derived-category--6` (Construction of f^!), which states it "induced by (2.10)". The sketch `proposition-comparison-immersions` (The pro-étale site) states it too ("and hence of functors D(U_ét,Λ) → D(X_proét,Λ)"), its clause `--1` only the underived version. 6 chapter-level backward arrows.
- `AlgebraicGeometry.ProEtale.DerivedNakayama.derived_nakayama_resolution` is on `lemma-reduction-derived-nakayama--1` (2.14), whose text #210 rewrote to state it (K_n is the cone of π^n); the coefficient sequence and its two-term resolution in the Lean statement are `corollary-finite-quotients-their-transition-maps--1`, `--2` (2.12). 1 section-level backward arrow.


## 6. Text citations against the block order

The same test on the text itself, without Lean: a citation `[id]` in a node of block A to something in block B, where B uses A
through the block arrows (so B comes later). 364 such citations; 322 are in prose (introductions and overviews: "we prove in
Chapter …", "we use this later in …"; the 36 whose wording looks like a use were read, none is one). Of the 42 in statements,
proofs, remarks and examples, most point ahead ("which we prove in Subsection …", "we return to this example", "as Theorem …
predicts", "Proposition … below is the content"). These use something later:

| # | Where | Uses | Blocks | Kind |
|---|---|---|---|---|
| 1 | `theorem-comparison-constructible-sheaves--1`, `corollary-finite-tor-amplitude-under-comparison--1` (layer 2) | `definition-constructible-sheaves` | 2.10 → Chapter 3 (Constructible complexes) | the clauses take "constructible" and "Tor amplitude" from the Chapter 3 definition; the readable text of 2.10 defines the notions for discrete rings in its own prose and says they agree with the later definition |
| 2 | `example-running-example-duality` (Frobenius and Poincaré duality) | `proposition-kummer-duality-integral-tate-module` | Verdier and Poincaré duality → Purity of real sheaves | the example justifies "H^1(C, Q_ℓ) is dual to V_ℓ J" by the later proposition |
| 3 | `lemma-removing-finitely-many-points` (D.5) | `theorem-cohomology-curves` | Appendix D → 4.4 | the statement refers to the assertions (C1)–(C8) of the theorem; the introduction of Appendix D recalls them |
| 4 | `example-locally-constant-functions-w-local` (2.2) | `proposition-pro-etale-site-separably-closed` | 2.2 → 2.12 | the example's last sentence rests on the later proposition ("below") |
| 5 | proof of `proposition-central-element-arithmetic-monodromy-group` (Central elements) | `lemma-determinant-weight-from-central-scalar` | Central elements → Tensor operations | an aside ("by Lemma … they do no harm"); the proposition does not need it, and the lemma is stated in the proposition's setting |

All five were fixed in both tex files (Nov 2026): 2.10's prose now defines Tor amplitude and D_ctf, and the two clauses refer to
§2.10; the running example takes dim H^1 = 2 from Kummer theory (Proposition `proposition-smooth-proper-curves-torsion-prime`) and
`corollary-torsion-jacobian-field-extension`; Lemma `lemma-removing-finitely-many-points` refers to the assertions listed at the start
of Appendix D; the example's sentence on pro-étale affines over a separably closed field is dropped; the aside in the proof of the
central element points ahead ("see Lemma … below"). Only the last still cites something later, as a pointer.
