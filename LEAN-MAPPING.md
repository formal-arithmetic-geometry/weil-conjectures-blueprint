# Lean names and dependencies of the declarations

How the `lean` and `uses` attributes of `blueprint/` were filled in, and how sure each Lean match is.

## Method

- **Lean names.** Each declaration was matched with the sketch node of `blueprint_old/` that states it, and that node's `lean` list (and its detail nodes') was checked against the Lean statements at the pinned revision of weil-conjectures. Names that only serve the proof were dropped. Where the old blueprint had none, the formalisation was searched for a declaration that states it. Every name exists at the pinned revision, and no name belongs to two declarations.
- **Coverage.** 421 of 538 declarations have Lean names: 233 high, 148 medium and 40 low confidence. Medium and low mean the Lean states only part of the declaration, a special case, or a variant (often with other coefficients); the notes below say which. 117 declarations, mostly examples and remarks, have none.
- **Declaration arrows** follow the citations of the natural-language notes, not Lean: `A uses B` when the statement or a proof of A cites B and uses it. Arrows with a definition at either end are left out for now. See `CITATION-CHECK.md`. The Lean names above are unchanged; `blueprint check --lean` will report where Lean depends on other declarations than the notes cite.
- **Cycles.** The citation arrows have no cycle; citations that only point ahead or take over a setting are not arrows (`CITATION-CHECK.md`).
- **Sections and subsections** have arrows only where the notes relate the two sections themselves: the text of the section (its own prose, not its declarations) says that one section uses or builds on the other. Arrows between their declarations do not make an arrow between the sections. Forward pointers ("proved below", "treated in Section X"), the scope of a convention, examples, analogies and the introduction's roadmap give none. The 31 arrows are listed at the end. Chapters keep the arrows written on them by hand.
- **No circular reasoning.** No chain of arrows returns to where it started: there is no cycle among the declarations, among the sections and subsections, or in all of them together. The two-way section arrows before came from merging all declaration arrows of a section into section arrows; two sections whose declarations use each other's in both directions got arrows both ways.

## Declarations

