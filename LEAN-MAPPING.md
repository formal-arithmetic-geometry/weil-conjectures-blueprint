# Lean names and dependencies of the declarations

How the `lean` and `uses` attributes of `blueprint/` were filled in, and how sure each Lean match is.

## Method

- **Lean names.** Each declaration was matched with the sketch node of `blueprint_old/` that states it, and that node's `lean` list (and its detail nodes') was checked against the Lean statements at the pinned revision of weil-conjectures. Names that only serve the proof were dropped. Where the old blueprint had none, the formalisation was searched for a declaration that states it. Every name exists at the pinned revision, and no name belongs to two declarations.
- **Coverage.** 421 of 538 declarations have Lean names: 233 high, 148 medium and 40 low confidence. Medium and low mean the Lean states only part of the declaration, a special case, or a variant (often with other coefficients); the notes below say which. 117 declarations, mostly examples and remarks, have none.
- **Second review: the pro-étale chapter and Appendices A–D and F** (139 declarations). Each node's statement was gone through part by part against the Lean of slopmaster2 (`f3cad3b`, now pinned): every part that Lean states gets the declaration stating it, and names that only serve a proof, duplicate another name, or state another node's content were dropped. 81 nodes are fully stated in Lean, 43 partly and 15 not at all; 64 names were added and 48 removed. In the table their confidence reads *full*, *partial* or *none* (reviewed), and the note says what Lean does not state.
- **Declaration arrows.** `A uses B` when a Lean name of `A` depends on a Lean name of `B`, reached as `blueprint extract` walks it: through unmapped constants of the project and stopping at mapped ones. Dependencies of the Lean statement go on the declaration and those of the proof on its proof. The walk uses the dependency facts of the last site build (the `site` branch). For the Lean names those facts do not cover, it follows references in the Lean source instead. These are 446 of the 1066 names; they add 375 of the arrows. Where one end has no Lean name, the references in the text (statement or proof) give the arrow instead.
- **Cycles.** Lean dependencies between names grouped by declaration can form cycles; within each strongly connected component only the arrows to earlier declarations are kept (87 arrows dropped).
- **Sections and subsections** use each other where the unit itself builds on the other as the notes present it: its constructions, main results or arguments need what the other develops. Each arrow was decided by reading the unit (prose, statements and proofs) and what the notes say about the two units; the arrows of the declarations are not merged into it. One incidental citation (an example, a remark, a comparison) makes no arrow, and neither does a forward pointer ("proved below", "until Section X"). An arrow goes to the most specific unit used, a subsection when only that subsection is used, and arrows between a section and a subsection are allowed. A theorem stated in one section and proved in a later one: its users point at the section where the proof is completed, and that section points back to the statement. Chapters keep the arrows written on them by hand.
- **Every unit is used**, except: the units of Appendix E, which the main text does not use; the last section of the main text (Integrality and independence of ℓ, which proves the Weil conjectures); smooth base change for all admissible coefficients (`sec-ell-adic-coefficients-3`), since the later text uses only the torsion version; and five overview sections of the Introduction (the six operations, the trace formula, Deligne's theorem, Outline, Prerequisites and reading guide), which nothing builds on. `sec-The-projective-line` and `sec-Compatibilities` have no arrow of their own because all their content is in subsections, which are used.
- **No circular reasoning.** No chain of arrows returns to where it started: there is no cycle among the declarations, among the sections and subsections, or in all of them together. The two-way section arrows before came from merging all declaration arrows of a section into section arrows; two sections whose declarations use each other's in both directions got arrows both ways.

## Declarations

### The pro-étale site

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `definition-ind-etale-pro-etale-weakly` | 8 | full (reviewed) | Ind-étale (algebra and ring-hom forms), pro-affine étale with its affine case, and weakly étale (scheme class, ring property, affine-chart description) are all stated. |
| `proposition-etale-implications` | 4 | full (reviewed) | Lean has no ring-level étale⇒ind-étale or weakly étale+fp⇒étale with a name; the scheme forms with affine source cover them via Spec. |
| `lemma-stability` | 7 | full (reviewed) | Mathlib's unnamed instances, under their auto-generated names (checked with Lean against the pinned Mathlib). |
| `definition-small-pro-etale-site` | 4 | full (reviewed) | proetalePrecoverage is the quasi-compact (fpqc-type) covers by weakly étale maps; Mathlib's QuasiCompactCover gives the explicit open-cover condition. |
| `proposition-pro-etale-coverings` | 3 | partial (reviewed) | (1) is stated for any qcqs object; (2) as étale/Zariski precoverages contained in the pro-étale one. Not in Lean: In (1), that the disjoint union of the finite affine refinement is affine and faithfully flat over U. |
| `proposition-topos-functoriality` | 6 | partial (reviewed) | toposFunctorialityInverseImage bundles the morphism of sites, f^{-1}⊣f_*, exactness of f^{-1} (sets and abelian) and the composition isomorphism. Not in Lean: That Sh(X_proét) is a Grothendieck topos. |
| `definition-w-local-w-strictly-local` | 5 | full (reviewed) | One declaration for each notion the definition introduces. |
| `proposition-w-local-components` | 2 | partial (reviewed) | Parts (1) and (3) are formalized; a search for (2) found nothing. Not in Lean: Part (2): the component through a closed point m is the image of Spec(R_m), and the strictly henselian consequence. |
| `example-locally-constant-functions-w-local` | 1 | partial (reviewed) | Only the computation of the spectrum is in Lean. Not in Lean: That LC(S,k') is w-local and w-strictly local, the computation of its local rings, and that it is w-contractible iff S is extremally disconnected. |
| `proposition-gleason-s-theorem` | 1 | full (reviewed) | CompactT2.Projective is exactly the lifting property along surjections of compact Hausdorff spaces. |
| `lemma-extremally-disconnected-covers` | 4 | full (reviewed) | Stonean.toProfinite says extremally disconnected compact Hausdorff spaces are profinite. |
| `proposition-splitting-ind-etale-covers` | 1 | full (reviewed) | Exact statement. |
| `theorem-existence-contractible-covers` | 1 | full (reviewed) | Exact statement. |
| `theorem-pro-etale-refinements-weakly-etale` | 2 | full (reviewed) | Algebra and ring-hom forms of the same statement. |
| `proposition-pro-etale-affines-form-basis` | 5 | full (reviewed) | The sheaf equivalence holds for any coefficient category with enough limits, so it covers sets and abelian groups. |
| `lemma-w-contractible-affines-projective` | 2 | full (reviewed) | Splitting of epimorphisms onto h_U; projectivity follows by definition-weak-contractibility's equivalences. |
| `theorem-enough-affine-weakly-contractible-objects` | 1 | full (reviewed) | Lean also has duplicates weaklyContractible_basis (part 1) and exists_isWeaklyContractible_cover; not added. |
| `definition-weak-contractibility` | 2 | full (reviewed) | The definition (the third, surjectivity form) plus the theorem giving the equivalent forms. |
| `example-weak-contractibility-point` | 0 | none (reviewed) | Example; nothing in Lean. Not in Lean: The whole example (the convergent sequence is not weakly contractible). |
| `corollary-evaluation-weakly-contractible-objects` | 4 | partial (reviewed) | (1) exactness and H^q vanishing for Λ-modules; (2) and (3) for R-modules. Not in Lean: In (1), RΓ(W,K) ≃ K(W) for every (unbounded) complex K. |
| `definition-repleteness` | 1 | full (reviewed) | Exact definition for sheaf topoi of sites. |
| `proposition-repleteness-pro-etale-topos` | 1 | full (reviewed) | Exact statement. |
| `proposition-exact-products` | 2 | full (reviewed) | Exact products for any index type; derived products are termwise, with cohomology commuting. |
| `proposition-milnor-sequence` | 3 | full (reviewed) | milnor_sequence covers R^p lim and (2.2); milnor_epimorphic the epimorphic case; the general D(C) Milnor sequence is kept for (2.2). |
| `example-nonzero-rlim-one` | 0 | none (reviewed) | Example; nothing in Lean. Not in Lean: The whole example (R^1 lim of multiplication by ℓ is Z_ℓ/Z). |
| `proposition-left-completeness` | 2 | full (reviewed) | The pro-étale statement and the general one for abelian categories with exact countable products. Lean's left_complete is a duplicate (not added). |
| `proposition-unbounded-functors-products` | 1 | partial (reviewed) | Only Rf_* is covered, with countable products and derived limits of towers. Not in Lean: RΓ(U,-) on unbounded complexes preserving products and derived limits; Rf_* for f_*R-modules (Lean has A-valued sheaves) and arbitrary products (Lean has countable ones). |
| `proposition-weakly-contractible-hypercovers` | 2 | full (reviewed) | Existence of the single-affine weakly contractible hypercover and formula (2.3) for bounded-below complexes. |
| `corollary-continuity-cohomology` | 2 | partial (reviewed) | Lean has the abelian-sheaf (degree 0) case of both assertions. Not in Lean: Both assertions for uniformly bounded-below complexes and ring sheaves R; the first for a general qcqs object U (Lean: U = X qcqs). |
| `definition-classical-pro-etale-sheaves` | 4 | full (reviewed) | Presentation, continuity map (2.4), classical sheaves, and classical complexes of module sheaves. |
| `proposition-comparison-morphism-inverse-image` | 7 | partial (reviewed) | ν, ν_*, ν^* with general coefficients, the adjunction, exactness, and (2.6) for qcqs étale towers. Not in Lean: Formula (2.5), (ν^*F)(V) = Γ(V_ét, h^*F). |
| `theorem-classical-sheaves-essential-image` | 3 | full (reviewed) | proEtaleClassicalSheaves states all three parts; full/faithful instances give full faithfulness for any Grothendieck abelian coefficient category. |
| `example-coefficient-sheaf-outside-classical-part` | 0 | none (reviewed) | Example; nothing in Lean states it. Not in Lean: the whole example (Z_ell,X not classical, reductions classical) |
| `lemma-acyclicity-pulled-back-injectives` | 1 | full (reviewed) | General Grothendieck abelian coefficients; covers Lambda-modules. |
| `theorem-bounded-below-cohomology-comparison` | 3 | full (reviewed) | boundedBelowComparison: unit iso, full faithfulness, RGamma iso (map = boundedBelowComparisonGlobalSections); unit_app is the general-coefficient form of (2.7). |
| `corollary-cohomology-pro-etale-affine` | 2 | partial (reviewed) | The étale continuity for D^+ (AlgebraicGeometry.derivedEtaleCohomology_limit) is only the proof's étale step, so it is not listed. Not in Lean: bounded-below complexes K (Lean: single abelian sheaves, degreewise); right side is pro-étale cohomology of the stages, equal to étale one via comparison |
| `corollary-bounded-below-classical-complexes` | 1 | partial (reviewed) | Hypothesis hunit is discharged by boundedBelowComparison (other node); coefficients CommRing with discrete topology. Not in Lean: weak Serre property (closure under kernels, cokernels, extensions) of classical module sheaves; Lean equivalence assumes the D+ unit iso as hypothesis |
| `theorem-comparison-direct-images` | 3 | full (reviewed) | General Grothendieck abelian coefficients on D+. isIso_comparisonDirectImagePlus is a Ring-Λ duplicate, not listed. |
| `lemma-comparison-direct-images-compatibilities` | 2 | partial (reviewed) | Both use c_g = rightDerivedFunctorPlusBaseChange(lowerStarComparisonUpperStarBaseChange), the map of theorem-comparison-direct-images. Not in Lean: part (1) (unit compatibility) not stated; part (2) only for finite Λ and qcqs g |
| `proposition-comparison-immersions` | 4 | partial (reviewed) | Closed-immersion direct-image iso is the content of theorem-comparison-direct-images, left there. Not in Lean: part (2): transport of the localization triangle to the pro-étale one with counit/unit identification |
| `lemma-torsors-under-classical-groups` | 0 | none (reviewed) | Doubtful: AlgebraicGeometry.Scheme.proEtale_locallyClassical_etaleCover (1),(3) (locally classical => classical, étale-local sections) implies it; assigned to the next proposition. Not in Lean: torsors under classical groups are classical with étale trivialization (no torsor statement in Lean) |
| `proposition-locally-constant-sheaves-finite-presentation` | 1 | partial (reviewed) | Lean: set-valued sheaves; locally constant => classical, with étale-local sections. Its parts (1),(3) also cover the torsor lemma. Not in Lean: Λ-module/finite presentation form; ν^* identifying étale and pro-étale local systems of finite presentation |
| `theorem-comparison-constructible-sheaves` | 1 | full (reviewed) | Covers classicality, the sheaf equivalence and the D^b_c equivalence (Noetherian coefficients, qcqs X). |
| `corollary-finite-tor-amplitude-under-comparison` | 1 | full (reviewed) | Tor amplitude preserved and detected, and the restricted ctf equivalence. |
| `definition-cohomological-dimension` | 2 | full (reviewed) | Suprema over classical ell-power torsion abelian sheaves; field notation is Spec K. |
| `lemma-cohomological-dimension-base-field` | 1 | full (reviewed) |  |
| `lemma-uniform-bounds-pro-etale-affines` | 2 | partial (reviewed) | Lean works with torsion abelian étale sheaves pulled back by ν^*, which covers classical A-module sheaves. Not in Lean: the bound d = dim X + cd_ell(k) (Lean bound is 2·dim X + 1 for both vanishings); k only finite or algebraically closed |
| `lemma-truncation-pro-etale-sections` | 0 | none (reviewed) | Only a private special case (étale affine W) exists: section_tail_bound in FiniteClassicalUnboundedComparison.lean. Not in Lean: the whole lemma |
| `proposition-unbounded-comparison-finite-coefficients` | 1 | partial (reviewed) | k finite or algebraically closed, A finite ell-primary. unboundedDirectImageComparison_boundedBelow is only the bounded-below case. Not in Lean: unbounded direct-image comparison (2.9) for all K in D(X_et,A); Lean only has the bounded-below case |
| `proposition-pro-etale-site-separably-closed` | 3 | partial (reviewed) | Sheaves of continuous functions are definitions (Profinite.continuousMapRingSheaf) of prose, not listed. Not in Lean: equivalence of pro-étale affines with profinite sets stated only as a dense subsite; topos equivalence stated for abelian sheaves |
| `lemma-comparison-completed-coefficients` | 1 | full (reviewed) | Integral limit, inverting ell, colimit over E and compatibility with pullback. |
| `corollary-finite-quotients-their-transition-maps` | 1 | full (reviewed) | Also contains the cone identification K_n = cone(π^n) of lemma-reduction-derived-nakayama part 1; one name, kept here. |
| `definition-tate-twists` | 11 | full (reviewed) | Doubtful: two parallel formalizations. Chose sk-def-sp family (follows text, used by spTwists_locallyFree); tateModule/tateTwistOne kept for the 'equivalently Qbar⊗Z_ell(1)' clause. |
| `lemma-inverse-image-coefficient-sheaves` | 2 | full (reviewed) | isIso_condensedPullbackHom gives f^{-1}Λ_Y ≅ Λ_X for every condensed ring; cartesianCoefficients adds twists and finite freeness. |
| `proposition-continuous-cohomology-pro-etale-cohomology` | 1 | full (reviewed) | Abelian sheaves presented as modules over the constant integer sheaf. |
| `corollary-continuous-etale-cohomology` | 0 | none (reviewed) | No Lean statement found. Not in Lean: identification with continuous étale cohomology (derived functor on inverse systems) |
| `example-first-cohomology-finite-field` | 0 | none (reviewed) | Example; not formalized. Not in Lean: the whole example (H^1 of F_q with Z_ell and Q_ell coefficients) |
| `proposition-extension-zero-restriction-closed-subscheme` | 10 | partial (reviewed) | Sheaf of R-algebras B; every assertion except j^* exactness has a matching RingSheaf declaration. Not in Lean: exactness of j^* not stated separately for module sheaves |
| `definition-local-cohomology` | 2 | partial (reviewed) | Lean defines i^*ker(id→j_*j^*) and its right derived functor; closedSupport_fiber gives the fibre formula. Not in Lean: arbitrary sheaf of rings R (Lean: pulled-back condensed coefficient ring Λ) |
| `lemma-local-cohomology-right-adjoint` | 1 | partial (reviewed) | i_* ⊣ RΓ_Z on derived categories of condensed-coefficient modules. Not in Lean: arbitrary sheaf of rings R; full faithfulness of derived i_* not part of this statement |
| `definition-derived-adic-completeness` | 2 | full (reviewed) | Completion map via K-flat representative; iff shows independence of representative. |
| `lemma-reduction-derived-nakayama` | 1 | partial (reviewed) | States K_1=0 ⇒ K=0 for derived complete K and the isomorphism criterion. Not in Lean: K_n = cone(π^n: K→K) stated in derived_nakayama_resolution, assigned to corollary-finite-quotients-their-transition-maps |

### Constructible complexes

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `definition-constructible-sheaves` | 8 | medium | Old sk-def-sfb-constructible plus constant-model defs whose docstrings cite its clauses 1-2; Tor amplitude defs. |
| `definition-lisse-sheaves` | 2 | medium | Condition (1) on X itself (locally finitely presented); IsLisseCoefficientModule is the lisse (locally free) predicate used for field coefficients. |
| `remark-constructible-sheaves-coefficient-rings` | 0 | — | Remark (sk-rem-n-constructible); no Lean statement of exactly it. |
| `example-integral-criterion-point` | 0 | — | Example; nothing formalizes it. |
| `lemma-bounds-finite-reductions` | 1 | high | Lean theorem cites sk-lem-integral-finite-levels; statement matches. |
| `lemma-perfect-complexes-over-oe` | 0 | — | Old sk-lem-integral-scalar-towers had no lean; only Padic.scalarQuotient defs exist, no theorem found. |
| `lemma-images-cohomology-finite-levels` | 0 | — | Clause (2) of old sk-lem-integral-scalar-towers; only defs (Padic.scalarQuotient) found, no theorem. |
| `lemma-local-constancy-finite-level` | 0 | — | No old node; no Lean formalization found. |
| `lemma-integral-model-weakly-contractible` | 0 | — | Proof step of local structure in old blueprint; no public Lean statement found. |
| `proposition-local-structure-integral-constructible-complexes` | 1 | high | Lean theorem cites sk-prop-integral-local-structure; statement matches (currently sorry). |
| `proposition-integral-constructibility-criterion` | 3 | medium | Docstrings cite sk-prop-integral-criterion: (1)<=>(2); residue criterion gives Dbc=Dctf (4). Clause (3) not separately stated. |
| `proposition-ctf-equals-bc` | 1 | high | States Dctf=Dbc for Z_l, Q_l, O_E, E, Qlbar (det-def-localizing-closure-ctf-equals-bc). |
| `lemma-flat-models-generators` | 3 | medium | Old sk-lem-sf-flat-model (etale flat model) plus pro-etale flat model and etale generation by a_!L. |
| `definition-lattice` | 0 | — | No Lean definition of lattices found; lattice existence results are stated inline. |
| `lemma-lattices-lisse-e-sheaves` | 2 | low | Only the "in particular" clause (lattice etale locally) is formalized; representability of the lattice sheaf is not. |
| `example-lattices-nodal-curve` | 0 | — | Example; not formalized. |
| `lemma-descent-lisse-qbar-sheaves-finite` | 1 | high | Docstring cites det-lem-coefficient-finite-descent-lisse; descends lisse Qlbar modules and morphisms to finite E. |
| `lemma-constructible-sheaves` | 4 | medium | coefficientHeart states all clauses of sk-lem-coefficient-heart; the other three are its clause-wise theorems. |
| `example-running-example` | 0 | — | Example; not formalized. |
| `corollary-coefficient-heart-b` | 2 | medium | Lean cites sk-cor-coefficient-heart-ii: triangulated and generation by a_!L. |
| `lemma-sections-support-closed-subscheme` | 2 | medium | Docstrings cite det-lem-formal-closed-support-derived/adjunction (clause 1); stratum Hom formula (3.1) only private. |
| `lemma-continuity-ext-out-constructible-complex` | 2 | medium | Lean cites sk-lem-constructible-ext-continuity; continuity for generated complexes, clause 1 via generation. |
| `lemma-descent-finite-coefficient-field` | 3 | medium | Lean cites sk-thm-sfb-qlbar-two-colimit assertions (Hom colimit, object descent); old list had only helper defs. |
| `lemma-lattices-after-finite-stratification` | 2 | medium | Stratified lisse integral lattices (sk-lem-stratified-lattice); old node had no lean. |
| `lemma-integral-models` | 2 | medium | Old detail lean (clause 1) plus det-lem-integral-models-stacks (clause 2); clauses 3-4 not found as single theorems. |
| `proposition-inverting-ell-full-derived-categories` | 0 | — | Old sk-prop-sfb-rationalization-full had no lean; no Lean statement found. |
| `proposition-inverting-ell` | 2 | medium | Old sk-thm-sfb-rationalization-comparison: the equivalence and localization statements; helper defs dropped. |

### Proper base change

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `question-stalks-proper-direct-image` | 0 | — | Question; not a statement. |
| `remark-cohomology-modules-underlying-abelian` | 0 | — | Remark; nothing states exactly it. |
| `definition-underived-base-change-map` | 1 | high | Old def-weil-pbc-underived-exchange under sk-def-exchange. |
| `definition-derived-base-change-map` | 2 | high | Old sk-def-exchange / def-weil-pbc-derived-exchange; baseChange is the same map (baseChange_eq_derivedBaseChangeMapPlus). |
| `lemma-identity-pasting` | 3 | high | Old sk-lem-pbc-exchange-pasting lean list. |
| `definition-pro-etale-base-change-map` | 2 | medium | Pro-etale unit-square-counit base change maps (discrete-ring sheaves; condensed-ring module objects). |
| `lemma-naturality-pasting-comparison` | 1 | low | Only the etale comparison clause is formalized; no pro-etale identity/pasting equations found. |
| `theorem-comparison-over-henselian-pair-degree` | 3 | high | Old sk-thm-pbc-henselian-h0 lean list (module/abelian sheaves rather than sets). |
| `example-henselian-needed` | 0 | — | Example; not formalized. |
| `lemma-sections-geometric-fibre` | 1 | high | From old sk-prop-pbc-degree-zero; states stalk-to-fibre-sections bijection (abelian sheaves). |
| `proposition-proper-base-change-degree-zero` | 1 | high | Old sk-prop-pbc-degree-zero / lemma-weil-pbc-proper-underived-exchange. |
| `example-pbc-fails-integral` | 0 | — | Example; not formalized. |
| `definition-torsion-sheaves` | 4 | high | Old sk-def-pbc torsion part; characterizations give the equivalent forms. |
| `definition-torsion-pbc-property` | 1 | high | Old sk-def-pbc PBC predicate. |
| `definition-injective-acyclicity` | 1 | high | Old sk-def-ia. |
| `lemma-acyclic-resolutions` | 2 | high | Old sk-thm-acyclicity lean list. |
| `theorem-pbc-injective-acyclicity` | 1 | medium | Old sk-thm-iff: (i)<=>(iii); dropped one-direction helper. Clause (ii) not separately stated. |
| `remark-henselian-pairs-facts` | 3 | medium | Remark cites Gabber (i), finite-etale lifting (ii), (4.8); these Lean theorems (old detail nodes) state exactly them. |
| `theorem-cohomology-curves` | 1 | low | Only the structure packaging C1-C8 (def-weil-pbc-eight-curve-assertions); no general theorem proving it found; etale not pro-etale. |
| `lemma-extension-separably-closed-ground-field` | 1 | high | Old sk-cor-curve-invariance. |
| `remark-properness-needed-c7` | 0 | — | Remark/example; not formalized. |
| `remark-finiteness-small-etale-topoi` | 1 | low | Only fact (2), the embedding into finite pushforwards, is a Lean theorem (old lemma-weil-pbc-constructible-finite-pushforward). |
| `lemma-acyclicity-closed-fibre` | 1 | high | Old sk-lem-pbc-p1-injective-fibre. |
| `proposition-cohomology-p-1-over-henselian` | 1 | high | Old sk-prop-pbc-p1-henselian. |
| `proposition-proper-base-change-projective-line` | 2 | high | Old sk-thm-p1 lean list. |
| `lemma-finite-morphisms` | 4 | high | Old sk-lem-pbc-finite lean list. |
| `example-finite-direct-image-double-cover` | 0 | — | Example; not formalized. |
| `lemma-composition-cancellation` | 2 | high | Old sk-lem-pbc-composition-cancellation; kept PBC versions, dropped IA helpers. |
| `lemma-finite-cover-projective-space` | 2 | high | Old sk-lem-pbc-symmetric-product; PBC-for-P^n name moved to lemma-pbc-projective-space. |
| `lemma-pbc-projective-space` | 1 | high | Old lem-weil-pbc-reduction-projective-space: PBC(P^1) for all S implies PBC(P^n). |
| `proposition-proper-base-change-etale-site` | 2 | high | Old sk-thm-reduction; general-ring version plus the torsion-ring variant. |
| `theorem-proper-base-change-classical-pro` | 2 | medium | Old sk-thm-properbasechange; pro-etale version only for finite Lambda with etale origin, plus etale torsion version. |
| `corollary-cohomology-geometric-fibres` | 1 | medium | Old cor-weil-pbc-geometric-fiber-finite (under sk-cor-pbc-torsion-stalk); etale-site stalk formula. |
| `proposition-proper-direct-image-finite-coefficients` | 1 | high | Lean cites det-ctf-finite-proper-tor (sk-prop-ctf-finite-proper): Dctf with Tor amplitude [a,b+d]. |
| `definition-completed-inverse-image` | 2 | medium | def-weil-pbc-completed-pullback: Rlim of pulled-back reduction tower. |
| `definition-projection-formula-map` | 1 | high | Ambient pro-etale projection map, adjoint of monoidal iso and counit. |
| `proposition-proper-base-change-complete-integral` | 0 | — | Old sk-prop-pbc-complete had no lean; no single Lean theorem found (only completion infrastructure). |
| `lemma-completed-ordinary-base-change` | 0 | — | No Lean statement found. |
| `proposition-proper-direct-image-constructible-complexes` | 4 | medium | Old sk-thm-sfb-proper-base-change names plus finite and integral clause-(1)-(3) theorems. |

### Construction of $f^!$

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `definition-localizing-subcategory` | 3 | high | Old sk-def-localizing-closure list: generic closure plus finite and condensed-ring instances. |
| `theorem-exceptional-inverse-image` | 0 | — | Summary theorem (old sk-thm-existence, no lean); headline part 3 = Brown existence theorems, shared with theorem-existence-exceptional-inverse-image. [merge: existence theorems kept on theorem-existence-exceptional-inverse-image] |
| `example-compactness-finite-field` | 0 | — | Example; not formalized. |
| `lemma-limits-sections-support` | 0 | — | Old sk-lem-formal-closed-support-ii had no lean; no Lean statement of t-exactness/derived-limit commutation found. |
| `lemma-ext-bound-lattices` | 0 | — | Explicit lattice bound not formalized; Lean proves uniform Ext bound via residue-field reduction instead. |
| `lemma-uniform-ext-bound` | 3 | high | Docstrings cite sk-lem-uniform-constructible-ext: property def and its E, Qlbar instances. |
| `example-ext-bound-finite-field` | 0 | — | Example; not formalized. |
| `definition-ind-constructible-sheaves` | 1 | high | Abbrev ind of constructible module objects (docstring sk-prop-ind-heart). |
| `proposition-ind-constructible-sheaves` | 4 | high | Part 1: ind full faithfulness (det-ind-heart-full-faithfulness); part 2: closure properties, E and Qlbar instances. |
| `corollary-ind-heart-b` | 2 | medium | Docstrings cite sk-cor-ind-heart-ii; abstract property and its derivation from continuity plus uniform bound. |
| `corollary-ambient-ind-derived` | 1 | medium | Docstring det-ambient-ind-derived-sums: Dic localizing, contains Loc(Dbc); truncation stability not separately stated. |
| `lemma-reduction-finitely-many-degrees` | 0 | — | Window iso not stated; only proof steps DerivedCategory.eq_zero_of_isLE / eq_zero_of_isGE_of_isLE (lower tail vanishing). |
| `theorem-compactness-rational-coefficients` | 2 | high | Docstrings cite sk-thm-constructible-compactness: Dbc compact in Loc(Dbc) for E and Qlbar. |
| `proposition-compactness-finite-coefficients` | 1 | medium | Docstring sk-prop-ctf-finite-compact; generation is in the Brown-hypotheses theorem; Loc^c = Dctf not stated. |
| `proposition-comparison-etale-derived-category` | 0 | — | Old sk-prop-ctf-finite-comparison had no lean; Lean uses etale-origin complexes instead of this equivalence. |
| `corollary-proper-direct-image-finite-coefficients-localizing` | 1 | low | Docstring cites det-ctf-finite-proper-localizing: proper Rp_* preserves sums of etale-origin complexes (contains Loc(Dctf)). |
| `lemma-uniform-bound-proper-direct-image` | 2 | medium | Docstrings cite sk-lem-proper-heart-bound: finite amplitude and sums on ind-constructible heart, E and Qlbar. |
| `lemma-proper-direct-image-unbounded-complexes` | 1 | low | Only part 3 in a weaker form (sums on Loc(Dbc), docstring sk-lem-proper-unbounded-window-ii); parts 1-2 not stated. |
| `lemma-structure-integral-constructible-complexes` | 1 | low | Only part (1) heart: Cons(X,O_E) closed under kernels, cokernels, extensions; local structure and duals not found. |
| `lemma-inverse-image-tensor-product` | 2 | low | Tensor and closed direct image preservation; pullback/j_! covered by general nodes; completed pullback agreement not found. |
| `proposition-compactness-proper-direct-image` | 2 | high | Docstrings cite sk-prop-int-compactness: compactness and Rp_* sums on Loc(Dbc(O_E)). |
| `proposition-proper-direct-image-extension-zero` | 5 | medium | Docstrings sk-prop-proper-image-localizing / det-proper-image-localizing-open; finite-A proper part not separately stated. |
| `lemma-checking-isomorphisms-constructible-complexes` | 1 | high | Docstring sk-lem-sf-determination; replaces old auxiliary five-lemma isIso3_of_isIso12. |
| `proposition-proper-base-change-localizing-categories` | 3 | medium | Docstrings sk-prop-proper-base-change-unbounded (E, Qlbar) and det-thm-sf-pf-adic-base-change (O_E); finite A absent. |
| `remark-compactifications` | 0 | — | Remark; Nagata statement belongs to the Nagata theorem node. |
| `proposition-construction-independence-rf-shriek` | 7 | medium | Old sk-prop-sf-comp-coherence names (independence, cocycle on etale D+) plus det-sf-comp-coherence-single Loc statements per coefficient. |
| `example-cuspidal-compactification` | 0 | — | Example; not formalized. |
| `proposition-composition-base-change-rf-shriek` | 4 | medium | Old sk-thm-sf-comp-composition name plus composition iso/associativity and base change (det-sf-comp-composition-base-change); etale finite level. |
| `proposition-forgetting-supports-composition` | 3 | low | Old node had no lean; etale forget-supports map, iso for proper f, compatibility of compositions for proper maps. |
| `lemma-hypotheses-brown-representability` | 4 | high | Docstrings cite sk-lem-brown-hypotheses for finite A, E, O_E, Qlbar. |
| `theorem-existence-exceptional-inverse-image` | 6 | high | Docstrings cite sk-prop-sf-existence; replaces old rightDerivedUpperShriekAdjunction (D+ etale-origin variant). |
| `proposition-composition-open-restriction-compactifications-f` | 4 | medium | Old sk-lem-sf-mate name (part 1) plus pro-etale composition mate, j^! = j^* (part 2), f^! = j^* p^! (part 4); finite coefficients. |

### Constructibility of $f^!$

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `remark-results-from-etale-theory` | 0 | — | Remark collecting classical inputs; no single statement. |
| `lemma-cycle-class-cartier-divisor` | 2 | high | Docstrings cite sk-lem-geo-cartier: canonical Cartier class with Chern equation, coefficient and base change compatibility. |
| `lemma-cohomology-projective-line-trace` | 3 | high | Docstrings cite sk-lem-geo-p1-cohomology: decomposition (6.2), trace (6.3), Noetherian base change. |
| `example-compact-supports-running-example` | 0 | — | Example; not formalized. |
| `lemma-class-diagonal-projective-line` | 2 | medium | Docstrings cite lem-amb-p1-diagonal-integrals: s_1 = s_2 = id; relative Cartier divisor part not stated. |
| `proposition-adjunction-projective-line` | 2 | medium | Docstrings cite sk-prop-geo-p1-adjunction / det-sp-p1-adjunction: adjunction and base change of counit (etale site). |
| `lemma-affine-space-etale-localization` | 3 | high | Old sk-lem-geo-affine-local detail names (parts 1, 2) plus affineSpaceAdjunction_baseChange (docstring clause 1). |
| `proposition-exceptional-inverse-image-smooth-morphism` | 5 | high | Old sk-prop-cohsm list plus canonical-map isomorphisms for parts 2 and 3. |
| `lemma-smooth-morphisms-locally-constant-sheaves` | 1 | high | Old detail lem-asd-smooth-generic-direct-image states this lemma. |
| `example-shrinking-base-smooth` | 0 | — | Example; not formalized. |
| `lemma-detection-proper-direct-image` | 2 | high | Old sk-lem-geo-finite-boundary details: parts (1) and (2). |
| `lemma-coordinate-projections` | 2 | high | Old sk-lem-geo-coordinates details: parts (1) and (2). |
| `lemma-extension-across-finite-subset` | 1 | medium | Finite-boundary step of Deligne induction (abstract form, takes the smooth direct-image input as hypothesis). |
| `lemma-universal-homeomorphism-base` | 1 | high | Old detail lem-fin-radicial-exchange-descent. |
| `lemma-generic-smooth-open` | 1 | high | Old detail lem-fin-generic-radicial-smoothing. |
| `theorem-generic-constructibility-base-change-rj` | 1 | high | Old detail thm-fin-deligne-generic-open. |
| `corollary-open-direct-image-over-field` | 3 | high | Old detail cor-fin-deligne-open-finite-coefficients plus base change (det-geo-open-finiteness-base-change), etale and pro-etale. |
| `proposition-open-direct-image-preserves-finite` | 3 | high | Old sk-cor-sf-direct-image-ctf list plus the precise [a,b+d], d >= cd(j) open-immersion bound. |
| `theorem-f-shriek-finite-coefficients` | 3 | medium | Old list kept exists_shift; dropped closed-immersion step; f^! preserves Dctf and restricted adjunction (transported etale f^!, not Brown adjoint). |
| `proposition-direct-image-along-open-immersion` | 3 | high | Docstrings cite sk-prop-open-coefficients, one per coefficient ring. |
| `proposition-ell-adic-cycle-class-diagonal` | 0 | — | Only fragmentary tower pieces (exists_diagonalTowerSystem, diagonal_limit_endpoints); no assembled statement found. |
| `proposition-projection-formula-rational-coefficients` | 4 | high | Docstrings cite sk-thm-sf-pf-field details: tensor closure and projection formula on Loc, E and Qlbar. |
| `proposition-projective-line-rational-coefficients` | 0 | — | Old sk-prop-p1-adjunction-rational had no lean; only RationalP1 transport fragments found. |
| `example-closed-support` | 0 | — | Example; not formalized. |
| `lemma-projection-formula-integral-coefficients` | 1 | high | Docstring det-thm-sf-pf-adic-projection: tensor closure and projection formula on Loc(Dbc(O_E)). |
| `theorem-f-shriek-ell-adic-coefficients` | 3 | high | Docstrings cite sk-thm-restriction / sk-thm-int-restriction: Brown f^! maps Dbc into Dbc, per coefficient ring. |

### The six operations on $\Dctf$

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `proposition-six-operations-dctf` | 3 | medium | Old det-rem-sf-matrix (finite A case of sk-thm-sf-ctf-stability); other coefficient rings not stated in Lean. |
| `example-internal-hom-affine-line` | 0 | — | Example; nothing states it. |
| `example-derived-reduction-point` | 0 | — | Example; nothing states it. |
| `definition-change-of-coefficients-maps` | 4 | high | Old sk-prop-scalar-six details: (Pull),(Shriek open),(Push),(Shriek) maps of ChangeOfCoefficients.lean; tensor/Hom maps not formalized there. |
| `lemma-extension-scalars-preserves-dctf` | 2 | medium | Old node empty; finite A->B preserves Dctf, flat extension preserves Dbc (E->F, ->Qbar). |
| `lemma-change-coefficients-direct-image` | 4 | medium | (Push) iso for O_E->E, E->F, E->Qbar, O_E->O_E/l^n; finite A->B general case not found. |
| `lemma-change-coefficients-compact-support` | 2 | medium | Finite-ring comparison iso for any compactification; O_E->E (Shriek) iso on Dbc. |
| `lemma-change-coefficients-exceptional-inverse-image` | 1 | medium | Exchange for f^! is iso, O_E->E case only (IntegralUpperShriekCompatibility). |
| `lemma-change-coefficients-internal-hom` | 1 | low | Only O_E->O_E/l^n case of RHom comparison found. |
| `proposition-six-operations-change-coefficients` | 2 | low | Old sketch empty; compatibility of (Pull) with (gf)^* and of (Push) with composite coefficient maps. |
| `proposition-dctf-x-qbar-2-colimit` | 5 | high | Old sk-prop-qlbar-two-colimit lean list. |
| `proposition-isomorphisms-reduce-finite-coefficients` | 1 | low | Old sketch empty; only integral step (reduction mod l^n detects isos) is formalized. |

### Smooth base change

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `theorem-smooth-base-change-classical-torsion` | 1 | high | Old sk-thm-smooth-base-change. |
| `lemma-degree-zero-calculation` | 2 | high | Old sk-prop-deg0 and detail sbc-lem-degree-zero-flat-base-change; dropped smooth special case. |
| `lemma-injectivity-base-change-map-degree` | 3 | high | Old sk-prop-injectivity lean list. |
| `lemma-reduction-field` | 2 | high | Old sk-lem-failure-field lean list. |
| `lemma-integral-changes-source-base` | 2 | high | Main theorems of old details sbc-lem-bc-integral-surjective / -base; helpers dropped. |
| `lemma-reduction-curve-over-normal-base` | 2 | high | Old sk-lem-universal-datum lean list. |
| `example-reduction-end-affine-line` | 0 | — | Example; nothing states it. |
| `proposition-base-change-larger-algebraically-closed` | 1 | high | Old sk-thm-vanishing lean list. |
| `theorem-smooth-base-change-classical-torsion-2` | 2 | medium | Pro-etale D+ classical torsion version; etale D+ version from old detail of sk-thm-sbc-derived. |
| `lemma-change-coefficients` | 2 | medium | CoefficientChangeCube: base change map commutes with flat coefficient change (formal part of sk-lem-sbc-exchange-compatibility). |
| `theorem-smooth-base-change-all-admissible` | 4 | medium | Old sketch empty; finite, O_E and Qbar cases (last docstring cites sk-thm-sbc-coefficients). |
| `remark-smooth-base-change-proper-base` | 0 | — | Remark. |
| `lemma-base-change-along-product-projection` | 1 | low | Old sketch empty; lem-kun-0f1n base change of Rg_* along product projection over a field (tensored form). |
| `definition-kunneth-map` | 2 | medium | Kunneth map for f1 x f2 (Qbar, ProperKunneth) and identity-factor map (8.4) on etale site. |
| `lemma-kunneth-finite-direct-image` | 0 | — | Proof step not formalized (Lean proves Kunneth via Stacks 0F1N instead). |
| `lemma-kunneth-field-coefficients` | 0 | — | Proof step not formalized. |
| `lemma-kunneth-one-identity-factor` | 2 | high | Old sk-lem-sf-kunneth-star; Lean statement is exactly Rf_*M box Q = R(f x id)_*(M box Q). |
| `proposition-ordinary-external-kunneth` | 2 | low | General f1 x f2 finite-A case absent; point-target case and proper Qbar case only. |

### Smooth purity

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `definition-exceptional-base-change-map` | 2 | high | Docstrings define exactly the adjoint of inverse compact-support base change composed with counit. |
| `definition-trace-map-affine-line` | 0 | — | Projective-line-based affine trace not found as a def. |
| `theorem-smooth-purity-all-admissible-coefficients` | 2 | low | Old sketch empty; Qbar orientation gamma_f (docstring cites sk-thm-purity-transport) at the unit only. |
| `definition-relative-dualizing-complex` | 1 | medium | omega_f = Rf^! Lambda_Y on etale site, finite coefficients. |
| `definition-representing-objects` | 0 | — | No formalization of representing pairs found. |
| `proposition-purity-vector-bundles` | 2 | medium | Old sk-prop-an (zero-section form) plus clause (ii) affine-space purity; only trivial bundles. |
| `definition-deformation-normal-bundle` | 2 | medium | Deformation space (extended Rees algebra model) and its data structure. |
| `example-deformation-origin-line` | 0 | — | Example. |
| `lemma-section-normal-bundle` | 1 | high | Old sk-thm-dnc lean list. |
| `lemma-naturality-under-base-change-etale` | 0 | — | Old sketch empty; no naturality statement for alpha found. |
| `proposition-relative-dualizing-complex` | 2 | high | Old sk-thm-smooth-purity name moved here; canonical iso omega_f = Lambda(d)[2d]. |
| `proposition-smooth-purity-finite-coefficients` | 2 | high | Old sk-thm-smooth-purity and detail def-pur-smooth-purity-map. |
| `proposition-sp-unique-adjoint` | 2 | low | Old sketch empty; abstract Mathlib uniqueness of right adjoints compatible with counits. |
| `definition-sp-scalar-extension` | 1 | medium | Extension of scalars of pro-etale module sheaves (derived via L(-)). |
| `lemma-sp-reduction` | 2 | medium | b(M) for finite A->B; c_{A,B} for f^! not found. |
| `proposition-sp-integral-towers` | 0 | — | Old sketch empty; no headline statement found. |
| `lemma-sp-tower-adjunction-foundation` | 0 | — | Old sketch empty; no headline statement found. |
| `proposition-sp-tower-geometric` | 0 | — | Old sketch empty; no headline statement found. |
| `proposition-sp-integral-adjunction` | 0 | — | Old sketch empty; no headline statement found. |
| `proposition-sp-rational` | 0 | — | Old sketch empty; no E-coefficient purity found. |
| `theorem-sp-qbar` | 2 | medium | Docstrings cite sk-thm-sp-qbar: f^!K = f^*K tensor omega_f and omega_f = Qbar(d)[2d]. |
| `proposition-compatibility-purity-base-change` | 4 | medium | Qbar orientation base change (cites sk-prop-sp-purity-bc), old finite coherence node, trace base change. |
| `proposition-compatibility-purity-composition` | 2 | low | Only composition with an open immersion is formalized (Qbar). |
| `definition-trace-map` | 2 | high | Old def-pur-smooth-trace; Qbar smoothTrace docstring cites sk-def-sp-trace. |
| `remark-trace-map-special-cases` | 0 | — | Remark. |
| `proposition-transitivity-trace-map` | 1 | high | Old thm-pur-trace-normalization-transitivity (composition part). |
| `proposition-compatibility-purity-change-coefficients` | 2 | medium | Old thm-pur-finite-reduction-of-purity: purity iso and trace commute with coefficient change functor. |
| `corollary-dualizing-complex-smooth-scheme` | 2 | medium | Qbar Rf^!Qbar=Qbar(d)[2d]; old cor-pur-finite-stage-smooth-dualizing-complex for finite. |

### Verdier and Poincaré duality

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `lemma-perfect-complexes-geometric-point` | 9 | medium | old sk-lem-finite minus helpers; added stalk/compact perfectness (finite coeff) and biduality at the point |
| `definition-verdier-dual-evaluation` | 6 | medium | old sk-def-ops (dropped derivedDual/cohomology); added double-dual morphism δ_K (pro-étale Q̄ℓ and étale finite) |
| `lemma-internal-adjunction-two-exchange-formulas` | 5 | medium | (10.2) tensor-Hom exchange, (10.3)/(10.4) natural isos, proper δ compatibility; old sketch had no lean |
| `example-biduality-punctured-line` | 0 | — | example; not formalized |
| `lemma-verdier-duality-preserves-constructibility` | 1 | medium | old sketch empty; étale finite-coefficient preservation of Dctf |
| `lemma-restriction-geometric-generic-fibre` | 3 | medium | old lem-weil-geometric-generic-exchange: three comparisons (direct image only for open immersions) |
| `lemma-double-dual-geometric-generic-fibre` | 2 | medium | old lem-weil-geometric-generic-duality main statements; helpers dropped |
| `theorem-verdier-biduality` | 4 | high | old lem-sf-verdier-biduality-equivalence (finite) plus pro-étale Q̄ℓ / O_E constructible biduality |
| `corollary-verdier-exchange-formulas` | 4 | medium | old sk-thm-sf-verdier-exchange names plus f^!D≅Df^* and i^*D≅Di^!; D Rf_* ≅ Rf_! D not found |
| `theorem-global-verdier-duality` | 3 | medium | old sk-thm-sf-global-duality; (10.5) only, (10.6) not found |
| `definition-perfect-pairing` | 2 | high | docstring cites sk-def-pairing: adjoint Y→[X,1] iso |
| `theorem-poincare-duality` | 5 | medium | old sk-thm-sf-identification + derived/proper Poincaré details; coefficient-change clause not covered |
| `corollary-degreewise-duality-over-fields` | 5 | medium | finite-field degreewise perfectness (étale) and Q̄ℓ lisse/constant Weil-sheaf forms; old details of sk-thm-derived-duality |
| `remark-duality-cohomology-groups-over-oe` | 0 | — | remark; not formalized as such |
| `theorem-trace-isomorphism-top-degree` | 4 | medium | finite-coeff étale trace iso and Q̄ℓ Weil-sheaf form (old thm-pod-trace-isomorphism), vanishing outside [0,2d] |
| `lemma-class-of-point` | 1 | medium | trace of point class is 1 for normalized orientation (finite self-injective coefficients) |
| `corollary-cup-product-pairing` | 2 | medium | Q̄ℓ constant coefficients over finite field: perfect cup pairing with (-1)^i symmetry; old sk-cor-trace name |
| `definition-weil-structure` | 5 | medium | old def-trf-strict-weil-complex; étale and Q̄ℓ Weil-object variants |
| `definition-frobenius-operator` | 3 | medium | compactly supported Frobenius RΓ_c(φ)∘pullback; old blueprint had none |
| `proposition-purity-trace-commute-frobenius` | 4 | medium | thm-pur-weil-equivariance-of-purity-and-trace (smooth f, hypothesis hcoh for trace) |
| `theorem-poincare-duality-frobenius` | 7 | high | old sk-thm-frobenius list plus its untwisted-similitude and reciprocal-eigenvalue details |
| `example-duality-multiplicative-group` | 0 | — | example |
| `example-running-example-duality` | 0 | — | example |

### The Lefschetz–Verdier formula

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `definition-categorical-trace` | 1 | high | old sk-d-trace |
| `proposition-properties-trace` | 6 | high | old sk-p-trace + prop-trf-trace-formal-laws; additivity via short exact sequences of complexes |
| `remark-coherent-additivity` | 0 | — | remark |
| `example-trace-not-determined-cohomology` | 0 | — | example |
| `definition-correspondence` | 4 | high | Q̄ℓ endocorrespondence + fixed locus (used downstream) and finite-coefficient étale version; not in old facts |
| `proposition-exceptional-external-kunneth` | 1 | medium | finite coefficients, existence of iso f1^!⊠f2^! ≅ (f1×f2)^!(⊠) (blueprint prop-trf-exceptional-kunneth) |
| `lemma-external-duality-trace-morphism` | 4 | medium | Künneth–Verdier iso P_X≅Hom(p2^*K,p1^!K) and H_c(K)≅c^!P_X; old sk-thm-sf-kunneth-verdier name |
| `definition-trace-morphism` | 2 | high | traceMap docstring: 𝓗_c(K)≅c^!(K⊠DK)→c^!RΔ_*ω→Rι_*ω_Fix |
| `definition-trace-class-local-terms` | 4 | high | traceClass, integral (def-trf-integration), localTerm (def-trf-local-term) |
| `lemma-local-terms-point` | 1 | high | ∫_s Tr(v) = tr(v) over the base point (prop-trf-pairing-point-normalization) |
| `definition-action-correspondence` | 1 | high | global operator T_c(u) on RΓ_c, same composite |
| `definition-pushforward-correspondence` | 7 | high | pushforward u'=δ∘Rg_*u∘γ, induced h on fixed loci, h_* on Borel–Moore sections |
| `theorem-proper-pushforward-lefschetz-verdier` | 3 | high | Varshavsky 1.2.5 pushforward compatibility and Lefschetz–Verdier formula / local-term sum |
| `example-correspondence-on-point` | 0 | — | example |
| `lemma-graded-pieces-filtered-operations` | 0 | — | filtered derived category not formalized |
| `lemma-filtered-trace-morphism` | 0 | — | filtered derived category not formalized |
| `lemma-lift-correspondence-invariant-decomposition` | 1 | low | only Z = rational point, no filtered lift: open piece u_U compatible with counit |
| `lemma-closed-piece-pushforward` | 1 | low | only Z = rational point: closed piece is pushforward of restricted u_Z, compatible with unit |
| `proposition-additivity-trace-classes` | 2 | medium | (1) triangle additivity under Hom-vanishing hypotheses; (2) only for Z a rational point |

### The trace formula

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `question-lefschetz-formula-frobenius` | 0 | — | Motivating question (old sk-q-trace-formula had no lean). |
| `definition-frobenius-correspondences-their-operators` | 6 | medium | sk-d-weil: Phi_X, iterates psi_m, operator T_{c_m}=RGamma_c(psi_m)∘Phi^#, stalk maps; old weilDatumIterate/stalkFrobenius kept (finite-coeff iterates). |
| `lemma-scheme-frobenius-geometric-frobenius` | 3 | low | sk-lem-tf-frobenius-convention had none; kappa iso (etale) plus psi_m=phi_m and T_{c_m}=Frob^m in model-Frobenius setting. |
| `remark-locality-warning` | 0 | — | Remark (old sk-rem-tf-locality-warning, no lean). |
| `lemma-frobenius-fixed-scheme` | 6 | high | Docstrings cite sk-lem-tf-fixed-points / thm-trf-frobenius-fixed-points: Fix ≅ ∐ s, finite, reduced, proper. |
| `remark-outline-local-computation` | 0 | — | Outline remark; no statement. |
| `lemma-local-term-restriction-map` | 3 | medium | sk-lem-tf-curve-supported-pairing: local term = integral of ev∘rho∘[psi]; general correspondence form. |
| `lemma-punctured-surface-punctured-curve` | 1 | high | det-tf-transverse-corner-constant: restriction RΓ(S−Y_S,F_ℓ)→RΓ(X_S−z,F_ℓ) bijective in all degrees. |
| `lemma-cohomology-near-two-transverse-divisors` | 2 | high | sk-lem-tf-transverse-boundary: M_z=0, local constancy on D2−z, restriction to M_w zero. |
| `lemma-restriction-punctured-curve` | 1 | high | sk-lem-tf-punctured-restriction, stated exactly. |
| `lemma-vanishing-restrictions-after-blowing-up` | 2 | high | sk-lem-tf-blowup-restriction (old name kept) plus the closed-subscheme form. |
| `lemma-covers-degree-prime-to-ell` | 3 | low | det-tf-restriction-zero-covers: Lean uses one global cover datum (prime-to-ℓ degree, ℓ-group monodromy); different route, no degree adjustment. |
| `lemma-tangent-cones-on-cover` | 2 | medium | det-tf-restriction-zero-covers (ii)-(iii): tangent cones on T' meet at origin, H' regular. |
| `lemma-descent-vanishing-finite-etale` | 3 | medium | det-tf-restriction-zero-trace-descent: pullback followed by trace is multiplication by d; vanishing descends. |
| `lemma-vanishing-local-term-zero-stalk` | 3 | high | sk-lem-tf-curve-restriction-zero: rho=0 (classical model and Qlbar form), hence LT_y(psi)=0. |
| `proposition-frobenius-local-term-curve` | 1 | high | sk-p-frob / thm-trf-frobenius-local-term: LT_y(v)=tr(v_y) on smooth curve, v arbitrary. |
| `example-frobenius-projective-line` | 0 | — | Example; nothing formalizes it. |
| `lemma-comparison-via-relative-frobenius` | 9 | high | sk-i-relative-frob parts (1)-(4); old relativeFrobenius finiteness names kept. |
| `lemma-additivity-open-subscheme-complement` | 3 | high | sk-i-global-additivity: trace of RΓ_c(ψ)∘Φ^# additive over U and Z; induced piece correspondences. |
| `theorem-trace-formula-frobenius-correspondence` | 2 | high | sk-thm-tf-coefficient-morphism-formula; Lean coefficients are Qlbar, not finite A. |
| `proposition-integral-trace-formula` | 0 | — | sk-prop-tf-transport-integral: no Lean; O_E-coefficient operators T_{c_m} not defined (RationalModel.lean notes). |
| `lemma-integral-models-rational-frobenius-correspondences` | 3 | high | sk-lem-tf-rational-model; operator identity for T_{c_m} not formalized, stalk identity is. |
| `remark-integral-frobenius-correspondences-not-invertible` | 0 | — | Remark (old sk-rem-tf-weil-lattices, no lean). |
| `theorem-grothendieck-lefschetz-trace-formula` | 4 | high | Old det-thm-tf-uniform-formula-weil names (Qlbar form 12.4) plus new weilTraceFormula (Weil objects). |
| `definition-trace-function` | 3 | high | def-fd-trace-function: t_K(x)=alternating trace of Frob on stalk; complex, sheaf and Weil-object versions. |
| `corollary-trace-functions-direct-image-compact` | 1 | high | Exactly t_{Rf_!K}(y)=Σ_{x↦y} t_K(x) (twisted-Frobenius generalisation). |
| `example-trace-function-squaring` | 0 | — | Example; not formalized. |
| `proposition-function-sheaf-dictionary` | 3 | medium | Parts (1),(2) (lisse tensor only),(4) via triangles; (3),(5) are the corollary/theorem names, not repeated. |
| `lemma-logarithm-determinant` | 3 | high | sk-prop-logdet: vector-space identity; alternating product covers the perfect-complex version. |
| `theorem-trace-formula-euler-product` | 1 | high | thm-trf-l-function-euler-product: L(X0,K,T)=∏ det(...)^{(-1)^{i+1}} coefficientwise. |
| `corollary-point-counting-zeta-function` | 4 | medium | cor-trf-point-counting; Euler product over closed points; Z∈Q(T) (Dwork). Cohomological det product for constant sheaf not separately named. |
| `example-running-example-trace-formula` | 0 | — | Example; not formalized. |
| `corollary-functional-equation` | 2 | medium | Old sk-cor-tf-functional-equation names (minus helper even_finrank_cohomology_middle) plus weil_functional_equation for Z(1/q^dT). [merge: weil_functional_equation kept on theorem-weil-conjectures-smooth-proper-schemes] |
| `example-functional-equation-projective-line` | 0 | — | Example; not formalized. |
| `remark-duality-and-weights` | 0 | — | Remark. |

### Weights

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `definition-weights` | 6 | medium | sk-d-real-weights: sheaf-level defs preferred over WeilGroup curve-rep defs; no separate pure-complex predicate found. |
| `lemma-weil-sheaves-point-mixed` | 1 | medium | Weil sheaves on quasi-finite k0-schemes are mixed (Qlbar case; E-part not formalized). |
| `lemma-bounding-weights-mixed-sheaf` | 2 | high | sk-lem-wgen-punctual-cutoff (both directions). |
| `example-kummer-extension` | 0 | — | Example; not formalized. |
| `lemma-filtrations-spectra` | 5 | high | sk-p-linear-filtration and p-linear-spectra (filtration product, dual, wedge, tensor). |
| `proposition-weights-under-usual-operations` | 15 | medium | sk-r-real-linear parts at sheaf level; mixed tensor/dual parts not found. |
| `lemma-geometric-coverings-normal-scheme` | 0 | — | sk-lem-wrp-normal-geometric-cover: no Lean found (old had none). |
| `lemma-global-lattice-normal-scheme` | 2 | low | Lattice of a lisse sheaf (cocycle form) on regular schemes; tex is normal schemes. |
| `proposition-lattices-representations-normal-scheme` | 2 | medium | sk-p-real-integral: lisse Qlbar-sheaves ≃ continuous reps on connected normal (regular) scheme. |
| `theorem-weights-rf-shriek` | 1 | high | sk-cor-dl-general-complex: Rf_! D_{≤w} ⊂ D_{≤w}. |

### Purity of real sheaves

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `lemma-proper-smooth-model` | 2 | high | sk-i-real-compactification plus detail giving projectivity; étale boundary not stated separately. |
| `proposition-kummer-duality-integral-tate-module` | 2 | medium | sk-d-real-jacobian datum (J[l^n]≃Pic[l^n]) plus finite-level dual-Tate pairing; transpose-matrix clause not formalized. |
| `proposition-no-fixed-class-degree-one` | 1 | high | sk-prop-wrp-h1-no-fixed; proper case and residue steps are proof helpers. |
| `lemma-invariant-additive-characters` | 1 | high | sk-lem-wrp-additive; Z_l-valued form of the statement. |
| `theorem-rank-one-sheaves-have-finite` | 2 | high | sk-p-real-rankone sheaf form plus character form from detail thm-wf-rank-one-finite-geometric-image-curve. |
| `corollary-rank-one-weights` | 3 | high | sk-cor-wrp-rankone-pure plus weight formula and independence of s (detail cor-wf-rank-one-punctual-purity-curve). |
| `definition-determinant-weight` | 3 | high | def-wf-determinantal-weight, HasDetWeight (old sketch), multiset for DW(V). |
| `corollary-determinant-weights` | 4 | medium | Details of sk-d-real-detweights; first two (Purity.lean) state purity/finite geometric det directly. |
| `remark-determinant-weight-pure-constituents` | 0 | — | Old remark had no lean; no theorem found stating the rank-weighted average. |
| `definition-weil-representation` | 1 | medium | IsLisse = continuity on geometric part; also listed on old sk-d-real-weil (possible overlap). |
| `lemma-restriction-normal-subgroup` | 1 | high | sk-i-restriction. |
| `lemma-tensor-exterior-powers-filtered-representations` | 6 | medium | Detail nodes of sk-r-linear-library; dropped Jordan–Hölder/Schur helpers. |
| `definition-monodromy-groups` | 2 | medium | From old d-monodromy detail (Zariski closures as vanishing ideals). |
| `lemma-normality-geometric-monodromy` | 5 | high | sk-lem-walg-normal-commutator; dropped generic GL-group helpers. |
| `lemma-identity-component` | 4 | high | sk-p-product / p-product; Lie and semisimplicity names dropped as proof steps. |
| `definition-tensor-construction` | 0 | — | No Lean definition of tensor construction found. |
| `proposition-central-element-arithmetic-monodromy-group` | 2 | medium | sk-p-central; .map transports central pair to polynomial (tensor) constructions. |
| `lemma-determinant-weight-from-central-scalar` | 2 | high | sk-p-readout and its detail. |
| `proposition-determinant-weights-tensor-operations` | 4 | high | sk-prop-walg-determinant-weights parts (1),(2); dual part (3) not found. |
| `lemma-degree-zero-top-cohomology` | 5 | medium | Detail nodes of sk-lem-wrp-hc2 plus vanishing above 2 for lisse; H^2_c identification only for affine curves. |
| `definition-real-sheaves` | 2 | high | Old sketch had WeilGroup.IsReal; WeilSheaf.IsReal is the sheaf-level definition. |
| `lemma-positivity-euler-factors` | 2 | high | lem-rp-even-tensor-positivity part (ii); sheaf and representation forms. |
| `example-even-tensor-powers` | 0 | — | Example. |
| `lemma-positivity-convergence` | 1 | high | lem-rp-positive-product-radius under sk-lem-wrp-positive-euler. |
| `proposition-bound-largest-determinant-weight` | 2 | high | sk-p-real-rankin and lem-rp-upper-bound (same statement, weight vs absolute value form). |
| `theorem-purity-real-sheaves-curves` | 2 | high | sk-p-real-purity plus sheaf-level form from thm-rp-real-lisse-purity-affine. |

### Pure sheaves on curves

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `definition-middle-extension` | 1 | high | Docstring cites def-wf-middle-extension: ordinary direct image j_*. |
| `lemma-boundary-stalk` | 3 | medium | Frobenius-equivariant stalk = inertia invariants (unconditional); lisse extension clause, Weil and torsion forms (old sketch). |
| `example-boundary-stalks-g-m` | 0 | — | Example. |
| `lemma-point-count-bound` | 1 | high | sk-lem-wrp-point-count; finite-scheme clause not separately formalized. |
| `proposition-weights-j-boundary-points` | 2 | high | sk-p-real-semi plus sheaf form from lem-wf-boundary-semicontinuity. |
| `corollary-unramified-boundary-point` | 3 | high | sk-cor-wrp-unramified-purity; sheaf versions of first clause and of 'pure on dense open ⇒ pure'. |
| `lemma-extreme-degrees-affine-curve` | 4 | high | sk-l-dl-a1-endpoints / lem-a1-middle-extension-endpoints. |
| `lemma-cohomological-range-curve` | 2 | medium | Weil-sheaf forms (dim ≤1, and old lem-zl-affine-curve-range affine case). |
| `proposition-twisting-weight-zero-adding-dual` | 4 | medium | Details of sk-prop-wrp-real-envelope plus existence of b and weight-zero purity; trace=2Re not separately stated. |
| `definition-growth-squared-traces` | 4 | high | def-wf-l2-norm under sk-def-wrp-l2-definition (S_n and nu for complexes and sheaves). |
| `lemma-radius-squared-traces` | 2 | high | lem-wf-l2-radius and the series definition def-wf-l2-series. |
| `lemma-bounds-squared-traces` | 5 | medium | Part (1) via lem-wf-l2-upper; parts (2),(3) only through energy-bound and constant-twist lemmas. |
| `lemma-growth-finite-corrections` | 1 | low | Gives nu(K) ≤ max(nu(L), a-1), the key inequality; equality conclusion not stated. |
| `theorem-weights-sums-squared-traces` | 1 | high | sk-thm-wrp-l2-dictionary; real-case step dropped as proof helper. |
| `corollary-sums-squared-traces-j-shriek` | 1 | medium | Old sk-lem-wft-l2-middle: nu(j_*M)=nu(M)=w, only on dense opens of A^1, no j_! clause. |

### The Fourier transform

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `lemma-artin-schreier-character-sheaf` | 6 | medium | Weil-sheaf L_psi with multiplicativity, dual, trace, purity (details of sk-lem-as-properties); trivialization at zero absent. |
| `example-gauss-sum-over-f-3` | 0 | — | Example. |
| `lemma-kunneth-formula-compact-supports` | 0 | — | Old sketch empty; no Weil-complex compact-support Künneth found. |
| `lemma-integral-linear-character` | 1 | low | Relative line-bundle vanishing (lambda≠0 case, old detail lem-fd-cohomology-affine-line-character); lambda=0 trace case not included. |
| `proposition-base-change-fourier-inversion` | 4 | medium | Found by search (line over k0 only): fibre/base change, linearity over base, stalk formula. |
| `proposition-fourier-inversion` | 3 | high | Found by search: both inversion formulas on the line (docstrings cite lem-fd-inversion). |
| `lemma-fourier-transform-constant-sheaf` | 2 | high | Found by search; docstrings cite lem-fd-first-formula. |
| `corollary-plancherel` | 3 | high | sk-cor-plancherel details (cor-fd-plancherel, l2 shift) plus rank-r version. |
| `definition-punctual-sheaf` | 0 | — | Lean uses support.Finite inline; no punctual predicate. |
| `lemma-largest-punctual-subsheaf` | 3 | low | Found by search: pieces on the affine line (kernel of unit punctual, no punctual maps into j_*M); maximality not stated. |
| `definition-perverse-sheaves-curve` | 4 | high | Definitions from thm-a1-curve-perverse-heart detail. |
| `lemma-perverse-sheaves-curve` | 4 | medium | sk-lem-wft-curve-heart detail; t-structure only via orthogonality, heart abelianness not formalized. |
| `lemma-perverse-weil-sheaves` | 0 | — | Lean notes the curve perverse heart carries no abelian structure; not formalized. |
| `lemma-simple-objects` | 3 | high | sk-lem-wft-curve-simples detail plus punctual simple criterion. |
| `example-extension-by-zero-not-simple` | 0 | — | Example. |
| `proposition-fourier-transform-perverse-heart` | 3 | high | sk-p-dl-a1-perverse and thm-a1-fourier-t-exact. |
| `proposition-fourier-transform-middle-extension` | 2 | high | sk-p-dl-a1-middle; IsNonexceptional encodes the hypothesis. |
| `lemma-unramified-at-infinity-no-linear-characters` | 2 | high | lem-a1-unramified-nonexceptional; plus ramification of L_psi(ax) at infinity. |

### Deligne's theorem for curves

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `lemma-fourier-transform-boundary-sequence` | 4 | high | Old sketch sk-p-dl-a1-correction (title-equal); structure plus existence, lisse and weight-bound parts. |
| `example-kummer-no-boundary` | 0 | — | Example; nothing states it. |
| `lemma-twisted-envelope` | 0 | — | Old sketch sk-lem-wrp-twisted-envelope had no lean; no general statement found (isReal_realifiedKernel is only a special instance). |
| `proposition-purity-lisse-part-fourier-transform` | 1 | high | Old sketch sk-p-dl-a1-some-weight; detail nodes are proof helpers. |
| `theorem-weight-fourier-transform` | 1 | high | Old sketch sk-p-dl-a1-fourier-weight; eq_add_one/Plancherel detail names are proof steps. |
| `corollary-h-1-c-stalk-fourier` | 2 | high | Old sketch sk-c-dl-a1-hc1 plus detail cor-fd-origin-stationary-phase (H^2_c=0 and H^1_c iso stalk at 0'). |
| `lemma-local-duality-point-c-u` | 1 | high | Old sketch sk-i-dl-a1-local. |
| `example-local-duality-origin` | 0 | — | Example; nothing states it. |
| `proposition-exactness-fixed-pure-weight` | 1 | high | Old sketch sk-p-dl-a1-exact. |
| `theorem-weight-bound-affine-line` | 1 | high | Old sketch sk-thm-dl-a1-upper; dropped H^0_c=0 / H^2_c purity names, not in this statement. |
| `lemma-weight-bound-constant-extension` | 1 | medium | Old detail lem-a1-weight-bound-constant-extension; Frobenius-module form, only the used direction. |
| `lemma-finite-extension-base-field-moving` | 0 | — | Lean avoids this step (finite map to P^1 instead); old lem-a1-unramified-at-infinity names state only consequent H^1_c bounds. |
| `lemma-finite-generically-etale-map-line` | 3 | medium | Details of old sk-lem-wft-finite-map: existence of C',pi; lisse/pure part; RGamma_c comparison. |
| `theorem-weight-bound-affine-curve` | 1 | high | Old sketch sk-thm-wft-affine-curve-upper. |
| `theorem-weight-bound-curve` | 2 | high | Old sketch sk-thm-wft-curve-middle-upper; second name is the 'in particular U=C' case. |

### Deligne's theorem in general

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `lemma-finite-quasi-finite-direct-images` | 6 | high | Old detail lem-zl-quasi-finite under sketch sk-l-dl-general-quasifinite: exactness, weight bounds, purity. |
| `lemma-detecting-irreducibility-finite-quotient` | 1 | high | Old sketch sk-lem-wgen-finite-witness. |
| `lemma-curve-preserving-finite-cover` | 1 | high | Old sketch sk-lem-wgen-bertini-cover. |
| `corollary-curve-preserving-geometric-irreducibility` | 1 | high | Old sketch sk-cor-wgen-bertini-irreducible. |
| `lemma-geometric-constituents-after-constant-extension` | 1 | medium | Old sketch sk-lem-wgen-geometric-constituents; stated for representations (Weil group, normal geometric subgroup). |
| `lemma-mixedness-descends-constant-extension` | 0 | — | No old lean; Lean proof of IsReal.isMixed avoids constant-extension descent; no matching statement found. |
| `lemma-mixedness-open-closed` | 1 | medium | No old sketch; weight-bounded form (IsMixed is exists w) from old detail lem-zl-morphism-open-closed-reduction. |
| `theorem-real-constructible-sheaves-are-mixed` | 1 | high | Old sketch sk-i-dl-general-real. |
| `theorem-pure-lisse-sheaves-over-relative` | 1 | high | Old detail thm-zl-relative-affine-curve-core states general h; sketch's _of_affineLine is only the complement case. |
| `lemma-weights-exact-sequence` | 1 | high | Old sketch sk-lem-wgen-triangle-weights had no lean; of_exact states it for an exact short complex. |
| `lemma-weight-bounds-partitions` | 2 | medium | Parts (1) source and (2) target open-closed; Lean states them per morphism (all K) rather than per sheaf. |
| `proposition-relative-affine-line` | 1 | high | Old sketch sk-prop-wgen-relative-line. |
| `example-leading-coefficient-stratification` | 0 | — | Example; nothing states it. |
| `lemma-relative-noether-normalization-over-stratification` | 1 | high | Old detail thm-zl-relative-noether states the partition form; sketch's dense version is the generic-step complement. |
| `theorem-direct-image-mixed-sheaf` | 1 | high | Old sketch sk-thm-dl-general-sheaf. |

### Proof of the Weil conjectures

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `theorem-purity-higher-direct-images-under` | 2 | high | Old sketch sk-prop-smooth-proper-purity / detail prop-zl-smooth-proper-relative-purity. |
| `corollary-purity-cohomology-smooth-proper-variety` | 2 | medium | Old sketch sk-input-weights; chose constant-sheaf purity statements (Lean assumes geometrically connected) over lisse/aux names. |
| `lemma-hankel-rank-rationality` | 3 | high | Old sketch sk-prop-criterion: (1)<->(3), (2)<->(3), descent. |
| `lemma-reduced-fractions-integer-coefficients` | 1 | high | Old sketch sk-lem-wweil-integer-rationality. |
| `definition-reciprocal-root` | 0 | — | No Lean definition of reciprocal root; Lean uses roots of P.reverse (Polynomial.ordinary_reciprocal_roots is a lemma). |
| `lemma-reciprocal-roots-zeta` | 2 | low | From old sk-thm-weil-final details: parity products N_l/D_l separation and A^(l)=N_l, B^(l)=D_l; Lean route differs. |
| `theorem-weil-conjectures-smooth-proper-schemes` | 6 | high | Old sketch sk-thm-weil-final; parts (1)-(4) via integral factors, RH, Betti, functional equation. |
| `example-zeta-projective-space-elliptic-curve` | 0 | — | Example; nothing states it. |
| `example-running-example-purity` | 0 | — | Example; old sk-ex-ex-run-end had no lean. |
| `corollary-point-count-estimates` | 2 | high | Old sketch sk-cor-hasse; general bound and curve case. Dropped abstract-form complement name. |

### Nagata compactification and Chow's lemma

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `definition-compactification-refinement` | 6 | partial (reviewed) | Refinement has hj'=j and S-morphism; IsStrict is h^{-1}(X)=X; iff_app_injective is the 'i.e.' injectivity (for qc f). Not in Lean: Quasi-compactness of j is not a field of Compactification; it holds iff f is quasi-compact. |
| `theorem-nagata-s-compactification-theorem` | 1 | full (reviewed) | Finite type = LocallyOfFiniteType + QuasiCompact; base CompactSpace + QuasiSeparatedSpace. |
| `lemma-schematic-closure-uniqueness` | 4 | full (reviewed) | Mathlib image is a closed subscheme by construction; anonymous Mathlib instance gives U open in image. Lean needs no quasi-separatedness of T. |
| `lemma-uniqueness-maps-dense-open` | 1 | full (reviewed) | Primed version is literally the S-scheme form; the dense open is any scheme-theoretically dominant morphism. |
| `lemma-passing-schematic-closure` | 4 | partial (reviewed) | Pushforward comparison j_!≅i_*j_{Z,!} and Rp_*j_!≅R(pi)_*j_{Z,!} for E and Q̄_ℓ, with i the proper refinement Z→X̄. Not in Lean: Only bounded constructible complexes of E- or Q̄_ℓ-sheaves over a field k, not arbitrary Λ and unbounded K; stated for any proper strict refinement h, not specifically the schematic closure. |
| `remark-non-noetherian-compactifications` | 2 | partial (reviewed) | Lean states only the last sentence: dense refinements exist for any compactification of a quasi-compact morphism. Not in Lean: The scope remarks (same proof when complement is quasi-compact; failure of exactness otherwise) are not stated. |
| `proposition-dense-compactifications-form-cofiltered-category` | 3 | full (reviewed) | Common dense refinement holds for any nonempty finite family of compactifications of qc f; refinement_morphisms gives proper, h^{-1}(X)=X, unique. |
| `remark-base-change-compactification` | 3 | partial (reviewed) | Closure of X×S' being dense is denseRefinement (given to remark-non-noetherian-compactifications). Not in Lean: Agreement of the base-changed direct image with the schematic-closure one, and comparisons on common refinements, are not stated as such. |
| `definition-admissible-blow-up` | 3 | full (reviewed) | Blow-up glued from affine Rees-algebra charts; IsAdmissible has finite-type ideal and center disjoint from U. Lean drops the qcqs hypotheses. |
| `lemma-making-open-schematically-dense` | 2 | full (reviewed) | Cartier boundary J with support = complement of preimage of U; complement of an invertible ideal's support is dense, so the preimage is dense. |
| `example-blow-up-embedded-point` | 0 | none (reviewed) | Example. Not in Lean: Lean has no computation of this example. |
| `definition-strict-transform` | 3 | full (reviewed) | Lean defines it as the scheme-theoretic image of the part over the complement of the centre, i.e. ideal of sections supported on the preimage of E. |
| `lemma-products-composites-u-admissible-blow` | 4 | full (reviewed) | Common blow-up stated for two centres (product ideal dominates each); finite families by induction. |
| `definition-quasi-domination` | 1 | full (reviewed) | Fields: dense open U, S-map hom, closed graph in Y ×_S X. |
| `proposition-relative-form-zariski-s-main` | 2 | full (reviewed) | Factorization and quasi-affineness, same hypotheses. |
| `theorem-extension-partial-section` | 1 | full (reviewed) | Lean also assumes Y qcqs, which follows from p qc and separated over qcqs T. |
| `corollary-extension-proper-target` | 1 | full (reviewed) | Same statement. |
| `theorem-elimination-indeterminacy` | 1 | partial (reviewed) | Density follows for the witness eliminationBlowup via coe_support_eliminationCentre and isSchemeTheoreticallyDominant_blowupMap_preimage_compl_support; not packaged. Not in Lean: Schematic density of the preimage of U in T' is not stated by the existence theorem. |
| `lemma-extending-graph-from-compactification` | 2 | full (reviewed) | ProperExtension packages the V-admissible blow-up, V', proper ψ, ψ^{-1}(V)=V and ψ\|_V = id. |
| `lemma-separation-closures` | 1 | full (reviewed) | Constructible closed subsets of qcqs V are given as closed sets with quasi-compact complement. |
| `lemma-extending-isomorphism-over-closure-closed` | 1 | full (reviewed) | Same statement. |
| `lemma-gluing-after-admissible-blow-ups` | 3 | full (reviewed) | Density statement assumes T_i qcqs, automatic for finite type over qcqs S. |
| `proposition-compactifying-union-two-opens` | 1 | full (reviewed) | Same statement over a Noetherian base. |
| `lemma-affine-covers-dense-intersection` | 3 | partial (reviewed) | Cover part needs only X quasi-compact with finitely many irreducible components. Not in Lean: No single statement that each U_r has a compactification closed in P^n_S; projectiveClosure_spec needs an immersion into A^n_S (Stacks 04II). |
| `theorem-chow-s-lemma-projective-form` | 2 | full (reviewed) | exists_chow_finite_type gives π proper surjective and immersion i_S; chow_relative_ample upgrades for proper f (also states extra ampleness). |

### Abelian varieties

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `example-cube-two-factors` | 0 | none (reviewed) | Illustrative example; nothing in Lean states it. Not in Lean: the whole example (elliptic curve line bundle trivial on slices but not trivial) |
| `lemma-triviality-fibres` | 2 | full (reviewed) | Part 1 with B = L^{-1} via A⊗B≅O; part 2 is the closedness for N = O. Lean works over a general proper flat base with geometrically integral fibres. |
| `corollary-triviality-over-open-cover-base` | 0 | none (reviewed) | Lean glues along a section instead (nonempty_iso_of_forall_exists_nonempty_iso_preimageSnd), which is a different statement. Not in Lean: f_*L invertible and f^*f_*L -> L an isomorphism |
| `lemma-h-1-structure-sheaf-product` | 0 | none (reviewed) | Lean only has H^1 vanishing of the cross ideal (TheoremOfCube.subsingleton_H_one_crossIdeal), a proof input, not this statement. Not in Lean: the restriction isomorphism H^1(PxQ,O) -> H^1(P,O)+H^1(Q,O) |
| `lemma-triviality-near-fibre` | 1 | full (reviewed) | Stated for M, N isomorphic on the slices and on the fibre over a field-valued point; L case is N = O. |
| `theorem-theorem-cube` | 1 | full (reviewed) | Lean form M ≅ N from isomorphisms on three slices; L case is N = O. nonempty_iso_cube is the abelian-variety corollary, not this node. |
| `lemma-rigidity` | 1 | full (reviewed) | Local rigidity; Lean assumes X geometrically connected and geometrically reduced, weaker than geometrically integral. |
| `definition-abelian-variety` | 3 | partial (reviewed) | Class uses ConnectedSpace; the iff bridges to geometric connectedness. A[n] = kernel of 𝟙 A ^ n. Not in Lean: symmetric invertible sheaf ([-1]^*L ≅ L) has no Lean definition; [n] is just 𝟙 A ^ n |
| `lemma-abelian-variety-commutative` | 2 | full (reviewed) | Both assertions are instances. |
| `lemma-symmetric-ample-sheaf` | 4 | full (reviewed) | Projectivity; an ample L exists; L⊗[-1]^*L is ample and symmetric. |
| `proposition-pullback-multiplication-n` | 1 | partial (reviewed) | Only the symmetric case [n]^*N ≅ N^{n^2} is in Lean. nonempty_iso_cube (the trivial sheaf on AxAxA) is a proof input. Not in Lean: the general formula [n]^*L ≅ L^{n(n+1)/2} ⊗ ([-1]^*L)^{n(n-1)/2} for non-symmetric L |
| `proposition-multiplication-n` | 6 | full (reviewed) | Étale part is stated as CharP K p with p not dividing n, which is the same as n invertible. |
| `definition-tate-module` | 3 | full (reviewed) | T_l is defined as T_l(A(kbar)); the Equiv identifies it with the limit of A[l^n](kbar) along multiplication by l. |
| `proposition-integral-tate-module` | 3 | partial (reviewed) | The Galois action on T_l is defined componentwise. Field invariance for A over an algebraically closed field is bijective_toUnit_comp_torsionSubgroupScheme, which is assigned to the torsion corollary. Not in Lean: T_l/l^n T_l ≅ A[l^n](kbar); Galois equivariance of the transition maps and projections as statements; invariance under larger algebraically closed fields for A over a non-closed k |
| `proposition-no-frobenius-fixed-vector` | 3 | partial (reviewed) | The automorphism is stated for arithmetic Frobenius σ; σ-1 is bijective exactly when F-1 = σ^{-1}-1 is. Not in Lean: the powers F^m with m>1 (Lean has m=1 over any finite base field, so F^m only through base change to F_{q^m}); F^m-1 an automorphism of V_l A ⊗ E |

### The Picard scheme of a curve

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `definition-relative-picard-functor` | 2 | full (reviewed) | Lean sheafifies T ↦ Pic(C_T) and does not quotient by Pic(T) first; Zariski-locally trivial classes die, so the fppf sheaf is the same. Representability is used as RepresentableBy, with no named Picard-scheme definition. |
| `lemma-rigidification-along-section` | 8 | full (reviewed) | Rigidified pairs are classes with σ_T^*L trivial. Surjectivity onto Pic_{C/S}(T) and the splitting are in bijective_pic_split. The normalization formula is picMulEquivProdPicardFunctorNormalized. |
| `theorem-riemann-roch-coherent-serre-duality` | 5 | full (reviewed) | Lean's Modules.degree is defined as χ(L)-χ(O), so RR is χ(O)=1-g. deg L ≥ 2g-1 matches deg L > 2g-2. |
| `corollary-serre-duality-field-extension` | 2 | partial (reviewed) | Only the consequences dim H^0(ω)=g and invariance of the genus under field extension. Not in Lean: compatibility of the Serre duality pairing with extension of scalars |
| `lemma-coherent-base-change-invertible-sheaves` | 6 | partial (reviewed) | Use i=0, r=1: the open locus U_{0,1}, f_*L invertible there, base change of f_*L, and R^1=0. Perfectness is stated over a Noetherian base only. Not in Lean: local perfectness of Rf_*L over an arbitrary (non-Noetherian) k-scheme T |
| `theorem-hilbert-schemes-points-smooth-curve` | 4 | full (reviewed) | The Hilbert functor is by definition finite locally free degree-d closed subschemes; isInvertible gives the Cartier property for every T. |
| `proposition-divisors-degree-g-open-chart` | 3 | full (reviewed) | Lean assumes k separably closed with a rational point σ; F is picardFunctorInvertibleDirectImage. |
| `lemma-twisting-h-0-1-h` | 1 | full (reviewed) | Exact match: k separably closed, any extension K, an invertible M_0 on C. |
| `lemma-representability-picard-functor` | 1 | partial (reviewed) | Lean assumes geometrically integral, which the text derives from connected over k separably closed. Represented by a group scheme compatible with ⊗. Not in Lean: locally of finite type; cover by the translates M^{-1}F (only the general criterion exists_isOpenImmersion_of_representable_open_subfunctor) |
| `lemma-tangent-space-picard-functor` | 1 | full (reviewed) | ker(Pic(X[ε]) -> Pic X) ≅ H^1(X,O_X), also compatible with scaling. |
| `theorem-picard-scheme-jacobian-over-separably` | 6 | partial (reviewed) | theorem_of_the_base gives representability, the decomposition, the components and their k-points; exists_jacobian_baseChange gives J abelian, J(k)=Pic^0 and base change. Not in Lean: base change of the degree-d components (stated by nonempty_representableBy_picardFunctorDegree_baseChange, assigned to proposition-jacobian-over-ground-field) |
| `corollary-degree-jacobian` | 5 | full (reviewed) | Kernel is Pic^0; J(C)(k)=Pic^0 comes from the main theorem (exists_jacobian_baseChange). |
| `example-degree-sequence-genus-zero-one` | 0 | none (reviewed) | Example; nothing in Lean states it. Not in Lean: the computations for P^1 and elliptic curves |
| `example-two-torsion-elliptic-curve` | 0 | none (reviewed) | Example; nothing in Lean states it. Not in Lean: the 2-torsion of y^2=(x-e1)(x-e2)(x-e3) |
| `corollary-torsion-jacobian-field-extension` | 4 | full (reviewed) | J[n](k) ≅ (Z/n)^{2g} is stated through Pic[n]. Field invariance comes from bijective_toUnit together with jacobian_compatibility (J(C_k') = J(C)_k'). ker of deg mod n is nPic. |
| `proposition-jacobian-over-ground-field` | 2 | full (reviewed) | exists_jacobian_descent: J_0 proper, smooth of dim g, geometrically integral commutative group representing Pic^0, base change to kbar, Galois-equivariant J_0(kbar)=Pic^0(C). |
| `proposition-h-1-curve-tate-module` | 4 | partial (reviewed) | Lean's version is for finite K, the case the main text needs. Possible overlap with proposition-kummer-duality-integral-tate-module, which holds JacobianTorsionDatum. Not in Lean: a general ground field (Lean: finite fields only); pro-étale rather than étale cohomology; the inverse-limit isomorphism with T_l J_0 |

### Cohomology of torsion sheaves on curves

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `lemma-cohomology-multiplicative-group` | 3 | full (reviewed) | Etale version carries naturality under pullback; pro-etale version for nu^*G_m; Br=0 for smooth C (a version without smoothness, IsCurve.subsingleton_cohomologicalBrauerGroup, also exists). |
| `proposition-smooth-proper-curves-torsion-prime` | 1 | full (reviewed) | Single theorem bundling H^0..H^q, J[n](k), degree mod n, and invariance under algebraically closed extension (etale site). |
| `remark-twists-projective-line` | 0 | none (reviewed) | Remark; nothing in Lean states it. Not in Lean: Twist identification H^2(C,Z/n)=(Z/n)(-1) and the P^1 normalization are not stated. |
| `proposition-cohomology-smooth-affine-curve` | 5 | partial (reviewed) | IsConnectedCurve.sheafH_constantZMod_of_isAffine is declared inside namespace AlgebraicGeometry (lk.py indexes it without the prefix). Not in Lean: Surjectivity of the sum map onto Z/n; H^1(U) only as cardinality n^(2g+#D-1), not as (Z/n)^r; Lean uses Z/n coefficients with residues in Z/n(-1) instead of mu_n. |
| `proposition-p-torsion-smooth-proper-curve` | 5 | partial (reviewed) | Finiteness and base change are stated for Lambda/r coefficients (r prime), which include F_p. Not in Lean: H^1 is identified with the Frobenius fixed points of an unnamed finite-dimensional V, not explicitly H^1(C,O_C); the bound dim_Fp H^1 <= g is not stated. |
| `lemma-p-torsion-affine-curve-characteristic` | 1 | partial (reviewed) | Vanishing for q>=2 holds for any affine scheme with p=0. Not in Lean: H^1(U,F_p) = Gamma(U,O)/(phi-1)Gamma(U,O) is not stated; pro-etale transfer not stated. |
| `example-affine-line-characteristic-p` | 0 | none (reviewed) | Example; no Lean statement. Not in Lean: The computation of H^1(A^1,F_p) and its failure of finiteness/invariance are only mentioned in docstrings. |
| `lemma-finite-morphisms-cohomology` | 1 | partial (reviewed) | Etale-site statements only. Not in Lean: Exactness and base change of h_* (on the etale site they are lemma-finite-morphisms' names); pro-etale classical versions not stated. |
| `lemma-sheaves-finite-support-finite-morphisms` | 3 | partial (reviewed) | Vanishing stated in general on C; H^0 and invariance via the zero-dimensional case. Not in Lean: H^0 as the sum of stalks and its field-extension invariance are stated only for zero-dimensional C (the support), not for a sheaf on C supported at finitely many points. |
| `lemma-normalization-constant-sheaf` | 1 | partial (reviewed) | Lean: for finite surjective nu iso over a dense open, M_C -> nu_* M is mono with constructible cokernel vanishing on that open (j_! generality). Not in Lean: Branch formula M^b/Delta M for the cokernel; compatibility with algebraically closed extension; arbitrary finite M (Lean: Lambda/l). |
| `lemma-removing-finitely-many-points` | 1 | full (reviewed) | Matches hypotheses: reduced curve, dense open, constructible F with rF=0, assertions C1-C8. |
| `lemma-reduction-unipotent-local-system` | 1 | full (reviewed) | Cover of degree prime to l, filtration by constant F_l, and retraction of the unit. |

### Specialization and contracting correspondences

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `example-nearby-cycles-node` | 0 | — | Example; nothing states it. |
| `lemma-nearby-cycles-constant-family` | 0 | — | Lean has only point/trait cases (isIso_traitModel_unit); general constant family not found. |
| `example-normal-cone-point` | 0 | — | Example; nothing states it. |
| `lemma-functoriality-deformation` | 6 | medium | Found via Lean docstrings citing old det-sp-dnc-base-change (old blueprint had none). |
| `lemma-base-change-cone-x-z` | 4 | high | Lean docstrings cite old sk-lem-tf-sp-defect-exchanges details; Qbar_ell coefficients. |
| `lemma-case-z-v-x-m` | 2 | medium | Docstrings cite det-sp-thick-origin; Lean states constant unit coefficients (finite ring, Qbar_ell). |
| `lemma-vanishing-generic-points-principal-divisor` | 1 | high | Docstring cites det-sp-generic-divisor; principal divisor V(h), Qbar_ell coefficients. |
| `theorem-verdier-s-theorem-specialization-zero` | 3 | high | Docstrings cite det-sp-zero-section-vanishing / sk-thm-tf-sp-zero-section; Qbar_ell coefficients. |
| `proposition-external-kunneth-formula-nearby-cycles` | 2 | high | Docstrings cite sk-prop-tf-nearby-external-kunneth; Lean uses bounded constructible Qbar_ell. |
| `lemma-kunneth-map-proper-direct-image` | 1 | high | Docstring cites det-nearby-kunneth-proper. |
| `lemma-finite-support-global-sections` | 1 | high | Docstring cites det-nearby-kunneth-finite-support. |
| `lemma-quasi-finite-coordinates` | 0 | — | No Lean statement found; Lean Kunneth proof uses chart-dimension embeddings instead. |
| `lemma-kunneth-map-slice` | 2 | low | Lean states only the "in particular" isomorphism transfer for slices, per coefficient ring. |
| `lemma-compatibilities-base-change-maps` | 1 | low | Abstract mate form of (E.8), docstring cites det-nearby-exceptional-tensor (2). |
| `lemma-composition-exceptional-base-change-maps` | 2 | medium | beta composition (det-nearby-exceptional-tensor (3)) and theta law (mate-coherences (4)); conditional forms. |
| `lemma-base-change-maps-external-duality` | 2 | low | Abstract forms of (E.10), docstrings cite det-nearby-structural-product. |
| `lemma-base-change-maps-fixed-point-scheme` | 1 | medium | States (E.12) given compact-support exchange hypotheses; docstring cites mate-coherences (6). |
| `proposition-nearby-cycles-commute-verdier-duality` | 2 | high | Docstring cites sk-prop-tf-nearby-duality-foundation; Qbar_ell coefficients. |
| `lemma-nearby-duality-proper-direct-image` | 3 | medium | det-tf-nearby-duality-proper: abstract (E.14), open restriction, and RGamma(delta) iso as form of (E.15). |
| `lemma-duality-invariants-pro-p` | 3 | medium | Docstrings cite det-tf-invariants-duality; module-level pro-p and categorical finite-group forms, plus pairing. |
| `lemma-nearby-duality-slice` | 1 | low | Lean proves the iso consequence of (E.18) assuming TwistEquation; docstring cites det-tf-nearby-duality-slice. |
| `proposition-specialization-trace-class` | 2 | low | Lean defines sp_F and computes sp(Tr); full identity Tr(u_s)=sp(Tr(u)) not stated (vanishing route). |
| `lemma-nearby-cycles-universal-kernel` | 2 | high | Docstrings cite det-tf-sp-universal-kernel first and second identities. |
| `lemma-section-specialized-correspondence` | 2 | medium | Docstrings cite det-tf-sp-kernel-pullback (E.20) and second part; deformation setting, with hypotheses. |
| `corollary-specialization-when-fixed-point-scheme` | 1 | low | Only the contracting-deformation instance (injectivity on the component) is formalized. |
| `lemma-normal-cones-contracting-ideals` | 2 | medium | Docstrings cite det-tf-cone-zero-sections (1),(2); (1) only set-theoretically in Lean. |
| `example-contracting-squaring` | 0 | — | Example; nothing states it. |
| `lemma-fixed-point-scheme-deformation` | 0 | — | No Lean statement of the reduced fixed-scheme isomorphism found; only point-case facts used in exists_traceSpecialization. |
| `remark-reduction-connected-fixed-point-scheme` | 0 | — | Remark; nothing states it. |
| `theorem-contracting-correspondences-local-terms` | 1 | low | Lean has only Z a point: restriction of trace class equals pushforward; general Z not formalized. |
| `corollary-contracting-local-terms-point` | 2 | high | Point case of sk-thm-tf-contracting-local-term; ofGraph version is the (id,h) case. |

### Algebraic groups in characteristic zero

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `proposition-cartier-s-theorem` | 4 | full (reviewed) | Algebraic group = group scheme of finite type over Omega, so the general GrpObj statements suffice. |
| `lemma-connected-components-images-homomorphisms` | 7 | full (reviewed) | Subgroup structure of G° is an instance (GrpObj, IsMonHom.Normal) on GrpObj.identityComponent. |
| `lemma-stable-subspaces-center` | 2 | full (reviewed) | Stability statement for connected G with rational representation; centre formula for connected closed subgroups of GL_n. |
| `lemma-lie-s-theorem` | 1 | full (reviewed) | Lean assumes char 0 and triangularizable action, automatic over Omega. |
| `lemma-engel-s-theorem` | 2 | partial (reviewed) | Solvability follows from nilpotency by a Mathlib instance. Not in Lean: The strictly upper triangular basis is stated only as nilpotency of M as a Lie module (equivalent flag form). |
| `lemma-cartan-s-criterion` | 1 | full (reviewed) | Exact trace-form criterion for Lie subalgebras of End(M). |
| `lemma-killing` | 1 | partial (reviewed) | Nondegeneracy only. Not in Lean: [l,l]=l is not stated separately (only inside the proof of center_sup_derivedSeries_eq_top). |
| `proposition-lie-algebras-faithful-semisimple-representation` | 2 | full (reviewed) | HasCentralRadical is radical = center; second gives Z+[l,l]=l. |

## Section arrows

| Unit | uses | Why | Where the notes say it |
|---|---|---|---|
| `sec-w-local-and-w-contractible-rings` | `sec-Weakly-etale-morphisms` | Constructing contractible covers and pro-étale refinements uses stability of ind-étale/weakly étale maps under composition and base change. | proof of theorem-existence-contractible-covers, proof of theorem-pro-etale-refinements-weakly-etale (lemma-stability) |
| `sec-Affine-bases` | `sec-Weakly-etale-morphisms` | Spec D is an object of the site because ind-étale implies weakly étale and weakly étale maps compose (Proposition etale-implications, Lemma stability). | proof of theorem-enough-affine-weakly-contractible-objects |
| `sec-Affine-bases` | `sec-w-local-and-w-contractible-rings` | Basis of pro-étale affines from the refinement theorem; w-contractible affines are projective by splitting of ind-étale covers and cover by existence theorem. | prose-02-15, proof of proposition-pro-etale-affines-form-basis, proof of lemma-w-contractible-affines-projective, proof of theorem-enough-affine-weakly-contractible-objects |
| `sec-Weakly-contractible-objects` | `sec-Affine-bases` | Spectra of w-contractible rings are weakly contractible and cover every object; the evaluation corollary rests on these two facts. | prose-02-19, proof of corollary-evaluation-weakly-contractible-objects |
| `sec-Repleteness-and-limits` | `sec-Weakly-contractible-objects` | Repleteness, exact products and the Milnor sequence are proved by evaluating on weakly contractible objects, where epimorphisms are surjective. | proof of proposition-repleteness-pro-etale-topos, proof of proposition-exact-products, proof of proposition-milnor-sequence |
| `sec-Left-completeness-and-hypercovers` | `sec-Weakly-contractible-objects` | Hypercovers by weakly contractible affines: their terms have no higher cohomology and sections commute with filtered colimits. | proof of proposition-weakly-contractible-hypercovers, proof of corollary-continuity-cohomology |
| `sec-Left-completeness-and-hypercovers` | `sec-Repleteness-and-limits` | Left completeness is deduced from the Milnor sequence; 'products are exact, so that the Milnor sequence applies'. | prose-02-25, proof of proposition-left-completeness, proposition-unbounded-functors-products (2.1) |
| `sec-Classical-sheaves` | `sec-Weakly-etale-morphisms` | nu_X is defined by inclusion of étale objects, since étale maps are weakly étale and étale covers are pro-étale covers; classicality uses pro-étale affine presentations. | definition-classical-pro-etale-sheaves, proof of proposition-comparison-morphism-inverse-image |
| `sec-Classical-sheaves` | `sec-Affine-bases` | Classical sheaves = essential image of nu^*: the counit is checked on pro-étale affines, which form a covering basis. | proof of theorem-classical-sheaves-essential-image |
| `sec-Comparison-with-the-etale-site` | `sec-w-local-and-w-contractible-rings` | Acyclicity of pulled-back injectives: pro-étale covers of affines are refined by ind-étale ones (refinement theorem), making Čech complexes colimits of étale ones. | proof of lemma-acyclicity-pulled-back-injectives |
| `sec-Comparison-with-the-etale-site` | `sec-Classical-sheaves` | Bounded-below comparison uses full faithfulness of nu^* and formula (2.6); classical complexes are characterized via the essential-image theorem. | prose-02-32, proof of theorem-bounded-below-cohomology-comparison, proof of corollary-bounded-below-classical-complexes |
| `sec-Direct-images` | `sec-Classical-sheaves` | The comparison map is built from nu^* and evaluated on pro-étale affines by formula (2.6). | prose-02-36, proof of theorem-comparison-direct-images, proof of proposition-comparison-immersions |
| `sec-Direct-images` | `sec-Comparison-with-the-etale-site` | Comparison of direct images is proved from (2.6) and the bounded-below cohomology comparison; classical complexes are pullbacks. | proof of theorem-comparison-direct-images, prose-02-37 |
| `sec-Constructible-sheaves` | `sec-w-local-and-w-contractible-rings` | Descending torsors: refine a trivializing cover to one ind-étale affine via the refinement theorem. | proof of lemma-torsors-under-classical-groups |
| `sec-Constructible-sheaves` | `sec-Classical-sheaves` | Torsors under classical groups are classical by the essential-image theorem; exactness and monoidality of nu^* give the Tor comparison. | proof of lemma-torsors-under-classical-groups, proof of corollary-finite-tor-amplitude-under-comparison |
| `sec-Constructible-sheaves` | `sec-Comparison-with-the-etale-site` | Classical sheaves are closed under extensions (R^1 nu_* vanishes) and the derived equivalence uses bounded-below classical complexes. | prose-02-41, proof of theorem-comparison-constructible-sheaves |
| `sec-Constructible-sheaves` | `sec-Direct-images` | Induction on strata: j_! and i_* preserve classical sheaves 'by the comparisons of Section Direct images'. | prose-02-41, proof of theorem-comparison-constructible-sheaves |
| `sec-Unbounded-complexes` | `sec-Conventions` | Needs the standing convention that k is finite or algebraically closed: 'For our field k the hypothesis holds' (cd_l(k) finite); Conventions says this is why k is so chosen. | prose-02-45, lemma-uniform-bounds-pro-etale-affines, prose-01-10 |
| `sec-Unbounded-complexes` | `sec-Left-completeness-and-hypercovers` | Truncation lemma: by left completeness L is the derived limit of truncations; the Milnor sequence bounds degrees. | proof of lemma-truncation-pro-etale-sections |
| `sec-Unbounded-complexes` | `sec-Classical-sheaves` | Uniform bounds write F=nu^*F_et by the essential-image theorem; classical sheaves closed under direct sums. | proof of lemma-uniform-bounds-pro-etale-affines, prose-02-47 |
| `sec-Unbounded-complexes` | `sec-Comparison-with-the-etale-site` | cd_l agrees with étale cd by the comparison; the unbounded comparison reduces to the bounded-below theorem. | prose-02-45, proof of lemma-uniform-bounds-pro-etale-affines, proof of proposition-unbounded-comparison-finite-coefficients |
| `sec-Unbounded-complexes` | `sec-Direct-images` | Unbounded comparison of direct images reduces to Theorem comparison-direct-images on bounded-below truncations. | proof of proposition-unbounded-comparison-finite-coefficients, prose-02-45 |
| `subsec-Condensed-rings` | `sec-Weil-cohomology` | Condensed coefficients are introduced because the discrete constant sheaf Z_l has H^1=0 on Spec F_q (Section Weil cohomology): 'We therefore need' a coefficient ring keeping the topology. | prose-02-49 |
| `subsec-Condensed-rings` | `sec-Weakly-etale-morphisms` | Identifies pro-étale affines over Spec Omega (ind-étale algebras) and their fpqc covers with profinite sets and finite surjective families. | proposition-pro-etale-site-separably-closed and its proof |
| `subsec-Condensed-rings` | `sec-Affine-bases` | The pro-étale site of a separably closed field is profinite sets; the topoi agree because pro-étale affines form a basis. | proof of proposition-pro-etale-site-separably-closed |
| `subsec-Coefficient-sheaves` | `sec-Weakly-etale-morphisms` | p_X is built from the pro-étale scheme Spec LC(S,Z) and the structure morphism of topoi; f^{-1}Lambda_Y = Lambda_X from functoriality. | prose-02-51 |
| `subsec-Coefficient-sheaves` | `subsec-Condensed-rings` | Lambda_X = p_X^* Lambda for condensed rings Lambda on the site of profinite sets, including the colimit condensed ring Qbar_l. | prose-02-51, lemma-comparison-completed-coefficients and proof |
| `subsec-Inverse-image` | `subsec-Coefficient-sheaves` | f^{-1}Lambda_Y = Lambda_X from p_Y∘f=p_X; Tate twists and finite freeness of O_{E'} over O_E pulled back along p_X. | proof of lemma-inverse-image-coefficient-sheaves |
| `sec-Continuous-cohomology` | `sec-Repleteness-and-limits` | F ≃ Rlim F_n by the last assertion of the Milnor sequence proposition; the exact sequence (2.11) is the Milnor sequence. | proof of proposition-continuous-cohomology-pro-etale-cohomology, prose-02-58 |
| `sec-Continuous-cohomology` | `sec-Comparison-with-the-etale-site` | Each R Gamma(X_proet,F_n) is étale cohomology by the bounded-below comparison, giving continuous étale cohomology. | proof of corollary-continuous-etale-cohomology, prose-02-57 |
| `sec-Continuous-cohomology` | `subsec-Coefficient-sheaves` | Z_l,X is the inverse limit of the classical (Z/l^n)_X with surjective transitions (Lemma comparison-completed-coefficients). | prose-02-56, example-first-cohomology-finite-field |
| `sec-Extension-by-zero-and-completion` | `sec-Weakly-contractible-objects` | i^* preserves limits because evaluating on a weakly contractible affine is evaluation on one object; such objects detect isomorphisms. | prose-02-59, proof of proposition-extension-zero-restriction-closed-subscheme (Step 1) |
| `sec-Extension-by-zero-and-completion` | `sec-Repleteness-and-limits` | Statements about limits of module sheaves under j_! follow 'as j_! is exact and products are exact'. | proof of proposition-extension-zero-restriction-closed-subscheme (Step 3) |
| `sec-Extension-by-zero-and-completion` | `subsec-Coefficient-sheaves` | Derived completeness is defined for O_{E,X}=p_X^*O_E; K_n is the cone of pi^n by the two-term resolution of (O_E/pi^n)_X. | definition-derived-adic-completeness, proof of lemma-reduction-derived-nakayama |
| `sec-Derived-functors` | `subsec-Inverse-image` | f^*M is just f^{-1}M since f^{-1}Lambda_Y ≃ Lambda_X, making f^* exact. | prose-03-02, prose-02-55 |
| `sec-Constructibility` | `sec-Weakly-etale-morphisms` | The local condition is imposed on a pro-étale cover {U_i→X}; lisse = condition on X itself | definition-constructible-sheaves, definition-lisse-sheaves |
| `sec-Constructibility` | `sec-Coefficient-rings` | One definition of constructibility for every condensed coefficient ring Lambda, with Lambda_X and restriction M\|_Z=g^*M from the coefficient-ring section. | prose-03-03, definition-constructible-sheaves |
| `sec-Constructibility` | `subsec-Condensed-rings` | Constructibility is defined for a commutative condensed ring Λ, locally Λ_U⊗_{Λ(*)}P with Λ(*) the sections over the point | definition-constructible-sheaves |
| `sec-Constructibility` | `sec-Derived-functors` | Definitions use M\|_Z=g^*M, D(X_proet,Λ) and ⊗^L (Tor amplitude) of the derived functors set up just before | prose-03-03, definition-constructible-sheaves |
| `sec-Integral-constructible-complexes` | `sec-Affine-bases` | Local structure: 'Choose an affine weakly contractible cover W→S' to make finite-level trivializations global | proof of proposition-local-structure-integral-constructible-complexes |
| `sec-Integral-constructible-complexes` | `sec-Weakly-contractible-objects` | Mittag-Leffler argument: 'Since W is weakly contractible, taking sections over W is exact' | proof of lemma-integral-model-weakly-contractible, prose-03-12 |
| `sec-Integral-constructible-complexes` | `sec-Repleteness-and-limits` | Milnor sequence: R^1lim vanishes for epimorphic towers, used in bounds and the constructibility criterion. | proof of lemma-bounds-finite-reductions, proof of lemma-integral-model-weakly-contractible, proof of proposition-integral-constructibility-criterion |
| `sec-Integral-constructible-complexes` | `sec-Constructible-sheaves` | Finite reductions are classical constructible complexes by the comparison theorem; Tor bounds carried over. | proof of lemma-bounds-finite-reductions, prose-03-07 |
| `sec-Integral-constructible-complexes` | `subsec-Coefficient-sheaves` | O_{E,X} is the limit of its finite quotients (Lemma comparison-completed-coefficients). | proof of proposition-integral-constructibility-criterion |
| `sec-Integral-constructible-complexes` | `sec-Extension-by-zero-and-completion` | Works with derived complete complexes, derived Nakayama, and limit-preservation of j_!, i^*. | prose-03-07, proof of proposition-integral-constructibility-criterion, proof of lemma-integral-model-weakly-contractible |
| `sec-Integral-constructible-complexes` | `sec-Derived-functors` | Extension by zero a_!=i_*j_! from strata 'factored as in Section Derived-functors' preserves completeness | proof of proposition-integral-constructibility-criterion |
| `sec-Integral-constructible-complexes` | `sec-Constructibility` | Criterion characterizes Dbc(X,O_E) of the Definition; (3)⇒(1) checks Definition (1); (4) is D^b_ctf | proposition-integral-constructibility-criterion and its proof |
| `sec-Finite-Tor-amplitude` | `sec-Constructible-sheaves` | Flat models: C=ν^*C_et by corollary-finite-tor-amplitude-under-comparison, then pull back the étale flat model | proof of lemma-flat-models-generators |
| `sec-Finite-Tor-amplitude` | `sec-Constructibility` | Field case: constructible sheaves are locally Λ_U⊗P, hence flat; the Tor condition and the Z/ℓ^2 example of Section Constructibility | proof of proposition-ctf-equals-bc, prose-03-17 |
| `sec-Finite-Tor-amplitude` | `sec-Integral-constructible-complexes` | For O_E (hence Z_ℓ) ctf=bc 'is the equivalence of (1) and (4) in the criterion above' | proof of proposition-ctf-equals-bc |
| `sec-Field-coefficients` | `subsec-Coefficient-sheaves` | Sections of E_X are continuous functions to E; Qbar_X = colim E_X (Lemma comparison-completed-coefficients). | proof of lemma-lattices-lisse-e-sheaves, proof of lemma-descent-lisse-qbar-sheaves-finite |
| `sec-Field-coefficients` | `sec-Derived-functors` | Dévissage to 'the sheaves a_!L of Section Derived-functors'; filtration (3) and generators are a_!L | prose-03-18, lemma-constructible-sheaves, corollary-coefficient-heart-b |
| `sec-Field-coefficients` | `sec-Constructibility` | Works with lisse/constructible E- and Qbar-sheaves as defined there (constructible = lisse on strata) | prose-03-18 |
| `sec-Field-coefficients` | `sec-Finite-Tor-amplitude` | 'Λ=E or Qbar, so that D^b_ctf=Dbc and we can argue with constructible cohomology sheaves and standard truncations' | prose-03-18 |
| `sec-Continuity-of-Ext` | `sec-Left-completeness-and-hypercovers` | Continuity of Ext reduces to Corollary continuity-cohomology for cohomology and higher direct images. | prose-03-24, proof of lemma-continuity-ext-out-constructible-complex |
| `sec-Continuity-of-Ext` | `sec-Extension-by-zero-and-completion` | Stratum formula uses local cohomology and its adjunction with i_*. | lemma-sections-support-closed-subscheme and its proof |
| `sec-Continuity-of-Ext` | `sec-Field-coefficients` | Reduce M to generators a_!L by corollary-coefficient-heart-b (filtration of lemma-constructible-sheaves(3)) | prose-03-24, proof of lemma-continuity-ext-out-constructible-complex |
| `sec-Descent-to-a-finite-extension` | `sec-Field-coefficients` | Objects descend along the filtration of lemma-constructible-sheaves(3), lisse pieces by lemma-descent-lisse-qbar-sheaves-finite | proof of lemma-descent-finite-coefficient-field |
| `sec-Descent-to-a-finite-extension` | `sec-Continuity-of-Ext` | 'Morphisms descend because Hom out of a constructible complex commutes with this colimit' (lemma-continuity-ext) | proof of lemma-descent-finite-coefficient-field |
| `sec-Lattices-after-stratification` | `sec-Field-coefficients` | Proof starts from the étale X-scheme of lattices (lemma-lattices-lisse-e-sheaves); nodal curve example repaired | proof of lemma-lattices-after-finite-stratification, prose-03-28 |
| `sec-Integral-models` | `subsec-Inverse-image` | (3) inverse image: f^* sends finite free O_{E,Y}-modules to finite free O_{E,X}-modules by lemma-inverse-image-coefficient-sheaves | proof of lemma-integral-models |
| `sec-Integral-models` | `sec-Integral-constructible-complexes` | (2),(3) use the two characterizations of the integral criterion and the local structure proposition | prose-03-30, proof of lemma-integral-models |
| `sec-Integral-models` | `sec-Field-coefficients` | (4) combines the dévissage of corollary-coefficient-heart-b with lattices | proof of lemma-integral-models |
| `sec-Integral-models` | `sec-Descent-to-a-finite-extension` | (4) 'For Qbar, we first descend to a finite E by Lemma descent-finite-coefficient-field' | proof of lemma-integral-models, prose-03-27 |
| `sec-Integral-models` | `sec-Lattices-after-stratification` | (4): 'We refine the stratum S as in Lemma lattices-after-finite-stratification' to get L_0 | proof of lemma-integral-models, prose-03-28 |
| `sec-Inverting-ell` | `sec-Extension-by-zero-and-completion` | 'By the localization sequences of Proposition extension-zero-restriction-closed-subscheme a larger power kills every cohomology sheaf' | proof of proposition-inverting-ell |
| `sec-Inverting-ell` | `sec-Constructibility` | Killing by a power of ℓ: 'By Definition constructible-sheaves there is a finite stratification…' with finitely generated P | proof of proposition-inverting-ell |
| `sec-Inverting-ell` | `sec-Integral-models` | Essential surjectivity: 'recall from Lemma integral-models(4) that Dbc(X,E) is generated by objects from Dbc(X,O_E)' | proof of proposition-inverting-ell |
| `sec-The-base-change-map` | `sec-Direct-images` | Naturality of pasting uses the comparison isomorphisms of direct images and their compatibilities. | lemma-naturality-pasting-comparison and its proof |
| `sec-The-base-change-map` | `subsec-Inverse-image` | Inverse images are exact for admissible Lambda (Lemma inverse-image-coefficient-sheaves), needed for the adjunction f^*⊣Rf_*. | prose-04-07 |
| `sec-The-base-change-map` | `sec-Derived-functors` | Pro-étale map is the adjoint transpose for f^*⊣Rf_* on unbounded derived categories, set up in Derived functors | prose-04-07, definition-pro-etale-base-change-map |
| `sec-Base-change-in-degree-zero` | `sec-The-base-change-map` | Main result: the underived base change map (4.2) is an isomorphism for proper f; computed via its description on sections | proposition-proper-base-change-degree-zero and proof |
| `sec-Torsion-sheaves-and-acyclicity` | `sec-The-base-change-map` | PBC_Λ(f) is defined by the base change map (4.3); (iii)⇒(ii) identifies the termwise map with (4.3) via (4.4) | definition-torsion-pbc-property, proof of theorem-pbc-injective-acyclicity |
| `sec-Torsion-sheaves-and-acyclicity` | `sec-Base-change-in-degree-zero` | Main step (iii)⇒(ii) applies the degree-zero isomorphism termwise to an injective resolution | prose-04-15, proof of theorem-pbc-injective-acyclicity |
| `subsec-Henselian-pairs-and-curves` | `sec-Comparison-with-the-etale-site` | Lemma extension-separably-closed-ground-field: 'By the classical comparison we may compute on the étale site' | proof of lemma-extension-separably-closed-ground-field |
| `subsec-Henselian-pairs-and-curves` | `sec-Devissage` | Theorem cohomology-curves is stated here and 'The proof is in Appendix D', completed in Section Dévissage | proof of theorem-cohomology-curves, proof/theorem-cohomology-curves/2 |
| `subsec-Injectives-on-the-closed-fibre` | `sec-Base-change-in-degree-zero` | 'we apply the comparison in degree zero of Theorem comparison-over-henselian-pair-degree to an injective resolution' | prose-04-23, proof of proposition-cohomology-p-1-over-henselian |
| `subsec-Injectives-on-the-closed-fibre` | `subsec-Henselian-pairs-and-curves` | Acyclicity on the closed fibre uses Gabber's theorem (i) and lifting finite torsors (4.8) from remark-henselian-pairs-facts | proof of lemma-acyclicity-closed-fibre |
| `subsec-Arbitrary-base-change` | `sec-The-base-change-map` | Top square commutes 'by the definition of the base change map' on sections; modules vs abelian sheaves remark | proof of proposition-proper-base-change-projective-line |
| `subsec-Arbitrary-base-change` | `sec-Torsion-sheaves-and-acyclicity` | Proposition is PBC for π on torsion complexes and concludes IA_Λ(π) (definitions of PBC/IA, torsion sheaves) | proposition-proper-base-change-projective-line |
| `subsec-Arbitrary-base-change` | `subsec-Henselian-pairs-and-curves` | Bottom arrow is an isomorphism by lemma-extension-separably-closed-ground-field ('second place where properness enters') | prose-04-27, proof of proposition-proper-base-change-projective-line |
| `subsec-Arbitrary-base-change` | `subsec-Injectives-on-the-closed-fibre` | Stalks of R^qπ_*F are cohomology of P^1 over the residue field by proposition-cohomology-p-1-over-henselian | prose-04-27, proof of proposition-proper-base-change-projective-line |
| `sec-Proper-morphisms` | `sec-The-base-change-map` | Lemma finite-morphisms: underived and derived base change maps (4.2),(4.3) are isomorphisms for finite u | lemma-finite-morphisms and proof |
| `sec-Proper-morphisms` | `sec-Base-change-in-degree-zero` | Composition/cancellation uses u'_*g_X^*J≃g_Y^*u_*J by proper base change in degree zero | proof of lemma-composition-cancellation |
| `sec-Proper-morphisms` | `sec-Torsion-sheaves-and-acyclicity` | Composition and descent 'best proved on the level of injective acyclicity. By Theorem pbc-injective-acyclicity it is equivalent' | prose-04-30, proof of lemma-composition-cancellation |
| `sec-Proper-morphisms` | `sec-Chows-lemma` | Last descent: Theorem chow-s-lemma-projective-form over an affine, non-Noetherian base, proved in Appendix A | proof of proposition-proper-base-change-etale-site, prose-04-33 |
| `sec-Pro-etale-complexes` | `sec-Comparison-with-the-etale-site` | Proper base change on the pro-étale site: write K=nu^*K_et by Corollary bounded-below-classical-complexes. | prose-04-34, proof of theorem-proper-base-change-classical-pro |
| `sec-Pro-etale-complexes` | `sec-Direct-images` | nu^* commutes with direct images along proper maps (Theorem comparison-direct-images). | prose-04-34, proof of theorem-proper-base-change-classical-pro |
| `sec-Pro-etale-complexes` | `subsec-Condensed-rings` | Geometric fibres: the topos of a separably closed field is that of condensed sets. | proof of corollary-cohomology-geometric-fibres |
| `sec-Pro-etale-complexes` | `sec-The-base-change-map` | Statement is for the pro-étale map (4.5); last assertion of lemma-naturality-pasting-comparison transports the étale isomorphism | theorem-proper-base-change-classical-pro and proof |
| `sec-Pro-etale-complexes` | `sec-Torsion-sheaves-and-acyclicity` | Dévissage via F=colim F[n] (Definition torsion-sheaves), continuity (4.7), truncation argument of theorem-pbc-injective-acyclicity | proof of theorem-proper-base-change-classical-pro |
| `sec-Pro-etale-complexes` | `subsec-Arbitrary-base-change` | PBC_{Λ/pΛ}(f) holds by Propositions proper-base-change-projective-line and …-etale-site | proof of theorem-proper-base-change-classical-pro, prose-04-34 |
| `sec-Pro-etale-complexes` | `sec-Proper-morphisms` | Same: proposition-proper-base-change-etale-site (conditional on P^1) gives étale PBC for torsion rings | proof of theorem-proper-base-change-classical-pro, prose-04-34 |
| `sec-Finite-coefficients` | `sec-Direct-images` | 'by Theorem comparison-direct-images so do the proper direct images' — transport from the étale site | proof of proposition-proper-direct-image-finite-coefficients |
| `sec-Finite-coefficients` | `sec-Constructible-sheaves` | Étale and pro-étale D^b_ctf agree (Corollary finite-tor-amplitude-under-comparison). | proof of proposition-proper-direct-image-finite-coefficients |
| `sec-Finite-coefficients` | `sec-Unbounded-complexes` | Tor bound [a,b+d] is in terms of cd_ℓ(X_ȳ) of Definition cohomological-dimension | proposition-proper-direct-image-finite-coefficients |
| `sec-Finite-coefficients` | `sec-Pro-etale-complexes` | 'proper base change identifies the geometric stalks of Rp_*C with the cohomology of its fibres', giving the Tor bound | prose-04-37, proof of proposition-proper-direct-image-finite-coefficients |
| `sec-ell-adic-coefficients` | `subsec-Coefficient-sheaves` | Reductions as cones of π_E^n via corollary-finite-quotients-their-transition-maps | proof of proposition-proper-base-change-complete-integral |
| `sec-ell-adic-coefficients` | `sec-Extension-by-zero-and-completion` | Derived π_E-completeness, completed inverse image and towers of Definition derived-adic-completeness | definition-completed-inverse-image, proof of proposition-proper-base-change-complete-integral |
| `sec-ell-adic-coefficients` | `sec-The-base-change-map` | Completed vs ordinary map: both built from the counit 'as in Definition pro-etale-base-change-map' | proof of lemma-completed-ordinary-base-change |
| `sec-ell-adic-coefficients` | `sec-Pro-etale-complexes` | 'Theorem proper-base-change-classical-pro applies at each finite level'; pass to the derived limit | proof of proposition-proper-base-change-complete-integral, prose-04-38 |
| `sec-Proper-direct-image` | `sec-Left-completeness-and-hypercovers` | Rp_* commutes with inverting l and extending scalars by continuity of cohomology. | prose-04-42, proof of proposition-proper-direct-image-constructible-complexes |
| `sec-Proper-direct-image` | `subsec-Inverse-image` | Uses that extension of scalars to E'/E is a finite direct sum (Inverse image says it is used in this proof). | prose-02-54, proof of proposition-proper-direct-image-constructible-complexes |
| `sec-Proper-direct-image` | `sec-Extension-by-zero-and-completion` | Derived Nakayama reduces integral statements to C/pi_E=0. | prose-04-42, proof of proposition-proper-direct-image-constructible-complexes |
| `sec-Proper-direct-image` | `sec-Integral-constructible-complexes` | Integral constructibility criterion and lemma-bounds-finite-reductions reduce O_E to torsion coefficients | prose-04-42, proof of proposition-proper-direct-image-constructible-complexes |
| `sec-Proper-direct-image` | `sec-Field-coefficients` | Rp_* preserves Dbc(E), Dbc(Qbar) since these are triangulated (corollary-coefficient-heart-b) | proof of proposition-proper-direct-image-constructible-complexes |
| `sec-Proper-direct-image` | `sec-Integral-models` | Inverse image preserves Dbc(O_E) (lemma-integral-models(3)); rational case via generators of (4) | proof of proposition-proper-direct-image-constructible-complexes |
| `sec-Proper-direct-image` | `sec-Pro-etale-complexes` | Finite coefficients: 'Proper base change holds by Theorem proper-base-change-classical-pro with Λ=A' | proof of proposition-proper-direct-image-constructible-complexes |
| `sec-Proper-direct-image` | `sec-Finite-coefficients` | 'For finite coefficients, constructibility and the Tor bound are Proposition proper-direct-image-finite-coefficients' | prose-04-42, proof of proposition-proper-direct-image-constructible-complexes |
| `sec-Proper-direct-image` | `sec-ell-adic-coefficients` | Integral case: Proposition proper-base-change-complete-integral and Lemma completed-ordinary-base-change | proof of proposition-proper-direct-image-constructible-complexes |
| `sec-Existence-and-finiteness-of-f` | `sec-Finite-Tor-amplitude` | 'By Proposition ctf-equals-bc the theorem holds with Dbc in place of D^b_ctf' for ℓ-adic Λ | prose-05-04, prose-05-03 |
| `sec-Compactness-of-constructible-complexes` | `sec-Field-coefficients` | 'the constructible heart, which is abelian by Lemma constructible-sheaves' | prose-05-06 |
| `sec-Compactness-of-constructible-complexes` | `sec-Continuity-of-Ext` | Uses that Ext^q(C,-) commutes with filtered colimits (Lemma continuity-ext, Section Continuity-of-Ext) | prose-05-06 |
| `sec-Compactness-of-constructible-complexes` | `sec-Existence-and-finiteness-of-f` | Shows bounded constructible complexes are compact in Loc(D^b_c), the localizing category of the existence section. | prose-05-06 |
| `subsec-A-uniform-bound-for-Ext` | `sec-Unbounded-complexes` | The Ext bound d_C is a sum of the cohomological dimensions cd_l, finite by Lemma cohomological-dimension-base-field. | prose-05-07, proof of lemma-ext-bound-lattices |
| `subsec-A-uniform-bound-for-Ext` | `sec-Descent-to-a-finite-extension` | The Qbar case reduces to finite E via Ext over Qbar as colimit over finite extensions. | proof of lemma-uniform-ext-bound |
| `subsec-A-uniform-bound-for-Ext` | `sec-Lattices-after-stratification` | Uniform Ext bound: 'After refining the stratifications (Lemma lattices-after-…), L and M contain lattices' | proof of lemma-uniform-ext-bound, prose-05-09 |
| `subsec-A-uniform-bound-for-Ext` | `sec-Integral-models` | b_!M_0 lies in D^b_c(X,O_E), hence is derived complete, which lets one pass to the limit over reductions. | proof of lemma-ext-bound-lattices |
| `subsec-Ind-constructible-sheaves` | `subsec-A-uniform-bound-for-Ext` | Corollary ind-heart-b extends the uniform Ext bound d_C from constructible to ind-constructible sheaves. | corollary-ind-heart-b, prose-05-11 |
| `subsec-Rational-coefficients` | `sec-Repleteness-and-limits` | Exact products give L = Rlim tau_{>=-n} L and the Milnor sequence for unbounded-below L. | proof of lemma-reduction-finitely-many-degrees |
| `subsec-Rational-coefficients` | `subsec-Ind-constructible-sheaves` | Reduction to finitely many degrees and compactness use Ext vanishing on IndCons and Loc(D^b_c) ⊂ D_ic. | prose-05-13, proof of lemma-reduction-finitely-many-degrees, proof of theorem-compactness-rational-coefficients |
| `sec-Compactness-for-finite-coefficients` | `sec-Constructible-sheaves` | On D^b_ctf the étale and pro-étale categories agree (Corollary finite-tor-amplitude-under-comparison). | proof of proposition-comparison-etale-derived-category |
| `sec-Compactness-for-finite-coefficients` | `sec-Unbounded-complexes` | Compactness is proved on the étale site and transported by the unbounded comparison for finite coefficients. | proof of proposition-compactness-finite-coefficients, proof of proposition-comparison-etale-derived-category |
| `sec-Compactness-for-finite-coefficients` | `sec-Finite-Tor-amplitude` | 'we work with the bounded flat models of Lemma flat-models-generators'; reduction to a_!L | prose-05-16, proof of proposition-compactness-finite-coefficients |
| `sec-Compactness-for-finite-coefficients` | `sec-Continuity-of-Ext` | Writes RHom(a_!L,-) as RGamma(S, L^vee ⊗ u^*RGamma_Z) by the étale form of the sections-with-support lemma. | proof of proposition-compactness-finite-coefficients |
| `sec-Compactness-for-finite-coefficients` | `sec-Finite-coefficients` | 'Proper direct image preserves D^b_ctf by Proposition proper-direct-image-finite-coefficients' | prose-05-16, prose-05-18 |
| `sec-Compactness-for-finite-coefficients` | `sec-Existence-and-finiteness-of-f` | Proves compact generation of Loc(D^b_ctf(X,A)) and identifies it with D(X_et,A). | proposition-compactness-finite-coefficients, proposition-comparison-etale-derived-category |
| `sec-Direct-image-with-compact-support` | `sec-Proper-direct-image` | Rf_!=Rp_*j_! built on Rp_* preserving D^b_ctf with base change (Construction-of-Rf, Direct-sums) | prose-04-42, proof of proposition-construction-independence-rf-shriek, proof of lemma-uniform-bound-proper-direct-image |
| `sec-Direct-image-with-compact-support` | `sec-Existence-and-finiteness-of-f` | Defines Rf_!=Rp_* j_! on the localizing categories Loc(D^b_ctf)=Loc(D^b_c) and must show it preserves direct sums. | prose-05-19 |
| `subsec-Direct-sums` | `sec-Weakly-contractible-objects` | R^qp_* is computed on affine weakly contractible V, where Gamma(V,-) is exact (5.5). | prose-05-20 |
| `subsec-Direct-sums` | `sec-Repleteness-and-limits` | Milnor exact sequence in the proofs of the uniform bound and unbounded proper direct image. | proof of lemma-uniform-bound-proper-direct-image, proof of lemma-proper-direct-image-unbounded-complexes |
| `subsec-Direct-sums` | `sec-Left-completeness-and-hypercovers` | Uniform bound and unbounded direct images use continuity of cohomology and left completeness. | proof of lemma-uniform-bound-proper-direct-image, proof of lemma-proper-direct-image-unbounded-complexes, prose-05-20 |
| `subsec-Direct-sums` | `sec-Field-coefficients` | Dévissage of constructible sheaves to a_!L and descent of lisse Qbar-sheaves to finite E. | proof of lemma-uniform-bound-proper-direct-image |
| `subsec-Direct-sums` | `sec-Lattices-after-stratification` | Uniform bound for proper direct image: after refinement L_E contains a lattice L_0 | proof of lemma-uniform-bound-proper-direct-image |
| `subsec-Direct-sums` | `sec-Proper-direct-image` | For constructible M, R^qp_*M is constructible since Rp_* preserves D^b_c. | proof of lemma-uniform-bound-proper-direct-image |
| `subsec-Direct-sums` | `subsec-Ind-constructible-sheaves` | R^qp_* preserves IndCons; Rp_* on D_ic uses closure of IndCons under kernels, cokernels, extensions. | lemma-proper-direct-image-unbounded-complexes, proof of lemma-proper-direct-image-unbounded-complexes |
| `subsec-Integral-coefficients` | `sec-Left-completeness-and-hypercovers` | Continuity then follows from continuity of cohomology. | proof of proposition-compactness-proper-direct-image |
| `subsec-Integral-coefficients` | `sec-Integral-constructible-complexes` | Lemma structure-integral-constructible-complexes: criterion conditions stable under cones; local structure proposition | proof of lemma-structure-integral-constructible-complexes |
| `subsec-Integral-coefficients` | `sec-Continuity-of-Ext` | Continuity of Ext out of a_!L via the sections-with-support formula, using only dualizability. | proof of proposition-compactness-proper-direct-image |
| `subsec-Integral-coefficients` | `sec-Integral-models` | Preservation of D^b_c(-,O_E) by the operations follows from Lemma integral-models(3). | proof of lemma-inverse-image-tensor-product |
| `subsec-Integral-coefficients` | `sec-Compactness-of-constructible-complexes` | For O_E the rational compactness proof (uniform Ext bound, reduction to finitely many degrees, compactness theorem) goes through. | prose-05-23, proof of proposition-compactness-proper-direct-image |
| `subsec-Integral-coefficients` | `subsec-Direct-sums` | The rational direct-sum argument for Rp_* (Lemma proper-direct-image-unbounded-complexes) goes through for O_E. | prose-05-23, proof of proposition-compactness-proper-direct-image |
| `subsec-Construction-of-Rf` | `sec-Proper-direct-image` | Proper base change and preservation of D^b_ctf by Rp_* are the inputs for independence of the compactification. | prose-05-27, proof of proposition-proper-base-change-localizing-categories, proof of proposition-construction-independence-rf-shriek |
| `subsec-Construction-of-Rf` | `sec-Compactness-for-finite-coefficients` | For finite A, Rp_* preserves sums on the localizing categories (Corollary). | proof of proposition-proper-direct-image-extension-zero |
| `subsec-Construction-of-Rf` | `subsec-Direct-sums` | For E and Qbar, Rp_* preserves direct sums by Lemma proper-direct-image-unbounded-complexes. | prose-05-27, proof of proposition-proper-direct-image-extension-zero |
| `subsec-Construction-of-Rf` | `subsec-Integral-coefficients` | For O_E, Rp_* preserves sums and j_!, inverse image preserve D^b_c by the integral results. | proof of proposition-proper-direct-image-extension-zero, proof of proposition-proper-base-change-localizing-categories |
| `subsec-Construction-of-Rf` | `sec-Compactifications` | Nagata compactifications, refinements and common refinements of dense compactifications. | remark-compactifications, proof of proposition-construction-independence-rf-shriek |
| `sec-Brown-representability` | `sec-Existence-and-finiteness-of-f` | Brown representability on Loc(D^b_ctf) gives f^!, part (3) of the theorem. | prose-05-33, lemma-hypotheses-brown-representability |
| `sec-Brown-representability` | `subsec-Rational-coefficients` | Compactness for E and Qbar is Theorem compactness-rational-coefficients. | proof of lemma-hypotheses-brown-representability, prose-05-15 |
| `sec-Brown-representability` | `sec-Compactness-for-finite-coefficients` | Compactness for finite A is Proposition compactness-finite-coefficients. | proof of lemma-hypotheses-brown-representability |
| `sec-Brown-representability` | `sec-Direct-image-with-compact-support` | Needs Rf_! preserving sums and D^b_ctf (Construction of Rf_!) and O_E compactness (Integral coefficients). | prose-05-33, proof of lemma-hypotheses-brown-representability |
| `sec-Composition-and-restriction` | `subsec-Construction-of-Rf` | Right adjoints of the composition and Rf_!=Rp_*j_! isomorphisms give (gf)^!=f^!g^!, j^!=j^*. | prose-05-35, proof of proposition-composition-open-restriction-compactifications-f |
| `sec-Composition-and-restriction` | `sec-Brown-representability` | Brown representability gives f^! one morphism at a time; uniqueness of adjoints relates them. | prose-05-35 |
| `sec-Conventions-2` | `sec-Comparison-with-the-etale-site` | The transported operations include cohomology and the category D^+_class. | prose-06-02 |
| `sec-Conventions-2` | `sec-Direct-images` | Torsion arguments run on the étale site and are transported, nu^* identifying direct images compatibly with units and counits. | prose-06-02 |
| `sec-Conventions-2` | `sec-Constructible-sheaves` | For finite coefficients objects of D^b_c are classical, and finite Tor amplitude can be checked on the étale site. | prose-06-02 |
| `sec-Conventions-2` | `sec-Unbounded-complexes` | D(X_proet,Lambda) for finite Lambda is identified with D(X_et,Lambda) by the unbounded comparison. | prose-06-02 |
| `sec-Conventions-2` | `sec-Pro-etale-complexes` | Results from étale theory: 'On the étale site this is Theorem proper-base-change-classical-pro' | remark-results-from-etale-theory |
| `sec-Conventions-2` | `sec-Compactness-for-finite-coefficients` | D_class is identified with Loc(D^b_ctf), on which f^! was constructed. | prose-06-02 |
| `sec-Conventions-2` | `subsec-Construction-of-Rf` | The comparison identifies the composition maps and forgetting-supports maps of Rf_! on the two sites. | prose-06-02 |
| `sec-Conventions-2` | `sec-Brown-representability` | Rf_! and f^! on D_class are those of Theorem existence-exceptional-inverse-image. | prose-06-02 |
| `sec-Duality-for-the-projective-line` | `sec-Conventions-2` | Constructs cycle class, trace and unit/counit on the étale site and transports them by nu^*, as in Conventions. | proof of lemma-cycle-class-cartier-divisor, prose-06-07, prose-06-08 |
| `sec-Duality-for-the-projective-line` | `sec-Kummer-theory` | Cohomology of P^1 geometric fibres from the genus-zero case of Proposition smooth-proper-curves-torsion-prime. | proof of lemma-cohomology-projective-line-trace |
| `sec-Smooth-morphisms` | `sec-Constructible-sheaves` | A locally constant sheaf of finite presentation has an étale trivialization (Proposition locally-constant-sheaves-finite-presentation). | proof of lemma-smooth-morphisms-locally-constant-sheaves |
| `sec-Smooth-morphisms` | `sec-Conventions-2` | Works with f^! on D_class, computed on the étale site. | lemma-affine-space-etale-localization, proposition-exceptional-inverse-image-smooth-morphism |
| `sec-Smooth-morphisms` | `sec-Duality-for-the-projective-line` | p_d^!=p_d^*(d)[2d] follows from the adjunction (6.7) for P^1 and j_! -\| j^*. | proof of lemma-affine-space-etale-localization, prose-06-09 |
| `sec-Coordinate-projections` | `sec-Conventions-2` | Detection lemma is stated in D^+_class and proved on the étale sites. | lemma-detection-proper-direct-image, proof of lemma-detection-proper-direct-image |
| `sec-Generic-base-change` | `sec-Smooth-morphisms` | Lemma smooth-morphisms-locally-constant-sheaves controls R(bj)_*F in Step 2. | proof of lemma-extension-across-finite-subset, prose-06-12 |
| `sec-Generic-base-change` | `sec-Coordinate-projections` | Step 1 uses coordinate projections; Step 2 uses detection by proper direct image. | proof of theorem-generic-constructibility-base-change-rj, proof of lemma-extension-across-finite-subset |
| `sec-Finite-coefficients-2` | `sec-Unbounded-complexes` | Rj_* on the étale site is identified with the pro-étale one by the unbounded comparison; Tor amplitude grows by cd_l(j). | proof of proposition-open-direct-image-preserves-finite, prose-06-17 |
| `sec-Finite-coefficients-2` | `sec-Extension-by-zero-and-completion` | Closed-immersion case of f^! uses local cohomology R Gamma_Z of Section Extension by zero. | proof of theorem-f-shriek-finite-coefficients |
| `sec-Finite-coefficients-2` | `sec-Continuity-of-Ext` | RGamma_Z is right adjoint to i_* (Lemma sections-support-closed-subscheme(1)). | proof of theorem-f-shriek-finite-coefficients |
| `sec-Finite-coefficients-2` | `sec-Finite-coefficients` | Rf_! preserves D^b_ctf(-,A), so the adjunction restricts. | proof of theorem-f-shriek-finite-coefficients |
| `sec-Finite-coefficients-2` | `sec-Brown-representability` | The theorem concerns the right adjoint f^! of Theorem existence-exceptional-inverse-image. | theorem-f-shriek-finite-coefficients, prose-06-17 |
| `sec-Finite-coefficients-2` | `sec-Composition-and-restriction` | Gluing: f^! compatible with composition and restriction to opens. | proof of theorem-f-shriek-finite-coefficients |
| `sec-Finite-coefficients-2` | `sec-Conventions-2` | cd_ell(j) finite (Remark results-from-etale-theory); Tor amplitude checked on the étale site. | proof of proposition-open-direct-image-preserves-finite |
| `sec-Finite-coefficients-2` | `sec-Duality-for-the-projective-line` | p^! for affine space from the adjunction Rq_* -\| q^*(1)[2] for P^1. | proof of theorem-f-shriek-finite-coefficients |
| `sec-Finite-coefficients-2` | `sec-Smooth-morphisms` | Lemma affine-space-etale-localization gives p^!=p^*(d)[2d]. | proof of theorem-f-shriek-finite-coefficients |
| `sec-Finite-coefficients-2` | `sec-Generic-base-change` | Rj_* is bounded constructible by Corollary open-direct-image-over-field; the proposition bounds Tor amplitude. | proof of proposition-open-direct-image-preserves-finite |
| `sec-ell-adic-coefficients-2` | `sec-Left-completeness-and-hypercovers` | Rj_* commutes with the filtered colimits inverting ell and extending scalars. | proof of proposition-direct-image-along-open-immersion |
| `sec-ell-adic-coefficients-2` | `sec-Integral-constructible-complexes` | Integral constructibility criterion: derived complete with constructible reduction. | prose-06-19, proof of proposition-direct-image-along-open-immersion |
| `sec-ell-adic-coefficients-2` | `sec-Integral-models` | 'rational complexes are built from integral ones (Lemma integral-models(4))' | prose-06-19 |
| `sec-ell-adic-coefficients-2` | `sec-Generic-base-change` | Mod pi_E reduction of Rj_*K is bounded constructible by Corollary open-direct-image-over-field. | proof of proposition-direct-image-along-open-immersion |
| `subsec-The-projective-line` | `sec-Repleteness-and-limits` | Repleteness and exact products make Rlim of the system the derived ell-completion. | proof of proposition-ell-adic-cycle-class-diagonal |
| `subsec-The-projective-line` | `sec-Left-completeness-and-hypercovers` | Passage to E, Qbar via colimits by continuity of cohomology. | proof of proposition-ell-adic-cycle-class-diagonal |
| `subsec-The-projective-line` | `subsec-Inverse-image` | Base change: pullback commutes with Rlim (Lemma inverse-image-coefficient-sheaves). | proof of proposition-ell-adic-cycle-class-diagonal |
| `subsec-The-projective-line` | `sec-Field-coefficients` | D^b_c closed under tensor product by the dévissage of Corollary coefficient-heart-b. | proof of proposition-projection-formula-rational-coefficients |
| `subsec-The-projective-line` | `sec-Proper-direct-image` | The projection formula on D^b_c is extended to the localizing categories. | proof of proposition-projection-formula-rational-coefficients |
| `subsec-The-projective-line` | `subsec-Construction-of-Rf` | Proper base change on Loc(D^b_ctf) and checking isomorphisms on D^b_ctf. | prose-06-21, proof of proposition-projection-formula-rational-coefficients, proof of proposition-projective-line-rational-coefficients |
| `subsec-The-projective-line` | `sec-Brown-representability` | Identifies q^! of Theorem existence-exceptional-inverse-image with q^*(1)[2]. | proposition-projective-line-rational-coefficients |
| `subsec-The-projective-line` | `sec-Duality-for-the-projective-line` | Lifts cycle class of the diagonal and trace to O_E and reruns the torsion proof of the P^1 adjunction. | prose-06-20, proposition-ell-adic-cycle-class-diagonal, proof of proposition-projective-line-rational-coefficients |
| `subsec-Finiteness-of-f` | `sec-Continuity-of-Ext` | i^! = RGamma_Z since RGamma_Z is right adjoint to i_*. | prose-06-23 |
| `subsec-Finiteness-of-f` | `sec-Proper-direct-image` | Projection formula on D^b_c, extended to localizing categories. | proof of lemma-projection-formula-integral-coefficients |
| `subsec-Finiteness-of-f` | `subsec-Integral-coefficients` | Rp_* preserves direct sums for O_E; inverse image and tensor preserve D^b_c(-,O_E). | prose-06-24, proof of lemma-projection-formula-integral-coefficients, proof of theorem-f-shriek-ell-adic-coefficients |
| `subsec-Finiteness-of-f` | `subsec-Construction-of-Rf` | Proper base change on Loc, checking isomorphisms, Rf_! preserves D^b_c. | proof of theorem-f-shriek-ell-adic-coefficients, proof of lemma-projection-formula-integral-coefficients |
| `subsec-Finiteness-of-f` | `sec-Composition-and-restriction` | u^*f^! = i^!p^!v^* by composition and open restriction. | proof of theorem-f-shriek-ell-adic-coefficients |
| `subsec-Finiteness-of-f` | `sec-Finite-coefficients-2` | Repeats the argument for finite coefficients with O_E, E, Qbar. | prose-06-25, proof of theorem-f-shriek-ell-adic-coefficients |
| `subsec-Finiteness-of-f` | `subsec-The-projective-line` | Adjunction for P^1 with l-adic coefficients and projection formula with rational coefficients. | proof of theorem-f-shriek-ell-adic-coefficients, proof of lemma-projection-formula-integral-coefficients |
| `sec-Proof-of-the-theorem` | `sec-Existence-and-finiteness-of-f` | Proves Theorem exceptional-inverse-image stated there by collecting references. | prose-06-26, proof of theorem-exceptional-inverse-image |
| `sec-Proof-of-the-theorem` | `sec-Direct-image-with-compact-support` | Part (2): construction of Rf_!, resting on proper direct image preserving sums (Direct sums, Integral coefficients). | proof of theorem-exceptional-inverse-image |
| `sec-Proof-of-the-theorem` | `sec-Brown-representability` | Parts (1) and (3): Lemma hypotheses-brown-representability and Theorem existence-exceptional-inverse-image. | proof of theorem-exceptional-inverse-image |
| `sec-Proof-of-the-theorem` | `sec-Finite-coefficients-2` | Part (4) for finite A is Theorem f-shriek-finite-coefficients. | proof of theorem-exceptional-inverse-image |
| `sec-Proof-of-the-theorem` | `subsec-Finiteness-of-f` | Part (4) for O_E, E, Qbar is Theorem f-shriek-ell-adic-coefficients. | proof of theorem-exceptional-inverse-image |
| `sec-Stability-of-Dbctf` | `sec-Constructibility` | Stability of D^b_ctf under operations follows 'from Definition constructible-sheaves: on each stratum such a sheaf is locally Λ⊗P' | proof of proposition-six-operations-dctf |
| `sec-Stability-of-Dbctf` | `sec-Finite-Tor-amplitude` | Tensor products and Hom reduce to the local description Lambda_S⊗P and the bounded flat models of Lemma flat-models-generators. | proposition-six-operations-dctf (proof), prose-07-01 |
| `sec-Stability-of-Dbctf` | `sec-Proper-direct-image` | 'Proper direct image preserves D^b_ctf by Proposition proper-direct-image-constructible-complexes' | proof of proposition-six-operations-dctf |
| `sec-Stability-of-Dbctf` | `subsec-Integral-coefficients` | Pullback and tensor preserve D^b_c(-,O_E) by Lemma inverse-image-tensor-product. | proof of proposition-six-operations-dctf |
| `sec-Stability-of-Dbctf` | `sec-Finite-coefficients-2` | Open direct image preserves D^b_ctf for finite A. | proof of proposition-six-operations-dctf |
| `sec-Stability-of-Dbctf` | `sec-ell-adic-coefficients-2` | Open direct image preserves D^b_c for O_E, E, Qbar. | proof of proposition-six-operations-dctf |
| `sec-Stability-of-Dbctf` | `sec-Proof-of-the-theorem` | f^! preserves D^b_ctf, part of the theorem now controlled (Section Proof of the theorem). | prose-07-01, proof of proposition-six-operations-dctf |
| `sec-Stability-of-Dbctf` | `sec-Compactifications` | Rf_* = Rp_*Rj_* for a compactification f=pj separates the proper and the open part. | proposition-six-operations-dctf (proof), prose-07-02 |
| `sec-Change-of-coefficients` | `sec-Left-completeness-and-hypercovers` | For O_E→E and E→Qbar, Rf_* commutes with uniformly bounded below colimits (Corollary continuity-cohomology). | lemma-change-coefficients-direct-image (proof) |
| `sec-Change-of-coefficients` | `sec-Descent-to-a-finite-extension` | D^b_ctf(X,Qbar) as 2-colimit: 'Both are parts of Lemma descent-finite-coefficient-field' | proof of proposition-dctf-x-qbar-2-colimit, prose-07-08 |
| `sec-Change-of-coefficients` | `sec-Compactness-for-finite-coefficients` | For maps of finite rings the Rf_* comparison is computed on the étale site via Proposition comparison-etale-derived-category. | lemma-change-coefficients-direct-image (proof) |
| `sec-Change-of-coefficients` | `subsec-Construction-of-Rf` | Comparison for Rf_! uses compactifications, independence (as in construction-independence-rf-shriek) and composition isomorphisms for Rf_!. | lemma-change-coefficients-compact-support (proof), prose-07-06 |
| `sec-Change-of-coefficients` | `sec-Duality-for-the-projective-line` | f^! for P^1 is q^*(1)[2] via the trace/diagonal adjunction, which commutes with change of coefficients by construction. | lemma-change-coefficients-exceptional-inverse-image (proof) |
| `sec-Change-of-coefficients` | `subsec-The-projective-line` | The integral cycle class of the diagonal and trace are compatible with change of coefficients. | lemma-change-coefficients-exceptional-inverse-image (proof) |
| `sec-Change-of-coefficients` | `sec-Proof-of-the-theorem` | f^!K in D^b_ctf by the theorem, needed to define beta_{f,K}. | prose-07-06 |
| `sec-Change-of-coefficients` | `sec-Stability-of-Dbctf` | Comparisons are stated on Dctf; internal Hom is reduced to Ra_*(P^∨⊗a^!L) 'as in the proof of Proposition six-operations-dctf'. | lemma-change-coefficients-internal-hom (proof) |
| `sec-Reduction-to-finite-coefficients` | `sec-Extension-by-zero-and-completion` | Derived Nakayama reduces C=0 to C/pi_E=0 in the main reduction proposition. | proof of proposition-isomorphisms-reduce-finite-coefficients |
| `sec-Reduction-to-finite-coefficients` | `sec-Integral-constructible-complexes` | F(K),G(K) in Dbc(O_E) are derived π_E-complete by the integral criterion | proof of proposition-isomorphisms-reduce-finite-coefficients |
| `sec-Reduction-to-finite-coefficients` | `sec-Integral-models` | Every object of Dbc(X,E) is built by cones from K_0[1/ell] (Lemma integral-models (4)). | proposition-isomorphisms-reduce-finite-coefficients (proof) |
| `sec-Reduction-to-finite-coefficients` | `sec-Change-of-coefficients` | Hypothesis of the principle holds by Proposition six-operations-change-coefficients; the Qbar step uses the 2-colimit. | proposition-isomorphisms-reduce-finite-coefficients (+proof), prose-07-10 |
| `sec-The-base-change-map-2` | `sec-The-base-change-map` | 'The base change map g^*Rf_*K→Rf'_*g'^*K is the map (4.5) of Section The-base-change-map' | prose-08-02 |
| `sec-Torsion-sheaves` | `sec-Direct-images` | Both sides and the base change map are transported to the étale site by Theorem comparison-direct-images. | prose-08-04 |
| `sec-Torsion-sheaves` | `sec-The-base-change-map` | Lemma naturality-pasting-comparison identifies base change map with inverse image of étale one | prose-08-04 |
| `sec-Torsion-sheaves` | `sec-The-base-change-map-2` | The theorem is stated for the square (8.1) and the map (4.5) fixed there. | theorem-smooth-base-change-classical-torsion |
| `sec-Degree-zero` | `sec-The-base-change-map-2` | The degree-zero lemma concerns the square (8.1) with g flat with geometrically reduced fibres. | lemma-degree-zero-calculation |
| `sec-The-induction-hypothesis` | `sec-Torsion-sheaves` | BC(g,n,r) is set up to prove the torsion theorem; a sheaf F as in the theorem is reduced to Z/n-modules. | prose-08-06 |
| `sec-Reduction-to-curves` | `sec-The-induction-hypothesis` | All lemmas assume BC(g,n,q-1) and move a failure of BC(g,n,q); g affine smooth of relative dimension one. | prose-08-07, lemma-injectivity-base-change-map-degree, lemma-reduction-curve-over-normal-base |
| `sec-Change-of-base-field` | `sec-Direct-images` | Work on the étale site since direct images along qcqs maps compare (Theorem comparison-direct-images). | proposition-base-change-larger-algebraically-closed (proof), theorem-smooth-base-change-classical-torsion (proof) |
| `sec-Change-of-base-field` | `sec-Constructible-sheaves` | Lemma torsors-under-classical-groups: the H^1 class is a finite étale Z/m-torsor. | proposition-base-change-larger-algebraically-closed (proof) |
| `sec-Change-of-base-field` | `subsec-Henselian-pairs-and-curves` | Uses (C_2) and (C_6) of Theorem cohomology-curves for curves over algebraically closed fields | prose-08-12, proof of proposition-base-change-larger-algebraically-closed |
| `sec-Change-of-base-field` | `sec-Torsion-sheaves` | Contains the proof of Theorem smooth-base-change-classical-torsion stated there, transferred to the pro-étale site. | theorem-smooth-base-change-classical-torsion (proof) |
| `sec-Change-of-base-field` | `sec-Degree-zero` | The degree-zero case starting the induction is Lemma degree-zero-calculation. | theorem-smooth-base-change-classical-torsion (proof) |
| `sec-Change-of-base-field` | `sec-The-induction-hypothesis` | Induction via BC(g,n,q-1), étale coordinates and composition reduce to affine g of relative dimension one. | theorem-smooth-base-change-classical-torsion (proof) |
| `sec-Change-of-base-field` | `sec-Reduction-to-curves` | A failure gives R^qh_*Z/m≠0 by Lemma reduction-curve-over-normal-base, contradicted by the proposition. | prose-08-12, theorem-smooth-base-change-classical-torsion (proof) |
| `sec-Bounded-below-complexes` | `sec-Comparison-with-the-etale-site` | Corollary bounded-below-classical-complexes: the direct and inverse images involved are classical. | theorem-smooth-base-change-classical-torsion-2 (proof) |
| `sec-Bounded-below-complexes` | `sec-Direct-images` | Theorem comparison-direct-images lets one argue with hypercohomology spectral sequences on the étale sites. | theorem-smooth-base-change-classical-torsion-2 (proof) |
| `sec-Bounded-below-complexes` | `sec-The-base-change-map` | Lemma naturality-pasting-comparison identifies the comparison with (4.5). | theorem-smooth-base-change-classical-torsion-2 (proof) |
| `sec-Bounded-below-complexes` | `sec-The-base-change-map-2` | Statement for complexes in the square (8.1) with the map (4.5) on D^+_class. | theorem-smooth-base-change-classical-torsion-2 |
| `sec-Bounded-below-complexes` | `sec-Change-of-base-field` | For a classical sheaf the assertion is the torsion theorem, whose proof is completed in Change of base field. | theorem-smooth-base-change-classical-torsion-2 (proof) |
| `sec-ell-adic-coefficients-3` | `sec-Constructible-sheaves` | For finite A, K is classical by Theorem comparison-constructible-sheaves. | theorem-smooth-base-change-all-admissible (proof) |
| `sec-ell-adic-coefficients-3` | `sec-Stability-of-Dbctf` | Both sides lie in Dctf(Y',Lambda) by Proposition six-operations-dctf. | theorem-smooth-base-change-all-admissible (proof) |
| `sec-ell-adic-coefficients-3` | `sec-Change-of-coefficients` | Lemma change-coefficients: the base change map commutes with the comparisons of Proposition six-operations-change-coefficients. | lemma-change-coefficients (+proof) |
| `sec-ell-adic-coefficients-3` | `sec-Reduction-to-finite-coefficients` | Other rings follow by Proposition isomorphisms-reduce-finite-coefficients applied to the base change map. | theorem-smooth-base-change-all-admissible (proof) |
| `sec-ell-adic-coefficients-3` | `sec-The-base-change-map-2` | Theorem stated for the square (8.1) and map (4.5); compatibilities of the base change map recalled there. | theorem-smooth-base-change-all-admissible, prose-08-02 |
| `sec-ell-adic-coefficients-3` | `sec-Bounded-below-complexes` | For finite A the theorem is smooth base change for torsion complexes. | prose-08-16, theorem-smooth-base-change-all-admissible (proof) |
| `sec-The-Kunneth-formula` | `sec-Direct-images` | Arguments on the étale site transported by Theorem comparison-direct-images. | lemma-base-change-along-product-projection (proof), lemma-kunneth-field-coefficients (proof) |
| `sec-The-Kunneth-formula` | `sec-Constructible-sheaves` | Small étale models of constructible complexes (Theorem comparison-constructible-sheaves). | lemma-kunneth-field-coefficients (proof), lemma-kunneth-one-identity-factor (proof) |
| `sec-The-Kunneth-formula` | `sec-The-base-change-map` | Lemma identity-pasting: the composite of the two base change maps is the one for f. | lemma-base-change-along-product-projection (proof) |
| `sec-The-Kunneth-formula` | `sec-Proper-morphisms` | Proper base change for f̄ applied to Rj_*M on the étale site. | lemma-base-change-along-product-projection (proof) |
| `sec-The-Kunneth-formula` | `sec-Stability-of-Dbctf` | Source and target of the Künneth map lie in Dctf; Rf_{2*}M_2 in Dctf. | lemma-kunneth-one-identity-factor (proof), proposition-ordinary-external-kunneth (proof) |
| `sec-The-Kunneth-formula` | `sec-Change-of-coefficients` | Reduction modulo maximal ideals via change-of-coefficients maps respecting the counit. | lemma-kunneth-one-identity-factor (proof) |
| `sec-The-Kunneth-formula` | `sec-Bounded-below-complexes` | Base change along a product projection uses base change under extension of the ground field, a consequence of smooth base change for torsion complexes. | lemma-base-change-along-product-projection (proof) |
| `sec-The-Kunneth-formula` | `sec-Compactifications` | Compactify f=f̄j (Nagata) so that only an open immersion and a proper map remain. | lemma-base-change-along-product-projection (proof) |
| `sec-Statement` | `subsec-Coefficient-sheaves` | Smooth purity is stated with the Tate twists Lambda_X(d) for admissible coefficient rings. | prose-09-02 |
| `sec-Statement` | `subsec-Construction-of-Rf` | Exceptional base change map uses the base change isomorphism of Proposition composition-base-change-rf-shriek(2). | definition-exceptional-base-change-map |
| `sec-Statement` | `sec-Composition-and-restriction` | Property (3) uses the composition isomorphism f^!h^!≃(hf)^! of Proposition composition-open-restriction-compactifications-f. | theorem-smooth-purity-all-admissible-coefficients |
| `sec-Statement` | `sec-Duality-for-the-projective-line` | Trace map of A^1 (9.1) uses Tr_q of Lemma cohomology-projective-line-trace for finite Lambda. | definition-trace-map-affine-line |
| `sec-Statement` | `subsec-The-projective-line` | For l-adic Lambda, Tr_q is the trace of Proposition ell-adic-cycle-class-diagonal. | definition-trace-map-affine-line |
| `sec-Statement` | `sec-Proof-of-the-theorem` | 'The functors are those of Theorem exceptional-inverse-image, restricted to Dctf'; counit of Rf_!⊣f^!. | prose-09-02 |
| `sec-Statement` | `sec-Change-of-coefficients` | Property (4) is stated through the change-of-coefficients isomorphisms for f^! and f^*. | theorem-smooth-purity-all-admissible-coefficients |
| `sec-The-tensor-product-map` | `sec-Smooth-morphisms` | The map (9.4) and exceptional base change (9.6) are isomorphisms by Proposition exceptional-inverse-image-smooth-morphism(2),(3); local form on charts. | prose-09-07 |
| `sec-The-tensor-product-map` | `sec-Statement` | Uses omega_f (9.3) and the exceptional base change map of Definition exceptional-base-change-map. | prose-09-07 |
| `sec-The-trace-map-of-affine-space` | `sec-Compactness-for-finite-coefficients` | Pro-étale and étale Dctf identified (Proposition comparison-etale-derived-category), so f^! is the classical one and computed on étale sites. | prose-09-09 |
| `sec-The-trace-map-of-affine-space` | `sec-Conventions-2` | Geometric computations with finite coefficients of Section Conventions-2 (projection formula, f^! on D_class). | prose-09-09 |
| `sec-The-trace-map-of-affine-space` | `sec-Duality-for-the-projective-line` | Splitting (9.8), Tr_q, the diagonal class (9.9) and the adjunction Rq_*⊣q^*(1)[2] of Proposition adjunction-projective-line. | prose-09-08 |
| `sec-The-trace-map-of-affine-space` | `sec-Smooth-morphisms` | Rp_d!⊣p_d^*(d)[2d] (Lemma affine-space-etale-localization) and the chart form of f^! (Proposition exceptional-inverse-image-smooth-morphism(1)). | prose-09-08, prose-09-09, proposition-purity-vector-bundles (proof) |
| `sec-The-trace-map-of-affine-space` | `sec-Statement` | The counit at the constant sheaf is the trace map of the affine line (9.1). | prose-09-08 |
| `sec-Finite-coefficients-3` | `sec-Smooth-morphisms` | Proposition exceptional-inverse-image-smooth-morphism (1),(3): omega's are locally constant and satisfy base change. | lemma-section-normal-bundle (proof), proposition-relative-dualizing-complex (proof) |
| `sec-Finite-coefficients-3` | `sec-Statement` | Constructs gamma_f of the theorem with finite coefficients, compatible with base change as property (2) requires; uses omega_f. | prose-09-13, prose-09-16 |
| `sec-Finite-coefficients-3` | `sec-The-tensor-product-map` | gamma_{f,A} is the orientation composed with the isomorphism (9.4). | proposition-smooth-purity-finite-coefficients (proof), prose-09-16 |
| `sec-Finite-coefficients-3` | `sec-The-trace-map-of-affine-space` | The orientation of omega_f ends with purity for vector bundles applied to T_{X/Y}; agreement with (9.11) on charts. | proposition-relative-dualizing-complex (proof), prose-09-11, prose-09-16 |
| `subsec-Change-of-finite-coefficients` | `sec-Finite-Tor-amplitude` | For R f̄_* one resolves B by free A-modules and uses the flat models of Lemma flat-models-generators. | lemma-sp-reduction (proof) |
| `subsec-Change-of-finite-coefficients` | `sec-Duality-for-the-projective-line` | On charts the counit is built from the trace of P^1, which commutes with extension of coefficients. | lemma-sp-reduction (proof) |
| `subsec-Change-of-finite-coefficients` | `sec-Smooth-morphisms` | Invertibility of c_{A,B} checked on a chart f\|_U=p_d∘e of Proposition exceptional-inverse-image-smooth-morphism(1). | lemma-sp-reduction (proof) |
| `subsec-Change-of-finite-coefficients` | `sec-Change-of-coefficients` | The comparison b for Rf_! is the change of coefficients of Proposition six-operations-change-coefficients. | lemma-sp-reduction (proof) |
| `subsec-Change-of-finite-coefficients` | `sec-The-tensor-product-map` | The map (9.4) commutes with change of coefficients. | prose-09-20 |
| `subsec-Change-of-finite-coefficients` | `sec-The-trace-map-of-affine-space` | Orientation compatibility for vector bundles follows from the P^1 construction (Proposition purity-vector-bundles, splitting (9.8)). | prose-09-20 |
| `subsec-Change-of-finite-coefficients` | `sec-Finite-coefficients-3` | (9.17): gamma_{f,A} commutes with change of coefficients, using the uniqueness in Lemma section-normal-bundle. | prose-09-20 |
| `subsec-Integral-coefficients-2` | `sec-Integral-constructible-complexes` | Limits of normalized towers are in Dbc by the criterion of Proposition integral-constructibility-criterion. | proposition-sp-integral-towers (proof) |
| `subsec-Integral-coefficients-2` | `subsec-Integral-coefficients` | Uniform bounds for reductions from Lemma structure-integral-constructible-complexes. | proposition-sp-integral-towers (proof) |
| `subsec-Integral-coefficients-2` | `sec-Brown-representability` | H_{f,O_E} is identified with the right adjoint of Theorem existence-exceptional-inverse-image. | proposition-sp-integral-adjunction |
| `subsec-Integral-coefficients-2` | `sec-Stability-of-Dbctf` | Each level of Rf_{!,•} lies in Dctf by Proposition six-operations-dctf. | prose-09-23 |
| `subsec-Integral-coefficients-2` | `sec-The-tensor-product-map` | gamma_{f,•} composes the inverse orientation with the map (9.4) on towers. | prose-09-24 |
| `subsec-Integral-coefficients-2` | `sec-The-trace-map-of-affine-space` | The adjunction on towers repeats the construction of that section, gluing representing pairs via (9.12). | proposition-sp-tower-geometric (proof) |
| `subsec-Integral-coefficients-2` | `sec-Finite-coefficients-3` | Orientation passes to towers; uniqueness of Lemma section-normal-bundle levelwise; levels are gamma_{f,O_E/l^n}. | prose-09-24 |
| `subsec-Integral-coefficients-2` | `subsec-Change-of-finite-coefficients` | Reduction maps of f^!_• are built from the comparisons c of Lemma sp-reduction; normalized towers via (9.17). | proposition-sp-tower-geometric, prose-09-24 |
| `subsec-Field-coefficients` | `sec-Inverting-ell` | 'Both statements are Proposition inverting-ell: essential surjectivity provides the models, (9.21) is full faithfulness' | prose-09-26 |
| `subsec-Field-coefficients` | `sec-Change-of-coefficients` | Dbc(T,Qbar) is the 2-colimit of the Dbc(T,F); Rf_! and f^* commute with extension of scalars. | theorem-sp-qbar (proof) |
| `subsec-Field-coefficients` | `subsec-Change-of-finite-coefficients` | Extended pairs of towers represent Hom(Rf_!(-),K_n) by Lemma sp-reduction, so adjunctions over E⊂F correspond. | prose-09-27 |
| `subsec-Field-coefficients` | `subsec-Integral-coefficients-2` | The adjunction over E is the integral adjunction of Proposition sp-integral-adjunction with l inverted. | proposition-sp-rational (proof), prose-09-26 |
| `subsec-Base-change-and-composition` | `subsec-Construction-of-Rf` | red carries the base change and composition isomorphisms of Proposition composition-base-change-rf-shriek to towers. | prose-09-30 |
| `subsec-Base-change-and-composition` | `sec-Composition-and-restriction` | The integral composition isomorphisms are those of Proposition composition-open-restriction-compactifications-f(1). | prose-09-31 |
| `subsec-Base-change-and-composition` | `sec-Smooth-morphisms` | Finite exceptional base change isomorphisms are Proposition exceptional-inverse-image-smooth-morphism(3). | prose-09-30 |
| `subsec-Base-change-and-composition` | `sec-Change-of-coefficients` | Change-of-coefficients maps (Lemma change-coefficients-direct-image, Proposition six-operations-change-coefficients) carry units, counits and base change maps. | prose-09-30 |
| `subsec-Base-change-and-composition` | `sec-Statement` | Shows the limit maps are the exceptional base change map of Definition exceptional-base-change-map; proves properties (2),(3). | prose-09-30, proposition-compatibility-purity-base-change |
| `subsec-Base-change-and-composition` | `sec-The-tensor-product-map` | Both propositions compare the orientations and the maps (9.4). | proposition-compatibility-purity-base-change (proof), proposition-compatibility-purity-composition (proof) |
| `subsec-Base-change-and-composition` | `sec-The-trace-map-of-affine-space` | Composition: on adapted charts both orientations are the iterated integration preceding (9.11). | proposition-compatibility-purity-composition (proof) |
| `subsec-Base-change-and-composition` | `sec-Finite-coefficients-3` | Orientation commutes with base change by Lemma naturality-under-base-change-etale(1). | proposition-compatibility-purity-base-change (proof) |
| `subsec-Base-change-and-composition` | `subsec-Change-of-finite-coefficients` | Integral and rational base change and composition isomorphisms start from Lemma sp-reduction. | subsec-Base-change-and-composition proofs |
| `subsec-Base-change-and-composition` | `subsec-Integral-coefficients-2` | They are built from the tower adjunction for O_E. | subsec-Base-change-and-composition proofs |
| `subsec-Base-change-and-composition` | `subsec-Field-coefficients` | The rational and Qbar cases use Proposition sp-rational and Theorem sp-qbar. | subsec-Base-change-and-composition proofs |
| `subsec-The-trace-map` | `sec-The-trace-map-of-affine-space` | For A^d the trace map is the trace map of affine space (9.11). | remark-trace-map-special-cases, prose-09-33 |
| `subsec-The-trace-map` | `subsec-Base-change-and-composition` | Transitivity of the trace map: the maps gamma compose by Proposition compatibility-purity-composition. | proposition-transitivity-trace-map (proof) |
| `subsec-Change-of-coefficients` | `sec-Change-of-coefficients` | Identifies c_{A,B} and the tower comparisons with the change-of-coefficients maps for f^! of Proposition six-operations-change-coefficients. | prose-09-34, proposition-compatibility-purity-change-coefficients (proof) |
| `subsec-Change-of-coefficients` | `subsec-Change-of-finite-coefficients` | Uses (9.16), (9.17) of Lemma sp-reduction. | proposition-compatibility-purity-change-coefficients.proof |
| `subsec-Change-of-coefficients` | `subsec-Integral-coefficients-2` | Uses the tower construction of gamma_{f,O_E}. | proposition-compatibility-purity-change-coefficients.proof |
| `subsec-Change-of-coefficients` | `subsec-Field-coefficients` | Extension of scalars from finite extensions of Q_l (Section subsec-Field-coefficients). | proposition-compatibility-purity-change-coefficients.proof |
| `subsec-Change-of-coefficients` | `subsec-Base-change-and-composition` | The integral counit reduces to level n of the counit on towers (comparison of red established there). | proposition-compatibility-purity-change-coefficients (proof) |
| `sec-Proof-of-smooth-purity` | `sec-Extension-by-zero-and-completion` | Derived Nakayama gives that the cone of Tr_p vanishes. | theorem-smooth-purity-all-admissible-coefficients (proof) |
| `sec-Proof-of-smooth-purity` | `subsec-The-projective-line` | The integral trace of Proposition ell-adic-cycle-class-diagonal lifts the finite ones. | theorem-smooth-purity-all-admissible-coefficients (proof) |
| `sec-Proof-of-smooth-purity` | `sec-Statement` | Proves Theorem smooth-purity-all-admissible-coefficients stated there, including the trace normalization (1) with (9.1). | theorem-smooth-purity-all-admissible-coefficients (proof), prose-09-35 |
| `sec-Proof-of-smooth-purity` | `sec-The-trace-map-of-affine-space` | The trace map with Z/l coefficients is an isomorphism, so Tr_p is invertible integrally. | theorem-smooth-purity-all-admissible-coefficients (proof) |
| `sec-Proof-of-smooth-purity` | `sec-Finite-coefficients-3` | gamma_{f,A} for finite A; property (1) from the comparison after Proposition relative-dualizing-complex. | theorem-smooth-purity-all-admissible-coefficients (proof) |
| `sec-Proof-of-smooth-purity` | `sec-ell-adic-coefficients-4` | gamma_f for O_E, E, Qbar from Propositions sp-integral-adjunction, sp-rational, Theorem sp-qbar and sp-unique-adjoint. | theorem-smooth-purity-all-admissible-coefficients (proof) |
| `sec-Proof-of-smooth-purity` | `subsec-Integral-coefficients-2` | gamma_f for O_E is built by the tower adjunction (Proposition sp-integral-adjunction). | theorem-smooth-purity-all-admissible-coefficients.proof |
| `sec-Proof-of-smooth-purity` | `subsec-Field-coefficients` | gamma_f for E and Qbar comes from Proposition sp-rational and Theorem sp-qbar. | theorem-smooth-purity-all-admissible-coefficients.proof |
| `sec-Proof-of-smooth-purity` | `subsec-Base-change-and-composition` | Properties (2) and (3) of smooth purity are the base change and composition compatibilities proved there. | theorem-smooth-purity-all-admissible-coefficients.proof |
| `sec-Proof-of-smooth-purity` | `subsec-The-trace-map` | The trace part of the theorem (1) comes from the trace map of the Compatibilities section. | theorem-smooth-purity-all-admissible-coefficients.proof |
| `sec-Proof-of-smooth-purity` | `subsec-Change-of-coefficients` | Property (4) is Proposition compatibility-purity-change-coefficients. | theorem-smooth-purity-all-admissible-coefficients.proof |
| `sec-Exchange-formulas` | `sec-Continuous-cohomology` | 'By the comparisons of Section Continuous cohomology', global sections identify D^b_ctf of a geometric point. | proof of lemma-perfect-complexes-geometric-point |
| `sec-Exchange-formulas` | `sec-Existence-and-finiteness-of-f` | ω_X=a_X^!Λ and both exchange formulas rest on the adjunction Rf_!⊣f^! on the localizing categories Loc(Dctf). | definition-verdier-dual-evaluation; proof of lemma-internal-adjunction-two-exchange-formulas |
| `sec-Exchange-formulas` | `sec-Compactness-for-finite-coefficients` | For finite coefficients the projection formula follows from the comparison with the étale derived category. | proof of lemma-internal-adjunction-two-exchange-formulas |
| `sec-Exchange-formulas` | `sec-ell-adic-coefficients-2` | Projection formula needed in the Yoneda computation: rational case Prop. projection-formula-rational, integral case Lemma projection-formula-integral. | proof of lemma-internal-adjunction-two-exchange-formulas |
| `sec-Exchange-formulas` | `sec-Stability-of-Dbctf` | Direct images and pullback preserve Dctf (Proposition six-operations-dctf): perfect stalks, pullback preserves Loc, Yoneda in Loc. | lemma-perfect-complexes-geometric-point (proof), lemma-internal-adjunction-two-exchange-formulas (proof) |
| `sec-Verdier-biduality` | `sec-Left-completeness-and-hypercovers` | Direct image commutes with passage to the geometric generic fibre by continuity of cohomology (Corollary continuity-cohomology). | proof of lemma-restriction-geometric-generic-fibre |
| `sec-Verdier-biduality` | `sec-Finite-Tor-amplitude` | Dévissage of K to generators t_!P uses the bounded flat models of Lemma flat-models-generators; reused for internal Hom comparison. | proof of lemma-verdier-duality-preserves-constructibility; proof of lemma-restriction-geometric-generic-fibre |
| `sec-Verdier-biduality` | `sec-Compactness-for-finite-coefficients` | With finite coefficients Dctf and direct images are computed by their classical étale counterparts (comparison proposition). | proof of lemma-restriction-geometric-generic-fibre |
| `sec-Verdier-biduality` | `sec-Stability-of-Dbctf` | Verdier duality preserves constructibility because a_X^! and internal Hom preserve Dctf. | lemma-verdier-duality-preserves-constructibility (proof) |
| `sec-Verdier-biduality` | `sec-Change-of-coefficients` | Proposition six-operations-change-coefficients identifies the extensions of scalars of the biduality map. | theorem-verdier-biduality (proof) |
| `sec-Verdier-biduality` | `sec-Reduction-to-finite-coefficients` | The finite case of biduality implies it for every admissible Lambda by the reduction principle. | theorem-verdier-biduality (proof) |
| `sec-Verdier-biduality` | `sec-Statement` | Smooth purity identifies D_T P on smooth strata and gives ω_X≃i^!A(r+1)[2r+2], producing the twist (1)[2] on the generic fibre. | proof of lemma-verdier-duality-preserves-constructibility; proof of lemma-double-dual-geometric-generic-fibre |
| `sec-Verdier-biduality` | `sec-Proof-of-smooth-purity` | Smooth purity identifies D_T P with P^∨(r)[2r] on smooth strata and computes f^! on A^r. | lemma-verdier-duality-preserves-constructibility (proof), lemma-double-dual-geometric-generic-fibre (proof) |
| `sec-Verdier-biduality` | `sec-Exchange-formulas` | Biduality proof: dimension-zero case is the perfect-complex lemma; R Γ(X,δ_K) identified with double dual via the proper exchange formula; corollary dualizes (10.3),(10.4). | proof of theorem-verdier-biduality; proof of corollary-verdier-exchange-formulas |
| `sec-Poincare-duality` | `sec-Change-of-coefficients` | Compatibility of the pairing with change of coefficients via Proposition six-operations-change-coefficients. | theorem-poincare-duality (+proof) |
| `sec-Poincare-duality` | `sec-Statement` | Smooth purity theorem gives ω_X≃Λ(d)[2d] and D_XK≃K^∨(d)[2d], and its compatibility with coefficient change. | theorem-poincare-duality; proof of theorem-poincare-duality |
| `sec-Poincare-duality` | `subsec-The-trace-map` | The Poincaré pairing uses Tr_X induced by the trace map of a_X. | theorem-poincare-duality (+proof), prose-10-11 |
| `sec-Poincare-duality` | `sec-Proof-of-smooth-purity` | omega_X≃Lambda_X(d)[2d] by Corollary dualizing-complex-smooth-scheme / smooth purity. | theorem-poincare-duality (+proof), prose-10-13 |
| `sec-Poincare-duality` | `sec-Exchange-formulas` | Perfect-complex lemma identifies D_s with RHom(-,Λ); the pairing comes from the construction of (10.3) via evaluation and counit. | proof of theorem-global-verdier-duality; proof of theorem-poincare-duality |
| `sec-Poincare-duality` | `sec-Verdier-biduality` | Global Verdier duality is the first two Verdier exchange formulas of Corollary verdier-exchange-formulas for f=a_X. | proof of theorem-global-verdier-duality; prose-10-12 |
| `sec-Cohomology-in-top-degree` | `sec-Change-of-coefficients` | Complexes and traces over A obtained from Z/l^n by derived extension of scalars. | theorem-trace-isomorphism-top-degree (proof) |
| `sec-Cohomology-in-top-degree` | `subsec-The-trace-map` | The trace isomorphism in top degree is the map induced by Tr_X of Definition trace-map. | theorem-trace-isomorphism-top-degree |
| `sec-Cohomology-in-top-degree` | `sec-Poincare-duality` | Top-degree trace isomorphism is read off from Poincaré duality in degree zero; cup product pairing from degreewise duality over fields. | proof of theorem-trace-isomorphism-top-degree; proof of corollary-cup-product-pairing |
| `sec-Frobenius-and-Poincare-duality` | `subsec-Base-change-and-composition` | gamma_f commutes with Frobenius: Proposition compatibility-purity-base-change for the Frobenius square. | proposition-purity-trace-commute-frobenius (proof) |
| `sec-Frobenius-and-Poincare-duality` | `subsec-The-trace-map` | The statement for Tr_f, the counit composed with gamma_f. | proposition-purity-trace-commute-frobenius (+proof) |
| `sec-Frobenius-and-Poincare-duality` | `sec-Poincare-duality` | The pairing β_K of (10.7) is shown Frobenius-equivariant; over fields degreewise duality gives the eigenvalue relation q^d/α. | theorem-poincare-duality-frobenius; proof of theorem-poincare-duality-frobenius |
| `sec-Frobenius-and-Poincare-duality` | `sec-Weil-complexes` | Theorem is stated for Weil complexes (Definition weil-structure) and Frobenius operators F; uses transport of Weil structures along f^!, f^*, Rf_!. | theorem-poincare-duality-frobenius; prose-10-23 |
| `sec-Correspondences` | `sec-Existence-and-finiteness-of-f` | A cohomological correspondence is u:c_2^*K→c_1^!K; pushing forward uses the counit of Rc_{1!}⊣c_1^!. | prose-11-06; definition-correspondence |
| `sec-The-exceptional-Kunneth-formula` | `sec-Finite-Tor-amplitude` | Dévissage to generators j_!F with lisse F of finite projective stalks via Lemma flat-models-generators. | proof of proposition-exceptional-external-kunneth; proof of lemma-external-duality-trace-morphism |
| `sec-The-exceptional-Kunneth-formula` | `subsec-Construction-of-Rf` | Künneth isomorphism for Rf_! is obtained from base change for compact supports and the projection formula; defines α. | prose-11-08 |
| `sec-The-exceptional-Kunneth-formula` | `sec-Stability-of-Dbctf` | Dévissage: the third term stays in Dctf by Proposition six-operations-dctf. | proposition-exceptional-external-kunneth (proof) |
| `sec-The-exceptional-Kunneth-formula` | `sec-The-Kunneth-formula` | Künneth for ordinary direct images (Proposition ordinary-external-kunneth) is an input of the Künneth formulas for Hom and Verdier duals. | prose-11-08, proposition-exceptional-external-kunneth (proof), lemma-external-duality-trace-morphism (proof) |
| `sec-The-exceptional-Kunneth-formula` | `sec-Statement` | Constant coefficients: smooth purity computes f_i^! as twisted pullbacks so both sides of α agree. | proof of proposition-exceptional-external-kunneth |
| `sec-The-exceptional-Kunneth-formula` | `subsec-The-trace-map` | alpha is identified via the compatibility of the trace map with products. | proposition-exceptional-external-kunneth (proof) |
| `sec-The-exceptional-Kunneth-formula` | `sec-Proof-of-smooth-purity` | For smooth f_i the exceptional Künneth map is computed by smooth purity f_i^!=f_i^*(d_i)[2d_i]. | proposition-exceptional-external-kunneth (proof) |
| `sec-The-exceptional-Kunneth-formula` | `sec-Verdier-biduality` | Exceptional exchange (Corollary verdier-exchange-formulas) for closed pushforward; Verdier exchange and biduality rewrite Hom(p_U^*M,p_V^!N) as a dual. | proof of proposition-exceptional-external-kunneth; proof of lemma-external-duality-trace-morphism |
| `sec-The-exceptional-Kunneth-formula` | `sec-Correspondences` | External duality is stated for a correspondence c; the trace morphism lands on the fixed locus Fix(c) via i_c, d_c. | lemma-external-duality-trace-morphism; definition-trace-morphism |
| `sec-Trace-classes-and-local-terms` | `sec-Exchange-formulas` | ρ_f: R(f×f)_*P_X≃P_Y uses the exchange D_YRf_*≃Rf_*D_X for proper f; evaluation compatibility since duality is defined by the counit. | proof of theorem-proper-pushforward-lefschetz-verdier |
| `sec-Trace-classes-and-local-terms` | `sec-Traces-of-perfect-complexes` | On the point the local term is the categorical trace; this gives the global side tr(T_c(u)) of Lefschetz–Verdier. | lemma-local-terms-point; prose-11-12; proof of theorem-proper-pushforward-lefschetz-verdier |
| `sec-Trace-classes-and-local-terms` | `sec-Correspondences` | T_c(u), pushforward of correspondences and local terms are defined for cohomological correspondences and their fixed loci. | definition-action-correspondence; definition-pushforward-correspondence; definition-trace-class-local-terms |
| `sec-Trace-classes-and-local-terms` | `sec-The-exceptional-Kunneth-formula` | Trace class: u is a section of c^!(K⊠D_XK) by external duality, composed with the trace morphism. | prose-11-11; definition-trace-class-local-terms; proof of lemma-local-terms-point |
| `sec-Additivity-of-trace-classes` | `sec-Correspondences` | Lifting a correspondence to an invariant open/closed decomposition restricts c to c_U, c_Z and uses Θ=Rc_{1!}c_2^*. | prose-11-18; lemma-lift-correspondence-invariant-decomposition |
| `sec-Additivity-of-trace-classes` | `sec-The-exceptional-Kunneth-formula` | The trace morphism of Definition trace-morphism and external duality are lifted to filtered complexes. | prose-11-17; proof of lemma-filtered-trace-morphism |
| `sec-Additivity-of-trace-classes` | `sec-Trace-classes-and-local-terms` | Additivity is for trace classes Tr_c(u); the closed piece is a pushforward of correspondences (Definition pushforward-correspondence). | proposition-additivity-trace-classes; lemma-closed-piece-pushforward |
| `sec-Frobenius-correspondences` | `sec-Weil-complexes` | Compares Φ_X with the semilinear Fr_X of Weil structures: T_{c_m}(ψ_m)=Frob_{X,K}^m (Definitions weil-structure, frobenius-operator). | lemma-scheme-frobenius-geometric-frobenius; prose-12-04 |
| `sec-Frobenius-correspondences` | `sec-Correspondences` | ψ_m is a cohomological correspondence for the graph c_m=(id,Φ_X^m). | definition-frobenius-correspondences-their-operators |
| `sec-Frobenius-correspondences` | `sec-Trace-classes-and-local-terms` | Operator of a Frobenius correspondence on R Γ_c is T_c of Definition action-correspondence. | definition-frobenius-correspondences-their-operators |
| `sec-Local-terms-on-a-curve` | `sec-Frobenius-correspondences` | The Frobenius fixed scheme Fix(Φ_X^m)=Fix(c_m) is the set of F_{q^m}-points, each with its own local term. | lemma-frobenius-fixed-scheme; prose-12-06 |
| `subsec-The-local-term-as-a-restriction-map` | `sec-The-exceptional-Kunneth-formula` | External duality identifies γ^!P with Hom((Φ^m)^*K,K); the evaluation adjoint is the map defining the trace morphism. | proof of lemma-local-term-restriction-map; prose-12-08 |
| `subsec-The-local-term-as-a-restriction-map` | `sec-Trace-classes-and-local-terms` | Rewrites the local term LT_y(ψ) of Definition trace-class-local-terms as a restriction map from Γ- to y-supported cohomology. | lemma-local-term-restriction-map; proof of lemma-local-term-restriction-map |
| `subsec-The-local-term-as-a-restriction-map` | `sec-Frobenius-correspondences` | The class [ψ] comes from a Frobenius correspondence ψ:(Φ_X^m)^*K→K on the graph of Φ_X^m. | lemma-local-term-restriction-map; prose-12-09 |
| `subsec-Vanishing-on-a-strictly-local-surface` | `sec-Proof-of-smooth-purity` | Purity identity i_{D_2}^!F_ℓ=F_ℓ(-1)[-2] obtained by transitivity from the dualizing complexes of the smooth schemes S and D_2. | proof of lemma-punctured-surface-punctured-curve |
| `subsec-Vanishing-on-a-strictly-local-surface` | `sec-Affine-curves` | Vanishing in degrees ≥2 on the punctured trait from Prop. cohomology-smooth-affine-curve. | proof of lemma-punctured-surface-punctured-curve |
| `subsec-The-local-term-at-a-zero-stalk` | `sec-Finite-Tor-amplitude` | Bounded finite projective lisse models of N and Q (Lemma flat-models-generators) to which the cover lemma is applied. | proof of lemma-vanishing-local-term-zero-stalk |
| `subsec-The-local-term-at-a-zero-stalk` | `sec-The-Kunneth-formula` | Ordinary external Künneth identifies P=(D_XK⊠K)\|_T with Rj_*j'_!(N⊠Q). | proof of lemma-vanishing-local-term-zero-stalk |
| `subsec-The-local-term-at-a-zero-stalk` | `sec-Exchange-formulas` | (D_XK)\|_{X_1}=Rj_{1*}N because the dual of an extension by zero is the direct image of the dual, (10.3) for j. | proof of lemma-vanishing-local-term-zero-stalk |
| `subsec-The-local-term-at-a-zero-stalk` | `subsec-The-local-term-as-a-restriction-map` | Vanishing of LT_y is proved by showing the restriction map ρ of Lemma local-term-restriction-map is zero. | lemma-vanishing-local-term-zero-stalk; prose-12-14; proof of lemma-vanishing-local-term-zero-stalk |
| `subsec-The-local-term-at-a-zero-stalk` | `subsec-Vanishing-on-a-strictly-local-surface` | On the cover the restriction r' vanishes by Lemma vanishing-restrictions-after-blowing-up. | proof of lemma-vanishing-local-term-zero-stalk |
| `subsec-The-local-term-at-a-fixed-point` | `sec-Trace-classes-and-local-terms` | Closed piece: local term is tr(ψ_ȳ\|K_ȳ) by compatibility with proper pushforward and Lemma local-terms-point. | proof of proposition-frobenius-local-term-curve |
| `subsec-The-local-term-at-a-fixed-point` | `sec-Additivity-of-trace-classes` | Splits ψ along X∖{y} and {y} by the second half of Prop. additivity-trace-classes; closed piece is a pushforward. | proof of proposition-frobenius-local-term-curve; prose-12-15 |
| `subsec-The-local-term-at-a-fixed-point` | `sec-Frobenius-correspondences` | Proposition concerns local terms of a Frobenius correspondence ψ:(Φ_X^m)^*K→K at a rational point. | proposition-frobenius-local-term-curve |
| `subsec-The-local-term-at-a-fixed-point` | `subsec-The-local-term-at-a-zero-stalk` | The open piece has zero stalk at y, so its local term vanishes by Lemma vanishing-local-term-zero-stalk. | proof of proposition-frobenius-local-term-curve; prose-12-15 |
| `sec-Frobenius-and-Rf` | `subsec-Construction-of-Rf` | θ_{f,m} is built from base change for compact supports and composition of Rf_!; fibres via base change. | lemma-comparison-via-relative-frobenius; proof of lemma-comparison-via-relative-frobenius |
| `sec-Frobenius-and-Rf` | `sec-Traces-of-perfect-complexes` | Traces add on the two-step filtered object R Γ_c of the localization triangle (Prop. properties-trace). | proof of lemma-additivity-open-subscheme-complement |
| `sec-Frobenius-and-Rf` | `sec-Frobenius-correspondences` | Rf_!K gets a Frobenius correspondence ψ' whose operator T_{c_m} matches that of ψ and whose stalks are fibre operators. | lemma-comparison-via-relative-frobenius |
| `sec-Finite-coefficients-4` | `sec-Stability-of-Dbctf` | L=Rf_!K lies in Dctf(Y,A) by Proposition six-operations-dctf. | theorem-trace-formula-frobenius-correspondence (proof) |
| `sec-Finite-coefficients-4` | `sec-Exchange-formulas` | Both sides are defined because R Γ_c and stalks are perfect (Lemma perfect-complexes-geometric-point). | proof of theorem-trace-formula-frobenius-correspondence |
| `sec-Finite-coefficients-4` | `sec-Trace-classes-and-local-terms` | On proper P^1 the trace equals the sum of local terms by Theorem proper-pushforward-lefschetz-verdier. | proof of theorem-trace-formula-frobenius-correspondence |
| `sec-Finite-coefficients-4` | `sec-Frobenius-correspondences` | The theorem is about T_{c_m}(ψ_m) and stalk maps of Definition frobenius-correspondences-their-operators. | theorem-trace-formula-frobenius-correspondence; prose-12-19 |
| `sec-Finite-coefficients-4` | `sec-Local-terms-on-a-curve` | The fixed points of Φ^m on P^1 are the rational points, so the Lefschetz–Verdier sum is over pointwise local terms (Lemma frobenius-fixed-scheme). | proof of theorem-trace-formula-frobenius-correspondence; prose-12-07 |
| `sec-Finite-coefficients-4` | `subsec-The-local-term-at-a-fixed-point` | Affine line step: each local term on P^1 is a trace on a stalk, and vanishes at ∞ (Prop. frobenius-local-term-curve). | proof of theorem-trace-formula-frobenius-correspondence; prose-12-19 |
| `sec-Finite-coefficients-4` | `sec-Frobenius-and-Rf` | Induction on coordinates via Lemma comparison-via-relative-frobenius; general X_0 by Lemma additivity-open-subscheme-complement. | proof of theorem-trace-formula-frobenius-correspondence |
| `sec-ell-adic-coefficients-5` | `sec-Extension-by-zero-and-completion` | Integral κ_m is the derived limit over the tower of reductions of a derived complete K (Definition derived-adic-completeness). | prose-12-20 |
| `sec-ell-adic-coefficients-5` | `sec-Inverting-ell` | Integral models of rational Frobenius correspondences via Dbc(O_E)[1/ℓ]≃Dbc(E) | proof of lemma-integral-models-rational-frobenius-correspondences |
| `sec-ell-adic-coefficients-5` | `sec-Change-of-coefficients` | Passage of the trace formula between coefficient rings uses the change-of-coefficients isomorphisms and the 2-colimit for Qbar. | theorem-grothendieck-lefschetz-trace-formula (+proof), proposition-integral-trace-formula (proof) |
| `sec-ell-adic-coefficients-5` | `sec-Exchange-formulas` | The complexes inside the traces are perfect (Lemma perfect-complexes-geometric-point). | proof of theorem-grothendieck-lefschetz-trace-formula; proof of proposition-integral-trace-formula |
| `sec-ell-adic-coefficients-5` | `sec-Weil-complexes` | Main theorem is stated for Weil complexes with Frob_{X,K} of Section Weil-complexes. | theorem-grothendieck-lefschetz-trace-formula |
| `sec-ell-adic-coefficients-5` | `sec-Traces-of-perfect-complexes` | Traces commute with reduction and scalar extension, chain formula, and over fields equal alternating sums on cohomology. | proof of proposition-integral-trace-formula; proof of theorem-grothendieck-lefschetz-trace-formula |
| `sec-ell-adic-coefficients-5` | `sec-Frobenius-correspondences` | Weil structure composed with κ_1 is a Frobenius correspondence; Lemma scheme-frobenius-geometric-frobenius identifies the operators. | proof of theorem-grothendieck-lefschetz-trace-formula; prose-12-20 |
| `sec-ell-adic-coefficients-5` | `sec-Finite-coefficients-4` | Integral formula reduces mod π^n to the finite-coefficient trace formula, which is the finite case of the main theorem. | proof of proposition-integral-trace-formula; proof of theorem-grothendieck-lefschetz-trace-formula |
| `sec-The-function-sheaf-dictionary-2` | `sec-The-function-sheaf-dictionary` | States and proves the dictionary table set up in the Introduction: 'This is Grothendieck's function–sheaf dictionary (Section ...)'. | prose-12-24, proposition-function-sheaf-dictionary, prose-01-04 |
| `sec-The-function-sheaf-dictionary-2` | `sec-Change-of-coefficients` | The trace-function statement extends to other coefficient rings by the comparisons of Proposition six-operations-change-coefficients. | corollary-trace-functions-direct-image-compact (proof) |
| `sec-The-function-sheaf-dictionary-2` | `sec-Exchange-formulas` | Stalks are perfect, so represented by bounded complexes of finite projectives (Lemma perfect-complexes-geometric-point). | proof of proposition-function-sheaf-dictionary |
| `sec-The-function-sheaf-dictionary-2` | `sec-Weil-complexes` | Operations carry the Weil structures described after Definition weil-structure. | prose-12-26; corollary-trace-functions-direct-image-compact |
| `sec-The-function-sheaf-dictionary-2` | `sec-Traces-of-perfect-complexes` | Chain formula gives multiplicativity of traces on tensor products and sign of shifts. | proof of proposition-function-sheaf-dictionary; prose-12-25 |
| `sec-The-function-sheaf-dictionary-2` | `sec-Frobenius-correspondences` | Translation from φκ_1 to geometric Frobenius by Lemma scheme-frobenius-geometric-frobenius. | proof of corollary-trace-functions-direct-image-compact |
| `sec-The-function-sheaf-dictionary-2` | `sec-Frobenius-and-Rf` | Stalk Frobenius of Rf_!K equals the fibre Frobenius by part (4) of Lemma comparison-via-relative-frobenius. | proof of corollary-trace-functions-direct-image-compact |
| `sec-The-function-sheaf-dictionary-2` | `sec-ell-adic-coefficients-5` | Part (5) is the Grothendieck–Lefschetz formula; trace functions defined for Weil complexes as in that theorem; corollary is it on fibres. | proof of proposition-function-sheaf-dictionary; proof of corollary-trace-functions-direct-image-compact; definition-trace-function |
| `sec-Rationality-and-the-functional-equation` | `sec-Cohomology-in-top-degree` | For odd d the pairing on H^d is perfect alternating (Corollary cup-product-pairing), so b_d is even. | proof of corollary-functional-equation |
| `sec-Rationality-and-the-functional-equation` | `sec-Weil-complexes` | Constant Weil structure on Λ_X and Frobenius operators F_i of Section Weil-complexes. | corollary-point-counting-zeta-function; corollary-functional-equation |
| `sec-Rationality-and-the-functional-equation` | `sec-Frobenius-and-Poincare-duality` | Functional equation: Theorem poincare-duality-frobenius gives b_{2d-i}=b_i and eigenvalues q^d/α. | proof of corollary-functional-equation |
| `sec-Rationality-and-the-functional-equation` | `sec-Traces-of-perfect-complexes` | Logarithm of determinant for a perfect complex uses that the categorical trace over a field is the alternating trace. | proof of lemma-logarithm-determinant |
| `sec-Rationality-and-the-functional-equation` | `sec-ell-adic-coefficients-5` | Euler product is the trace formula (12.3) for all m; point counting is it for the constant sheaf. | proof of theorem-trace-formula-euler-product; proof of corollary-point-counting-zeta-function |
| `sec-Weil-sheaves-and-weights` | `sec-Weil-complexes` | Geometric Frobenius, Weil complexes and their Frobenius operators are those of Section Weil-complexes. | situation-weil |
| `sec-Weil-sheaves-and-weights` | `sec-Rationality-and-the-functional-equation` | Pointwise weights are defined via the local Frobenius Frob_x at closed points of Theorem trace-formula-euler-product. | situation-weil |
| `sec-Lisse-sheaves-as-representations` | `sec-Constructible-sheaves` | Finite reductions of the lattice are finite locally constant étale sheaves by the comparison theorem for constructible sheaves. | lemma-global-lattice-normal-scheme.proof |
| `sec-Lisse-sheaves-as-representations` | `subsec-Coefficient-sheaves` | Works with lisse E_X-modules of the pro-étale coefficient category; M = lim M_n by lemma-comparison-completed-coefficients. | lemma-global-lattice-normal-scheme, its proof |
| `sec-Lisse-sheaves-as-representations` | `sec-Field-coefficients` | Uses the étale X-scheme representing lattices in L (lemma-lattices-lisse-e-sheaves) as the object whose components are shown finite étale. | lemma-global-lattice-normal-scheme.proof |
| `sec-Lisse-sheaves-as-representations` | `sec-Lattices-after-stratification` | Global lattice on a normal scheme: 'then we argue as in' the stratified-lattice lemma, pushing the universal lattice down by the trace. | prose-13-09, lemma-global-lattice-normal-scheme.proof |
| `sec-Delignes-theorem-2` | `sec-Weil-sheaves-and-weights` | D_{<=w} is defined by Definition weights; the shift behaviour comes from Proposition weights-under-usual-operations. | prose-13-12, theorem-weights-rf-shriek |
| `subsec-Frobenius-invariants` | `sec-Left-completeness-and-hypercovers` | Cohomology on qcqs U commutes with filtered colimits (corollary-continuity-cohomology) to compute H^1(U,Q_l). | proposition-no-fixed-class-degree-one.proof |
| `subsec-Frobenius-invariants` | `subsec-Coefficient-sheaves` | Q_l on U_proet is Z_l[1/l], so H^1(U,Q_l) is the rationalization of the inverse limit. | proposition-no-fixed-class-degree-one.proof |
| `subsec-Frobenius-invariants` | `sec-Continuous-cohomology` | H^1 with Z_l coefficients computed as continuous cohomology (Proposition continuous-cohomology-pro-etale-cohomology). | proof of proposition-no-fixed-class-degree-one |
| `subsec-Frobenius-invariants` | `sec-Poincare-duality` | Kummer duality for the Tate module: derived Poincaré duality for the constant sheaf gives H^1(C,A_n)≃Hom(H^1(C,A_n(1)),A_n). | proof of proposition-kummer-duality-integral-tate-module |
| `subsec-Frobenius-invariants` | `sec-Compactifications` | Smooth projective model of the curve: compactify by Nagata's theorem and normalize. | lemma-proper-smooth-model.proof |
| `subsec-Frobenius-invariants` | `sec-Tate-modules` | Proper case: arithmetic Frobenius has no fixed vector on T_l J; T_l J is finite free. | proposition-no-fixed-class-degree-one.proof, proposition-kummer-duality-integral-tate-module.proof |
| `subsec-Frobenius-invariants` | `sec-Torsion-points` | H^1(C,A_n(1)) free of rank 2g by corollary-torsion-jacobian-field-extension, needed for degreewise duality. | proposition-kummer-duality-integral-tate-module.proof |
| `subsec-Frobenius-invariants` | `sec-Descent-to-the-ground-field` | First identification H^1(C,A_n(1)) = J[l^n](k), Galois-equivariantly, is proposition-h-1-curve-tate-module. | proposition-kummer-duality-integral-tate-module.proof |
| `subsec-Frobenius-invariants` | `sec-Kummer-theory` | H^0(C,A_n)=A_n and H^2(C,A_n(1))=A_n for the smooth proper curve, inputs to the duality with the Tate module. | proposition-kummer-duality-integral-tate-module.proof |
| `subsec-Finite-monodromy` | `sec-Weil-sheaves-and-weights` | Works with W(U_0), the lift s and Frob_x of the Convention; weight lambda_iota(c) as for B_b. | prose-14-06, prose-14-09, corollary-rank-one-weights |
| `subsec-Finite-monodromy` | `sec-Lisse-sheaves-as-representations` | A rank-one lisse Weil sheaf is a character of W(U_0); determinant weight is defined via the corresponding representation rho. | prose-14-02, definition-determinant-weight |
| `subsec-Finite-monodromy` | `subsec-Frobenius-invariants` | Invariant additive characters vanish because Frobenius-fixed classes in H^1(U,Z/l^n) vanish (proposition-no-fixed-class-degree-one). | lemma-invariant-additive-characters.proof, prose-14-06 |
| `sec-Determinant-weights` | `sec-Sheaves-of-rank-one` | 'The later subsections Determinant-weights to Exterior-powers are built on it' (the section's own prose). | prose-14-02 |
| `subsec-Representations-and-filtrations` | `sec-Weil-sheaves-and-weights` | Throughout U_0, s in W(U_0) as in Convention situation-weil; Weil representations are the lisse Weil sheaves. | prose-14-12, prose-14-13 |
| `subsec-Representations-and-filtrations` | `sec-Lisse-sheaves-as-representations` | 'We treat lisse sheaves as representations of the Weil group'; Weil representations are the lisse Weil Qbar_l-sheaves. | prose-14-12, prose-14-13, definition-weil-representation |
| `subsec-Central-elements` | `subsec-Representations-and-filtrations` | Weil representations; semisimplicity restricts to G^0 by lemma-restriction-normal-subgroup in the proof of lemma-identity-component. | lemma-identity-component.proof |
| `subsec-Central-elements` | `sec-Smoothness-and-components` | Finite component group and closed connected images of homomorphisms (lemma-connected-components-images-homomorphisms). | lemma-identity-component.proof, proposition-central-element-arithmetic-monodromy-group.proof |
| `subsec-Central-elements` | `sec-Lie-algebras` | lemma-stable-subspaces-center makes V a faithful semisimple g-module and gives Lie(T)=Z(g). | lemma-identity-component.proof |
| `subsec-Central-elements` | `sec-Reductive-Lie-algebras` | g = Z(g)+[g,g] by proposition-lie-algebras-faithful-semisimple-representation, the key step of G^0=Z(G^0)^0 H^0. | lemma-identity-component.proof |
| `subsec-Tensor-operations` | `sec-Weil-sheaves-and-weights` | dw(Q)=lambda_iota(c_Q)/N with lambda_iota the additive function of Proposition weights-under-usual-operations. | prose-14-11, lemma-determinant-weight-from-central-scalar |
| `subsec-Tensor-operations` | `subsec-Finite-monodromy` | Uses Definition determinant-weight and finiteness of geometric monodromy on determinants (det(h\|Q) a root of unity). | prose-14-20, lemma-determinant-weight-from-central-scalar.proof |
| `subsec-Tensor-operations` | `subsec-Representations-and-filtrations` | Filtrations of tensor and exterior powers identify simple factors, allowing passage to semisimplifications. | proposition-determinant-weights-tensor-operations.proof |
| `subsec-Tensor-operations` | `subsec-Central-elements` | Scalars of the central element z=h rho(s)^N on simple factors give determinant weights. | lemma-determinant-weight-from-central-scalar, proposition-determinant-weights-tensor-operations.proof, prose-14-21 |
| `sec-Rankins-bound` | `sec-Poincare-duality` | Degreewise Poincaré duality computes H^2_c(U,F)^∨=H^0(U,F^∨(1)). | proof of lemma-degree-zero-top-cohomology |
| `sec-Rankins-bound` | `sec-Rationality-and-the-functional-equation` | L-function of T on U_0 written as ratio of det(1-Ft\|H^i_c) by Theorem trace-formula-euler-product. | proof of proposition-bound-largest-determinant-weight |
| `sec-Rankins-bound` | `sec-Weil-sheaves-and-weights` | Eigenvalues of filtered spaces and tensor powers (lemma-filtrations-spectra); weights of H^0, H^2_c. | proposition-bound-largest-determinant-weight.proof, lemma-degree-zero-top-cohomology |
| `sec-Rankins-bound` | `sec-Lisse-sheaves-as-representations` | H^0 and H^2_c are computed from the description of a lisse sheaf by its representation V of pi_1(U). | lemma-degree-zero-top-cohomology and proof |
| `sec-Rankins-bound` | `subsec-Finite-monodromy` | The bound is by the largest determinant weight (Definition determinant-weight); a rank-one factor with eigenvalue b has determinant weight lambda(b). | proposition-bound-largest-determinant-weight and proof |
| `sec-Rankins-bound` | `sec-Determinant-weights` | 'This subsection proves the two facts about determinant weights that Rankin's argument needs' (the section's own prose). | prose-14-11 |
| `sec-Rankins-bound` | `subsec-Tensor-operations` | Every constituent of G^{(x)2m} has determinant weight <= 2m*beta by Proposition determinant-weights-tensor-operations(1); this bounds H^2_c. | proposition-bound-largest-determinant-weight.proof, prose-14-23 |
| `sec-Exterior-powers-and-purity` | `subsec-Finite-monodromy` | Determinants det G_j are pure of known weight (Corollaries rank-one-weights, determinant-weights). | theorem-purity-real-sheaves-curves.proof, prose-14-28 |
| `sec-Exterior-powers-and-purity` | `subsec-Tensor-operations` | Proposition determinant-weights-tensor-operations(2) finds the exterior power where a group of constituents has the largest determinant weight. | theorem-purity-real-sheaves-curves.proof, prose-14-22 |
| `sec-Exterior-powers-and-purity` | `sec-Rankins-bound` | Applies Proposition bound-largest-determinant-weight to exterior powers and to the dual. | theorem-purity-real-sheaves-curves.proof, prose-14-28 |
| `sec-Weights-of-middle-extensions` | `sec-Poincare-duality` | Degreewise Poincaré duality (d=1) shows H^r_c vanishes for r>2. | proof of lemma-cohomological-range-curve |
| `sec-Weights-of-middle-extensions` | `sec-Rationality-and-the-functional-equation` | By the trace formula (Euler product) the Taylor series of the convergent product is that of the rational function ιL_U. | proof of proposition-weights-j-boundary-points |
| `sec-Weights-of-middle-extensions` | `sec-Weil-sheaves-and-weights` | Main results are stated in terms of purity and 'punctually of weights <= a' of Definition weights. | proposition-weights-j-boundary-points, corollary-unramified-boundary-point |
| `sec-Weights-of-middle-extensions` | `sec-Lisse-sheaves-as-representations` | Boundary stalk (j_*F)_z = V^{I_z}, via finite reductions of a stable lattice and Galois theory. | lemma-boundary-stalk.proof |
| `sec-Weights-of-middle-extensions` | `sec-Rankins-bound` | H^2_c(U,F) computed with its weights by lemma-degree-zero-top-cohomology bounds the poles of L_X; also extreme degrees. | proposition-weights-j-boundary-points.proof, lemma-extreme-degrees-affine-curve.proof |
| `sec-Growth-of-squared-traces` | `sec-Rationality-and-the-functional-equation` | The Euler product and trace formula express the squared-trace series as L'/L with L a ratio of determinants. | proof of theorem-weights-sums-squared-traces; definition-growth-squared-traces |
| `sec-Growth-of-squared-traces` | `sec-Weil-sheaves-and-weights` | Twisting by B_b to weight zero (Proposition weights-under-usual-operations) and lambda_iota(b) shift of nu. | proposition-twisting-weight-zero-adding-dual.proof, lemma-bounds-squared-traces |
| `sec-Growth-of-squared-traces` | `sec-Rankins-bound` | Real case: positivity of Euler factors and H^2_c of lemma-degree-zero-top-cohomology force a pole on \|t\|=q^{-w-1}. | theorem-weights-sums-squared-traces.proof, prose-15-01 |
| `sec-Growth-of-squared-traces` | `sec-Weights-of-middle-extensions` | Point-count bound for S_n, and boundary stalks of j_* have weights <= w (Prop. weights-j-boundary-points). | lemma-bounds-squared-traces, corollary-sums-squared-traces-j-shriek.proof |
| `sec-The-Artin-Schreier-sheaf` | `subsec-Construction-of-Rf` | Künneth formula for compact supports rests on Rh_!=Rf_!Rp_1! and proper base change for Rf_!. | lemma-kunneth-formula-compact-supports.proof |
| `sec-The-Artin-Schreier-sheaf` | `subsec-The-trace-map` | The trace map for A^r→Spec k is the isomorphism RΓ_c(A^r,E)(r)[2r]≃E, on constants the trace (9.11). | lemma-integral-linear-character (proof) |
| `sec-The-Artin-Schreier-sheaf` | `sec-Kummer-theory` | RGamma_c(A^1,E)=E(-1)[-2] from the cohomology of P^1 (Appendix D) and localization, starting the vanishing argument. | lemma-integral-linear-character.proof |
| `sec-Fourier-inversion` | `subsec-Construction-of-Rf` | FT = Rp_2!(...); stalk formula and base change are proper base change for Rp_2!, composites by composition of Rf_!. | proposition-base-change-fourier-inversion.proof, proposition-fourier-inversion.proof |
| `sec-Fourier-inversion` | `sec-Stability-of-Dbctf` | 'since the six operations preserve constructibility, this defines a triangulated functor FT_psi: Dbc(V,E)->Dbc(V^,E)'. | prose-16-06 |
| `sec-Fourier-inversion` | `sec-Weil-complexes` | Inversion and the transform of the constant sheaf are isomorphisms of Weil complexes, commuting with Weil structures. | proposition-fourier-inversion.proof, lemma-fourier-transform-constant-sheaf |
| `sec-Fourier-inversion` | `sec-The-Artin-Schreier-sheaf` | FT kernel is the pullback of L_psi; inversion and the constant-sheaf transform reduce to lemma-integral-linear-character. | prose-16-06, proposition-fourier-inversion.proof, lemma-fourier-transform-constant-sheaf.proof |
| `sec-The-Plancherel-formula` | `sec-The-function-sheaf-dictionary-2` | The dictionary computes the trace function of the Fourier transform step by step (parts (1)-(3)). | prose-16-08 |
| `sec-The-Plancherel-formula` | `sec-Growth-of-squared-traces` | Consequence nu(FT K)=nu(K)+1 uses nu and t_{K,n} of Definition growth-squared-traces. | corollary-plancherel, prose-16-08 |
| `sec-The-Plancherel-formula` | `sec-The-Artin-Schreier-sheaf` | Trace of the kernel K_psi is psi(Tr<x,y>) by lemma-artin-schreier-character-sheaf. | prose-16-08 |
| `sec-The-Plancherel-formula` | `sec-Fourier-inversion` | Plancherel is a statement about FT_psi, defined in (16.1). | corollary-plancherel, prose-16-08 |
| `sec-Perverse-sheaves-on-a-curve` | `sec-Weil-complexes` | A perverse Weil sheaf is a perverse sheaf with a Weil structure, morphisms as in Definition weil-structure. | definition-perverse-sheaves-curve |
| `sec-Perverse-sheaves-on-a-curve` | `sec-Lisse-sheaves-as-representations` | A lisse sheaf has no punctual subsheaf: generization maps injective via the lattice of proposition-lattices-representations-normal-scheme. | lemma-largest-punctual-subsheaf.proof |
| `sec-Perverse-t-exactness` | `sec-Weights-of-middle-extensions` | Degrees of stalks bounded by lemma-cohomological-range-curve; H^2_c = (V(x)chi_y)_{pi_1}(-1) by lemma-extreme-degrees-affine-curve. | proposition-fourier-transform-perverse-heart.proof |
| `sec-Perverse-t-exactness` | `sec-The-Artin-Schreier-sheaf` | The characters chi_y are pairwise distinct since RGamma_c of a nontrivial L_psi vanishes (lemma-integral-linear-character). | proposition-fourier-transform-perverse-heart.proof |
| `sec-Perverse-t-exactness` | `sec-Fourier-inversion` | Stalk formula (16.2) reduces to H^*_c on the line; the quasi-inverse FT_{psi^-1}(-)(1) comes from Fourier inversion. | proposition-fourier-transform-perverse-heart.proof, prose-16-15 |
| `sec-Perverse-t-exactness` | `sec-Perverse-sheaves-on-a-curve` | t-exactness for the perverse t-structure of lemma-perverse-sheaves-curve; Weil statement via lemma-perverse-weil-sheaves. | proposition-fourier-transform-perverse-heart and proof |
| `sec-Middle-extensions` | `subsec-Representations-and-filtrations` | Trivial geometric constituent excluded by semisimplicity of the restriction to pi_1 (lemma-restriction-normal-subgroup). | lemma-unramified-at-infinity-no-linear-characters.proof |
| `sec-Middle-extensions` | `sec-The-Artin-Schreier-sheaf` | The excluded constituents are the character sheaves L_psi(ax); ramification at infinity of the Artin–Schreier cover. | lemma-unramified-at-infinity-no-linear-characters.proof, prose-16-16 |
| `sec-Middle-extensions` | `sec-Fourier-inversion` | A punctual transform is excluded 'by Fourier inversion and exactness', restricting the kernel to {a}xA^1. | proposition-fourier-transform-middle-extension.proof |
| `sec-Middle-extensions` | `sec-Perverse-sheaves-on-a-curve` | By lemma-simple-objects the simple transform is punctual or an irreducible middle extension. | proposition-fourier-transform-middle-extension.proof |
| `sec-Middle-extensions` | `sec-Perverse-t-exactness` | 'By Proposition fourier-transform-perverse-heart, the transform of the simple object (j_*M)[1] is simple'. | proposition-fourier-transform-middle-extension.proof |
| `sec-Purity-of-the-lisse-part` | `sec-The-function-sheaf-dictionary-2` | Trace formula for Rp_{2!} (Corollary trace-functions-direct-image-compact) gives -t_H(y)=Σ_x t_F(x,y). | proof of proposition-purity-lisse-part-fourier-transform |
| `sec-Purity-of-the-lisse-part` | `sec-Exterior-powers-and-purity` | A twist of M' is a quotient of a real sheaf, to which Theorem purity-real-sheaves-curves applies. | proposition-purity-lisse-part-fourier-transform.proof |
| `sec-Purity-of-the-lisse-part` | `sec-Weights-of-middle-extensions` | Boundary weights from Proposition weights-j-boundary-points; extreme degrees; purity extended by corollary-unramified-boundary-point. | lemma-fourier-transform-boundary-sequence.proof, proposition-purity-lisse-part-fourier-transform.proof |
| `sec-Purity-of-the-lisse-part` | `sec-Growth-of-squared-traces` | Twist to weight zero and add the dual (Proposition twisting-weight-zero-adding-dual) before transforming. | proposition-purity-lisse-part-fourier-transform.proof, lemma-twisted-envelope.proof |
| `sec-Purity-of-the-lisse-part` | `sec-Fourier-inversion` | Stalk formula of proposition-base-change-fourier-inversion computes the stalks of FT(j_!M). | lemma-fourier-transform-boundary-sequence.proof |
| `sec-Purity-of-the-lisse-part` | `sec-Perverse-sheaves-on-a-curve` | Uses lemma-simple-objects on the perverse transform to get the surjection onto j'_*M'. | proposition-purity-lisse-part-fourier-transform.proof |
| `sec-Purity-of-the-lisse-part` | `sec-Middle-extensions` | M' is defined by FT((j_*M)[1]) = (j'_*M')[1] of Proposition fourier-transform-middle-extension. | prose-17-02, lemma-fourier-transform-boundary-sequence.proof |
| `sec-The-weight-of-the-Fourier-transform` | `sec-Weights-of-middle-extensions` | Stalk of j'_*M' at 0' is the inertia invariants (lemma-boundary-stalk), weights bounded by the Proposition. | corollary-h-1-c-stalk-fourier.proof |
| `sec-The-weight-of-the-Fourier-transform` | `sec-Growth-of-squared-traces` | nu = weight for pure sheaves and for their j_* (corollary-sums-squared-traces-j-shriek). | theorem-weight-fourier-transform.proof, prose-17-05 |
| `sec-The-weight-of-the-Fourier-transform` | `sec-Fourier-inversion` | Stalk of FT((j_*M)[1]) at 0' is RGamma_c(A^1,j_*M)[2] by the stalk formula. | corollary-h-1-c-stalk-fourier.proof |
| `sec-The-weight-of-the-Fourier-transform` | `sec-The-Plancherel-formula` | v = nu(FT((j_*M)[1])) = nu((j_*M)[1]) + 1 = w+1 by the Plancherel formula. | theorem-weight-fourier-transform.proof |
| `sec-The-weight-of-the-Fourier-transform` | `sec-Middle-extensions` | Uses the defining isomorphism FT((j_*M)[1]) = (j'_*M')[1] in the Plancherel computation and the stalk comparison. | theorem-weight-fourier-transform.proof, corollary-h-1-c-stalk-fourier.proof |
| `sec-The-weight-of-the-Fourier-transform` | `sec-Purity-of-the-lisse-part` | By Prop. purity-lisse-part M' is pure of some weight v; Plancherel then finds v. Purity had to come first. | prose-17-05, theorem-weight-fourier-transform.proof |
| `sec-The-affine-line` | `sec-Verdier-biduality` | Local duality lemma: duality exchanges Rj_* with j_! and i^* with i^! (Verdier exchange formulas). | lemma-local-duality-point-c-u.proof |
| `sec-The-affine-line` | `sec-Poincare-duality` | Local duality uses D_U F = F^vee(1)[2] for a lisse sheaf on the smooth curve. | lemma-local-duality-point-c-u.proof |
| `sec-The-affine-line` | `sec-Weil-sheaves-and-weights` | Irreducible geometrically constant factors are sheaves B_b of Proposition weights-under-usual-operations. | theorem-weight-bound-affine-line.proof |
| `sec-The-affine-line` | `sec-Weights-of-middle-extensions` | Source of the boundary map has weights <= w at points of C\U by Proposition weights-j-boundary-points. | proposition-exactness-fixed-pure-weight.proof, prose-17-07 |
| `sec-The-affine-line` | `sec-The-Artin-Schreier-sheaf` | Geometrically constant factors: middle extension constant, so H^1_c vanishes by the trivial case of lemma-integral-linear-character. | theorem-weight-bound-affine-line.proof |
| `sec-The-affine-line` | `sec-Middle-extensions` | Hypothesis of the middle-extension proposition checked by lemma-unramified-at-infinity-no-linear-characters. | theorem-weight-bound-affine-line.proof, prose-17-10 |
| `sec-The-affine-line` | `sec-The-weight-of-the-Fourier-transform` | Induction along a composition series from the irreducible case, Cor. h-1-c-stalk-fourier, to the weight bound on the line. | prose-17-07, prose-17-09, theorem-weight-bound-affine-line.proof |
| `sec-Arbitrary-curves` | `sec-Weil-sheaves-and-weights` | Over Spec k_0 the bounds are conditions on eigenvalues (lemmas weil-sheaves-point-mixed, bounding-weights-mixed-sheaf). | theorem-weight-bound-curve.proof |
| `sec-Arbitrary-curves` | `sec-Weights-of-middle-extensions` | Boundary stalks of j_*F have weights <= w; lisse extension is j_*; extreme degrees on affine curves. | theorem-weight-bound-affine-curve.proof, theorem-weight-bound-curve.proof |
| `sec-Arbitrary-curves` | `sec-The-affine-line` | Reduces every affine curve to the bound on opens of the line unramified at infinity (Thm weight-bound-affine-line). | prose-17-11, theorem-weight-bound-affine-curve.proof |
| `sec-Arbitrary-curves` | `sec-Riemann-Roch-and-Serre-duality` | Riemann-Roch gives a function with a single pole of order prime to p, hence a finite generically etale map to A^1. | prose-17-11, lemma-finite-generically-etale-map-line.proof |
| `sec-Quasi-finite-morphisms-and-curves` | `sec-Proper-morphisms` | 'For a finite map, exactness follows from Lemma finite-morphisms' | proof of lemma-finite-quasi-finite-direct-images |
| `sec-Quasi-finite-morphisms-and-curves` | `subsec-Construction-of-Rf` | Rg_! = gbar_* j_! for the Zariski factorization (composition of Rf_!). | lemma-finite-quasi-finite-direct-images.proof |
| `sec-Quasi-finite-morphisms-and-curves` | `sec-Weil-sheaves-and-weights` | The lemma is about preserving mixed sheaves of weights at most w and D_{<=w}, as defined there. | lemma-finite-quasi-finite-direct-images |
| `sec-Quasi-finite-morphisms-and-curves` | `sec-Lisse-sheaves-as-representations` | Curves preserving irreducibility: lisse sheaves are treated as lattice representations of pi_1, finite quotients as Galois covers. | prose-18-04, corollary-curve-preserving-geometric-irreducibility.proof |
| `sec-Quasi-finite-morphisms-and-curves` | `sec-Delignes-theorem-2` | Finite and quasi-finite direct images are shown to map D_{<=w}(Z_0) into D_{<=w}(Y_0). | lemma-finite-quasi-finite-direct-images |
| `sec-Mixedness-of-real-sheaves` | `sec-Weil-sheaves-and-weights` | Extensions and Weil subobjects of mixed sheaves are mixed (Proposition weights-under-usual-operations). | lemma-mixedness-open-closed.proof, lemma-mixedness-descends-constant-extension.proof |
| `sec-Mixedness-of-real-sheaves` | `subsec-Representations-and-filtrations` | Geometric restriction of each irreducible factor is semisimple by lemma-restriction-normal-subgroup. | lemma-geometric-constituents-after-constant-extension.proof |
| `sec-Mixedness-of-real-sheaves` | `sec-Exterior-powers-and-purity` | Passes from purity of real sheaves on curves (Theorem purity-real-sheaves-curves) to mixedness on any base. | prose-18-06, theorem-real-constructible-sheaves-are-mixed.proof |
| `sec-Mixedness-of-real-sheaves` | `sec-Quasi-finite-morphisms-and-curves` | Curves keeping constituents irreducible (Cor.) and quasi-finite direct images for descent and gluing of strata. | prose-18-06, theorem-real-constructible-sheaves-are-mixed.proof, lemma-mixedness-descends-constant-extension.proof |
| `sec-Relative-affine-curves` | `subsec-Construction-of-Rf` | Base change for Rh_! identifies stalks with H^i_c of fibres. | theorem-pure-lisse-sheaves-over-relative.proof |
| `sec-Relative-affine-curves` | `sec-Rationality-and-the-functional-equation` | Euler product and determinant identity express L_ι(U_y,G,T) as ιP_1/ιP_2. | proof of theorem-pure-lisse-sheaves-over-relative |
| `sec-Relative-affine-curves` | `sec-Weil-sheaves-and-weights` | Mixed filtration plus pointwise bound gives weights via lemma-bounding-weights-mixed-sheaf; summands mixed by the Proposition. | theorem-pure-lisse-sheaves-over-relative.proof, prose-18-08 |
| `sec-Relative-affine-curves` | `sec-Weights-of-middle-extensions` | lemma-extreme-degrees-affine-curve on fibre components: vanishing outside degrees 1,2 and the roots of P_2. | theorem-pure-lisse-sheaves-over-relative.proof |
| `sec-Relative-affine-curves` | `sec-Growth-of-squared-traces` | Mixedness by twisting to weight zero and adding the dual: G of Proposition twisting-weight-zero-adding-dual. | theorem-pure-lisse-sheaves-over-relative.proof |
| `sec-Relative-affine-curves` | `sec-Arbitrary-curves` | The curve case (Thm weight-bound-curve) bounds stalks H^i_c of fibres and separates moduli of P_1 and P_2. | prose-18-08, theorem-pure-lisse-sheaves-over-relative.proof |
| `sec-Relative-affine-curves` | `sec-Mixedness-of-real-sheaves` | R^ih_!G is real, hence mixed by Theorem real-constructible-sheaves-are-mixed. | theorem-pure-lisse-sheaves-over-relative.proof |
| `sec-Proof-of-Delignes-theorem` | `subsec-Construction-of-Rf` | Base change and composition for Rf_! in partitions and the Leray spectral sequence. | lemma-weight-bounds-partitions.proof, theorem-direct-image-mixed-sheaf.proof |
| `sec-Proof-of-Delignes-theorem` | `sec-Weil-sheaves-and-weights` | Mixed sheaves of weights <= u closed under subquotients and extensions (Prop. weights-under-usual-operations). | lemma-weights-exact-sequence.proof, lemma-weight-bounds-partitions.proof |
| `sec-Proof-of-Delignes-theorem` | `sec-Delignes-theorem-2` | Proves Theorem weights-rf-shriek 'stated in Section Delignes-theorem-2', for K in D_{<=w}. | prose-18-13, theorem-weights-rf-shriek.proof |
| `sec-Proof-of-Delignes-theorem` | `sec-Quasi-finite-morphisms-and-curves` | Quasi-finite maps have the property (Lemma finite-quasi-finite-direct-images); used in partitions and the relative line. | prose-18-09, proposition-relative-affine-line.proof, theorem-direct-image-mixed-sheaf.proof |
| `sec-Proof-of-Delignes-theorem` | `sec-Relative-affine-curves` | On the lisse part the projection of the relative line is a relative affine curve; apply Theorem pure-lisse-sheaves-over-relative. | proposition-relative-affine-line.proof |
| `sec-The-Riemann-hypothesis` | `subsec-Construction-of-Rf` | For proper f the compactification definition gives Rf_! = Rf_*; base change computes stalks. | theorem-purity-higher-direct-images-under.proof |
| `sec-The-Riemann-hypothesis` | `sec-Poincare-duality` | Degreewise duality on the smooth proper geometric fibre gives a perfect pairing H^i×H^{2d-i}. | proof of theorem-purity-higher-direct-images-under |
| `sec-The-Riemann-hypothesis` | `sec-Frobenius-and-Poincare-duality` | Theorem poincare-duality-frobenius makes the fibre pairing Frobenius-equivariant, turning the upper weight bound into the lower one. | proof of theorem-purity-higher-direct-images-under |
| `sec-The-Riemann-hypothesis` | `sec-Weil-sheaves-and-weights` | Statement and conclusion are about punctually pure and mixed Weil sheaves in the sense defined there. | theorem-purity-higher-direct-images-under |
| `sec-The-Riemann-hypothesis` | `sec-Proof-of-Delignes-theorem` | Upper bound for R^if_* F (and for the dual) is Theorem direct-image-mixed-sheaf. | prose-19-02, theorem-purity-higher-direct-images-under.proof |
| `sec-Rational-power-series` | `sec-Rationality-and-the-functional-equation` | Z(X_0,T)∈Q(T)∩(1+TZ[[T]]) by Corollary point-counting-zeta-function. | prose-19-06 |
| `sec-Integrality-and-independence-of-ell` | `sec-The-Weil-conjectures` | Its main theorem proves the Weil conjectures (1)-(4) on the zeta function as formulated there ('with the statement on Betti numbers as above'). | theorem-weil-conjectures-smooth-proper-schemes, prose-01-08, example-running-example-purity |
| `sec-Integrality-and-independence-of-ell` | `sec-Cohomology-in-top-degree` | H^0=Q_ℓ with trivial Frobenius and tr_X:H^{2d}≃Q_ℓ(-d) by Theorem trace-isomorphism-top-degree. | proof of theorem-weil-conjectures-smooth-proper-schemes; proof of corollary-point-count-estimates |
| `sec-Integrality-and-independence-of-ell` | `sec-Rationality-and-the-functional-equation` | Determinant identity of Corollary point-counting-zeta-function and the functional equation give (3),(4) of the Weil conjectures. | prose-19-07; proof of theorem-weil-conjectures-smooth-proper-schemes; proof of corollary-point-count-estimates |
| `sec-Integrality-and-independence-of-ell` | `sec-The-Riemann-hypothesis` | Purity (Cor. purity-cohomology-smooth-proper-variety) makes the P_{i,ell} pairwise coprime, so no cancellation. | prose-19-07, lemma-reciprocal-roots-zeta.proof |
| `sec-Integrality-and-independence-of-ell` | `sec-Rational-power-series` | Uses the unique reduced fraction A/B in Z[T] (Lemma reduced-fractions-integer-coefficients) and its uniqueness argument. | prose-19-07, lemma-reciprocal-roots-zeta.proof, theorem-weil-conjectures-smooth-proper-schemes.proof |
| `sec-Integrality-and-independence-of-ell` | `sec-Kummer-theory` | For curves b_1=2g by the cohomology calculation of Appendix D (H^1(C,mu_n)=J[n]), giving Weil's bound 2g q^{m/2}. | corollary-point-count-estimates.proof, example-zeta-projective-space-elliptic-curve |
| `sec-Compactifications` | `sec-Extension-by-zero-and-completion` | Passing to the schematic closure needs exactness of i_* on the pro-etale site (Prop. extension-zero-restriction-closed-subscheme). | lemma-passing-schematic-closure.proof, remark-non-noetherian-compactifications |
| `sec-Elimination-of-indeterminacy` | `sec-Compactifications` | Works with compactifications, schematic closures and uniqueness of maps on dense opens (Lemma uniqueness-maps-dense-open). | prose-A-18, lemma-extending-graph-from-compactification |
| `sec-Separation-by-blow-ups` | `sec-Elimination-of-indeterminacy` | Both lemmas use elimination of indeterminacy from the previous subsection; admissible blow-up calculus. | prose-A-19, lemma-gluing-after-admissible-blow-ups.proof, lemma-extending-isomorphism-over-closure-closed.proof, proposition-compactifying-union-two-opens.proof |
| `sec-Proof-of-Nagatas-theorem` | `sec-Compactifications` | Proves the theorem stated there; schematic closures (Lemma schematic-closure-uniqueness) make compactifications dense. | lemma-affine-covers-dense-intersection.proof, theorem-nagata-s-compactification-theorem.proof |
| `sec-Proof-of-Nagatas-theorem` | `sec-Separation-by-blow-ups` | Noetherian case: induction over a dense affine cover using Prop. compactifying-union-two-opens. | prose-A-23, theorem-nagata-s-compactification-theorem.proof |
| `sec-Chows-lemma` | `sec-Proof-of-Nagatas-theorem` | Chow's lemma is deduced from the Noetherian case by the approximation argument in the proof of Nagata's theorem. | theorem-chow-s-lemma-projective-form.proof |
| `sec-Multiplication-by-n` | `sec-The-theorem-of-the-cube` | Rigidity gives commutativity; the theorem of the cube gives [n]^*L formula, hence degree n^{2g}. | prose-B-07, lemma-abelian-variety-commutative.proof, proposition-pullback-multiplication-n.proof |
| `sec-Tate-modules` | `sec-Multiplication-by-n` | Orders of A[ell^n] and divisibility of A(kbar) from Prop. multiplication-n make T_ell A free of rank 2g. | prose-B-12, proposition-integral-tate-module.proof |
| `sec-Hilbert-schemes-of-points` | `sec-The-Picard-functor` | The chart F is a subfunctor of Pic_{C/k} described by rigidified sheaves 'as in Lemma rigidification-along-section'. | prose-C-09, proposition-divisors-degree-g-open-chart |
| `sec-Hilbert-schemes-of-points` | `sec-Riemann-Roch-and-Serre-duality` | Openness of the chart is coherent base change; degree g of the divisors and the twisting lemma come from Riemann-Roch. | prose-C-09, proposition-divisors-degree-g-open-chart.proof, lemma-twisting-h-0-1-h.proof |
| `sec-The-Jacobian` | `sec-The-Picard-functor` | The Jacobian section represents the fppf Picard functor, rigidifying at a point P in C(k). | lemma-representability-picard-functor, lemma-representability-picard-functor.proof |
| `sec-The-Jacobian` | `sec-Riemann-Roch-and-Serre-duality` | Covering by charts and local constancy of the degree use coherent base change and Riemann-Roch. | lemma-representability-picard-functor.proof, theorem-picard-scheme-jacobian-over-separably.proof |
| `sec-The-Jacobian` | `sec-Hilbert-schemes-of-points` | Pic_{C/k} is glued from translates of the chart of Proposition divisors-degree-g-open-chart using the twists of Lemma twisting-h-0-1-h; properness via the Abel map from Hilb^g. | lemma-representability-picard-functor.proof, theorem-picard-scheme-jacobian-over-separably.proof, prose-C-11 |
| `sec-Torsion-points` | `sec-Multiplication-by-n` | J(C)[n] finite etale of rank n^{2g} and J(C)(k) divisible by Prop. multiplication-n. | corollary-torsion-jacobian-field-extension.proof |
| `sec-Torsion-points` | `sec-Tate-modules` | J(C)[ell^m](k) = (Z/ell^m)^{2g} by Prop. integral-tate-module. | corollary-torsion-jacobian-field-extension.proof |
| `sec-Torsion-points` | `sec-The-Jacobian` | J(C)[n] and Pic(C)[n] computed from the degree sequence of Corollary degree-jacobian and base change of the Jacobian (Theorem picard-scheme-jacobian). | corollary-torsion-jacobian-field-extension.proof, prose-C-14 |
| `sec-Descent-to-the-ground-field` | `sec-Comparison-with-the-etale-site` | H^1(C,Z/l^n(1)) = J_0[l^n] is computed on the etale site and transported by Theorem bounded-below-cohomology-comparison. | proposition-h-1-curve-tate-module.proof |
| `sec-Descent-to-the-ground-field` | `sec-The-Picard-functor` | J_0 represents the degree-zero fppf Picard sheaf; its finite presentation follows from Lemma rigidification-along-section. | proposition-jacobian-over-ground-field, proposition-jacobian-over-ground-field.proof |
| `sec-Descent-to-the-ground-field` | `sec-The-Jacobian` | J_0 is obtained by descending the Jacobian J_s over k_s given by Theorem picard-scheme-jacobian-over-separably. | proposition-jacobian-over-ground-field.proof, prose-C-15 |
| `sec-Kummer-theory` | `sec-Comparison-with-the-etale-site` | Étale computations of G_m cohomology carried to C_proet by the bounded-below comparison. | proof of lemma-cohomology-multiplicative-group |
| `sec-Kummer-theory` | `sec-Riemann-Roch-and-Serre-duality` | Tsen's theorem, giving H^q(C,G_m)=0 for q>=2, is proved by counting dimensions with Riemann-Roch. | lemma-cohomology-multiplicative-group.proof |
| `sec-Kummer-theory` | `sec-The-Jacobian` | H^1(C,mu_n)=Pic(C)[n] and H^2=Pic(C)/n are computed from the degree sequence of Corollary degree-jacobian. | proposition-smooth-proper-curves-torsion-prime.proof, prose-D-03 |
| `sec-Kummer-theory` | `sec-Torsion-points` | J(C)[n] finite etale of rank n^{2g}, divisibility and invariance under field extension from Corollary torsion-jacobian-field-extension. | proposition-smooth-proper-curves-torsion-prime.proof |
| `sec-Affine-curves` | `sec-Torsion-points` | Pic(U) is n-divisible because J(C-bar)(k) is (Corollary torsion-jacobian-field-extension); used for H^2=0 and surjectivity of the residue map. | proposition-cohomology-smooth-affine-curve.proof |
| `sec-Affine-curves` | `sec-Kummer-theory` | Vanishing above degree one via the Kummer sequence and Lemma cohomology-multiplicative-group; field invariance from Proposition smooth-proper-curves-torsion-prime. | proposition-cohomology-smooth-affine-curve.proof |
| `sec-The-Artin-Schreier-sequence` | `sec-Comparison-with-the-etale-site` | The Artin-Schreier computations on the etale site are carried over to the pro-etale site by Theorem bounded-below-cohomology-comparison. | proposition-p-torsion-smooth-proper-curve.proof, lemma-p-torsion-affine-curve-characteristic.proof |
| `sec-Normalization` | `sec-Comparison-with-the-etale-site` | Finite direct image statements are transported to the pro-etale site by Theorem bounded-below-cohomology-comparison. | lemma-finite-morphisms-cohomology.proof |
| `sec-Normalization` | `sec-Proper-morphisms` | Lemma finite-morphisms-cohomology: by Lemma finite-morphisms h_* is exact, stalks are products, commutes with base change | proof of lemma-finite-morphisms-cohomology |
| `sec-Normalization` | `sec-Kummer-theory` | 'All assertions of Theorem cohomology-curves for constant F_l follow from the calculations on smooth curves': the proper case l!=p is the Kummer proposition. | prose-D-13, prose-D-05 |
| `sec-Normalization` | `sec-Affine-curves` | The smooth-curve calculations for l!=p include affine curves (Proposition cohomology-smooth-affine-curve, prose-D-05), to which normalization reduces. | prose-D-13, prose-D-05 |
| `sec-Normalization` | `sec-The-Artin-Schreier-sequence` | For l=p, the smooth-curve calculation reduced to by normalization is the Artin-Schreier one (prose-D-09). | prose-D-13, prose-D-09 |
| `sec-Extension-by-zero` | `sec-Normalization` | The term supported on Z has no higher cohomology by Lemma sheaves-finite-support; j_!F_l is handled via Lemmas normalization-constant-sheaf and finite-morphisms-cohomology. | lemma-removing-finitely-many-points.proof, prose-D-15 |
| `sec-Reduction-to-constant-coefficients` | `sec-Constructible-sheaves` | G is the pullback of a finite etale local system by Proposition locally-constant-sheaves-finite-presentation, hence a monodromy representation. | lemma-reduction-unipotent-local-system.proof |
| `sec-Reduction-to-constant-coefficients` | `sec-Extension-by-zero` | The graded pieces j'_!F_l satisfy the assertions 'by the calculation for constant sheaves extended by zero'. | prose-D-17 |
| `sec-Devissage` | `sec-Comparison-with-the-etale-site` | 'By Theorem bounded-below-cohomology-comparison, we may work on C_et' and the conclusions are carried back to the pro-etale site. | proof/theorem-cohomology-curves/2 |
| `sec-Devissage` | `sec-Normalization` | Finite direct images (Lemma finite-morphisms-cohomology), normalization and Lemma sheaves-finite-support reduce to smooth curves. | proof/theorem-cohomology-curves/2 |
| `sec-Devissage` | `sec-Extension-by-zero` | Proof of Theorem cohomology-curves: 'By Lemma removing-finitely-many-points we may replace the sheaf by its extension by zero.' | proof/theorem-cohomology-curves/2 |
| `sec-Devissage` | `sec-Reduction-to-constant-coefficients` | Lemma reduction-unipotent-local-system reduces to constant F_l extended by zero on finite covers. | proof/theorem-cohomology-curves/2 |
| `sec-Specialization-to-the-normal-cone` | `sec-Constructible-sheaves` | Sp_{X,Z} and tau_{X,Z} on D^b_ctf are transported from the etale constructions by Theorem comparison-constructible-sheaves. | prose-E-09, prose-E-01, theorem-verdier-s-theorem-specialization-zero.proof |
| `sec-Specialization-to-the-normal-cone` | `sec-Bounded-below-complexes` | Invertibility of the nearby-cycle base change maps for smooth g uses smooth base change for torsion coefficients. | prose-E-03 |
| `sec-Kunneth-formula-for-nearby-cycles` | `sec-The-Kunneth-formula` | On the geometric fibres the ordinary external Künneth formula is used. | prose-E-10 |
| `sec-Kunneth-formula-for-nearby-cycles` | `sec-Specialization-to-the-normal-cone` | Uses the geometric nearby cycles functor and its base change maps set up there; Pi_{L,M} is defined by those base change maps. | prose-E-10, prose-E-02, prose-E-03 |
| `sec-Base-change-for-nearby-cycles` | `sec-The-exceptional-Kunneth-formula` | Uses the external duality isomorphism ξ:p_2^*ω_X→p_1^!A_X of Lemma external-duality-trace-morphism. | prose-E-16 |
| `sec-Base-change-for-nearby-cycles` | `sec-Compactifications` | nu_f is defined by choosing a relative Nagata compactification f=ph and is independent of it via common refinements. | prose-E-15 |
| `sec-Base-change-for-nearby-cycles` | `sec-Specialization-to-the-normal-cone` | alpha_f is 'the base change map for pullback of i*Rj_*' introduced there; chi, nu, beta are built from it. | prose-E-15, prose-E-03 |
| `sec-Duality-for-nearby-cycles` | `sec-Proof-of-smooth-purity` | On the smooth ambient space, smooth purity identifies theta with the identity of the dualizing complex, giving the twist A(1)[2]. | lemma-nearby-duality-slice.proof, prose-E-21 |
| `sec-Duality-for-nearby-cycles` | `sec-Verdier-biduality` | Lemmas restriction-geometric-generic-fibre and double-dual-geometric-generic-fibre applied on each geometric fibre. | prose-E-21 |
| `sec-Duality-for-nearby-cycles` | `sec-Kunneth-formula-for-nearby-cycles` | Same argument as the Kunneth formula, using Lemmas finite-support-global-sections and quasi-finite-coordinates and the slicing formula (E.2). | proposition-nearby-cycles-commute-verdier-duality.proof, prose-E-19 |
| `sec-Duality-for-nearby-cycles` | `sec-Base-change-for-nearby-cycles` | delta_{X,M} is built from chi_f, nu_f, beta_f, mu_X and theta_X 'of the preceding subsection'. | prose-E-18, lemma-nearby-duality-proper-direct-image |
| `sec-Specialization-of-the-trace-class` | `sec-The-exceptional-Kunneth-formula` | Specialization of the trace class is built from P_X, λ_K and e_K of external duality and Definition trace-morphism. | prose-E-23; proof of proposition-specialization-trace-class |
| `sec-Specialization-of-the-trace-class` | `sec-Trace-classes-and-local-terms` | The proposition compares the trace classes Tr_{c_s}(u_s) and Tr_{c_eta}(u) defined there. | proposition-specialization-trace-class |
| `sec-Specialization-of-the-trace-class` | `sec-Specialization-to-the-normal-cone` | Corollary specialization-when-fixed-point-scheme uses Lemma nearby-cycles-constant-family. | corollary-specialization-when-fixed-point-scheme.proof |
| `sec-Specialization-of-the-trace-class` | `sec-Kunneth-formula-for-nearby-cycles` | Nearby cycles commute with external products by Proposition external-kunneth-formula-nearby-cycles. | prose-E-22, prose-E-23 |
| `sec-Specialization-of-the-trace-class` | `sec-Base-change-for-nearby-cycles` | u_s is built from alpha, beta and the identities of the four lemmas of that section. | prose-E-22, proposition-specialization-trace-class, prose-E-15 |
| `sec-Specialization-of-the-trace-class` | `sec-Duality-for-nearby-cycles` | Nearby cycles commute with Verdier duality by Proposition nearby-cycles-commute-verdier-duality. | prose-E-22, prose-E-23 |
| `sec-Contracting-correspondences` | `sec-Trace-classes-and-local-terms` | Local terms of contracting correspondences via Theorem proper-pushforward-lefschetz-verdier and trace classes. | proof of theorem-contracting-correspondences-local-terms |
| `sec-Contracting-correspondences` | `sec-Additivity-of-trace-classes` | Closed graded piece is the proper pushforward of u_Z (Lemma closed-piece-pushforward); restriction to Z as before Lemma lift-correspondence. | proof of theorem-contracting-correspondences-local-terms; prose-E-29 |
| `sec-Contracting-correspondences` | `sec-Specialization-to-the-normal-cone` | Verdier's theorem identifies Sp_{X,Z}(K) on the zero section with K\|_Z. | theorem-contracting-correspondences-local-terms.proof |
| `sec-Contracting-correspondences` | `sec-Specialization-of-the-trace-class` | Proposition specialization-trace-class and Corollary specialization-when-fixed-point-scheme transfer the trace class to the normal cone. | theorem-contracting-correspondences-local-terms.proof |
| `sec-Lie-algebras` | `sec-Smoothness-and-components` | Stable subspaces and center: compares closed subgroups with G via Lemma connected-components-images-homomorphisms(3) and Cartier's theorem. | lemma-stable-subspaces-center.proof, prose-F-04 |
| `sec-Reductive-Lie-algebras` | `sec-Cartans-criterion` | Killing form nondegenerate by Cartan's criterion; the radical is central via a common eigenvector from Lie's theorem. | lemma-killing.proof, proposition-lie-algebras-faithful-semisimple-representation.proof |
