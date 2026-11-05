# Fixes of the old blueprint (PRs #107–#132) checked against the new blueprint

PRs #107–#132 fixed errors in the old blueprint (now `blueprint_old/`). They came from Wei Yang's answers on Zulip (#1412, #1423, #1441, #1451, #1561), the blueprint verification (the BF items) and maintenance drafts. PRs #107–#114 were merged into the old blueprint. #115 is a tool bump. #116–#132 were still open, and their paths no longer exist.

Every fix item was checked against the new sources: `DerivedCategoryAndSixFunctorsChoice_readable.tex` (R below) and its refinement `blueprint-layer-2.tex` (L2). For each item the counterpart passage was found and its hypotheses and argument were compared, not just its wording. There are 81 items.

- **73 items need no change.** Either the new notes already get the point right (*ok*), or the statement or argument that had the defect is not in the new notes (*gone*).
- **8 items were still needed.** They are 7 distinct gaps, since #118 and #129 share Zulip #1561 item #47. They are fixed in both tex files and in `blueprint/`.

## The fixes

Line numbers are those after the change. The `blueprint/` nodes were regenerated with `scripts/retex.py`. Only the 16 nodes these edits touch differ from `main`; the `kind = "matter"` of the Introduction, which retex does not produce, was left as it is. `uses` arrows are unchanged.

| PR · item | Where (R / L2) | Gap | Fix |
|---|---|---|---|
| #130 · BF35 | `lemma-inverse-image-coefficient-sheaves`, R:3405 / L2:3970 (clause `bp-r054-2`), and the prose before it | The Tate-twist clause was stated for any morphism of schemes. Twists are defined only where ℓ is invertible (`definition-tate-twists`). | The clause, its proof and the prose now say "if ℓ is invertible on Y". |
| #130 · BF37 | proof of `lemma-descent-lisse-qbar-sheaves-finite`, R:4714 / L2:5600 | "On a quasi-compact object, taking sections commutes with filtered colimits" needs quasi-separatedness too. | "quasi-compact quasi-separated object". The argument was already applied only to qcqs objects. |
| #127 · Zulip #1561 #41 | proof of `lemma-uniform-ext-bound`, case Λ = Q̄_ℓ, R:7718 / L2:9456 (and the justification of `bp-r135-2`) | L and M were descended together to one field E before the source strata were refined, so the bound could depend on the target M. | Descend L alone to E₀, then refine the source strata and choose the lattice. Only then descend M, to some E ⊃ E₀. The bound cd_ℓ(j)+cd_ℓ(S)+2 then depends on L only. |
| #119 · BF8 | proofs of `theorem-weight-bound-affine-curve` (R:24421 / L2:31666) and `theorem-weight-bound-curve` (R:24476 / L2:31729) | The step from the weights of the stalks at the boundary points to the weights of H⁰_c(Z, ·) on the finite boundary Z had no argument. | Added the Frobenius-cycle argument over the constant field k_m of the proof: Frobenius permutes the e = [κ(z):k_m] geometric points over z, and its e-th power is F_z. Cited `lemma-finite-quasi-finite-direct-images`, which makes the same computation. |
| #113 · #19 | proof of `lemma-external-duality-trace-morphism`, R:17275 / L2:22502 | The exchange c^! RHom(P,Q) ≅ RHom(c^*P, c^!Q) was tested against any M in D(C_proét, A), but c^! is defined only on Loc(D^b_ctf). | Yoneda inside Loc(D_ctf(C,A)) = D(C_ét, A) (`proposition-comparison-etale-derived-category`), with the projection formula (Stacks 0GL5). The chain of four adjunction isomorphisms is written out. |
| #114 · #14 | proof of `theorem-verdier-biduality`, finite base field, R:15987 / L2:20657 (and the justification of `bp-r253-1`) | The step to the algebraic closure cited the curve lemma, which carries a twist (1)[2]. Nothing showed that ω pulls back to ω, or that δ is compatible with the pullback. | The comparisons of `lemma-restriction-geometric-generic-fibre` hold for g: X ×_k k̄ → X, with B = Spec k. A local embedding V ⊂ A^r_k gives g^*ω_V ≅ ω_V̄ with no twist and no shift. The argument of `lemma-double-dual-geometric-generic-fibre` then carries δ to δ, and every geometric point factors through X ×_k k̄. |
| #118 · #47 and #129 · #47 | the prose before `definition-frobenius-operator` (R:16664 / L2:21659), the definition itself, and the proof of `lemma-scheme-frobenius-geometric-frobenius` (R:18050 / L2:23500) | Three gaps. (a) "Pullback along Fr_T" on RΓ_c was never constructed. (b) Base change of Rf_! along the semilinear Fr was justified as "transport of structure", but Rf_! is built from compactifications over k. (c) T_{c_m}(ψ_m) = Frob^m was proved by an unspecified argument with mates, and compatibility with iteration was only asserted. | (a)/(b): compute with compactifications descended from k₀. Then Fr is an automorphism of the compactification that preserves the open part, and base change is transport of structure. Pullback maps pb_h on RΓ (natural and transitive, for any morphism h) define pb_{Fr_T}, independent of the compactification. (c): κ_m = θ^m with θ: F^* ≅ id; an induction gives ψ_m = φ_m κ_m; both pullback maps are computed on one compactification, and Stacks 03SP, on the étale site, shows that pullback along the absolute Frobenius is the identity on RΓ. |