### The pro-étale site

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `definition-ind-etale-pro-etale-weakly` | 8 | high | sk-def-pe-morphisms definitions; comparison lemmas moved to proposition-etale-implications |
| `proposition-etale-implications` | 4 | medium | old sketch empty; ind-etale=>weakly etale (ring), etale=>weakly etale and weakly etale+lfp=>etale (scheme form, det-pe-morphisms-etale-comparison) |
| `lemma-stability` | 4 | medium | sk-lem-pe-weakly-etale-stability; scheme base change/composition/Zariski locality are unnamed Mathlib instances |
| `definition-small-pro-etale-site` | 3 | high | sk-def-pe-site |
| `proposition-pro-etale-coverings` | 3 | medium | old sketch empty; finite affine refinement (qcqs form) and etale/Zariski precoverage comparisons |
| `proposition-topos-functoriality` | 6 | medium | toposFunctorialityInverseImage cites det-pe-topos-functoriality-inverse-image; plus abelian adjunction/exactness from old sketch |
| `definition-w-local-w-strictly-local` | 5 | high | sk-def-pe-wlocal / det-pe-wlocal-strict-contractible |
| `proposition-w-local-components` | 2 | medium | parts (1) and (3); part (2) not found |
| `example-locally-constant-functions-w-local` | 0 | — | example; no exact formalization |
| `proposition-gleason-s-theorem` | 2 | high | sk-prop-pe-stonean / det-pe-stonean-projective (Mathlib) |
| `lemma-extremally-disconnected-covers` | 4 | medium | det-pe-stonean-cover; Stonean presentation of CompHaus, Stonean spaces are profinite (Mathlib) |
| `proposition-splitting-ind-etale-covers` | 1 | high | sk-prop-pe-wc-rings |
| `theorem-existence-contractible-covers` | 1 | high | sk-thm-pe-wc-cover; stage lemmas dropped |
| `theorem-pro-etale-refinements-weakly-etale` | 2 | high | sk-thm-pe-indetale-refinement |
| `proposition-pro-etale-affines-form-basis` | 4 | high | sk-prop-pe-affine-basis |
| `lemma-w-contractible-affines-projective` | 2 | high | det-pe-wcb-projective (second cites it in docstring) |
| `theorem-enough-affine-weakly-contractible-objects` | 2 | high | det-pe-wcb-cover; covering half of sk-thm-pe-weakly-contractible-basis |
| `definition-weak-contractibility` | 2 | high | sk-def-pe-weak-contractible; equivalences cite det-pe-weak-contractible-equivalences |
| `example-weak-contractibility-point` | 0 | — | example; not formalized |
| `corollary-evaluation-weakly-contractible-objects` | 4 | medium | parts (1),(2),(3); peSectionsLimitsColimits and sections_conservative cite det-pe-sections-* nodes |
| `definition-repleteness` | 1 | high | sk-def-pe-replete |
| `proposition-repleteness-pro-etale-topos` | 1 | high | sk-prop-pe-replete |
| `proposition-exact-products` | 2 | high | cite det-pe-products-exact / det-pe-products-derived; replace old countable-only names |
| `proposition-milnor-sequence` | 4 | high | sk-prop-pe-milnor; milnor_sequence/milnor_epimorphic cite det-pe-milnor-* nodes |
| `example-nonzero-rlim-one` | 0 | — | example; not formalized |
| `proposition-left-completeness` | 2 | high | sk-prop-pe-left-complete / det-pe-left-complete-iso |
| `proposition-unbounded-functors-products` | 2 | low | old sketch empty; only Rf_* preserves derived limits found, nothing for RGamma(U,-) |
| `proposition-weakly-contractible-hypercovers` | 2 | medium | old sketch empty; hypercover existence cites det-pe-hypercover-existence; (2.3) via hypercover total complex |
| `corollary-continuity-cohomology` | 1 | low | only sheaf (not bounded complex) case of the R^q f_* assertion found (det-pe-bounded-continuity-direct-image) |
| `definition-classical-pro-etale-sheaves` | 4 | medium | cite sk-def-pe-classical-definition / det-pe-classical-definition-continuity-map |
| `proposition-comparison-morphism-inverse-image` | 7 | high | sk-prop-pe-comparison-morphism |
| `theorem-classical-sheaves-essential-image` | 5 | high | sk-thm-pe-classical-sheaves; first two cite it / det-pe-classical-sheaves-modules |
| `example-coefficient-sheaf-outside-classical-part` | 0 | — | example/remark; not formalized |
| `lemma-acyclicity-pulled-back-injectives` | 1 | high | sk-lem-pe-injective-acyclicity |
| `theorem-bounded-below-cohomology-comparison` | 3 | high | sk-prop-sf-comparison (boundedBelowComparison cites it) |
| `corollary-cohomology-pro-etale-affine` | 0 | — | sk-cor-pe-affine-continuity had no Lean; nothing found |
| `corollary-bounded-below-classical-complexes` | 1 | medium | cites det-pe-classical-derived-equivalence; weak Serre part not separately found |
| `theorem-comparison-direct-images` | 3 | medium | sk-thm-pe-direct-image-comparison; directImageComparisonAmbient* cite it |
| `lemma-comparison-direct-images-compatibilities` | 0 | — | only private lemmas (ProEtaleDirectImageMateCompatibility) found |
| `proposition-comparison-immersions` | 1 | low | only part (1) (2.10) found; old sketch empty |
| `lemma-torsors-under-classical-groups` | 0 | — | sk-lem-pe-torsor-comparison had no Lean; nothing found |
| `proposition-locally-constant-sheaves-finite-presentation` | 1 | low | sheaves-of-sets form: locally constant => classical with etale trivializing cover; old sketch empty |
| `theorem-comparison-constructible-sheaves` | 1 | high | cites sk-thm-pe-constructible-comparison |
| `corollary-finite-tor-amplitude-under-comparison` | 1 | medium | cites det-pe-finite-tor-comparison-noetherian; old fact names no longer exist |
| `definition-cohomological-dimension` | 2 | high | cite sk-def-cd |
| `lemma-cohomological-dimension-base-field` | 1 | high | cites sk-lem-base-field-cd |
| `lemma-uniform-bounds-pro-etale-affines` | 1 | low | only last assertion cd_l(g)<infinity found |
| `lemma-truncation-pro-etale-sections` | 0 | — | det-pe-unbounded-classical-truncation had no Lean; nothing found |
| `proposition-unbounded-comparison-finite-coefficients` | 0 | — | sk-prop-pe-unbounded-classical had no Lean; only bounded-below direct image iso found |
| `proposition-pro-etale-site-separably-closed` | 3 | medium | old sketch empty; dense profinite subsite, topos equivalence, constant=continuous for discrete coefficients |
| `lemma-comparison-completed-coefficients` | 1 | high | cites sk-prop-sfb-qlbar-colimit-x; old padic*RingObj defs dropped |
| `corollary-finite-quotients-their-transition-maps` | 1 | medium | det-pe-derived-nakayama-resolution: exact sequence, transitions, all X |
| `definition-tate-twists` | 6 | high | sk-def-sp-tate-twist; spTwists_locallyFree for rank-one local freeness |
| `lemma-inverse-image-coefficient-sheaves` | 3 | high | sk-prop-sfb-cartesian-coefficients (cartesianCoefficients cites it) |
| `proposition-continuous-cohomology-pro-etale-cohomology` | 0 | — | old sketch listed proof steps only (isHomotopyLimit_mapCone_Q_of_epi, IsHomotopyLimit.map); no statement found |
| `corollary-continuous-etale-cohomology` | 0 | — | sk-cor-pe-continuous-etale had no Lean |
| `example-first-cohomology-finite-field` | 0 | — | remark/example; not formalized |
| `proposition-extension-zero-restriction-closed-subscheme` | 10 | medium | sk-prop-sf-open-closed-triangle; RingSheaf versions match sheaf-of-rings statement part by part |
| `definition-local-cohomology` | 2 | medium | det-lem-formal-closed-support-adjunction: RGamma_Z with fibre formula |
| `lemma-local-cohomology-right-adjoint` | 1 | medium | det-lem-formal-closed-support-adjunction: i_* -\| RGamma_Z on derived categories |
| `definition-derived-adic-completeness` | 2 | high | sk-def-pe-derived-completion |
| `lemma-reduction-derived-nakayama` | 1 | high | cites det-pe-derived-nakayama-first-reduction; cone part is in derived_nakayama_resolution (given to corollary) |

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
| `definition-compactification-refinement` | 5 | high | Old sk-def-nagata-sketch-data; IsStrict encodes h^{-1}(X)=X; dropped category API. |
| `theorem-nagata-s-compactification-theorem` | 2 | high | Old sk-thm-nagata-compactification lean list. |
| `lemma-schematic-closure-uniqueness` | 4 | high | Old sk-lem-nagata-sketch-closure (closure part) plus detail ker_morphismRestrict for restriction to opens. |
| `lemma-uniqueness-maps-dense-open` | 3 | high | Uniqueness half of old sk-lem-nagata-sketch-closure, plus its detail and Chow detail forms. |
| `lemma-passing-schematic-closure` | 4 | medium | Old sk-lem-nagata-density-normalization; Lean states bounded constructible case over k only. |
| `remark-non-noetherian-compactifications` | 0 | — | Remark; old sk-rem-nagata-closure-scope had no lean. |
| `proposition-dense-compactifications-form-cofiltered-category` | 3 | high | Old sk-prop-nagata-sketch-comp-category lean list. |
| `remark-base-change-compactification` | 0 | — | Remark; old sk-rem-nagata-base-change had no lean. |
| `definition-admissible-blow-up` | 3 | high | Old sk-def-nagata-admissible lean list. |
| `lemma-making-open-schematically-dense` | 3 | high | Old sk-lem-nagata-boundary-divisor plus detail stating density of preimage directly. |
| `example-blow-up-embedded-point` | 0 | — | Example; nothing states it. |
| `definition-strict-transform` | 1 | medium | Old detail def-nagata-strict-transform; Lean defines it as scheme-theoretic closure of the part over U. |
| `lemma-products-composites-u-admissible-blow` | 4 | high | Old sk-lem-nagata-sketch-blowups lean list. |
| `definition-quasi-domination` | 1 | high | Old detail def-nagata-conrad-quasi-domination (Extends not part of the tex definition). |
| `proposition-relative-form-zariski-s-main` | 2 | high | Old details lemma-nagata-zmt-open-immersion-affine-factorization and quasi-affine morphism lemma. |
| `theorem-extension-partial-section` | 1 | high | Old detail thm-nagata-conrad-elimination (sketch had none); Lean adds Y qcqs. |
| `corollary-extension-proper-target` | 1 | high | Old sk-cor-nagata-sketch-proper-extension. |
| `theorem-elimination-indeterminacy` | 1 | high | Old sk-lem-nagata-sketch-elimination; Lean omits the density clause. |
| `lemma-extending-graph-from-compactification` | 2 | high | Old sk-lem-nagata-sketch-graph plus graph-extension structure detail. |
| `lemma-separation-closures` | 1 | high | Old sk-lem-nagata-sketch-boundary. |
| `lemma-extending-isomorphism-over-closure-closed` | 1 | high | Old sk-lem-nagata-sketch-near-closure. |
| `lemma-gluing-after-admissible-blow-ups` | 2 | high | Old sk-lem-nagata-sketch-common. |
| `proposition-compactifying-union-two-opens` | 1 | high | Old sk-thm-nagata-sketch-two-open. |
| `lemma-affine-covers-dense-intersection` | 3 | medium | Old sk-lem-nagata-sketch-affine-cover plus existence detail; compactification is not stated projective. |
| `theorem-chow-s-lemma-projective-form` | 3 | medium | Old sk-thm-chow-projective; no single proper-qcqs closed-immersion statement in Lean, parts only. |

