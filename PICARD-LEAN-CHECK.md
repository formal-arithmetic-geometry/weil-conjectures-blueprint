# Picard Framework: findings (2026-10-19)

Lean reference: `slopmaster2` at 1e776bcfb6. Every Lean name in the section exists there, and none of the
declarations contains `sorry`. Only files under `blueprint/sec-picard-framework/` were edited (206 files, uncommitted,
on branch `nagata-abelian-lean-check`). Graph check: no `uses` cycles, no dangling uses, no uses of remarks.
`lake exe blueprint check`: see the end of this summary.

## 1. Statements vs Lean

| | Nodes |
|---|---:|
| Already matched their Lean declarations | 142 |
| Fixed to follow Lean (statement and/or Lean names) | 95 |
| Lean names added (had none) | 22 |
| Without any Lean counterpart | 0 |

Main changes:
- **Riemann–Roch block** (`sk-thm-picard-rr`): hypothesis is now "smooth proper curve with H^0(C,O)=k"
  (Lean), instead of "smooth projective geometrically connected"; full coherent Riemann–Roch
  (`eulerChar_eq_coherentDegree_add`) replaces the free-sheaf version; "identifications commute with field
  extension" weakened to "genus and degree are invariant under field extension" (Lean has no base change of the
  duality/trace). `lem-sc-negative-degree-no-sections` was false for disconnected curves (two disjoint P^1); fixed.
- **Semicontinuity / base change** (`sk-thm-picard-semicon`): Lean states the base-change results over an affine
  base in Čech form; the lemmas were restated so, and the base-change isomorphism (Grauert) now needs a reduced
  locally Noetherian base. Nine proofs that used the old global form were rewritten along Lean's routes
  (`lem-pc-rational-hyp`, `prop-pc-xk-integral`, `lem-pc-flat-rf-open`, `lem-pd-degree-locally-constant`,
  `lem-pc-f-open-subfunctor`, `lem-pc-zero-scheme-recd`, `thm-pc-f-representable`, `lem-pc-flf-properties` (it used
  flat base change along the non-flat Spec κ(s)→S), `lem-pc-vanishing-above-dim`).
- **Coherent base change** (`sk-thm-picard-perfect`) and coherence (a): Rf_* is locally a finite free complex in
  degrees [0,d] with R^q f'_* ≅ H^q(g^*P) for every base change (Lean `IsFiniteFreeComplex`), instead of a
  canonical derived base-change isomorphism.
- **Descent / representability**: `lem-pc-fpqc-descent` without flatness; `lem-pd-morphisms-descend` needed a
  faithfully flat quasi-compact hypothesis (was false without it); `thm-pd-fpqc-local-properties` for any field
  extension; the representability criterion over S-schemes with small values, pointing at the project's
  `isRepresentable_of_isSheaf_of_zariskiCovers`.
- **Duality**: `lem-sc-finite-duality` needed a generic-separability hypothesis (was false without it).
- **Divisors and line bundles**: `lem-pc-divisor-line-bundle-agrees-sc` now gives equality of classes in Pic only;
  `lem-sc-line-bundle-rational-section` says L ≅ O(E1)⊗O(−E2) for effective E1, E2.
