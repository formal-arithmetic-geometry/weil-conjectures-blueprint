# Lean names of the layer-2 clauses whose declaration is proved
On the site, 616 clauses (`<id>--<k>`) of declarations that carry Lean names had none themselves,
so they counted as *absent*: progress stood at 830 of 1719. Each of these clauses was compared with
the Lean proof of its declaration (weil-conjectures `94ce2d8`, Mathlib `0df444a`): does the proof go
through the clause, which declaration states it, or does Lean take another route?

## Result

| Verdict | Clauses | Names placed |
|---|---|---|
| the declaration's own name | 286 | 283 |
| project lemma | 124 | 103 |
| Mathlib | 9 | 9 |
| partial | 114 | 15 |
| inside a proof | 12 | 0 |
| different route | 10 | 0 |
| not formalized | 61 | 0 |
| **total** | **616** | **410** (543 names) |

- **The declaration's own name.** The clause is what one of the declaration's names states, often
  the whole declaration (a single clause) or one conjunct of a bundle. The name now sits on the
  declaration and on the clause, and a bundle's name on each clause it states. Until now no name sat
  on two nodes; the two layers are separate graphs (`scripts/lean_uses.py` draws arrows within a
  layer only and never between a declaration and its own clauses), so this changes no arrow of the
  declaration layer.
- **Project lemma / Mathlib.** A declaration stating the clause, or a more general statement it
  specialises from.
- **Partial.** Lean states a special case or a part. Names are placed only where the one missing
  hypothesis is one the declaration's own names already assume (marked `RESTRICTION-ONLY` below).
- **Inside a proof / different route / not formalized.** No name: the clause is a step of a Lean
  proof with no declaration of its own, the Lean proof does not go through it, or Lean does not
  state it.
- Names left out: auto-generated instance names, and names already on another node (listed as
  conflicts in the table).

Whether a name is proved is not decided here: the site reads it from the oleans. Several names
rest on `sorry` and will show as *stated*.

## How the Lean proofs relate to the blueprint, by chapter

The notes below are the reviewers' notes, one per group of chapters, as written. Their remarks on
`sorry` were made without a build; the site's status is what counts.

### Group 1

Verdicts: parent-name 47, partial 15, project 9, mathlib 1, not-formalized 1.

Every new name in `names`/`partial_names` was grepped against `blueprint/`. The only names already on a node are parent names; genuine conflicts with other nodes are listed in `conflicts`. The proetale package was present.

### Per parent

- **proposition-pro-etale-affines-form-basis**: follows the blueprint. `AffineProEt.isCoverDense_toProEt` (proetale) is --1 verbatim (reduce to an affine base, then `RingHom.WeaklyEtale.exists_indEtale_comp`).
- **lemma-w-contractible-affines-projective**: follows the blueprint. `proetale_weakContractible_equivalences` packages --2 (split epis ⇔ projective ⇔ surjective on sections) together with the affine case.
- **lemma-local-cohomology-right-adjoint**: follows the blueprint, but coefficients are the pulled-back condensed ring Λ. --1 is `closedSupportDerivedAdjunction`, --2 is `closedSupport_fiber`. Full faithfulness of derived i_* has no declaration of its own.
- **definition-local-cohomology**: `closedSupport` = i^*∘ker(unit of j^*⊣j_*). RΓ_Z is only `(closedSupport …).rightDerivedFunctor`.
- **lemma-reduction-derived-nakayama**: each clause is stated twice by parent names. In `isZero_of_…`/`isIso_of_…` the notion `derivedCompleteIntegers` is orthogonality-based, which makes --2 tautological. `derived_nakayama_first_reduction` uses genuine `IsDerivedComplete` and follows the blueprint's K_1 → K_{n+1} → K_n induction.
- **proposition-extension-zero-restriction-closed-subscheme**: the 10 parent names map almost one-to-one onto the clauses. Lean takes a different route throughout: every RingSheaf statement is transported from R-module sheaves through `Mod.forget`.
  - i^* preserving limits is proved over a finite affine cover whose closed fibres detect isomorphisms.
  - Exactness of j_! is transported rather than obtained from the pair (j^*, i^*) detecting exactness.
  - Products and R lim under j_! come from sheaf-level product preservation, exact products and the Milnor triangle, not from the open–closed triangle.
  - Base change comes from support on U'.
  - Gaps and additions: --6 (left exactness of j^*) is not stated, so partial. --9 is the unlisted `RingSheaf.preservesLimitsOfShape_mapDerivedCategory_openImmersionLowerShriek`.
- **lemma-stability**: follows the blueprint (WeaklyEtale = Flat ⊓ diagonal Flat). --1 and --3 are the parent's auto-named Mathlib instances. --8 is `WeaklyEtale.Spec_iff` plus `Algebra.weaklyEtale_iff`.
- **proposition-pro-etale-coverings**: `exists_finite_affine_of_mem_topology` is --1, stated more generally for qcqs objects. The statement that the disjoint union is affine and faithfully flat is not formalized.
- **proposition-etale-implications**: --2 is the scheme-level `WeaklyEtale.etale`. The ring version is an unnamed instance. Same Kähler-ideal argument as the blueprint.
- **corollary-cohomology-pro-etale-affine**: weaker and different route. Lean works one degree at a time, for abelian sheaves only, via continuity of étale cohomology (Stacks 09YQ) plus the comparison bijection. Partial.
- **corollary-bounded-below-classical-complexes**:
  - --2 is `classicalDerivedEquivalence`, but it assumes the D⁺ unit is invertible.
  - --1 (weak Serre subcategory) exists only for "étale origin" sheaves, with no link to Lean's `IsClassical*` predicates. The Lean proof does not use --1.
- **definition-repleteness / proposition-repleteness-pro-etale-topos**: each single clause equals its parent name.
- **proposition-unbounded-comparison-finite-coefficients**:
  - --1 is the parent name, valid for k finite or algebraically closed. Lean proves it via the counit on the classical image rather than the blueprint's truncation argument.
  - --2 is formalized only for bounded-below K.
- **definition-cohomological-dimension**: the definitions match; all three clauses are parent names. Field notation cd_ℓ(K) is just the definition at Spec K.
- **lemma-uniform-bounds-pro-etale-affines**: Lean's bound is 2·dim X + 1, not dim X + cd_ℓ(k), so --1 is partial.
  - --2 skips the blueprint's Čech argument and bounds each stage directly.
  - --3 is `relativeCohomologicalDimension_lt_top_of_finiteType`, which is more general.
- **lemma-cohomological-dimension-base-field**: both clauses are conjuncts of `cohomologicalDimension_baseField`. Lean goes through étale torsion cd and the comparison.
- **proposition-unbounded-functors-products**: only the Rf_* half is formalized (right adjoint ⇒ products and derived limits of towers). RΓ(U,−) for arbitrary U is missing, and unbounded Rf_* has no name. Both clauses partial.
- **proposition-weakly-contractible-hypercovers**: follows Stacks 09A1/09A2. The parent names state the clauses.
- **proposition-left-completeness**: Milnor-sequence route. The parent names state the clause.
- **proposition-continuous-cohomology-pro-etale-cohomology**: `continuousCohomology` states the clause, but **its proof is `sorry`** (ProEtaleContinuousCohomology.lean:153).
- **corollary-evaluation-weakly-contractible-objects**: follows the blueprint.
  - --2 is the parent name.
  - --4 and --6 are stated exactly by `peSectionsLimitsColimits` and `ProEt.sections_conservative`, which already sit on siblings --5 and --7 (conflicts).
  - --3 (unbounded RΓ(W,K) = K(W)) is not formalized.
- **definition-tate-twists**: the sp-family follows the blueprint's construction (finite → Kummer → integral → rational → Qbar colimit). --4 is `spFiniteKummer_existsUnique`/`spFiniteKummer`. --9 is partial: `tateTwistOne` (Qbar ⊗ ℤ_ℓ(1)) is never proved isomorphic to `spQbarTwist`.
- **lemma-comparison-completed-coefficients**: follows the blueprint clause by clause. --1 is `sfb_normalized_integral_quotient_cone` (stated for general compact rings), --2 is `completedCondensedRational`, --3 is `isColimitPadicAlgClRingObjCocone`. --4 (f^* compatibility) exists only as conjuncts.
- **proposition-pro-etale-site-separably-closed**: dense subsite plus the comparison lemma. --2 is partial: the equivalence is stated for abelian sheaves over separably closed fields, and for sets only over algebraically closed fields.
- **lemma-inverse-image-coefficient-sheaves**: follows the blueprint. --2 is `spRoots_cartesian`/`spFiniteTwists_cartesian`/`spTwists_cartesian`; --3 is `cartesianCoefficients_finiteFree`.
- **proposition-comparison-morphism-inverse-image**: --1 is the parent names `Scheme.toProEt` and `comparisonLowerStar`; the unclaimed `isContinuous_toProEt` and `representablyFlat_toProEt` could be added. For (2.6), clause --3, Lean takes a different route: ν^* is a Kan extension plus sheafification, and the colimit formula is proved by the continuity theorem `isColimit_comparisonUpperStar_mapCocone` (affine case, then gluing over an affine hypercover), not via formula (2.5).
- **definition-classical-pro-etale-sheaves**: --2 is `IsClassicalModuleComplex`; the unclaimed variants are `IsClassicalComplex` and `IsClassicalComplexFor`.
- **lemma-extremally-disconnected-covers**: Mathlib. --2 is `Profinite.presentation` (with `.π` and `.epi_π`). --3 is `Stonean.toProfinite` for the compact case; the totally-separated instance is anonymous, so it cannot be cited.
- **theorem-pro-etale-refinements-weakly-etale / proposition-gleason-s-theorem**: each single clause is identical to its parent; the parent names state it.
- **lemma-comparison-direct-images-compatibilities**: follows the blueprint (mates, the counit identity, then the unit via `Adjunction.map_unit_comp_eq_unit`).
  - --1 is partial: `comparison_unit` holds only for qcqs g.
  - --2 is partial: `fixedComparisonDirectImageMatePlus_counit` needs finite Λ and qcqs g; `ComparisonCore.comparison_counit` needs qcqs g only.
  - --3 is `comparisonDirectImagePlus_comp` (any g).
- **proposition-comparison-immersions**:
  - --2 is stated exactly by `mapDerivedCategoryOpenImmersionLowerShriekComparisonUpperStarIso`, which is already on proposition-comparison-etale-derived-category--6 (conflict).
  - --3: the isomorphisms exist only for general maps, and the triangle transport is not formalized. Partial.
  - --4 is the parent name `rightDerivedLowerShriekOfCompactificationComparisonIso`.

### Clauses best stated by Mathlib declarations

- lemma-extremally-disconnected-covers--2: `Profinite.presentation`, `Profinite.presentation.π`, `Profinite.presentation.epi_π`
- lemma-extremally-disconnected-covers--3: `Stonean.toProfinite` (parent name); the main sentence is an anonymous Mathlib instance
- proposition-gleason-s-theorem--1: `CompactT2.projective_iff_extremallyDisconnected` (parent name); also `CompHaus.Gleason`
- lemma-stability--1 and --3: Mathlib's auto-named WeaklyEtale instances (parent names)
- lemma-stability--8: `Algebra.weaklyEtale_iff` (Mathlib, generated by `mk_iff`) together with the project's `AlgebraicGeometry.WeaklyEtale.Spec_iff`
- corollary-evaluation-weakly-contractible-objects--4: partly `SheafOfModules.evaluationPreservesLimitsOfSize` (universe-limited)

### Group 2

70 clauses in 22 parents. Verdicts: parent-name 31, project 19, partial 14, mathlib 2, not-formalized 2, inline 1, different-route 1.
Sources: weil-conjectures `94ce2d8` and proetale (`.lake/packages/proetale`, present; no relevant names came from it), Mathlib `0df444a`.
None of the cited files contains `sorry` or `axiom` (file-level grep; transitive dependencies not checked; the "sorried input" note in `ConstructibleSheaf/ProEtaleModule/DerivedCategory.lean` is stale, because `CategoryTheory/ModuleObjects/GrothendieckAbelian.lean` has no `sorry`).

### Per parent

- **proposition-composition-open-restriction-compactifications-f** (--3, --6, --7, --8). Lean follows the blueprint (mates and uniqueness of right adjoints) but proves almost everything only on the étale site with finite Λ (`SixFunctors/Etale/Derived/UpperShriekLocality.lean`). For ℓ-adic coefficients, f^! is *defined* as Rg^! ⋙ i^*. --6 is the parent name `existsUnique_rightDerivedUpperShriekOfCompactificationIso`. --3 has only the left unit law (`Correspondence.upperShriekComp_id_left_hom_app`, for Q̄ℓ). For --7 and --8, Lean states the two ingredients (open restriction of f^!, and detection of isomorphisms on a covering) but no locality statement.
- **definition-localizing-subcategory**, **theorem-compactness-rational-coefficients**, **proposition-proper-base-change-localizing-categories**, **lemma-checking-isomorphisms-constructible-complexes**: each single clause repeats the parent, so the verdict is parent-name. Proper base change on Loc has no finite-coefficient version.
- **corollary-ambient-ind-derived**. Follows the blueprint. In --1, the abstract `DerivedCategory.homologyProperty_*` lemmas (triangulated, sums, truncations) are specialised by a `have` inside the parent proof. --2 is the parent name.
- **definition-ind-constructible-sheaves**: both clauses are the parent definition `IsIndConstructibleModuleObject`, which is `ObjectProperty.ind` of the constructibles.
- **proposition-ind-constructible-sheaves**. Follows the blueprint, through finite presentability of constructibles. --1 and --2 are both the parent name `indHeart_fullFaithfulness`. For --3 to --7 Lean has specific or general project lemmas: `indConstructible_filteredColimits_and_sums(_padicAlgCl)`, `ObjectProperty.ind_isClosedUnder{ColimitsOfShape_discrete,Kernels,Cokernels}`, `indConstructible_of_shortExact(_padicAlgCl)`. Grothendieck abelian (--8) is not formalized. --9 is Mathlib.
- **corollary-ind-heart-b**. Follows the blueprint. `indConstructible_ext_vanishing_and_sums` states both clauses; it is given for --1, and the general `DerivedCategory.compactFor_singleFunctor_of_homFactorsThroughFilteredColimits` for --2.
- **lemma-uniform-ext-bound**: E and Q̄ℓ clauses are the two parent theorems. The Q̄ℓ case is proved by descent from E, as in the blueprint.
- **lemma-uniform-bound-proper-direct-image** and **lemma-proper-direct-image-unbounded-complexes**: **different route**. Lean uses only *some* uniform bound d, not 2d+1, and replaces IndCons/Dic by `constructibleCoproductClosure`. It never shows that Rp_* lands in Dic. It reduces sums of unbounded complexes to bounded families by abstract dévissage plus left completeness (`DerivedCategory.isIso_sigmaComparison_of_homologyProperty`), not by the finite window (5.6). So unbounded --2 is different-route, and the amplitude and sums clauses are partial.
- **proposition-forgetting-supports-composition**. --1 is the parent names. For --2, independence is a parent name. The composition square exists only for proper p, f (`properShriekComp_compactificationForgetSupports`, which is marked auxiliary).
- **proposition-construction-independence-rf-shriek**. Follows the blueprint (refinements, common refinement). --2 to --6 are conjuncts of the parent names. Independence (--7) and the cocycle (--8) are stated only on the étale site (finite Λ) and on pro-étale Dbc for ℓ-adic Λ; there is no pro-étale finite case and nothing on Loc.
- **proposition-proper-direct-image-extension-zero**. Follows the blueprint. Conjuncts of the parent names cover --3 to --7. The finite-A clause --1 (Rp_* maps Loc into Loc) is missing. --2's natural name is already on corollary-proper-direct-image-finite-coefficients-localizing. --8: the finite case is new; the ℓ-adic name conflicts with lemma-inverse-image-tensor-product--3.
- **lemma-inverse-image-tensor-product--5** (comparison with the completed inverse image): not formalized for module objects. A separate integral/completed pullback model, `WeilConjectures.IntegralCompletedComparison.Comparison`, may be related and needs a check by someone who knows it.
- **proposition-compactness-proper-direct-image**: both clauses are the parent names.
- **lemma-structure-integral-constructible-complexes**. --1 is partial: the triangulated instance, essential smallness and the Serre property are stated, but truncation stability of pro-étale Dbc is not found. --2 is the definition `IsConstructibleModuleObject`, which conflicts with definition-constructible-sheaves. For --3, Lean has only the Tor amplitude [-1,0] (`integral_ctf_equals_bc`), not dualizability.
- **proposition-compactness-finite-coefficients**. Lean takes a different route: a finite-window argument on the pro-étale side instead of the explicit RHom formula. --1 is the parent name; its generator half (`compactlyGeneratesLocalizingClosure_...`) sits on lemma-hypotheses-brown-representability. For --2 (Loc^c = Dctf) only the abstract `compact_mem_finite_thick_of_generators` exists.
- **corollary-proper-direct-image-finite-coefficients-localizing--1**: partial. The parent name gives only the direct-sum part, for the étale-origin class; Loc to Loc is not stated.
- **lemma-hypotheses-brown-representability**. Follows the blueprint. The generic structural facts have general project names: `isLocalizing_localizingClosure`, `hasCoproducts_fullSubcategory`, `isIdempotentComplete_localizingClosure`, `essentiallySmall_constructibleFiniteTor`, `exists_skeleton_boundedConstructible`. Local smallness (--1) holds by construction. The four compact-generation clauses are the parent names.
- **theorem-existence-exceptional-inverse-image**. Follows the blueprint (Brown representability). --1 is the parent names. --2 is Mathlib `Adjunction.isTriangulated_rightAdjoint`. --3 is `Adjunction.existsUnique_iso_comp_counit`. --4 is `ObjectProperty.preservesColimitsOfShape_of_localizingClosureLift_adjunction`.

### Clauses best stated by Mathlib declarations

- proposition-ind-constructible-sheaves--9: `CategoryTheory.ObjectProperty.preservesKernels_ι`, `CategoryTheory.ObjectProperty.preservesCokernels_ι`
- theorem-existence-exceptional-inverse-image--2: `CategoryTheory.Adjunction.isTriangulated_rightAdjoint`
- Related but not assigned: `CategoryTheory.ObjectProperty.ind` (definition-ind-constructible-sheaves) and the unnamed Mathlib instance `Abelian P.FullSubcategory` (the abelian half of proposition-ind-constructible-sheaves--8).

### Conflicts reported

- proposition-proper-direct-image-extension-zero--2: `AlgebraicGeometry.ProEtale.isIso_sigmaComparison_rightDerivedLowerStar_of_etaleOriginHomology` (on corollary-proper-direct-image-finite-coefficients-localizing)
- proposition-proper-direct-image-extension-zero--8: `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_openImmersionLowerShriek_obj` (on lemma-inverse-image-tensor-product--3)
- lemma-structure-integral-constructible-complexes--2: `AlgebraicGeometry.ProEtale.IsConstructibleModuleObject` (on definition-constructible-sheaves)
- proposition-compactness-finite-coefficients--1: `AlgebraicGeometry.ProEtale.DerivedCategory.compactlyGeneratesLocalizingClosure_constructibleFiniteTor` (on lemma-hypotheses-brown-representability)

### Names proposed for two clauses

- proposition-composition-...--7 and --8 rely on the same detection lemma, but it is listed only on --7.
- proposition-ind-constructible-sheaves--1 and --2 both use the parent name `indHeart_fullFaithfulness`.

### Group 3

### Part A (chap-Verdier-and-Poincare-duality, 8 parents, 24 clauses)

#### lemma-internal-adjunction-two-exchange-formulas (--3, --4)
- (10.4) is proved by mate calculus from the internal-Hom exchange at N = ω_Y. That is the same adjunction content as the blueprint's Yoneda argument, stated on all of D for finite Λ, and it is already a parent name (`Etale.nonempty_iso_verdierDual_leftDerivedUpperStar`, `WeilComplex.nonempty_upperShriek_verdierDual_iso`).
- Lean takes a different route for the proper δ-compatibility (--4). It proves that Rf_*δ_K and δ_{Rf_*K} are *isomorphic arrows* (parent name) using an abstract projection-formula lemma and the canonical comparison Rf_*𝔻 ⟶ 𝔻Rf_*. The equality of composites holds only in "formal core" form for an arbitrary square and its mate (`Etale.map_verdierDualDoubleDual_app_comp_mateEquiv`). Verdict: partial.

#### lemma-perfect-complexes-geometric-point (--6, --7, --8)
- Follows the blueprint. All three clauses are parent names: `isPerfect_geometricStalk`, `DerivedCategory.IsPerfect.ihom_unit` and `IsPerfect.isIso_toIhomIhomUnit`.
- Unclaimed field versions also exist: `isPerfect_geometricStalk_of_field` and `_padicAlgCl`.

#### definition-frobenius-operator (--1)
- The clause is the whole definition, so it is parent-name (`WeilBoundedConstructible.compactFrobenius`, `ProEtale.compactFrobenius`).

#### theorem-global-verdier-duality (--1, --2, --3)
- (10.5) is the inverse of the tensor–Hom exchange at N = Λ. These are the parent names.
- (10.6) is not formalized for Λ-coefficients over an algebraically closed field. Only the Weil-complex analogue exists (`WeilComplex.nonempty_verdierDual_derivedLowerStar_iso`), so the verdict is partial.
- The pairing description (--3) is stated by `Etale.uncurry_derivedHomLowerShriekIsoOfAdjunction_hom_app_app`: the uncurried exchange equals the cup product, then evaluation, then the counit.

#### theorem-poincare-duality (--1 … --9)
- Lean proves perfectness of β_K directly, using a Yoneda argument from the projection formula. Separately, it proves that the adjoint of β_K equals purity followed by the inverse of global Verdier duality (`Etale.curry_poincarePairing_eq`), which is exactly clause --7.
- --1 (ω ≅ Λ(d)[2d]) is smooth purity. Its name conflicts with theorem-smooth-purity-all-admissible-coefficients--1.
- --3/--4/--5: K^∨ = `Etale.DerivedCategory.coefficientDual`. In Lean, "perfect" means dualizable.
- --9 (change of coefficients) is only conditional (`Etale.map_poincarePairing`, with the constituent compatibilities as hypotheses).

#### definition-perfect-pairing (--1)
- The clause is the whole definition, so it is parent-name (`CategoryTheory.MonoidalClosed.IsPerfectPairing`).

#### lemma-double-dual-geometric-generic-fibre (--1)
- The clause is the whole lemma, so it is parent-name. Lean states a weaker form: Lg^*δ_K is an iso iff δ_{Lg^*K} is, and the twist is an abstract invertible L.

#### theorem-verdier-biduality (--1, --3, --5, --6)
- Finite coefficients (--1) follow the blueprint's induction through the generic fibre and the proper push-forward (parent names).
- --3, E coefficients: Lean skips this stage and goes from 𝒪_E to Q̄ℓ through integral models (not-formalized).
- --5, exactness: only stated for Weil complexes (partial).
- --6, anti-equivalence: `Etale.verdierDualEquivalence`, finite Λ only.

#### Clauses best stated by Mathlib declarations
- None. The general categorical facts used (IsPerfectPairing, toIhomIhomUnit, IsDualizable.ihom_unit) are in the project's `WeilConjectures/Mathlib/` folder, not in Mathlib itself.
### Part B (chap-Verdier-and-Poincare-duality, 6 parents, 28 clauses)

#### corollary-verdier-exchange-formulas
The parent's Lean names are étale, finite-Λ statements, each the existence of an isomorphism. `nonempty_iso_rightDerivedUpperShriek_verdierDual` is clause --3 for any compactifiable morphism. `nonempty_iso_leftDerivedUpperStar_verdierDual` is clause --7 (closed immersions). Both follow the blueprint: the exchange of `Rf^!` with `RHom`, then biduality.
- Clause --2 (`D Rf_* ≅ Rf_! D`) is formalized only for Q̄_ℓ Weil complexes, as `WeilComplex.nonempty_verdierDual_derivedLowerStar_iso`, by the blueprint route. LEAN-MAPPING says it was "not found".
- Clause --4 for general f exists only in the undualized form `Rf^! ≅ D f^* D` (CtfStability clause (v), and `WeilComplex.nonempty_upperShriek_obj_iso`).
- Clause --6 is a specialization of the --2 lemma.

#### theorem-poincare-duality-frobenius
The Lean proof follows the blueprint for the equivariance clauses (--2, --3, --4). The `*_of_iso` variants in `Frobenius/DualTateData.lean` include the contragredient datum, which is clause --1 (`contragredientWeilDatum(Iso)`). The equivariance of the smooth trace stays a hypothesis `hTr`.

For the clauses over a field, Lean uses abstract linear algebra on similitudes (`ZetaLinearAlgebra/Pairing.lean`). Perfectness of the pairing is an assumption there.
- Clause --6 is the parent name `conj_frobeniusOperator_eq_smul_inverse_dualMap`.
- Clause --8 is the parent name `roots_map_charpoly_frobeniusOperator`.
- Clause --5 (F invertible) has a different route: Lean derives it from the similitude and perfectness, not from φ_K being an isomorphism. It is never stated on its own.
- Clauses --7 and --9 are stated only abstractly: `Module.finrank_of_isPerfPair` (Mathlib) and `LinearMap.det_mul_det_of_similitude` (project).

#### proposition-purity-trace-commute-frobenius
The Lean proof follows the blueprint (`WeilEquivariance.lean`).
- Clause --1 (cartesian Frobenius square) is `Scheme.Hom.isPullback_geometricGaloisFrobenius_geometricFiberMap`.
- Clause --2 is `Etale.upperShriekBaseChangeMap` together with the named instance `isIso_upperShriekBaseChangeMap` for automorphisms.
- Clause --3 is the general compact-support base change iso, which is already on proposition-composition-base-change-rf-shriek--4 (conflict).
- Clauses --4 and --5 are parent names. The trace square assumes `hcoh` (base-change compatibility of the purity map), which is not proved.

#### corollary-cup-product-pairing
Lean works with an abstract `FrobeniusModule.TraceCup` structure, with graded commutativity as a structure field, applied to H^•(X₀⊗k̄, Q̄_ℓ) over F_q.
- Clause --2 is the parent name `TraceCup.pairing_comm_of_eq_two_mul`.
- Clause --3 (alternating middle pairing) is proved inline in `AlgebraicGeometry.Scheme.even_finrank_cohomology_middle`.

#### lemma-class-of-point
The Lean proof takes a different route: an existential normalized orientation. All point classes are equal (`pointClass_eq`) and the trace of a point class is invertible, so the orientation can be rescaled. The blueprint instead composes counits.
- Clause --1 is the parent name.
- Clause --2 ([x] generates H^{2d}) is not stated.

#### theorem-trace-isomorphism-top-degree
- Finite stage (--3): `TateOrientation.bijective_untwistedTraceMap(_comp_cohomologyAddEquivCompactSupport)` covers finite Λ that are self-injective, which includes the admissible stages A_{E,n}. There is no scalar-extension step to general finite A.
- O_E and E stages: --5 and --7 (trace) and --6 (vanishing) are not formalized. The module docs say these stages are unavailable. Vanishing goes from profinite lattices straight to Q̄_ℓ by a filtered colimit.
- Q̄_ℓ stage (--9): the parent name `WeilSheaf.traceIsomorphism_adicConstant` is only existential (some Frobenius-compatible iso H^{2d} ≅ Q̄_ℓ(-d) for X₀ over F_q), not "the specified trace is an iso". Verdict: partial.

#### Clauses best stated by Mathlib declarations
- theorem-poincare-duality-frobenius--7: `Module.finrank_of_isPerfPair`.
- Generic linear algebra in the project rather than in Mathlib: theorem-poincare-duality-frobenius--9 (`LinearMap.det_mul_det_of_similitude`) and theorem-poincare-duality-frobenius--5 (`LinearMap.isUnit_det_of_similitude`, partial).

#### Sorry / axiom notes
No cited declaration contains `sorry` directly. The project's only live `sorry`s are in `WeilSheaf/SmoothPurity.lean:296`, `SmoothUnitBaseChangeEtale.lean:343` and `WeilFourierInversion.lean`, and none is in a cited file. Transitive axioms were not machine-checked. The header of `WeilSheaf/VerdierDual.lean` still says "stated with sorry", but its proofs are now complete.
### chap-Abelian-varieties

- **definition-abelian-variety** (--2, --4): Neither [n] nor "symmetric sheaf" has a def. [n] is the expression `𝟙 A ^ n` (A[n] = `torsionSubgroupScheme`, ker of `𝟙 A ^ n`). Symmetric is written out as `Nonempty (overPullback ι[A] L ≅ L)`. Both clauses are inline.
- **lemma-symmetric-ample-sheaf** (--1 = whole lemma): parent-name. The four parent names (Projective.lean) follow the blueprint exactly: closed immersion into P^n, then j^*O(1), then L ⊗ [-1]^*L ample and symmetric.
- **proposition-no-frobenius-fixed-vector**: follows the blueprint (finiteness of A(k_0), then the group-theoretic Tate-module lemma), but only for m = 1 and the Frobenius over the given finite field. The automorphism statement uses arithmetic σ. F^m for m>1 needs base change to F_{q^m}, and ⊗E (clause --4) is not formalized. Unassigned helpers: `eq_zero_of_galoisRepresentation_frobenius_eq_self`, `frobeniusSubOneLinearEquiv` and `finiteDimensional_rationalTateModule` (RationalTateModule.lean), recorded as partial names.
- **proposition-integral-tate-module**: --1 is the parent name `nonempty_addEquiv_torsionBy_points`. --3 (T/ℓ^n ≅ A[ℓ^n]) is not formalized; Lean gets T ≅ Z_ℓ^{2g} from divisibility and torsion counts without this quotient. --4 is partial: Galois equivariance holds by construction (`galoisRepresentation` is componentwise; `coe_galoisRepresentation_apply` is equivariance of the projections). Field invariance is only for A over an algebraically closed field (`bijective_toUnit_comp_torsionSubgroupScheme`, already on corollary-torsion-jacobian-field-extension--2).
- **lemma-rigidity**, **theorem-theorem-cube**: single clause equal to the parent, so parent-name. The Lean statements are slightly more general (rigidity: geometrically connected and reduced, Y arbitrary; cube: M ≅ N form).

### chap-Algebraic-groups-in-characteristic-zero

- **lemma-stable-subspaces-center**: the two parent names are exactly the two clauses (`invariant_iff_differential_invariant` for --1, `range_lieAlgebraMap_identityComponent_center` for --2).
- **lemma-connected-components-images-homomorphisms**: --2 uses `isClosed_range_of_isMonHom` for closedness (SGA 3 route via base change to k̄) and `exists_isMonHom_imageι` for the subgroup-scheme structure, which assumes G proper. --3 is `GrpObj.isIso_left_of_differential_bijective` (with the matrix form `eq_of_le_of_lieSubalgebra_eq`). All are parent names.
- **lemma-cartan-s-criterion**: single clause, parent-name `LieSubalgebra.isSolvable_of_trace_mul_eq_zero` (project, built on Mathlib).
- **lemma-engel-s-theorem**: takes a different route from the blueprint. There is no triangular basis; Lean uses Mathlib's `LieModule.isNilpotent_iff_forall'` (flag form) and `LieAlgebra.isNilpotent_iff_forall` with ad-nilpotence. --1 and --3 are the two conjuncts of the parent name `exists_forall_apply_eq_zero_and_isNilpotent`. --2 is different-route. --4 is the Mathlib instance `LieAlgebra.isSolvable_of_isNilpotent`.
- **lemma-killing**: --1 is the parent name. --2 is newly found: `LieAlgebra.HasTrivialRadical.derivedSeries_eq_top` (CartanCriterion.lean:94) states [l,l] = l. LEAN-MAPPING.md:677 says this is "not stated separately", which is out of date.

#### Clauses best stated by Mathlib declarations
- lemma-engel-s-theorem--4: `LieAlgebra.isSolvable_of_isNilpotent` (Mathlib/Algebra/Lie/Nilpotent.lean:739)
- (background, already parent names) lemma-engel-s-theorem--1/--3 rest on Mathlib's `LieModule.isNilpotent_iff_forall'`, and lemma-killing--1 is a wrapper of Mathlib's `LieAlgebra.IsKilling.killingForm_nondegenerate`.

### Group 4

69 clauses. Verdicts: parent-name 41, partial 15, project 9, inline 2, different-route 1, not-formalized 1.
No conflicts with existing names except where noted. I checked only direct `sorry` in the files of newly proposed names (none; `BoundedConstructibleLowerStar.lean` mentions `sorry` only in a comment). I did not check transitive dependencies, because that needs a build. Proetale was present but did not supply any of the names.

### chap-Specialization-and-contracting-correspondences

- **proposition-external-kunneth-formula-nearby-cycles**: follows the blueprint (chart-dimension induction, slicing), with Qbar_ell coefficients. The clause is `isIso_kunnethMap`.
- **lemma-finite-support-global-sections**: stated directly (Qbar_ell).
- **lemma-kunneth-map-slice**: the Lean proof uses the blueprint's identifications as exchange maps on the geometric slice:
  - (2) change of trait: `isIso_pullbackExchange_baseChangeHom_traitMap_{of_generic,padicIntegers,residueField}`;
  - (3) compatibility square: `map_kunnethMap_sliceSpecial_comp_pullbackExchange`, whose docstring cites the lemma;
  - (1) invariants: only the split-mono / averaging form (partial).

  The torsion case descends along the Galois layer of S' -> S instead of taking P-invariants.
- **lemma-kunneth-map-proper-direct-image**: abstract commutative square, stated directly.
- **corollary-contracting-local-terms-point**: both clauses are the parent's names.
- **lemma-normal-cones-contracting-ideals**: the lifts are `deformationSpaceMap`, which is a conflict because it is already on lemma-functoriality-deformation. Their special fibres are `normalConeMap`, with `normalConeMap_normalConeToDeformationSpace` linking the two. Clause (1) is only set-theoretic in Lean.
- **theorem-contracting-correspondences-local-terms**: Lean covers only Z equal to a rational point. Its proof uses additivity, proper pushforward and the vanishing lemma rather than the general specialization argument. Clause 2's point case is the corollary's name (conflict).
- **lemma-duality-invariants-pro-p**: abstract module-level and categorical forms.
- **proposition-nearby-cycles-commute-verdier-duality**: direct.
- **lemma-nearby-duality-proper-direct-image**: clauses 1 and 2 are abstract `Verdier.nearbyDualityMap_proper` and `nearbyDualityMap_restrict`. For (E.14), Lean only shows RGamma(delta) is an isomorphism, not that it equals the identity (partial).
- **lemma-nearby-duality-slice**: only the isomorphism consequence of (E.17), with the twist equation as a hypothesis (partial).
- **lemma-nearby-cycles-universal-kernel**: both identities are stated (parent names).
- **lemma-section-specialized-correspondence**: better names exist in `SpecializedCorrespondenceSection.lean`. The `_of_kunneth` and `supportSpecializationUnit` versions discharge the first universal-kernel identity and use sigma_C as in the text.
- **corollary-specialization-when-fixed-point-scheme**: only the case F_red = {y} x S (contracting deformation): `integral_sp_eq_map_integral_restrict` and `restrict_eq_zero_of_sp_eq_zero` (partial).
- **proposition-specialization-trace-class**: different route. Lean defines sp_F (`TraceSpecialization.sp`) but never proves Tr(u_s) = sp(Tr(u)). It proves vanishing (`sp_traceClass_eq_zero`) plus injectivity on the point component. u_s exists only inline, and `specialCorrespondence` has u := 0.
- **Base change for nearby cycles** (E.8–E.11): abstract mate-calculus statements with compatibilities as hypotheses. For the theta composition law, `dualizingExchange_eq_comp` handles general d, whereas the parent's `θ_comp_law` covers only the proper-model case.
- **Specialization to the normal cone**: follows the blueprint (defect C_{X,Z}, exchanges, blow-up), all with Qbar_ell coefficients. The "in particular" clause of Verdier's theorem is stated only for a point. The thick origin is stated for finite free modules (`..._finiteCoefficientConstant`), not for all finite modules.

### chap-Proper-base-change

- **lemma-composition-cancellation**: (i) uses pasting of base change maps rather than the IA spectral sequence; (ii) follows the blueprint.
- **theorem-cohomology-curves**: there is no assertion-by-assertion proof. `IsCurve.Assertions.of_finite_coefficients` proves all eight assertions for every sheaf of modules over a finite ring, via reduction to constructible F_r-sheaves. C3–C6 are therefore partial: unbounded torsion sheaves are not covered.
- **theorem-pbc-injective-acyclicity**: `Etale.tfae_hasTorsionBaseChange` together with `hasTorsionBaseChange_iff_forall_isIso_baseChangeHomologyMap` cover clause (ii), which LEAN-MAPPING had listed as absent.
- **definition-torsion-sheaves--2**: F[n] appears only inline, inside `IsTorsionAbelianSheaf`.
- **proposition-proper-direct-image-constructible-complexes**:
  - --4 is `CondensedRing.boundedConstructible_rightDerivedLowerStar_obj` (Qbar_ell, any finite-type f);
  - --11 is `isIso_properProjectionMap_boundedConstructible_rational` (E or Qbar_ell).
- The remaining clauses in this chapter are single clauses equal to the parent (parent-name). Etale-site statements stand in for the pro-etale classical ones.

### chap-Smooth-base-change

- **theorem-smooth-base-change-all-admissible**: the O_E and Qbar_ell cases are parent names. The E case is not formalized.
- **Kunneth**: Lean takes the Stacks 0F1N route (`isIso_tensorBaseChangeMap`, general finite Lambda), so the field-coefficient reduction is bypassed. The ordinary external Kunneth is only stated in special cases (point target; proper over Qbar_ell; open immersion over Qbar_ell), so it is partial.

### Clauses best stated by Mathlib declarations

None. Every clause in this group is stated, if at all, by project declarations. The homological-algebra clause lemma-acyclic-resolutions--1 uses project names in `CategoryTheory.Functor`, which are already on its parent.

### Group 5

Verdict convention: the verdict says what Lean states. `names` holds only names that are on no node yet; names that state the clause but already sit on another node go under `conflicts`. So a `project` verdict with empty `names` means "stated in Lean, but the name is taken".
Counts: project 31, parent-name 21, partial 8, not-formalized 8, mathlib 2, inline 1.

Sorry check: two declarations are proved by `sorry`. `AlgebraicGeometry.ProEtale.integral_local_structure`, the parent name of proposition-local-structure-integral-constructible-complexes, has `sorry` at IntegralLocalStructure.lean:841. The bundle `AlgebraicGeometry.ProEtale.coefficientHeartStatement` has `sorry` at CoefficientHeartStatement.lean:106, so I did not propose it. None of the other cited files contains `sorry` directly. Several of them import, at some distance, files that contain `sorry` (for example SixFunctors/Etale/Derived/IntegralVerdier.lean and SixFunctors/CoefficientReduction.lean). I did not check axiom use per declaration (that needs `#print axioms`). The proetale package is present but was not needed.

### chap-The-six-operations-on-Dbctf

**proposition-six-operations-dctf (18 clauses).** The parent's Lean names cover only finite Λ on the **étale** site. On the pro-étale side, Lean splits by coefficient ring rather than following the blueprint:
- Finite A: statements are transported from the étale site along ν^*.
- ℓ-adic coefficients: the `CondensedRing` framework has a separate copy of each result for Q̄ℓ (namespace `CondensedRing`), for E (`ContinuousMapRingObj`) and for O_E (`PadicIntegersRingObj`). Rf_* is handled by Deligne finiteness via dévissage to a sheaf in degree 0, not by the compactification f = pj. RHom is handled by noetherian induction from the lisse case. Rf_! and the adjunctions are restrictions of the ambient ones (`Adjunction.restrictFullyFaithful`).

Gaps and caveats:
- Several exact statements are already on other nodes:
  - Rf_* for finite A and for O_E/E.
  - f^! for all four coefficient types.
  - The O_E tensor statement.
- Pro-étale finite-coefficient tensor, f^*⊣Rf_* and tensor–Hom adjunctions exist only on the étale site (partial).
- For --7/8/9, preservation of Rf_! is encoded as a def plus a compatibility iso, not as a theorem.

**proposition-isomorphisms-reduce-finite-coefficients.** Lean has only the integral conservativity step: reduction mod π or mod ℓⁿ detects isomorphisms on Dbc(O_E). There is no reduction principle for abstract F, G, θ, and no E or Q̄ℓ steps (--1, --3, --4 are not formalized).

**proposition-dctf-x-qbar-2-colimit.** --1 is exactly the parent's `constructibleCocone_isFilteredTwoColimit`.

**definition-change-of-coefficients-maps.** For --1, the parent's `derivedPullIso` is built as a conjugate of the restriction-of-scalars iso, not literally by associativity of derived pullback; it is the same canonical iso. For --3, the tensor iso `derivedExtendScalarsTensorIso` is already on proposition-six-operations-change-coefficients--6.

**lemma-extension-scalars-preserves-dctf.** --1 is the whole lemma. The parent name covers finite A→B; the ℓ-adic names sit on the duplicate clause proposition-six-operations-change-coefficients--1.

**lemma-change-coefficients-compact-support.** Both clauses are covered by the parent names. --1 is the finite-ring case; the ℓ-adic isos sit on definition-change-of-coefficients-maps--5. --2 is independence of the compactification.

**proposition-six-operations-change-coefficients (9 clauses).**
- --8 has a free project name (pullback transitivity in coefficients).
- --13 is the parent's `ihomComparison_comp_app`.
- --18/--19 are exactly Mathlib's `unit_mateEquiv` / `mateEquiv_counit`.
- --22 is `LaxMonoidal.coev_ihomComparison`, a project file in the Mathlib-mirror folder.
- Transitivity in coefficients and compatibility with composition are **not formalized** for Rf_! and f^! (--10, --11, --16, --17).

**lemma-change-coefficients-direct-image.** The Lean route is the same as the blueprint's.
- O_E→E (--4) and E→Q̄ℓ (--5) are exact matches, but the names are taken by proposition-six-operations-change-coefficients--3.
- O_E→O_E/ℓⁿ (--2) is the parent name.
- Finite A→B (--1) exists only for proper g.
- O_E→O_F (--3) has only the generic finite-free lemma.
- For composites (--6), only the decomposition lemma exists, and it is on another node.

### chap-Constructible-complexes

Here the Lean proofs mostly follow the blueprint, and many clauses are the whole parent statement (parent-name):
- continuity of Ext;
- sections with closed support --1/--2;
- descent of lisse Q̄ℓ-sheaves;
- coefficient-heart-b --1/--2;
- descent to a finite coefficient field --1/--2;
- local structure of integral constructible complexes (sorry, see above);
- ctf = bc;
- flat models --3 (étale site).

Notable points:
- **sections-support--3:** formula (3.1) is used only inside the proof of `CondensedRing.constructibleExtContinuityStratum` (inline).
- **definition-lisse-sheaves--2:** not formalized. The only "lisse complex" notion in Lean means dualizable (HRS), which is a different definition.
- **lemma-constructible-sheaves --1..4:** all are conjuncts of `coefficientHeart_closure`, which is on sibling --5. There is no finer public name.
- **proposition-inverting-ell--1:** follows from the parent's `integral_scalar_map_eq` with f = id, g = 0. The route differs: continuity of Hom along multiplication by ℓ, not charts.
- **lemma-bounds-finite-reductions:** Lean has one lemma per clause: `integral_finite_constructibility` (--1), `integral_finite_residue_tor` (--2, using a pro-étale nilpotent-residue criterion instead of minimal stalk resolutions), and `integral_finite_tower_bounds` (--3). --4 is the parent's last conjunct.
- **lemma-flat-models-generators--2:** two free étale-site names.
- **lemma-integral-models:**
  - --3: the free name `CondensedRing.boundedConstructible_leftDerivedUpperStar_obj`, also proposed for six-ops-dctf--1, so one node must give it up.
  - --4: the parent's `boundedConstructible_tensorObj`.
  - --5: only as the open part plus the closed part, both on lemma-inverse-image-tensor-product.
  - --6/--7: both conjuncts of the single public bundle `WeilConjectures.SixFunctors.integral_models_generators`; the per-clause lemmas are private.

### Clauses best stated by Mathlib
- proposition-six-operations-change-coefficients--18: `CategoryTheory.unit_mateEquiv`
- proposition-six-operations-change-coefficients--19: `CategoryTheory.mateEquiv_counit`

The project's Mathlib-mirror lemmas `CategoryTheory.Functor.LaxMonoidal.ihomComparison_comp_app` (parent of --13) and `coev_ihomComparison` (--22) are Mathlib-style, but they live in the project, not in upstream Mathlib.

### Duplicate proposals to resolve
- `CondensedRing.boundedConstructible_leftDerivedUpperStar_obj`: proposed for six-ops-dctf--1 and for lemma-integral-models--3.
- `WeilConjectures.SixFunctors.integral_models_generators`: proposed for lemma-integral-models--6 and --7.
- `CondensedRing.boundedConstructible_rightDerivedLowerStar_obj` (Q̄ℓ, any f): proposed for six-ops-dctf--5, but it may be wanted by proposition-proper-direct-image-constructible-complexes--4, which is unnamed while its O_E/E siblings use the analogous lemmas.

### Group 6

Verdict counts (77 clauses): parent-name 34, project 19, partial 14, not-formalized 6, different-route 2, inline 2.

General notes:
- Some parent-name entries also list extra names that are on no node yet: `localTerm_traceClass_frobeniusGraph_eq_supportedRestriction`, `relativeFrobenius_fst`/`_snd`, `HasWeightsAtMost.tateTwist`, `mem_detWeightMultiset_iff`.
- There is no build at 94ce2d8, so `#print axioms` was not run. The cited files contain no literal `sorry`. However, TraceFormulaCorollaries.lean documents `WeilSheaf.poincareDuality` as not yet sorry-free; this affects `duality_reciprocity`, `reciprocity` and `functional_equation_frobeniusCharpolyRev`.
- Every cited name was checked to be declared in the sources. Conflicts were checked with grep over blueprint/.
- **Clauses best stated by Mathlib declarations: none in this group.**


#### lemma-frobenius-fixed-scheme
The Lean proof follows the blueprint: `FixedLocus.isoSigmaPoint` gives Fix ≅ ∐ Spec k, finiteness follows from it, and properness and reducedness follow from finiteness (FixedPointComponent.lean). Clause --4 (properness) is exactly the parent name `FixedLocus.isProper_hom`.

#### lemma-local-term-restriction-map
Same idea as the blueprint, but the Lean version is global: the supported restriction ρ_P is built on the whole fixed locus and then restricted to the point y, with ℚ̄_ℓ coefficients rather than a finite ring A. The Frobenius-graph theorem `Correspondence.localTerm_traceClass_frobeniusGraph_eq_supportedRestriction` (FrobeniusSupportedRestriction.lean:109) is the most specific statement and is on no node; it also fits the parent.

#### lemma-restriction-punctured-curve
Follows the blueprint. The single clause is the parent name `Etale.puncturedRestriction_eq_zero`, stated for any closed subscheme C rather than only a curve.

#### lemma-tangent-cones-on-cover
Follows the blueprint (miracle flatness; étale away from H∪V; degree e²). For --1, the new names `CoverDatum.flat_π`, `free_and_finrank_π`, `etale_π_openComplement` and `natCard_geometricFiber_π` add to the parent's `isFinite_π`, `regular` and `isDiscreteValuationRing_H'`. `CoverDatum.tangentConesOnCover` (TangentConesOnCover.lean:233) is the assembled statement of the whole parent; recommend adding it to the parent.

#### lemma-covers-degree-prime-to-ell
The single clause equals the parent. Lean constructs one cover datum with ramification index e prime to ℓ (Sylow cover + normalization) and does not state "for every multiple d of d₁". That form exists only at field level as `IsGalois.exists_coversDegreePrimeToEll`, which is on no node.

#### lemma-additivity-open-subscheme-complement
Follows the blueprint: additivity of traces on the localization triangle. --2 is `trace_compactPullback_comp_eq_add`. --1 is `openPieceCoefficient` / `closedPieceCoefficient`. The correspondences on j^*K and i^*K appear only inside other definitions, and the stalk-map claim is not stated for coefficient morphisms.

#### lemma-comparison-via-relative-frobenius
RelativeFrobeniusIterate.lean follows items (1)–(4) exactly, and the parent's 9 names split cleanly across the four clauses. New for --1: `AlgebraicGeometry.relativeFrobenius_fst` and `relativeFrobenius_snd` (the equations f'∘r = f and p∘r = Φ_X). The definition `AlgebraicGeometry.relativeFrobenius` is unassigned; it belongs to the --text-1 setup.

#### theorem-grothendieck-lefschetz-trace-formula
Different route. Lean proves the ℚ̄_ℓ formula directly: the relative form `weilShriekTraceFunction` comes by Noetherian induction from generic base cases, and `weilTraceFormula` is its case Y = Spec k, with the Frobenius twisted by a finite-order automorphism e (e = 𝟙 is the clause). The blueprint's chain finite A → 𝒪_E → E → ℚ̄_ℓ does not appear. So --1, --2, --3 and --7 are not-formalized, and --4 is parent-name.

**Clauses best stated by Mathlib declarations:** none in this part. All relevant statements are project declarations; proetale was present but no clause here needed it.

**Sorry/axiom status:** not verified. There is no build (lake cache has no outputs for 94ce2d8). None of the cited declarations contain `sorry` in their own text.

#### lemma-integral-models-rational-frobenius-correspondences
The Lean proof follows the blueprint, in WeilConjectures/TraceFormula/RationalModel.lean.
- --1 is `exists_integralModel_frobeniusCorrespondence`.
- --3 (stalks) is `pow_smul_upperStar_map_frobeniusCoefficientIterate_eq`.
- Both are already parent names. Lean uses ℓ^N instead of π_E^N, which is equivalent.
- --2, the T_{c_m} identity, is not formalized. The file's docstring says so: the compactly supported operators exist only for ℚ̄_ℓ coefficients.
- Lean stops at the intermediate iterate identity `pow_smul_frobeniusCoefficientIterate_eq`, which is a parent name but no clause.

#### lemma-logarithm-determinant
The Lean proof follows the blueprint (logarithmic-derivative proof).
- --1 is `LinearMap.inv_charpolyRev_eq_exp`, a parent name.
- --2: the definition is `LinearMap.alternatingCharpolyRevProd` with e = 1, a new name. It works on a graded family (W_i, F_i), not on a perfect complex.
- --3 is only partial. `LinearMap.inv_alternatingCharpolyRevProd_eq_exp` uses the alternating sum of traces on cohomology, not the categorical trace tr_L.
- The bridge between the two is proposition-properties-trace--6, whose closest Lean statement is `DerivedCategory.trace_eq_algebraMap_sum_negOnePow_linearMapTrace`.

#### corollary-point-counting-zeta-function
- Only --1 was in my list. Lean has `weilPointCount` (a parent name): ℚ̄_ℓ only, alternating-trace form, Frobenius twisted by a finite-order e.
- The categorical-trace statement for finite, integral and ℚ_ℓ/E coefficients is not formalized; the trace formula itself exists only for ℚ̄_ℓ. Verdict: partial.

#### corollary-functional-equation
The Lean proof follows the blueprint's decomposition (Betti symmetry, parity, D², determinant form, sign form), with two differences:
- It works through the integral Frobenius factors P_i: b_i = deg P_i and D_i = ±lc P_i, identified with dim H^i and det F_i over ℚ̄_ℓ.
- All X₀-level statements assume geometrically connected. The blueprint only assumes pure dimension d.

The abstract algebra is in ZetaFunction/ClassicalFunctionalEquation.lean:
- `prod_determinant_sq`, `alternatingProdEval_eq_prod_determinant`, `alternatingProdEval_eq`
- `weilSign`, `weilSign_eq_one_or_eq_neg_one`

The definitions are in ZetaFunction/BettiNumbers.lean and BettiSymmetry.lean:
- `weilBettiNumber` with `weilBettiNumber_eq_finrank`
- `Polynomial.alternatingNatDegreeSum`
- `weilDeterminantScalar` with `map_weilDeterminantConstant_eq_det`

None of these is on any node yet. `weil_functional_equation` is already on theorem-weil-conjectures-smooth-proper-schemes (conflict for --10).

**Recommendation:** add `AlgebraicGeometry.Scheme.functional_equation_frobeniusCharpolyRev` (TraceFormulaCorollaries.lean:398) to the parent. It is the cohomological statement over ℚ̄_ℓ of the whole corollary in one conjunction: b_{2d-i} = b_i, dχ even, D² = q^{dχ}, both forms of the functional equation, and ε = ±1.

**Sorry caveat:** the TraceFormulaCorollaries.lean module docstring says `WeilSheaf.poincareDuality` is "not yet sorry-free". This could not be checked because there is no build at 94ce2d8, so `#print axioms` was not run. It affects `duality_reciprocity`, `reciprocity` and `functional_equation_frobeniusCharpolyRev`. The abstract polynomial lemmas do not depend on it.

#### Clauses best stated by Mathlib declarations
None. Mathlib (0df444a) has no determinant–trace exponential identity (only `Matrix.eval_charpolyRev` and `coeff_charpolyRev_eq_neg_trace`). Every clause here is stated by project declarations or not at all.

#### theorem-trace-formula-frobenius-correspondence (1 clause)
Different route. The blueprint works with a finite ℓ-primary ring A, compactifies and applies Lefschetz–Verdier on P^1. Lean works only with Q̄_ℓ coefficients (`Dᵇc(X)⟦padicAlgClRingObj ℓ⟧`). It proves `TraceFormulaHolds` (degree 1) for a model Frobenius by induction on the size of an affine cover (open/closed additivity), then gets degree m by changing the field. There is no finite-coefficient trace formula in Lean. Clause --1 is the parent name `trace_frobeniusCompactOperator_eq_sum`, with the coefficient caveat.

#### proposition-function-sheaf-dictionary (3 clauses)
Follows the blueprint, in the `WeilComplex` (Q̄_ℓ) framework of siblings --1/--2. (3) is `WeilComplex.traceFunction_derivedLowerShriek`: base change to the point, then Grothendieck–Lefschetz on the fibre. (4) is `traceFunction_eq_add_openClosed` plus the j_! value lemmas: open–closed triangle, then (3) along the immersions. (5) is the Grothendieck–Lefschetz theorem; both its names are already on theorem-grothendieck-lefschetz-trace-formula (conflicts).

#### lemma-scheme-frobenius-geometric-frobenius (4 clauses)
κ_m and ψ_m = φ_m κ_m are formalized on the étale site (`Etale.leftDerivedUpperStarGeometricFiberFrobeniusIterateIso`, `…IterateHomIso_add_hom_app`, `weilDatumIterate_schemeFrobeniusForm_hom`). The pro-étale trace formula takes a different route: Weil objects are defined for the scheme Frobenius Φ itself, so κ = id. In that setting, T_{c_m}(φ_m) = Frob^m is `WeilBoundedConstructible.globalOperator_graph_eq_pow`. Clause --4 (arbitrary morphism) has no counterpart in its Galois form. Its pro-étale content is `globalOperator_ofGraph`, already on definition-frobenius-correspondences-their-operators--5.

#### definition-frobenius-correspondences-their-operators (1 clause)
--3 ("a Frobenius correspondence is a morphism ψ : Φ^*K → K") has no declaration. It appears only as a binder type (inline).

#### proposition-properties-trace (3 clauses)
Follows the blueprint. All three clauses are the parent's own names:
- --4 `trace_eq_algebraMap_sum_negOnePow_linearMapTrace`, for free modules, not projective
- --5 `trace_eq_trace_add_trace_of_shortExact`, short exact sequence form instead of the filtered derived category
- --6 `trace_eq_algebraMap_sum_negOnePow_trace_homologyMap`, via the project's Hopf trace formula

#### lemma-local-terms-point (1)
Clause is the parent name `Correspondence.integral_traceClass_ofEnd`; follows the blueprint.

#### theorem-proper-pushforward-lefschetz-verdier (1)
--3 is the parent name `BorelMooreSection.integral_eq_sum_localTerm`; follows the blueprint.

#### proposition-exceptional-external-kunneth (1)
Clause is the parent name `Etale.nonempty_iso_externalProduct_rightDerivedUpperShriek`. It states only that some isomorphism exists, not that α is one.

#### lemma-lift-correspondence-invariant-decomposition / proposition-additivity-trace-classes / lemma-closed-piece-pushforward
Different route. There is no filtered derived category. Lean uses a morphism of open–closed triangles, for Z a rational point only:
- u^U is `pointOpenPieceCoeff`, with its counit square.
- u^Z is the pushforward of the restricted map, with its unit square.

Additivity is `traceClass_eq_add_of_distTriang`, under Hom-vanishing hypotheses. Verdicts: lift--1 partial; additivity--1 different-route; closed-piece--1 is the parent name (point case).

#### Clauses best stated by Mathlib
None. All clauses here are project-level. Mathlib only provides ingredients (`LinearMap.trace`, `Int.negOnePow`) used inside the project's trace lemmas.

#### lemma-filtrations-spectra
Lean follows the blueprint split: charpoly factorization over a filtration (--1), plus dual, wedge and tensor spectra (--3/4/5), all in WeilConjectures/Mathlib/LinearAlgebra/Charpoly/Basic.lean. The multiset form (--2) is never stated. It is derived inline in WeilGroup.isPunctuallyPure_subquotient_of_isReal from charpoly_eq_prod_charpoly_mapQ_of_le and Mathlib's Polynomial.roots_prod.

#### proposition-weights-under-usual-operations
Lean works only with bounded mixedness: `IsMixedOfWeightsAtMost`, defined as the filtration closure of "punctually pure of some weight ≤ w", with `IsMixed` = ∃ w.
- Formalized: extension, sub/quotient and pullback closure, for pullback along immersions only as a declaration; general pullback is inline in IsMixed.upperStar.
- Pure operations are formalized: tensor, dual, constant and Tate twist, upperStar.
- No sheaf-level mixed tensor (--5) and no mixed dual or annihilator filtration (--6). There are only punctual-bound or representation-level analogues: HasWeightsAtMost.tensorObj and Representation.HasGradedPieces.dual.
- B_b (--11) is not a standalone definition. Lean defines F ⊗ B_b directly as WeilSheaf.constantTwist, which is already on another node.

#### lemma-subobjects-quotients-weil-sheaves
Same route (ObjectProperty.filtrationClosure closed under subobjects/quotients). The parent names IsMixedOfWeightsAtMost.of_mono/of_epi are exactly clause --3. There is no IsMixed.of_mono.

#### proposition-lattices-representations-normal-scheme
Different route. Lean (exists_lisseMonodromy_of_isIntegrallyClosed_stalk) builds the monodromy equivalence from universal profinite étale covers, with ℚ̄_ℓ coefficients. It does not use lattices or the lattice fibre functor. The clause equals the parent, so it is partial with the parent names as conflicts.

#### lemma-global-lattice-normal-scheme
Lean proves a cocycle/twisted-section form of lattice existence only on regular schemes (Bhatt–Scholze finite invariant lattice set). It does not cover normal schemes, and the M_n / inverse-limit claims are not stated. The clause equals the parent: partial.

#### proposition-bound-largest-determinant-weight
Follows the blueprint (Rankin–Selberg on tensor squares). The clause equals the parent and is exactly WeilGroup.sq_norm_le_rpow_of_isReal.

#### lemma-positivity-euler-factors
Follows the blueprint. The clause equals the parent and is exactly WeilSheaf.IsReal.inv_localPolynomial_stalk_tensorPow_nonneg (t instead of t^{deg x}; lisse assumed).

#### lemma-degree-zero-top-cohomology
- H^0 = invariants (--1) and H_c^2 = coinvariants(-1) (--2, affine only) are formalized.
- Weight statements are only partial:
  - H_c^2 weights ≤ a+2 is proved only for pure input.
  - H^0 weight bound and H^0 purity are not stated as declarations. The key eigenvalue lemma exists_hasEigenvalue_stalk_of_hasEigenvalue_globalSections is free. H^0 purity appears inline as `have hΓ` in isPureOfWeightOver_geometricCoinvariants.
  - H_c^2 purity is the parent names.

#### Clauses best stated by Mathlib
None. Polynomial.roots_prod is only the general fact behind lemma-filtrations-spectra--2, which is derived inline.

#### proposition-kummer-duality-integral-tate-module
Lean takes a finite-level route. JacobianTorsionDatum carries J0(Kbar)[l^n] ≃ Pic(C)[l^n]. kummerEquiv and its two compatibility lemmas give clause 1, but they sit on proposition-h-1-curve-tate-module, as the blueprint proof itself says. bijective_curvePairing (on no node) is the finite-level Poincaré duality. exists_picTorsionPairing packages the finite-level characters compatibly with reduction and Frobenius. There is no inverse limit, no Hom(T_l J, Z_l), and no B^t matrix statement, so clauses 2 and 3 are partial. Finite base field only.

#### definition-determinant-weight
Direct definitions. detWeightMultiset (parent name) is DW(V) as a multiset over a composition series. mem_detWeightMultiset_iff (on no node) is the lemma identifying it with the set described in the blueprint.

#### corollary-determinant-weights
Follows the blueprint. Clause 2 is exactly two of the parent's names: Representation.detWeight_mul_of_mem_ker (independence of s) and WeilGroup.isPunctuallyPure_det_baseChange_iff (independence of the coefficient field).

#### lemma-normality-geometric-monodromy
Follows the blueprint (closure via vanishing ideals). Clause 1 is the parent's names: arithmeticMonodromy_le_geometricMonodromy, normal_zeroLocus_geometricMonodromy, instIsHopfIdealVanishingIdeal and isRadical_vanishingIdeal.

#### proposition-determinant-weights-tensor-operations
Lean (central element / scalar readout) covers parts (1) and (2) only. Part (3), DW(V^∨) = -DW(V), is not formalized. Only the punctual-purity analogue IsPunctuallyPure.dual exists.

#### lemma-tensor-exterior-powers-filtered-representations
The statements are the same as the blueprint's, though the construction differs. Lean builds the ⋀^r filtration by induction on two-step extensions instead of sorting basis wedges. Clauses 1 and 2 are the parent's hasGradedPieces_tprod and CompositionSeries.hasGradedPieces_exteriorPower. Clause 3 is the general refinement theorem Representation.CompositionSeries.exists_equiv_sigma_of_monotone (on no node), plus the parent's nontrivial_piTensorProduct_exteriorPower_iff for nonvanishing.

#### Clauses best stated by Mathlib declarations
None. Every statement above is in the project (WeilConjectures, including its WeilConjectures/Mathlib/ staging directory). Only standard ingredients used in proofs come from Mathlib, e.g. SemidirectProduct and the Jordan–Hölder machinery.

### Group 7

### chap-Smooth-purity

**theorem-smooth-purity-all-admissible-coefficients**: The parent names (`smoothOrientation`, `isIso_smoothOrientation`) give only the Q̄_ℓ orientation at K = unit. It is canonical only if the integral lift of the finite orientations exists, and that existence is not formalized, so a non-canonical iso is used as a fallback. Lean jumps from integral (non-canonical, König's lemma) directly to Q̄_ℓ and has no E stage. The affine-line normalizations (--5..--8) are not formalized: Lean normalizes on the A¹ fundamental class (`exists_affineLineFundamentalClass_comp_smoothPurityTrace`, explicitly not the canonical γ), not via the P¹ trace (9.1). Composition (--10) exists only for open immersions, and change of coefficients (--11) only for finite rings with hypotheses (both are names already on other nodes).

**proposition-transitivity-trace-map**: The single clause is the parent (`smoothPurityTrace_comp`, finite étale). Lean follows the blueprint (trace = counit ∘ Rf_!γ), with the γ composition coherence as a hypothesis.

**proposition-compatibility-purity-change-coefficients**: Only the finite→finite case exists: `map_smoothPurityIso_hom_comp` and `map_smoothPurityTrace`, the parent's names, i.e. clauses --1 and --2. Both are conditional on constituent compatibilities (θ, φ, twist) and counit compatibility. Lean follows the blueprint's constituent-wise route (9.17). All integral, E and Q̄_ℓ stages (--3..--14) are not formalized. The integral canonical orientation exists only as a predicate (`IsIntegralSmoothOrientation`).

**proposition-compatibility-purity-base-change**: --1 (finite) is stated exactly by `Etale.canonicalSmoothPurityMap_baseChange`, but its proof is **`sorry`**. The parent name `leftDerivedUpperStar_map_comp_smoothPullbackExchange_hom` is tautological. --2 (O_E) and --3 (E) are not formalized. --4 (Q̄_ℓ) was already named.

**proposition-compatibility-purity-composition**: Only the Q̄_ℓ, K = unit case with g an open immersion is formalized (the parent names). It holds by construction, since the orientation is normalized via `smoothImageFactor`, and not by the chart and iterated-integration argument. The finite, integral and E clauses are not formalized.

**Single-clause parents** (the clause text equals the parent): proposition-relative-dualizing-complex, proposition-smooth-purity-finite-coefficients, definition-deformation-normal-bundle, lemma-section-normal-bundle, proposition-purity-vector-bundles, corollary-dualizing-complex-smooth-scheme and theorem-sp-qbar get the verdict parent-name. Lean's finite smooth purity takes a different route from the blueprint: diagonal frame classes (Kummer boundaries) glued into a fundamental class of Δ, instead of deformation to the normal bundle plus vector-bundle purity (Basic.lean docstring of `nonempty_iso_dualizingComplex_twistShift`). For definition-deformation-normal-bundle--1, two extra lemmas identify the Rees model with "blowup minus strict transform": `IdealSheafData.deformationSpaceIsoBlowupModelOpen` and `range_deformationSpaceToBlowup_eq_compl_strictTransform_of_ofFiniteType`.

**lemma-sp-reduction**: --1 (b(M)) is the parent's names. c_{A,B} for f^! (--2, --3) and the transitivities (--4, --5) are not formalized for smooth f. The only analogue is the closed-immersion mate `Etale.derivedExtendScalarsUpperShriekMap` with its counit lemma.

No clause in this chapter is best stated by a Mathlib declaration (theorem-sp-qbar would only need `Adjunction` packaging).
## g7 — chap-Constructibility-of-f (39 clauses)

Verdicts: parent-name 28, project 3, not-formalized 4, different-route 3, inline 1.
Lean revision: weil-conjectures 94ce2d8. None of the names cited for this chapter contain `sorry` or `axiom`. Several of these
parents have a single clause that repeats the parent statement, which is phrased on the étale site.
For those clauses the parent's names are reused (verdict parent-name), as the sibling clauses in
this chapter already do.

### Per parent

- **definition-exceptional-base-change-finite**: `rightDerivedUpperShriekBaseChangeMap` is the mate
  of inv(Ex_!), the same definition as the blueprint's.
- **lemma-affine-space-etale-localization**: Lean follows the blueprint. It builds p_d^! = p_d^*(d)[2d]
  from the P^1 adjunction, the affine-line chart and induction on d.
  - Base change of the unit and counit (clauses 2 and 3) is stated as the mate β being an
    isomorphism (`affineSpaceAdjunction_baseChange`), not as literal equations of counits.
  - Clause 4 (u^*f^! ≅ (fu)^!) is the parent's existence name.
  - Clause 5 (counit formula) is stated by `Etale.existsUnique_etaleAmbientAdjointLocalityIso`.
  - Clause 6 (cocycle condition for u u') appears only in that theorem's docstring proof, so it is
    not formalized.
- **proposition-exceptional-inverse-image-smooth-morphism** (clauses 1–3): Lean takes a different
  route.
  - Smooth duality is proved without orientation, via EtaleSmoothDuality, AffineLine/AffineSpace
    smooth duality and gluing over charts (`satisfiesSmoothDuality_chart`).
  - It shows that ω is a shifted rank-one local system and that the canonical tensor map is an
    isomorphism.
  - It never identifies (f^!N)|_U with e^*p_d^*N(d)[2d] or ω|_U with Λ(d)[2d]. The twist only
    appears later, in global smooth purity (`nonempty_iso_dualizingComplex_twistShift`), which is
    downstream of this proposition and already on other nodes.
- **lemma-smooth-morphisms-locally-constant-sheaves**: single clause; the parent's name states it
  on the étale site.
- **proposition-projection-formula-rational-coefficients**: two clauses, matching the parent's
  E / Q̄_ℓ names (tensor closure, then the projection formula).
- **theorem-f-shriek-ell-adic-coefficients**: clauses 1–3 each match one coefficient ring's
  restriction theorem.
  - The Lean proof takes a different route from the blueprint's chart argument (i^!, p^!).
  - Rf_!(c) restricted to Dbc is i_! ⋙ Rp_*, which is a left adjoint, and Dbc detects
    isomorphisms in Loc(Dbc).
  - The restricted adjunction (clause 4) appears only as a `have` inside these proofs, so its
    verdict is inline.
- **lemma-projection-formula-integral-coefficients**, **proposition-direct-image-along-open-immersion**:
  one name per clause; the clauses match the coefficient-ring split.
- **lemma-extension-across-finite-subset**: single clause, parent-name, with a caveat (medium
  confidence). The Lean form is abstract:
  - U is given rather than produced;
  - the smooth or locally-constant input becomes the hypothesis `ha`;
  - b is proper rather than projective.
- **lemma-universal-homeomorphism-base**: parent-name, stated over Set.univ (no open U′ or U) and
  without passing to reduced fibre products.
- **lemma-generic-smooth-open**: parent-name, same statement as the parent.
- **proposition-open-direct-image-preserves-finite**: single clause, parent-name, same statement as
  the parent.
- **theorem-f-shriek-finite-coefficients**: clause 1 is the parent's `ProEtale.constructibleFiniteTor_rightDerivedUpperShriek`
  and clause 2 is the parent's restricted adjunction. Lean transports the étale f^! through ν^*
  instead of using the Brown adjoint.
- **lemma-class-diagonal-projective-line**: parent-name (s_1 = s_2 = id, and the diagonal ideal is
  invertible).
- **lemma-cohomology-projective-line-trace**: `geoP1Cohomology` bundles the decomposition
  isomorphism, its base change and the base change of the trace. `geoP1DecompositionMap` and
  `geoP1Trace` are the definitions. All four clauses are covered by the parent's names.
- **proposition-adjunction-projective-line**:
  - Covered: the adjunction (`exists_projectiveLineAdjunction`, clause 1) and base change of the
    counit (`projectiveLineAdjunctionBaseChange_of_isNormalized`, clause 3). The more specific
    `projectiveLineCounit_baseChange` is on no node.
  - Not formalized: base change of the unit (clause 2) and compatibility of the unit and counit
    with change of finite coefficients (clauses 4 and 5).
- **lemma-cycle-class-cartier-divisor**: has more specific declarations than the parent's bundled
  `exists_geoCartierCycleClass`:
  - `geoCartierCanonicalClass_chern` (clause 1);
  - `geoCartierCanonicalClass_scalar` and `geoCartierCanonicalClass_pullback` (clause 2).

  These are new names, not yet on any node.

### Clauses best stated by Mathlib declarations
None. Every name in this chapter is a project declaration (namespaces `AlgebraicGeometry.Etale`,
`AlgebraicGeometry.ProEtale(.CondensedRing)`, `AlgebraicGeometry`). Nothing comes from proetale.

### Group 8

Lean sources: weil-conjectures `94ce2d8` (slopmaster2) plus its proetale dependency; Mathlib `0df444a`.
Every name below was checked: the declaration exists in the cited file, and the name is not on any
other blueprint node, except for names flagged as parent names or conflicts.

**Marker `RESTRICTION-ONLY`.** Some clauses are marked `partial` only because Lean assumes a
hypothesis the blueprint does not, and the parent's own Lean names already assume it. Examples:
`[GeometricallyConnected]` in ch. 19, only the affine line / rank 1 in the Fourier chapter,
geometrically connected curves in the weight bound, bounded-constructible coefficients in
`lemma-passing-schematic-closure`. Apart from that hypothesis the statement matches. The evidence
string of each such clause starts with `RESTRICTION-ONLY`. If the coordinator accepts these
restrictions, as was done for the parents, those `partial_names` can be promoted to `names`.

Some `partial` entries list one of the parent's own names in `partial_names`. That is deliberate:
the name states only part of the clause.

**Sorry.** Many files in the project contain `sorry`; for example WeilFourierInversion,
SmoothPurity and PoincareDuality/Pod*. The cited files were checked directly. The one cited
declaration proved by `sorry` is `WeilComplex.nonempty_iso_affineFourierTransform_comp_self`, the
rank-n Fourier inversion. It is only mentioned and is not proposed. Whether the top-level theorems
depend on a `sorry` through Poincaré duality or smooth purity was not checked, because there was
no build to run `#print axioms`.

### Proof of the Weil conjectures (ch. 19)

- **theorem-weil-conjectures-smooth-proper-schemes**: the Lean route differs. Lean does not build
  `P_i` from the reciprocal roots of `A` and `B`. `exists_isWeilFactorization_of_smoothProper`
  builds the factors for one prime `l0`. It uses the trace datum, Poincaré duality and
  universal purity (`exists_isWeilFactorization_of_prime`), then transfers to every other `l`
  through `IsWeilFactorization.unique`. Each clause has a precise declaration:
  - `IsIntegralFrobeniusFactor.unique` (--2) needs no smoothness hypothesis.
  - `existsUnique_isIntegralFrobeniusFactor` (--1).
  - `integral_frobenius_factors` (--3).
  - `weilBettiNumber` (--6) and `Polynomial.alternatingNatDegreeSum` (--14) are definitions.
  - `natDegree_eq_finrank_of_isIntegralFrobeniusFactor` and `weilBettiNumber_eq_finrank` (--8).
  - `betti_symmetry` (--9).
  - `endpoints_of_isIntegralFrobeniusFactor` (--10..13).

  Everything except --2 assumes `[GeometricallyConnected]`. Clauses 10-13 assume it in the
  blueprint as well, so they are `project`. The others are `partial` with `RESTRICTION-ONLY`.
  Clauses --4 and --5 are stated only by `riemann_hypothesis`, a parent name. Clauses --15 and
  --16 are stated by `weil_functional_equation`, a parent name. The more specific
  `reciprocity`, for --15, is already on `corollary-functional-equation` and is listed as a
  conflict.
- **lemma-reciprocal-roots-zeta**: different route. Lean proves `A = prod_odd P_i` and
  `B = prod_even P_i` from the integral factors and the uniqueness of the normalized presentation
  (`integral_recovery`, a parent name; `isNormalizedIntegralFraction_prod`). The weights of the
  roots of `A` and `B` then come from the Riemann hypothesis for the `P_i`.
  - --5 and --6 are `different-route`: no weight is chosen per root.
  - --3 is `Polynomial.ne_zero_of_mem_roots_reverse`.
  - --4 is `partial`: integrality is stated only for weight-stratum members.
  - --7 is `partial`: `realization_independence`, which is on no node, states it for the
    weight-i stratum.
- **corollary-point-count-estimates**: the two clauses are exactly the two parent names.
- **theorem-purity-higher-direct-images-under**: both clauses have declarations,
  `WeilSheaf.higherLowerShriekObjIsoOfIsProper` (--1) and `isPunctuallyPureOfWeight_higherLowerStar`
  (--2). The Lean proof of the lower weight bound is fibrewise, using proper base change and
  Poincaré duality on the fibres, not relative Verdier duality. For --3 ("mixed of a single
  weight"), Lean has only the "weights at most" direction.
- **lemma-reduced-fractions-integer-coefficients** and **lemma-hankel-rank-rationality**: each
  single clause is the parent statement, so the verdict is `parent-name`.

### Fourier transform

The Lean Fourier theory for Weil complexes exists only on the affine line over `k0` (r = 1,
S = Spec k0). A second library, `AlgebraicGeometry.Etale.*` under `FourierTransform/`, handles
rank r, a general base S and arbitrary pairings, but only with torsion coefficients.

- **proposition-fourier-inversion--2**: the parent name `nonempty_iso_fourierTransform_comp_self`
  covers r = 1 (`RESTRICTION-ONLY`). The rank-n Weil version is `sorry`.
- **lemma-fourier-transform-constant-sheaf--1/--2**: the parent names, exact.
- **proposition-base-change-fourier-inversion--1**: only the torsion étale version
  `Etale.nonempty_iso_fourierTransform_baseChange` exists, so `partial`.
- **lemma-artin-schreier-character-sheaf**: --1 is covered by the parent names. Lean uses the
  k0-cover `u^q - u = x`. --4 and --5 (normalization at zero) are not formalized: Lean has only
  `Nonempty` isomorphisms and no specified trivialization.
- **lemma-integral-linear-character**: --1 and --2 are `partial`. The Weil statements are r = 1
  (parent names) and the general-r statements are torsion only (`Etale.*`). --3 (the
  trace-map normalization) is not formalized.
- **lemma-largest-punctual-subsheaf** (affine line only):
  - --2: the kernel is written inline.
  - --3: `partial` (the kernel is punctual; maps from punctual sheaves to `j_*N` vanish).
  - --4 and --5: not formalized.
- **lemma-perverse-sheaves-curve--1**: no t-structure is constructed, and the Lean module
  docstring says the heart has no abelian structure. Only the orthogonality axiom exists
  (a parent name), so `partial`.
- **lemma-simple-objects--2**: `partial` through `eq_zero_or_isIso_of_mono_middleExtension`,
  which covers subobjects only. Lean proves simplicity directly instead.

### Deligne–Laumon (curves and general)

The Lean route follows the blueprint throughout. Most clauses repeat their single-clause parent,
so the verdict is `parent-name`.

- `theorem-weight-bound-curve--1/--2`: `partial`, `RESTRICTION-ONLY` (Lean adds geometric
  connectedness of U and C).
- `lemma-weight-bound-constant-extension--1`: `partial`. Lean proves only one direction of the
  iff, for abstract Frobenius modules.
- `theorem-weight-bound-affine-line--1`: `project`, through the more specific degree-1 lemma
  `LisseOnDenseOpen.hasWeightsAtMostOver_compactlySupportedCohomology_one`.
- `lemma-weight-bounds-partitions--2`: uses the universal-in-K form, as the sibling --1 already
  does.

### Pure sheaves on curves

The L²-weight `ν` is defined only for Weil sheaves, not complexes (`traceEnergy`, `l2Weight`).

- `lemma-bounds-squared-traces--3`: `partial`. Only the boundary-energy case
  `exists_boundaryEnergy_le` exists.
- `lemma-bounds-squared-traces--4`: `partial`.
- `proposition-twisting-weight-zero-adding-dual--7`: holds because `realEnvelope` is defined as a
  biproduct, so the name is Mathlib's `biprod.inl_fst`.
- The other clauses are parent names.

### Picard scheme

- `corollary-torsion-jacobian-field-extension--4`: inline in the proof of
  `pic_proper_ntorsion_torsion`.
- `proposition-h-1-curve-tate-module--2`: `partial`. Only compatibility of the finite levels is
  stated; there is no inverse-limit isomorphism.
- `definition-relative-picard-functor--2`: Lean uses `Functor.RepresentableBy` directly.
- `lemma-coherent-base-change-invertible-sheaves--2`: `partial`. Lean's own docstring says the
  derived base-change map is not available; the closest name is already on sibling --1, so it is
  listed as a conflict.

### Nagata / Chow

The Lean route follows the blueprint. All clauses are parent names, except:

- `lemma-products-composites-u-admissible-blow--1`: `partial`. Lean covers two blow-ups; the
  extension to finitely many is not stated.
- `lemma-passing-schematic-closure--1/--2`: `partial`, `RESTRICTION-ONLY`. Lean covers bounded
  constructible coefficients and general proper refinements.

### Cohomology of torsion sheaves on curves

- `proposition-smooth-proper-curves-torsion-prime--1..5`: precise sub-declarations exist below
  the bundled parent name:
  - `IsConnectedCurve.sheafH_rootsOfUnitySheaf_of_isProper` (--1, --3, --4).
  - `exists_addEquiv_sheafH_rootsOfUnitySheaf_one_jacobian` (--2).
  - `rootsOfUnityCohomologyMap_baseChangeField` (--5).
- `lemma-normalization-constant-sheaf`:
  - --1 is `partial`: coefficients `Λ/l` only, and no description of the cokernel by branches.
  - --2 is not formalized, as the Lean docstring says.
- `proposition-p-torsion-smooth-proper-curve--4`: `partial`. The bound `dim ≤ g` is missing.

### Clauses best stated by Mathlib declarations

- `proposition-twisting-weight-zero-adding-dual--7`: `CategoryTheory.Limits.biprod.inl_fst`. The
  sheaf E is defined as the biproduct `F⁰ ⊞ (F⁰)^∨`, so the direct-summand claim is this
  general lemma.
- `definition-relative-picard-functor--2`: `CategoryTheory.Functor.RepresentableBy`. This is the
  general notion of a representing object, so the match is not very specific.

No other clause in g8 is best stated by Mathlib. The candidates were checked, for example the
reciprocal-root facts and the Hankel-rank facts. They are stated in the project, sometimes in its
`WeilConjectures/Mathlib/` upstreaming folder, such as `Polynomial.alternatingNatDegreeSum`,
`Polynomial.monic_reverse_of_coeff_zero_eq_one` and `Matrix.bddAbove_range_rank_submatrix_iff`.
Those folder entries are project names, not Mathlib names.

## Every clause

### chap-Abelian-varieties

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `definition-abelian-variety--2` | inside a proof |  | The definition is used in place as the expression `𝟙 A ^ n` (Mathlib's monoid structure on Hom(X, A)), with no separate def. |
| `definition-abelian-variety--4` | inside a proof |  | Symmetry is written out as an isomorphism [-1]^*L ≅ L where it is needed. There is no def. |
| `lemma-rigidity--1` | the declaration's own name | `AlgebraicGeometry.exists_mem_and_comp_eq_of_subsingleton_image` | Single clause equal to the parent. WeilConjectures/AlgebraicGeometry/AbelianVariety/Rigidity.lean:245 exists_mem_and_comp_eq_of_subsingleton_image is the parent's name. It assumes X proper, geometrically connected and geometrically reduced (weaker than geomet… |
| `lemma-symmetric-ample-sheaf--1` | the declaration's own name | `AlgebraicGeometry.IsAbelianVariety.exists_isClosedImmersion_projectiveSpace`<br>`AlgebraicGeometry.IsAbelianVariety.exists_isAmple`<br>`AlgebraicGeometry.IsAbelianVariety.isAmple_symmetrisation`<br>`AlgebraicGeometry.IsAbelianVariety.nonempty_iso_overPullback_inv_symmetrisation` | The single clause is the whole parent statement. WeilConjectures/AlgebraicGeometry/AbelianVariety/Projective.lean:79 exists_isClosedImmersion_projectiveSpace states 'projective'. :97 exists_isAmple gives an ample L, :112 isAmple_symmetrisation shows L ⊗ [-1]^… |
| `proposition-integral-tate-module--1` | the declaration's own name | `AlgebraicGeometry.IsAbelianVariety.nonempty_addEquiv_torsionBy_points` | WeilConjectures/AlgebraicGeometry/AbelianVariety/GeometricPoints.lean:189 nonempty_addEquiv_torsionBy_points: for n prime to char K and any algebraically closed K' ⊇ K, the n-torsion of A(K') is ≃+ (Fin (2g) → ZMod n). Take n = ℓ^n. This is a parent name. Con… |
| `proposition-integral-tate-module--3` | not formalized |  | Not needed. T_ℓ A ≅ Z_ℓ^{2g} is obtained directly from divisibility and torsion counts (AddCommGroup.tateModule.nonempty_linearEquiv_of_natCard_eq). |
| `proposition-integral-tate-module--4` | partial |  | AbelianVariety/TateModule.lean:366 geometricPointsAddEquiv (parent): σ acts on A(K̄) by group automorphisms, so it commutes with [ℓ] and preserves A[ℓ^n](K̄). TateModule.lean:417 galoisRepresentation (parent) is the componentwise action. TateModule.lean:428 c… |
| `proposition-no-frobenius-fixed-vector--1` | partial |  | WeilConjectures/AlgebraicGeometry/AbelianVariety/TateModule.lean:454 (parent name) shows that geometric Frobenius F fixes no nonzero t ∈ T_ℓ A. WeilConjectures/AlgebraicGeometry/AbelianVariety/RationalTateModule.lean:91 eq_zero_of_galoisRepresentation_frobeni… |
| `proposition-no-frobenius-fixed-vector--2` | partial |  | WeilConjectures/AlgebraicGeometry/AbelianVariety/TateModule.lean:470 eq_zero_of_map_geometricFrobenius_eq_self (parent name): (V_ℓ A)^F = 0 for m = 1 only. There is no F^m version. Conflicts: AlgebraicGeometry.IsAbelianVariety.eq_zero_of_map_geometricFrobeniu… |
| `proposition-no-frobenius-fixed-vector--3` | partial |  | WeilConjectures/AlgebraicGeometry/AbelianVariety/RationalTateModule.lean:103 bijective_rationalTateModuleGaloisMap_frobenius_sub_id (parent name): σ - 1 is bijective on V_ℓ A. :121 frobeniusSubOneLinearEquiv packages it as a linear automorphism. :73 finiteDim… |
| `proposition-no-frobenius-fixed-vector--4` | not formalized |  | Not used. The Lean development does not extend scalars on V_ℓ A of an abelian variety. |
| `theorem-theorem-cube--1` | the declaration's own name | `AlgebraicGeometry.nonempty_iso_of_nonempty_iso_overPullback_slices` | Single clause equal to the parent. WeilConjectures/AlgebraicGeometry/TheoremOfCube.lean:333 nonempty_iso_of_nonempty_iso_overPullback_slices: invertible M, N isomorphic on the three slices give M ≅ N. The clause is the case N = O. Z is only assumed connected;… |

### chap-Algebraic-groups-in-characteristic-zero

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `lemma-cartan-s-criterion--1` | the declaration's own name | `LieSubalgebra.isSolvable_of_trace_mul_eq_zero` | Single clause equal to the parent. WeilConjectures/Mathlib/Algebra/Lie/CartanCriterion.lean:52 LieSubalgebra.isSolvable_of_trace_mul_eq_zero (project file in the Mathlib-mirror dir): tr(XY)=0 for X ∈ derivedSeries 1, Y ∈ A ⇒ A solvable, char 0, finite-dimensi… |
| `lemma-connected-components-images-homomorphisms--2` | the declaration's own name | `AlgebraicGeometry.isClosed_range_of_isMonHom`<br>`AlgebraicGeometry.exists_isMonHom_imageι` | WeilConjectures/AlgebraicGeometry/GroupScheme/Basic.lean:874 isClosed_range_of_isMonHom: for G of finite type and G' locally of finite type, the image of a homomorphism is closed. This is the topological content. WeilConjectures/AlgebraicGeometry/GroupScheme/… |
| `lemma-connected-components-images-homomorphisms--3` | the declaration's own name | `AlgebraicGeometry.GrpObj.isIso_left_of_differential_bijective`<br>`AlgebraicGeometry.GeneralLinearGroup.eq_of_le_of_lieSubalgebra_eq` | WeilConjectures/AlgebraicGeometry/GroupScheme/Lie/Dimension.lean:205 GrpObj.isIso_left_of_differential_bijective: K → G a closed-immersion homomorphism, G connected of finite type, char 0, differential bijective ⇒ iso, i.e. K = G. This is the clause. WeilConj… |
| `lemma-engel-s-theorem--1` | the declaration's own name | `LieSubalgebra.exists_forall_apply_eq_zero_and_isNilpotent`<br>`LieModule.isNilpotent_iff_forall'` | WeilConjectures/Mathlib/Algebra/Lie/Engel.lean:40 LieSubalgebra.exists_forall_apply_eq_zero_and_isNilpotent, first conjunct: for nontrivial finite-dimensional M and A consisting of nilpotent endomorphisms, ∃ v ≠ 0 with X v = 0 for all X ∈ A. Exactly the claus… |
| `lemma-engel-s-theorem--2` | different route |  | Lean never builds the basis. Nilpotence of A comes directly from LieAlgebra.isNilpotent_iff_forall applied to ad X, which is nilpotent by LieAlgebra.isNilpotent_ad_of_isNilpotent, instead of by triangular matrices. |
| `lemma-engel-s-theorem--3` | the declaration's own name | `LieSubalgebra.exists_forall_apply_eq_zero_and_isNilpotent` | WeilConjectures/Mathlib/Algebra/Lie/Engel.lean:40, second conjunct `LieRing.IsNilpotent A`. Exactly the clause. Conflicts: LieSubalgebra.exists_forall_apply_eq_zero_and_isNilpotent |
| `lemma-engel-s-theorem--4` | Mathlib | `LieAlgebra.isSolvable_of_isNilpotent` | Mathlib/Algebra/Lie/Nilpotent.lean:739 `instance (priority := 100) LieAlgebra.isSolvable_of_isNilpotent (L) [LieModule.IsNilpotent L L] : LieAlgebra.IsSolvable L`. This is an explicitly named instance: a nilpotent Lie algebra is solvable. Combined with clause… |
| `lemma-killing--1` | the declaration's own name | `LieAlgebra.HasTrivialRadical.killingForm_nondegenerate` | WeilConjectures/Mathlib/Algebra/Lie/CartanCriterion.lean:86 LieAlgebra.HasTrivialRadical.killingForm_nondegenerate: finite-dimensional, char 0, trivial radical ⇒ Killing form nondegenerate. Exactly the clause. It wraps Mathlib's LieAlgebra.IsKilling.killingFo… |
| `lemma-killing--2` | project lemma | `LieAlgebra.HasTrivialRadical.derivedSeries_eq_top` | WeilConjectures/Mathlib/Algebra/Lie/CartanCriterion.lean:94 `theorem derivedSeries_eq_top [HasTrivialRadical k L] : derivedSeries k L 1 = ⊤` inside `namespace LieAlgebra.HasTrivialRadical` (k a char-0 field, L finite-dimensional). derivedSeries k L 1 = ⁅L, L⁆… |
| `lemma-stable-subspaces-center--1` | the declaration's own name | `AlgebraicGeometry.GeneralLinearGroup.invariant_iff_differential_invariant` | WeilConjectures/AlgebraicGeometry/GroupScheme/GeneralLinear/Lie.lean:757 (`_root_.AlgebraicGeometry.GeneralLinearGroup.invariant_iff_differential_invariant`). For a connected G locally of finite type, a rational representation r and U ≤ m → k: U is stable und… |
| `lemma-stable-subspaces-center--2` | the declaration's own name | `AlgebraicGeometry.GeneralLinearGroup.range_lieAlgebraMap_identityComponent_center` | WeilConjectures/AlgebraicGeometry/GroupScheme/GeneralLinear/ClosedSubgroup/Comparison.lean:217 range_lieAlgebraMap_identityComponent_center: for connected V(I) ⊆ GL_n (algebraically closed, char 0), the range of Lie(Z(G)°) → Lie(G) is the centre of Lie(G). Th… |

### chap-Cohomology-of-torsion-sheaves-on-curves

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `lemma-cohomology-multiplicative-group--1` | the declaration's own name | `AlgebraicGeometry.IsCurve.rightDerived_globalSections_comparisonUpperStar_gmSheaf` | WeilConjectures/AlgebraicGeometry/Curve/GmCohomology.lean:91 (parent name), first conjunct: for C a smooth separated curve of finite type over an algebraically closed field, H^1(C_proet, nu^* G_m) = Pic(C) (via the comparison RGamma(C_proet, nu^*F) = RGamma(C… |
| `lemma-cohomology-multiplicative-group--2` | the declaration's own name | `AlgebraicGeometry.IsCurve.rightDerived_globalSections_comparisonUpperStar_gmSheaf` | GmCohomology.lean:91 (parent name), second conjunct: H^q(C_proet, nu^* G_m) = 0 (IsZero) for q >= 2. The etale vanishing is IsCurve.subsingleton_sheafH_gmSheaf_of_smooth (cited in the docstring at :54) and the last conjunct of the parent name sheafH_gmSheaf_o… |
| `lemma-normalization-constant-sheaf--1` | partial |  | WeilConjectures/AlgebraicGeometry/Curve/Reductions.lean:661 (parent's only name): for a reduced curve X over an algebraically closed field, nu : X' -> X finite surjective and an iso over a dense open V (the properties of the normalization used), there is a mo… |
| `lemma-normalization-constant-sheaf--2` | not formalized |  | Field-extension invariance of curve cohomology is proved by other means (e.g. bijective_cohomologyMap_constantModSheaf_of_isProper, bijective_fieldExtensionCohomologyMap_of_isAffine). |
| `proposition-cohomology-smooth-affine-curve--1` | the declaration's own name | `AlgebraicGeometry.Scheme.residueSequence_exact`<br>`AlgebraicGeometry.Scheme.gysinH2_eq_zero_iff` | WeilConjectures/AlgebraicGeometry/FundamentalGroup/ResidueSequenceGysin.lean:521 Scheme.residueSequence_exact (parent name): 0 -> H^1(C, Z/N) -> H^1(U, Z/N) -> H^0(D, Z/N(-1)) -> H^2(C, Z/N) exact (restriction injective; exact at H^1(U) and at the residue ter… |
| `proposition-p-torsion-smooth-proper-curve--4` | partial |  | WeilConjectures/AlgebraicGeometry/Curve/SmoothCalculations.lean:397 finite_sheafH_constantModSheaf_of_isProper (parent name): H^q(C, F_r) finite for every q and every prime r (r = p included, via Artin-Schreier); :547 bijective_cohomologyMap_constantModSheaf_… |
| `proposition-smooth-proper-curves-torsion-prime--1` | project lemma | `AlgebraicGeometry.IsConnectedCurve.sheafH_rootsOfUnitySheaf_of_isProper` | WeilConjectures/AlgebraicGeometry/Curve/RootsOfUnityCohomology.lean:139 (namespace AlgebraicGeometry.IsConnectedCurve, :115) sheafH_rootsOfUnitySheaf_of_isProper, part 1: H^0(C, mu_n) -> O(C)^x is injective with image the units a with a^n = 1 (= mu_n(k) since… |
| `proposition-smooth-proper-curves-torsion-prime--2` | project lemma | `AlgebraicGeometry.IsConnectedCurve.exists_addEquiv_sheafH_rootsOfUnitySheaf_one_jacobian` | WeilConjectures/AlgebraicGeometry/Curve/RootsOfUnityCohomology.lean:359 exists_addEquiv_sheafH_rootsOfUnitySheaf_one_jacobian: there is an abelian variety J of dimension g with Pic^0(C) = J(k) and an isomorphism H^1(C, mu_n) = J[n](k) compatible with the Kumm… |
| `proposition-smooth-proper-curves-torsion-prime--3` | project lemma | `AlgebraicGeometry.IsConnectedCurve.sheafH_rootsOfUnitySheaf_of_isProper` | RootsOfUnityCohomology.lean:139 sheafH_rootsOfUnitySheaf_of_isProper, part 3: the Kummer boundary delta^2 : Pic(C) -> H^2(C, mu_n) is surjective and there is a unique deg_n : H^2(C, mu_n) = Z/n with deg_n(delta^2 [L]) = deg L mod n. Same declaration as --1 an… |
| `proposition-smooth-proper-curves-torsion-prime--4` | project lemma | `AlgebraicGeometry.IsConnectedCurve.sheafH_rootsOfUnitySheaf_of_isProper` | RootsOfUnityCohomology.lean:139 sheafH_rootsOfUnitySheaf_of_isProper, part 4: H^q(C, mu_n) = 0 (Subsingleton) for q > 2; part 3 gives the degree-two normalization deg_n(delta^2[L]) = deg L mod n stated in this clause. |
| `proposition-smooth-proper-curves-torsion-prime--5` | project lemma | `AlgebraicGeometry.IsConnectedCurve.rootsOfUnityCohomologyMap_baseChangeField` | RootsOfUnityCohomology.lean:278 rootsOfUnityCohomologyMap_baseChangeField: for k -> k' algebraically closed, the pullback maps H^q(C, mu_n) -> H^q(C_{k'}, mu_n) are bijective for all q and are the inclusion mu_n(k) -> mu_n(k'), base change of line bundles on … |

### chap-Constructibility-of-f

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `definition-exceptional-base-change-finite--1` | the declaration's own name | `AlgebraicGeometry.Etale.rightDerivedUpperShriekBaseChangeMap` | WeilConjectures/SixFunctors/Etale/Derived/UpperShriekCanonicalMaps.lean:146 defines Rf^! ⋙ Lg'^* ⟶ Lg^* ⋙ Rf'^! as mateEquiv of inv of the compact-support base change map Ex_! under Rf_! ⊣ Rf^! and Rf'_! ⊣ Rf'^!, i.e. exactly the transpose (6.2). Finite Λ, ét… |
| `lemma-affine-space-etale-localization--1` | the declaration's own name | `AlgebraicGeometry.Etale.nonempty_rightDerivedLowerShriek_adjunction_affineSpace` | WeilConjectures/SixFunctors/Etale/Derived/SmoothDuality/AffineSpaceTwistAdjunction.lean:208: Nonempty (Rp_{d!} ⊣ Lp_d^* ⋙ twistShift d) for 𝔸^d_S ⟶ S, normalized Tate twist, exponent of Λ invertible on S; docstring 'This is also clause 1 of sk-lem-geo-affine-… |
| `lemma-affine-space-etale-localization--2` | the declaration's own name | `AlgebraicGeometry.Etale.affineSpaceAdjunction_baseChange` | WeilConjectures/SixFunctors/Etale/Derived/SmoothDuality/SmoothBaseChange.lean:664, second conjunct: for every cartesian square of 𝔸^d_S ⟶ S (quasi-compact compactifiable base change) the base change map Lg'^* Rp^! ⟶ Rp'^! Lg^* (rightDerivedUpperShriekBaseChan… |
| `lemma-affine-space-etale-localization--3` | the declaration's own name | `AlgebraicGeometry.Etale.affineSpaceAdjunction_baseChange` | Same declaration as --2 (SmoothBaseChange.lean:664): the mate formulation covers unit and counit simultaneously (docstring 'compatibility of the unit and counit of Ra_! ⊣ Ra^! with base change'). No separate unit statement. |
| `lemma-affine-space-etale-localization--4` | the declaration's own name | `AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_comp_leftDerivedUpperStar_of_etale` | WeilConjectures/SixFunctors/Etale/Derived/EtaleLocalizationUpperShriek.lean:60: for u étale, separated, quasi-compact, Nonempty (Rf^! ⋙ Lu^* ≅ R(u ≫ f)^!), by uniqueness of right adjoints from Ru_! ⊣ Lu^* and R(u≫f)_! ≅ Ru_! ⋙ Rf_!. |
| `lemma-affine-space-etale-localization--5` | project lemma | `AlgebraicGeometry.Etale.existsUnique_etaleAmbientAdjointLocalityIso` | WeilConjectures/AlgebraicGeometry/Etale/EtaleAmbientAdjointLocality.lean:453: for finite A, u étale separated finite type, Noetherian U,X,S, any right adjoints F of Rf_!(c), G of R(fu)_!(d): ∃! e : F ⋙ u^* ≅ G with R(fu)_!(e_K) ≫ ε^G_K = (comparison R(fu)_! ≅… |
| `lemma-affine-space-etale-localization--6` | not formalized |  | Not needed by the Lean proofs, which use existence (Nonempty) of the localization iso only. |
| `lemma-class-diagonal-projective-line--1` | the declaration's own name | `AlgebraicGeometry.Etale.projectiveLineTrace_diagonal`<br>`AlgebraicGeometry.Etale.projectiveLineTrace_diagonal_swap`<br>`AlgebraicGeometry.Etale.projectiveLine_diagonal_ker_isInvertible` | WeilConjectures/EtaleCohomology/Purity/Smooth/ProjectiveLineDiagonalIntegrals.lean:288 (s_1 = id) and :337 (s_2 = id); WeilConjectures/AlgebraicGeometry/ProjectiveLineDiagonalCartier.lean:35 (ideal of the diagonal of P^1_S invertible, for every S — hence stab… |
| `lemma-cohomology-projective-line-trace--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.geoP1DecompositionMap`<br>`AlgebraicGeometry.ProEtale.geoP1Cohomology` | WeilConjectures/AlgebraicGeometry/Geo/GeoP1Cohomology.lean:361 defines the map Λ_S ⊕ Λ_S(-1)[-2] ⟶ Rp_*Λ from the unit and the Kummer Chern class (pro-étale, via comparison of the étale map); :1019 geoP1Cohomology, first conjunct: IsIso (geoP1DecompositionMap… |
| `lemma-cohomology-projective-line-trace--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.geoP1Cohomology` | GeoP1Cohomology.lean:1019, conjunct `(geoP1Pullback A g).map (geoP1DecompositionMap .. S ..) ≫ geoP1UnitExchange A g = geoP1SourceMap .. g .. ≫ geoP1DecompositionMap .. S' ..` for every g : S' → S of Noetherian schemes. |
| `lemma-cohomology-projective-line-trace--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.geoP1Trace` | GeoP1Cohomology.lean:459: geoP1Trace = b.inv ≫ biprod.snd, projection onto the constant summand of the twisted decomposition b : Λ(1)[2] ⊞ Λ ≅ Rp_*Λ(1)[2]; geoP1Cohomology fixes b.hom = geoP1TwistedMap. |
| `lemma-cohomology-projective-line-trace--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.geoP1Cohomology` | GeoP1Cohomology.lean:1019, last conjunct: (geoP1Pullback A g).map (geoP1Trace .. S ..) ≫ unit pullback iso = geoP1TwistExchange .. g .. ≫ geoP1Trace .. S' .. for every Noetherian g. |
| `lemma-cycle-class-cartier-divisor--1` | project lemma | `AlgebraicGeometry.ProEtale.geoCartierCanonicalClass_chern` | WeilConjectures/AlgebraicGeometry/Geo/GeoCartierCanonicalChern.lean:203: GeoCartierChernEquation for geoCartierCanonicalClass (the class c_D : i_*Λ_D ⟶ Λ_Z(1)[2] as an Ext², defined at GeoCartierCanonicalClass.lean:32, a parent name) — its composite with Λ_Z … |
| `lemma-cycle-class-cartier-divisor--2` | project lemma | `AlgebraicGeometry.ProEtale.geoCartierCanonicalClass_scalar`<br>`AlgebraicGeometry.ProEtale.geoCartierCanonicalClass_pullback` | WeilConjectures/AlgebraicGeometry/Cartier/CartierReductionScalar.lean:59 (GeoCartierScalarCompatibility for any ring hom φ : A →+* B of finite rings) and WeilConjectures/AlgebraicGeometry/Cartier/CartierReductionPullback.lean:110 (for a cartesian square with … |
| `lemma-extension-across-finite-subset--1` | the declaration's own name | `AlgebraicGeometry.Etale.HasDirectImageBaseChangeOnPlus.of_finite_boundary` | WeilConjectures/SixFunctors/Etale/Derived/Finiteness/Deligne/FiniteBoundary.lean:78. Caveat (as on the parent, confidence medium): abstract form — the open U ⊆ S over which Z is finite is given, not produced, smoothness of X/S and local constancy of F are rep… |
| `lemma-generic-smooth-open--1` | the declaration's own name | `AlgebraicGeometry.exists_isFinite_universallyInjective_smooth_dense` | WeilConjectures/AlgebraicGeometry/GenericFiber/RadicialSmoothing.lean:103: nonempty open U, finite surjective universally injective π : S' → U with S' integral, reduced dense open immersion V ⊆ X' smooth over S', F\|_V finite locally constant, and every gener… |
| `lemma-projection-formula-integral-coefficients--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isIso_projectionMap_of_localizingBoundedConstructible_padicIntegersRingObj` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/ProjectionFormulaAdic.lean:125: projection formula map iso on Loc(Dbc(-,O_E)) for proper p. |
| `lemma-smooth-morphisms-locally-constant-sheaves--1` | the declaration's own name | `AlgebraicGeometry.Etale.exists_nonempty_open_smooth_directImage_lisse_baseChange` | WeilConjectures/AlgebraicGeometry/SmoothGenericDirectImage.lean:118: S integral finite type over k, f separated smooth, L finite locally constant Z/ℓ-sheaf on X_ét: ∃ nonempty open U, Rf_{U*}L bounded with finite locally constant cohomology and derivedBaseCha… |
| `lemma-universal-homeomorphism-base--1` | the declaration's own name | `AlgebraicGeometry.Etale.HasConstructibleDirectImageBaseChangeOn.of_isFinite_of_surjective` | WeilConjectures/SixFunctors/Etale/Derived/Finiteness/Deligne.lean:429: π finite, surjective, universally injective (finite universal homeomorphism); bounded constructibility + base change of Rj'_*(F\|X') over S' implies it over S. Caveat: stated with Set.univ… |
| `proposition-adjunction-projective-line--1` | the declaration's own name | `AlgebraicGeometry.Etale.exists_projectiveLineAdjunction` | WeilConjectures/SixFunctors/Etale/Derived/SmoothDuality/ProjectiveLineAdjunction.lean:244: ∃ adj : Rq_! ⊣ Lq^* ⋙ (1)[2] with counit = projectiveLineCounit (projection formula + trace). Unit built from the diagonal class (exists_projectiveLineAdjunction_of_cla… |
| `proposition-adjunction-projective-line--2` | not formalized |  | Lean only needs counit compatibility (it determines the mate β, projectiveLineBaseChange_of_adjunction); unit compatibility is formally implied but not stated. |
| `proposition-adjunction-projective-line--3` | the declaration's own name | `AlgebraicGeometry.Etale.projectiveLineAdjunctionBaseChange_of_isNormalized` | SmoothDuality/ProjectiveLineAdjunctionBaseChange.lean:183: ProjectiveLineAdjunctionBaseChange Λ — for every g : S' → S, Ex_! ≫ Rq'_!(pullback/twist isos) ≫ ε'_{g^*K} = Lg^*(ε_K). More specific underlying lemma, not on any node: AlgebraicGeometry.Etale.project… |
| `proposition-adjunction-projective-line--4` | not formalized |  | Lean builds the adjunction separately for each finite Λ; no coefficient-change compatibility is used on the main line. |
| `proposition-adjunction-projective-line--5` | not formalized |  | As --4. |
| `proposition-direct-image-along-open-immersion--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightDerivedLowerStar_openImmersion_padicIntegersRingObj` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/LocalizingInputs.lean:227 (O_E): Rj_* preserves Dbc for a quasi-compact open immersion. |
| `proposition-direct-image-along-open-immersion--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightDerivedLowerStar_openImmersion_continuousMapRingObj` | LocalizingInputs.lean:353 (Λ = E). |
| `proposition-direct-image-along-open-immersion--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightDerivedLowerStar_openImmersion_padicAlgClRingObj` | LocalizingInputs.lean:476 (Λ = Q̄_ℓ). |
| `proposition-exceptional-inverse-image-smooth-morphism--1` | different route |  | Lean proves part (2) (tensor formula) orientation-free: EtaleSmoothDuality + AffineLine/AffineSpaceSmoothDuality (canonical tensor maps iso, ω a shifted rank-one local system), glued along étale-local charts V → 𝔸^d_U → U (Charts.lean), giving exists_dualizin… |
| `proposition-exceptional-inverse-image-smooth-morphism--2` | different route |  | See --1: orientation-free gluing of tensor-map isomorphisms; chart counits never made explicit. |
| `proposition-exceptional-inverse-image-smooth-morphism--3` | different route |  | Rank-one-ness of ω (clause --4, isInvertible_dualizingComplex / exists_dualizingComplex_iso_and_tensor) is proved without the twisted chart form; the twist is identified only later via the diagonal (smooth purity chapter). |
| `proposition-open-direct-image-preserves-finite--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedLowerStar`<br>`AlgebraicGeometry.ProEtale.projection_torAmplitudeIn_rightDerivedLowerStar_of_isOpenImmersion` | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/Stability.lean:131 (Rf_* preserves Dbc on X_proét) and :261 (open immersion j with d ≥ cd(j): Tor amplitude [a,b] ↦ [a,b+d]). The parent also lists torAmplitudeIn_rightDerivedLowerStar (:224, boun… |
| `proposition-projection-formula-rational-coefficients--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.tensor_mem_localizingBoundedConstructible_continuousMapRingObj`<br>`AlgebraicGeometry.ProEtale.CondensedRing.tensor_mem_localizingBoundedConstructible_padicAlgClRingObj` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/ProjectionFormulaField.lean:93 (Λ = E) and :171 (Λ = Q̄_ℓ): Dbc closed under ⊗ᴸ and A ⊗ᴸ B ∈ Loc(Dbc) for A,B ∈ Loc(Dbc); docstrings cite det-thm-sf-pf-field-tensor. |
| `proposition-projection-formula-rational-coefficients--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isIso_projectionMap_of_localizingBoundedConstructible_continuousMapRingObj`<br>`AlgebraicGeometry.ProEtale.CondensedRing.isIso_projectionMap_of_localizingBoundedConstructible_padicAlgClRingObj` | ProjectionFormulaField.lean:111 (E) and :189 (Q̄_ℓ): for proper p, (Rp_*A) ⊗ᴸ B ⟶ Rp_*(A ⊗ᴸ p^*B) iso for A ∈ Loc(Dbc(X)), B ∈ Loc(Dbc(Y)). |
| `theorem-f-shriek-ell-adic-coefficients--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightAdjoint_rightDerivedLowerShriekLocalizing_padicIntegersRingObj` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/ProperUpperShriekExistence.lean:183 (O_E): every right adjoint G of Rf_!(c) on Loc(Dbc(-,O_E)) maps Dbc(Y) into Dbc(X). |
| `theorem-f-shriek-ell-adic-coefficients--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightAdjoint_rightDerivedLowerShriekLocalizing_continuousMapRingObj` | ProperUpperShriekExistence.lean:145 (Λ = E, a finite subextension of Q̄_ℓ/Q_ℓ). |
| `theorem-f-shriek-ell-adic-coefficients--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightAdjoint_rightDerivedLowerShriekLocalizing_padicAlgClRingObj` | ProperUpperShriekExistence.lean:222 (Λ = Q̄_ℓ). |
| `theorem-f-shriek-ell-adic-coefficients--4` | inside a proof |  | The restricted adjunction is the input (a `have`) of the Lean proof rather than its consequence. |
| `theorem-f-shriek-finite-coefficients--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.constructibleFiniteTor_rightDerivedUpperShriek` | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/UpperShriekFiniteness.lean:211: pro-étale Rf^! maps Dctf(Y,A) into Dctf(X,A) (via exists_shift_constructibleTorAmplitudeIn_rightDerivedUpperShriek, :191, uniform shift c). |
| `theorem-f-shriek-finite-coefficients--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.DerivedCategoryFiniteTor.rightDerivedLowerShriekAdjunction` | UpperShriekFiniteness.lean:247: the adjunction Rf_! ⊣ Rf^! between the full subcategories Dctf, obtained by restricting the pro-étale exceptional adjunction (rightDerivedUpperShriekAdjunction) since both functors preserve Dctf. |

### chap-Constructible-complexes

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `corollary-coefficient-heart-b--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.constantModelBoundedConstructible_field_triangulated` | Parent's AlgebraicGeometry.ProEtale.constantModelBoundedConstructible_field_triangulated (WeilConjectures/AlgebraicGeometry/Coefficient/CoefficientHeartTriangulated.lean:116): Dbc(X,E or Qbar) is a triangulated subcategory. |
| `corollary-coefficient-heart-b--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.coefficientHeart_generation` | Parent's AlgebraicGeometry.ProEtale.coefficientHeart_generation (WeilConjectures/AlgebraicGeometry/Coefficient/CoefficientHeartGeneration.lean:177): generation by finitely many cones of shifted a_!L with L lisse. |
| `definition-lisse-sheaves--2` | not formalized |  | Definition not formalized. |
| `lemma-bounds-finite-reductions--1` | project lemma | `AlgebraicGeometry.ProEtale.integral_finite_constructibility` | WeilConjectures/AlgebraicGeometry/Integral/Finite/IntegralFiniteConstructibility.lean:128: given K_1 bounded constructible, every derived reduction K_n is bounded constructible (first conjunct); second conjunct propagates finite local models on a fixed stratu… |
| `lemma-bounds-finite-reductions--2` | project lemma | `AlgebraicGeometry.ProEtale.integral_finite_residue_tor` | WeilConjectures/AlgebraicGeometry/Integral/Finite/IntegralFiniteResidueTor.lean:450: a constructible complex L over O_E/pi^{n+1} whose residue reduction has cohomology in [a,b] has Tor amplitude in [a,b]; with integral_finite_residue_normalization (residue re… |
| `lemma-bounds-finite-reductions--3` | project lemma | `AlgebraicGeometry.ProEtale.integral_finite_tower_bounds` | WeilConjectures/AlgebraicGeometry/Integral/Finite/IntegralFiniteTowerBounds.lean:104: derived complete K whose integral levels lie in [a,b] with epimorphic top transitions has cohomology in [a,b]. The level hypotheses come from integral_finite_reduction_range… |
| `lemma-bounds-finite-reductions--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.integral_finite_levels` | Last conjunct of the parent's AlgebraicGeometry.ProEtale.integral_finite_levels (WeilConjectures/AlgebraicGeometry/Integral/Finite/IntegralFiniteLevels.lean:127-140): finite constant local models of the cohomology of K_1 on a stratum propagate to all K_n. Als… |
| `lemma-constructible-sheaves--1` | project lemma |  | WeilConjectures/AlgebraicGeometry/Coefficient/CoefficientHeartClosure.lean:476: for Lambda = E or Qbar and X noetherian, IsConstantModelConstructible is closed under kernels (second block, first conjunct). The name is on sibling --5. No more specific public d… |
| `lemma-constructible-sheaves--2` | project lemma |  | CoefficientHeartClosure.lean:476, closure under cokernels conjunct; name on sibling --5. Conflicts: AlgebraicGeometry.ProEtale.coefficientHeart_closure |
| `lemma-constructible-sheaves--3` | project lemma |  | CoefficientHeartClosure.lean:476, closure under extensions conjunct; name on sibling --5. Conflicts: AlgebraicGeometry.ProEtale.coefficientHeart_closure |
| `lemma-constructible-sheaves--4` | project lemma |  | CoefficientHeartClosure.lean:476, Nonempty (Abelian (ConstantModelConstructible ...)) conjunct; name on sibling --5. Conflicts: AlgebraicGeometry.ProEtale.coefficientHeart_closure |
| `lemma-continuity-ext-out-constructible-complex--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.constructible_ext_continuity` | Clause = whole lemma. Parent's AlgebraicGeometry.ProEtale.constructible_ext_continuity (WeilConjectures/AlgebraicGeometry/Constructible/ConstructibleExtContinuity.lean:208) states the continuity for E, Qbar and O_E for objects generated by extensions/shifts o… |
| `lemma-descent-finite-coefficient-field--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.coefficient_finite_descent_hom` | Parent's AlgebraicGeometry.ProEtale.coefficient_finite_descent_hom (WeilConjectures/AlgebraicGeometry/Coefficient/CoefficientFiniteDescentHom.lean:694) is the Hom-colimit bijection, clause (1). |
| `lemma-descent-finite-coefficient-field--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.coefficient_finite_descent_objects` | Parent's AlgebraicGeometry.ProEtale.coefficient_finite_descent_objects (WeilConjectures/AlgebraicGeometry/Coefficient/CoefficientFiniteDescentObjects.lean:347) is descent of objects, clause (2). |
| `lemma-descent-lisse-qbar-sheaves-finite--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.coefficient_finite_descent_lisse` | Clause = whole lemma; parent's AlgebraicGeometry.ProEtale.coefficient_finite_descent_lisse (WeilConjectures/AlgebraicGeometry/Coefficient/CoefficientFiniteDescentLisse.lean:430). |
| `lemma-flat-models-generators--2` | project lemma | `AlgebraicGeometry.Etale.exists_chain_opens_flat_isFiniteLocallyConstantSheaf`<br>`AlgebraicGeometry.etale_flatConstructible_orderedStratification` | WeilConjectures/SixFunctors/Etale/Derived/Stability/FlatModelGeneration.lean:155: a flat constructible sheaf on X_et (X noetherian, finite Lambda) has a finite chain of opens whose strata restrictions are finite locally constant, flat, with finite projective … |
| `lemma-flat-models-generators--3` | the declaration's own name | `AlgebraicGeometry.Etale.constructibleFiniteTor_eq_triangEnvelope_ctfGenerators_of_isNoetherian` | Parent's AlgebraicGeometry.Etale.constructibleFiniteTor_eq_triangEnvelope_ctfGenerators_of_isNoetherian (WeilConjectures/SixFunctors/Etale/Derived/Stability/FlatModelGeneration.lean:292): Dctf (etale site, noetherian X) is the triangulated envelope (shifts, e… |
| `lemma-integral-models--3` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_leftDerivedUpperStar_obj` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleUpperStar.lean:119 (_of_scheme: for any condensed ring Lambda, in particular O_E, and any morphism of schemes, Lg^* preserves Dbc) is exactly the clause but is on lemma-inverse-imag… |
| `lemma-integral-models--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_tensorObj` | Parent's AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_tensorObj (WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleTensorObj.lean:204) is the general tensor preservation under LisseTensorHypotheses. The O_E special… |
| `lemma-integral-models--5` | project lemma |  | Open part: WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructible.lean:233 (j_! preserves Dbc), on lemma-inverse-image-tensor-product--3; closed part: BoundedConstructibleClosedPushforward.lean:104 (Ri_* preserves Dbc), on lemma-invers… |
| `lemma-integral-models--6` | project lemma | `WeilConjectures.SixFunctors.integral_models_generators` | WeilConjectures/SixFunctors/Integral/IntegralModelsGenerators.lean:1884, first conjunct: every K in Dbc(X,E) (X separated finite type over k, char k != l) lies in the smallest triangulated, iso-closed subcategory containing the E-extensions of a_!L0 with L0 l… |
| `lemma-integral-models--7` | project lemma | `WeilConjectures.SixFunctors.integral_models_generators` | IntegralModelsGenerators.lean:1884, second conjunct: every K in Dbc(X,Qbar_l) lies, for some finite E, in the triangulated envelope of Qbar tensor_E E tensor_{O_E} a_!L0. Same bundle as proposed for --6; if names must be unique, give it to one of --6/--7 and … |
| `lemma-sections-support-closed-subscheme--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.formal_closed_support_derived` | Parent's AlgebraicGeometry.ProEtale.CondensedRing.formal_closed_support_derived (WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/Formal/FormalClosedSupportDerived.lean:183) and formal_closed_support_adjunction (FormalClosedSupportAdjunction.lean:415… |
| `lemma-sections-support-closed-subscheme--2` | the declaration's own name |  | The same parent names state the Hom-complex isomorphism HomComplex(i_*A, I) ~ HomComplex(A, Gamma_Z I) for K-injective I (FormalClosedSupportDerived.lean:198-210, FormalClosedSupportAdjunction.lean:436-440), i.e. RHom_X(i_*N,K) = RHom_Z(N, RGamma_Z K). |
| `lemma-sections-support-closed-subscheme--3` | inside a proof |  | Inline in the continuity-of-Ext stratum proof. |
| `proposition-ctf-equals-bc--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.localizingClosure_ctf_equals_bc` | Clause = whole proposition; parent's AlgebraicGeometry.ProEtale.localizingClosure_ctf_equals_bc (WeilConjectures/AlgebraicGeometry/ProEtaleCoefficients/LocalizingClosureCtfEqualsBc.lean:537). |
| `proposition-inverting-ell--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.integral_scalar_map_eq` | Parent's AlgebraicGeometry.ProEtale.CondensedRing.integral_scalar_map_eq (WeilConjectures/AlgebraicGeometry/ContinuousIntegralScalarMapEq.lean:69): two morphisms of Dbc(X,O_E) (X noetherian) with equal image in E-coefficients agree after multiplying by l^n. W… |
| `proposition-local-structure-integral-constructible-complexes--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.integral_local_structure` | Clause = whole proposition; parent's AlgebraicGeometry.ProEtale.integral_local_structure (WeilConjectures/AlgebraicGeometry/Integral/IntegralLocalStructure.lean:820). WARNING: its proof is `sorry` (line 841). |

### chap-Construction-of-f

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `corollary-ambient-ind-derived--1` | project lemma | `DerivedCategory.homologyProperty_isTriangulated`<br>`DerivedCategory.homologyProperty_sigma`<br>`DerivedCategory.homologyProperty_truncLE`<br>`DerivedCategory.homologyProperty_truncGE` | General statements about DerivedCategory.homologyProperty P (complexes with all H^n in P), specialised to P = IsIndConstructibleModuleObject R once IndCons is a weak Serre class closed under sums (IsIndConstructibleHeart): WeilConjectures/Mathlib/Algebra/Homo… |
| `corollary-ambient-ind-derived--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.localizingClosure_boundedConstructible_le` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/CompactConstructible.lean:164: given IsIndConstructibleHeart R, (boundedConstructible R).localizingClosure <= homologyProperty (IsIndConstructibleModuleObject R), i.e. Loc(Dbc) is contained in Dic. |
| `corollary-ind-heart-b--1` | project lemma | `AlgebraicGeometry.ProEtale.indConstructible_ext_vanishing_and_sums` | WeilConjectures/AlgebraicGeometry/IndConstructibleExtStatement.lean:62, first conjunct: for C constructible (E or Qbar_l), given the bound d of the uniform Ext lemma for constructible targets, Hom(C, B[q]) is trivial for q > d and all ind-constructible B (doc… |
| `corollary-ind-heart-b--2` | project lemma | `DerivedCategory.compactFor_singleFunctor_of_homFactorsThroughFilteredColimits` | WeilConjectures/CategoryTheory/DerivedCategory/CompactOfBoundedExt.lean:384: if maps out of s factor through filtered colimits, Hom(s, -[n]) commutes with direct sums of objects of C (CompactFor = every map to the coproduct is a finite sum through the summand… |
| `corollary-proper-direct-image-finite-coefficients-localizing--1` | partial |  | Clause text is identical to the parent. The parent name (FiniteCoefficient/Derived/LowerStarCoproducts.lean:147) gives only the direct sums part, for complexes with cohomology of etale origin (Loc(Dctf) is inside by DerivedCategory.isLocalizing_etaleOriginHom… |
| `definition-ind-constructible-sheaves--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.IsIndConstructibleModuleObject` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/CompactConstructible.lean:93: abbrev = ObjectProperty.ind (IsConstructibleModuleObject R); Mathlib CategoryTheory.ObjectProperty.ind (Mathlib/CategoryTheory/ObjectProperty/Ind.lean:44) is 'X is a filte… |
| `definition-ind-constructible-sheaves--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.IsIndConstructibleModuleObject` | Same declaration (CompactConstructible.lean:93). In Lean a full subcategory is an ObjectProperty, and IndCons(X,Lambda) is (IsIndConstructibleModuleObject R).FullSubcategory (Mathlib ObjectProperty.FullSubcategory); no separate declaration names the notation. |
| `definition-localizing-subcategory--1` | the declaration's own name | `CategoryTheory.ObjectProperty.localizingClosure`<br>`AlgebraicGeometry.ProEtale.DerivedCategory.localizingConstructibleFiniteTor`<br>`AlgebraicGeometry.ProEtale.CondensedRing.localizingBoundedConstructible` | Clause text is identical to the parent. WeilConjectures/CategoryTheory/Triangulated/LocalizingClosure.lean:75 (smallest localizing = triangulated, iso-closed, coproduct-closed property containing P); SixFunctors/ProEtale/FiniteCoefficient/Derived/UpperShriekL… |
| `lemma-checking-isomorphisms-constructible-complexes--1` | the declaration's own name | `CategoryTheory.NatTrans.isIso_app_of_localizingClosure` | Clause text is identical to the parent. WeilConjectures/CategoryTheory/Triangulated/LocalizingDetermination.lean:148. |
| `lemma-hypotheses-brown-representability--1` | inside a proof |  | Implicit in the Lean types (universe bookkeeping). |
| `lemma-hypotheses-brown-representability--2` | project lemma | `CategoryTheory.ObjectProperty.isLocalizing_localizingClosure` | WeilConjectures/CategoryTheory/Triangulated/LocalizingClosure.lean:97: Loc(P) is localizing, and IsLocalizing (:56) extends P.IsTriangulated, so the full subcategory inherits the triangulated structure (Mathlib's instances for triangulated ObjectProperty). |
| `lemma-hypotheses-brown-representability--3` | project lemma | `CategoryTheory.ObjectProperty.hasCoproducts_fullSubcategory` | WeilConjectures/CategoryTheory/Triangulated/LocalizingClosure.lean:107 (named instance): a localizing property of a category with coproducts has coproducts, computed in C; preservesColimitsOfShape_ι (:113) says they are the ambient ones. |
| `lemma-hypotheses-brown-representability--4` | project lemma | `CategoryTheory.ObjectProperty.isIdempotentComplete_localizingClosure` | WeilConjectures/CategoryTheory/Triangulated/LocalizingClosureGeneration.lean:49: Loc(P) of a pretriangulated category with coproducts is idempotent complete (via Pretriangulated.isIdempotentComplete_of_hasCoproducts; docstring det-brown-hypotheses-ambient). A… |
| `lemma-hypotheses-brown-representability--5` | project lemma | `AlgebraicGeometry.ProEtale.DerivedCategory.essentiallySmall_constructibleFiniteTor`<br>`AlgebraicGeometry.ProEtale.CondensedRing.exists_skeleton_boundedConstructible` | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/EssentiallySmall.lean:87 (named instance: Dctf(X, Lambda) essentially small, finite Lambda, X qcqs; det-brown-hypotheses-small); SixFunctors/ProEtale/ModuleObject/Derived/UpperShriekLocalizing.lea… |
| `lemma-hypotheses-brown-representability--6` | the declaration's own name | `AlgebraicGeometry.ProEtale.DerivedCategory.compactlyGeneratesLocalizingClosure_constructibleFiniteTor` | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/UpperShriekLocalizing.lean:97, first conjunct: CompactlyGeneratesLocalizingClosure (BrownRepresentability/RightAdjoint.lean:221: small skeleton, compactness, detection of zero objects) for Dctf, f… |
| `lemma-hypotheses-brown-representability--7` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.compactlyGenerates_padicIntegersRingObj` | UpperShriekLocalizingEllAdic.lean:199 (O_E). |
| `lemma-hypotheses-brown-representability--8` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.compactlyGenerates_continuousMapRingObj` | UpperShriekLocalizingEllAdic.lean:123 (E, including Q_l). |
| `lemma-hypotheses-brown-representability--9` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.compactlyGenerates_padicAlgClRingObj` | UpperShriekLocalizingEllAdic.lean:269 (Qbar_l). |
| `lemma-inverse-image-tensor-product--5` | not formalized |  | The pro-etale l-adic development works only with uncompleted module objects, so this comparison is not needed by the parent's Lean proof. |
| `lemma-proper-direct-image-unbounded-complexes--1` | partial |  | WeilConjectures/CategoryTheory/DerivedCategory/CoproductsOfHomologyProperty.lean:85: abstract amplitude dévissage: if a triangulated Phi sends P[0] into degrees <= d, it sends bounded complexes with cohomology in P and in degrees <= n into degrees <= n + d (e… |
| `lemma-proper-direct-image-unbounded-complexes--2` | different route |  | Lean reduces sums of unbounded complexes to uniformly bounded families via left completeness of D(X_proet) (countable AB4*), not via the finite window (5.6). |
| `lemma-proper-direct-image-unbounded-complexes--3` | partial |  | WeilConjectures/CategoryTheory/DerivedCategory/CoproductsOfHomologyProperty.lean:271: for a weak Serre class P closed under sums, a triangulated G preserving countable products, not lowering degrees, of amplitude <= d on P[0] and commuting with sums of P[0]'s… |
| `lemma-structure-integral-constructible-complexes--1` | partial |  | WeilConjectures/ConstructibleSheaf/ProEtaleModule/DerivedCategory.lean:261 (named instance: Dbc(X, O_E) is a triangulated subcategory, X noetherian); SixFunctors/ProEtale/ModuleObject/Derived/UpperShriekLocalizing.lean:200 (constructible module objects are es… |
| `lemma-structure-integral-constructible-complexes--2` | project lemma |  | WeilConjectures/ConstructibleSheaf/ProEtaleModule/Def.lean:88: by definition, M is constructible iff there is a finite stratification on whose strata M is pro-etale locally finitely presented over R (for R = O_{E,X}, locally O_{E,S} (x) P with P finitely pres… |
| `lemma-structure-integral-constructible-complexes--3` | partial |  | WeilConjectures/AlgebraicGeometry/IntegralCtfEqualsBc.lean:62, first conjunct: every constructible module over O_E (and Z_l) has Tor amplitude in [-1, 0] (global, not just on strata). Not stated: dualizability on strata or that the dual has Tor amplitude [0, … |
| `lemma-uniform-bound-proper-direct-image--1` | partial |  | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/ProperLowerStarEllAdicBound.lean:73,96: there is d with Rp_*(N[0]) in degrees <= d for all constructible N (E, uniformly in E; Qbar_l); the bound is existential (2*dim via the O_E case, not 2d+1 explic… |
| `lemma-uniform-bound-proper-direct-image--2` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.isIso_sigmaComparison_rightDerivedLowerStar_singleFunctor` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/ProperLowerStarHeart.lean:140: for any qcqs f, Rf_* commutes with direct sums of module objects placed in degree 0 (any modules, more general than IndCons; equivalent to each R^q f_* commuting with sum… |
| `lemma-uniform-ext-bound--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.hasUniformConstructibleExtBound_continuousMapRingObj` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/CompactConstructibleEllAdic.lean:925: HasUniformConstructibleExtBound for E (k finite or separably closed), i.e. for C constructible there is N with Hom(C, B[n]) = 0 for n <= N and all constructible B … |
| `lemma-uniform-ext-bound--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.hasUniformConstructibleExtBound_padicAlgClRingObj` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/CompactConstructibleEllAdic.lean:1010: the same for Qbar_l. |
| `proposition-compactness-finite-coefficients--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.DerivedCategory.isCompactObj_of_constructibleFiniteTor` | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/CompactLocalizing.lean:209: objects of Dctf are compact in Loc(Dctf). The 'small skeleton is a set of compact generators' half is UpperShriekLocalizing.lean:97 (CompactlyGeneratesLocalizingClosure… |
| `proposition-compactness-finite-coefficients--2` | partial |  | WeilConjectures/CategoryTheory/CompactObjectFiniteThickFactor.lean:40: in a compactly generated triangulated category, every compact object is a retract of an object of the thick envelope of a finite sum of generators (Stacks 09SN/09SP; docstring det-ctf-fini… |
| `proposition-compactness-proper-direct-image--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isCompactObj_boundedConstructible_padicIntegersRingObj` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/UpperShriekLocalizingEllAdic.lean:184: every object of Dbc(X, O_E) is compact in Loc(Dbc(X, O_E)) (k finite or separably closed). |
| `proposition-compactness-proper-direct-image--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.properLowerStarHypotheses_padicIntegersRingObj` | UpperShriekLocalizingEllAdic.lean:215: ProperLowerStarHypotheses (UpperShriekLocalizing.lean:301), second conjunct: the restriction of Rp_* to Loc(Dbc(Z, O_E)) preserves direct sums. |
| `proposition-composition-open-restriction-compactifications-f--3` | partial |  | WeilConjectures/TraceFormula/PointNormalizationBaseChange.lean:435 (namespace AlgebraicGeometry.ProEtale.CondensedRing, then Correspondence, lines 69/284): left unit law R(1 >> a)^! = Ra^! >> R(1)^! = Ra^! is the identity, for boundedConstructibleUpperShriekC… |
| `proposition-composition-open-restriction-compactifications-f--6` | the declaration's own name | `AlgebraicGeometry.Etale.existsUnique_rightDerivedUpperShriekOfCompactificationIso` | WeilConjectures/SixFunctors/Etale/Derived/UpperShriekLocality.lean:219: for finite Lambda and any compactification c = (i, p) of f, the unique iso Rf^! = Rp^! >> Di^* compatible with the adjunctions (Rp^! >> Di^* is right adjoint to Di_! >> Rp_*, def rightDer… |
| `proposition-composition-open-restriction-compactifications-f--7` | partial |  | WeilConjectures/SixFunctors/Etale/Derived/UpperShriekLocality.lean:162 (j^* Rf^! = R(j >> f)^! for a quasi-compact open immersion j) and :64 (a map of D(X_et, Lambda) whose restrictions along a jointly surjective family are isos is an iso; docstring cites det… |
| `proposition-composition-open-restriction-compactifications-f--8` | partial |  | WeilConjectures/SixFunctors/Etale/Derived/UpperShriekLocality.lean:141: u^* Rf^! = Rf_V^! v^* for open immersions v : V -> Y, u : X_V -> X with u >> f = f_V >> v (finite Lambda, etale). Combined with isIso_of_isIso_mapDerivedCategoryUpperStar_map_of_jointlySu… |
| `proposition-construction-independence-rf-shriek--1` | project lemma | `AlgebraicGeometry.ProEtale.isTriangulated_rightDerivedLowerShriekOfCompactification`<br>`AlgebraicGeometry.ProEtale.CondensedRing.isTriangulated_boundedConstructibleLowerShriekOfCompactification` | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/LowerShriekTriangulated.lean:56 (named instance: Rf^c_! = Rfbar_* j_! on D(X_proet) is triangulated, finite A); SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleTriangulatedBasic.lean… |
| `proposition-construction-independence-rf-shriek--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.DerivedCategory.localizingConstructibleFiniteTor_lowerShriek`<br>`AlgebraicGeometry.ProEtale.CondensedRing.lowerShriek_continuousMapRingObj`<br>`AlgebraicGeometry.ProEtale.CondensedRing.lowerShriek_padicIntegersRingObj`<br>`AlgebraicGeometry.ProEtale.CondensedRing.lowerShriek_padicAlgClRingObj` | Third conjunct of each: UpperShriekLocalizing.lean:124 (finite A) and LowerShriekLocalizingHypotheses (ModuleObject/Derived/UpperShriekLocalizing.lean:131) proved in UpperShriekLocalizingEllAdic.lean:153,230,294: the restriction of Rp_* o j_! to Loc preserves… |
| `proposition-construction-independence-rf-shriek--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.DerivedCategory.localizingConstructibleFiniteTor_lowerShriek` | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/UpperShriekLocalizing.lean:124, second conjunct: Rf_!(c) maps Dctf(X_proet, Lambda) into Dctf(Y_proet, Lambda) for finite Lambda. More specific helper: AlgebraicGeometry.ProEtale.constructibleFini… |
| `proposition-construction-independence-rf-shriek--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.lowerShriek_padicIntegersRingObj` | UpperShriekLocalizingEllAdic.lean:230, second conjunct of LowerShriekLocalizingHypotheses: Rp_* o j_! maps Dctf = Dbc(X, O_E) into Dbc(Y, O_E). |
| `proposition-construction-independence-rf-shriek--5` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.lowerShriek_continuousMapRingObj` | UpperShriekLocalizingEllAdic.lean:153, second conjunct (E). |
| `proposition-construction-independence-rf-shriek--6` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.lowerShriek_padicAlgClRingObj` | UpperShriekLocalizingEllAdic.lean:294, second conjunct (Qbar_l). |
| `proposition-construction-independence-rf-shriek--7` | partial |  | WeilConjectures/SixFunctors/Etale/Derived/LowerShriekIndependenceUnbounded.lean:209 (etale, finite Lambda, unbounded D: Rf_!(c) = Rf_!(d) via the common refinement Compactification.inf c d); SixFunctors/ProEtale/ModuleObject/BaseChangeTheorems/LowerShriek/Com… |
| `proposition-construction-independence-rf-shriek--8` | partial |  | WeilConjectures/SixFunctors/Etale/Derived/LowerShriekCoherence.lean:376: for three compactifications c1, c2, c3, iso(c1,c2) >> iso(c2,c3) = iso(c1,c3) (docstring: 'the cocycle condition', sk-prop-sf-comp-coherence), on D^+ of the etale site, finite Lambda. Pa… |
| `proposition-forgetting-supports-composition--1` | the declaration's own name | `AlgebraicGeometry.Etale.compactificationForgetSupports`<br>`AlgebraicGeometry.Etale.derivedOpenImmersionLowerShriekToLowerStar` | WeilConjectures/SixFunctors/Etale/Derived/LowerShriekProjectionProper.lean:83: eta for a compactification c = (i, g): Rg_* applied to D(i_!) -> Ri_*, followed by Ri_* >> Rg_* -> Rf_*. LowerShriekToLowerStar.lean:82: D(j_!) -> Rj_*, the transpose under D(j^*) … |
| `proposition-forgetting-supports-composition--2` | partial |  | Independence: parent name, SixFunctors/Etale/Derived/CompactificationRefinementLowerStar.lean:222 (Rf_!(c) = Rf_!(d) followed by eta_d is eta_c; finite Lambda). Composition square: only for proper p, f and compatible compactifications d, e, AlgebraicGeometry/… |
| `proposition-ind-constructible-sheaves--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.indHeart_fullFaithfulness` | WeilConjectures/AlgebraicGeometry/SixFunctors/IndHeartFullFaithfulness.lean:153, via def IndHeartFullFaithfulnessAssertions (:104): constructibles are finitely presentable, and there is a realization functor Phi : Ind(Cons) -> Mod with Ind.yoneda >> Phi = inc… |
| `proposition-ind-constructible-sheaves--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.indHeart_fullFaithfulness` | Same theorem (IndHeartFullFaithfulness.lean:153), last conjunct of IndHeartFullFaithfulnessAssertions (:104): Phi.essImage M <-> ObjectProperty.ind (constructible) M. Same name as clause --1 (one theorem states both). |
| `proposition-ind-constructible-sheaves--3` | project lemma | `AlgebraicGeometry.ProEtale.indConstructible_filteredColimits_and_sums`<br>`AlgebraicGeometry.ProEtale.indConstructible_filteredColimits_and_sums_padicAlgCl` | WeilConjectures/AlgebraicGeometry/SixFunctors/IndConstructibleFilteredColimits.lean:155 (E) and :233 (Qbar_l): first conjunct, for every small filtered diagram B of ind-constructible modules and colimit cocone c, c.pt is ind-constructible (docstring cites sk-… |
| `proposition-ind-constructible-sheaves--4` | project lemma | `CategoryTheory.ObjectProperty.ind_isClosedUnderColimitsOfShape_discrete` | WeilConjectures/CategoryTheory/ObjectProperty/IndHeart.lean:394: if objects of P are finitely presentable, P contains zero and is closed under extensions, then ind P is closed under direct sums (docstring: det-ind-heart-filtered-colimits). Specialises to cons… |
| `proposition-ind-constructible-sheaves--5` | project lemma | `CategoryTheory.ObjectProperty.ind_isClosedUnderKernels` | WeilConjectures/CategoryTheory/ObjectProperty/IndHeart.lean:330: P <= finitely presentable and P closed under kernels => ind P closed under kernels (docstring: det-ind-heart-kernels-cokernels). For the coefficient rings this is a field of the parent names isI… |
| `proposition-ind-constructible-sheaves--6` | project lemma | `CategoryTheory.ObjectProperty.ind_isClosedUnderCokernels` | WeilConjectures/CategoryTheory/ObjectProperty/IndHeart.lean:353: same for cokernels (det-ind-heart-kernels-cokernels). |
| `proposition-ind-constructible-sheaves--7` | project lemma | `AlgebraicGeometry.ProEtale.indConstructible_of_shortExact`<br>`AlgebraicGeometry.ProEtale.indConstructible_of_shortExact_padicAlgCl` | WeilConjectures/AlgebraicGeometry/SixFunctors/IndConstructibleExtensions.lean:217 (E) and :259 (Qbar_l): in a short exact sequence with ind-constructible X1 and X3, X2 is ind-constructible (docstring cites sk-prop-ind-heart-extensions). General form: Category… |
| `proposition-ind-constructible-sheaves--8` | not formalized |  | Lean never uses the Grothendieck abelian structure of IndCons; it works in the ambient module category. |
| `proposition-ind-constructible-sheaves--9` | Mathlib | `CategoryTheory.ObjectProperty.preservesKernels_ι`<br>`CategoryTheory.ObjectProperty.preservesCokernels_ι` | Mathlib/CategoryTheory/ObjectProperty/Kernels.lean:110,158 (namespace CategoryTheory.ObjectProperty): for P closed under kernels (resp. cokernels), the inclusion P.ι preserves kernels (resp. cokernels); for an additive functor of abelian categories this is ex… |
| `proposition-proper-base-change-localizing-categories--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_of_localizing_continuousMapRingObj`<br>`AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_of_localizing_padicAlgClRingObj`<br>`AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_of_localizingBoundedConstructible_padicIntegersRingObj` | Clause text is identical to the parent. LocalizingInputs.lean:332,456 and ProjectionFormulaAdic.lean:101 (E, Qbar_l, O_E). Not found for finite coefficients A on Loc(Dctf). Unused related names: CondensedRing.isIso_baseChangeMap_of_localizing_padicIntegersRin… |
| `proposition-proper-direct-image-extension-zero--1` | partial |  | Parent names, first conjunct: LocalizingInputs.lean:310,434,189: Rp_* maps Loc(Dbc(X)) into Loc(Dbc(Y)) for E, Qbar_l, O_E (exactness: Rp_* is triangulated, instance CondensedRing.isTriangulated_rightDerivedLowerStar, Localizing.lean:104). No statement found … |
| `proposition-proper-direct-image-extension-zero--2` | project lemma |  | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/LowerStarCoproducts.lean:147: for proper p, Rp_* commutes with coproducts of pro-etale complexes with cohomology of etale origin; Loc(Dctf) lies in that class by DerivedCategory.isLocalizing_etale… |
| `proposition-proper-direct-image-extension-zero--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.localizingBoundedConstructible_rightDerivedLowerStar_padicIntegersRingObj` | LocalizingInputs.lean:189, second conjunct: R(p_*) PreservesCoproductsOn Loc(Dbc(X, O_E)). (Also properLowerStarHypotheses_padicIntegersRingObj, parent name of proposition-compactness-proper-direct-image.) |
| `proposition-proper-direct-image-extension-zero--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.localizingBoundedConstructible_lowerStar_lowerShriek_continuousMapRingObj` | LocalizingInputs.lean:310, first conjunct, PreservesCoproductsOn Loc(Dbc(X, E)). |
| `proposition-proper-direct-image-extension-zero--5` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.localizingBoundedConstructible_lowerStar_lowerShriek_padicAlgClRingObj` | LocalizingInputs.lean:434, first conjunct (Qbar_l). |
| `proposition-proper-direct-image-extension-zero--6` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.localizingClosure_boundedConstructible_openImmersionLowerShriek`<br>`AlgebraicGeometry.ProEtale.localizingClosure_constructibleFiniteTor_openImmersionLowerShriek` | Third conjunct: OpenLowerShriekLocalizing.lean:65 (ModuleObject, any condensed ring Lambda: j_! maps Loc(Dbc(U)) into Loc(Dbc(X))) and FiniteCoefficient/Derived/OpenLowerShriekLocalizing.lean:98 (finite Lambda, Loc(Dctf)). j_! is triangulated (mapDerivedCateg… |
| `proposition-proper-direct-image-extension-zero--7` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.localizingClosure_boundedConstructible_openImmersionLowerShriek`<br>`AlgebraicGeometry.ProEtale.localizingClosure_constructibleFiniteTor_openImmersionLowerShriek` | Second conjunct of the same two theorems: D(j_!) preserves coproducts (proved by an anonymous instance from j_! being a left adjoint). |
| `proposition-proper-direct-image-extension-zero--8` | project lemma | `AlgebraicGeometry.ProEtale.constructibleFiniteTor_mapDerivedCategory_openImmersionLowerShriek` | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/OpenLowerShriekLocalizing.lean:58: j_! carries Dctf(U_proet, Lambda) into Dctf(X_proet, Lambda) for finite Lambda. The l-adic case is CondensedRing.boundedConstructible_openImmersionLowerShriek_ob… |
| `theorem-compactness-rational-coefficients--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isCompactObj_boundedConstructible_continuousMapRingObj`<br>`AlgebraicGeometry.ProEtale.CondensedRing.isCompactObj_boundedConstructible_padicAlgClRingObj` | Clause text is identical to the parent. WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/UpperShriekLocalizingEllAdic.lean:109,257: objects of Dbc are compact in Loc(Dbc) for E and Qbar_l (k finite or separably closed). The 'more precisely' family st… |
| `theorem-existence-exceptional-inverse-image--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.rightDerivedUpperShriekLocalizing`<br>`AlgebraicGeometry.ProEtale.rightDerivedUpperShriekLocalizingAdjunction` | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/UpperShriekLocalizing.lean:218,225: f^! : Loc(Dctf(Y)) -> Loc(Dctf(X)) and the adjunction Rf_! -\| f^! (finite Lambda). The l-adic existence is in the parent names exists_rightAdjoint_rightDerived… |
| `theorem-existence-exceptional-inverse-image--2` | Mathlib | `CategoryTheory.Adjunction.isTriangulated_rightAdjoint` | Mathlib/CategoryTheory/Triangulated/Adjunction.lean:60 (namespace CategoryTheory.Adjunction): the right adjoint of a triangulated functor (adjunction compatible with shifts) is triangulated. Used by the anonymous instance (rightDerivedUpperShriekLocalizing ..… |
| `theorem-existence-exceptional-inverse-image--3` | project lemma | `CategoryTheory.Adjunction.existsUnique_iso_comp_counit` | WeilConjectures/CategoryTheory/Triangulated/BrownRepresentability/RightAdjoint.lean:160: two right adjoints of F are isomorphic by a unique iso compatible with the counits (docstring det-sf-existence-brown (3)). Also the last conjunct of the parent names exis… |
| `theorem-existence-exceptional-inverse-image--4` | project lemma | `CategoryTheory.ObjectProperty.preservesColimitsOfShape_of_localizingClosureLift_adjunction` | WeilConjectures/CategoryTheory/Triangulated/BrownRepresentability/RightAdjoint.lean:309: if P1, P2 compactly generate their localizing closures and Phi maps P1 into P2, every right adjoint of Phi : Loc(P1) -> Loc(P2) preserves coproducts (docstring det-sf-exi… |

### chap-Nagata-compactification-and-Chows-lemma

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `corollary-extension-proper-target--1` | the declaration's own name | `AlgebraicGeometry.exists_admissibleBlowup_extend_of_isProper` | WeilConjectures/Blowup/ProperTargetExtension.lean:76 (parent's only name): X qcqs, U dense quasi-compact open, y : Y -> S proper, f : U -> Y over S: there is a U-admissible blow-up B and g : Bl -> Y over S extending f on the preimage of U. Single clause = who… |
| `definition-quasi-domination--1` | the declaration's own name | `AlgebraicGeometry.QuasiDomination` | WeilConjectures/Blowup/QuasiDomination.lean:72 structure QuasiDomination (x : X -> S) (y : Y -> S) [IsSeparated y] (parent's only name): dense open U, S-map U -> Y with closed graph. Single clause = whole parent. |
| `lemma-affine-covers-dense-intersection--2` | the declaration's own name | `AlgebraicGeometry.AffineSpace.projectiveClosure_spec`<br>`AlgebraicGeometry.HasCompactification.of_isQuasiAffine` | WeilConjectures/Compactification/AffineProjective.lean:51 AffineSpace.projectiveClosure_spec (parent name): for an immersion U -> A^n_S, the scheme-theoretic image in P^n_S is a proper (projective) compactification of U -> S with U schematically dense; Compac… |
| `lemma-making-open-schematically-dense--1` | the declaration's own name | `AlgebraicGeometry.exists_admissibleBlowup_cartierBoundary`<br>`AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.isSchemeTheoreticallyDominant_compl_support` | WeilConjectures/Blowup/AdmissibleBlowup.lean:664 exists_admissibleBlowup_cartierBoundary (parent name): T qcqs, U quasi-compact: a U-admissible blow-up with an invertible ideal J whose support is exactly the complement of the preimage of U (effective Cartier … |
| `lemma-passing-schematic-closure--1` | partial | `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinementPushforward`<br>`AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinementPushforward_padicAlgCl` | RESTRICTION-ONLY (same restriction as the parent's names): WeilConjectures/SixFunctors/ProEtale/ModuleObject/BaseChangeTheorems/LowerShriek/CompactificationIndependence.lean:419 (parent names; the _padicAlgCl variant for Qbar_l): for a proper refinement h : Z… |
| `lemma-passing-schematic-closure--2` | partial | `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekRefinementIso`<br>`AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructibleLowerShriekRefinementIso` | RESTRICTION-ONLY (same restriction as the parent's names): CompactificationIndependence.lean:283 boundedConstructibleLowerShriekRefinementIso (parent name; ContinuousMapRingObj variant also a parent name): i_{1!} then Rp_{1*} = i_! then Rp_* along a refinemen… |
| `lemma-products-composites-u-admissible-blow--1` | partial |  | WeilConjectures/Blowup/Extension.lean:455 def IsAdmissible.mul (parent name): the product of two U-admissible centers is U-admissible; Blowup/AdmissibleBlowup.lean:276 Scheme.IdealSheafData.exists_blowup_mul_iso (parent name, declared with _root_.): Bl_{I*L} … |
| `proposition-compactifying-union-two-opens--1` | the declaration's own name | `AlgebraicGeometry.HasCompactification.of_two_open_cover` | WeilConjectures/Compactification/TwoOpen.lean:661 (parent's only name): S Noetherian, u : U -> S separated quasi-compact locally of finite type, U = O_1 u O_2 with O_1 n O_2 dense and each O_i -> S compactifiable: u is compactifiable. Single clause = whole pa… |
| `proposition-dense-compactifications-form-cofiltered-category--1` | the declaration's own name | `AlgebraicGeometry.Compactification.exists_isDense_isStrict_refinement` | WeilConjectures/Compactification/DenseCategory.lean:147 (parent name): every finite nonempty family of compactifications of a quasi-compact f has a common dense strict refinement (stronger: the family need not be dense). |
| `proposition-dense-compactifications-form-cofiltered-category--2` | the declaration's own name | `AlgebraicGeometry.Compactification.refinement_morphisms` | WeilConjectures/Compactification/StrictRefinement.lean:140 (parent name): for c dense (i schematically dominant) and h : c.Z -> d.Z over Y with c.i h = d.i: h is proper, h^{-1}(d.i(X)) = c.i(X), and h is unique. Exactly the clause. |
| `proposition-dense-compactifications-form-cofiltered-category--3` | the declaration's own name | `AlgebraicGeometry.Compactification.DenseCategory.isCofiltered_and_isThin` | WeilConjectures/Compactification/DenseCategory.lean:167 (parent name): for Y qcqs and f separated quasi-compact locally of finite type, the category of dense compactifications is cofiltered (and thin). |
| `proposition-relative-form-zariski-s-main--1` | the declaration's own name | `AlgebraicGeometry.Scheme.Hom.exists_isOpenImmersion_isAffineHom_of_locallyQuasiFinite` | WeilConjectures/Mathlib/AlgebraicGeometry/QuasiAffine.lean:62 (parent's only name): a separated quasi-compact locally quasi-finite morphism locally of finite type factors as an open immersion followed by an affine morphism (through f.normalization). Exactly t… |

### chap-Proof-of-the-Weil-conjectures

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `corollary-point-count-estimates--1` | the declaration's own name | `AlgebraicGeometry.Scheme.abs_pointCount_sub_le_sum_finrank` | WeilConjectures/ZetaFunction/HasseWeil.lean:302 abs_pointCount_sub_le_sum_finrank (parent name): for X0 smooth proper geometrically connected of dimension d >= 1, every l != p and n != 0, \|#X0(F_{q^n}) - (q^{dn}+1)\| <= sum_{0<i<2d} dim H^i_l * q^{in/2}. Cla… |
| `corollary-point-count-estimates--2` | the declaration's own name | `AlgebraicGeometry.Scheme.Hom.abs_pointCount_sub_le_two_mul_genus` | WeilConjectures/ZetaFunction/HasseWeil.lean:268 Hom.abs_pointCount_sub_le_two_mul_genus (parent name): smooth (rel. dim 1) proper geometrically integral curve of genus g, \|#C(F_{q^n}) - (q^n + 1)\| <= 2 g q^{n/2}. Lean assumes geometrically integral; for a s… |
| `lemma-hankel-rank-rationality--1` | the declaration's own name | `PowerSeries.exists_normalized_fraction_iff_finiteDimensional_shiftSpan`<br>`Matrix.bddAbove_range_rank_submatrix_iff` | WeilConjectures/ZetaLinearAlgebra/ShiftSpan.lean:257 exists_normalized_fraction_iff_finiteDimensional_shiftSpan (parent name): (1) <-> (3) (f B = A with B(0)=1 iff span of the shifted coefficient sequences is finite-dimensional). WeilConjectures/Mathlib/Linea… |
| `lemma-reciprocal-roots-zeta--1` | partial | `AlgebraicGeometry.Scheme.integral_recovery` | RESTRICTION-ONLY (same restriction as the parent's names: Lean assumes [GeometricallyConnected], the blueprint does not; otherwise exact): WeilConjectures/ZetaFunction/RealizationIndependence.lean:152 integral_recovery (parent name): for Z = A/B the normalize… |
| `lemma-reciprocal-roots-zeta--2` | partial | `AlgebraicGeometry.Scheme.integral_recovery` | RESTRICTION-ONLY (same restriction as the parent's names: Lean assumes [GeometricallyConnected], the blueprint does not; otherwise exact): WeilConjectures/ZetaFunction/RealizationIndependence.lean:152 integral_recovery (parent name): B.map = evenFrobeniusProd… |
| `lemma-reciprocal-roots-zeta--3` | project lemma | `Polynomial.ne_zero_of_mem_roots_reverse` | WeilConjectures/ZetaLinearAlgebra/ReciprocalRoots.lean:69 (namespace Polynomial, :46) ne_zero_of_mem_roots_reverse: a root of P.reverse (a reciprocal root) over a field is nonzero; proof is the blueprint's (constant coefficient of the reverse is the leading c… |
| `lemma-reciprocal-roots-zeta--4` | partial |  | WeilConjectures/ZetaLinearAlgebra/GaloisStrata.lean:149 (namespace Polynomial) isIntegral_of_mem_weilStratum: for C in Z[T] with C(0)=1, every element of a weight stratum of the reciprocal roots of C is an algebraic integer (only for stratum members, not all … |
| `lemma-reciprocal-roots-zeta--5` | different route |  | Lean does not choose a weight per root. It proves A = prod_{odd} P_i, B = prod_{even} P_i with the integral factors (integral_recovery); the weight of a root of A/B then comes from the Riemann hypothesis for the P_i (WeilRiemannHypothesis, from exists_isWeilF… |
| `lemma-reciprocal-roots-zeta--6` | different route |  | Lean transfers weights to A, B only through A = prod_{odd} P_i (integral_recovery) and RH for P_i; the embedding-extension argument appears as PadicAlgCl.exists_ringHom_complex_apply_eq inside exists_isWeilFactorization_of_smoothProper (universal purity of th… |
| `lemma-reciprocal-roots-zeta--7` | partial |  | WeilConjectures/ZetaFunction/RealizationIndependence.lean:196 realization_independence (not on any node): for every l != p and every l-adic realization rho : Qbar = Qbar^(l) in Qbar_l, the stratum polynomial Q_i = prod_{a in R_i}(1 - aT) of A (i odd) / B (i e… |
| `lemma-reduced-fractions-integer-coefficients--1` | the declaration's own name | `PowerSeries.existsUnique_isNormalizedIntegralFraction` | WeilConjectures/ZetaLinearAlgebra/ReciprocalRoots.lean:181 PowerSeries.existsUnique_isNormalizedIntegralFraction (parent's only name): f in Z[[T]] with constant coefficient 1, rational over Q, has a unique (A,B) in Z[T]^2 with IsNormalizedIntegralFraction (A(… |
| `theorem-purity-higher-direct-images-under--1` | project lemma | `AlgebraicGeometry.WeilSheaf.higherLowerShriekObjIsoOfIsProper` | WeilConjectures/ZetaFunction/RelativePurity.lean:150 noncomputable def WeilSheaf.higherLowerShriekObjIsoOfIsProper (inside namespace AlgebraicGeometry, :78): for proper f, R^i f_! F = R^i f_* F as an isomorphism in the category of Weil sheaves (hence Weil-equ… |
| `theorem-purity-higher-direct-images-under--2` | project lemma | `AlgebraicGeometry.WeilSheaf.isPunctuallyPureOfWeight_higherLowerStar` | WeilConjectures/ZetaFunction/RelativePurity.lean:234 (namespace AlgebraicGeometry.WeilSheaf) isPunctuallyPureOfWeight_higherLowerStar: f smooth proper of pure relative dimension d, F lisse punctually iota-pure of weight w, then R^i f_* F is punctually iota-pu… |
| `theorem-purity-higher-direct-images-under--3` | partial |  | WeilConjectures/DeligneLaumon/Reduction/QuasiFiniteMixed.lean:67 (namespace AlgebraicGeometry.WeilSheaf, :42) IsPunctuallyPureOfWeight.isMixedOfWeightsAtMost: punctually pure of weight w implies mixed of weights at most w (filtration 0 in F). Applied to --2 i… |
| `theorem-weil-conjectures-smooth-proper-schemes--1` | partial | `AlgebraicGeometry.Scheme.existsUnique_isIntegralFrobeniusFactor` | RESTRICTION-ONLY (same restriction as the parent's names: Lean assumes [GeometricallyConnected], the blueprint does not; otherwise exact): WeilConjectures/ZetaFunction/IntegralFrobeniusFactors.lean:77 existsUnique_isIntegralFrobeniusFactor: for i <= 2d, exist… |
| `theorem-weil-conjectures-smooth-proper-schemes--2` | project lemma | `AlgebraicGeometry.Scheme.IsIntegralFrobeniusFactor.unique` | WeilConjectures/ZetaFunction/IntegralFrobeniusFactors.lean:59 IsIntegralFrobeniusFactor.unique: two integral realizations P, P' of the degree-i determinant factor are equal; proof picks one l != p and uses injectivity of Z -> Qbar_l, exactly the blueprint pro… |
| `theorem-weil-conjectures-smooth-proper-schemes--3` | partial | `AlgebraicGeometry.Scheme.integral_frobenius_factors` | RESTRICTION-ONLY (same restriction as the parent's names: Lean assumes [GeometricallyConnected], the blueprint does not; otherwise exact): WeilConjectures/ZetaFunction/IntegralFrobeniusFactors.lean:101 integral_frobenius_factors, second conjunct: for every fa… |
| `theorem-weil-conjectures-smooth-proper-schemes--4` | partial | `AlgebraicGeometry.Scheme.riemann_hypothesis` | RESTRICTION-ONLY (same restriction as the parent's names: Lean assumes [GeometricallyConnected], the blueprint does not; otherwise exact): WeilConjectures/ZetaFunction/FinalTheorems.lean:174 riemann_hypothesis (parent name), first conjunct: every root alpha o… |
| `theorem-weil-conjectures-smooth-proper-schemes--5` | partial | `AlgebraicGeometry.Scheme.riemann_hypothesis` | RESTRICTION-ONLY (same restriction as the parent's names: Lean assumes [GeometricallyConnected], the blueprint does not; otherwise exact): WeilConjectures/ZetaFunction/FinalTheorems.lean:174 riemann_hypothesis (parent name), first conjunct: every reciprocal r… |
| `theorem-weil-conjectures-smooth-proper-schemes--6` | project lemma | `AlgebraicGeometry.weilBettiNumber` | WeilConjectures/ZetaFunction/BettiNumbers.lean:50 def weilBettiNumber P i := deg P_i for 0<=i<=n, 0 otherwise (namespace AlgebraicGeometry, line 44); weilBettiNumber_natCast (:53) identifies it with (P i).natDegree. The final theorems (weil_betti etc.) use (P… |
| `theorem-weil-conjectures-smooth-proper-schemes--8` | partial | `AlgebraicGeometry.Scheme.natDegree_eq_finrank_of_isIntegralFrobeniusFactor`<br>`AlgebraicGeometry.Scheme.weilBettiNumber_eq_finrank` | RESTRICTION-ONLY (same restriction as the parent's names: Lean assumes [GeometricallyConnected], the blueprint does not; otherwise exact): WeilConjectures/ZetaFunction/BettiSymmetry.lean:119 natDegree_eq_finrank_of_isIntegralFrobeniusFactor: if P is an integr… |
| `theorem-weil-conjectures-smooth-proper-schemes--9` | partial | `AlgebraicGeometry.Scheme.betti_symmetry` | RESTRICTION-ONLY (same restriction as the parent's names: Lean assumes [GeometricallyConnected], the blueprint does not; otherwise exact): WeilConjectures/ZetaFunction/BettiSymmetry.lean:229 betti_symmetry, second conjunct: deg P_{rev i} = deg P_i (rev i = 2d… |
| `theorem-weil-conjectures-smooth-proper-schemes--10` | project lemma | `AlgebraicGeometry.Scheme.endpoints_of_isIntegralFrobeniusFactor` | WeilConjectures/ZetaFunction/BettiSymmetry.lean:195 endpoints_of_isIntegralFrobeniusFactor, first conjunct: P 0 = 1 - X for the integral Frobenius factors of X0 smooth proper geometrically connected (hypotheses match the clause). Same statement also inside be… |
| `theorem-weil-conjectures-smooth-proper-schemes--11` | project lemma | `AlgebraicGeometry.Scheme.endpoints_of_isIntegralFrobeniusFactor` | WeilConjectures/ZetaFunction/BettiSymmetry.lean:195 endpoints_of_isIntegralFrobeniusFactor, second conjunct: P (last 2d) = 1 - C(q^d) X. l-adic version frobeniusCharpolyRev_two_mul (SmoothProper.lean:75) via the trace of Poincare duality. |
| `theorem-weil-conjectures-smooth-proper-schemes--12` | project lemma | `AlgebraicGeometry.Scheme.endpoints_of_isIntegralFrobeniusFactor` | WeilConjectures/ZetaFunction/BettiSymmetry.lean:195 endpoints_of_isIntegralFrobeniusFactor, third conjunct: (P 0).natDegree = 1. |
| `theorem-weil-conjectures-smooth-proper-schemes--13` | project lemma | `AlgebraicGeometry.Scheme.endpoints_of_isIntegralFrobeniusFactor` | WeilConjectures/ZetaFunction/BettiSymmetry.lean:195 endpoints_of_isIntegralFrobeniusFactor, fourth conjunct: (P (last 2d)).natDegree = 1. |
| `theorem-weil-conjectures-smooth-proper-schemes--14` | project lemma | `Polynomial.alternatingNatDegreeSum` | WeilConjectures/Mathlib/Algebra/Polynomial/BigOperators.lean:38 def Polynomial.alternatingNatDegreeSum P := sum_i (-1)^i (P i).natDegree (namespace Polynomial, :33); this is chi = sum (-1)^i b_i, used as chi in weil_functional_equation and reciprocity. |
| `theorem-weil-conjectures-smooth-proper-schemes--15` | partial | `AlgebraicGeometry.Scheme.weil_functional_equation` | RESTRICTION-ONLY (same restriction as the parent's names: Lean assumes [GeometricallyConnected], the blueprint does not; otherwise exact): WeilConjectures/ZetaFunction/FinalTheorems.lean:258 weil_functional_equation (parent name): 'exists m, d * alternatingNa… |
| `theorem-weil-conjectures-smooth-proper-schemes--16` | partial | `AlgebraicGeometry.Scheme.weil_functional_equation` | RESTRICTION-ONLY (same restriction as the parent's names: Lean assumes [GeometricallyConnected], the blueprint does not; otherwise exact): WeilConjectures/ZetaFunction/FinalTheorems.lean:258 weil_functional_equation (parent name), last conjunct: weilSign = +-… |

### chap-Proper-base-change

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `definition-completed-inverse-image--1` | the declaration's own name | `AlgebraicGeometry.Scheme.completedPullbackObject`<br>`AlgebraicGeometry.Scheme.completedPullbackFunctor` | AlgebraicGeometry/Completed/CompletedTowerPullbackSupplement.lean:872: completedPullbackObject K = Rlim of the pullback of the reduction tower of K, i.e. Rlim_n g^*(M tensor O_E/pi^n). Clause text equals the parent. |
| `definition-torsion-sheaves--2` | inside a proof |  | Inline in the torsion definition. |
| `lemma-acyclic-resolutions--1` | the declaration's own name | `CategoryTheory.Functor.rightDerivedObjIsoOfResolution`<br>`CategoryTheory.Functor.nonempty_rightDerivedObjIso_homology_of_acyclic`<br>`CategoryTheory.Functor.isIso_rightDerivedFunctorPlusUnit_app_of_rightAcyclic` | Clause text equals the parent; the first two names give H^q(vM) = R^q v F for an acyclic resolution, the third the general statement for bounded below complexes of v-acyclic objects (LEAN-MAPPING high). |
| `lemma-composition-cancellation--1` | the declaration's own name | `AlgebraicGeometry.Etale.HasTorsionBaseChange.comp` | SixFunctors/Etale/BaseChangeTheorems/Cancellation.lean:181: PBC(f) and PBC(h) imply PBC(f >> h), torsion Lambda. Exactly clause (i). |
| `lemma-composition-cancellation--2` | the declaration's own name | `AlgebraicGeometry.Etale.HasTorsionBaseChange.of_comp` | Cancellation.lean:390: [Surjective f], PBC(f) and PBC(f >> h) imply PBC(h). Exactly clause (ii). |
| `lemma-extension-separably-closed-ground-field--1` | the declaration's own name | `AlgebraicGeometry.IsCurve.bijective_cohomologyMap_of_isSepClosed` | AlgebraicGeometry/Curve/FieldExtension.lean:233: k <= k' separably closed, C proper curve, F torsion etale Lambda-module sheaf: H^q(C,F) -> H^q(C',F\|) bijective for all q. Clause text equals the parent; caveat: etale cohomology of etale sheaves (the blueprin… |
| `proposition-proper-base-change-projective-line--2` | the declaration's own name | `AlgebraicGeometry.Etale.hasInjectiveAcyclicity_projectiveLine` | SixFunctors/Etale/BaseChangeTheorems/ProjectiveLine/GeometricStalk.lean:215: HasInjectiveAcyclicity Lambda (P^1_S -> S), i.e. IA_Lambda(pi). |
| `proposition-proper-direct-image-constructible-complexes--4` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightDerivedLowerStar_obj` | SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleLowerStar.lean:150 (in namespace AlgebraicGeometry.ProEtale.CondensedRing, not the ContinuousMapRingObj/PadicIntegersRingObj sub-namespaces used by siblings --3/--2): Rf_* carries bounded construct… |
| `proposition-proper-direct-image-constructible-complexes--11` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.isIso_properProjectionMap_boundedConstructible_rational` | SixFunctors/ProEtale/ModuleObject/Derived/Proper/ProperBaseChangeRational.lean:448 (p proper, section variable at :312): for Lambda = E (continuousMapRingObj E, E/Q_ell finite) or Qbar_ell, the projection map Rp_*K tensor M -> Rp_*(K tensor p^*M) is an iso fo… |
| `proposition-proper-direct-image-finite-coefficients--1` | the declaration's own name | `AlgebraicGeometry.Etale.isBoundedConstructible_hasTorAmplitudeIn_rightDerivedLowerStar_of_proper` | Parent's only name; clause text equals the parent (D_ctf preserved with Tor amplitude [a, b+d]); LEAN-MAPPING high confidence. |
| `theorem-cohomology-curves--3` | partial |  | AlgebraicGeometry/Curve/FiniteCoefficientAssertions.lean:43: for a finite ring Lambda, k algebraically closed and X a curve, IsCurve.Assertions Lambda f F holds for every sheaf of Lambda-modules; field C3 (Assertions.lean:180) is H^q = 0 for q > 1 when char k… |
| `theorem-cohomology-curves--4` | partial |  | FiniteCoefficientAssertions.lean:43, field C4 (finite_of_isTorsionSheafOfInvertibleOrder, Assertions.lean:185): H^q finite for constructible F with torsion prime to char k, for sheaves of modules over a finite ring. A constructible sheaf with finite stalks on… |
| `theorem-cohomology-curves--5` | partial |  | FiniteCoefficientAssertions.lean:43, field C5 (finite_of_isProper, Assertions.lean:190): H^q finite for X proper and F constructible, for sheaves of modules over a finite ring. Same caveat as --4 (abelian constructible sheaves with finite stalks need the redu… |
| `theorem-cohomology-curves--6` | partial |  | FiniteCoefficientAssertions.lean:43, field C6 (bijective_cohomologyMap_of_isTorsionSheafOfInvertibleOrder, Assertions.lean:195): pullback H^q(C,F) -> H^q(C_{k'},F\|) bijective for algebraically closed k'/k and F with invertible torsion, for modules over a fin… |
| `theorem-pbc-injective-acyclicity--1` | project lemma | `AlgebraicGeometry.Etale.tfae_hasTorsionBaseChange`<br>`AlgebraicGeometry.Etale.hasTorsionBaseChange_iff_forall_isIso_baseChangeHomologyMap` | SixFunctors/Etale/BaseChangeTheorems/Characterization.lean:84: for f proper, TFAE [PBC(f), base change maps on cohomology sheaves g^* R^q f_* F -> R^q f'_* g'^* F are isos for every torsion F and q, IA(f) with Lambda/p coefficients for every prime p]; :54 sta… |
| `theorem-proper-base-change-classical-pro--1` | the declaration's own name | `AlgebraicGeometry.Etale.isIso_baseChange_of_isProper_of_torsionHomology` | SixFunctors/Etale/BaseChangeTheorems/Proper.lean:117: f proper, any g, K in D^+(X_et, Lambda) with torsion cohomology sheaves: the derived base change map is an iso. Clause text equals the parent. Caveat: stated on the etale site; the blueprint's D^+_class(X_… |

### chap-Pure-sheaves-on-curves

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `corollary-unramified-boundary-point--1` | the declaration's own name | `AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.isPureOfWeight_stalk_directImage_of_isLisse` | WeilConjectures/WeilSheaf/UnramifiedBoundaryPurity.lean:70 (parent name): j : U0 -> C0 dense open in a smooth geometrically connected curve, F lisse punctually iota-pure of weight w, x a closed point where F is unramified (j_*F lisse on a neighbourhood of x):… |
| `definition-middle-extension--1` | the declaration's own name | `AlgebraicGeometry.Etale.middleExtension` | WeilConjectures/EtaleCohomology/Purity/RealSheaves/Boundary.lean:328 (namespace AlgebraicGeometry.Etale, :320) abbrev middleExtension A j := (j)_*[A], the underived direct image of etale sheaves along an open immersion (parent's only name). Single clause = wh… |
| `lemma-boundary-stalk--1` | the declaration's own name | `AlgebraicGeometry.WeilGroup.exists_equivalence_isLisse_stalk_directImage_boundaryStalk_eq_invariants` | WeilConjectures/EtaleCohomology/Purity/RealSheaves/BoundaryStalkInvariantsUnconditional.lean:62 (parent name): for U0 a nonempty open of a smooth geometrically connected curve (U0 geometrically connected), there is an equivalence lisse sheaves <-> representat… |
| `lemma-bounds-squared-traces--3` | partial |  | Lean has trace energies only for Weil sheaves (WeilConjectures/DeligneLaumon/AffineLine/TraceEnergy.lean:105 traceEnergy), not for complexes. The only punctual energy bound is :823 LisseOnDenseOpen.exists_boundaryEnergy_le: the boundary contribution of j_*M (… |
| `lemma-bounds-squared-traces--4` | partial |  | WeilConjectures/DeligneLaumon/AffineLine/TraceEnergy.lean:226 l2Weight_le_of_traceEnergy_le (parent name): S_n(F) <= C q^{nB} for n >= 1 implies nu(F) <= B - 1; with B = a this is the 'hence' step of the clause. Stated for Weil sheaves (not complexes), and no… |
| `lemma-growth-finite-corrections--1` | the declaration's own name | `AlgebraicGeometry.WeilSheaf.l2Weight_le_max_of_traceEnergy_le_add` | WeilConjectures/DeligneLaumon/AffineLine/TraceEnergy.lean:309 l2Weight_le_max_of_traceEnergy_le_add (parent's only name): S_m(E) <= S_m(F) + C q^{mB} implies nu(E) <= max(nu(F), B - 1) (E, F sheaves, possibly on different schemes). The clause (equality when m… |
| `lemma-radius-squared-traces--1` | the declaration's own name | `AlgebraicGeometry.WeilSheaf.lt_l2Weight_iff`<br>`AlgebraicGeometry.WeilSheaf.l2Series` | WeilConjectures/DeligneLaumon/AffineLine/TraceEnergy.lean:131 def l2Series (the series sum S_m t^{m-1}) and :236 lt_l2Weight_iff (parent names): for every real beta, beta < nu(F) iff radius(phi_F) < q^{-(beta+1)}, i.e. radius = q^{-nu-1} with the stated conve… |
| `proposition-twisting-weight-zero-adding-dual--7` | Mathlib | `CategoryTheory.Limits.biprod.inl_fst` | WeilConjectures/DeligneLaumon/AffineLine/TraceEnergy.lean:341 def realEnvelope F hF b := F.constantTwist b ⊞ (F.constantTwist b).dual (already on --3, hence listed as conflict). The direct-summand property is Mathlib's Mathlib/CategoryTheory/Limits/Shapes/Bin… |

### chap-Purity-of-real-sheaves

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `corollary-determinant-weights--2` | the declaration's own name | `AlgebraicGeometry.WeilGroup.isPunctuallyPure_det_baseChange_iff`<br>`Representation.detWeight_mul_of_mem_ker` | Two of the parent's names are exactly this clause. (a) Representation.detWeight_mul_of_mem_ker (WeilConjectures/AlgebraicGeometry/LinearAlgebraicGroup/Weights.lean:173): dw(u*γ) = dw(γ) for degree-zero u when the geometric determinant is finite, i.e. independ… |
| `definition-determinant-weight--2` | the declaration's own name | `AlgebraicGeometry.WeilGroup.mem_detWeightMultiset_iff` | Parent name AlgebraicGeometry.WeilGroup.detWeightMultiset (WeilConjectures/EtaleCohomology/Purity/RealSheaves/DetWeights.lean:262) is this definition: the multiset of determinant weights of the composition factors. It is a multiset rather than a set; the blue… |
| `lemma-degree-zero-top-cohomology--1` | the declaration's own name | `AlgebraicGeometry.WeilGroup.exists_globalSections_linearEquiv_invariants` | Parent name AlgebraicGeometry.WeilGroup.exists_globalSections_linearEquiv_invariants (EtaleCohomology/Purity/RealSheaves/WeilFundamentalRepresentationSections.lean:232): Γ(C,F) ≃ π₁-invariants of the fundamental representation, Frobenius-equivariant. Parent n… |
| `lemma-degree-zero-top-cohomology--5` | partial |  | WeilConjectures/WeilSheaf/GeometricCoinvariants.lean:225: every Frobenius eigenvalue β on Γ(X̄,G) has β^{deg x} a local Frobenius eigenvalue at some closed point x. The H^0 weight bound follows at once, but is not stated for general X. ZetaFunction/Weights.le… |
| `lemma-degree-zero-top-cohomology--6` | partial |  | DeligneLaumon/AffineLine/CurveTopBound.lean:89: H_c^2(C,G) has weights <= w+2, but assumes G punctually PURE of weight w (smooth affine curve, lisse), not 'weights <= a'. EtaleCohomology/Purity/RealSheaves/SheafSemicontinuity.lean:125: F lisse with weights <=… |
| `lemma-degree-zero-top-cohomology--7` | partial |  | H_c^2 half: parent names WeilSheaf/CurveTopCohomology.lean:80 and DeligneLaumon/AffineLine/AffineCurveUpper.lean:303 (F punctually pure of weight w, lisse, smooth geometrically connected affine curve gives H_c^2 pure of weight w+2). H^0 half: no declaration. … |
| `lemma-normality-geometric-monodromy--1` | the declaration's own name | `Matrix.GeneralLinearGroup.instIsHopfIdealVanishingIdeal`<br>`Matrix.GeneralLinearGroup.isRadical_vanishingIdeal` | The parent's names give this clause. WeilConjectures/AlgebraicGeometry/LinearAlgebraicGroup/Monodromy.lean:441 arithmeticMonodromy_le_geometricMonodromy: ideal of G ≤ ideal of H, i.e. H ⊆ G. Monodromy.lean:456 normal_zeroLocus_geometricMonodromy: H(R) is norm… |
| `lemma-positivity-euler-factors--1` | the declaration's own name | `AlgebraicGeometry.WeilSheaf.IsReal.inv_localPolynomial_stalk_tensorPow_nonneg` | Clause text equals the parent. Parent name AlgebraicGeometry.WeilSheaf.IsReal.inv_localPolynomial_stalk_tensorPow_nonneg (EtaleCohomology/Purity/RealSheaves/SheafWeightOperations.lean:234): for lisse ι-real G and even k, the coefficients of ι det(1 - t F_x \|… |
| `lemma-tensor-exterior-powers-filtered-representations--1` | the declaration's own name | `Representation.CompositionSeries.hasGradedPieces_tprod` | Parent name Representation.CompositionSeries.hasGradedPieces_tprod (WeilConjectures/RepresentationTheory/Filtration.lean:583): for composition series s of V and s' of V', V⊗V' has a filtration whose graded pieces are A_i⊗B_j, each pair exactly once (HasGraded… |
| `lemma-tensor-exterior-powers-filtered-representations--2` | the declaration's own name | `Representation.CompositionSeries.hasGradedPieces_exteriorPower`<br>`Representation.nontrivial_piTensorProduct_exteriorPower_iff` | Parent name Representation.CompositionSeries.hasGradedPieces_exteriorPower (WeilConjectures/RepresentationTheory/ExteriorPowerFiltration.lean:248): ⋀^r V has a filtration with graded pieces ⨂_i ⋀^{n_i} A_i, one for each tuple with Σn_i=r. Lean indexes all tup… |
| `lemma-tensor-exterior-powers-filtered-representations--3` | project lemma | `Representation.CompositionSeries.exists_equiv_sigma_of_monotone` | WeilConjectures/RepresentationTheory/Filtration.lean:438 (namespace Representation.CompositionSeries, on no node). Given a finite filtration F and a composition series t_i of each graded piece, the factors of any composition series of V correspond bijectively… |
| `proposition-bound-largest-determinant-weight--1` | the declaration's own name | `AlgebraicGeometry.WeilGroup.sq_norm_le_rpow_of_isReal` | Clause text equals the parent. Parent name AlgebraicGeometry.WeilGroup.sq_norm_le_rpow_of_isReal (EtaleCohomology/Purity/RealSheaves/Purity.lean:561) states \|ι α\|^2 <= q_x^d for every local eigenvalue when all constituents have det weight <= d (smooth geome… |
| `proposition-determinant-weights-tensor-operations--3` | not formalized |  | The parent's Lean names cover only tensor (1) and exterior power (2). Part (3) is not used in Lean. |
| `proposition-kummer-duality-integral-tate-module--1` | project lemma |  | WeilConjectures/EtaleCohomology/Purity/RealSheaves/JacobianKummer.lean:107 kummerEquiv : H^1(C, mu_{l^n}) ≃+ J0(Kbar)[l^n]; :123 kummerEquiv_restrictMuH (Galois equivariance); :144 kummerEquiv_map_rootsOfUnityPowMap (transition maps z↦z^l correspond to [l]). … |
| `proposition-kummer-duality-integral-tate-module--2` | partial |  | WeilConjectures/AlgebraicGeometry/FundamentalGroup/CurvePairing.lean:242 bijective_curvePairing: the finite-level cup-trace pairing H^1(X,Z/l^n) × H^1(X,mu_{l^n}) → Z/l^n is perfect (both adjoints bijective), with H^1(X,Z/l^n) modelled as continuous character… |
| `proposition-kummer-duality-integral-tate-module--3` | partial |  | Frobenius.lean:246, third conjunct of exists_picTorsionPairing: Psi_n of a torsor transported along the geometric Galois Frobenius equals Psi_n of the torsor composed with pullback of line bundles along that Frobenius. This is the finite-level Frobenius invar… |

### chap-Smooth-base-change

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `lemma-base-change-along-product-projection--1` | the declaration's own name | `AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_field` | SixFunctors/Etale/Derived/Kunneth/OpenImmersionBaseChange.lean:101: for j : U -> X separated of finite type and the base change along W = X x_K Y -> X, the exchange q1^{-1} R^i j_* F -> R^i h_* e^{-1} F is an iso for every sheaf F and degree i (Lambda killed … |
| `lemma-kunneth-field-coefficients--1` | the declaration's own name | `AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap` | SixFunctors/Etale/Derived/Kunneth/Ordinary.lean:158: for finite Lambda with invertible exponent and schemes of finite type over a field, the base change map Lp^*E tensor Lf'^* Rg_* F -> Rh_*(...) of (8.4) is an iso for all E, F (unbounded). More general than … |
| `lemma-kunneth-finite-direct-image--1` | the declaration's own name | `AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap_lowerStar_unit`<br>`AlgebraicGeometry.Etale.isIso_tensorBaseChangeMap_rightDerivedLowerStar_unit` | Kunneth/FlatSingle/Devissage.lean:82 (Q = pi_* A for pi finite, single sheaf F) and FiniteGood.lean:148 (R pi'_* Lambda, given base change hypotheses). Caveat: one summand pi_*A, not a finite direct sum (additive extension not stated). |
| `proposition-ordinary-external-kunneth--1` | partial |  | Clause text equals the parent. SixFunctors/Etale/Derived/Kunneth/Ordinary.lean:234 (parent name): Kunneth for RGamma over a separably closed field, i.e. Y_i = Spec k, finite Lambda. TraceFormula/ProperKunneth.lean:309 (parent name, explicitly named instance):… |
| `theorem-smooth-base-change-all-admissible--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_app_padicIntegers_of_smooth` | SixFunctors/ProEtale/ModuleObject/BaseChangeTheorems/SmoothPadicIntegers.lean:108: p smooth, ell invertible on S, K bounded constructible O_E-complex: the base change map is an iso. |
| `theorem-smooth-base-change-all-admissible--3` | not formalized |  | The Qbar_ell case (--4) goes directly through integral models, skipping E. |
| `theorem-smooth-base-change-all-admissible--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_smooth` | SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleSmoothBaseChange.lean:71: v smooth, K in D^b_c(X, Qbar_ell): Lv^* Rp_* K -> Rp'_* Lu^* K is an iso. |

### chap-Smooth-purity

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `corollary-dualizing-complex-smooth-scheme--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.smoothPurityIso`<br>`AlgebraicGeometry.Etale.exists_counit_eq_smoothPurityTrace` | The clause equals the parent. Parent names AlgebraicGeometry.ProEtale.CondensedRing.smoothPurityIso (SmoothPurity/Defs.lean:450, Qbar) and AlgebraicGeometry.Etale.exists_counit_eq_smoothPurityTrace (Trace.lean:372, finite). Integral and E coefficients are not… |
| `definition-deformation-normal-bundle--1` | the declaration's own name | `AlgebraicGeometry.Scheme.IdealSheafData.deformationSpaceIsoBlowupModelOpen`<br>`AlgebraicGeometry.Scheme.IdealSheafData.range_deformationSpaceToBlowup_eq_compl_strictTransform_of_ofFiniteType` | The clause equals the parent. The parent name AlgebraicGeometry.Scheme.IdealSheafData.deformationSpace (AlgebraicGeometry/DeformationSpace.lean:220) is the extended-Rees-algebra model Spec_X O_X[t, I t^{-1}]. Two lemmas identify it with the clause's descripti… |
| `lemma-section-normal-bundle--1` | the declaration's own name | `AlgebraicGeometry.Etale.nonempty_iso_sectionInvariant_normalCone` | The clause equals the parent. Parent name AlgebraicGeometry.Etale.nonempty_iso_sectionInvariant_normalCone (EtaleCohomology/Purity/Smooth/Deformation.lean:625) gives only the existence of the iso, not the canonical one built by restricting to t=0. A pro-étale… |
| `lemma-sp-reduction--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.rightDerivedLowerShriekExtendScalarsMap` | Parent names AlgebraicGeometry.ProEtale.rightDerivedLowerShriekExtendScalarsMap (SixFunctors/ProEtale/FiniteCoefficient/Derived/ExtendScalars/LowerShriek.lean:110), the map Ψ(Rf_!K) → Rf_!(ΨK), and isIso_rightDerivedLowerShriekExtendScalarsMap_app (:120), whi… |
| `lemma-sp-reduction--2` | not formalized |  | Not formalized for smooth f. |
| `lemma-sp-reduction--3` | not formalized |  | Not formalized for finite A→B and smooth f. |
| `lemma-sp-reduction--4` | not formalized |  | Not formalized. |
| `lemma-sp-reduction--5` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-base-change--1` | project lemma | `AlgebraicGeometry.Etale.canonicalSmoothPurityMap_baseChange` | WeilConjectures/EtaleCohomology/Purity/Smooth/CanonicalPurityBaseChange.lean:175: for a cartesian square and K ∈ D(Y_ét,Λ), finite Λ, Lg'^*(γ_f(K))∘(upperShriekBaseChangeMap) = (Lg'^*Lf^* ≅ Lf'^*Lg^*)∘γ_{f'}(g^*K). Here γ is the canonical purity map (canonica… |
| `proposition-compatibility-purity-base-change--2` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-base-change--3` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-change-coefficients--1` | the declaration's own name | `AlgebraicGeometry.Etale.map_smoothPurityIso_hom_comp` | Parent name AlgebraicGeometry.Etale.map_smoothPurityIso_hom_comp (EtaleCohomology/Purity/Smooth/Reduction.lean:90): for a change of coefficients Ψ between finite rings, vS∘Ψ(γ_{f,K}) = γ_{f,ΨK}∘v0. It is conditional: the comparison isos and the compatibilitie… |
| `proposition-compatibility-purity-change-coefficients--2` | the declaration's own name | `AlgebraicGeometry.Etale.map_smoothPurityTrace` | Parent name AlgebraicGeometry.Etale.map_smoothPurityTrace (EtaleCohomology/Purity/Smooth/Reduction.lean:160): Ψ_Y(Tr^sm_{f,K}) = Tr^sm_{f,ΨK}∘Rf_!(v0)∘ψ for finite Λ→Λ'. It is derived from the purity square hγ and the counit compatibility hS, which are both h… |
| `proposition-compatibility-purity-change-coefficients--3` | not formalized |  | Not formalized. The integral stage uses a non-canonical orientation (nonempty_iso_integralTateTwist_upperShriekUnit). |
| `proposition-compatibility-purity-change-coefficients--4` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-change-coefficients--5` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-change-coefficients--6` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-change-coefficients--7` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-change-coefficients--8` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-change-coefficients--9` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-change-coefficients--10` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-change-coefficients--11` | not formalized |  | Not formalized. In Lean the Qbar orientation is built from the integral one, skipping E. |
| `proposition-compatibility-purity-change-coefficients--12` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-change-coefficients--13` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-change-coefficients--14` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-composition--1` | not formalized |  | Not formalized. The chart and iterated-integration argument is absent. |
| `proposition-compatibility-purity-composition--2` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-composition--3` | not formalized |  | Not formalized. |
| `proposition-compatibility-purity-composition--4` | partial |  | The parent's own names (SmoothPurity/Defs.lean:358, :483) are the Qbar case with g an open immersion (relative dimension 0) and K = unit. They hold by construction: the orientation is normalized along open immersions via smoothImageFactor. General smooth g is… |
| `proposition-purity-vector-bundles--1` | the declaration's own name | `AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_affineSpace` | The clause equals the parent. Parent names AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_affineSpace (EtaleCohomology/Purity/Smooth/AffineSpacePurity.lean:163) and ..._affineSpaceZero (AffineSpace.lean:258) cover only trivial bundles A^d_S, as … |
| `proposition-relative-dualizing-complex--1` | the declaration's own name | `AlgebraicGeometry.Etale.dualizingComplexTwistShiftIso` | The clause equals the parent. Parent name AlgebraicGeometry.Etale.dualizingComplexTwistShiftIso (EtaleCohomology/Purity/Smooth/DiagonalOrientation.lean:230) is the canonical iso ω_f ≅ Λ_X(d)[2d] (finite Λ, étale site). |
| `proposition-smooth-purity-finite-coefficients--1` | the declaration's own name | `AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_twistShift`<br>`AlgebraicGeometry.Etale.smoothPurityIso` | The clause equals the parent. Parent names AlgebraicGeometry.Etale.smoothPurityIso (Basic.lean:236, a def taking θ and φ as arguments) and AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_twistShift (Basic.lean:261, existence of Rf^!K ≅ Lf^*K(d)[2… |
| `proposition-transitivity-trace-map--1` | the declaration's own name | `AlgebraicGeometry.Etale.smoothPurityTrace_comp` | The clause text equals the parent statement. AlgebraicGeometry.Etale.smoothPurityTrace_comp (EtaleCohomology/Purity/Smooth/Trace.lean:231) states Tr_{f≫g}(K) = Tr_g(K)∘Rg_!(Tr_f(g^*K(e)[2e]))∘(composition isos). It holds for finite Λ (étale), with the purity … |
| `theorem-smooth-purity-all-admissible-coefficients--3` | not formalized |  | Lean goes from integral (nonempty_iso_integralTateTwist_upperShriekUnit) directly to Qbar_ell by extension of scalars. There is no E stage. |
| `theorem-smooth-purity-all-admissible-coefficients--4` | partial |  | WeilConjectures/SmoothPurity/OrientationCanonical.lean:122 nonempty_iso_tateTwist_upperShriekUnit: Qbar_ell,X(d)[2d] ≅ Rf^! Qbar_ell,Y. This covers only K = the unit (constant sheaf), as a bare Nonempty and not the designated map. The parent's names smoothOri… |
| `theorem-smooth-purity-all-admissible-coefficients--5` | not formalized |  | Lean normalizes on the zero-section fundamental class of A^1 rather than through the trace (9.1) built from P^1. |
| `theorem-smooth-purity-all-admissible-coefficients--6` | not formalized |  | Not formalized. |
| `theorem-smooth-purity-all-admissible-coefficients--7` | not formalized |  | Not formalized. |
| `theorem-smooth-purity-all-admissible-coefficients--8` | not formalized |  | Not formalized. The Qbar orientation is normalized only along open immersions. |
| `theorem-smooth-purity-all-admissible-coefficients--10` | partial |  | The only composition statements for the designated γ are the Qbar, K = unit case where h is an open immersion: SmoothPurity/Defs.lean:358 and :483. Both are already on proposition-compatibility-purity-composition. AlgebraicGeometry.Etale.smoothPurityTrace_com… |
| `theorem-smooth-purity-all-admissible-coefficients--11` | partial |  | AlgebraicGeometry.Etale.map_smoothPurityIso_hom_comp (EtaleCohomology/Purity/Smooth/Reduction.lean:90) is already on proposition-compatibility-purity-change-coefficients. It covers only finite Λ→Λ' and is conditional: the compatibilities htw, hθ, hφ of the co… |
| `theorem-sp-qbar--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isIso_smoothPurityMap`<br>`AlgebraicGeometry.ProEtale.CondensedRing.isIso_upperShriekUnitTensorMap_of_smooth` | The clause equals the parent. Parent names isIso_smoothPurityMap (SmoothPurity/Defs.lean:440, Qbar unit purity) and isIso_upperShriekUnitTensorMap_of_smooth (TraceFormula/PurityDevissage.lean:209, f^!K ≅ f^*K ⊗ f^!Qbar). Together they give f^! ≅ f^*(d)[2d], h… |

### chap-Specialization-and-contracting-correspondences

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `corollary-contracting-local-terms-point--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_eq_integral_of_isContractingAt` | WeilConjectures/TraceFormula/ContractingGraph.lean:145: if c is contracting at the fixed rational point y and B is an open-closed proper subscheme of the fixed locus with underlying set {y}, the local term along B is the integral of the trace class of the res… |
| `corollary-contracting-local-terms-point--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_ofGraph_eq_trace_of_isContractingAt` | ContractingGraph.lean:355: for the graph correspondence (id, h) contracting at x, the local term along B = {x} is the trace of the stalk map v_x : K_x -> K_x, i.e. LT_y(u) = tr(u_y \| K_y). |
| `corollary-specialization-when-fixed-point-scheme--1` | partial |  | ComponentSpecializationIntegral.lean:103 (docstring cites this corollary, case F_red = {y} x S): for the contracting deformation and a component B = {y} whose class is specialized, integral of sp_F(z) = sigma^{-1} Psi_s(integral of z\|_B) sigma, i.e. sp_F is … |
| `corollary-specialization-when-fixed-point-scheme--2` | partial |  | DeformationTraceSpecialization.lean:167: sp(z) = 0 implies z\|_B = 0 (injectivity on the component B = {y}), given SpecializesComponentClass. Vanishing.lean:84 (parent's own name): exists a TraceSpecialization with sp z = 0 -> z\|_B = 0, hypothesis-free. Only… |
| `lemma-base-change-cone-x-z--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.nonempty_specializationDefect_lowerStar_iso` | DefectExchanges.lean:104: f proper, C_{X,Z}(Rf_*L') = Rf_{Z*} C_{X',Z'}(L') with Z' = f^{-1}Z (I.comap). Qbar_ell. |
| `lemma-base-change-cone-x-z--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.nonempty_specializationDefect_upperStar_iso` | DefectExchanges.lean:73: f smooth, C_{X',Z'}(f^*L) = f_Z^* C_{X,Z}(L). |
| `lemma-base-change-cone-x-z--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isZero_specializationDefect_lowerStar_centreι` | DefectExchanges.lean:170: C_{X,Z}(i_* M) = 0 for M bounded constructible on Z. |
| `lemma-base-change-cone-x-z--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.nonempty_specializationDefect_lowerShriek_upperStar_iso` | DefectExchanges.lean:186: for the open complement j of the centre, C_{X,Z}(j_!j^*L) = C_{X,Z}(L) (existence of an isomorphism only; the docstring notes the map itself is not asserted). |
| `lemma-base-change-maps-external-duality--1` | the declaration's own name | `CategoryTheory.exceptionalTwisted_of_constant` | WeilConjectures/TraceFormula/Specialization/StructuralProduct.lean:54: (a tensor alpha) mu S_V(kappa_M) beta = (b tensor 1) kappa'_{S_W M}, the twisted case (E.10), deduced from the constant case (hypothesis hconst) and (E.8) (hypothesis hET). The constant ca… |
| `lemma-base-change-maps-fixed-point-scheme--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.fixedSquare_of_compactSupportExchange_app` | CompactSupportExchange.lean:297: the fixed-square identity R iota'_* beta_d o chi_iota o Psi_C(B) = B' o Rc'^!(chi_Delta) o beta_c(R Delta_*) given compact-support exchange compatibilities (hypotheses). Clause text equals the parent. |
| `lemma-case-z-v-x-m--1` | partial |  | ThickOriginFiniteModule.lean:146 (docstring cites lemma-case-z-v-x-m): C_{A^1,V(x^m)}(M_X) = 0 for M finite free over a finite ring T killed by a prime ell != char (all finite modules when T is a field); :121 the same for finite direct sums of Qbar_ell. The p… |
| `lemma-compatibilities-base-change-maps--1` | the declaration's own name | `CategoryTheory.whiskerRight_comp_μ_comp_map_comp_mateEquiv_app` | WeilConjectures/TraceFormula/Specialization/ExceptionalTensor.lean:48: (alpha tensor 1) mu_V S_V(t) beta = (1 tensor beta) t' G'(mu_W), for beta the mate of the compact-support exchange nu, given the compatibility h1 of nu with the projection formula. This is… |
| `lemma-composition-exceptional-base-change-maps--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.exceptionalExchange_comp_app` | CompactSupportExchange.lean:132: beta_{ad} = d'^! beta_a o beta_d(a^!) when the compact-support exchange of d >> a is the composite of those of d and a (hypothesis). The concrete proper-model instance is NearbyCyclesModel.IsTraitModelOfGenericBase.exceptional… |
| `lemma-composition-exceptional-base-change-maps--2` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.dualizingExchange_eq_comp` | CompactSupportExchange.lean:229: for d : F -> X and theta defined as dualizingExchange, theta_F = d'^! theta_X o beta_d(omega_X) (through the composition isomorphisms of dualizing complexes), assuming the compact-support exchange of a_F is the composite of th… |
| `lemma-duality-invariants-pro-p--1` | the declaration's own name | `Representation.invariantsDualEquiv`<br>`CategoryTheory.invariantsDualIso`<br>`CategoryTheory.uncurry_invariantsDualIso_hom` | Clause text equals the parent. RepresentationTheory/ProfiniteInvariantsDual.lean:89: Hom_A(E,omega)^G = Hom_A(E^G,omega) for a compact group with invertible open indices (pro-p case, module level). NearbyDualityInvariants.lean:151: (D E)^G = D(E^G) for a fini… |
| `lemma-finite-support-global-sections--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isZero_of_isZero_upperStar_finsetComplOpens` | WeilConjectures/TraceFormula/Specialization/ClosedPointsSupport.lean:483: for X separated of finite type over a separably closed field and a finite set S of closed points, a bounded constructible C with zero restriction to X minus S and zero RGamma(X,C) is ze… |
| `lemma-functoriality-deformation--1` | the declaration's own name | `AlgebraicGeometry.Scheme.IdealSheafData.deformationSpaceMap` | AlgebraicGeometry/DeformationSpace/BaseChange.lean:195: the morphism D_J X' -> D_I X over h : X' -> X for h^*I <= J. |
| `lemma-functoriality-deformation--2` | the declaration's own name | `AlgebraicGeometry.Scheme.IdealSheafData.isClosedImmersion_deformationSpaceToPullback`<br>`AlgebraicGeometry.Scheme.IdealSheafData.isIso_deformationSpaceToPullback_of_flat` | BaseChangeClosedImmersion.lean:291 (J = I.comap h: D_J X' -> X' x_X D_I X is a closed immersion) and :342 (an isomorphism if h is flat). |
| `lemma-functoriality-deformation--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isPullback_zeroSectionSpecialFibreMap` | Specialization/DefectCentreMap.lean:330: the special fibre N_{Z'}X' -> N_Z X pulls the zero section back to the zero section (IsPullback, i.e. schematically), for Z' = f^{-1}Z. |
| `lemma-functoriality-deformation--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isProper_deformationTotalMap`<br>`AlgebraicGeometry.ProEtale.CondensedRing.smooth_deformationTotalMap` | DefectCentreMap.lean:158 and :166: for J = f^{-1}I, the map of total spaces of the deformation models is proper if f is proper, smooth if f is smooth. (Underlying: IdealSheafData.isProper_deformationSpaceMap.) |
| `lemma-kunneth-map-proper-direct-image--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.kunnethMap_comp_pushforwardExchange` | WeilConjectures/SixFunctors/NearbyCycles/KunnethProper.lean:177: R k'_* Pi_{A,B} o kappa o (chi box chi) = chi o Psi_{P1}(kappa) o Pi_{Rg_*A, Rh_*B} for morphisms of models; for proper maps chi are the proper exchange isomorphisms. Clause text equals the pare… |
| `lemma-kunneth-map-slice--1` | partial |  | Identification (E.2) for b: RPsi_X L\|_{s'} = (RPsi_{X'/S'} L')^P. TraitSliceInvariantsProof.lean:179 (docstring: 'generic-slicing identification of nearby cycles with invariants', identification (2)) states that the slicing exchange Lsigma^* Psi_M A -> Psi_{… |
| `lemma-kunneth-map-slice--2` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_pullbackExchange_baseChangeHom_traitMap_of_generic`<br>`AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_pullbackExchange_baseChangeHom_traitMap_padicIntegers`<br>`AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_pullbackExchange_baseChangeHom_traitMap_residueField` | Invariance of nearby cycles under change of trait, RPsi_{Y/S}M\|_{s'} = RPsi_{Y'/S'}M'. TraitChangeInvariance.lean:94 (Qbar_ell), NearbyKunnethSliceIntegral.lean:298 (O_E) and :329 (F_E, finite coefficients): for the change of trait Spec K[[t]] -> Spec k'[[t]… |
| `lemma-kunneth-map-slice--3` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.map_kunnethMap_sliceSpecial_comp_pullbackExchange` | NearbyKunnethSliceSquare.lean:68, docstring cites lemma-kunneth-map-slice: identifying the restrictions over s' of the nearby cycles of A, B, A box B with those of the slices through the pullback exchanges ((E.2) for b, change of trait, (E.2) for b o pr1), th… |
| `lemma-kunneth-map-slice--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_map_kunnethMap_of_isIso_sliceFst_residueField`<br>`AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_map_kunnethMap_of_isIso_sliceFst_padicIntegers` | NearbyKunnethSliceTorsion.lean:167 (F_E coefficients) and NearbyKunnethSliceIntegralStep.lean:79 (O_E): if the Kunneth map of the geometric slice is invertible, so is the pullback of Pi_{A,B} to the special fibre of the slice of P. This is exactly the 'in par… |
| `lemma-nearby-cycles-universal-kernel--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.map_kunnethVerdierMap_comp_eq` | WeilConjectures/TraceFormula/Specialization/UniversalKernelFirst.lean:64: h o Sp(lambda_K) = lambda_{K'} o rho for any h whose uncurry is (alpha_{p2} tensor 1) mu Sp(ev) beta_{p1}, given the compatibility hkappa of beta_{p1} with the exceptional Kunneth maps … |
| `lemma-nearby-cycles-universal-kernel--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.universalKernelSpecialization_comp_evaluationKernel` | UniversalKernelDiagonal.lean:135: e_{K'} o rho = R Delta_{s*} theta_X o chi_Delta o S(e_K), K' = Sp_{X,x}(K). Exactly the second identity. |
| `lemma-nearby-duality-proper-direct-image--1` | the declaration's own name | `CategoryTheory.Verdier.nearbyDualityMap_proper` | WeilConjectures/TraceFormula/Specialization/NearbyDualityMap.lean:173 (docstring det-tf-nearby-duality-proper (1)): for lax monoidal G = Rf_eta*, G' = Rf_s* with traces and exchange chi satisfying the monoidal and trace compatibilities, Psi_Y(G D M -> D G M) … |
| `lemma-nearby-duality-proper-direct-image--2` | the declaration's own name | `CategoryTheory.Verdier.nearbyDualityMap_restrict` | NearbyDualityMap.lean:259 (det-tf-nearby-duality-proper (2)): for F = j_eta^*, F' = j_s^* and a monoidal exchange alpha compatible with the dualizing maps, j_s^* delta_{X,M} is identified with delta_{U,j^*M} under alpha. Abstract form, compatibilities as hypo… |
| `lemma-nearby-duality-proper-direct-image--3` | partial |  | NearbyDualityCompactification.lean:114 (parent's own name): for X, X' and the total space proper, RGamma(X', delta_{M,K}) is an isomorphism; the docstring says it is identified with the identity of RHom(RGamma(X_etabar,K),Qbar_ell), but the statement only ass… |
| `lemma-nearby-duality-slice--1` | partial |  | NearbyDualityGenericBaseSlice.lean:162 (parent's own name; clause text equals the parent): assuming the twist equation H (TwistEquation) and that the slice duality maps are isomorphisms, the pullback of delta_{M,L} to the special fibre of the slice is an isom… |
| `lemma-normal-cones-contracting-ideals--1` | project lemma | `AlgebraicGeometry.Scheme.IdealSheafData.normalConeMap`<br>`AlgebraicGeometry.Scheme.IdealSheafData.normalConeMap_normalConeToDeformationSpace` | The lifts c~_i : D_{Z'}C -> D_Z X are deformationSpaceMap h I J hJ (AlgebraicGeometry/DeformationSpace/BaseChange.lean:195, for h^*I <= J; already on lemma-functoriality-deformation, hence a conflict). Their special fibres gamma_i are normalConeMap (NormalCon… |
| `lemma-normal-cones-contracting-ideals--2` | partial |  | NormalConeMap.lean:313 (parent's own name): if J = h^*I . O_{X'}, the preimage of the zero section of N_I X under N_J X' -> N_I X is the zero section of N_J X', set-theoretically only. The scheme-theoretic equality gamma_1^{-1}(Z) = Z' is not stated (LEAN-MAP… |
| `lemma-normal-cones-contracting-ideals--3` | the declaration's own name | `AlgebraicGeometry.Scheme.IdealSheafData.range_normalConeMap_subset_range_normalConeZeroSection` | NormalConeMap.lean:266: if h^*I <= J and (h^*I)^n <= J^{n+1} with n > 0, then range(N_J X' -> N_I X) is contained in the range of the zero section, set-theoretically. Exactly the clause. |
| `lemma-section-specialized-correspondence--1` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.IsContractingAt.map_exceptionalHomIso_inv_comp_supportHomSpecialization_of_kunneth` | SpecializedCorrespondenceSection.lean:147 (file docstring cites lemma-section-specialized-correspondence): h_c Psi_C(lambda_{c_eta,K}) = lambda_{c_s,K'} c_s^! rho beta_c(P_X), with the first universal-kernel identity discharged; remaining hypotheses are the c… |
| `lemma-section-specialized-correspondence--2` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.IsContractingAt.curry_comp_eq_supportSpecializationUnit_comp_map_comp` | SpecializedCorrespondenceSection.lean:183 (docstring cites lemma-section-specialized-correspondence, second part): if k_u corresponds to u then u_s = beta_{c1} Psi_C(u) alpha_{c2} corresponds to c_s^! rho beta_c Psi_C(k_u) sigma_C, written with sigma_C as in … |
| `lemma-vanishing-generic-points-principal-divisor--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.exists_dense_isZero_specializationDefect` | DefectGenericDivisor.lean:92: X normal, Z = V(h) principal, i^*L = 0 implies the defect vanishes on a dense open of Z (hence at all generic points). Qbar_ell coefficients. Clause text equals the parent. |
| `proposition-external-kunneth-formula-nearby-cycles--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_kunnethMap` | WeilConjectures/TraceFormula/Specialization/NearbyKunneth.lean:90 states that the Kunneth map of nearby cycles Psi_M A box Psi_N B -> Psi_P(A box B) is an isomorphism for the product P of trait models of finite type, for bounded constructible A, B. The clause… |
| `proposition-nearby-cycles-commute-verdier-duality--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_nearbyDualityMap` | WeilConjectures/TraceFormula/Specialization/NearbyDualityLocal.lean:89: the duality map delta_{M,K} : Psi D K -> D Psi K is an isomorphism for trait models of a base (Qbar_ell coefficients). Clause text equals the parent. |
| `proposition-specialization-trace-class--1` | inside a proof |  | Lean's vanishing route never needs u_s as a coefficient of c'. |
| `proposition-specialization-trace-class--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.TraceSpecialization.sp` | Specialization/Basic.lean:208: sp z = sigma_F >> Psi_F.map z >> theta_F, i.e. sp_F(z) = theta_F Psi_F(z) sigma_F. Exactly the definition clause. |
| `proposition-specialization-trace-class--3` | different route |  | Lean takes the vanishing route: it never compares with the trace class of u_s. It shows that sp of the trace class vanishes when the specialized universal kernel vanishes, then uses injectivity of sp on the point component (exists_traceSpecialization) to get … |
| `theorem-contracting-correspondences-local-terms--1` | partial |  | ContractingLocalTerm.lean:80 (the parent's own name): only for Z = {x} a rational point with C_Z the reduced point y (IsContractingAt): Tr_c(u)\|_B = e_*(Tr_{c_Z}(u_Z)). General closed Z, the neighbourhood W, and the statement that h_{F0} is an isomorphism af… |
| `theorem-contracting-correspondences-local-terms--2` | partial |  | Only the point case is stated: ContractingGraph.lean:145 gives LT_B(u) = integral of Tr(u_Z) for Z = {x}, F0 = B proper with underlying set {y}; it is the lean name of corollary-contracting-local-terms-point (--1), hence listed as a conflict. LT_{F0}(u) = LT_… |
| `theorem-verdier-s-theorem-specialization-zero--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isIso_zeroSectionMap` | WeilConjectures/TraceFormula/Specialization/ZeroSectionVanishing.lean:98: epsilon_{X,Z}(L) : Le^* Sp_{X,Z}(L) -> Psi_{Z x S}(Li^* L) is an isomorphism for every closed Z = V(I) and bounded constructible Qbar_ell L. Equivalent form isZero_specializationDefect … |
| `theorem-verdier-s-theorem-specialization-zero--2` | partial |  | Specialization/NearbyCycles.lean:114 (parent's own name): if K_x = 0 then the restriction of Sp_{X,x}(K) to the zero section vanishes; only for Z a rational point x. For general Z the vanishing follows in one step from isIso_zeroSectionMap but is not stated s… |

### chap-The-Deligne-Laumon-theorem-for-curves

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `lemma-finite-generically-etale-map-line--1` | the declaration's own name | `AlgebraicGeometry.AffineSpace.exists_isOpenImmersion_isFinite_etale_morphismRestrict` | WeilConjectures/AlgebraicGeometry/Curve/FiniteMapToLine.lean:296 exists_isOpenImmersion_isFinite_etale_morphismRestrict (parent name): for C smooth affine geometrically connected curve over a finite field, there are C' smooth geometrically connected containin… |
| `lemma-finite-generically-etale-map-line--2` | the declaration's own name | `AlgebraicGeometry.WeilSheaf.isLisse_and_isPunctuallyPureOfWeight_upperStar_lowerStar_extensionByZero` | WeilConjectures/DeligneLaumon/AffineLine/AffineCurveUpper.lean:395 (parent name): for j : C -> C' quasi-compact open immersion, g : C' -> Y finite, W open over which g is etale with g^{-1}W in C, F lisse and punctually iota-pure of weight w, the restriction o… |
| `lemma-finite-generically-etale-map-line--3` | the declaration's own name | `AlgebraicGeometry.WeilSheaf.nonempty_equiv_compactlySupportedCohomology_lowerStar_extensionByZero` | WeilConjectures/DeligneLaumon/Reduction/FiniteMap.lean:78 (parent name): H^i_c(C, F) = H^i_c(Y, g_* j_! F) as Frobenius modules, for every i (j open immersion, g finite). Degreewise isomorphisms (Nonempty) rather than a canonical identification of RGamma_c co… |
| `lemma-fourier-transform-boundary-sequence--2` | the declaration's own name | `AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.isLisse`<br>`AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.hasWeightsAtMost` | WeilConjectures/DeligneLaumon/AffineLine/ZeroExtension.lean:369 FourierCorrection.isLisse (parent name): the correction sheaf B' = c.seq.X_1 is lisse on the whole dual line; :379 FourierCorrection.hasWeightsAtMost (parent name): B' has weights at most w when … |
| `lemma-weight-bound-constant-extension--1` | partial |  | WeilConjectures/ZetaLinearAlgebra/FrobeniusModule/Exact.lean:168 HasWeightsAtMost.of_powFrobenius (parent's only name): for an abstract Frobenius module M and m != 0, weights <= b for F^m over q^m imply weights <= b over q (the 'if' direction only). :148 hasE… |
| `theorem-weight-bound-affine-curve--1` | the declaration's own name | `AlgebraicGeometry.hasWeightsAtMostOver_compactlySupportedCohomology_of_isAffine_of_isLisse` | WeilConjectures/DeligneLaumon/Reduction/AffineCurve.lean:207 (parent name): for C smooth geometrically connected affine curve and F lisse punctually iota-pure of weight w, H^r_c(C,F) has weights at most w + r for all r (r = 1 is the clause), plus vanishing/pu… |
| `theorem-weight-bound-affine-line--1` | project lemma | `AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.hasWeightsAtMostOver_compactlySupportedCohomology_one` | WeilConjectures/DeligneLaumon/AffineLine/Upper.lean:150 LisseOnDenseOpen.hasWeightsAtMostOver_compactlySupportedCohomology_one: for D = (j : U0 -> A^1 dense open, F lisse) unramified at infinity and F punctually iota-pure of weight w, H^1_c(A^1, j_*F) has wei… |
| `theorem-weight-bound-curve--1` | partial | `AlgebraicGeometry.hasWeightsAtMostOver_compactlySupportedCohomology_directImage_of_isCurve` | RESTRICTION-ONLY (same restriction as the parent's names): WeilConjectures/DeligneLaumon/Reduction/OpenLine.lean:62 (parent name): for j : U -> C a dense open immersion of smooth curves and F lisse punctually iota-pure of weight w, H^r_c(C, j_*F) has weights … |
| `theorem-weight-bound-curve--2` | partial | `AlgebraicGeometry.hasWeightsAtMostOver_compactlySupportedCohomology_of_isCurve` | RESTRICTION-ONLY (same restriction as the parent's names): WeilConjectures/DeligneLaumon/Reduction/OpenLine.lean:169 (parent name): for C smooth geometrically connected separated quasi-compact curve and F lisse punctually pure of weight w, H^r_c(C,F) has weig… |
| `theorem-weight-fourier-transform--1` | the declaration's own name | `AlgebraicGeometry.isPunctuallyPureOfWeight_add_one_of_isFourierPartner` | WeilConjectures/DeligneLaumon/AffineLine/FourierWeight.lean:198 (parent's only name): for M nonzero irreducible nonexceptional lisse, punctually iota-pure of weight w, and its Fourier partner M', M' is punctually iota-pure of weight w + 1. The single clause i… |

### chap-The-Deligne-Laumon-theorem-in-general

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `corollary-curve-preserving-geometric-irreducibility--1` | the declaration's own name | `AlgebraicGeometry.WeilSheaf.exists_isClosedImmersion_isIrreducibleLocalSystem_upperStar` | WeilConjectures/DeligneLaumon/Reduction/CurveTesting.lean:152 (parent's only name): X0 smooth geometrically connected affine of dimension >= 1, Weil sheaves with geometrically irreducible local-system restrictions, finite set S of kbar-points: closed immersio… |
| `lemma-detecting-irreducibility-finite-quotient--1` | the declaration's own name | `Representation.exists_forall_isIrreducible_baseChange_of_congr` | WeilConjectures/RepresentationTheory/FiniteMatrixWitness.lean:176 (parent's only name): a representation with matrices in O (a lattice), absolutely irreducible: there is N such that every subgroup whose matrices are congruent mod m^N to all of rho(G) acts abs… |
| `lemma-geometric-constituents-after-constant-extension--1` | the declaration's own name | `Representation.exists_filtration_isIrreducible_restrict` | WeilConjectures/RepresentationTheory/Clifford.lean:396 (parent's only name): representation of W over an algebraically closed field, normal subgroup P (geometric fundamental group) and F in W: there are m >= 1 and a finite chain of subspaces stable under P an… |
| `lemma-relative-noether-normalization-over-stratification--1` | the declaration's own name | `AlgebraicGeometry.exists_partition_isFinite_toIteratedAffineLine` | WeilConjectures/AlgebraicGeometry/NoetherNormalization.lean:606 (parent's only name): for f : X -> Y of finite type to a Noetherian Y, finite partitions of X and Y into reduced locally closed pieces, each source piece mapping to a target piece through a finit… |
| `lemma-weight-bounds-partitions--2` | the declaration's own name | `AlgebraicGeometry.HasDirectImageWeightBound.of_openClosed_target` | WeilConjectures/DeligneLaumon/Reduction/FormalSteps.lean:592 HasDirectImageWeightBound.of_openClosed_target (parent's only name): for V open with closed complement T in Y and the base changes f_V, f_T, if the direct-image weight bound holds for f_V and f_T th… |

### chap-The-Fourier-transform

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `lemma-artin-schreier-character-sheaf--1` | the declaration's own name | `AlgebraicGeometry.artinSchreier`<br>`AlgebraicGeometry.isLisse_artinSchreier`<br>`AlgebraicGeometry.WeilSheaf.finrank_stalk_artinSchreier`<br>`AlgebraicGeometry.nonempty_artinSchreier_zero_iso_adicConstant` | Parent names: WeilConjectures/WeilSheaf/Fourier.lean:902 def artinSchreier psi a (pullback along x -> a x of the psi-isotypic part of the Artin-Schreier cover u^q - u = x with group k0); :1202 isLisse_artinSchreier; WeilSheaf/ArtinSchreierPurity.lean:162 finr… |
| `lemma-artin-schreier-character-sheaf--4` | not formalized |  | Lean never needs normalized isomorphisms: all Fourier statements are up to (non-specified) isomorphism (Nonempty). |
| `lemma-artin-schreier-character-sheaf--5` | not formalized |  | As for --4: only existence of isomorphisms is used. |
| `lemma-fourier-transform-constant-sheaf--1` | the declaration's own name | `AlgebraicGeometry.nonempty_iso_fourierTransform_obj_adicConstant` | WeilConjectures/WeilSheaf/FourierFirstFormula.lean:227 nonempty_iso_fourierTransform_obj_adicConstant (parent name): for psi nontrivial, FT_psi(Qbar_l) = (delta_0(-1))[-1] on the affine line over k0, exactly the clause (V = A^1_{k0}). E = Qbar_l (PadicAlgCl). |
| `lemma-fourier-transform-constant-sheaf--2` | the declaration's own name | `AlgebraicGeometry.nonempty_iso_fourierTransform_obj_delta` | WeilConjectures/WeilSheaf/FourierFirstFormula.lean:172 nonempty_iso_fourierTransform_obj_delta (parent name): FT_psi(delta_0) = Qbar_l[1] on the affine line over k0 (no nontriviality needed). |
| `lemma-integral-linear-character--1` | partial |  | WeilConjectures/WeilSheaf/FourierInversion/OtherSections.lean:97 WeilComplex.nonempty_iso_upperStar_comp_derivedLowerShriek_of_isPullback (parent name): for the trivial line bundle pi : Y = X x A^1 -> X, R pi_! pi^* P = P(-1)[-2] (relative, Weil coefficients,… |
| `lemma-integral-linear-character--2` | partial |  | WeilConjectures/WeilSheaf/FourierInversion/Vanishing.lean:309 WeilComplex.isZero_derivedLowerShriek_tensorLisse_artinSchreierOf_upperStar (parent name): R pi_!(L_psi(a s) (x) pi^*P) = 0 for the trivial line bundle and a a unit (r = 1, relative, Weil coefficie… |
| `lemma-integral-linear-character--3` | not formalized |  | Not needed: Lean's Fourier statements are up to unspecified isomorphism. |
| `lemma-largest-punctual-subsheaf--2` | inside a proof |  | Inline kernel of the unit G -> j_* j^* G. |
| `lemma-largest-punctual-subsheaf--3` | partial |  | WeilConjectures/DeligneLaumon/AffineLine/DirectImageUnit.lean:80 support_finite_kernel_unit_app (parent name): ker(G -> j_*j^*G) is punctual (finite support), for a dense open j of the affine line. :116 eq_zero_of_support_finite_lowerStar: every map from a pu… |
| `lemma-largest-punctual-subsheaf--4` | not formalized |  | Lean works with sheaves already without punctual subsheaves (hypothesis hG in mono_unit_app) instead of passing to F/F_p. |
| `lemma-largest-punctual-subsheaf--5` | not formalized |  | Not needed in the Lean route. |
| `lemma-perverse-sheaves-curve--1` | partial |  | WeilConjectures/DeligneLaumon/AffineLine/Perverse.lean:146 isCurvePerverseLower_iff_forall_hom_eq_zero (parent name): on a smooth curve the lower class is the right orthogonal of pD^{<=-1} (the orthogonality axiom of a t-structure). The module docstring (line… |
| `lemma-simple-objects--2` | partial |  | WeilConjectures/DeligneLaumon/AffineLine/Perverse.lean:675 WeilComplex.eq_zero_or_isIso_of_mono_middleExtension: every monomorphism Q -> P = (j_*N)[1] in the curve perverse full subcategory (N irreducible lisse) is 0 or an isomorphism; hence no nonzero punctu… |
| `proposition-base-change-fourier-inversion--1` | partial |  | WeilConjectures/FourierTransform/Properties/BaseChange.lean:90 (namespace AlgebraicGeometry.Etale, :35) nonempty_iso_fourierTransform_baseChange: for cartesian squares over g : S' -> S, FT_psi(u^* K) = u'^* FT_psi(K) naturally, for a general pairing V x_S V' … |
| `proposition-fourier-inversion--2` | partial | `AlgebraicGeometry.nonempty_iso_fourierTransform_comp_self` | RESTRICTION-ONLY (same restriction as the parent's names): WeilConjectures/WeilSheaf/FourierInversion/Reflection.lean:261 nonempty_iso_fourierTransform_comp_self (parent name): for nontrivial psi, FT_psi o FT_psi = [-1]^* ((-)(-1)[-2])[1][1] naturally, i.e. F… |

### chap-The-Lefschetz-Verdier-formula

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `lemma-closed-piece-pushforward--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.upperStar_map_unit_comp_restrictedClosedPieceCoeff` | Clause = parent text. AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.upperStar_map_unit_comp_restrictedClosedPieceCoeff (WeilConjectures/TraceFormula/ContractingClosedPiece.lean:334): the pushforward (restrictedClosedPieceDiagram hy sq).pushforwardCo… |
| `lemma-lift-correspondence-invariant-decomposition--1` | partial |  | No filtered-derived-category lift. Only for Z a rational point x: pointOpenPieceCoeff (WeilConjectures/TraceFormula/ContractingPieces.lean:138) defines u_U; parent name pointOpenPieceCoeff_comp_map_counit (ContractingOpenPiece.lean:172) is the open square Rc1… |
| `lemma-local-terms-point--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.integral_traceClass_ofEnd` | Clause = parent text. AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.integral_traceClass_ofEnd (WeilConjectures/TraceFormula/PointNormalization.lean:103): integral over s of Tr(ofEnd K v) = trace v for dualizable K on the point (Qbar_l coefficients r… |
| `proposition-additivity-trace-classes--1` | different route |  | Triangulated-category argument (comp_eq_add_of_distTriang on rows K'⊠N→K⊠N→K''⊠N) with Hom-vanishing hypotheses, discharged by support considerations in the open-closed point case (traceClass_eq_add_of_isPullback). |
| `proposition-exceptional-external-kunneth--1` | the declaration's own name | `AlgebraicGeometry.Etale.nonempty_iso_externalProduct_rightDerivedUpperShriek` | Clause = parent text. AlgebraicGeometry.Etale.nonempty_iso_externalProduct_rightDerivedUpperShriek (WeilConjectures/SixFunctors/Etale/Derived/Kunneth/Exceptional.lean:187) for constructible finite-Tor N_i. Caveat: Lean states Nonempty (Rf1^!N1 ⊠ Rf2^!N2 ≅ R(f… |
| `proposition-properties-trace--4` | the declaration's own name | `DerivedCategory.trace_eq_algebraMap_sum_negOnePow_linearMapTrace` | Parent name DerivedCategory.trace_eq_algebraMap_sum_negOnePow_linearMapTrace (WeilConjectures/CategoryTheory/DerivedCategory/PerfectTrace.lean:158): categorical trace = sum (-1)^i Tr(v^i \| P^i). Caveat: components assumed Module.Free + finite (not finite pro… |
| `proposition-properties-trace--5` | the declaration's own name | `DerivedCategory.trace_eq_trace_add_trace_of_shortExact` | Parent name DerivedCategory.trace_eq_trace_add_trace_of_shortExact (WeilConjectures/CategoryTheory/DerivedCategory/TraceLaws.lean:59): for a short exact sequence 0→P'→P→P''→0 of bounded complexes of finite free modules with endomorphism (v',v,v''), tr(v\|P)=t… |
| `proposition-properties-trace--6` | the declaration's own name | `DerivedCategory.trace_eq_algebraMap_sum_negOnePow_trace_homologyMap` | Parent name DerivedCategory.trace_eq_algebraMap_sum_negOnePow_trace_homologyMap (WeilConjectures/CategoryTheory/DerivedCategory/TraceLaws.lean:113): over a field, tr(v\|P) = sum (-1)^i Tr(H^i(v)\|H^i(P)). |
| `theorem-proper-pushforward-lefschetz-verdier--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.BorelMooreSection.integral_eq_sum_localTerm` | Parent name AlgebraicGeometry.ProEtale.CondensedRing.BorelMooreSection.integral_eq_sum_localTerm (WeilConjectures/TraceFormula/LocalTerm.lean:455): for X proper and a finite clopen decomposition j_b : B_b → X, ∫_X α = Σ_b LT_{B_b}(α); applied to α = Tr_c(u) i… |

### chap-The-Picard-scheme-of-a-curve

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `corollary-torsion-jacobian-field-extension--4` | inside a proof |  | Lean goes straight to Pic(C)[n] = (Z/n)^{2g} via Pic(C) = Z x J(k) (exists_jacobian_addEquiv_prod). |
| `definition-relative-picard-functor--2` | Mathlib | `CategoryTheory.Functor.RepresentableBy` | No project definition 'Picard scheme'. Lean expresses 'J is a Picard scheme' as (picardFunctor f).RepresentableBy J (resp. for picardFunctorDegree), using Mathlib's structure Mathlib/CategoryTheory/Yoneda.lean:284 Functor.RepresentableBy (namespace CategoryTh… |
| `lemma-coherent-base-change-invertible-sheaves--2` | partial |  | The derived base-change isomorphism L a^* R f_* L = R f'_* L' is not stated; WeilConjectures/AlgebraicGeometry/Cohomology/DirectImage/PerfectLocusOfRank.lean:43-45 says the canonical base-change map 'is not available'. Closest: Cohomology/DirectImage/FiniteFr… |
| `lemma-rigidification-along-section--1` | the declaration's own name | `AlgebraicGeometry.picardFunctorNormalized`<br>`AlgebraicGeometry.bijective_toPicardFunctor_picardFunctorNormalized`<br>`AlgebraicGeometry.isIso_picardFunctorNormalized_ι_comp_toPicardFunctor` | WeilConjectures/AlgebraicGeometry/Picard/Defs.lean:356 def picardFunctorNormalized f sigma: the subfunctor of classes L in Pic(C_T) with sigma_T^* L trivial; :913 bijective_toPicardFunctor_picardFunctorNormalized: under (*) (pushforwardUnitMap iso for every T… |
| `lemma-tangent-space-picard-functor--1` | the declaration's own name | `AlgebraicGeometry.Scheme.exists_addEquiv_ker_picMap_dualNumbersι` | WeilConjectures/AlgebraicGeometry/Picard/DualNumbers.lean:283 (parent's only name): ker(Pic(X[eps]) -> Pic(X)) = H^1(X, O_X) as additive groups, compatibly with the scalar actions. Single clause = whole parent. |
| `lemma-twisting-h-0-1-h--1` | the declaration's own name | `AlgebraicGeometry.Scheme.exists_isInvertible_twist` | WeilConjectures/AlgebraicGeometry/Curve/RiemannRoch.lean:2024 exists_isInvertible_twist (parent's only name): k separably closed, X connected (smooth proper curve section variables), L invertible on X_K: there is L0 invertible on X with h^0(X_K, L (x) L0_K) =… |
| `proposition-h-1-curve-tate-module--1` | the declaration's own name | `AlgebraicGeometry.JacobianTorsionDatum.kummerEquiv`<br>`AlgebraicGeometry.JacobianTorsionDatum.kummerEquiv_restrictMuH`<br>`AlgebraicGeometry.JacobianTorsionDatum.kummerEquiv_map_rootsOfUnityPowMap` | WeilConjectures/EtaleCohomology/Purity/RealSheaves/JacobianKummer.lean:107 def kummerEquiv: H^1(C, mu_{l^n}) = J0(Kbar)[l^n]; :123 kummerEquiv_restrictMuH: Galois-equivariance; :144 kummerEquiv_map_rootsOfUnityPowMap: z -> z^l corresponds to multiplication by… |
| `proposition-h-1-curve-tate-module--2` | partial |  | WeilConjectures/EtaleCohomology/Purity/RealSheaves/JacobianKummer.lean:144 kummerEquiv_map_rootsOfUnityPowMap (parent name): the finite-level isomorphisms are compatible with the transition maps (docstring: 'Hence they form a compatible system identifying lim… |
| `theorem-picard-scheme-jacobian-over-separably--4` | the declaration's own name | `AlgebraicGeometry.nonempty_tangentSpaceAt_linearEquiv_H_one` | WeilConjectures/AlgebraicGeometry/Picard/Jacobian.lean:1496 (parent name): for X smooth proper geometrically integral curve over a separably closed k and J representing Pic^0 compatibly with group laws, the tangent space of J at the unit is k-linearly isomorp… |

### chap-The-pro-etale-site

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `corollary-bounded-below-classical-complexes--1` | partial |  | WeilConjectures/SixFunctors/ProEtale/FullCohomologicalDimension.lean:214 etaleOrigin_of_shortExact: sheaves of étale origin (the essential image of ν^*) are closed under extensions. WeilConjectures/Mathlib/CategoryTheory/ObjectProperty/EssImageKernels.lean:32… |
| `corollary-bounded-below-classical-complexes--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.classicalDerivedEquivalence` | WeilConjectures/AlgebraicGeometry/Classical/ClassicalDerivedEquivalence.lean:84 (parent name): an equivalence between D^+(X_ét, Λ) and bounded-below classical complexes (ClassicalPlus X Λ), given by ν^* and Rν_*. Caveat: it assumes as a hypothesis (hunit) tha… |
| `corollary-cohomology-pro-etale-affine--1` | partial |  | WeilConjectures/SixFunctors/ProEtale/Comparison/CohomologyLimit.lean:186 and :205, the parent's own names; the clause repeats the parent statement. They give H^q(X_proét, ν^*(F\|_X)) = colim_i H^q((X_i)_proét, ν^*(F\|_{X_i})) for a cofiltered qcqs system with… |
| `corollary-evaluation-weakly-contractible-objects--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.isZero_rightDerived_sectionsFunctor_of_isWeaklyContractible` | WeilConjectures/SixFunctors/ProEtale/GaloisAcyclic/WContractible.lean:54: IsZero (((sectionsFunctor W).rightDerived (q+1)).obj F) for W weakly contractible and F a sheaf of Λ-modules, Λ any ring (abelian sheaves are the case Λ = ℤ). That is, H^q(W,F) = 0 for … |
| `corollary-evaluation-weakly-contractible-objects--3` | not formalized |  | The Lean parent stops at vanishing of the higher derived functors (clause 2). |
| `corollary-evaluation-weakly-contractible-objects--4` | partial |  | CategoryTheory.peSectionsLimitsColimits (WeilConjectures/AlgebraicGeometry/ProEtaleSectionsLimitsColimits.lean:275), first conjunct: SheafOfModules.evaluation R (op W) preserves limits of any size, for W affine weakly contractible. That is exactly the clause,… |
| `corollary-evaluation-weakly-contractible-objects--6` | partial |  | AlgebraicGeometry.Scheme.ProEt.sections_conservative (WeilConjectures/AlgebraicGeometry/ProEtale/SectionsConservative.lean:149): its conjuncts 1-2 are exactly this clause (exactness of short complexes, and acyclicity of unbounded complexes of R-module sheaves… |
| `definition-classical-pro-etale-sheaves--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.IsClassicalModuleComplex`<br>`AlgebraicGeometry.ProEtale.IsClassicalComplex`<br>`AlgebraicGeometry.ProEtale.IsClassicalComplexFor` | WeilConjectures/CategoryTheory/Integral/ClassicalModuleDefinition.lean:42 `def IsClassicalModuleComplex K := ∀ q, IsClassicalModuleSheaf (H^q K)`, the parent name, for module sheaves over a ring sheaf R. Two unclaimed variants state the same definition for ot… |
| `definition-cohomological-dimension--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.cohomologicalDimension` | WeilConjectures/AlgebraicGeometry/Cohomological/CohomologicalDimension.lean:656. cohomologicalDimension ℓ hℓ X is the sSup of the n for which some classical, ℓ-power-torsion abelian pro-étale sheaf has nonzero H^n. The supremum is taken in WithTop ℕ. This is … |
| `definition-cohomological-dimension--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.relativeCohomologicalDimension` | CohomologicalDimension.lean:665. relativeCohomologicalDimension ℓ hℓ g, for g qcqs, is the sSup of the n for which some classical ℓ-power-torsion F has H^n(Rg_* F) ≠ 0. This is cd_ℓ(g). |
| `definition-cohomological-dimension--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.cohomologicalDimension` | This is a notation clause. The docstring of cohomologicalDimension (CohomologicalDimension.lean:650-655) defines cd_ℓ(K) for a field K as the expression at Spec (.of K), and Lean writes it as cohomologicalDimension ℓ hℓ (Spec (.of K)). There is no separate de… |
| `definition-local-cohomology--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.closedSupport` | CondensedClosedSupportAdjunction.lean:115 `def closedSupport i j := supportKernel Λ j ⋙ supportPullback Λ i`, i.e. i^* ker(F → j_*j^*F); supportKernel (:98) is the kernel of the open unit. The derived functor RΓ_Z has no name of its own and is used as (closed… |
| `definition-repleteness--1` | the declaration's own name | `CategoryTheory.GrothendieckTopology.IsReplete` | WeilConjectures/CategoryTheory/RepleteSheafTopos.lean:40 (parent name). It is exactly the definition: for an inverse sequence of sheaves of sets with epimorphic transition maps, the limit projections are epimorphisms. The single clause equals the parent. |
| `definition-tate-twists--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.spFiniteTwist` | WeilConjectures/AlgebraicGeometry/ProEtale/Tate/ProEtaleTateTwistLevelsSupplement.lean:164: spFiniteTwist A r hA := Scheme.tateFiniteLine X ℓ A r …, i.e. μ_{ℓ^{r+1}} ⊗ A_X for finite A with ℓ^{r+1}A = 0. The index is shifted: r stands for the exponent r+1. Pa… |
| `definition-tate-twists--4` | project lemma | `AlgebraicGeometry.ProEtale.spFiniteKummer_existsUnique`<br>`AlgebraicGeometry.ProEtale.spFiniteKummer` | WeilConjectures/AlgebraicGeometry/ProEtale/Tate/ProEtaleTateTwistConstructionsSupplement.lean:616 spFiniteKummer_existsUnique: for r ≤ n, there is a unique morphism tateFiniteLine … n ⟶ tateFiniteLine … r that is an isomorphism and acts as the root power map … |
| `definition-tate-twists--7` | the declaration's own name | `AlgebraicGeometry.ProEtale.spQbarTwist` | ProEtaleTateTwistConstructionsSupplement.lean:602 spQbarTwist. Its underlying sheaf spQbarTwistAb (:443) is the colimit of spRationalTwistDiagram (:433), E ↦ E_X(1), with the unique compatible Qbar_X-action. That is exactly Qbar_X(1) = colim_E E_X(1). Parent … |
| `definition-tate-twists--9` | partial |  | WeilConjectures/TateTwist/ProEtale.lean:150: tateTwistOne := extendScalars along ℤ_ℓ,X → Qbar_X of tateModule (= lim μ_{ℓ^n}). This defines only the right-hand side Qbar_X ⊗ ℤ_ℓ,X(1), and it is a parent name. No declaration compares it with the colimit constr… |
| `definition-tate-twists--13` | the declaration's own name | `AlgebraicGeometry.ProEtale.spInternalComplexTwist` | WeilConjectures/AlgebraicGeometry/Internal/InternalSignedTateTwist.lean:42: spInternalComplexTwist X R L K d := K ⊗ (singleFunctor 0).obj (spInternalSignedTwist X R L d), the derived tensor product with Λ_X(d) placed in degree 0, i.e. K(d). Parent name. |
| `lemma-cohomological-dimension-base-field--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.cohomologicalDimension_baseField` | WeilConjectures/AlgebraicGeometry/Base/BaseFieldCohomologicalDimension.lean:100, first conjunct: if K is algebraically closed, cohomologicalDimension ℓ hℓ (Spec K) = 0. |
| `lemma-cohomological-dimension-base-field--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.cohomologicalDimension_baseField` | BaseFieldCohomologicalDimension.lean:100, second conjunct: if K is finite, cohomologicalDimension ℓ hℓ (Spec K) ≤ 1. |
| `lemma-comparison-completed-coefficients--1` | project lemma | `AlgebraicGeometry.ProEtale.sfb_normalized_integral_quotient_cone` | WeilConjectures/AlgebraicGeometry/ProEtale/ProEtaleNormalizedIntegralTower.lean:254. Let R be a compact Hausdorff ring and I an ideal whose finite quotients R/I^n separate points. The lemma gives a cone R̲ → (R/I^n) that is a limit of ring objects after p_X^*… |
| `lemma-comparison-completed-coefficients--2` | project lemma | `AlgebraicGeometry.ProEtale.completedCondensedRational` | WeilConjectures/AlgebraicGeometry/Completed/CompletedCondensedCoefficients.lean:1399. For each finite E it gives the ℓ-telescope legs O_{E,X} → E_X, with j 0 the inclusion and ℓ·j(n+1) = j(n), and ℓ invertible on E_X. It proves the universal property E_X = O_… |
| `lemma-comparison-completed-coefficients--3` | project lemma | `AlgebraicGeometry.ProEtale.isColimitPadicAlgClRingObjCocone` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Colimit/Compatibility.lean:715: IsColimit (padicAlgClRingObjCocone X ℓ). The inclusions E_X → Qbar_X exhibit Qbar_X as the filtered colimit of the E_X in abelian pro-étale sheaves. It is the image under p_X^* … |
| `lemma-comparison-completed-coefficients--4` | partial |  | WeilConjectures/AlgebraicGeometry/ProEtale/ProEtaleCompletedCoefficients.lean:299 (parent name). Compatibility with f^* appears only as conjuncts: the f^*-limit and f^*-leg fields of SfbCompletedCoefficientComparison, and the last two conjuncts of the parent … |
| `lemma-comparison-direct-images-compatibilities--1` | partial |  | WeilConjectures/SixFunctors/ProEtale/BaseChange/ComparisonUnit.lean:72 `comparison_unit`. For qcqs f and G ∈ D⁺(V_ét, Λ) it states ν^*(unit_G) ≫ c_f ≫ Rf_*(β) = unit at ν^*G. Here c_f is rightDerivedLowerStarComparisonIso', built from rightDerivedFunctorPlusB… |
| `lemma-comparison-direct-images-compatibilities--2` | partial |  | WeilConjectures/AlgebraicGeometry/FixedComparisonDirectImageMate.lean:110 `fixedComparisonDirectImageMatePlus_counit` (parent name) states β ≫ f^*(c_f) ≫ counit = ν^*(étale counit) on D⁺, with c_f = rightDerivedFunctorPlusBaseChange (lowerStarComparisonUpperS… |
| `lemma-comparison-direct-images-compatibilities--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.comparisonDirectImagePlus_comp` | WeilConjectures/AlgebraicGeometry/Comparison/ComparisonDirectImage.lean:528. For any ring Λ and any f : U ⟶ V, g : V ⟶ W, it states c_{f≫g} = c_g ≫ Rg_*(c_f), under etaleComparisonDirectImageCompIso and proEtaleComparisonDirectImageCompIso (R(g∘f)_* ≅ Rg_*Rf_… |
| `lemma-extremally-disconnected-covers--2` | Mathlib | `Profinite.presentation`<br>`Profinite.presentation.π`<br>`Profinite.presentation.epi_π` | Mathlib/Topology/Category/Stonean/Basic.lean. Line 257: `Profinite.presentation (X : Profinite) : Stonean`, a compact Hausdorff extremally disconnected space. Line 263: `presentation.π : Stonean.toProfinite.obj X.presentation ⟶ X`, so the source is profinite.… |
| `lemma-extremally-disconnected-covers--3` | the declaration's own name | `Stonean.toProfinite` | Mathlib/Topology/Category/Stonean/Basic.lean:104 `abbrev Stonean.toProfinite : Stonean ⥤ Profinite` is the parent name. It states the 'in particular' sentence: every extremally disconnected compact Hausdorff space is profinite. The main sentence (extremally d… |
| `lemma-inverse-image-coefficient-sheaves--2` | project lemma | `AlgebraicGeometry.ProEtale.spRoots_cartesian`<br>`AlgebraicGeometry.ProEtale.spFiniteTwists_cartesian`<br>`AlgebraicGeometry.ProEtale.spTwists_cartesian` | All in WeilConjectures/AlgebraicGeometry/Cartesian/CartesianCoefficientTwistsSupplement.lean. :544 spRoots_cartesian: the map f^{-1}μ_{ℓ^n,Y} → μ_{ℓ^n,X} is an isomorphism. :1958 spFiniteTwists_cartesian: the finite twists have signed comparison isomorphisms,… |
| `lemma-inverse-image-coefficient-sheaves--3` | project lemma | `AlgebraicGeometry.ProEtale.cartesianCoefficients_finiteFree` | WeilConjectures/AlgebraicGeometry/Cartesian/CartesianCoefficientsFiniteFree.lean:539. For E ≤ F, an integral basis exists. For every X it gives e₀ X : Mod.finiteFree (O_{E,X}) d ≅ O_{F,X} as an O_{E,X}-module, so O_{F,X} is finite free with rank independent o… |
| `lemma-local-cohomology-right-adjoint--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.closedSupportDerivedAdjunction` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/Condensed/CondensedClosedSupportAdjunction.lean:376 (namespace AlgebraicGeometry.ProEtale.CondensedRing): (lowerStar Λ i).mapDerivedCategory ⊣ (closedSupport Λ i j).rightDerivedFunctor, for i a closed … |
| `lemma-local-cohomology-right-adjoint--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.closedSupport_fiber` | CondensedClosedSupportAdjunction.lean:784. For K ≅ Q(I) with I K-injective, RΓ_Z K ≅ i^*(Q(mappingCone(I → j_*j^*I)[-1])). Since j_*j^*I computes Rj_*j^*K, this is the fibre formula, stated on a K-injective representative. Same coefficient caveat as --1. |
| `lemma-reduction-derived-nakayama--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.isZero_of_derivedCompleteIntegers_of_isZero_derivedReduction`<br>`AlgebraicGeometry.ProEtale.derived_nakayama_first_reduction` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/DerivedComplete/Basic.lean:64: derivedCompleteIntegers K ∧ IsZero (derivedReduction K) → IsZero K. Caveat: derivedCompleteIntegers (:53) is defined as right-orthogonality to complexes with vanishing first redu… |
| `lemma-reduction-derived-nakayama--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.isIso_of_derivedCompleteIntegers_of_isIso_derivedReduction_map`<br>`AlgebraicGeometry.ProEtale.derived_nakayama_first_reduction` | DerivedComplete/Basic.lean:113: for φ : K ⟶ L with K and L derivedCompleteIntegers and IsIso (derivedReduction.map φ), IsIso φ. The caveat about the orthogonality definition from --2 applies. The fourth conjunct of derived_nakayama_first_reduction (DerivedNak… |
| `lemma-stability--1` | the declaration's own name |  | Mathlib/AlgebraicGeometry/Morphisms/WeaklyEtale.lean:75 `instance : MorphismProperty.IsStableUnderBaseChange @WeaklyEtale`. It is anonymous; the parent already carries its auto-generated name AlgebraicGeometry.WeaklyEtale.instIsStableUnderBaseChangeScheme. It… |
| `lemma-stability--3` | the declaration's own name |  | Mathlib/AlgebraicGeometry/Morphisms/WeaklyEtale.lean:80 `instance : IsZariskiLocalAtSource @WeaklyEtale`. Its auto-generated name AlgebraicGeometry.WeaklyEtale.instIsZariskiLocalAtSource is already on the parent. IsZariskiLocalAtSource is exactly the clause's… |
| `lemma-stability--8` | project lemma | `AlgebraicGeometry.WeaklyEtale.Spec_iff`<br>`Algebra.weaklyEtale_iff` | WeilConjectures/AlgebraicGeometry/Morphisms/WeaklyEtale.lean:54 `Spec_iff : WeaklyEtale (Spec.map f) ↔ f.hom.WeaklyEtale`. RingHom.WeaklyEtale unfolds to Algebra.WeaklyEtale. Mathlib/RingTheory/Etale/Weakly.lean:36 `@[mk_iff] class Algebra.WeaklyEtale` (field… |
| `lemma-uniform-bounds-pro-etale-affines--1` | partial |  | WeilConjectures/AlgebraicGeometry/ProEtale/Classical/ProEtaleClassicalBounds.lean:322 (a parent name). The first conjunct of HasClassicalUniformBounds gives vanishing of H^q(U, ν^*G) for pro-affine-étale U and q > 2·dim X + 1, for torsion étale G. Missing: th… |
| `lemma-uniform-bounds-pro-etale-affines--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.hasClassicalUniformBounds` | ProEtaleClassicalBounds.lean:322, second conjunct of HasClassicalUniformBounds. It gives vanishing of H^q(X ×_Y V, ν^*G) for pro-affine-étale V over Y and q > c, where c = 2·dim X + 1 depends only on X. Caveats: k is finite or algebraically closed, and F is ν… |
| `lemma-uniform-bounds-pro-etale-affines--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.relativeCohomologicalDimension_lt_top_of_finiteType` | WeilConjectures/AlgebraicGeometry/Cohomological/CohomologicalDimension.lean:848. For any field K with cd_ℓ(Spec K) < ⊤ and g : X ⟶ Y of finite type between finite-type K-schemes, cd_ℓ(g) < ⊤. This is more general than the clause. |
| `lemma-w-contractible-affines-projective--2` | the declaration's own name | `AlgebraicGeometry.Scheme.proetale_weakContractible_equivalences` | WeilConjectures/AlgebraicGeometry/ProEtaleCoefficients/WeakContractibleEquivalences.lean:73. For any W : X.ProEt, its first two conjuncts are: every epi F ⟶ uliftYoneda W splits ↔ Projective (uliftYoneda W) ↔ every epi F ⟶ G of sheaves of sets is surjective o… |
| `proposition-comparison-immersions--2` | project lemma |  | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/OpenCover.lean:141 `mapDerivedCategoryOpenImmersionLowerShriekComparisonUpperStarIso j : D(j^ét_!) ⋙ D(ν_X^*) ≅ D(ν_U^*) ⋙ D(j^proét_!)`. It lives on unbounded derived categories, works for any Gr… |
| `proposition-comparison-immersions--3` | partial |  | Lean states the two isomorphisms for general (qcqs) morphisms, and closed immersions are a special case. ν^*Ri_* ≅ Ri_*ν^*: rightDerivedLowerStarComparisonPlusIso (FiniteCoefficient/Derived/ComparisonLowerStarCanonical.lean:92) is already on theorem-compariso… |
| `proposition-comparison-immersions--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.rightDerivedLowerShriekOfCompactificationComparisonIso` | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/LowerShriekComparison.lean:133. For a Compactification c of f (Compactification/Defs.lean:69: open immersion c.i, proper c.g, f = c.i ≫ c.g), it gives an isomorphism Rḡ_*^{proét} j_! ν_X^* ≅ ν_Y^*… |
| `proposition-comparison-morphism-inverse-image--1` | the declaration's own name | `AlgebraicGeometry.Scheme.toProEt`<br>`AlgebraicGeometry.ProEtale.comparisonLowerStar` | WeilConjectures/Mathlib/AlgebraicGeometry/Sites/Proetale.lean:420 `def toProEt : X.Etale ⥤ X.ProEt` (namespace AlgebraicGeometry.Scheme, section ToProEt) is the inclusion of étale objects. The instances that make it a morphism of topoi have explicit names, Al… |
| `proposition-comparison-morphism-inverse-image--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.isColimit_comparisonUpperStar_mapCocone` | WeilConjectures/SixFunctors/ProEtale/Comparison/Continuity.lean:488. Take a cofiltered diagram K of qcqs étale S-schemes with affine transition maps, and a cone c that is a limit of schemes. Then ((comparisonUpperStar A S).obj F).obj.mapCocone c.op is a colim… |
| `proposition-continuous-cohomology-pro-etale-cohomology--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.continuousCohomology` | The clause equals the parent. WeilConjectures/AlgebraicGeometry/ProEtaleContinuousCohomology.lean:89, first conjunct: RΓ(X, lim F_n) is the derived limit of the RΓ(X, F_n), for epimorphic towers. Its proof is SORRY (line 153). The lemma continuousCohomology_l… |
| `proposition-etale-implications--2` | the declaration's own name | `AlgebraicGeometry.WeaklyEtale.etale` | WeilConjectures/AlgebraicGeometry/Morphisms/WeaklyEtale.lean:46 `instance etale [WeaklyEtale f] [LocallyOfFinitePresentation f] : Etale f` (parent name). This is the scheme version; the ring clause follows with f = Spec.map, via Spec_iff. The ring version is … |
| `proposition-extension-zero-restriction-closed-subscheme--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.RingSheaf.preservesLimitsOfSize_upperStar_of_isCompl`<br>`AlgebraicGeometry.ProEtale.RingSheaf.preservesColimitsOfSize_upperStar` | WeilConjectures/SixFunctors/ProEtale/RingSheaf/Limits.lean:48: i^* on B-module sheaves preserves all small limits, hence is left exact. Limits.lean:59: it preserves all small colimits, hence is right exact. No single declaration states that i^* is exact; exac… |
| `proposition-extension-zero-restriction-closed-subscheme--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.RingSheaf.preservesLimitsOfSize_upperStar_of_isCompl` | RingSheaf/Limits.lean:48: PreservesLimitsOfSize.{u+1,u+1} (upperStar B i), for X qcqs and i a closed immersion with quasi-compact open complement j. This is exactly the clause. |
| `proposition-extension-zero-restriction-closed-subscheme--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.RingSheaf.preservesColimitsOfSize_upperStar` | RingSheaf/Limits.lean:59: PreservesColimitsOfSize.{u+1,u+1} (upperStar B i), derived from upperStarLowerStarAdjunction. This is exactly the clause. |
| `proposition-extension-zero-restriction-closed-subscheme--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.RingSheaf.preservesFiniteColimits_lowerStar_of_isCompl`<br>`AlgebraicGeometry.ProEtale.RingSheaf.preservesFiniteLimits_lowerStar` | RingSheaf/OpenClosed.lean:92: preservesFiniteColimits_lowerStar_of_isCompl, a parent name, states that i_* is right exact, the nontrivial half. RingSheaf/OpenClosed.lean:66: the named instance preservesFiniteLimits_lowerStar (g : Y ⟶ X) gives left exactness, … |
| `proposition-extension-zero-restriction-closed-subscheme--5` | the declaration's own name | `AlgebraicGeometry.ProEtale.RingSheaf.fullyFaithfulLowerStar` | RingSheaf/OpenClosed.lean:116: def fullyFaithfulLowerStar : (lowerStar B i).FullyFaithful. It is built from the counit isomorphism, the named instance isIso_upperStarLowerStarAdjunction_counit (OpenClosed.lean:103), which is on no node. |
| `proposition-extension-zero-restriction-closed-subscheme--6` | partial |  | RingSheaf/OpenClosed.lean:61: the instance preservesFiniteColimits_upperStar (g : Y ⟶ X) says g^*, hence j^*, is right exact. Missing: no declaration states left exactness of j^* on B-module sheaves. It follows only implicitly, by instance inference, from j^*… |
| `proposition-extension-zero-restriction-closed-subscheme--7` | the declaration's own name | `AlgebraicGeometry.ProEtale.RingSheaf.preservesFiniteLimits_openImmersionLowerShriek`<br>`AlgebraicGeometry.ProEtale.RingSheaf.preservesFiniteColimits_openImmersionLowerShriek` | RingSheaf/OpenClosed.lean:82: j_! preserves finite limits. OpenClosed.lean:74: j_! preserves finite colimits, as a left adjoint. Together they state exactness. Both are named instances on the parent. |
| `proposition-extension-zero-restriction-closed-subscheme--8` | the declaration's own name | `AlgebraicGeometry.ProEtale.RingSheaf.shortExact_openClosedShortComplex` | RingSheaf/OpenClosed.lean:189: (openClosedShortComplex B i j hij M).ShortExact for every B-module sheaf M. The complex itself is the def AlgebraicGeometry.ProEtale.RingSheaf.openClosedShortComplex (OpenClosed.lean:156). It is on no node and could be added as … |
| `proposition-extension-zero-restriction-closed-subscheme--9` | project lemma | `AlgebraicGeometry.ProEtale.RingSheaf.preservesLimitsOfShape_mapDerivedCategory_openImmersionLowerShriek` | RingSheaf/DerivedLimits.lean:83: PreservesLimitsOfShape (Discrete β) (openImmersionLowerShriek B i j hij).mapDerivedCategory, i.e. j_! from D(U_proét, j^*B) to D(X_proét, B) preserves products of complexes. Its docstring cites the product assertion of sk-prop… |
| `proposition-extension-zero-restriction-closed-subscheme--10` | the declaration's own name | `AlgebraicGeometry.ProEtale.RingSheaf.isHomotopyLimit_mapCone_openImmersionLowerShriek` | RingSheaf/DerivedLimits.lean:102: for a tower K : ℕᵒᵖ ⥤ D(U_proét, j^*B) and a homotopy-limit cone c (Milnor triangle), j_! of c is again a homotopy-limit cone, i.e. j_! preserves R lim of towers. |
| `proposition-extension-zero-restriction-closed-subscheme--11` | the declaration's own name | `AlgebraicGeometry.ProEtale.RingSheaf.isIso_openImmersionLowerShriekBaseChangeHom` | RingSheaf/BaseChangeIso.lean:106: IsIso (openImmersionLowerShriekBaseChangeHom ...), where the canonical map j'_! g_U^* ⟶ g^* j_! on module sheaves is the def at :92. The def AlgebraicGeometry.ProEtale.RingSheaf.openImmersionLowerShriekBaseChangeHom and the i… |
| `proposition-gleason-s-theorem--1` | the declaration's own name | `CompactT2.projective_iff_extremallyDisconnected` | The single clause is identical to the parent. Mathlib/Topology/ExtremallyDisconnected.lean:285 `CompactT2.projective_iff_extremallyDisconnected`; CompactT2.Projective is the lifting property along continuous surjections of compact T2 spaces. The categorical f… |
| `proposition-left-completeness--1` | the declaration's own name | `AlgebraicGeometry.Scheme.ProEt.left_complete_quasiIso`<br>`DerivedCategory.isHomotopyLimit_truncGECone` | The clause equals the whole parent. WeilConjectures/AlgebraicGeometry/ProEtale/ProEtaleLeftComplete.lean:324: K → Rlim τ≥−n K is a quasi-isomorphism. WeilConjectures/CategoryTheory/DerivedCategory/LeftComplete.lean:151: in D(C) with exact countable products, … |
| `proposition-pro-etale-affines-form-basis--1` | the declaration's own name | `AlgebraicGeometry.Scheme.AffineProEt.isCoverDense_toProEt` | .lake/packages/proetale/Proetale/Topology/Comparison/Affine.lean:155 `instance isCoverDense_toProEt : (toProEt S).IsCoverDense (ProEt.topology S)` (namespace AlgebraicGeometry.Scheme.AffineProEt), an explicitly named instance. IsCoverDense says every object o… |
| `proposition-pro-etale-coverings--1` | the declaration's own name | `AlgebraicGeometry.Scheme.ProEt.exists_finite_affine_of_mem_topology` | WeilConjectures/AlgebraicGeometry/ProEtale/CohomologyFilteredColimit.lean:53 (parent name). For W with quasi-compact quasi-separated underlying scheme (affine is a special case), every covering sieve contains a finite covering family of affine objects. Caveat… |
| `proposition-pro-etale-site-separably-closed--2` | partial |  | isEquivalence_upperStarFromPoint (WeilConjectures/SixFunctors/ProEtale/ModuleObject/SepClosedPoint.lean:59, a named instance) shows that for Ω separably closed, p^* from condensed abelian groups is an equivalence; this covers abelian sheaves only, not sets. g… |
| `proposition-repleteness-pro-etale-topos--1` | the declaration's own name | `AlgebraicGeometry.Scheme.isReplete_proEtale` | WeilConjectures/AlgebraicGeometry/ProEtaleReplete.lean:47 `isReplete_proEtale X : IsReplete (ProEt.topology X)`, the parent name and exactly the clause. |
| `proposition-unbounded-comparison-finite-coefficients--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.finiteCoefficientDerivedComparison_fullyFaithful` | WeilConjectures/AlgebraicGeometry/Unbounded/UnboundedSiteComparison.lean:61 (parent name): the comparison D(X_ét, A) → D(X_proét, A) is triangulated, fully faithful and preserves arbitrary direct sums. Hypotheses: k finite or algebraically closed (also noted … |
| `proposition-unbounded-comparison-finite-coefficients--2` | partial |  | WeilConjectures/AlgebraicGeometry/UnboundedDirectImageComparisonMap.lean:83 defines the map (2.9) on the unbounded derived category. WeilConjectures/AlgebraicGeometry/UnboundedDirectImageBoundedBelow.lean:131 proves it is an isomorphism for A finite and g qcq… |
| `proposition-unbounded-functors-products--1` | partial |  | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/LowerShriek.lean:219: rightDerivedGlobalSections X : D(X_proét, A) ⥤ D(A), the unbounded RΓ(X,−). WeilConjectures/CategoryTheory/GrothendieckAbelian/KInjectiveResolution.lean:173: a named instance… |
| `proposition-unbounded-functors-products--2` | partial |  | WeilConjectures/SixFunctors/ProEtale/Adic/DerivedLowerStarDerivedLimit.lean:93 (a parent name): Rg_* sends a derived-limit triangle of an ℕ-tower to one for the image tower, together with a product comparison isomorphism. :109 gives the same in homotopy-limit… |
| `proposition-weakly-contractible-hypercovers--1` | the declaration's own name | `AlgebraicGeometry.exists_proetale_hypercover_single_affine` | WeilConjectures/AlgebraicGeometry/ProEtaleCoefficients/HypercoverExistence.lean:62, third conjunct. For U with qcqs U.left there is a simplicial hypercover W of U in which every term is Spec D, with D w-contractible, weakly étale over X and weakly contractibl… |
| `proposition-weakly-contractible-hypercovers--2` | the declaration's own name | `AlgebraicGeometry.Scheme.ProEt.hypercover_computes_boundedBelow_complex` | WeilConjectures/AlgebraicGeometry/ProEtale/Hypercover/ProEtaleHypercoverComputesBoundedComplexSupplement.lean:121. For a hypercover with weakly contractible terms, there is a natural isomorphism between derived evaluation and the total complex of K^b(U_r) (fo… |
| `theorem-pro-etale-refinements-weakly-etale--1` | the declaration's own name | `Algebra.WeaklyEtale.exists_indEtale`<br>`RingHom.WeaklyEtale.exists_indEtale_comp` | The single clause is identical to the parent. WeilConjectures/RingTheory/ProEtale/WeaklyEtaleIndEtale.lean:409 states ∃ T, IndEtale S T ∧ FaithfullyFlat S T ∧ IndEtale R T, and :419 gives the ring-hom form. The same names also exist in proetale (.lake/package… |

### chap-The-six-operations-on-Dbctf

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `definition-change-of-coefficients-maps--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.derivedPullIso` | The parent's AlgebraicGeometry.ProEtale.CondensedRing.derivedPullIso (WeilConjectures/SixFunctors/ProEtale/ModuleObject/ChangeOfCoefficients.lean:236) is the (Pull) iso Lf^* then T ~ T then Lf^*. It is built as the conjugate of derivedComapLowerStarIso along … |
| `definition-change-of-coefficients-maps--3` | project lemma |  | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/ProjectionMapExtendScalars.lean:57: the tensor comparison T(K tensor L) ~ TK tensor TL of the derived extension of scalars (leftDerivedTensorComparison of the strong monoidal Ext). This is the clause's… |
| `lemma-change-coefficients-compact-support--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.isIso_rightDerivedLowerShriekOfCompactificationExtendScalarsMap_app` | Parent's AlgebraicGeometry.ProEtale.isIso_rightDerivedLowerShriekOfCompactificationExtendScalarsMap_app (WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/ExtendScalars/LowerShriek.lean:93): for finite R -> S and any compactification, the (Shriek… |
| `lemma-change-coefficients-compact-support--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.BoundedConstructibleCoefficientChange.squareCompatible_lowerShriekOfCompactificationIso` | Parent's AlgebraicGeometry.ProEtale.CondensedRing.BoundedConstructibleCoefficientChange.squareCompatible_lowerShriekOfCompactificationIso (WeilConjectures/SixFunctors/ProEtale/ModuleObject/BaseChangeTheorems/LowerShriek/CoefficientChangeRefinement.lean:181): … |
| `lemma-change-coefficients-direct-image--1` | partial |  | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/ExtendScalars/LowerStar.lean:114 (finite R -> S, proper g, objects j_!K with K in Dctf); WeilConjectures/SixFunctors/Etale/Derived/CoefficientChangeLowerStar.lean:61 (etale site, finite Lambda, pr… |
| `lemma-change-coefficients-direct-image--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedUpperStarExtendScalarsPushHom_integersModPow_app` | Parent's AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedUpperStarExtendScalarsPushHom_integersModPow_app (WeilConjectures/SixFunctors/ProEtale/ModuleObject/PushIntegersModPowFinal.lean:97): (Push) iso for O_E -> O_E/l^n, any f, K bounded below. Covers … |
| `lemma-change-coefficients-direct-image--3` | partial |  | E -> F: WeilConjectures/SixFunctors/ProEtale/ModuleObject/Colimit/Compatibility.lean:816 (named instance, (Push) iso on all objects) - on proposition-six-operations-change-coefficients--3. General finite-free coefficient change: WeilConjectures/SixFunctors/Pr… |
| `lemma-change-coefficients-direct-image--4` | project lemma |  | WeilConjectures/SixFunctors/ProEtale/ModuleObject/PushIntegralDerivedIso.lean:199: qcqs f, bounded below K in D(O_E,X), (Push) for O_E -> E is an iso - exactly the clause; already on proposition-six-operations-change-coefficients--3. Conflicts: AlgebraicGeome… |
| `lemma-change-coefficients-direct-image--5` | project lemma |  | WeilConjectures/SixFunctors/ProEtale/ModuleObject/PushPadicSubfieldFinite.lean:148: qcqs f, bounded below K in D(E_X), (Push) for E -> Qbar_l is an iso - exactly the clause; already on proposition-six-operations-change-coefficients--3. (The conditional helper… |
| `lemma-change-coefficients-direct-image--6` | partial |  | WeilConjectures/SixFunctors/ProEtale/ModuleObject/ChangeOfCoefficientsComp.lean:120 states the decomposition of the (Push) comparison for c = a then b into those for a and b (on proposition-six-operations-change-coefficients--9). The iso conclusion for compos… |
| `lemma-extension-scalars-preserves-dctf--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.constructibleFiniteTor_leftDerivedSheafExtendScalars` | Clause = whole lemma. Parent's AlgebraicGeometry.ProEtale.constructibleFiniteTor_leftDerivedSheafExtendScalars (WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/ExtendScalars/Constructible.lean:58) covers finite A -> B. The l-adic maps (flat ext… |
| `proposition-dctf-x-qbar-2-colimit--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.constructibleCocone`<br>`AlgebraicGeometry.ProEtale.constructibleCocone_isFilteredTwoColimit` | The parent's AlgebraicGeometry.ProEtale.constructibleCocone_isFilteredTwoColimit (WeilConjectures/SixFunctors/ProEtale/ModuleObject/Colimit/TwoColimit.lean:574) states that the cocone constructibleCocone of the Dbc(X,E) under scalar extension is a filtered 2-… |
| `proposition-isomorphisms-reduce-finite-coefficients--1` | not formalized |  | Lean only formalizes the integral conservativity step of the parent. |
| `proposition-isomorphisms-reduce-finite-coefficients--2` | partial |  | WeilConjectures/SixFunctors/ProEtale/ModuleObject/ReductionNakayama.lean:89: a morphism of Dbc(X,O_E) complexes (X noetherian) is an isomorphism if its derived reduction mod pi_E is - exactly the derived-Nakayama step of this clause. WeilConjectures/SixFuncto… |
| `proposition-isomorphisms-reduce-finite-coefficients--3` | not formalized |  | Not formalized. |
| `proposition-isomorphisms-reduce-finite-coefficients--4` | not formalized |  | Not formalized. |
| `proposition-six-operations-change-coefficients--8` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.derivedUpperStarExtendScalarsIso_hom_app_of_coefficient_comp` | WeilConjectures/WeilSheaf/SmoothPurityCoefficientPullComp.lean:87: for c = a then b, the pullback comparison derivedUpperStarExtendScalarsIso c f equals the composite of those for a and b up to the transitivity isos derivedExtendScalarsCompIso. derivedUpperSt… |
| `proposition-six-operations-change-coefficients--10` | not formalized |  | Not formalized (would follow from --9 derivedPushHom_comp_app and the open (Shriek) iso). |
| `proposition-six-operations-change-coefficients--11` | not formalized |  | Not formalized. |
| `proposition-six-operations-change-coefficients--13` | the declaration's own name | `CategoryTheory.Functor.LaxMonoidal.ihomComparison_comp_app` | Parent's only name CategoryTheory.Functor.LaxMonoidal.ihomComparison_comp_app (WeilConjectures/Mathlib/CategoryTheory/Monoidal/Closed/Basic.lean:280): the ihom comparison of a composite of lax monoidal functors is the composite of the comparisons - exactly th… |
| `proposition-six-operations-change-coefficients--16` | not formalized |  | Not formalized. |
| `proposition-six-operations-change-coefficients--17` | not formalized |  | Not formalized. |
| `proposition-six-operations-change-coefficients--18` | Mathlib | `CategoryTheory.unit_mateEquiv` | Mathlib/CategoryTheory/Adjunction/Mates.lean:136: G(eta_c) then mateEquiv(alpha) = eta'_{Gc} then R'(alpha); with alpha = c_F^{-1} and mate = c_G this is G'(c_F) o c_G o T1(eta) = eta' (the clause's identity). Project version WeilConjectures/CategoryTheory/Ad… |
| `proposition-six-operations-change-coefficients--19` | Mathlib | `CategoryTheory.mateEquiv_counit` | Mathlib/CategoryTheory/Adjunction/Mates.lean:123: L'(mateEquiv(alpha)_d) then eps' = alpha then H(eps_d); with alpha = c_F^{-1}, composing with c_F gives eps' o F'(c_G) o c_F = T2(eps), the clause. Project version NatTrans.SquareCompatible.counit (SquareCompa… |
| `proposition-six-operations-change-coefficients--22` | project lemma | `CategoryTheory.Functor.LaxMonoidal.coev_ihomComparison` | WeilConjectures/Mathlib/CategoryTheory/Monoidal/Closed/Basic.lean:136: G(coev_A B) then ihomComparison = coev_{GA}(GB) then [GA,-](mu_{A,B}), i.e. the lax monoidal functor carries the unit (coevaluation) of tensorLeft A -\| ihom A to the unit over the target,… |
| `proposition-six-operations-dctf--1` | project lemma | `AlgebraicGeometry.ProEtale.constructibleFiniteTor_leftDerivedFunctor_upperStar_obj`<br>`AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_leftDerivedUpperStar_obj` | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/LocalizationFiniteTor.lean:313 (finite Lambda, pro-etale: Lg^* maps Dctf(X) into Dctf(Y) for any g); WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructible.lean:179 (any co… |
| `proposition-six-operations-dctf--2` | project lemma |  | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/Stability.lean:131 and :224 state, for any separated finite-type f and finite Lambda, that pro-etale Rf_* preserves Dbc and Tor amplitude [a,b] -> [a,b+2d]; together exactly this clause, but both … |
| `proposition-six-operations-dctf--3` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructibleLowerStar` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleLowerStar.lean:330: for any morphism f of separated finite-type k-schemes (char k = p != l), R f_* with coefficients O_E maps Dbc to Dbc (Deligne finiteness). It is exactly the clau… |
| `proposition-six-operations-dctf--4` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructibleLowerStar` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleLowerStar.lean:233 (E-coefficients, any f between separated finite-type k-schemes: Rf_* preserves Dbc) is exactly the clause but already on proposition-proper-direct-image-construct… |
| `proposition-six-operations-dctf--5` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightDerivedLowerStar_obj` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleLowerStar.lean:151: Qbar_l coefficients, any morphism f of separated finite-type k-schemes, R f_* K is bounded constructible for K in Dbc(X, Qbar_l). Dbc = Dctf for Qbar_l. Not yet … |
| `proposition-six-operations-dctf--6` | project lemma | `AlgebraicGeometry.ProEtale.constructibleFiniteTor_rightDerivedLowerShriek`<br>`AlgebraicGeometry.ProEtale.constructibleFiniteTor_rightDerivedLowerShriekOfCompactification` | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/UpperShriekFiniteness.lean:227 (pro-etale Rf_! maps Dctf(X,A) into Dctf(Y,A)); WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/CompactifFiniteTor.lean:68 (same for Rf_!(c) = Rp_* j_… |
| `proposition-six-operations-dctf--7` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructibleLowerShriek`<br>`AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.boundedConstructibleLowerShriekCompatibility` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleLowerStar.lean:586 (def: Rf_! = i_! then Rp_* as a functor Dbc(X,O_E) -> Dbc(Y,O_E)) and :599 (iso: this functor followed by the inclusion is the ambient R(f)_! restricted to Dbc). … |
| `proposition-six-operations-dctf--8` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructibleLowerShriek`<br>`AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.boundedConstructibleLowerShriekCompatibility` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleLowerStar.lean:511 and :523 (E-coefficient analogue of --7). Same caveat (def + compatibility iso). |
| `proposition-six-operations-dctf--9` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriek`<br>`AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekCompatibility` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleLowerStar.lean:440 and :452 (Qbar_l analogue of --7). Same caveat (def + compatibility iso). |
| `proposition-six-operations-dctf--10` | project lemma |  | WeilConjectures/SixFunctors/ProEtale/FiniteCoefficient/Derived/UpperShriekFiniteness.lean:211 states exactly this (pro-etale f^! maps Dctf(Y,A) into Dctf(X,A)) but is on theorem-f-shriek-finite-coefficients (whose clause --1 is the same statement). Etale-site… |
| `proposition-six-operations-dctf--11` | project lemma |  | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/ProperUpperShriekExistence.lean:183: every right adjoint f^! of Rf_! on Loc(Dbc(-,O_E)) maps Dbc(Y,O_E) into Dbc(X,O_E). Exactly the clause; already on theorem-f-shriek-ell-adic-coefficients (parent of… |
| `proposition-six-operations-dctf--12` | project lemma |  | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/ProperUpperShriekExistence.lean:145 (E-coefficients); exactly the clause, already on theorem-f-shriek-ell-adic-coefficients. Conflicts: AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rig… |
| `proposition-six-operations-dctf--13` | project lemma |  | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/ProperUpperShriekExistence.lean:222 (Qbar_l); exactly the clause, already on theorem-f-shriek-ell-adic-coefficients. Conflicts: AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightAdjoin… |
| `proposition-six-operations-dctf--14` | partial |  | Qbar: WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructible.lean:338 (Dbc(X,Qbar) contains the unit and is closed under derived tensor); E: same file :397; O_E: :460 (already on lemma-inverse-image-tensor-product--2). Finite A: only o… |
| `proposition-six-operations-dctf--15` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.isMonoidalClosed_boundedConstructible`<br>`AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.isMonoidalClosed_boundedConstructible`<br>`AlgebraicGeometry.ProEtale.CondensedRing.PadicIntegersRingObj.isMonoidalClosed_boundedConstructible` | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleLowerStar.lean:628 (Qbar), :695 (E), :766 (O_E): Dbc(X,Lambda) is stable under the derived internal hom RHom(-,-). The finite-A case is the parent's own name ProEtale.DerivedCategor… |
| `proposition-six-operations-dctf--16` | partial |  | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleLowerStar.lean:174 (Qbar), :268 (E), :359 (O_E): Lf^* -\| Rf_* on Dbc defined as Adjunction.restrictFullyFaithful of the ambient derived adjunction, i.e. literally the restriction. … |
| `proposition-six-operations-dctf--17` | partial |  | Finite A, pro-etale: UpperShriekFiniteness.lean:247 (restricted Rf_! -\| f^! on Dctf, units/counits of the ambient adjunction) - on theorem-f-shriek-finite-coefficients. Finite A, etale: WeilConjectures/SixFunctors/Etale/Derived/Adjunctions.lean:234 (restrict… |
| `proposition-six-operations-dctf--18` | partial |  | WeilConjectures/SixFunctors/ProEtale/ModuleObject/Derived/BoundedConstructibleLowerStar.lean:669 (Qbar), :737 (E), :808 (O_E): K tensor - -\| RHom(K,-) on Dbc, the ihom adjunction of the full monoidal closed subcategory (identified with the ambient functors b… |

### chap-The-trace-formula

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `corollary-functional-equation--1` | project lemma | `AlgebraicGeometry.weilBettiNumber`<br>`AlgebraicGeometry.Scheme.weilBettiNumber_eq_finrank` | WeilConjectures/ZetaFunction/BettiNumbers.lean:50 (namespace AlgebraicGeometry): weilBettiNumber P i = deg P_i, for a family of integral Frobenius factors. BettiSymmetry.lean:158 (namespace AlgebraicGeometry.Scheme): weilBettiNumber P i = finrank_{ℚ̄_ℓ} H^i(X… |
| `corollary-functional-equation--2` | project lemma | `Polynomial.alternatingNatDegreeSum` | WeilConjectures/Mathlib/Algebra/Polynomial/BigOperators.lean:38 (namespace Polynomial): alternatingNatDegreeSum P := ∑_i (-1)^i deg P_i. With b_i = deg P_i (clause --1) this is χ. The docstring at BettiNumbers.lean:68-71 says so explicitly. It is the χ used i… |
| `corollary-functional-equation--3` | project lemma | `AlgebraicGeometry.weilDeterminantScalar`<br>`AlgebraicGeometry.Scheme.map_weilDeterminantConstant_eq_det` | BettiNumbers.lean:72: weilDeterminantScalar P := ∏_i D_i^{(-1)^i} ∈ ℚ, where D_i = weilDeterminantConstant P_i = (-1)^{b_i}·lc(P_i). BettiSymmetry.lean:132: the image of D_i in ℚ̄_ℓ is det(F \| H^i(X₀⊗k̄, ℚ̄_ℓ)). Together: D = ∏ det(F_i)^{(-1)^i}. Not on any … |
| `corollary-functional-equation--4` | the declaration's own name | `AlgebraicGeometry.Scheme.duality_reciprocity` | WeilConjectures/ZetaFunction/DualityReciprocity.lean:91, second conjunct: ∀ i, (P i.rev).natDegree = (P i).natDegree, i.e. b_{2d-i} = b_i given b_i = deg P_i (clause --1). Other options: AlgebraicGeometry.WeilFunctionalEquation.natDegree_rev (BettiNumbers.lea… |
| `corollary-functional-equation--5` | the declaration's own name | `AlgebraicGeometry.Scheme.reciprocity` | DualityReciprocity.lean:136, third conjunct: Even ((d:ℤ) * alternatingNatDegreeSum P), i.e. dχ is even. Its proof (l.148-164) follows the blueprint: the middle-degree term via even_finrank_cohomology_middle (l.57, alternating middle pairing for odd d). Abstra… |
| `corollary-functional-equation--6` | project lemma | `AlgebraicGeometry.WeilFunctionalEquation.prod_determinant_sq` | WeilConjectures/ZetaFunction/ClassicalFunctionalEquation.lean:125 (namespace AlgebraicGeometry). Statement: for normalized Weil factors satisfying WeilFunctionalEquation (reciprocal roots matched), (∏_i ((-1)^{b_i} lc P_i)^{(-1)^i})² = q^{dχ}, i.e. D² = q^{dχ… |
| `corollary-functional-equation--7` | project lemma | `AlgebraicGeometry.WeilFunctionalEquation.alternatingProdEval_eq_prod_determinant` | ClassicalFunctionalEquation.lean:181. Statement: for Weil factors satisfying WeilFunctionalEquation, ∏P_i(q^{-d}t^{-1})^{(-1)^{i+1}} = (-1)^χ t^χ D ∏P_i(t)^{(-1)^{i+1}} at every t ≠ 0 in ℂ. Since Z = ∏P_i^{(-1)^{i+1}} as rational functions, this is the identi… |
| `corollary-functional-equation--8` | project lemma | `AlgebraicGeometry.weilSign` | ClassicalFunctionalEquation.lean:79: weilSign q m P := (-1)^χ q^{-m} ∏_i ((-1)^{b_i} lc P_i)^{(-1)^i} = (-1)^χ D q^{-m}, with m = dχ/2 passed as an argument (to avoid truncating division). This is ε. Not on any node. |
| `corollary-functional-equation--9` | project lemma | `AlgebraicGeometry.weilSign_eq_one_or_eq_neg_one` | ClassicalFunctionalEquation.lean:160. Statement: for Weil factors satisfying WeilFunctionalEquation with dχ = 2m, weilSign q m P = 1 ∨ = -1. Proof: square it and use prod_determinant_sq, as in the blueprint. The ε = ±1 conjunct of weil_functional_equation (on… |
| `corollary-functional-equation--10` | project lemma | `AlgebraicGeometry.WeilFunctionalEquation.alternatingProdEval_eq` | ClassicalFunctionalEquation.lean:223. Statement: ∏P_i(q^{-d}t^{-1})^{(-1)^{i+1}} = weilSign·q^m·t^χ·∏P_i(t)^{(-1)^{i+1}} for t ≠ 0 with no factor vanishing, where dχ = 2m. This is Z(1/(q^dT)) = ε q^{dχ/2} T^χ Z(T), with the same rational-function caveat as --… |
| `corollary-point-counting-zeta-function--1` | partial |  | WeilConjectures/TraceFormula/Statement.lean:176. Statement: weilStalkTraceAlternatingSum of the canonical Weil unit on RΓ_c(X, ℚ̄_ℓ) = Nat.card(frobeniusFixedPoints e n), for an automorphism e of finite order (e = 𝟙 gives #X(F_{qⁿ})). This covers only Λ = ℚ̄_… |
| `definition-frobenius-correspondences-their-operators--3` | inside a proof |  | Used as hypothesis type everywhere; no definition needed. |
| `lemma-additivity-open-subscheme-complement--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.CoefficientMorphism.openPieceCoefficient`<br>`AlgebraicGeometry.ProEtale.CondensedRing.CoefficientMorphism.closedPieceCoefficient` | WeilConjectures/TraceFormula/CoefficientMorphismPieces.lean:216 openPieceCoefficient (ψ_U on Rj_!Lj^*K: compact-support base change then Rj_! of the restriction of ψ); :281 closedPieceCoefficient (ψ_Z on Ri_*Li^*K). The correspondences on j^*K and i^*K are no… |
| `lemma-additivity-open-subscheme-complement--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.trace_compactPullback_comp_eq_add` | WeilConjectures/TraceFormula/CoefficientMorphismAdditivity.lean:112: trace(RΓ_c(X,ψ)∘Φ^♯) = trace(RΓ_c(U,ψ\|_U)∘Φ_U^♯) + trace(RΓ_c(Z,ψ\|_Z)∘Φ_Z^♯) for an open j with closed complement i, both Φ-stable, any ψ. Stated for a single Φ; the m-th iterate is the ca… |
| `lemma-comparison-via-relative-frobenius--1` | the declaration's own name | `AlgebraicGeometry.isFinite_relativeFrobenius`<br>`AlgebraicGeometry.isUniversalHomeomorphism_relativeFrobenius`<br>`AlgebraicGeometry.isFinite_and_isUniversalHomeomorphism_relativeFrobenius`<br>`AlgebraicGeometry.ProEtale.CondensedRing.lowerShriekFrobeniusComparison`<br>`AlgebraicGeometry.ProEtale.CondensedRing.lowerShriekFrobeniusComparison_add`<br>`AlgebraicGeometry.relativeFrobenius_fst`<br>`AlgebraicGeometry.relativeFrobenius_snd` | WeilConjectures/AlgebraicGeometry/RelativeFrobenius.lean:218,229 (named instances: r_m finite, universal homeomorphism), :243 (model-Frobenius version for Φ^m); :80 relativeFrobenius_fst (f'∘r = f) and :86 relativeFrobenius_snd (p∘r = Φ_X), both NEW and on no… |
| `lemma-comparison-via-relative-frobenius--2` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.lowerShriekFrobeniusCoefficient`<br>`AlgebraicGeometry.ProEtale.CondensedRing.frobeniusCoefficientIterate_lowerShriekFrobeniusCoefficient` | TraceFormula/RelativeFrobeniusIterate.lean:161 lowerShriekFrobeniusCoefficient (ψ' = Rf_!ψ ∘ θ_{f,1}, 'sk-i-relative-frob (2)'); :200 frobeniusCoefficientIterate_lowerShriekFrobeniusCoefficient (ψ'_m = Rf_!ψ_m ∘ θ_{f,m}). |
| `lemma-comparison-via-relative-frobenius--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.frobeniusCompactOperator_lowerShriekFrobeniusCoefficient` | TraceFormula/RelativeFrobeniusIterate.lean:254: the composition isomorphism RΓ_c(Y,Rf_!K) ≅ RΓ_c(X,K) intertwines F_{c,m}(ψ') and F_{c,m}(ψ) for every m ('sk-i-relative-frob (3)'). |
| `lemma-comparison-via-relative-frobenius--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.stalk_lowerShriekFrobeniusCoefficient_iterate` | TraceFormula/RelativeFrobeniusIterate.lean:339: for y fixed by Φ_Y^m with fibre Z carrying Φ_Z = Φ_X^m\|_Z, proper base change (Rf_!K)_ȳ ≅ RΓ_c(Z,K\|_Z) identifies the stalk map of ψ'_m with F_{c,1}(ψ_m\|_Z) ('sk-i-relative-frob (4)'). Docstring points to IsM… |
| `lemma-covers-degree-prime-to-ell--1` | the declaration's own name | `AlgebraicGeometry.Etale.CurveLocalModel.nonempty_coverDatum`<br>`AlgebraicGeometry.Scheme.exists_sylow_galoisCover_trivializing`<br>`AlgebraicGeometry.exists_finite_smooth_cover_not_dvd_ramificationIdx` | Clause text identical to parent. nonempty_coverDatum: WeilConjectures/TraceFormula/CurveLocal/CoverDatumExistence.lean:179 (cover datum = smooth curve C finite over a neighbourhood U of y, k-point c over y, ramification index e prime to ℓ, étale over the punc… |
| `lemma-frobenius-fixed-scheme--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.isProper_hom` | WeilConjectures/TraceFormula/FixedPointComponent.lean:229 (namespace AlgebraicGeometry.ProEtale.CondensedRing, Correspondence): FixedLocus.isProper_hom [QuasiCompact f₀][LocallyOfFiniteType f₀] ... (hm : 1 ≤ m) : IsProper F.F.hom — exactly 'Fix(Φ_X^m) is prop… |
| `lemma-integral-models-rational-frobenius-correspondences--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.exists_integralModel_frobeniusCorrespondence` | WeilConjectures/TraceFormula/RationalModel.lean:314 (namespace AlgebraicGeometry.ProEtale.CondensedRing, l.67). Statement: for every K : Dᵇc(X)⟦E⟧ and every ψ : LΦ^*K ⟶ K there exist K₀ : Dᵇc(X)⟦𝒪_E⟧, e : (K₀)_E ≅ K, N : ℕ and θ : LΦ^*K₀ ⟶ K₀ with ℓ^N • ψ = θ… |
| `lemma-integral-models-rational-frobenius-correspondences--2` | not formalized |  | Lean stops at the iterate identity (pow_smul_frobeniusCoefficientIterate_eq, by induction on m using additivity of LΦ^*) and does not pass to T_{c_m}. |
| `lemma-integral-models-rational-frobenius-correspondences--3` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.pow_smul_upperStar_map_frobeniusCoefficientIterate_eq` | RationalModel.lean:270. Under the hypothesis ℓ^N ψ = θ ⊗ E, it states ℓ^{Nm} • Ly^*(ψ_m) = Ly^*(θ_m) ⊗ E for every y : T ⟶ X (more general than a geometric point), read through the comparisons. This is the stalk identity (ψ_E)_{m,ȳ} = π_E^{-Nm}(θ_{m,ȳ} ⊗ E), … |
| `lemma-local-term-restriction-map--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_point_traceClass_eq_supportedRestriction`<br>`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_frobeniusGraph_eq_supportedRestriction` | Clause text is identical to the parent. Parent name localTerm_point_traceClass_eq_supportedRestriction: WeilConjectures/TraceFormula/SupportedRestriction.lean:322 (general endocorrespondence, point y open and closed in Fix). NEW, more specific and on no node:… |
| `lemma-logarithm-determinant--1` | the declaration's own name | `LinearMap.inv_charpolyRev_eq_exp` | WeilConjectures/ZetaLinearAlgebra/DetTrace.lean:208 (namespace LinearMap). Statement: for F : Module.End K V, V finite-dimensional, K a field of characteristic zero, (F.charpolyRev : K⟦X⟧)⁻¹ = exp.subst(∑_{n≥1} tr(F^n) Tⁿ/n). This is exactly (12.5). The compa… |
| `lemma-logarithm-determinant--2` | project lemma | `LinearMap.alternatingCharpolyRevProd` | DetTrace.lean:360. alternatingCharpolyRevProd s F e := ∏_{i∈s} det(1 - T^e F_i \| W_i)^{(-1)^i} for a finite graded family (W_i, F_i). With e = 1 and W_i = H^i(P), v_i = H^i(v), this is the clause's det(1 - Tv \| P). Caveat: Lean takes the graded family as in… |
| `lemma-logarithm-determinant--3` | partial |  | WeilConjectures/ZetaFunction/CohomologicalFamily.lean:70. Statement: (alternatingCharpolyRevProd s u 1)⁻¹ = exp(alternatingTraceSeries s u), where the coefficients are (∑_i (-1)^i Tr(u_iⁿ))/n. This is (12.5) for the graded family, with the alternating sum of … |
| `lemma-restriction-punctured-curve--1` | the declaration's own name | `AlgebraicGeometry.Etale.puncturedRestriction_eq_zero` | Clause text identical to parent. WeilConjectures/TraceFormula/PuncturedRestriction.lean:357 (namespace AlgebraicGeometry.Etale): with Y connected, C ⟶ Z closed, C ∩ Y = {s}, s' a geometric point of the strict localization, globalSectionsRestriction (punctured… |
| `lemma-scheme-frobenius-geometric-frobenius--1` | project lemma | `AlgebraicGeometry.Etale.leftDerivedUpperStarGeometricFiberFrobeniusIterateIso`<br>`AlgebraicGeometry.Etale.leftDerivedUpperStarIterateHomIso_add_hom_app` | WeilConjectures/SixFunctors/Etale/Derived/SchemeGaloisIterate.lean:253 defines kappa_m : L(Phi_X^m)^* ≅ L(Fr_X^m)^* (docstring cites the lemma, 'the isomorphisms kappa_m'), iterating the parent's kappa_1 = leftDerivedUpperStarGeometricFiberFrobeniusIso; :171 … |
| `lemma-scheme-frobenius-geometric-frobenius--2` | project lemma | `AlgebraicGeometry.Etale.weilDatumIterate_schemeFrobeniusForm_hom` | WeilConjectures/SixFunctors/Etale/Derived/SchemeGaloisIterate.lean:272, docstring 'lemma-scheme-frobenius-geometric-frobenius (psi_m = phi_m kappa_m)': for a Weil structure phi : LFr_X^*K ≅ K, iterates of psi = phi∘kappa_1 are phi_m∘kappa_m. (General-morphism… |
| `lemma-scheme-frobenius-geometric-frobenius--3` | project lemma | `AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.globalOperator_graph_eq_pow` | WeilConjectures/TraceFormula/FrobeniusCorrespondence.lean:185, docstring cites the lemma: (K.graph m).globalOperator = (K.globalOperator 1)^m, i.e. T_{c_m}(phi_m) = Frob_{X,K}^m. Caveat: in Lean the Weil structure is for the scheme Frobenius Phi itself, so ka… |
| `lemma-scheme-frobenius-geometric-frobenius--4` | different route |  | Lean works throughout with arbitrary psi : LPhi^*K → K and frobeniusCompactOperator, so no transfer from Fr_X to Phi_X is needed. Conflicts: AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.globalOperator_ofGraph |
| `lemma-tangent-cones-on-cover--1` | project lemma | `AlgebraicGeometry.Etale.CurveLocalModel.CoverDatum.flat_π`<br>`AlgebraicGeometry.Etale.CurveLocalModel.CoverDatum.free_and_finrank_π`<br>`AlgebraicGeometry.Etale.CurveLocalModel.CoverDatum.etale_π_openComplement`<br>`AlgebraicGeometry.Etale.CurveLocalModel.CoverDatum.natCard_geometricFiber_π` | All in WeilConjectures/TraceFormula/CurveLocal/TangentConesOnCover.lean (namespace AlgebraicGeometry.Etale.CurveLocalModel, CoverDatum): flat_π:131 (π : T'⟶T flat); free_and_finrank_π:186 (strict local ring of T' is free of rank e² over that of T; e = local d… |
| `proposition-function-sheaf-dictionary--3` | project lemma | `AlgebraicGeometry.WeilComplex.traceFunction_derivedLowerShriek` | WeilConjectures/WeilSheaf/TraceFunctionLowerShriek.lean:198, docstring cites 'proposition-function-sheaf-dictionary, part (3); corollary-trace-functions-direct-image-compact': t_{Rf0!K,n}(y) = sum_{x in X(F_{q^n}), f(x)=y} t_{K,n}(x) for Weil complexes over Q… |
| `proposition-function-sheaf-dictionary--4` | project lemma | `AlgebraicGeometry.WeilComplex.traceFunction_eq_add_openClosed`<br>`AlgebraicGeometry.WeilComplex.traceFunction_derivedLowerShriek_upperStar_mapFieldPoints`<br>`AlgebraicGeometry.WeilComplex.traceFunction_derivedLowerShriek_upperStar_of_notMem_range` | WeilConjectures/WeilSheaf/TraceFunctionLowerShriek.lean:292 (t_{K,n} = t_{j!j*K,n} + t_{i*i*K,n}, docstring 'part (4)'), :304 (t_{j!j*K} = t_K on U), :314 (t_{j!j*K} = 0 off U). Symmetric i_* statements at :323 and :333 (traceFunction_derivedLowerStar_upperSt… |
| `proposition-function-sheaf-dictionary--5` | project lemma |  | Part (5) is the Grothendieck-Lefschetz formula. WeilComplex.sum_trace_compactlySupportedCohomology_eq_sum_traceFunction (WeilConjectures/ZetaFunction/WeilObjectComparison.lean:142): sum_i (-1)^i Tr(Frob^m \| H^i_c) = sum_{y in X(F_{q^m})} t_{K,m}(y); weilTrac… |
| `theorem-grothendieck-lefschetz-trace-formula--1` | not formalized |  | Lean proves the ℚ̄_ℓ formula directly by Noetherian induction from base cases (weilShriekTraceFunction_of_genericallyHolds, ShriekTraceFunctionBaseCases) and never passes through finite coefficients. |
| `theorem-grothendieck-lefschetz-trace-formula--2` | not formalized |  | Bypassed: the Lean proof works over ℚ̄_ℓ throughout. |
| `theorem-grothendieck-lefschetz-trace-formula--3` | not formalized |  | Bypassed: the Lean proof works over ℚ̄_ℓ throughout. |
| `theorem-grothendieck-lefschetz-trace-formula--4` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.weilTraceFormula`<br>`AlgebraicGeometry.WeilComplex.sum_trace_compactlySupportedCohomology_eq_sum_traceFunction` | TraceFormula/Statement.lean:160 weilTraceFormula: for X separated of finite type over 𝔽_q, e an automorphism of finite order, K a Weil object of Dᵇc(X)⟦ℚ̄_ℓ⟧ and n ≠ 0, the global trace of RΓ_c equals Σ over the frobeniusFixedPoints of the local traces (weilS… |
| `theorem-grothendieck-lefschetz-trace-formula--7` | not formalized |  | Not needed in the Lean route (single coefficient ring ℚ̄_ℓ). |
| `theorem-trace-formula-frobenius-correspondence--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.trace_frobeniusCompactOperator_eq_sum` | Clause text = full parent statement. Parent name AlgebraicGeometry.ProEtale.CondensedRing.trace_frobeniusCompactOperator_eq_sum (WeilConjectures/TraceFormula/CoefficientMorphism.lean:246): tr(F_{c,m}(psi)) = sum over FixedPoint Phi m of tr(graphStalkMap ... p… |

### chap-Verdier-and-Poincare-duality

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `corollary-cup-product-pairing--2` | the declaration's own name | `AlgebraicGeometry.WeilSheaf.exists_traceCup_poincarePairing`<br>`FrobeniusModule.TraceCup.pairing_comm_of_eq_two_mul` | WeilConjectures/ZetaLinearAlgebra/TraceCup.lean:118: for a trace–cup structure of even degree n = 2m, ⟨y,x⟩ = (-1)^i ⟨x,y⟩. It is applied to H^•(X⊗k̄, Q̄_ℓ) in AlgebraicGeometry.WeilSheaf.exists_traceCup_poincarePairing (WeilSheaf/PoincareDuality.lean:223, al… |
| `corollary-cup-product-pairing--3` | inside a proof |  | Inline step of the proof of even middle Betti number (Q̄_ℓ, X₀ over F_q). The blueprint argument is the same. |
| `corollary-verdier-exchange-formulas--2` | project lemma | `AlgebraicGeometry.WeilComplex.nonempty_verdierDual_derivedLowerStar_iso` | WeilConjectures/WeilSheaf/VerdierDualLocalization.lean:120 (namespace AlgebraicGeometry.WeilComplex): Nonempty (D_Y (Rf_* G) ≅ Rf_! (D_X G)) for a separated finite-type f over k₀ = F_q, Q̄_ℓ Weil complexes (docstring: 'Step 1: the dual of a direct image'). Sa… |
| `corollary-verdier-exchange-formulas--3` | the declaration's own name | `AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_verdierDual` | WeilConjectures/SixFunctors/Etale/Derived/BoundaryDuality.lean:95: for any i : Z ⟶ T with compactification (and aT, i≫aT compactifiable), finite Λ, Nonempty (Ri^! (D_T K) ≅ D_Z (Li^* K)) for every K — exactly D_X f^* ≅ f^! D_Y (no ctf hypothesis needed). It i… |
| `corollary-verdier-exchange-formulas--4` | partial |  | No declaration states D_X f^! L ≅ f^* D_Y L for general f (grep for verdierDual applied to op(Rf^! ...) finds only the closed-immersion case BoundaryDuality.lean:115, a parent name, = clause --7). WeilConjectures/SixFunctors/Etale/Derived/Stability/CtfStabili… |
| `corollary-verdier-exchange-formulas--6` | project lemma |  | No open-immersion-specific declaration found. WeilConjectures/WeilSheaf/VerdierDualLocalization.lean:120 (D_Y Rf_* G ≅ Rf_! D_X G for separated finite-type f) specializes to j. It is used with f = j in nonempty_verdierDual_upperStar_derivedLowerStar_iso (line… |
| `corollary-verdier-exchange-formulas--7` | the declaration's own name | `AlgebraicGeometry.Etale.nonempty_iso_leftDerivedUpperStar_verdierDual` | WeilConjectures/SixFunctors/Etale/Derived/BoundaryDuality.lean:115: k alg. closed, closed immersion i : Z ⟶ T, L ∈ Dctf(T, Λ), Nonempty (Li^* (D_T L) ≅ D_Z (Ri^! L)) — exactly i^* D_X ≅ D_Z i^!. It is a parent lean name. Conflicts: AlgebraicGeometry.Etale.non… |
| `definition-frobenius-operator--1` | the declaration's own name | `AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.compactFrobenius`<br>`AlgebraicGeometry.ProEtale.compactFrobenius` | The clause is the whole definition. WeilConjectures/TraceFormula/CompactCohomology.lean:290 WeilBoundedConstructible.compactFrobenius: the Frobenius of RΓ_c(X,(K,φ)), explicitly RΓ_c(X,K) ≅ L(𝟙)^*Ra_{X!}K --θ--> Ra_{X!}LΦ^*K --Ra_{X!}φ--> Ra_{X!}K (pullback t… |
| `definition-perfect-pairing--1` | the declaration's own name | `CategoryTheory.MonoidalClosed.IsPerfectPairing`<br>`AlgebraicGeometry.Etale.IsPerfectPairing` | Clause = whole definition. WeilConjectures/Mathlib/CategoryTheory/Monoidal/Closed/Basic.lean:217 structure IsPerfectPairing (b : X ⊗ Y ⟶ 𝟙) : isIso (curry b), i.e. the adjoint Y → [X,𝟙] is an iso; WeilConjectures/SixFunctors/Etale/Derived/TensorStructure.lean… |
| `lemma-class-of-point--1` | the declaration's own name | `AlgebraicGeometry.Etale.exists_tateOrientation_traceMap_pointClass` | WeilConjectures/EtaleCohomology/PoincareDuality/TraceIsomorphism.lean:371: ∃ Tate orientation γ such that γ.traceMap (pointClass a x) = 1 for every k-point x (finite self-injective Λ). The parent's only name; it is clause --1 in existential form (normalized o… |
| `lemma-class-of-point--2` | not formalized |  | Not used downstream in Lean. |
| `lemma-double-dual-geometric-generic-fibre--1` | the declaration's own name | `AlgebraicGeometry.Etale.exists_iso_leftDerivedUpperStar_dualizingComplex_of_generic`<br>`AlgebraicGeometry.Etale.isIso_leftDerivedUpperStar_map_verdierDualDoubleDual_app_iff_of_generic` | Clause = whole lemma. WeilConjectures/SixFunctors/Etale/Derived/GenericFibre/Duality.lean:92: Lg^*ω_X ≅ ω_{X'} ⊗ L for an invertible L (pullback of ω_S; for S=A¹, Λ(1)[2]), Zariski-locally (X → P closed, P → S smooth). :173: Lg^*δ_K is an iso iff δ_{Lg^*K} is… |
| `lemma-internal-adjunction-two-exchange-formulas--3` | the declaration's own name | `AlgebraicGeometry.Etale.nonempty_iso_verdierDual_leftDerivedUpperStar`<br>`AlgebraicGeometry.WeilComplex.nonempty_upperShriek_verdierDual_iso` | WeilConjectures/SixFunctors/Etale/Derived/DualityPullback.lean:176 states Nonempty (Lf^*.op ⋙ 𝔻_X ≅ 𝔻_Y ⋙ Rf^!), i.e. f^! 𝔻_Y L ≅ 𝔻_X f^* L (finite Λ, all of D(Y_et), natural iso). WeilConjectures/WeilSheaf/VerdierDualLocalization.lean:137 states Rf^! 𝔻_Y K ≅… |
| `lemma-internal-adjunction-two-exchange-formulas--4` | partial |  | WeilConjectures/SixFunctors/Etale/Derived/DoubleDualCompat.lean:337 map_verdierDualDoubleDual_app_comp_mateEquiv: for ANY square α : 𝔻_Y Rf_* ⟶ Rf_* 𝔻_X and its mate m, Rf_*δ_K ≫ m_{𝔻_X K} = δ_{Rf_*K} ≫ 𝔻_Y α_K (the 'formal core'). The clause is this with α =… |
| `lemma-perfect-complexes-geometric-point--6` | the declaration's own name | `AlgebraicGeometry.Etale.isPerfect_geometricStalk`<br>`AlgebraicGeometry.Etale.isPerfect_geometricStalk_of_field`<br>`AlgebraicGeometry.Etale.isPerfect_geometricStalk_padicAlgCl` | WeilConjectures/SixFunctors/Etale/Derived/Finiteness/CompactSupport.lean:236 isPerfect_geometricStalk (parent name): for K ∈ Dctf(X,Λ), finite Λ, RΓ(Spec Ω, Lx̄^*K) is perfect. Field-coefficient versions (on no node): WeilConjectures/SixFunctors/Etale/Derived… |
| `lemma-perfect-complexes-geometric-point--7` | the declaration's own name | `DerivedCategory.IsPerfect.ihom_unit` | WeilConjectures/CategoryTheory/DerivedCategory/Perfect.lean:437 IsPerfect.ihom_unit: C perfect in D(ModuleCat R) ⇒ (ihom C).obj 𝟙 = RHom_R(C,R) perfect. Already a parent name; any comm ring R, so covers each perfect complex of the lemma. |
| `lemma-perfect-complexes-geometric-point--8` | the declaration's own name | `DerivedCategory.IsPerfect.isIso_toIhomIhomUnit` | WeilConjectures/CategoryTheory/DerivedCategory/Perfect.lean:602 IsPerfect.isIso_toIhomIhomUnit: for C perfect, the biduality map toIhomIhomUnit C : C ⟶ [[C,𝟙],𝟙] (curry of braiding ≫ evaluation) is an iso, for a given braiding on D(R). Already a parent name. |
| `proposition-purity-trace-commute-frobenius--1` | project lemma | `AlgebraicGeometry.Scheme.Hom.isPullback_geometricGaloisFrobenius_geometricFiberMap` | WeilConjectures/AlgebraicGeometry/GeometricFrobenius.lean:645 (namespace AlgebraicGeometry.Scheme.Hom): for φ : X₀ ⟶ Y₀ over k, the square of the base change φ̄ and the geometric Galois Frobenii Fr_X, Fr_Y is cartesian (IsPullback.of_horiz_isIso, since the ho… |
| `proposition-purity-trace-commute-frobenius--2` | project lemma | `AlgebraicGeometry.Etale.upperShriekBaseChangeMap`<br>`AlgebraicGeometry.Etale.isIso_upperShriekBaseChangeMap` | WeilConjectures/SixFunctors/Etale/Derived/VerdierDualWeil.lean:122 upperShriekBaseChangeMap: the exceptional base change Lg'^* Rf^! ⟶ Rf'^! Lg^*, defined as the mate of the inverse compact-support base change iso, which is how the clause's proof describes it.… |
| `proposition-purity-trace-commute-frobenius--3` | project lemma |  | WeilConjectures/SixFunctors/Etale/Derived/Exchange.lean:146: the compact-support base change map Lg^* Rf_! ⟶ Rf'_! Lg'^* (def AlgebraicGeometry.Etale.rightDerivedLowerShriekBaseChangeMap, LowerShriekBaseChange.lean:161, not on any node) is an iso for every ca… |
| `proposition-purity-trace-commute-frobenius--4` | the declaration's own name | `AlgebraicGeometry.Etale.isWeilMorphism_smoothPurityIso_hom`<br>`AlgebraicGeometry.Etale.PurityFrobeniusDatum.isWeilMorphism_schemeFrobenius_smoothPurityIso_hom` | WeilConjectures/EtaleCohomology/Purity/Smooth/WeilEquivariance.lean:139: for a cartesian square g_X ≫ f = f ≫ g_Y, the smooth purity map γ_{f,K} is a morphism of Weil objects between φ^pur (pullback datum with Tate twist) and φ^! — i.e. Fr_X^* γ_f(K) = γ_f(Fr… |
| `proposition-purity-trace-commute-frobenius--5` | the declaration's own name | `AlgebraicGeometry.Etale.isWeilMorphism_smoothCoefficientTrace`<br>`AlgebraicGeometry.Etale.PurityFrobeniusDatum.isWeilMorphism_schemeFrobenius_smoothCoefficientTrace` | WeilEquivariance.lean:213: the smooth trace Tr_{f,K} = counit ∘ Rf_! γ is a morphism of Weil objects for the compact-support transport of φ^pur and φ_K. This is the clause. Caveat: it assumes hcoh (smooth pullback exchange = exceptional base change, the base-… |
| `theorem-global-verdier-duality--1` | the declaration's own name | `AlgebraicGeometry.Etale.nonempty_iso_ihom_compactlySupportedGlobalSections_verdierDual`<br>`AlgebraicGeometry.Etale.globalVerdierDualityIso`<br>`AlgebraicGeometry.Etale.nonempty_iso_coefficientDual_rightDerivedLowerShriek` | WeilConjectures/SixFunctors/Etale/Derived/GlobalDuality.lean:251: over separably closed k, finite Λ, RHom_Λ(RΓ_c(X,K),Λ) ≅ RΓ(X,𝔻_X K) ((10.5) literally). GlobalVerdierDuality.lean:221 globalVerdierDualityIso and GlobalDuality.lean:216 give it in D(S_et) form… |
| `theorem-global-verdier-duality--2` | partial |  | No étale/Λ-coefficient statement of RΓ_c(X,𝔻_X K) ≅ RHom_Λ(RΓ(X,K),Λ) (or of 𝔻_Y Rf_* ≅ Rf_! 𝔻_X) exists; LEAN-MAPPING.md also records '(10.6) not found'. ProEtale.CondensedRing.dualVerdierExchange (PoincareDuality/Verdier.lean:226) only defines the map Θ_K :… |
| `theorem-global-verdier-duality--3` | project lemma | `AlgebraicGeometry.Etale.uncurry_derivedHomLowerShriekIsoOfAdjunction_hom_app_app` | WeilConjectures/SixFunctors/Etale/Derived/PoincareIdentification.lean:193: uncurry of the tensor–Hom exchange Ra_*RHom(M,G N) ⟶ RHom(Ra_!M,N) equals exchangePairing (PoincareIdentification.lean:182) = mixed-support cup product ≫ Ra_!(evaluation) ≫ counit of R… |
| `theorem-poincare-duality--1` | project lemma |  | WeilConjectures/EtaleCohomology/Purity/Smooth/Basic.lean:205 nonempty_iso_dualizingComplex_twistShift: f smooth of rel. dim d, normalized Tate twist, finite Λ with invertible exponent: ω ≅ Λ_X(d)[2d]. Already on theorem-smooth-purity-all-admissible-coefficien… |
| `theorem-poincare-duality--2` | the declaration's own name | `AlgebraicGeometry.Etale.Orientation.nonempty_iso_verdierDual_coefficientDual` | WeilConjectures/SixFunctors/Etale/Derived/Orientation.lean:448: for an orientation o of rel. dim d and K dualizable (=perfect), 𝔻_X K ≅ K^∨ ⊗ᴸ Λ_X(d)[2d]. Already a parent name. Lean needs K dualizable (blueprint states it for all K ∈ Dctf). |
| `theorem-poincare-duality--3` | project lemma | `AlgebraicGeometry.Etale.DerivedCategory.coefficientDual` | WeilConjectures/SixFunctors/Etale/Derived/Perfect/Dual.lean:78 coefficientDual := (RHom(X)[A]).flip.obj 𝟙, i.e. K^∨ = RHom_X(K, Λ_X). On no node. (twistedDual, EtaleCohomology/PoincareDuality/Pairing.lean:76, is K^∨(d).) |
| `theorem-poincare-duality--4` | project lemma | `AlgebraicGeometry.Etale.DerivedCategory.isDualizable_coefficientDual` | WeilConjectures/SixFunctors/Etale/Derived/Perfect/Dual.lean:119: IsDualizable K ⇒ IsDualizable K^∨. Lean renders 'perfect over Λ_X' as dualizability (convention in the file header); 'locally perfect ⇔ dualizable' is that convention, not proved here. On no nod… |
| `theorem-poincare-duality--5` | project lemma | `AlgebraicGeometry.Etale.DerivedCategory.coefficientDualIsoOfExactPairing` | WeilConjectures/SixFunctors/Etale/Derived/Perfect/Dual.lean:109: for an exact pairing (L,K), K^∨ = RHom(K,Λ_X) ≅ L, i.e. the internal dual is the (rigid) dual. Under the dualizability convention for 'perfect' this is 'K^∨ is the ordinary dual'. On no node. Mo… |
| `theorem-poincare-duality--6` | the declaration's own name | `AlgebraicGeometry.Etale.TateOrientation.isPerfectPairing_poincarePairing`<br>`AlgebraicGeometry.Etale.isPerfectPairing_poincarePairing_of_isSepClosed_of_isDualizable`<br>`AlgebraicGeometry.Etale.isPerfectPairing_poincarePairing` | WeilConjectures/EtaleCohomology/PoincareDuality/Pairing.lean:137 TateOrientation.isPerfectPairing_poincarePairing: β_K : Ra_!K ⊗ (Ra_*(K^∨(d)))[2d] → Λ_Y (cup product, twisted evaluation, smooth trace) is perfect for finite Λ, K dualizable. WeilConjectures/Si… |
| `theorem-poincare-duality--7` | project lemma | `AlgebraicGeometry.Etale.curry_poincarePairing_eq`<br>`AlgebraicGeometry.Etale.inv_curry_poincarePairing_eq` | WeilConjectures/SixFunctors/Etale/Derived/PoincareIdentification.lean:290 curry_poincarePairing_eq: curry β_K = (shift) ≫ Ra_*(purityVerdierDualMap γ K) ≫ (globalVerdierDualityIsoOfAdjunction K)^{-1}, i.e. the adjoint of β_K is the canonical map RΓ(X,K^∨(d))[… |
| `theorem-poincare-duality--8` | the declaration's own name | `AlgebraicGeometry.Etale.TateOrientation.isPerfectPairing_properPoincarePairing`<br>`AlgebraicGeometry.Etale.isPerfectPairing_properPoincarePairing` | WeilConjectures/EtaleCohomology/PoincareDuality/Pairing.lean:158 (parent name): for proper a, β_K read through Ra_! ≅ Ra_* (RΓ(X,K) ⊗ RΓ(X,K^∨(d))[2d] → Λ) is perfect. SixFunctors/Etale/Derived/PoincarePairing.lean:462 is the general-orientation version (on n… |
| `theorem-poincare-duality--9` | partial |  | WeilConjectures/EtaleCohomology/PoincareDuality/FiniteReduction.lean:137 map_poincarePairing: for a lax monoidal coefficient change G (e.g. reduction A_n → A_m) with comparison maps, G(β_K) = β_{K'} read through the comparisons, but only under hypotheses hE (… |
| `theorem-poincare-duality-frobenius--1` | project lemma | `AlgebraicGeometry.Etale.contragredientWeilDatum`<br>`AlgebraicGeometry.Etale.contragredientWeilDatumIso` | WeilConjectures/SixFunctors/Etale/Derived/WeilDual.lean:255 contragredientWeilDatum (docstring 'def-pod-dual-tate-datum'): Lg^* K^∨ ≅ RHom(Lg^*K, Lg^*Λ) → RHom(Lg^*K, Λ) → RHom(K, Λ) via φ_K^{-1}, which is the clause's Fr^*K^∨ ≅ (Fr^*K)^∨ --(φ_K^{-1})^∨--> K^… |
| `theorem-poincare-duality-frobenius--2` | project lemma | `AlgebraicGeometry.Etale.TateOrientation.isWeilPairing_poincarePairing_of_iso` | WeilConjectures/EtaleCohomology/PoincareDuality/Frobenius/DualTateData.lean:125: β_K is a morphism of Weil objects (IsWeilPairing) for φ_K, the contragredient twisted datum φ_{K^∨}⊗τ on K^∨(d) and the canonical datum on Λ_Y. More specific than the parent's Ta… |
| `theorem-poincare-duality-frobenius--3` | project lemma | `AlgebraicGeometry.Etale.TateOrientation.degreewisePoincarePairing_frobeniusOperator_eq_of_iso`<br>`AlgebraicGeometry.Etale.TateOrientation.degreewisePoincarePairing_frobeniusOperator_eq` | DualTateData.lean:147 (_of_iso, with the contragredient datum built in) and Frobenius/Equivariance.lean:123 (_eq, dual datum as hypothesis): ⟨F_{c,K} x, F_{K^∨(d)} y⟩_i = ⟨x, y⟩_i for H^i_c(X,K) × H^{2d-i}(X,K^∨(d)) → Λ, assuming End(Λ_Y) = Λ (true for Y = Sp… |
| `theorem-poincare-duality-frobenius--4` | project lemma | `AlgebraicGeometry.Etale.TateOrientation.untwistedDegreewisePoincarePairing_frobeniusOperator_of_iso` | DualTateData.lean:173: ⟨F_{c,K} x, F_{K^∨} y⟩^{untw}_i = q^d ⟨x,y⟩^{untw}_i, with F_{K^∨} from the contragredient datum, given τ on Λ_Y(-d) acting by q^d and the untwisted-trace equivariance hTr (hypothesis). The parent name TateOrientation.untwistedDegreewis… |
| `theorem-poincare-duality-frobenius--5` | partial |  | No declaration states that F is invertible on H^i_c(X,K). WeilConjectures/ZetaLinearAlgebra/Pairing.lean:131 LinearMap.isUnit_det_of_similitude (also injective_of_similitude, :111): for a perfect pairing p over a field with p(Fv,Gw) = c·p(v,w), c ≠ 0, det F i… |
| `theorem-poincare-duality-frobenius--6` | the declaration's own name | `AlgebraicGeometry.Etale.TateOrientation.conj_frobeniusOperator_eq_smul_inverse_dualMap` | Frobenius/Reciprocity.lean:62: Λ a field, line-valued untwisted pairing perfect (assumed as an instance), then Φ ∘ F_{K^∨} ∘ Φ^{-1} = q^d · (F_{c,K}^t)^{-1}, exactly the inverse-transpose clause. Conflicts: AlgebraicGeometry.Etale.TateOrientation.conj_frobeni… |
| `theorem-poincare-duality-frobenius--7` | Mathlib | `Module.finrank_of_isPerfPair` | Mathlib/LinearAlgebra/PerfectPairing/Basic.lean:79: a perfect pairing p : M →ₗ N →ₗ R with M finite free gives finrank R M = finrank R N. Applied to the untwisted pairing, made perfect by corollary-degreewise-duality-over-fields, this is the clause, as in the… |
| `theorem-poincare-duality-frobenius--8` | the declaration's own name | `AlgebraicGeometry.Etale.TateOrientation.roots_map_charpoly_frobeniusOperator` | Frobenius/Reciprocity.lean:97: roots (with multiplicity, in an alg. closed M ⊇ Λ) of charpoly F_{K^∨} on H^{2d-i}(X,K^∨) are ι(q^d)/α for the roots α of charpoly F_{c,K} on H^i_c(X,K). Exactly the clause; perfectness and freeness/finiteness are hypotheses. Co… |
| `theorem-poincare-duality-frobenius--9` | project lemma | `LinearMap.det_mul_det_of_similitude` | WeilConjectures/ZetaLinearAlgebra/Pairing.lean:194 (project file, namespace LinearMap): for a perfect pairing over a field and a similitude pair (F, G) with factor c, det F · det G = c^{finrank V}. With c = q^d, F = F_{c,K}, G = F_{K^∨} (similitude = clause -… |
| `theorem-trace-isomorphism-top-degree--3` | partial |  | WeilConjectures/EtaleCohomology/PoincareDuality/TraceIsomorphism.lean:215: for X smooth proper geometrically connected over alg. closed k, finite Λ with Module.Injective Λ Λ, every Tate orientation γ: tr^{(-d)} : H^{2d}(X, Λ) → Λ(-d) (ordinary cohomology, via… |
| `theorem-trace-isomorphism-top-degree--5` | not formalized |  | Lean skips the O_E stage: finite self-injective Λ (étale) and Q̄_ℓ Weil sheaves (existential) are proved separately. |
| `theorem-trace-isomorphism-top-degree--6` | not formalized |  | Different from the blueprint, which goes O_E → E (flat scalar extension) → Q̄_ℓ. Lean goes profinite lattices → Q̄_ℓ by a filtered colimit and never states the E stage. |
| `theorem-trace-isomorphism-top-degree--7` | not formalized |  | Not formalized; Lean goes directly to Q̄_ℓ. |
| `theorem-trace-isomorphism-top-degree--9` | partial |  | WeilConjectures/WeilSheaf/TraceIsomorphism.lean:324, clause 4: for X₀ proper over F_q, ∃ an iso H^{2d}(X₀⊗k̄, Q̄_ℓ) ≃ Q̄_ℓ with F acting by q^d (also the H_c and twisted forms). It is existential: some Frobenius-compatible iso, not that the specified trace tr… |
| `theorem-verdier-biduality--1` | the declaration's own name | `AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app`<br>`AlgebraicGeometry.Etale.isIso_verdierDualDoubleDual_app_of_field` | WeilConjectures/SixFunctors/Etale/Derived/VerdierBiduality.lean:74 (k algebraically closed) and VerdierBidualityField.lean:256 (any field k, exponent of Λ invertible): δ_K : K → 𝔻𝔻K is an iso for K ∈ Dctf(X,Λ), finite Λ, on the étale site (the blueprint's pro… |
| `theorem-verdier-biduality--3` | not formalized |  | Lean skips the E stage: finite → 𝒪_E (derived Nakayama) → Q̄ℓ (integral models + scalar extension). |
| `theorem-verdier-biduality--5` | partial |  | WeilConjectures/WeilSheaf/VerdierDual.lean:120: 𝔻_X on Weil complexes (Q̄ℓ, over a finite field k₀) commutes with shifts and is triangulated. For étale finite-coefficient Dctf and pro-étale 𝒪_E/Q̄ℓ Dᵇc no exactness statement for 𝔻_X exists; the general 'RHom(… |
| `theorem-verdier-biduality--6` | the declaration's own name | `AlgebraicGeometry.Etale.verdierDualEquivalence` | WeilConjectures/SixFunctors/Etale/Derived/VerdierBiduality.lean:103: (DerivedCategoryFiniteTor Λ X)ᵒᵖ ≌ DerivedCategoryFiniteTor Λ X induced by 𝔻_X with unit/counit δ (k algebraically closed, finite Λ). Only finite Λ; no anti-equivalence is stated for 𝒪_E or … |

### chap-Weights

| Clause | Verdict | Names placed | Why |
|---|---|---|---|
| `lemma-filtrations-spectra--2` | inside a proof |  | Parent name charpoly_eq_charpoly_restrict_mul_charpoly_mapQ is the two-step charpoly factorization. The multiset form is obtained ad hoc where needed (Rankin/purity proof) via Polynomial.roots_prod. |
| `lemma-global-lattice-normal-scheme--1` | partial |  | Clause text equals the parent. WeilConjectures/SixFunctors/ProEtale/Adic/LisseCover/RegularLattice.lean:41/96: for a REGULAR Noetherian scheme and a descent cocycle γ to GL_n(E) on a pro-étale cover, there is a lattice-valued twisted section. This is the cocy… |
| `lemma-subobjects-quotients-weil-sheaves--3` | the declaration's own name | `AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.of_mono` | Parent names AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.of_mono / .of_epi (DeligneLaumon/Reduction/Weights.lean, filtrationClosure closed under subobjects/quotients) are exactly the bounded part of the clause; a subquotient is of_epi after of_mono. Fo… |
| `proposition-lattices-representations-normal-scheme--1` | partial |  | Clause text equals the parent. WeilConjectures/SixFunctors/ProEtale/Adic/LisseMonodromyExists.lean:47: on a connected Noetherian scheme with integrally closed domain stalks (normal), there is a LisseMonodromy that is an equivalence at every base point (lisse … |
| `proposition-weights-under-usual-operations--1` | partial |  | WeilConjectures/DeligneLaumon/Reduction/Weights.lean:213 IsMixedOfWeightsAtMost.of_shortExact (parent name) states the version with a common bound w. No IsMixed extension lemma exists. The unbounded 'mixed' form follows by taking max of the bounds and IsMixed… |
| `proposition-weights-under-usual-operations--5` | partial |  | WeilConjectures/WeilSheaf/StalkTensor.lean:372 HasWeightsAtMost.tensorObj: F lisse with punctual weights <= w, G with punctual weights <= w' gives F⊗G with punctual weights <= w+w'. This is the punctual-upper-bound analogue, not mixedness. No sheaf-level mixe… |
| `proposition-weights-under-usual-operations--6` | partial |  | WeilConjectures/RepresentationTheory/Dual.lean:58 Representation.HasGradedPieces.dual: the annihilators of a filtration of ρ form a filtration of ρ^∨ whose graded pieces are the contragredients of the graded pieces (via Subrepresentation.subquotientDualEquiv,… |
| `proposition-weights-under-usual-operations--9` | partial |  | WeilConjectures/DeligneLaumon/Reduction/FormalSteps.lean:119/132 state preservation of 'mixed of weights at most w' under pullback only along an immersion [IsImmersion h] (the docstring says the hypothesis is unused); both are parent names. For a general morp… |
| `proposition-weights-under-usual-operations--11` | project lemma | `AlgebraicGeometry.WeilSheaf.stalkAt_frobenius_constantTwist_adicConstant` | WeilConjectures/WeilSheaf/Tensor.lean:86 WeilSheaf.constantTwist F b := F ⊗ 𝓑_b (same sheaf, Weil structure b•φ; docstring cites def-wf-constant-weil-twist), so 𝓑_b = (adicConstant).constantTwist b. It is already on proposition-twisting-weight-zero-adding-dua… |
| `proposition-weights-under-usual-operations--14` | the declaration's own name | `AlgebraicGeometry.WeilSheaf.HasWeightsAtMost.tateTwist` | Parent names AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.tateTwist (EtaleCohomology/Purity/RealSheaves/SheafWeightOperations.lean:140: pure of weight w gives F(n) pure of weight w-2n) and IsMixedOfWeightsAtMost.tateTwist (:151) state exactly the clau… |