### Abelian varieties

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `example-cube-two-factors` | 0 | — | Example; nothing formalizes it. |
| `lemma-triviality-fibres` | 2 | high | sk-lem-abelian-seesaw: part (1) criterion and part (2) closedness, general proper flat base. |
| `corollary-triviality-over-open-cover-base` | 0 | — | sk-cor-abelian-seesaw-descent: old detail says not formalized; Lean glues along a section instead. |
| `lemma-h-1-structure-sheaf-product` | 0 | — | Not formalized as stated; Lean only proves H^1 vanishing of a cross ideal (Kunneth.subsingleton_H_one_toModules_prodIdeal), a proof input. |
| `lemma-triviality-near-fibre` | 1 | high | sk-lem-abelian-cube-open; stated for M,N isomorphic on slices; rational-point variant dropped. |
| `theorem-theorem-cube` | 1 | high | sk-prop-av-cube / thm-av-cube-general. |
| `lemma-rigidity` | 1 | high | sk-prop-av-rigidity: local rigidity (neighbourhood V); global exists_eq_snd_comp dropped. |
| `definition-abelian-variety` | 3 | high | sk-def-av: class, geometric connectedness bridge, A[n]; symmetric sheaves are only a hypothesis in Lean. |
| `lemma-abelian-variety-commutative` | 2 | high | Details of sk-prop-av-mult-n-pullback: geometric integrality and commutativity. |
| `lemma-symmetric-ample-sheaf` | 4 | high | Details of sk-prop-av-mult-n-pullback: projectivity, ample sheaf, symmetrisation ample and symmetric. |
| `proposition-pullback-multiplication-n` | 1 | medium | lem-sc-mult-n-pullback: only the symmetric case [n]^*N = N^{n^2}; general formula not formalized. |
| `proposition-multiplication-n` | 8 | high | sk-prop-av-isogeny lean list, all parts of the statement. |
| `definition-tate-module` | 3 | high | def-wf-abelian-tate-module: T_l, V_l and identification with limit of A[l^n](kbar). |
| `proposition-integral-tate-module` | 4 | medium | sk-prop-av-tate-rank lean list; T/l^n quotient iso and field-independence not separately stated. |
| `proposition-no-frobenius-fixed-vector` | 3 | high | sk-p-tate lean list: T_l and V_l fixed parts vanish, F^m-1 automorphism. |