- **Subfunctor F / open chart** (`sk-def-picard-f`, `sk-thm-picard-f-representable`): X proper; k separably closed
  (Lean's hypothesis).
- Wrong Lean names replaced, e.g. `def-pc-fppf-site` (pointed at the Hilbert-sheaf theorem),
  `def-pc-subfunctor`, `lem-pc-projective-space-twist-cohomology` (field-level names on a ring-level statement),
  `lem-pc-twist-cocycle`.

### Decisions for the user
- Duplicate candidates (not deleted):
  - `det-picard-rr-duality` -> keep `lem-sc-riemann-roch-large-degree` (its h^0(ω)=g, h^1(ω)=1 already moved to
    `lem-sc-canonical-degree`); nothing uses it.
  - `lem-pc-genus-well-defined` -> keep `lem-pc-euler-characteristic-well-defined` (special case).
  - `det-picard-pic-split-pairs`: borderline delete candidate - only its "no automorphisms" part is in Lean; the
    pairs <-> classes bijection is not formalised.
- Possible duplicates across sections (flagged only): `lem-pc-smooth-characterization` vs `sbc-lem-smooth-criterion`;
  `lem-pc-affine-vanishing` vs `pqf-lem-affine-vanishing`; `lem-pc-tensor-dual-invertible` vs `lem-sc-invertible-dual`;
  `det-cor-jacobian-torsion-pic` vs `lem-sc-pic-proper-ntorsion`; `def-sc-effective-cartier-divisor` vs
  `def-nagata-invertible-ideal`; `lem-sc-flat-base-change-coherent` vs `lem-pc-flat-base-change-cohom`;
  `lem-pc-genus-base-change` vs `lem-sc-genus-invariant`.

### Broken outside the section (not edited)
- `rem-pc-sc-divisor` (Abelian Varieties): still says the divisor module *is* the one of
  `def-pc-divisor-line-bundle`; Lean (and now `lem-pc-divisor-line-bundle-agrees-sc`) gives only equality of classes.
- `lem-sc-divisor-class-curve` (Curve Estimates): its proof cites the old rational-section wording of
  `lem-sc-line-bundle-rational-section`.

### Smaller open points inside the section
- The sketch proofs of `sk-lem-picard-f-open`, `sk-prop-picard-degree-decomposition` and `sk-prop-jacobian-descent`
  still phrase base change in the old (derived) form; they remain true in the per-degree form.
- No node carries Lean's global derived model `exists_derived_model_higherDirectImage`, which the sketch proof of
  `sk-thm-picard-perfect` relies on.
- `lem-pc-vanishing-above-dim` now cites nodes in other Picard blocks that `sk-thm-picard-twist` does not declare
  (possible undeclared-edge infos).
- `lem-pd-canonical-descent-datum` claims a full descent datum but proves only the isomorphism (cocycle is in
  `lem-pd-descent-cocycle`); title of `thm-pd-effective-descent` says "quasi-projective" for a projective statement.

## 2. Correspondence with Appendix C of the tex

| Appendix C | Label | Block | Remarks |
|---|---|---|---|
| Def. Relative Picard functor | (subsection `app:picard-functor`) | `sk-def-picard-pic` | same; blueprint adds an example and notation |
| Lem. Rigidification along a section | `app:picard-rigidification` | `sk-prop-picard-pic-split` | same |
| Thm. Riemann–Roch and coherent Serre duality | `app:picard-riemann-roch` | `sk-thm-picard-rr` | Lean hypotheses (H^0=k); field-extension clause weakened; blueprint proves RR where the tex quotes Stacks 0B5B |
| Lem. Coherent base change for invertible sheaves | `app:picard-coherent-base-change` | `sk-thm-picard-perfect` | now per-degree isomorphisms and a local free complex (Lean), not derived base change |
| Thm. Hilbert schemes of points on a smooth curve | `app:picard-hilbert-theorem` | `sk-thm-picard-hilb-curves` | route via the general Hilbert representability block instead of Stacks 0B9A/0B9I |
| Prop. Divisors of degree g as an open chart | `app:picard-abel-chart` | `sk-thm-picard-f-representable` | assumes k separably closed (Lean); tex does not |
| Lem. Translating into the chart | `app:picard-twist` | `sk-thm-picard-twist` | same |
| Thm. Picard scheme and Jacobian | `app:picard-curve` | `sk-thm-picard-main` | same, plus a separably-closed complement |
| Cor. The degree sequence | `app:picard-degree` | `sk-cor-picard-degree` | same |
| Rem. Arbitrary ground fields and bases | `app:picard-relative-scope` | `sk-rem-picard-relative-scope` | same |
| Prop. Multiplication on an abelian variety | `app:abelian-multiplication` | `sk-thm-av-final` (Abelian Varieties) | not in this section |
| Cor. Torsion of the Jacobian | `app:jacobian-torsion` | `sk-cor-jacobian-torsion` | same route |
| Prop. The Jacobian over the ground field | `app:jacobian-ground-field` | `sk-prop-jacobian-descent` | **route differs**: tex via algebraic spaces (Stacks 0D2C, 0B8F); blueprint and Lean via Galois descent from the separable closure |
| Prop. Compatible Kummer and Tate modules | `app:jacobian-equivariant-kummer` | none here | lives in Purity of Real Sheaves (`sk-d-real-jacobian`) |

**Blueprint-only blocks (26, orders 714–740)**, all proof ingredients of the tex declarations; candidate homes if
folded one-to-one as was done for Nagata:

| Blocks | Used by the tex declaration |
|---|---|
| `sk-def-groth-ss`, `sk-thm-groth-ss`, `sk-thm-picard-cech`, `sk-lem-picard-affine`, `sk-lem-picard-cech-computes`, `sk-thm-picard-pn`, `sk-thm-picard-serre-a`, `sk-thm-picard-serre-b`, `sk-thm-picard-coherence`, `sk-thm-picard-semicon` | coherent base change (`sk-thm-picard-perfect`) |
| `sk-thm-picard-duality` | Riemann–Roch (`sk-thm-picard-rr`) |
| `sk-thm-picard-descent`, `sk-cor-picard-pic-sheaf` | Picard functor / rigidification |
| `sk-the-hilbert-functor--definition-1`, `sk-cor-picard-hilb-sheaf`, `sk-thm-picard-hilb-general` | Hilbert schemes of points |
| `sk-def-picard-f`, `sk-lem-picard-f-open`, `sk-lem-picard-zero-dictionary`, `sk-the-subsheaf-ff-and-its-representability--remark-1`, `sk-cor-picard-degree-g` | open chart (`sk-thm-picard-f-representable`) |
| `sk-prop-picard-dense-points` | translating into the chart (`sk-thm-picard-twist`) |
| `sk-prop-picard-schemes-criterion`, `sk-thm-picard-criterion`, `sk-prop-picard-degree-decomposition`, `sk-prop-picard-jacobian-tangent` | Picard scheme and Jacobian (`sk-thm-picard-main`) |

**Block-level cycles** (both already present at HEAD): `sk-prop-picard-degree-decomposition` <-> `sk-thm-picard-main`
and `sk-prop-picard-jacobian-tangent` <-> `sk-thm-picard-main`. Both blocks are parts of the tex theorem
`app:picard-curve`; folding them into `sk-thm-picard-main` would remove the cycles.

## Blueprint check

`lake exe blueprint check` on the tree with all Picard changes: **0 errors, 29 warnings** - the same 29 as before this round (all `[bad-link]` warnings in sec-proper-base-change/sk-thm-p1, pre-existing and unrelated to Picard). Info-level notices dropped from 3433 to 3429.

---

# Per-node details (from the five block checks and the follow-up)


## Statements or Lean names fixed to follow Lean

- `def-sp-etale-dictionary`: Lean proves that (f_*, h_*) is a composable pair with acyclicity; the text only named the pair **Fix:** added the clause that (f_*,h_*) is a composable pair with acyclicity because f_* is right adjoint to the exact f^{-1}
- `lem-sc-cech-spectral`: Lean assumes the site is essentially small **Fix:** added 'essentially small' to the hypotheses (the small etale and Zariski sites it is applied to satisfy it)
- `sk-thm-picard-cech`: same missing essential-smallness hypothesis (sketch) **Fix:** added 'essentially small'
- `lem-sp-right-adjoint-preserves-injectives`: Lean only needs u to preserve finite limits (arbitrary categories), not exactness between abelian categories **Fix:** statement generalised to finite-limit-preserving u (exact functor as example); proof now derives mono-preservation from preservation of kernel pairs
- `thm-sp-grothendieck-base-change`: text claimed a morphism 'natural in all the data' between the two sequences and required C, C' Grothendieck; Lean gives a morphism from gamma applied to the sequence of X to the sequence of alpha X, natural in X, equal on E_2 to the base-change morphism, with C, C' only abelian **Fix:** hypotheses restated (A,B,A',B' Grothendieck, C,C' abelian, left exact additive F,G,F',G'); conclusion made precise (direction, naturality in X, E_2 component); proof Step 2 gained a sentence on gamma and on the E_2 map
- `lem-pc-affine-cech-complex`: Lean states exactness in positive degrees of the (non-augmented) Cech complex of a quasi-coherent sheaf for a standard cover {D(f_i)} of an affine open; text claimed exactness of the augmented complex of modules **Fix:** statement rewritten in Lean's form (scheme, affine open V, quasi-coherent F, exact in positive degrees) with the dictionary V=Spec A, F(D(f...))=M_f...; proof adds the translation and still proves the augmented version
- `lem-pc-projective-space-twist-cohomology`: the four listed declarations are the field versions (P^n_k), the node is over an arbitrary commutative ring A; the ring versions exist **Fix:** Lean names replaced by the ring-level declarations: nonempty_H_twist_linearEquiv_monomialCechComplex_homology, nonempty_H_zero_twist_linearEquiv, subsingleton_H_zero_twist_of_neg, subsingleton_H_twist_of_ne_of_commRing, nonempty_H_twist_top_linearEquiv_finsupp, twistHTopBasis, subsingleton_H_twist_top_of_commRing, nonempty_H_twist_top_linearEquiv_self, subsingleton_H_twist_of_pos_of_commRing, finite_H_twist, nonempty_H_zero_twist_linearEquiv_of_card_eq_one (all AlgebraicGeometry.ProjectiveSpace.*)
- `lem-pc-twist-cocycle`: wrong declaration: twist is the definition of O(d), not the cocycle rule **Fix:** removed it from this node (moved to def-pc-projective-space-twist); transitionUnit_mul_transitionUnit kept
- `sk-thm-picard-coherence`: only (b) was covered; (a) in Lean (exists_isFiniteFreeComplex_higherDirectImage) gives, locally, a finite free complex P with H^q(g^*P) = R^q f'_* F' for each base change g and q separately (no derived-level/canonical base change, no 'perfect'), and the local vanishing bound d_U is not tied to fibre dimension **Fix:** (a) rewritten minimally to the Lean form; fibre-dimension clause replaced by 'for some d_U'; Lean names for (a),(c) and quasi-coherence added
- `def-pc-derived-direct-image`: text defined R^if_* as cohomology sheaves of Rf_*; Lean defines R^if_* (higherDirectImage) as the classical right derived functors of f_* on modules **Fix:** text now defines R^if_* as right derived functors of f_* (with R^if_*E=H^i(Rf_*E) for a module); added AlgebraicGeometry.Scheme.Modules.higherDirectImage
- `def-sc-kahler-differentials`: text defined Omega^1 as Delta^*(I/I^2); Lean defines it as the sheafification of the presheaf of Kaehler differentials (affine description via relativeDifferentialsRestrictFromSpecIso) **Fix:** primary definition now the sheafified presheaf of Kaehler differentials with its affine description; Delta^*(I/I^2) kept as a parenthetical equivalent
- `lem-sc-canonical-sheaf`: Lean: Omega^1_{X/S} is invertible for any f smooth of relative dimension one; text only for a smooth connected curve over k **Fix:** statement generalised (curve case kept as 'in particular'); proof rewritten over a base ring R via the Jacobian criterion, plus the reduction of the curve case
- `lem-sc-p1-monomial`: Lean holds over any field, text required k algebraically closed; the monomial basis of H^1 was not covered by a listed name **Fix:** 'algebraically closed' dropped (proof never used it); added AlgebraicGeometry.ProjectiveSpace.nonempty_H_twist_top_linearEquiv_finsupp for the basis
- `lem-pc-finite-linear-avoidance`: Lean does not need V finite-dimensional **Fix:** finite-dimensionality dropped; proof gains a reduction to the span of finitely many witnesses
- `lem-pc-projective-curve-linear-pair`: Lean only assumes Proj(S) has dimension one (S a standard graded domain), text assumed Proj(S) is a curve **Fix:** hypothesis changed to 'Proj(S) has dimension one (for instance a curve)'; proof now derives Noetherian/irreducible/1-dimensional directly instead of citing def-pc-curve
- `lem-pc-projective-coordinate-model`: Lean gives an integral standard graded S with X = Proj(S) over k (i over k); it does not state that S = k[x]/I for a homogeneous prime I nor that the iso is induced by i **Fix:** statement reduced to the Lean form (closed immersion over k; exists S and an iso over k); proof still constructs S = k[x]/I and notes the iso is over k
- `sk-thm-picard-perfect`: Claimed that the derived pullback of Rf_{T,*}L is canonically Rf_{T',*}L_{T'}, that formation of f_*L commutes with arbitrary base change via canonical maps, and that the semicon base-change maps are isomorphisms on U_{i,r} (no Noetherian hypothesis). Lean gives only a local finite free model P with H^q(g^*P) ≅ R^q f'_*F', and for g into U_{i,r} the existence of an isomorphism R^i f'_*F' ≅ g^*R^i f_*F. The Noetherian-approximation paragraph is not needed by Lean. **Fix:** Statement minimally edited to these forms (local model with H^q(a^*P) ≅ R^q f_{T',*}L_{T'}; existence of f_{T',*}L_{T'} ≅ a^*f_{T,*}L on the locus; arbitrary T handled by the general form; i ≥ 0; factorisation criterion spelled out on cohomology sheaves). Proof rewritten: local model from sk-thm-picard-coherence (a), splitting reductions up to homotopy (stable under pullback), and a global isomorphism R^if'_*F' ≅ g^*R^if_*F from a derived model of Rf_*F with degreewise base change (Lean exists_derived_model_higherDirectImage).
- `sk-thm-picard-semicon`: The statement now carries the locally Noetherian hypothesis, but it did not say where the canonical base-change maps come from (Lean defines them only for affine bases, through Čech complexes). The proof still claimed that Grauert's theorem needs no Noetherian hypothesis, and it used (a) as a perfect complex whose formation commutes with base change. **Fix:** Statement: the base-change maps are defined through Čech complexes of a finite affine cover over an affine open neighbourhood of t. Proof rewritten: semicontinuity and local freeness come from the local model of (a); the base-change map is 1⊗[z] ↦ [z⊗1] on Čech complexes; Grauert follows Lean: over a reduced Noetherian affine base the Čech complex is perfect compatibly with base change, then the normal form over A_p when h^q is constant on generizations. Added uses = [sk-thm-picard-coherence] to the proof file.
- `lem-pc-sigma-subfunctor`: Lean is for any f:X->S with a section; text only for X over a field with a rational point **Fix:** statement and proof generalized to f:X->S with section sigma (k-point case kept as example)
- `lem-pc-picard-functor-agrees-sc`: Lean holds for any scheme X over any commutative ring k (and affine restriction over any S); text required smooth projective curve over a field **Fix:** statement generalized (curve case as instance, general-S sentence added); proof notes it uses nothing about X
- `cor-pc-sigma-pic-iso`: Lean also covers integral proper X, and smooth rel. dim 1 proper geometrically integral X **Fix:** hypothesis widened by a parenthetical; proof unchanged (rests on lem-pc-rational-hyp, which now covers both cases)
- `lem-pc-degree-agrees-sc`: Lean gives deg O(E) = sum n_P [kappa(P):k] over any field; text only stated the algebraically closed comparison **Fix:** statement now gives the general formula, with the alg. closed case = deg D of def-sc-pic0; proof already proved it
- `lem-pc-rational-hyp`: Lean covers integral proper X with a section, and (without a section) smooth rel. dim 1 proper geometrically integral X **Fix:** statement widened; proof paragraph added for the geometrically integral case via lem-pc-h0-proper-variety (2)
- `lem-pc-structure-pushforward`: Lean: any proper X over k with H^0=k, and the canonical map O_T -> f_{T*}O is an iso; text: smooth projective curve, abstract iso **Fix:** statement generalized to proper X and stated for the canonical map; proof last sentence adjusted
- `def-pc-invertible-in-degree-zero`: Lean defines the condition on a family of (cohomology) modules M^q, not on an object of D(O_X) **Fix:** definition rewritten on families M^q (vanishing for q != i, M^i finite locally free of rank r; i=0,r=1 invertible), with the equivalent derived-category reading kept as a remark sentence
- `lem-pc-hilb-addition`: Lean needs only Hilb^d and Hilb^{d+1} representable, and describes the map on T-points as the ideal product I_Z * I_{Gamma_x}; text assumed all Hilb^e and said 'scheme-theoretic addition' **Fix:** hypothesis weakened to Hilb^d, Hilb^{d+1}; T-point description made precise
- `lem-pc-recd-locally-principal`: Lean: flat and locally of finite presentation; text: of finite presentation **Fix:** hypothesis weakened to locally of finite presentation
- `lem-pc-recd-pullback`: Lean: flat and locally of finite presentation; text: of finite presentation **Fix:** hypothesis weakened to locally of finite presentation
- `lem-pc-tensor-dual-invertible`: Lean proves M -> M^vv only as existence of an isomorphism (evaluation is canonical); lean list held only the biduality lemma **Fix:** statement: evaluation map canonical iso, M ≅ M^vv; four missing Lean names added
- `lem-pc-universal-divisor`: Lean: any X->S smooth of rel. dim 1, any d, H representing Hilb^d; universal object is a relative effective Cartier divisor and O(D_h) ≅ pullback of O(D_univ) for every T-point h. Text: only over k for Hilb^{d+1} and only the restriction to k-rational fibres **Fix:** statement and proof rewritten in Lean generality (index now d, not d+1); the k-rational-fibre statement kept as 'in particular'
- `lem-pc-projection-formula`: Lean only has R^q f_*(F ⊗ f^*N) ≅ R^q f_*F ⊗ N for N invertible (any f, any O_X-module F); text claimed the derived projection formula for qcqs f and K in D_QCoh **Fix:** statement weakened to the Lean form; new proof (q=0 local check, then derived functors since tensoring with an invertible module is an exact autoequivalence preserving injectives). Its only user (thm-pc-f-representable proof) needs only this form; def-pc-derived-category edge dropped
- `lem-pc-universal-adjoint-section`: Lean is the per-T form over any field (no separably closed hypothesis): quasi-coherence of f_{T*}O(D), cancellation of the sigma-terms, and Z(adjoint section) = D for L in F(T) with L ≅ O(D) ⊗ f_T^*N; text was a muddled H-only statement ('section 1 of O(D_univ) ⊗ f^*N_H^{-1}') **Fix:** statement rewritten as the three per-T assertions plus the H/W case as 'in particular'; new proof; uses: +def-pc-f-subfunctor, +def-pc-finite-locally-free, +lem-pc-projection-formula, -def-pc-separably-closed
- `sk-thm-picard-f-representable`: Lean requires k separably closed; sketch had no hypothesis on k **Fix:** added 'k is separably closed' (see sketch_changes)
- `def-pc-genus`: Lean defines dim_k H^1(X,O_X) for any k-scheme; text restricted to geometrically irreducible smooth projective curves **Fix:** context widened to proper k-schemes (curve case kept as the typical case)
- `lem-pc-vanishing-above-dim`: Lean: X smooth of rel. dim 1 and proper over k; text: smooth projective curve **Fix:** statement generalized; proof gets a Step 0 reducing to integral components and to projectivity (Tag 0A26)
- `prop-pc-xk-integral`: Lean needs no rational point (X connected, smooth, proper over separably closed k); lean list lacked the H^0/H^1 base-change names **Fix:** parenthetical stating the result without sigma; proof paragraph added (H^0 = k by separability); added Scheme.GlobalSectionsBijective.pullback and Scheme.arithmeticGenus_pullback
- `thm-sc-theorem-of-the-base`: Lean: C smooth of rel. dim 1, proper, geometrically integral; text: smooth projective curve **Fix:** hypothesis widened (projective curve kept as example); proof already argues for proper curves
- `lem-sc-pic-proper-decomposition`: Lean: any nonempty k-scheme smooth of rel. dim 1 and proper (no connectedness) **Fix:** hypothesis widened by a parenthetical; added picDegreeHom, coe_ker_picDegreeHom, surjective_picDegreeHom
- `lem-pc-fpqc-descent`: part (2) claimed that flatness descends; Lean has only finite presentation, local freeness (with f.p.), rank r and invertibility (Descent.lean: flatness of modules has no Mathlib name) **Fix:** dropped flatness from part (2); proof's '(2)' paragraph adjusted (Step 2 keeps flatness only as an auxiliary step)
- `def-pc-fppf-site`: wrong declaration (the Hilbert sheaf theorem, not the site) **Fix:** lean replaced by Scheme.fppfPrecoverage, Scheme.fppfTopology, GrothendieckTopology.over (Mathlib)
- `def-pc-subfunctor`: wrong declaration (the representability criterion); also stated on Sch while Lean works on Sch/S **Fix:** lean -> CategoryTheory.Subfunctor; text now for F:(Sch/S)^op->Sets
- `def-pc-cover`: text asked for an open covering indexed by I itself (one U_i per subfunctor); Lean ZariskiCovers is pointwise (each t has an open U and some index i), and lives on Sch/S **Fix:** rewritten to the pointwise form, with the equivalent 'open covering T=U_a with indices i_a' form; over Sch/S
- `def-pc-open-subfunctor`: Lean on (Sch/S), text on Sch **Fix:** text over S-schemes
- `lem-pc-schemes-criterion`: wrong declaration: Mathlib's version is about morphisms from representables on absolute Sch; the subfunctor form of this node is the project theorem, which is over S and needs small values **Fix:** lean -> AlgebraicGeometry.isRepresentable_of_isSheaf_of_zariskiCovers; text over Sch/S with small values, conclusion 'scheme over S'
- `def-pc-f-subfunctor`: Lean requires X -> Spec k flat, proper, locally of finite presentation; text had an arbitrary k-scheme **Fix:** added 'proper' (flat and lfp are automatic over a field for a proper scheme)
- `lem-pd-morphisms-descend`: Lean needs X->Y flat, surjective, quasi-compact; text had an arbitrary morphism (false in general) **Fix:** added 'faithfully flat and quasi-compact' hypothesis; proof notes it is an fpqc covering (only user lem-pd-group-scheme-descent applies it to a finite separable extension, fine)
- `thm-pd-fpqc-local-properties`: text restricted to finite K/k and omitted the proper/smooth-of-rel-dim-n/geometrically-integral descent carried by the listed names **Fix:** K/k arbitrary field extension; part (2) added; proof rewritten for arbitrary extensions (fpqc locality on target, no finite presentation of Z_K->Z) plus geometric integrality argument
- `lem-pc-zero-scheme-properties`: lean list did not cover the defining object or the closing claim I_{Z(s)} = im(s^vee) **Fix:** added Scheme.Modules.Hom.zeroLocus and Scheme.Modules.Hom.imageSubobject_dualMap_comp_dualUnitIso
- `lem-pc-zero-scheme-recd`: listed name only treats N = f_{T,*}L and the adjunction map, not an arbitrary N with the adjoint section s **Fix:** added exists_isEffectiveCartierCenter_hilbertPresheaf_zeroLocus_adjointSection and Scheme.Modules.Hom.zeroLocus_adjointSection_comp_whiskerLeft
- `the-subsheaf-ff-and-its-representability--remark-1`: the inverse formula on the image and 'W represents F through Phi' were not covered **Fix:** added invertibleDirectImageToHilbert, hilbertToPicardNormalized_invertibleDirectImageToHilbert, exists_representableBy_invertibleDirectImageToHilbert
- `prop-pd-picard-degree-decomposition`: only part (2) covered; parts (1), (3), (4) and delta had no names **Fix:** added picardDegree_mul, mul_mem_picardSubfunctorDegree, exists_decomposition_picardFunctor_representableBy, exists_decomposition_picardFunctor_isMonHom, exists_decomposition_picardTranslation
- `def-pd-separable-closure`: the defined notion and the faithful flatness of Spec k_s -> Spec k had no names **Fix:** added IsSepClosure and AlgebraicGeometry.surjective_inf_flat_inf_quasiCompact_Spec_map_algebraMap
- `thm-pd-jacobian-general-field`: exists_jacobian_descent gives the base change only to the algebraic closure; the text claims J_K = Pic^0_{C_K/K} for every K/k **Fix:** added AlgebraicGeometry.nonempty_representableBy_picardFunctorDegree_baseChange
- `sk-thm-picard-descent`: claimed flatness descends (not in Lean); rank-r name missing **Fix:** see sketch_changes
- `sk-prop-picard-schemes-criterion`: wrong declaration; Lean is over Sch/S with small values **Fix:** see sketch_changes
- `sk-def-picard-f`: missing properness **Fix:** see sketch_changes
- `sk-lem-picard-zero-dictionary`: listed name is the N = f_*L / adjunction-map form, not the adjoint-section form stated **Fix:** added exists_isEffectiveCartierCenter_hilbertPresheaf_zeroLocus_adjointSection
- `sk-the-subsheaf-ff-and-its-representability--remark-1`: inverse formula and representation-through-Phi not covered **Fix:** added hilbertToPicardNormalized_invertibleDirectImageToHilbert, exists_representableBy_invertibleDirectImageToHilbert
- `sk-prop-picard-degree-decomposition`: subgroup-scheme and translation clauses not covered **Fix:** added exists_decomposition_picardFunctor_representableBy, exists_decomposition_picardFunctor_isMonHom, exists_decomposition_picardTranslation
- `def-pc-degree-line-bundle`: second Lean name IdealSheafData.IsInvertible.degree_dual_toModules_eq_one is a lemma (deg O(P)=1 for a rational point), not part of this definition **Fix:** removed it from lean (moved to lem-pc-degree-base-change, which states that fact)
- `def-pc-divisor-line-bundle`: lean listed only the invertibility theorem, not the defined object I_D^vee **Fix:** added IdealSheafData.toModules and Modules.dual (the definition) and isInvertible_toModules; text unchanged
- `def-pc-field-tower`: only the purely-inseparable characterization lemma was listed for a node defining five notions **Fix:** added the Mathlib definitions; text unchanged
- `def-sc-effective-cartier-divisor`: lean named two theorems (isInvertible_toModules; isFinite_subschemeι_comp = finiteness on curves) instead of the definition; text restricted to curves while Lean (and several users: lem-sc-ample-complement-affine, def-pc-divisor-line-bundle) are for arbitrary schemes **Fix:** lean replaced by IdealSheafData.IsInvertible; definition stated for a scheme X (ideal locally generated by a non-zero-divisor on affine neighbourhoods of every point); dropped uses def-sc-curves
- `lem-pc-ample-positive-degree`: Lean needs H^0(X,O_X)=k (GlobalSectionsBijective) and is for smooth relative dim 1 + proper; text had 'smooth projective curve' (integral, H^0 possibly a bigger field) **Fix:** hypotheses now: smooth of relative dimension 1, proper, H^0(X,O_X)=k; proof gets a preliminaries paragraph (connected+regular => integral) and the (<=) direction now uses flat base change H^0(X_kbar)=kbar instead of lem-pc-h0-proper-variety / prop-pc-xk-integral; uses adjusted
- `lem-pc-degree-base-change`: text: proper curve of dim <=1 for all parts; Lean (2) needs X smooth of relative dimension 1 and states chi(L⊗O(D)) = chi(L) + dim Γ(O_D), deg O(D) = dim Γ(O_D), and general additivity deg(L⊗M)=deg L+deg M; (1) holds for any proper X **Fix:** (1) for proper X; (2) under 'X smooth of relative dimension 1', now states additivity for all invertible L,M, the effective-divisor formulas in the Lean form (with the old chi(L⊗M)=deg L+chi(M) kept as consequence), rational points n_i>=0, and deg(L'⊗M_K)=deg L'+deg M on X_K; proof rewritten (effective case via M|_D on finite D, general case via M ≅ O(D1)⊗O(D2)^-1); uses adjusted (dropped def-sc-divisor, def-pc-dimension, lem-pc-finite-support-hi, lem-pc-divisor-line-bundle-agrees-sc)
- `lem-pc-divisor-line-bundle-agrees-sc`: text claimed a canonical isomorphism of the subsheaf O_C(D) ⊂ k(C) with I_D^vee; Lean only proves equality of classes in Pic(C) (k(C) constant sheaf not available), for C smooth of rel. dim 1 over any field (integral Noetherian for part 2) **Fix:** statement now: (1) effective E: class [O_C(E)] of def-sc-divisor = class of I_E^vee; (2) on integral Noetherian C every effective Cartier divisor is such an E with n_P = ord_P; proof rewritten accordingly; uses + lem-sc-cartier-divisor-points
- `lem-pc-euler-additive`: second statement (Leray formula chi(Y,G)=Σ(-1)^i chi(X,R^if_*G)) is not in Lean; no user cites it **Fix:** removed the Leray part and its proof; added the two finiteness declarations that supply the hypotheses of eulerChar_eq_add_of_shortExact
- `lem-pc-euler-characteristic-well-defined`: finite-dimensionality of each H^i was not covered by the listed names **Fix:** added Modules.finiteDimensional_H_of_isProper
- `lem-pc-genus-base-change`: Lean is for any quasi-compact quasi-separated X over k; text assumed smooth projective geometrically irreducible with H^0=k plus an odd separably-closed clause **Fix:** statement generalised to qcqs X (dim H^1(O) invariant), smooth projective curve as 'in particular'; proof is flat base change; dropped uses def-sc-curves, lem-pc-proper-base-change
- `lem-pc-h0-proper-variety`: listed declaration only gives 'H^0 is a field'; finiteness over k and part (2) were missing **Fix:** added the two declarations (named in the Lean docstring); text unchanged
- `lem-pc-very-ample-descends`: Lean requires X proper over k; text said finite type **Fix:** hypothesis changed to 'X proper over k' (only user lem-pc-ample-positive-degree has proper X)
- `lem-sc-cartier-divisor-points`: Lean: any field k, C Noetherian integral smooth of rel. dim 1, conclusion I_D = ∏ I_P^{n_P}; text: smooth connected curve over (algebraically closed) k, stalk form only **Fix:** hypotheses now Noetherian integral smooth rel. dim 1 over a field; added the equivalent form I_D = ∏ I_{P_i}^{n_i}; proof no longer uses algebraic closedness; dropped uses def-sc-curves
- `lem-sc-flat-base-change-coherent`: listed declaration is only for field extensions K/k, but the text (and user lem-pc-structure-pushforward) uses an arbitrary flat k-algebra; Lean is for qcqs X, text for proper X **Fix:** added nonempty_H_baseChange_linearEquiv (arbitrary flat affine base change); statement generalised to quasi-compact quasi-separated X; proof: separated case by Čech, general case by Mayer–Vietoris induction (Stacks 02KH)
- `lem-sc-negative-degree-no-sections`: text (proper smooth curve over alg. closed k, possibly disconnected) is false without connectedness (Lean docstring: P^1 ⊔ P^1); Lean: any field, smooth rel. dim 1, proper, H^0=k **Fix:** hypotheses changed to Lean's; proof rewritten via the zero scheme of a section and deg O(D)=dim Γ(O_D) ≥ 0 (lem-pc-degree-base-change(2)) instead of rational sections / lem-sc-deg-principal-zero
- `lem-sc-riemann-roch`: lean listed eulerChar_free_eq (free sheaves only) although coherent RR exists in RiemannRochCoherent.lean; Lean works over any field with H^0(C,O_C)=k, text assumed k algebraically closed and C connected **Fix:** lean replaced by the coherent RR declarations; hypotheses now: smooth rel. dim 1, proper, H^0=k, g=dim H^1(O); part (1) now has an honest proof (deg is the χ-degree, χ(O)=1-g) instead of 'recorded classical input'; residue fields finite over k in the torsion step; additivity of deg via lem-pc-degree-base-change(2)
- `sk-thm-picard-rr`: lean list (eulerChar_free_eq etc.) missed duality, canonical degree, divisor-degree identification and coherent RR; 'these identifications commute with field extension' is not in Lean (no base change of Ω¹ or of the trace); Lean hypotheses are smooth proper + H^0=k **Fix:** see sketch_changes
- `lem-sc-finite-duality`: Lean needs the extra hypothesis that f is generically separable (stalk maps at generic points formally unramified); without it the statement is false, because the trace of differentials vanishes for an inseparable f. Lean also works over any field with C smooth of relative dimension 1 (not necessarily connected, k not necessarily algebraically closed), and also gives the sheaf-level isomorphism via a trace tau, natural in M. **Fix:** Statement rewritten: k any field, C smooth of relative dimension 1 over k, f finite flat over k and generically separable, sheaf-level iso phi -> tau o f_*phi and the global iso natural in M, plus a sentence that separability cannot be dropped. Proof adjusted: generic points xi of C, separability taken from the hypothesis, tau glued from traces, extension from O_C to M.
- `thm-sc-p1-duality`: The text assumed k algebraically closed; Lean works over any field and gives isomorphisms natural in G. **Fix:** Changed to 'Let k be a field' and added 'natural in G'. The proof uses no algebraic closedness.
- `lem-sc-rational-function-morphism`: Lean: any field k, X integral, smooth of relative dimension 1 and proper, t transcendental over k. Text: proper smooth connected curve with f not in k (only equivalent when k is algebraically closed). **Fix:** Hypotheses rewritten to follow Lean (integral, smooth of relative dimension one, proper over a field, f transcendental; for algebraically closed k this is f not in k). Added that at the generic point the morphism is [1:f]. The proof is unchanged and valid.
- `lem-sc-morphism-from-function`: Same hypothesis mismatch as lem-sc-rational-function-morphism. **Fix:** Hypotheses rewritten the same way. The surjectivity step of the proof now uses transcendence (a closed point has a residue field algebraic over k).
- `lem-sc-four-lemma`: The text required the rows to end in '-> 0'; Lean does not need X5->X6 or Y5->Y6 to be surjective. **Fix:** Dropped the trailing '-> 0' and noted that no surjectivity is needed. The proof never used it.
- `lem-sc-dim0-finite`: Lean is stated for Noetherian T0 spaces; the text only covered finite type k-schemes. **Fix:** Statement generalised to Noetherian T0 spaces, with finite type schemes over a field given as the example. Proof replaced by the topological argument (points closed via T0 and dim <= 0; irreducible components are points; finitely many).
- `lem-sc-smooth-regular`: Lean covers any scheme smooth over a field; the text only covered smooth curves. **Fix:** Statement generalised to a scheme X smooth over k (a smooth curve given as the example); the proof was renamed C -> X.
- `lem-sc-invertible-dual`: Lean covers any scheme; the text said 'C a curve'. **Fix:** Statement generalised to any scheme X (a curve given as the example). The proof is unchanged and local.
- `lem-sc-point-cartier`: Lean only needs C smooth of relative dimension 1 over a field; it does not need connectedness. **Fix:** Hypothesis changed to 'scheme smooth of relative dimension one over a field k (for instance a smooth connected curve)'. The proof is unchanged.
- `lem-pc-cech-resolution`: Lean uses the ordered Čech complex (products over all tuples I^{p+1}), not the alternating one. It computes the higher direct images R^q f_* (and Γ(S,R^qf_*) on global sections), not a derived object Rf_*. **Fix:** Statement now uses the ordered Čech complex, says exactness holds for any O_X-module, and says that for quasi-coherent F, applying f_* computes R^q f_* F, with the global-sections form H^q(Č(U,F)) = Γ(S,R^qf_*F). Proof: indices renamed to tuples, 'finite resolution' replaced by 'resolution by f_*-acyclics', global-sections step added.
- `lem-pc-flat-base-change-cohom`: Lean only has the affine form H^i(X,F)⊗_A B ≅ H^i(X',F') (S, S' affine, g flat, f qcqs) and the dimension equality over a field extension. The sheaf form g^*R^if_*F ≅ R^if'_*F' for arbitrary S, S' has no Lean counterpart. **Fix:** Statement restricted to affine S, S' (B-linear iso), with the field-extension dimension formula added. Proof: the sheaf-statement part removed, a two-line proof of the dimension formula added, and uses lem-pc-finite-support-hi and lem-pc-affine-vanishing dropped.
- `def-pc-derived-pullback`: Lean defines Lg^* as the left derived functor of termwise pullback. The text gave an 'explicit' K-flat formula through def-weil-derived-tensor, which is the pro-étale derived tensor and the wrong context. **Fix:** Now defined as the total left derived functor of g^* with its comparison map Lg^*E → g^*E. def-weil-derived-tensor removed from uses.
- `lem-pc-flat-complex-derived-pullback`: Content matched Lean, but the statement ('g^*E → Lg^*E is a quasi-isomorphism') and the proof relied on the old K-flat formula and on def-weil-derived-tensor. **Fix:** Statement now says the canonical map Lg^*E → g^*E is an iso in D(O_T). Proof redone via the derived-functor property: bounded-above acyclic flat complexes stay acyclic under g^*. def-weil-derived-tensor removed from uses.
- `lem-pc-rf-base-change-flat-module`: Lean works over affine S = Spec A and affine T = Spec B, with Rf_* represented by the Čech complex and Lg^* by B⊗K for the bounded flat truncation K. The text claimed a global iso for arbitrary S, T and f quasi-compact separated. **Fix:** Statement rewritten for affine S and T, describing the Čech/truncation model and the comparison map. Proof rewritten: homotopy equivalence with the alternating complex gives split exactness in degrees ≥ |I|-1, so K is flat and the truncation stays a quasi-isomorphism after ⊗B.
- `lem-pc-projective-noetherian-rf-perfect`: Lean: S affine Noetherian, f = closed immersion into P^n_S followed by projection, perfectness of the Čech complex in D(A). Text: S locally Noetherian, perfectness in D(O_S). **Fix:** Statement restricted to S = Spec A Noetherian, with Rf_*G represented by the Čech complex and perfect in D(A). Proof uses the bounded flat truncation from lem-pc-rf-base-change-flat-module, which is added to uses.
- `cor-pc-projective-noetherian-rf-perfect-base-change`: Lean: S affine Noetherian, T = Spec B affine and arbitrary. Text: S locally Noetherian, T arbitrary. **Fix:** Statement restricted to affine S (Noetherian) and affine T, with isomorphism and perfectness in D(B). Proof adjusted.
- `lem-pc-rf-perfect-base-change`: Lean (S affine) gives three things: (i) a local bounded finite free complex P on V ∋ t computing R^qf'_* after every base change T' → V; (ii) the Čech base-change iso for affine T; (iii) Čech perfectness in D(A) and D(B) only when A is Noetherian. Its docstring says non-Noetherian perfectness in D(A) is NOT deduced. The text claimed global perfectness in D(O_S) and a derived base-change iso for arbitrary T. **Fix:** Statement rewritten as the three clauses over affine S. Proof: (2) from lem-pc-rf-base-change-flat-module; (3) via lem-pc-coherent-hi + lem-pc-noetherian-flat-complex-perfect + the corollary; (1) is the classical input (Stacks 0B91/0A1H). Uses updated: +cor-pc-projective-noetherian-rf-perfect-base-change, lem-pc-cech-resolution, lem-pc-coherent-hi, lem-pc-noetherian-flat-complex-perfect.
- `thm-pc-semicontinuity-base-change`: Lean proves 'R^qf_*F finite locally free' over a reduced base without Noetherian hypotheses. It proves bijectivity of φ^q(t) only over a reduced locally Noetherian (affine) base, under the hypothesis that β^q is constant on the generizations of t. The text claimed φ^q(t) iso for every t over any reduced base. q is a natural number in Lean. **Fix:** (3) is now only the locally-free statement. New (4): T reduced and locally Noetherian, β^q constant on generizations of t ⇒ φ^q(t) iso. 'integer q ≥ 0'. Proof: local model now taken from lem-pc-rf-perfect-base-change(1); (1) describes φ via Čech complexes; the iso part moved to a new (4) argument (perfect Čech model over a Noetherian affine, localize at t, ranks constant on Spec A_p, normal form). Uses +lem-pc-cech-resolution, lem-pc-rf-base-change-flat-module. Missing Lean names added.
- `lem-pc-sepclosed-finite-sep-trivial`: Lean covers every separable (algebraic) extension; the text only covered finite ones. **Fix:** Statement generalised to every separable extension; proof done elementwise via minimal polynomials.
- `lem-pc-kbar-pure-insep`: Lean: exponential characteristic p (char 0 included) and any algebraic K/k. Text: char p and K = k̄ only. **Fix:** Statement generalised (exponential characteristic, any algebraic K/k, e.g. k̄). Proof: char-0 case added, letters renamed (E = k(α)), last step via lem-pc-sepclosed-finite-sep-trivial.
- `lem-sc-finite-duality`: Lean needs the extra hypothesis that f is generically separable (stalk maps at generic points formally unramified); without it the statement is false, because the trace of differentials vanishes for an inseparable f. Lean also works over any field with C smooth of relative dimension 1 (not necessarily connected, k not necessarily algebraically closed), and also gives the sheaf-level isomorphism via a trace tau, natural in M. **Fix:** Statement rewritten: k any field, C smooth of relative dimension 1 over k, f finite flat over k and generically separable, sheaf-level iso phi -> tau o f_*phi and the global iso natural in M, plus a sentence that separability cannot be dropped. Proof adjusted: generic points xi of C, separability taken from the hypothesis, tau glued from traces, extension from O_C to M.
- `thm-sc-p1-duality`: The text assumed k algebraically closed; Lean works over any field and gives isomorphisms natural in G. **Fix:** Changed to 'Let k be a field' and added 'natural in G'. The proof uses no algebraic closedness.
- `lem-sc-rational-function-morphism`: Lean: any field k, X integral, smooth of relative dimension 1 and proper, t transcendental over k. Text: proper smooth connected curve with f not in k (only equivalent when k is algebraically closed). **Fix:** Hypotheses rewritten to follow Lean (integral, smooth of relative dimension one, proper over a field, f transcendental; for algebraically closed k this is f not in k). Added that at the generic point the morphism is [1:f]. The proof is unchanged and valid.
- `lem-sc-morphism-from-function`: Same hypothesis mismatch as lem-sc-rational-function-morphism. **Fix:** Hypotheses rewritten the same way. The surjectivity step of the proof now uses transcendence (a closed point has a residue field algebraic over k).
- `lem-sc-four-lemma`: The text required the rows to end in '-> 0'; Lean does not need X5->X6 or Y5->Y6 to be surjective. **Fix:** Dropped the trailing '-> 0' and noted that no surjectivity is needed. The proof never used it.
- `lem-sc-dim0-finite`: Lean is stated for Noetherian T0 spaces; the text only covered finite type k-schemes. **Fix:** Statement generalised to Noetherian T0 spaces, with finite type schemes over a field given as the example. Proof replaced by the topological argument (points closed via T0 and dim <= 0; irreducible components are points; finitely many).
- `lem-sc-smooth-regular`: Lean covers any scheme smooth over a field; the text only covered smooth curves. **Fix:** Statement generalised to a scheme X smooth over k (a smooth curve given as the example); the proof was renamed C -> X.
- `lem-sc-invertible-dual`: Lean covers any scheme; the text said 'C a curve'. **Fix:** Statement generalised to any scheme X (a curve given as the example). The proof is unchanged and local.
- `lem-sc-point-cartier`: Lean only needs C smooth of relative dimension 1 over a field; it does not need connectedness. **Fix:** Hypothesis changed to 'scheme smooth of relative dimension one over a field k (for instance a smooth connected curve)'. The proof is unchanged.
- `sk-thm-picard-semicon`: The sketch claimed that the base-change maps are isomorphisms over every reduced base where the fibre dimension is locally constant. Lean proves this only over a reduced locally Noetherian base. It also listed only the semicontinuity declaration. **Fix:** Minimal text edit (iso clause now needs 'T moreover locally Noetherian') and Lean names added. See sketch_changes.

## Lean names added to nodes that had none

- `lem-pc-cech-exact`: `Module.FaithfullyFlat.exact_amitsurComplex`, `Algebra.TensorProduct.amitsurComplex`, `Algebra.TensorProduct.amitsurAugmentation`
- `def-pc-derived-category`: `AlgebraicGeometry.schemeDerivedCategory`, `AlgebraicGeometry.schemeDerivedQCohProperty`, `AlgebraicGeometry.schemeDerivedQCohCategory`
- `lem-pc-pic-presheaf-functorial`: `AlgebraicGeometry.picardPresheaf`, `AlgebraicGeometry.Scheme.Pic.map`, `AlgebraicGeometry.Scheme.Pic.map_id`, `AlgebraicGeometry.Scheme.Pic.map_comp`
- `lem-pc-genus-agrees-sc`: `AlgebraicGeometry.Scheme.genus_eq_arithmeticGenus`, `AlgebraicGeometry.Scheme.arithmeticGenus`, `AlgebraicGeometry.Scheme.Hom.genus`
- `det-picard-pic-split-pairs`: `AlgebraicGeometry.Scheme.Modules.eq_of_pullback_map_eq`, `AlgebraicGeometry.surjective_appTop_of_isIso_pushforwardUnitMap`, `AlgebraicGeometry.bijective_toPicardFunctor_picardFunctorNormalized`
- `lem-pc-flat-compose`: `AlgebraicGeometry.Flat.comp`
- `det-picard-f-representable-chart`: `AlgebraicGeometry.exists_representableBy_invertibleDirectImageToHilbert`, `AlgebraicGeometry.zeroLocus_adjointSection_eq_of_iso`, `AlgebraicGeometry.hilbertToPicardNormalized_invertibleDirectImageToHilbert`, `AlgebraicGeometry.hilbertPresheaf_curve_representable`
- `det-picard-main-degree`: `AlgebraicGeometry.exists_decomposition_picardFunctor`, `AlgebraicGeometry.isLocallyConstant_picardDegree`, `AlgebraicGeometry.exists_picardDegree_equiv_picardFunctorDegree`, `AlgebraicGeometry.exists_decomposition_picardFunctor_isMonHom`, `AlgebraicGeometry.exists_iso_representableBy_picardFunctorDegree_zero`
- `det-picard-main-geometry`: `AlgebraicGeometry.smoothOfRelativeDimension_of_representableBy_picardFunctor`, `AlgebraicGeometry.GrpObj.isSeparated_hom`, `AlgebraicGeometry.abelMapPresheaf`, `AlgebraicGeometry.exists_surjective_of_representableBy_picardFunctorDegree_genus`, `AlgebraicGeometry.theorem_of_the_base`
- `det-picard-main-jacobian`: `AlgebraicGeometry.exists_jacobian`, `AlgebraicGeometry.nonempty_tangentSpaceAt_linearEquiv_H_one`, `AlgebraicGeometry.nonempty_picardFunctor_iso_of_isPullback`, `AlgebraicGeometry.nonempty_representableBy_picardFunctorDegree_baseChange`, `AlgebraicGeometry.exists_jacobian_baseChange`
- `sk-cor-picard-degree`: `AlgebraicGeometry.Scheme.picDegreeHom`, `AlgebraicGeometry.Scheme.surjective_picDegreeHom`, `AlgebraicGeometry.Scheme.coe_ker_picDegreeHom`, `AlgebraicGeometry.Scheme.exists_mulEquiv_prod_ker_picDegreeHom`, `AlgebraicGeometry.exists_jacobian`
- `sk-cor-jacobian-torsion`: `AlgebraicGeometry.Scheme.Hom.pic_proper_ntorsion`, `AlgebraicGeometry.nonempty_addEquiv_torsionBy`, `AlgebraicGeometry.bijective_toUnit_comp_torsionSubgroupScheme`, `AlgebraicGeometry.jacobian_compatibility`, `AlgebraicGeometry.Scheme.surjective_pow_picardZero`, `AlgebraicGeometry.Scheme.ker_picDegreeMod`
- `det-cor-jacobian-torsion-kernel`: `AlgebraicGeometry.etale_torsionSubgroupScheme`, `AlgebraicGeometry.finrankΓ_torsionSubgroupScheme`, `AlgebraicGeometry.IsAbelianVariety.exists_overIso_sigma_torsionSubgroupScheme`, `AlgebraicGeometry.torsionByEquiv`, `AlgebraicGeometry.nonempty_addEquiv_torsionBy`, `AlgebraicGeometry.bijective_toUnit_comp_torsionSubgroupScheme`, `AlgebraicGeometry.jacobian_compatibility`
- `det-cor-jacobian-torsion-pic`: `AlgebraicGeometry.surjective_npow_points`, `AlgebraicGeometry.Scheme.surjective_pow_picardZero`, `AlgebraicGeometry.Scheme.ker_picDegreeMod`, `AlgebraicGeometry.Scheme.Hom.pic_proper_ntorsion_coker`
- `det-cor-jacobian-torsion-structure`: `AlgebraicGeometry.nonempty_addEquiv_torsionBy`, `AlgebraicGeometry.Scheme.Hom.pic_proper_ntorsion_torsion`
- `def-pc-zariski-sheaf-property`: `CategoryTheory.Presheaf.IsSheaf`, `AlgebraicGeometry.Scheme.zariskiTopology`, `CategoryTheory.GrothendieckTopology.over`
- `lem-pc-closed-imm-base-change`: `AlgebraicGeometry.closedSubscheme_baseChange_ideal_image`, `AlgebraicGeometry.flat_module_pullback_exact_pushforward_injective`, `AlgebraicGeometry.Flat.of_field`
- `lem-sc-canonical-degree`: `AlgebraicGeometry.Scheme.degree_relativeDifferentials`, `AlgebraicGeometry.Scheme.finrankH_relativeDifferentials_zero_eq_arithmeticGenus`, `AlgebraicGeometry.Scheme.serreDuality`, `AlgebraicGeometry.Scheme.Hom.isInvertible_relativeDifferentials`
- `lem-sc-line-bundle-rational-section`: `AlgebraicGeometry.Scheme.Modules.exists_nonempty_iso_dual_toModules_idealSheaf_tensorObj`
- `lem-sc-riemann-roch-large-degree`: `AlgebraicGeometry.Scheme.Modules.finrankH_one_eq_zero_of_degree`, `AlgebraicGeometry.Scheme.finrankH_zero_eq`
- `lem-sc-regular-local-domain`: `IsRegularLocalRing.isDomain`
- `def-weil-size-convention`: `AlgebraicGeometry.ProEtale.ModuleDerivedCategory`
- `lem-sc-regular-local-domain`: `IsRegularLocalRing.isDomain`

## Duplicate candidates (not deleted)

- `det-picard-rr-duality` -> keep `lem-sc-riemann-roch-large-degree`: nobody uses it; after alignment its (1) is thm-sc-serre-duality-curve, (2) is lem-sc-canonical-degree, (3) is lem-sc-riemann-roch-large-degree (deg>2g-2 ⟺ deg≥2g-1), (4) is lem-pc-proper-base-change/lem-pc-genus-base-change/lem-pc-degree-base-change(1)/prop-pc-xk-integral; it also shares its Lean names with those nodes. (Also aligned in place: hypotheses H^0=k, (4) restricted to what Lean has; Lean list added.)
- `lem-pc-genus-well-defined` -> keep `lem-pc-euler-characteristic-well-defined`: after aligning to Lean (Modules.finiteDimensional_H: H^q of an invertible module on a proper scheme is finite-dimensional) it is the invertible special case of lem-pc-euler-characteristic-well-defined (coherent modules); its only remaining citer is the remark rem-ptr-pc-genus-15

## Nodes without a Lean counterpart (not deleted)


## Sketch-level changes

- `sk-def-groth-ss`: lean list extended with SpectralSequence.pageInfinity and the double-complex abutment declarations (HomologicalComplex₂.columnFiltration, firstSpectralSequenceAbutment(_filtration), flipFirstSpectralSequenceAbutment(_filtration)) for the second half of the text; text unchanged
- `sk-thm-picard-cech`: added 'essentially small' to the site hypothesis (Lean requires EssentiallySmall C)
- `sk-thm-groth-ss`: lean list extended with CategoryTheory.Adjunction.isAcyclicComposablePair (acyclicity of (f_*,h_*)) and AlgebraicGeometry.Scheme.Modules.exists_leraySpectralSequence (Zariski O-module Leray sequence); text unchanged
- `sk-thm-picard-pn`: lean list extended with ProjectiveSpace.nonempty_H_zero_twist_linearEquiv_of_card_eq_one (n=0 clause) and ProjectiveSpace.canonicalModuleIsoTwist (omega = O(-n-1)); text unchanged
- `sk-thm-picard-coherence`: (a) rewritten: 'Rf_*F is perfect, represented by a finite free complex whose formation commutes with base change' -> 'locally a bounded finite free complex P with H^q(g^*P) = R^q f'_* F' for every base change g'; 'd_U bounds the fibre dimensions' -> 'for some d_U'; lean list now exists_isFiniteFreeComplex_higherDirectImage, isQuasicoherent_higherDirectImage, isFinitePresentation_higherDirectImage, exists_isZero_higherDirectImage_restrict, exists_isZero_higherDirectImage. Proof unchanged (it proves the stronger form)
- `sk-thm-picard-perfect`: Statement: replaced 'locally represented by a bounded complex ... derived pullback canonically Rf_{T',*}L_{T'}' with the local finite free model (H^q(a^*P) ≅ R^q f_{T',*}L_{T'}); replaced 'formation commutes with arbitrary base change' with 'f_{T',*}L_{T'} ≅ a^*f_{T,*}L for a landing in the locus'; replaced the Noetherian-approximation paragraph with 'the same holds for arbitrary T: the general form needs no Noetherian hypothesis'; general form: i ≥ 0 (was i ∈ Z), local description by higher direct images, 'base-change maps of sk-thm-picard-semicon are isomorphisms' replaced by 'R^if'_*F' ≅ g^*R^if_*F for g landing in U_{i,r}', factorisation criterion spelled out. Proof rewritten accordingly; 'Blueprint 50' provenance dropped; detailed forms now linked.
- `sk-thm-picard-semicon`: Statement: the canonical base-change maps are now said to be defined through Čech complexes over an affine open neighbourhood of t. Proof rewritten along Lean (see misaligned_fixed). Added sketch edge sk-thm-picard-semicon -> sk-thm-picard-coherence in the proof file's uses (the proof already cited it in text).
- `sec-picard-framework (_section.md summary)`: Semicon bullet: the base-change isomorphism is now claimed only over a reduced locally Noetherian base. Strand B: F is now described as the line bundles L with Rf_*L an invertible module in degree 0 (was ≅ O[0]).
- `sk-prop-picard-pic-split`: lean list extended: range_pic_mapHom_snd_eq_ker_toPicardFunctorHom, picMulEquivProdPicardFunctorNormalized (normalization formula / splitting), isIso_picardFunctorNormalized_ι_comp_toPicardFunctor (Pic_σ ≅ Pic), Scheme.Modules.eq_of_pullback_map_eq (pairs have no automorphisms), isIso_pushforwardUnitMap_pullback_snd_of_geometricallyIntegral (curve case of (∗)); text unchanged
- `sk-thm-picard-perfect`: lean list extended: exists_isFiniteFreeComplex_higherDirectImage, nonempty_higherDirectImage_iso_pullback_of_isPullback, exists_opens_range_subset_iff_isFiniteLocallyFreeInDegree; text unchanged (see misaligned_reported)
- `sk-thm-picard-hilb-curves`: lean list: added isIso_of_representableBy_hilbertPresheaf_zero (H_0 = Spec k); text unchanged
- `sk-thm-picard-f-representable`: text: 'Assume that C(k) contains a point P' -> 'Assume that k is separably closed and that C(k) contains a point P' (Lean isRepresentable_picardFunctorInvertibleDirectImage needs IsSepClosed k); lean list extended by exists_representableBy_invertibleDirectImageToHilbert and hilbertPresheaf_curve_representable
- `sk-thm-picard-main`: lean list extended: theorem_of_the_base, smoothOfRelativeDimension_of_representableBy_picardFunctor, nonempty_tangentSpaceAt_linearEquiv_H_one, exists_jacobian_baseChange; text unchanged
- `sk-cor-picard-degree`: lean field added (see lean_added); text unchanged
- `sk-cor-jacobian-torsion`: lean field added (see lean_added); text unchanged
- `sk-thm-picard-descent`: (D1): removed 'flatness' from the properties preserved/reflected; added AlgebraicGeometry.isFiniteLocallyFreeOfRank_of_toDescentData_iso to lean; proof sentence reworded (flatness/f.p. descend along faithfully flat maps)
- `sk-prop-picard-schemes-criterion`: G now a Zariski sheaf on (Sch/S) with small values; lean Scheme.LocalRepresentability.isRepresentable -> AlgebraicGeometry.isRepresentable_of_isSheaf_of_zariskiCovers
- `sk-def-picard-f`: X now a proper k-scheme
- `sk-lem-picard-zero-dictionary`: lean += exists_isEffectiveCartierCenter_hilbertPresheaf_zeroLocus_adjointSection (text unchanged)
- `sk-the-subsheaf-ff-and-its-representability--remark-1`: lean += hilbertToPicardNormalized_invertibleDirectImageToHilbert, exists_representableBy_invertibleDirectImageToHilbert (text unchanged)
- `sk-prop-picard-degree-decomposition`: lean += exists_decomposition_picardFunctor_representableBy, exists_decomposition_picardFunctor_isMonHom, exists_decomposition_picardTranslation (text unchanged)
- `sk-cor-picard-hilb-sheaf`: lean += isSheaf_zariskiTopology_hilbertPresheaf for 'hence Zariski' (text unchanged)
- `sk-cor-picard-pic-sheaf`: lean += AlgebraicGeometry.picardFunctor (Pic_{X/S} is a sheaf by construction) (text unchanged)
- `sk-thm-picard-rr`: hypothesis 'smooth projective geometrically connected curve' -> 'smooth proper curve with H^0(C,O_C)=k' (parenthetical now says this is equivalent to geometric connectedness and such curves are projective, Tag 0A26)
- `sk-thm-picard-rr`: 'These identifications commute with field extension' replaced by 'The genus and the degree are invariant under extension of the ground field' (moved after the vanishing display); Lean has no base change of Ω¹ or of the trace/duality isomorphism
- `sk-thm-picard-rr`: lean list replaced: dropped eulerChar_free_eq, added eulerChar_eq_degree_add, degree_dual_toModules, degree_tensorObj, exists_tensorObj_dual_toModules_iso, serreDuality, degree_relativeDifferentials, degree_pullback, arithmeticGenus_pullback, finrankH_one_eq_zero_of_degree, eulerChar_eq_coherentDegree_add (kept eulerChar_unit_eq, finrankH_zero_eq, isAmple_of_degree_pos, isAffine_compl_of_isAmple)
- `sk-thm-picard-rr`: sketch proof: H^0=k now a hypothesis (connected+regular => integral noted); 'Field extension' paragraph now proves only invariance of χ, degree, genus and H^0=K
- `sk-thm-picard-duality`: Text unchanged (it is aligned). Added Lean names: serreDuality_residueTrace, residueTrace, residueTrace_symm_mk, residueSum_differentialsPrincipalPartsMap (the n=1 trace pairing with Tate residues and the residue theorem), Modules.cupPairing and Modules.cupH0_naturality (the pairing and its naturality), serreDuality_zero, exists_serreDuality_zero_iso_trace and subsingleton_H_and_dual_of_smoothOfRelativeDimension_zero (the case n=0 with trace Tr_{A/k}), and genus_eq_arithmeticGenus (the genus comparison). All are in the AlgebraicGeometry.Scheme namespace.
- `sk-thm-picard-semicon`: Last clause changed from '... and the base-change maps in degree q are isomorphisms' to '..., and if T is moreover locally Noetherian, the base-change maps in degree q are isomorphisms' (Lean has the iso only over a reduced Noetherian base). Lean names added: cechBaseChangeMap, exists_isFiniteLocallyFreeOfRank_higherDirectImage_of_isLocallyConstant, bijective_cechBaseChangeMap_of_forall_specializes. Proof file unchanged (it proves the stronger statement).
- `sk-prop-picard-dense-points`: Text unchanged. Lean names added: infinite_fieldPoints, denseRange_baseChangeFieldPoint, exists_baseChangeFieldPoint_notMem_support_zeroLocus (all AlgebraicGeometry.Scheme.Hom.*). 'Smooth projective curve over separably closed k' gives the geometrically-integral hypothesis of infinite_fieldPoints: smooth gives geometrically reduced, and irreducible over a separably closed field gives geometrically irreducible.
- `sk-thm-picard-duality`: Text unchanged (it is aligned). Added Lean names: serreDuality_residueTrace, residueTrace, residueTrace_symm_mk, residueSum_differentialsPrincipalPartsMap (the n=1 trace pairing with Tate residues and the residue theorem), Modules.cupPairing and Modules.cupH0_naturality (the pairing and its naturality), serreDuality_zero, exists_serreDuality_zero_iso_trace and subsingleton_H_and_dual_of_smoothOfRelativeDimension_zero (the case n=0 with trace Tr_{A/k}), and genus_eq_arithmeticGenus (the genus comparison). All are in the AlgebraicGeometry.Scheme namespace.

## Breakages outside the section (not edited)

- `sk-thm-picard-perfect` (sec-picard-framework (block sk-thm-picard-perfect)): its proof reads sk-thm-picard-coherence (a) as a derived-level base change La^*Rf_{T,*}L = Rf_{T',*}L_{T'}; (a) now only gives, per base change and per degree, an isomorphism H^q(g^*P) = R^q f'_* F' (that is all Lean has)
- `sk-thm-picard-semicon` (sec-picard-framework (block sk-thm-picard-semicon)): its proof uses (a) as a perfect complex whose formation commutes with base change via the canonical maps (Grauert's iso clause); (a) now only gives non-canonical cohomology-level isomorphisms for each base change. Semicontinuity itself still follows; the Grauert isomorphism claim does not (the Lean docstring says the same)
- `rem-pc-sc-divisor` (sec-abelian-varieties (sk-def-av-jacobian, remark)): Lives outside sec-picard-framework, so it was not edited (hard rule). It says that the invertible module of an effective Cartier divisor 'is the one of def-pc-divisor-line-bundle (lem-pc-divisor-line-bundle-agrees-sc)', but that lemma now gives only equality of classes in Pic(C). Suggested minimal fix: '...the corresponding invertible module of an effective Cartier divisor has the same class in Pic(C) as the one of [def-pc-divisor-line-bundle] ([lem-pc-divisor-line-bundle-agrees-sc])'.
- `lem-pc-vanishing-above-dim` (sec-picard-framework (sk-thm-picard-twist)): its proof applies lem-pc-ample-positive-degree to a smooth proper curve without H^0(X,O_X)=k; the lemma now (following Lean isAmple_iff_degree_pos) requires H^0=k
- `lem-sc-divisor-class-curve` (sec-curve-estimates (sk-def-pic)): proof cites lem-sc-line-bundle-rational-section for 'every invertible module is O_C(D) with D=div(s) for a rational section s'; the lemma now states L ≅ O_C(E1)⊗O_C(-E2) for effective E1,E2 (surjectivity still follows via classes, but the rational-section clause is gone)
- `rem-pc-sc-divisor` (sec-abelian-varieties (remark)): says O_C(D) of an effective Cartier divisor is the module of def-sc-divisor via lem-pc-divisor-line-bundle-agrees-sc; that lemma now gives only equality of classes in Pic(C), not a canonical isomorphism of subsheaves of k(C)
- `lem-pd-degree-locally-constant` (sec-picard-framework (sk-prop-picard-degree-decomposition)): cites lem-pc-degree-base-change(2) as a 'projection formula'; (2) now requires X smooth of relative dimension 1 (true for its fibres, so probably fine) and its divisor clause needs n_i >= 0
- `lem-pc-rational-hyp` (sec-picard-framework (sk-prop-picard-pic-split)): The proof applies lem-pc-flat-base-change-cohom in its sheaf form f_{T,*}O_{X_T} = g^*f_*O_X for an arbitrary (non-affine) T. Only the affine module form remains.
- `prop-pc-xk-integral` (sec-picard-framework (sk-thm-picard-twist)): The proof cites lem-pc-flat-base-change-cohom for the sheaf iso g^*f_*O_X ≅ f_{K,*}O_{X_K}. The bases are affine (Spec K → Spec k), so it follows from the remaining module form, but the cited clause is gone. Should be rephrased as H^i(X,O)⊗_kK ≅ H^i(X_K,O).
- `lem-pc-flat-rf-open` (sec-picard-framework (sk-thm-picard-perfect)): The proof uses lem-pc-rf-perfect-base-change for global perfectness of Rf_*F in D(O_S) and Lg^*E ≅ Rf_{T,*} for arbitrary g. That lemma now only gives the local finite free model (clause 1), the affine Čech base change (2) and Noetherian perfectness (3). Should switch to clause (1).
- `lem-pd-degree-locally-constant` (sec-picard-framework (sk-prop-picard-degree-decomposition)): Same as lem-pc-flat-rf-open: relies on 'E = Rf_{T,*}L perfect and its formation commutes with arbitrary base change' from lem-pc-rf-perfect-base-change. Should use clause (1)'s local finite free model.
- `lem-pc-f-open-subfunctor` (sec-picard-framework (sk-lem-picard-f-open)): Uses lem-pc-rf-base-change-flat-module for Rf_{T',*}L_{T'} ≅ Lu^*Rf_{T,*}L with T, T' arbitrary. The lemma is now affine-only (S = Spec A, T = Spec B).
- `lem-pc-zero-scheme-recd` (sec-picard-framework (sk-lem-picard-zero-dictionary)): Uses lem-pc-rf-base-change-flat-module along Spec κ → T with T arbitrary. Now affine-only (fine after restricting to an affine nbhd of t, but the proof must say so).
- `thm-pc-f-representable` (sec-picard-framework (sk-thm-picard-f-representable)): Uses lem-pc-rf-base-change-flat-module for base change along arbitrary T' → T. Now affine-only.
- `sk-thm-picard-perfect` (sec-picard-framework (sketch _section.md)): Says that on U_{i,r} 'the base-change maps of [sk-thm-picard-semicon] are isomorphisms' with no Noetherian hypothesis. sk-thm-picard-semicon now asserts the iso only over a reduced locally Noetherian base.
- `sec-picard-framework` (sec-picard-framework (_section.md summary, line 40-44)): The summary 'over a reduced base local constancy makes R^qf_*F finite locally free with base change' should add 'with base change over a locally Noetherian base'.

## Follow-up rewrites inside the section

- `None`: Proof rewritten along Lean (range_subset_perfectLocusOfRank_iff): local finite free model P in degrees [0,d] from lem-pc-rf-perfect-base-change(1) over an affine open, lem-pc-perfect-locus for P, fibrewise identification U∩V = U_P, then globalisation over a cover of T. Removed perfectness/derived-pullback reasoning. uses: -def-pc-derived-pullback, -def-pc-perfect-complex, -lem-pc-flat-complex-derived-pullback, -thm-pc-semicontinuity-base-change; +def-pc-base-change, +def-pc-derived-direct-image.
- `None`: Proof follows Lean (GlobalSectionsBijective.of_section + isIso_pushforwardUnitMap_pullback_snd): H^0=k from the section, then lem-pc-structure-pushforward for every T. Dropped the sheaf-form flat base change. uses: -lem-pc-flat-base-change-cohom, -lem-pc-flat-field.
- `None`: Proof step (2) now uses the module form H^i(X,O)⊗_kK ≅ H^i(X_K,O) over the affine bases Spec K → Spec k (Lean GlobalSectionsBijective.pullback, arithmeticGenus_pullback via finrankH_pullback). f_{K,*}O = O_K is deduced from H^0 on the point Spec K.
- `None`: Proof rewritten along Lean (Modules.subsingleton_H_of_two_le). Reduce to an integral component, take a transcendental f ∈ k(X), use the finite π_f: X → P^1 of lem-sc-morphism-from-function, then lem-pc-affine-morphism-hi with Leray and lem-sc-p1-hi-vanishing. lem-pc-ample-positive-degree (which now needs H^0=k) is no longer used. uses replaced by def-pc-curve, def-pc-dimension, def-pc-smooth-projective-curve, def-sc-function-field, lem-pc-affine-morphism-hi, lem-sc-morphism-from-function, lem-sc-p1-hi-vanishing, lem-sc-smooth-regular, pqf-lem-leray.
- `None`: (1) now uses clause (1) of lem-pc-rf-perfect-base-change (local finite free model in degrees [0,d], over an affine open), as Lean isLocallyConstant_eulerCharFiber does. (2) now follows Lean picardPresheafDegree_mul_map_snd: on each fibre f_t^*N_t is trivial, so the fibres are isomorphic; this no longer uses lem-pc-degree-base-change(2) or Euler additivity. uses: -def-pc-perfect-complex, -lem-pc-euler-additive, -lem-pc-flat-complex-derived-pullback, -thm-pc-semicontinuity-base-change.
- `None`: Proof follows Lean (exists_opens_isInvertibleDirectImage_map_iff, IsInvertibleDirectImage.map_of_isProper). The open U of lem-pc-flat-rf-open gives the criterion; the subfunctor property follows because L ∈ F(T) forces U = T. Removed the Rf_{T',*} ≅ Lu^*Rf_{T,*} base change. uses: -lem-pc-rf-base-change-flat-module. Lean list extended with the two declarations above (both docstrings name this node).
- `None`: Fibre cohomology of L_t now comes from the subfunctor property (L_t ∈ F(κ(t))). s_t ≠ 0 is now shown on an affine V ∋ t with N|_V trivial: by lem-pc-cech-resolution the Čech complex is ≅ A[0], and lem-pc-rf-base-change-flat-module with affine bases V and Spec κ shows that the generator restricts to a basis of H^0(X_t,L_t). uses: -lem-pc-degree-zero-properties, +lem-pc-cech-resolution.
- `None`: W now comes directly from openness of F applied to L_H (lem-pc-f-open-subfunctor + def-pc-subfunctor), as in Lean exists_representableBy_invertibleDirectImageToHilbert. The twist/projection-formula detour is removed. Naturality of θ is no longer claimed via base change: ψ is natural, ψ∘θ = id, and θ∘ψ = id by lem-pc-universal-adjoint-section(3) applied to (a×id)^*L_H ≅ O(D_a)⊗f_T^*N'. uses: -lem-pc-flat-rf-open, -lem-pc-projection-formula, -lem-pc-rf-base-change-flat-module.
- `None`: Proof rewritten along Lean (isFiniteLocallyFreeOfRank_pushforward_unit, exists_ringEquiv_stalk_pushforward_tensorProduct_fiber). On an affine V = Spec A, B = Γ(f^{-1}V) is finite, flat and finitely presented, hence finite projective. X_s = Spec(B⊗κ(s)) and (f_*O)_s = B_p give the fibre isomorphism, and the rank is d by definition. The misuse of flat base change along Spec κ(s) → S is removed. uses: -lem-pc-flat-base-change-cohom.

## Notes from the per-block checks

- (pf-coh) Lean names added to already-aligned nodes (no text change): def-pc-projective-space-twist (+ProjectiveSpace.twist, isFreeGenerator_twistGenerator), def-pc-proj (+Proj.basicOpen, ProjectiveSpectrum.zeroLocus, AlgebraicGeometry.ProjectiveSpace), def-weil-abstract-derived-category (+DerivedCategory), lem-pc-coherent-hi / lem-pc-finite-support-hi / lem-pc-projective-coherent-higher-images (+Scheme.Modules.isQuasicoherent_higherDirectImage, needed for 'coherent' = quasi-coherent + finite presentation and for clause (1) of lem-pc-finite-support-hi).
- (pf-coh) lem-sc-cech-spectral now assumes an essentially small site; its users (sec-curve-estimates: lem-sc-ga-cohomology, lem-sc-brauer-zero-all-curves, lem-sc-etale-affine-qcoherent; sec-picard-framework: lem-sc-flat-base-change-coherent, lem-pc-flat-base-change-cohom, lem-sc-pic-tangent-space, lem-pc-cech-computes, lem-sc-p1-*) apply it to small etale or Zariski sites, which are essentially small (Lean: AlgebraicGeometry.Etale.essentiallySmall), so nothing breaks.
- (pf-coh) Possible duplicate outside the section: lem-pc-affine-vanishing (affine X) vs pqf-lem-affine-vanishing (sec-abelian-varieties, affine open U of X; Lean subsingleton_H_restrict_of_isAffineOpen) state the same fact.
- (pf-coh) Overlap outside the section: lem-sp-grothendieck-edge-maps repeats the edge-map clause of thm-sp-grothendieck (sec-abelian-varieties); sk-thm-groth-ss's Zariski Leray clause is pqf-lem-leray (sec-abelian-varieties). These are sketch/declaration layers, flagged only.
- (pf-coh) Overlap inside the section, other block: the closing sentence of def-pc-zero-scheme (local equation Spec(A/(a)), compatibility with base change, Z(s)=X iff s=0) restates lem-pc-zero-scheme-properties (block sk-lem-picard-zero-dictionary; Lean Hom.ideal_zeroLocus, Hom.comap_zeroLocus, Hom.zeroLocus_eq_bot_iff). Left untouched.
- (pf-coh) Special cases inside my blocks, not treated as duplicates (different generality, separate Lean declarations): lem-sc-p1-hi-vanishing is the case n=1, A=k of lem-pc-projective-space-cohomology-bound; lem-sc-p1-monomial (i)/(ii) is n=1, A=k of lem-pc-projective-space-twist-cohomology and (iii) of lem-pc-projective-space-canonical; lem-sc-p1-coherent-finite is a case of lem-pc-projective-space-coherent-finiteness.
- (pf-coh) sk-lem-picard-cech-computes says the isomorphism is the edge map of sk-thm-picard-cech; Lean (nonempty_cechComplex_linearEquiv_H_of_isSeparated) gives an isomorphism without identifying it with the edge map. Left as is (true, only unformalised).
- (pf-coh) lem-pc-finite-linear-avoidance: Lean also allows infinite division rings; the text keeps 'field' because its proof uses commutative polynomials.
- (pf-coh) All ProjectiveSpace declarations live on P(n; S) over an arbitrary base scheme S (pullback of Proj Z[x]); the blueprint's ring-level P^n_A = P(n; Spec A) is the special case used everywhere, so no text change.
- (pf-coh) The sketch edits in sk-thm-picard-cech and sk-thm-picard-coherence make those _section.md files differ from the tex mirror (DerivedCategoryAndSixFunctorsChoice_readable.tex §11).
- (pf-fixup) lem-pc-rf-perfect-base-change clause (1) and sk-thm-picard-coherence (a) say only 'a bounded complex P of finite free modules', but Lean exists_isFiniteFreeComplex_higherDirectImage gives P concentrated in degrees [0,d] (IsFiniteFreeComplex P d). The rewritten proofs of lem-pc-flat-rf-open and lem-pd-degree-locally-constant cite (1) for the [0,d] form: the cohomology criterion of lem-pc-perfect-locus and the Euler characteristic of P⊗κ(s) need it, since H^q(g^*P) is controlled only for q ≥ 0. The owner of those nodes should add 'concentrated in degrees [0,d]'.
- (pf-fixup) The sketch proof of sk-thm-picard-perfect gets a global isomorphism R^if'_*F' ≅ g^*R^if_*F from a derived model of Rf_*F whose derived pullback computes the R^qf'_*F' degreewise. This is Lean's route (exists_derived_model_higherDirectImage, used by nonempty_higherDirectImage_iso_pullback_of_isPullback), but no blueprint node carries that declaration.
- (pf-fixup) In-section sketch proofs owned by others that still read the old base-change form: sk-lem-picard-f-open proof ('Subfunctor property: base change of the statement ([sk-thm-picard-semicon] and the base-change comparison)'; the subfunctor property now follows from the open locus, as in lem-pc-f-open-subfunctor); sk-prop-picard-degree-decomposition proof ('complex whose formation commutes with base change to the fibres', which should cite the local model of sk-thm-picard-coherence (a)); sk-prop-jacobian-descent proof ('the perfect complex of [sk-thm-picard-semicon]'). All remain true in the per-degree form.
- (pf-fixup) lem-pc-projection-formula is no longer cited by thm-pc-f-representable; lem-pc-universal-adjoint-section still uses it.
- (pf-fixup) lem-pc-ample-positive-degree loses its user lem-pc-vanishing-above-dim. lem-pc-vanishing-above-dim now cites declarations in blocks sk-thm-picard-duality (lem-sc-morphism-from-function), sk-thm-picard-coherence (lem-sc-p1-hi-vanishing), sk-thm-picard-serre-b (lem-pc-affine-morphism-hi) and sec-abelian-varieties/sk-prop-av-pqf-finite (pqf-lem-leray). sk-thm-picard-twist/_section.md (not owned) does not declare these blocks, so the check may report undeclared edges. Block-level undeclared edges already existed, e.g. sk-lem-picard-zero-dictionary -> sk-lem-picard-f-open and -> sk-thm-picard-semicon.
- (pf-main) Every change outside a pure Lean-list extension is a generalization of the old statement, except two weakenings: lem-pc-projection-formula (now the R^q, invertible-N form) and lem-pc-tensor-dual-invertible (biduality now only 'M ≅ M^vv'). The only user of the former (thm-pc-f-representable proof) needs only the R^q form. No user outside the section was found that relies on the dropped parts.
- (pf-main) lem-pc-universal-divisor now indexes Hilb^d (previously Hilb^{d+1}) and works over any S. Its users (thm-pc-f-representable, lem-pc-universal-adjoint-section) only cite it generically.
- (pf-main) def-pc-invertible-in-degree-zero (now defined on families of cohomology modules) is cited by def-pc-f-subfunctor in sk-def-picard-f (another owner). That node's wording ('Rf_{T*}L ≅ invertible module placed in degree 0') remains consistent with the new definition.
- (pf-main) Lean lists extended on otherwise-aligned nodes: thm-pc-pic-split (+range_pic_mapHom_snd_eq_ker_toPicardFunctorHom, surjective_toPicardFunctorHom, picMulEquivProdPicardFunctorNormalized, sheafifyPicardFunctorNormalizedIso), lem-pc-divisor-line-bundle-properties (+IsInvertible.isInvertible_dual_toModules, IsInvertible.comap_of_flat, IsInvertible.nonempty_pullback_toModules_iso), and thm-sc-jacobian-representability (+exists_jacobian_baseChange, which covers its base-change clause together with Yoneda).
- (pf-main) prop-pc-xk-integral claims that X_K is projective. Lean has smoothness, properness and integrality of X_K, but no named base-change-of-projective lemma; the projectivity step is left to the proof (closed immersion into P^n base changes).
- (pf-main) sk-thm-picard-main _section body still contains the backticked node id `thm-pc-picard-representable`, a provenance-style mention. It was not touched.
- (pf-main) Possible duplicates of nodes outside the section: lem-pc-tensor-dual-invertible ~ lem-sc-invertible-dual (Lean docstring maps isInvertible_dual_and_nonempty_iso to lem-sc-invertible-dual); det-cor-jacobian-torsion-pic ~ lem-sc-pic-proper-ntorsion (sec-curve-estimates, Lean Scheme.Hom.pic_proper_ntorsion); det-cor-jacobian-torsion-structure ~ the A(k)[n] ≅ (Z/n)^{2g} node of the abelian-variety section (sk-prop-av-divisible-structure / nonempty_addEquiv_torsionBy).
- (pf-main) Possible duplicate inside the section, other owner: lem-pc-pic-presheaf-functorial ~ def-pc-picard-presheaf. Both map to AlgebraicGeometry.picardPresheaf, and functoriality is part of the definition. Kept, since the lemma has the separate functoriality text.
- (pf-main) Overlaps within my blocks that are not strict duplicates: det-picard-main-degree + det-picard-main-geometry vs thm-sc-theorem-of-the-base (separably closed, no O(dP) translation / Abel map / separatedness), and det-picard-main-jacobian vs thm-sc-jacobian-representability (tangent space vs separably closed base change). If the det layer is kept, the thm-sc nodes could be merged into them or vice versa.
- (pf-repr) lem-pc-smooth-characterization (this section) states the same as sbc-lem-smooth-criterion (sec-smooth-base-change/sk-def-smooth), up to where 'locally of finite presentation' sits; the Lean docstring of smooth_iff_flat_and_smooth_fiber names both. Candidate duplicate across sections.
- (pf-repr) lem-pd-canonical-descent-datum states that J_s 'carries a descent datum' (by def-pd-descent-datum this includes the cocycle), but its proof only constructs phi; the cocycle is lem-pd-descent-cocycle, which uses it. Not a duplicate (Lean splits it the same way: overTransport / overTransport_overTransport, bundled by overDescentDatum), but the canonical-datum statement could be weakened to 'carries a canonical isomorphism phi'. Left unchanged.
- (pf-repr) thm-pd-effective-descent: the title says 'quasi-projective' but the statement (and Lean isEffective_of_isHProjective) is for projective V->X.
- (pf-repr) Lean is more general than the text, left unchanged: def-pd-fibrewise-degree, def-pd-degree-morphism, lem-pd-degree-locally-constant (any proper flat lfp X->S instead of a curve over k); lem-pc-zero-scheme-recd and sk-lem-picard-zero-dictionary (any field, sketch says separably closed); lem-pd-group-scheme-descent (Lean only needs mult and unit compatible, text also asks for the inverse); lem-pc-degree-zero-properties (any abelian category, any object).
- (pf-repr) def-pc-subfunctor/def-pc-cover/def-pc-open-subfunctor/def-pc-zariski-sheaf-property now work over a base S; with S = Spec Z this recovers the old absolute versions, so no users break.
- (pf-repr) def-pd-degree-morphism lists lean name with the TOML escape range_picardFunctorDegree\u03b9 (= range_picardFunctorDegreeι, exists); left as is.
- (pf-rr) def-sc-effective-cartier-divisor duplicates def-nagata-invertible-ideal (sec-nagata-compactification); both now carry AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.
- (pf-rr) lem-sc-flat-base-change-coherent duplicates lem-pc-flat-base-change-cohom (sec-picard-framework, other block): same Lean names nonempty_H_baseChange_linearEquiv / nonempty_H_pullback_linearEquiv.
- (pf-rr) lem-pc-genus-base-change overlaps lem-sc-genus-invariant (sec-curve-estimates), which adds Jacobian compatibility.
- (pf-rr) def-pc-field-tower overlaps def-weil-algebraic-closure (sec-nagata-compactification) on IsAlgClosure.
- (pf-rr) lem-a1-finite-map-curve (sec-deligne-laumon-a1) applies lem-sc-riemann-roch over a finite field k_0; the generalisation to any field with H^0=k now covers that use (previously the lemma required k algebraically closed).
- (pf-rr) The Lean docstring of eulerChar_free_eq and the RiemannRoch.lean module doc still say coherent RR is 'a genuine narrowing'; RiemannRochCoherent.lean (eulerChar_eq_coherentDegree_add) now proves it, so that docstring is stale.
- (pf-rr) lem-pc-proper-base-change proof links [lem-pc-projective-proper] without a uses edge (pre-existing, left as a pointer).
- (pf-rr) Remarks rem-ptr-pc-genus-15 and rem-ptr-pc-divisor-line-bundle-4 point to ids not in their uses (def-pc-genus, lem-pc-genus-agrees-sc, lem-pc-divisor-line-bundle-properties); untouched as remarks.
- (pf-rr) Global uses-graph cycle check after the edits: no cycles.
- (pf-semicon-part-duality) thm-sc-p1-duality now holds over any field, but its proof cites lem-sc-p1-monomial (block sk-thm-picard-coherence, same section, not mine), which is still stated for an algebraically closed field. Its computation does not depend on the field, so its hypothesis should be weakened to 'a field' by the owner of that block. (thm-sc-serre-duality-curve, over any field, already relied on this.)
- (pf-semicon-part-duality) lem-sc-pullback-degree: fixed a typo in the divisor notation (sum_P n_P[P'] -> sum_{P'} n_{P'}[P']); its content was already aligned.
- (pf-semicon-part-duality) lem-sc-deg-principal-zero and lem-sc-pullback-degree: Lean uses 'integral' where the text says 'connected'. These are equivalent for smooth curves, so they were left as aligned.
- (pf-semicon-part-duality) No duplicates in this block. The remark rem-pc-closed-point-cartier-sc repeats lem-sc-point-cartier, but remarks were skipped.
- (pf-semicon) Lean-name additions on nodes classified as aligned: def-weil-pbc-proetale-site gets AlgebraicGeometry.Scheme.ProEt and AlgebraicGeometry.Scheme.ProEt.topology (Mathlib site and topology) next to ModuleDerivedCategory; its text was lightly adjusted to the universe form (U-small schemes, no 'U-bounded/skeleton'). def-pc-separably-closed gets IsSepClosed (the actual definition) and IsSepClosed.iff_forall_finrank_eq_one (the 'no nontrivial finite separable extension' equivalence) next to IsSepClosed.iff_exists_root.
- (pf-semicon) lem-pc-flf-properties (sk-the-hilbert-functor--definition-1) cites lem-pc-flat-base-change-cohom for N⊗κ(s) = Γ(X_s,O), but Spec κ(s) → S is not flat. This was a misuse before the change too.
- (pf-semicon) Possible duplicates outside the section: def-weil-pbc-proetale-site (first paragraph) vs def-weil-pbc-small-proetale-site (sec-proetale-coefficients, lean AlgebraicGeometry.Scheme.ProEt); def-pc-separably-closed vs def-kun-separably-closed (sec-proetale-coefficients, lean IsSepClosed).
- (pf-semicon) lem-pc-sepclosed-finite-sep-trivial: the title still says 'finite separable extensions are trivial'. The statement now covers all separable extensions; the title was left as is.
- (pf-semicon) def-pc-perfect-complex has uses def-sc-invertible-module, which its text does not mention (it serves the remark rem-ptr-pc-perfect-complex-9). Left untouched.
- (pf-semicon) Duality block (handled by a sub-fork): see entries above from that part.
- (pf-semicon) thm-sc-p1-duality now holds over any field, but its proof cites lem-sc-p1-monomial (block sk-thm-picard-coherence, same section, not mine), which is still stated for an algebraically closed field. Its computation does not depend on the field, so its hypothesis should be weakened to 'a field' by the owner of that block. (thm-sc-serre-duality-curve, over any field, already relied on this.)
- (pf-semicon) lem-sc-pullback-degree: fixed a typo in the divisor notation (sum_P n_P[P'] -> sum_{P'} n_{P'}[P']); its content was already aligned.
- (pf-semicon) lem-sc-deg-principal-zero and lem-sc-pullback-degree: Lean uses 'integral' where the text says 'connected'. These are equivalent for smooth curves, so they were left as aligned.
- (pf-semicon) No duplicates in this block. The remark rem-pc-closed-point-cartier-sc repeats lem-sc-point-cartier, but remarks were skipped.

# Round 2 (user decisions, 2026-10-21)

Lean reference: `slopmaster2` at a762b776d6. Blueprint check afterwards: 0 errors, 9 warnings (all pre-existing
`[bad-link]` in sec-proper-base-change/sk-thm-p1), 3271 infos (3446 before this round). Graph: no cycles, no dangling
`uses`.

## 1. Duplicate candidates: all have Lean names, so all are reported, none deleted

| Candidate | Kept/compared node | Lean name of the candidate |
|---|---|---|
| `det-picard-rr-duality` | `lem-sc-riemann-roch-large-degree` | `Scheme.serreDuality`, `finrankH_relativeDifferentials_zero_eq_arithmeticGenus`, … |
| `lem-pc-genus-well-defined` | `lem-pc-euler-characteristic-well-defined` | `Scheme.Modules.finiteDimensional_H` (the kept node uses different declarations) |
| `det-picard-pic-split-pairs` | (only its no-automorphism part is in Lean) | `Modules.eq_of_pullback_map_eq`, `surjective_appTop_of_isIso_pushforwardUnitMap`, … |
| `lem-pc-smooth-characterization` | `sbc-lem-smooth-criterion` (Smooth Base Change) | `smooth_iff_flat_and_smooth_fiber` (the other has a different declaration) |
| `lem-pc-affine-vanishing` | `pqf-lem-affine-vanishing` (Abelian Varieties) | `Modules.subsingleton_H_succ_of_isAffine` (different declaration) |
| `lem-pc-tensor-dual-invertible` | `lem-sc-invertible-dual` | `Modules.IsInvertible.dual`, `…tensorObj`, … |
| `det-cor-jacobian-torsion-pic` | `lem-sc-pic-proper-ntorsion` (Curve Estimates) | `surjective_npow_points`, `Scheme.surjective_pow_picardZero`, … |
| `def-sc-effective-cartier-divisor` | `def-nagata-invertible-ideal` (Nagata) | `IdealSheafData.IsInvertible` (same declaration on both) |
| `lem-sc-flat-base-change-coherent` | `lem-pc-flat-base-change-cohom` | `Modules.nonempty_H_baseChange_linearEquiv` (shared) |
| `lem-pc-genus-base-change` | `lem-sc-genus-invariant` (Curve Estimates) | `Scheme.arithmeticGenus_pullback` (different declaration) |
| `lem-pc-pic-presheaf-functorial` | `def-pc-picard-presheaf` | `picardPresheaf`, `Pic.map`, `Pic.map_id`, `Pic.map_comp` |

## 2. `rem-pc-sc-divisor` (remark, Abelian Varieties)
The last sentence now says that for an effective Cartier divisor, O_C(D) has the same class in Pic(C) as the
invertible module of `def-pc-divisor-line-bundle` (`lem-pc-divisor-line-bundle-agrees-sc`). It no longer says the two
modules are equal.

## 3. `lem-sc-divisor-class-curve` (Curve Estimates)
Surjectivity in the proof now uses the current `lem-sc-line-bundle-rational-section`: L ≅ I_{E1}^∨ ⊗ I_{E2}, and
`lem-pc-divisor-line-bundle-agrees-sc` identifies the class of I_E^∨ with that of O_C(E), so [L] is the image of E1 − E2.
Proof `uses`: `lem-sc-line-bundle-rational-section`, `lem-pc-divisor-line-bundle-agrees-sc`.

## 4. Derived versus per-degree base change (examples, nothing changed yet)
The round-1 statements that are now per-degree:
- `sk-thm-picard-coherence` (a): "a complex P of finite free O_U-modules in degrees [0,d_U] such that for every
  g: T'→U … H^q(g^*P) ≅ R^q f'_*F' for all q". These are separate, non-canonical isomorphisms, one for each g and each q.
  HEAD said: "Rf_*F is perfect: locally represented by a bounded complex of finite free O_T-modules whose formation
  commutes with every base change".
- `sk-thm-picard-perfect`: "H^q(a^*P) ≅ R^q f_{T',*}L_{T'} for all q and every a: T'→U" and "R^i f'_*F' ≅ g^*R^i f_*F".
  Tex `app:picard-coherent-base-change`: "the base change map La^*Rf_{T,*}L → Rf_{T',*}L_{T'} is an isomorphism in
  the derived category".
- `lem-pc-rf-perfect-base-change` (1): "isomorphisms H^q(g^*P) ≅ R^q f'_*G' for all q ≥ 0". Its clause (2) is already
  derived, but only over affine S and T.
- `thm-pc-semicontinuity-base-change`: base-change maps φ^q(t) one degree at a time.

Lean has both forms:
- **Per-degree:** `exists_isFiniteFreeComplex_higherDirectImage` and
  `nonempty_higherDirectImage_iso_pullback_of_isPullback`. Their docstrings say the isomorphisms are not the
  canonical maps.
- **Derived and canonical:** `AlgebraicGeometry.exists_isIso_canonicalModuleBaseChange_of_isFlatOver`. For f
  quasi-compact and separated and G quasi-coherent and flat over S, the canonical map Lg^*Rf_*G → Rf'_*g'^*G
  (composed with the comparison Lg'^*G → g'^*G) is an isomorphism for every cartesian square. No blueprint node
  carries it yet. Its docstring cites the missing id `lem-pc-relatively-flat-canonical-module-base-change`.

So the tex's derived form can be restored on these nodes with that declaration as the Lean counterpart.

## 5. New node `lem-pc-higher-direct-image-derived-model` (detail layer, block `sk-thm-picard-perfect`, order 689)
Lean: `Scheme.Modules.exists_derived_model_higherDirectImage`, whose docstring already cites this id. The statement
follows Lean: E ∈ D(O_T) with H^n(E) = 0 for n < 0, H^q(E) ≅ R^q f_*F, and H^q(Lg^*E) ≅ R^q f'_*(g'^*F) for every
cartesian square. The proof takes E = Rf_*F and uses the flat Čech base change of `lem-pc-rf-base-change-flat-module`.
The sketch proof of `sk-thm-picard-perfect` links it at the step that needs a global derived model. The tex does not
mention it.

## 6. `lem-pc-vanishing-above-dim`
Its proof no longer cites `lem-pc-ample-positive-degree`, which needs H^0 = k; the round-1 follow-up removed it.
Every remaining citation's hypotheses hold: integral component, transcendental f, finite π_f, affine
pushforward, Leray, and vanishing on P^1_k over any field. The block `sk-thm-picard-twist` now declares the blocks
these citations live in: `sk-thm-picard-perfect`, `sk-thm-picard-rr` and `sec-abelian-varieties`.

## 7. Descent nodes
- `lem-pd-canonical-descent-datum` now states what `RepresentableBy.overDescentDatum` proves. For any p: X→Y, any
  presheaf F on schemes over Y and any V over X representing the restriction of F, the canonical transport of points
  is a descent datum: natural, the identity on equal points, and satisfying the cocycle condition. The datum
  involves no choice. The Jacobian J_s over k_s/k is the "in particular" case. The old text claimed a full datum but
  constructed only φ.
- `lem-pd-descent-cocycle` is now the self-contained cocycle identity τ_{23}∘τ_{12} = τ_{13} for that transport
  (`overTransport_overTransport`). The dependency now runs cocycle → canonical datum, as in Lean.
- `thm-pd-effective-descent` is retitled "Effective descent for projective schemes".

## 8. Blueprint-only blocks moved into the detail layer
The 26 blueprint-only blocks (orders 714–740) are now detail nodes in the tex block that uses them. Each block
statement became a detail node that keeps its id, because Lean docstrings cite these ids. Its sketch proof became the
node's proof, its `sketch` tag was removed, and its detail nodes moved along with it. The section now has 11 sketch
blocks, one per tex declaration of Appendix C (plus the remark `sk-rem-picard-relative-scope`).

| Former block(s) | Now under |
|---|---|
| `sk-def-groth-ss`, `sk-thm-groth-ss`, `sk-thm-picard-cech`, `sk-lem-picard-affine`, `sk-lem-picard-cech-computes`, `sk-thm-picard-pn`, `sk-thm-picard-serre-a`, `sk-thm-picard-serre-b`, `sk-thm-picard-coherence`, `sk-thm-picard-semicon` | `sk-thm-picard-perfect` (coherent base change) |
| `sk-thm-picard-duality` | `sk-thm-picard-rr` |
| `sk-thm-picard-descent`, `sk-cor-picard-pic-sheaf` | `sk-def-picard-pic` |
| `sk-the-hilbert-functor--definition-1`, `sk-cor-picard-hilb-sheaf`, `sk-thm-picard-hilb-general` | `sk-thm-picard-hilb-curves` |
| `sk-def-picard-f`, `sk-lem-picard-f-open`, `sk-lem-picard-zero-dictionary`, `sk-the-subsheaf-ff-and-its-representability--remark-1`, `sk-cor-picard-degree-g` | `sk-thm-picard-f-representable` |
| `sk-prop-picard-dense-points` | `sk-thm-picard-twist` |
| `sk-prop-picard-schemes-criterion`, `sk-thm-picard-criterion`, `sk-prop-picard-degree-decomposition`, `sk-prop-picard-jacobian-tangent` | `sk-thm-picard-main` |

- **Block cycle.** The plain mapping produced one cycle among `sk-def-picard-pic`, `sk-prop-picard-pic-split`,
  `sk-thm-picard-hilb-curves`, `sk-thm-picard-f-representable` and `sk-thm-picard-main`. Six detail nodes were moved
  to their earliest user to break it:
  - `def-pc-subfunctor`, `def-pc-fppf-site`, `def-pc-representable-functor` and `lem-pc-tensor-dual-invertible` →
    `sk-def-picard-pic`;
  - `lem-pc-divisor-line-bundle-properties` → `sk-prop-picard-pic-split`;
  - `lem-pc-schemes-criterion` → `sk-thm-picard-hilb-curves`.

  The block graph is now acyclic, including the two old cycles through degree-decomposition and jacobian-tangent.
  Some forward block edges remain (e.g. `sk-thm-picard-rr` → `sk-thm-picard-perfect`, because Riemann–Roch uses the
  P^1 cohomology in the coherent block).
- **Citations of the converted wrappers.** Their block citations now point to declarations:
  - `sk-def-picard-pic` → `def-pc-picard-functor`;
  - `sk-thm-picard-rr` → `lem-sc-riemann-roch`;
  - `sk-prop-picard-pic-split` → `thm-pc-pic-split`;
  - `sk-thm-picard-main` → `thm-pc-picard-representable`;
  - `sk-def-curve` → `def-sc-curves`;
  - the `sk-def-av-*` seam citations were dropped, since the target blocks keep them.
- **Sketch-level `uses` repointed to the target block,** including three outside Picard: `sk-thm-curveestimate`
  (Curve Estimates), `sk-thm-reduction` and `sk-lem-pbc-composition-cancellation` (Proper Base Change). Missing
  block-level declarations were added to the 11 tex blocks, and `sec-nagata-compactification` was added to the
  section's `uses`.
- **Open point.** The converted nodes keep their `sk-…` ids although they are now detail nodes. Renaming them (e.g.
  `det-…`) would need the Lean docstrings that cite them to change too.

# Round 3 (user decisions, 2026-10-21)

Blueprint check afterwards: 0 errors, the 9 pre-existing warnings, 3283 infos. Graph: no cycles, no dangling `uses`.

**Derived form.** Nodes with a derived Lean counterpart are now stated in derived form:
- `sk-thm-picard-perfect`: tex wording.
- `det-thm-picard-coherence` (a): derived base change, and perfectness over a locally Noetherian base.
- `lem-pc-higher-direct-image-derived-model` (c).

The global derived base change is the new node `lem-pc-relatively-flat-canonical-module-base-change`.
`lem-pc-rf-base-change-flat-module` keeps the affine Čech form. `lem-pc-flat-base-change-cohom` is parked (no derived
Lean counterpart for flat g).

**1. Block order (option a).**
- 42 nodes moved from `sk-thm-picard-perfect` into `sk-thm-picard-rr`: the coherent cohomology that Riemann–Roch uses.
- Definitions went to their earliest user: `def-pc-picard-presheaf`, `def-pc-rational-point`, `def-pc-genus`,
  `def-pc-separably-closed`, `def-pc-finite-locally-free`, ….
- Two block cycles came out of this: `pic-split` ↔ `rr` and `f-representable` ↔ `twist`. They were removed with the
  earliest-user rule:
  - `lem-pc-genus-agrees-sc`, `lem-pc-degree-agrees-sc` and `lem-pc-divisor-line-bundle-properties` →
    `sk-thm-picard-rr`;
  - the rr lemmas needed by `lem-pc-rational-hyp` → `sk-prop-picard-pic-split`, 27 nodes in all: H^0 of proper
    varieties, finite-support and flat base change, and their Čech and projective-space dependencies;
  - `prop-pc-xk-integral`, `lem-pc-vanishing-above-dim` and `lem-pc-projective-proper` →
    `sk-thm-picard-f-representable`.
- Result: no forward edge between the Picard tex blocks, so the block order is the tex order. Block `uses` were
  recomputed: missing ones added, stale ones dropped.

**2. Renamed** the 26 converted nodes `sk-…` → `det-…`. Two names were shortened:
`det-the-hilbert-functor--definition-1` → `det-pc-hilbert-functor` and
`det-the-subsheaf-ff-and-its-representability--remark-1` → `det-pc-subsheaf-f-representable`. All references in
the blueprint were updated (66 files). Lean docstrings that cite the old `sk-…` ids now point at ids that no longer
exist, e.g. `sk-thm-picard-coherence`.

**3. Generalized to Lean** (details and proposed tex wording in `PICARD-TEX-CHANGES.md`):
- `def-pd-fibrewise-degree`, `def-pd-degree-morphism` and `lem-pd-degree-locally-constant`: any proper flat X→S
  locally of finite presentation. `lem-pd-degree-locally-constant` gained clause (4) for field-valued points.
- `det-lem-picard-zero-dictionary`: any field.
- `lem-pd-group-scheme-descent`: any faithfully flat quasi-compact base change, with only multiplication and unit
  required to be compatible.
- `lem-pc-degree-zero-properties`: any abelian category.

**4.** The tex-route differences (chart over separably closed k, Riemann–Roch hypotheses, Hilbert route, Galois
descent for the Jacobian) are recorded in `PICARD-TEX-CHANGES.md`, Part 2. They are not changed.

**5. `prop-pc-xk-integral`** now follows Lean:
- X is connected, smooth of relative dimension 1 and proper over a separably closed k; no rational point or
  projectivity is needed.
- X_K is integral, smooth and proper; there is no projectivity claim.
- Users repaired: the proof of `prop-pd-picard-degree-decomposition` and the remark `rem-pc-conventions`.
- `sk-thm-picard-hilb-curves`: "smooth projective" → "smooth proper", as in the tex and in Lean.

**6. Duplicates deleted**; edges and links moved to the survivor, and Lean names merged:

| Deleted | Kept |
|---|---|
| `det-picard-rr-duality` | `lem-sc-riemann-roch-large-degree` |
| `lem-pc-genus-well-defined` | `lem-pc-euler-characteristic-well-defined` |
| `det-picard-pic-split-pairs` | — (its Lean names were already on the rigidification block) |
| `lem-pc-pic-presheaf-functorial` | `def-pc-picard-presheaf` (functoriality sentence added) |
| `lem-sc-invertible-dual` | `lem-pc-tensor-dual-invertible` |
| `lem-sc-flat-base-change-coherent` | `lem-pc-flat-base-change-cohom` |
| `lem-pc-affine-vanishing` | `pqf-lem-affine-vanishing` (Abelian Varieties) |
| `def-sc-effective-cartier-divisor` | `def-nagata-invertible-ideal` (Nagata) |
| `sbc-lem-smooth-criterion` (Smooth Base Change) | `lem-pc-smooth-characterization` |
| `def-weil-pbc-small-proetale-site` (Pro-étale) | `def-weil-pbc-proetale-site` |
| `def-kun-separably-closed` (Pro-étale) | `def-pc-separably-closed` (separable-closure sentence added) |

Not duplicates, so kept:
- `det-cor-jacobian-torsion-pic` vs `lem-sc-pic-proper-ntorsion`: each has clauses the other lacks.
- `lem-pc-genus-base-change` vs `lem-sc-genus-invariant`: they use different notions of genus, dim H¹(O) and
  dim Γ(Ω¹).
- `def-pc-field-tower` vs `def-weil-algebraic-closure`: the field-tower node defines five notions.

**7. Missing ids cited by Lean docstrings**, added as detail nodes (the Lean repo was not changed):
- `lem-pc-relatively-flat-canonical-module-base-change`, in `sk-thm-picard-perfect`, for
  `exists_isIso_canonicalModuleBaseChange_of_isFlatOver`.
- `lem-pc-universal-finite-free-complex`, in `sk-thm-picard-perfect`, for `exists_isFiniteFreeComplex_higherDirectImage`.
  `det-thm-picard-coherence` (a) now cites it, and that declaration moved off the coherence node.

Still cited by a Lean docstring without a node: `lem-pc-base-change-map-cech`, an internal Čech step of the derived
base change.