Both tex files compile with pdflatex, with no errors and no undefined references. `blueprint check` reports 0 errors and 0 warnings, the same output as `main`. KaTeX renders all 561 formulas of the changed nodes. A separate review checked each fix (composition orders, labels and the Stacks tags 0739, 0GL5, 03SP), and its corrections are included: the constant field k_m in #119, the notation X_{k̄} in #114, pb_h in #47 (instead of a ♯ that looked like the ring map ♯), and qcqs intersections in #130.

Optional points found during the check, not changed:

- R:9485 says Stacks 0F0C has a finiteness hypothesis on f. 0F0C may not have one.
- `lemma-sp-reduction` (R:~14385) bounds a spectral sequence by finite cohomological dimension with no citation. Stacks 0F12 or Derived Categories 13.32.2 would do.
- `lemma-uniform-bounds-pro-etale-affines` (R:~3027) uses the alternating Čech complex without Stacks 01FM.
- The justification of clause `bp-r210-1` (L2) could say that ℓ is invertible. It follows from the conventions.
- `lemma-global-lattice-normal-scheme` cites `lemma-lattices-lisse-e-sheaves` over an arbitrary field. That lemma sits under the convention "over k", though its proof works for any qcqs X.
- In `proposition-composition-base-change-rf-shriek` (2), independence of the compactification is argued in one sentence.
- The remark after `theorem-global-verdier-duality` (finite base field) uses the global comparison g^* 𝔻_X ≅ 𝔻_{X̄} g^*. The biduality proof now gives it only locally.

## All items

*ok* means the new notes already state it correctly. *gone* means the defective statement or argument is not in the new notes. *fixed* means it was fixed here.

### Merged PRs (#107–#114)

| PR | Item | Old node | New counterpart | Verdict |
|---|---|---|---|---|
| #107 | #1 | `det-def-sfb-dc-setting` | §Conventions, R:931 | ok: k is finite or algebraically closed, char k ≠ ℓ |
| #107 | #17 | `sk-lem-stratified-lattice` | `lemma-lattices-after-finite-stratification` | gone: no normal-Noetherian statement uses it |
| #108 | #18 | `def-weil-exceptional-inverse-image` | `theorem-exceptional-inverse-image` | ok: separated schemes of finite type over k |
| #109 | #2 | `def-exchange-projection` | `proposition-composition-base-change-rf-shriek` (2) | ok (terse): refinement maps are determined on the open part |
| #109 | #4 | `prop-exc-base-change-proper` | `proposition-composition-open-restriction-compactifications-f` (3) | ok: proved by composition and j^! = j^*, with no map β |
| #109 | #15 | `lem-amb-etale-adjoint-locality`, `lem-amb-etale-compact-comparisons` | `lemma-affine-space-etale-localization`, `proposition-construction-independence-rf-shriek` | ok: torsion A, with unbounded complexes handled through Loc |
| #110 | #3 | `def-sf-setting` and others | `section-coefficient-rings`, `theorem-verdier-biduality` | ok: A is finite commutative; biduality at a point comes from perfect complexes |
| #110 | #25 | `def-sf-kv-maps` | Künneth α, R:~17090 | ok: arbitrary finite A |
| #111 | #16 | `def-sf-datum`, `rem-sf-axiom-verification`, `rem-sf-pf-done` | none | gone: there is no axiomatic package |
| #112 | #5 | `thm-pur-finite-reduction-of-purity` | eq. `sp-scalar-gamma` | ok: compared through the counit |
| #112 | #6 | `prop-pur-dnc-family-constancy` | `lemma-section-normal-bundle` | ok: pure relative dimension d |
| #112 | #7 | `def-pur-flasque-support`, `lem-pur-supported-hom` | `definition-local-cohomology` | ok: covered by the standing convention |
| #112 | #8 | `det-sp-rational-localized-hom` | eq. `sp-localized-hom` | ok |
| #112 | #9 | `thm-pur-vector-bundle-thom` | none | gone: no Thom class or sign identity |
| #112 | #21 | `det-sp-reduction-tower-normalized` | `proposition-sp-integral-towers` | ok: an arbitrary T is never claimed |
| #113 | #10 | `sk-thm-sf-kunneth-verdier` (general coefficients) | `proposition-exceptional-external-kunneth` | gone: stated for finite A only |
| #113 | #11 | `lem-fix-operation-reduction` | `lemma-change-coefficients-exceptional-inverse-image` | ok |
| #113 | #12 | `lem-exc-proetale-closed-support` | `lemma-sections-support-closed-subscheme` | ok: K-injective resolution, Stacks 079P |
| #113 | #19 | `lem-trf-exceptional-internal-hom-exchange` | `lemma-external-duality-trace-morphism` | **fixed** |
| #113 | #20 | `def-sf-kv-maps` | the prose before `proposition-exceptional-external-kunneth` | ok: Y_i separated |
| #113 | #24 | `lem-fix-weil-operations` | `definition-weil-structure`, `theorem-poincare-duality-frobenius` | ok: every admissible Λ |
| #114 | #13 | `sk-lem-finite` (complement) | `lemma-perfect-complexes-geometric-point` | gone: no complement |
| #114 | #14 | `det-pd-biduality-coefficients` | `theorem-verdier-biduality` | **fixed** |
| #114 | #23 | `prop-functor-package` (7) | `lemma-internal-adjunction-two-exchange-formulas` | ok: proved unconditionally inside Loc |