### The Picard scheme of a curve

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `definition-relative-picard-functor` | 2 | high | sk-def-picard-pic / def-pc-picard-functor: fppf sheafification of the Picard presheaf. |
| `lemma-rigidification-along-section` | 8 | medium | sk-prop-picard-pic-split list minus isIso_pushforwardUnitMap..geometricallyIntegral (hypothesis check, helper). |
| `theorem-riemann-roch-coherent-serre-duality` | 5 | medium | sk-thm-picard-rr: kept RR, duality, deg omega, large-degree consequences; dropped degree/ampleness helpers. |
| `corollary-serre-duality-field-extension` | 2 | low | Pairing compatibility not formalized (old detail lean=[]); names state dim H^0(omega)=g and genus base-change invariance. |
| `lemma-coherent-base-change-invertible-sheaves` | 7 | medium | sk-thm-picard-perfect lean list (perfectness, derived base change, open locus, invertibility, R^1=0). |
| `theorem-hilbert-schemes-points-smooth-curve` | 4 | medium | sk-thm-picard-hilb-curves + thm-pc-hilb-curves; addition map dropped, universal divisor added. |
| `proposition-divisors-degree-g-open-chart` | 3 | medium | sk-thm-picard-f-representable; Hilbert representability helper dropped, map W->Pic added. |
| `lemma-twisting-h-0-1-h` | 1 | high | sk-thm-picard-twist / lem-pc-twist. |
| `lemma-representability-picard-functor` | 1 | medium | thm-pc-picard-representable; covering by translates is internal to the proof. |
| `lemma-tangent-space-picard-functor` | 1 | high | Found in Picard/DualNumbers.lean: ker(Pic(X[eps])->Pic(X)) = H^1(X,O_X). |
| `theorem-picard-scheme-jacobian-over-separably` | 6 | medium | sk-thm-picard-main list; isRepresentable_picardFunctor moved to the representability lemma; degree decomposition added. |
| `corollary-degree-jacobian` | 4 | high | sk-cor-picard-degree / lem-sc-pic-proper-decomposition; exists_jacobian dropped (belongs to main theorem). |
| `example-degree-sequence-genus-zero-one` | 0 | — | Example; nothing formalizes it. |
| `example-two-torsion-elliptic-curve` | 0 | — | Example; nothing formalizes it. |
| `corollary-torsion-jacobian-field-extension` | 4 | medium | sk-cor-jacobian-torsion list minus generic abelian-variety torsion helpers. |
| `proposition-jacobian-over-ground-field` | 3 | medium | sk-prop-jacobian-descent / thm-pd-jacobian-general-field; Galois-equivariance via exists_jacobian_galoisAction. |
| `proposition-h-1-curve-tate-module` | 2 | low | Old detail lem-wf-curve-kummer-jacobian-tate-module; Lean: H^1(mu_m)=Pic[m] plus transition compatibility, no Galois/limit form. |

### Cohomology of torsion sheaves on curves

| Declaration | Lean names | Confidence | Note |
|---|---|---|---|
| `lemma-cohomology-multiplicative-group` | 3 | high | sk-thm-br lean list. |
| `proposition-smooth-proper-curves-torsion-prime` | 1 | high | sk-thm-curveestimate: single theorem bundling all parts. |
| `remark-twists-projective-line` | 0 | — | Remark; nothing states it. |
| `proposition-cohomology-smooth-affine-curve` | 5 | medium | sk-prop-curve-affine-kummer lean list. |
| `proposition-p-torsion-smooth-proper-curve` | 5 | medium | sk-prop-curve-artin-schreier lean list; last two are general-coefficient forms of finiteness/invariance. |
| `lemma-p-torsion-affine-curve-characteristic` | 1 | medium | sk-lem-curve-affine-artin-schreier: only the q>1 vanishing is stated; H^1 quotient formula not formalized; AS-sequence helpers dropped. |
| `example-affine-line-characteristic-p` | 0 | — | Example (old sk-rem-curve-wild-example had no lean). |
| `lemma-finite-morphisms-cohomology` | 1 | medium | From sk-lem-curve-finite-support list: exactness, base change, Rh_*=h_* (etale site, not pro-etale). [merge: exactness/base change kept on lemma-finite-morphisms] |
| `lemma-sheaves-finite-support-finite-morphisms` | 2 | medium | From sk-lem-curve-finite-support: zero-dimensional cohomology and field-extension invariance (stated on 0-dim schemes). |
| `lemma-normalization-constant-sheaf` | 1 | medium | Old detail lemma-weil-pbc-normalization-exact-sequence: mono with constructible cokernel off a dense open; branch formula not stated. |
| `lemma-removing-finitely-many-points` | 1 | high | sk-lem-curve-dense-open; open-closed short exact sequence helper dropped. |
| `lemma-reduction-unipotent-local-system` | 1 | high | sk-lem-curve-sylow-trace. |

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
| `proposition-cartier-s-theorem` | 6 | high | sk-i-cartier list minus GrpObj.lieEquiv_mul (helper). |
| `lemma-connected-components-images-homomorphisms` | 8 | high | sk-p-geometry list minus equal-dimension helper isIso_left_of_topologicalKrullDim_eq. |
| `lemma-stable-subspaces-center` | 2 | high | sk-p-comparison. |
| `lemma-lie-s-theorem` | 1 | high | sk-lem-walg-lie-eigenvector. |
| `lemma-engel-s-theorem` | 1 | high | sk-lem-walg-engel. |
| `lemma-cartan-s-criterion` | 1 | high | sk-lem-walg-trace-criterion. |
| `lemma-killing` | 1 | medium | sk-lem-walg-killing detail; perfectness [l,l]=l not separately stated in Lean. |
| `proposition-lie-algebras-faithful-semisimple-representation` | 2 | high | sk-p-lie. |