### Open PRs (#116–#132, now closed)

| PR | Item | Old node | New counterpart | Verdict |
|---|---|---|---|---|
| #116 | BF2 | `lem-fd-first-formula` | `lemma-fourier-transform-constant-sheaf` | ok: ψ is nontrivial by definition |
| #116 | Zulip #1441 #32 | `sk-cor-plancherel` | `corollary-plancherel`, `proposition-fourier-inversion` | gone: the rank-r form K(−r) is stated |
| #116 | Zulip #1441 #36 | `thm-a1-curve-perverse-heart` | `lemma-perverse-sheaves-curve` | gone: an elementary proof, with no duality step |
| #116 | bpq #49 | `lem-fd-inversion`, `lem-fd-convolution-kernel` | Fourier setup, R:22801 | ok: includes S = Spec k |
| #117 | BF4 | `def-weil-pbc-scheme-conventions` | §Conventions | gone |
| #117 | BF15 | `def-weil-finite-tor-amplitude` | `definition-constructible-sheaves` | gone: no claim that it is triangulated |
| #117 | BF16 | `lem-sc-cd-affine-limit` | `lemma-uniform-bounds-pro-etale-affines` | gone: uses Stacks 03Q6 |
| #118 | BF7 | `cor-coef-integral-internal-hom` | `lemma-change-coefficients-internal-hom` | ok |
| #118 | BF9 | `def-pur-smooth-pullback-exchange` | `definition-exceptional-base-change-map` | ok |
| #118 | BF10 | `lem-pur-support-localization-triangle` | `lemma-local-cohomology-right-adjoint` | ok |
| #118 | BF13 | `thm-pur-kummer-affine-line` | none | gone: P¹ and localization are used instead |
| #118 | BF20 | `lem-kun-0f0c` | `theorem-results-from-etale-theory` | gone: Stacks 0F0C is cited |
| #118 | BF22 | `lem-pur-frame-independence` | `proposition-purity-vector-bundles` | gone: no Smith normal form |
| #118 | BF24 | `thm-pur-with-support-exactness` | `lemma-sections-support-closed-subscheme` | ok: injective terms, Stacks 079P |
| #118 | BF27 | `lem-sf-projection-finite-constant` | `lemma-change-coefficients-direct-image` | ok: Stacks 0F12 |
| #118 | Zulip #1441 #26 | `thm-pur-rank-one-thom` | trace of the affine line, R:13644 | gone |
| #118 | Zulip #1441 #28 | `thm-fix-general-biduality` | `theorem-verdier-biduality` | ok (its finite-field step: see #114 #14) |
| #118 | Zulip #1441 #29 | `lem-coef-finite-closed-shriek` | `lemma-change-coefficients-exceptional-inverse-image` | ok: no biduality, no cycle |
| #118 | Zulip #1451 #37 | `det-sp-rational-localized-hom` | eq. `sp-localized-hom` | ok |
| #118 | bpq #39 | `det-sp-orientation-charts`, `det-sp-orientation-vector-bundle` | `proposition-relative-dualizing-complex` | ok |
| #118 | #42 (bpq and #1561) | `det-sp-tower-gluing` | `proposition-sp-tower-geometric` | ok: the extension-by-zero cone, transitions by transposition |
| #118 | #46 (bpq and #1561) | `det-sp-scalar-extension-functor` | `definition-sp-scalar-extension`, `lemma-extension-scalars-preserves-dctf` | ok |
| #118 | Zulip #1561 #47 | `def-weil-global-geometric-frobenius` | `definition-frobenius-operator` | **fixed** |
| #119 | BF8 | `lem-a1-finite-boundary-weights` | `theorem-weight-bound-affine-curve`, `theorem-weight-bound-curve` | **fixed** |
| #120 | BF11 | `sk-cor-hasse` (abstract complement) | `corollary-point-count-estimates` | gone |
| #120 | BF25 | `thm-weil-final` | `theorem-weil-conjectures-smooth-proper-schemes` | ok |
| #121 | BF12 | `sk-thm-sf-tensor-hom` (complement) | `lemma-internal-adjunction-two-exchange-formulas` | gone |
| #121 | BF23 | `thm-pod-proper-poincare-duality` | `theorem-poincare-duality` | ok: ⊗^L_Λ with target Λ |
| #121 | Zulip #1441 #29 | `lem-coef-finite-exceptional` | `lemma-change-coefficients-exceptional-inverse-image` | ok |
| #121 | bpq #43 | `prop-trf-compact-support-perfectness` and others | `lemma-perfect-complexes-geometric-point`, `proposition-proper-direct-image-finite-coefficients` | ok: any finite ℓ-primary A |
| #121 | Zulip #1561 #43 | as above | as above | ok: the requested order of the argument |
| #122 | BF14 | `sbc-thm-finite-proetale-smooth-base-change` | `theorem-smooth-base-change-all-admissible` | ok (R); optional wording in L2 |
| #122 | Zulip #30 | `fix-prop-adjunctions` (composite unit) | none | gone |
| #122 | Zulip #31 | `fix-prop-adjunctions` (agreement with refinements) | `theorem-existence-exceptional-inverse-image` | gone: a single Rf_! |
| #123 | BF17 | `lem-chow-graph` | `theorem-chow-s-lemma-projective-form` | gone: Stacks 0202 is cited |
| #123 | BF31 | `sk-lem-nagata-sketch-boundary` | `lemma-separation-closures` | ok: no typo |
| #123 | BF39 | `thm-nagata-blowup-universal-property` | none | gone |
| #123 | BF41 | `lemma-nagata-diagonal-finite-presentation` | Nagata proof, R:26700 | gone |
| #124 | BF19 | `lem-galois-aut-profinite` | none | gone |
| #124 | BF38 | `lem-sc-ga-cohomology` | `proposition-p-torsion-smooth-proper-curve` | gone |
| #125 | BF21 | `lem-pc-very-ample-descends` | none | gone |
| #125 | BF32 | `lem-pc-projective-space-cohomology-bound` | none | gone |
| #126 | BF26 | `lem-tw-punctual-rescaling` | `proposition-weights-under-usual-operations` | ok |
| #126 | Zulip #1441 #33 | `lem-zl-quasi-finite` | `lemma-finite-quasi-finite-direct-images` | ok: separated by `situation-weil` |
| #126 | Zulip #1451 #38 | `lem-zl-composition-weight-bound` | `theorem-direct-image-mixed-sheaf` | ok |
| #127 | BF28 | `lem-weil-derived-tensor-resolution-independent` | none | gone |
| #127 | bpq #41 | `det-uniform-constructible-ext-rational` | `lemma-uniform-ext-bound` (case E) | ok |
| #127 | Zulip #1561 #41 | `det-uniform-constructible-ext-rational` | `lemma-uniform-ext-bound` (case Q̄_ℓ) | **fixed** |
| #128 | BF33 | `lem-kun-0f11` | the compactness proof, R:8228 | gone: Stacks 0F11 is cited with finite cd |
| #128 | BF36 | `thm-amb-p1-decomposition` | `lemma-cohomology-projective-line-trace` | ok: S is Noetherian and ℓ is invertible on it |
| #129 | BF34 | `det-tf-punctured-restriction-factorization` | `lemma-restriction-punctured-curve` | ok: N is bounded and j is affine |
| #129 | Zulip #1561 #47 | `prop-trf-graph-frobenius-operator` | `lemma-scheme-frobenius-geometric-frobenius` | **fixed** |
| #130 | BF35 | `sk-prop-sfb-cartesian-coefficients` | `lemma-inverse-image-coefficient-sheaves` | **fixed** |
| #130 | BF37 | `det-lem-coefficient-finite-descent-sections` | `lemma-descent-lisse-qbar-sheaves-finite` | **fixed** |
| #131 | BF40 | `lem-weil-pbc-normal-constant-generic` | none | gone |
| #132 | Zulip #1423 | `def-trf-admissibility` | none | gone: f^! for every admissible Λ |
| #132 | Zulip #1441 #27 | `def-trf-coefficient-conventions` | the trace formula, R:17836 | ok: any finite ℓ-primary A |