## Section arrows

| Section | uses | Because the notes say |
|---|---|---|
| `sec-Classical-sheaves` | `sec-Affine-bases` | The comparison theorems of Section [sec-Classical-sheaves] are proved on such affines. (`prose-02-15`) |
| `sec-Unbounded-complexes` | `sec-Comparison-with-the-etale-site` | Bounds on cohomological dimension are needed only for unbounded complexes (Section [sec-Unbounded-complexes]). (`prose-02-32`) |
| `sec-Constructible-sheaves` | `sec-Direct-images` | For extension by zero this follows from the comparisons of Section [sec-Direct-images]. For extensions it is Corollary [corollary-bounded-below-classical-complexes], which uses that $R^1\nu_{X,*}$ vanishes on classical sheaves. (`prose-02-41`) |
| `sec-Field-coefficients` | `sec-Derived-functors` | By dévissage we reduce statements about $\Dbc(X,\Lambda)$ to the simplest constructible sheaves, namely lisse sheaves extended by zero from a stratum, the sheaves $a_!L$ of Section [sec-Derived-functors]. (`prose-03-18`) |
| `sec-Compactness-of-constructible-complexes` | `sec-Continuity-of-Ext` | Besides the uniform bound $\Ext^q(C,N)=0$ for $q>d_C$ and all constructible $N$ (Lemma [lemma-uniform-ext-bound] below), we use that $\Ext^q(C,-)$ commutes with filtered colimits of complexes that vanish below a fixed degree, in particular of sheaves (Lemma [lemma-continuity-ext-out-constructible-co… (`prose-05-06`) |
| `sec-Integral-models` | `sec-Constructibility` | Recall from Proposition [proposition-integral-constructibility-criterion] in Section [sec-Constructibility] that an object lies in $\Dbc(X,\mathcal O_E)=D^b_{\mathrm{ctf}}(X,\mathcal O_E)$ precisely when it is derived complete and its reduction modulo $\pi_E$ is a bounded constructible complex pulle… (`prose-03-30`) |
| `sec-Direct-image-with-compact-support` | `sec-Proper-direct-image` | We need to know, for every admissible coefficient ring, that $Rp_*$ preserves $D^b_{\mathrm{ctf}}$ and satisfies proper base change and the projection formula there, because the construction of $Rf_!=Rp_*\circ j_!$ in Section [sec-Direct-image-with-compact-support] starts from these facts. (`prose-04-42`) |
| `sec-Direct-image-with-compact-support` | `sec-Compactness-of-constructible-complexes` | For this reason, here and in Section [sec-Direct-image-with-compact-support], we carry out truncation arguments among complexes with ind-constructible cohomology sheaves. (`prose-05-12`) |
| `sec-Brown-representability` | `sec-Direct-image-with-compact-support` | For $\mathcal O_E$ it uses the compactness proved in Section [subsec-Integral-coefficients] by reduction to torsion coefficients. Compactness enters a second time. (`prose-05-33`) |
| `sec-Conventions-2` | `sec-Direct-images` | These operations are the cohomology (Theorem [theorem-bounded-below-cohomology-comparison]); the direct images and their base change maps, also for unbounded complexes (Theorem [theorem-comparison-direct-images] and Proposition [proposition-unbounded-comparison-finite-coefficients]); and the inverse… (`prose-06-02`) |
| `sec-Duality-for-the-projective-line` | `sec-Conventions-2` | As explained in Section [sec-Conventions-2], we work on the étale sites of $S$, $\mathbf P^1_S$ and $\mathbf P^1_S\times_S\mathbf P^1_S$, and transport the results to the pro-étale site at the end. (`prose-06-07`) |
| `sec-ell-adic-coefficients-2` | `sec-Finite-coefficients-2` | The argument of Section [sec-Finite-coefficients-2] uses two geometric facts, namely the finiteness of $Rj_*$ for an open immersion and the adjunction for the projective line. We deduce both from the case of torsion coefficients. (`prose-06-19`) |
| `sec-ell-adic-coefficients-2` | `sec-Direct-image-with-compact-support` | The integral case also uses the structure of integral constructible complexes and the fact that proper direct image preserves direct sums (Section [subsec-Integral-coefficients]). (`prose-06-19`) |
| `subsec-Finiteness-of-f` | `subsec-Integral-coefficients` | For $\mathcal O_E$ we also need the projection formula on the localizing categories, which follows from the case of $\Dbc$ and the results of Section [subsec-Integral-coefficients]. (`prose-06-24`) |
| `sec-The-base-change-map-2` | `sec-ell-adic-coefficients-3` | Since the map is built from units and counits, it is compatible with all three, by Lemma [lemma-naturality-pasting-comparison] for the first two and by Lemma [lemma-change-coefficients] in Section [sec-ell-adic-coefficients-3] below for the third. Consider a cartesian square, with $X'=Y'\times_YX$, … (`prose-08-02`) |
| `sec-The-base-change-map-2` | `sec-The-base-change-map` | 5) of Section [sec-The-base-change-map], for $K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$. (`prose-08-02`) |
| `sec-Torsion-sheaves` | `sec-Change-of-base-field` | For $q=1$ it follows from the invariance of $H^1$ of curves and an extension theorem for covers (Section [sec-Change-of-base-field]). (`prose-08-04`) |
| `sec-Statement` | `sec-Conventions-2` | Proper base change, the projection formula and the localization triangle are the identities of Section [sec-Conventions-2], which we may prove on the étale sites by Proposition [proposition-comparison-etale-derived-category]. (`prose-09-05`) |
| `sec-The-trace-map-of-affine-space` | `sec-Conventions-2` | The geometric computations with finite coefficients in Section [sec-Conventions-2] are stated on the pro-étale site and proved by calculations on the étale site. (`prose-09-09`) |
| `sec-ell-adic-coefficients-4` | `sec-The-trace-map-of-affine-space` | In Section [sec-ell-adic-coefficients-4] we use this gluing to realize the compatible counits with finite coefficients as a single map of towers. On a vector bundle, the choice of a local trivialization transports (9.11) to a trace map. (`prose-09-09`) |
| `sec-Compatibilities` | `sec-Finite-coefficients-3` | The trace map in Section [sec-Compatibilities] relies on it as well. We prove the agreement for a vector bundle, where both orientations can be computed, and reduce a coordinate chart to the vector bundle $\mathbf A^d_Y$ by naturality. *Vector bundles.* Let $\pi:V\to S$ be a vector bundle of rank $d… (`prose-09-16`) |
| `sec-ell-adic-coefficients-5` | `sec-Traces-of-perfect-complexes` | This is how we pass from the trace formula over $\mathcal O_E/\pi_E^n$ to the trace formula over $\mathcal O_E$ and $E$ (Section [sec-ell-adic-coefficients-5]). (`prose-11-02`) |
| `sec-Frobenius-correspondences` | `sec-Weil-complexes` | The operator $T_{c_m}(\psi_m)$ is defined with the $k$-linear $\Phi_X$, while the Frobenius operator of Section [sec-Weil-complexes], whose trace the theorem is about, is defined with $\operatorname{Fr}_X$. (`prose-12-04`) |
| `sec-Weil-sheaves-and-weights` | `sec-Weil-complexes` | Geometric Frobenius, Weil complexes and their Frobenius operators are those of Section [sec-Weil-complexes]. (`situation-weil`) |
| `sec-Determinant-weights` | `sec-Sheaves-of-rank-one` | From the geometry of the curve we use only one fact, proved in Section [sec-Sheaves-of-rank-one]: the geometric fundamental group acts through a finite group on every determinant. (`prose-14-12`) |
| `sec-Rankins-bound` | `sec-Sheaves-of-rank-one` | The later subsections Sections [sec-Determinant-weights]–[sec-Exterior-powers-and-purity] are built on it. In rank one the question is about characters. (`prose-14-02`) |
| `sec-Exterior-powers-and-purity` | `sec-Sheaves-of-rank-one` | The later subsections Sections [sec-Determinant-weights]–[sec-Exterior-powers-and-purity] are built on it. In rank one the question is about characters. (`prose-14-02`) |
| `sec-Rankins-bound` | `sec-Determinant-weights` | This subsection proves the two facts about determinant weights that Rankin's argument in Section [sec-Rankins-bound] needs for the tensor and exterior powers of a real sheaf $\mathcal G$. (`prose-14-11`) |
| `sec-Exterior-powers-and-purity` | `sec-Determinant-weights` | In Section [sec-Exterior-powers-and-purity] we use this bound, and part (2), for the constituents of a real sheaf before we know that they are pure. (`prose-14-22`) |
| `sec-Proper-morphisms` | `sec-Chows-lemma` | In Section [sec-Proper-morphisms] proper base change is first proved for projective morphisms. (`prose-A-25`) |
| `sec-Specialization-of-the-trace-class` | `sec-Base-change-for-nearby-cycles` | They commute with external products by Proposition [proposition-external-kunneth-formula-nearby-cycles], with Verdier duality by Proposition [proposition-nearby-cycles-commute-verdier-duality], and with the four operations through the base change maps of Section [sec-Base-change-for-nearby-cycles]. … (`prose-E-22`) |
