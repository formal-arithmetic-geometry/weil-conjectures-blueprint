# Alignment of the sketch layer with `DerivedCategoryAndSixFunctorsChoice_readable.tex`

This file records how the sketch layer of the blueprint was aligned with the declarations of
`DerivedCategoryAndSixFunctorsChoice_readable.tex`. It also lists the top-level nodes that exist only in the
blueprint.

## Scope and conventions

- **Blocks.** The aligned blocks are those that were numbered 1–5 and 7–9 before this change: Nagata
  Compactification, Abelian Varieties, Picard Framework, Curve Estimates, Proper Base Change, Six Functors: Basic
  Constructions, Smooth Purity and Six Functors. A new block, *The Pro-étale Site and Coefficients*
  (`sec-proetale-coefficients`, order 700), sits between Picard Framework and Curve Estimates. Smooth Base Change has
  no counterpart in the tex file; its sketches are unchanged.
- **Declarations and sketch nodes.** Every `definition`, `lemma`, `proposition`, `theorem`, `corollary`,
  `convention`, `remark` and `example` environment of the tex file (226 in total) has a sketch node. 215 sketch
  nodes cover them. Where the tex states one result twice, or a node in the blueprint duplicated another, the copies
  were merged into one node (see "Merged duplicates"), and that node stands for each of the declarations involved.
  The introduction (§1) has no declarations.
- **Kinds.** The node kind follows the tex environment; a convention becomes a `definition` and an example a
  `remark`.
- **Statements.** The sketch statement and its proof are the tex statement and proof converted to Markdown.
  Where an existing sketch was reused, its id, `lean` names and detail nodes were kept.
- **Detail nodes.** Every non-remark sketch node is a directory with at least one detail node. Some detail nodes
  were moved in from elsewhere; others were written from the tex proof (ids `det-…`). Remarks and examples are
  single leaf files, without detail nodes or `uses`, following the existing rule that remarks are leaves.
- **Order.** Inside each block, the tex-aligned sketches come first, in tex order. The blueprint-only nodes follow
  in their previous relative order.
- **Macros.** Macros of the tex preamble that KaTeX lacked were added to `blueprint.toml`. Five tex macros mean
  something else in `blueprint.toml` (`\RHom`, `\Qbar`, `\et`, `\proet`, `\Ob`); those were expanded inline instead.

## Which block holds which chapter

Blocks must form a chain: a node may only `uses` nodes in its own block or in an earlier one. The tex chapters do
not form such a chain on their own. The appendices (§11–§13) are cited by the main text and themselves cite §2 and
§4. Each declaration was therefore placed so that the chain holds:

| Tex | Block |
|---|---|
| §11 Compactification and projective domination | Nagata Compactification (except #186, see below) |
| §2 Pro-étale site, §3 Coefficients (except #35–#37, #50, #51) | The Pro-étale Site and Coefficients |
| §12 Picard schemes and Jacobians | Picard Framework, except #212 in Abelian Varieties |
| §13 Cohomology of curves | Curve Estimates |
| §4 Proper base change | Proper Base Change |
| §5–§9, #35–#37, #50, #51 | Six Functors: Basic Constructions |
| §10 Smooth purity | Smooth Purity |

Some declarations are placed by content rather than by chapter:

- **#35–#37** (the "Unbounded complexes with finite coefficients" subsection) need the uniform cohomological bounds
  of Stacks 0F0V/0F10. In the blueprint those are proved through proper base change. The tex itself says this
  subsection is needed only for Brown representability, not for proper base change, so these declarations sit in
  Six Functors: Basic Constructions.
- **#50 and #51** (the main theorem on the exceptional inverse image and its corollary) are proved in §6–§9, so they
  sit in the same block as their proofs.
- **#81** (inverse image of the coefficient sheaves) and **#186** (the pro-étale lemma of the compactification
  appendix) are coefficient and pro-étale statements, and they sit in the new block.

Six Functors now holds only blueprint-only sketches: duality, Künneth, the six-operations package and others.


## Summary

| Block | Tex-aligned sketch nodes | Tex declarations covered | Existing sketch reused | New sketch node | Blueprint-only top-level nodes |
|---|---:|---:|---:|---:|---:|
| Nagata Compactification | 18 | 19 | 13 | 5 | 13 |
| The Pro-étale Site and Coefficients | 48 | 50 | 7 | 41 | 22 |
| Abelian Varieties | 1 | 1 | 1 | 0 | 39 |
| Picard Framework | 11 | 11 | 8 | 3 | 28 |
| Curve Estimates | 13 | 16 | 2 | 11 | 17 |
| Proper Base Change | 25 | 25 | 8 | 17 | 2 |
| Six Functors: Basic Constructions | 71 | 75 | 14 | 57 | 37 |
| Smooth Purity | 28 | 29 | 4 | 24 | 13 |
| Six Functors | 0 | 0 | 0 | 0 | 38 |
| **Total** | **215** | **226** | **57** | **158** | **209** |

## Dependency structure

On this branch, no `uses` arrow points from a block to a later block, and the node-level `uses` graph has no
cycle. The first version of the alignment had 382 backward arrows and three cycles. They came from three
sources, each handled as follows.

**Reused sketches whose role changed.** Some existing sketches had been rewritten to a tex statement that comes
later in the tex and depends on later results. Nodes that cited them for their old content then closed a loop.
These four sketches were restored to their `main` statement, and the tex declaration got a new sketch:

| Restored blueprint-only sketch | New sketch for the tex declaration |
|---|---|
| `sk-def-sfb-dc-restricted-functors` (the restricted functors on $D_{\mathrm{cons}}$) | `sk-lem-int-tensor` (#141 `i:tensor`) |
| `sk-def-sfb-dc-upper-shriek` (the old construction of $Rf^!$ on $D_{\mathrm{cons}}$) | `sk-thm-existence` (#50 `n:existence`) |
| `sk-def-sfb-coefficient-comparisons` (definition of the comparison maps) | `sk-prop-scalar-six` (#149 `n:scalar-six`) |
| `sk-prop-av-ntorsion-etale` (torsion of an abelian variety) | `sk-cor-jacobian-torsion` (#213 `app:jacobian-torsion`) |

Each link to one of these ids was then pointed at whichever node it means. A link means the tex result when it
comes from a node later in the tex, and the old content otherwise.

**Arrows not backed by the tex.** These arrows lay on a cycle or crossed blocks backwards, and the tex does not
cite the target. They were removed from `uses`; any prose link stays:

- `sk-lem-coefficient-finite-descent` → `sk-thm-sfb-qlbar-two-colimit`
- `sk-thm-sfb-rationalization-comparison` → `sk-lem-integral-models`
- `sk-prop-cohsm` → `sk-prop-an`
- `sk-thm-sf-pf-field` → `sk-thm-sf-pf-adic`
- `sk-thm-int-restriction` → `sk-thm-existence` (the arrow was "this completes the proof of the existence
  theorem", a remark, not a dependency)
- `sk-def-sfb-constructible` → `sk-def-sfb-bounded-constructible` and `sk-def-sf-categories` (both "compare"
  references)
- `sk-lem-curve-finite-support` → `sk-lem-pbc-finite` (the appendix re-derives the finite stalk computation)
- `sk-thm-chow-projective` → `sk-thm-chow`, replaced by `thm-chow-lemma`, the Noetherian Chow lemma that the
  proof actually uses

**Placement of detail nodes.** Detail nodes and blueprint-only sketches were placed by an exact optimisation
(minimum cut). Every `uses` arrow must point to the same or an earlier block, and as many nodes as possible stay
where the alignment put them or where they were on `main`. Result:

- 3,591 detail nodes in total. 3,244 of them exist on `main`, and 2,838 of those are still in the sketch directory they had on `main`. Some of those directories moved block together with their tex sketch. 727 detail nodes sit in a different block than on `main`. Most of these moved for one of two reasons:
  - Smooth Purity nodes went with the §5–§9 sketches to Six Functors: Basic Constructions (276 nodes).
  - Étale and pro-étale foundations went from Six Functors: Basic Constructions, Proper Base Change and Smooth Purity into the new block.
  347 detail nodes are new on this branch.
- 36 blueprint-only top-level nodes sit in a different block than on `main`. The coefficient foundations of Six Functors: Basic Constructions moved to the new block. The setting and exchange sketches that the §5–§9 sketches build on moved from Smooth Purity and Six Functors to Six Functors: Basic Constructions. The last table marks each of them.
- The summary pages (`sec-*/_section.md`) of the blocks that now use the new block list it in their `uses`.
  This includes blocks outside the alignment, such as Trace Formula and Zeta Functions, whose nodes use étale
  foundations that now live in the new block.

## Merged duplicates

Top-level nodes that stated the same result or definition were merged into one node, and the copies were deleted.
The surviving node received each copy's detail nodes. It also received anything a copy stated beyond the survivor,
added as a "Complement" or "Moreover" paragraph together with the corresponding proof. Every reference to a deleted
id now points to the survivor.

| Surviving node | Merged and deleted | Added to the survivor |
|---|---|---|
| `sk-thm-chow-projective` (#201) | `sk-thm-chow` (#72, the affine-base case) | its detail nodes and `lean` names |
| `sk-cor-pe-bounded-continuity` (#22) | `sk-lem-bounded-continuity` (#85), `sk-lem-proper-heart-continuity` (#100) | continuity for any sheaf of rings, including $R^qp_*$, and its proof |
| `sk-thm-curve-package` (#214) | `sk-thm-pbc-curve-input` (#62) | detail nodes |
| `sk-cor-curve-invariance` (#226) | `sk-lem-pbc-curve-field-extension` (#63) | detail nodes |
| `sk-rem-curve-wild-example` (#221) | `sk-rem-pbc-characteristic-torsion` (#64) | why the field-extension step needs properness |
| `sk-thm-picard-main` (#209) | `sk-prop-jacobian` | the Jacobian complement over a separably closed field, and its proof |
| `sk-thm-sfb-qlbar-two-colimit` (#150) | `sk-lem-coefficient-finite-descent` (#88) | the statement is now the full lemma #88, with the 2-colimit as part (4) |
| `sk-prop-geo-p1-adjunction` (#119) | `sk-lem-sp-p1` (#153) | diagonal integrals, and the restriction to $\Dctf$ for $\mathbf Z/\ell^n$ |
| `sk-prop-cohsm` (#121) | `sk-prop-sp-tensor` (#158), `sk-prop-sp-exceptional-bc` (#159) | descriptions of (G11) and (G12), and the chart form of $\omega_f$ |
| `sk-lem-sf-flat-model` (#109) | `sk-lem-sf-ctf-generation` | generation over any Noetherian scheme, and its proof |
| `sk-thm-purity-transport` (#151) | `sk-prop-sp-comparison-brown` (#182) | identification with the Brown $f^!$ and uniqueness (proof step 5) |
| `sk-def-sf-weil-complexes` (#181) | `sk-def-weil` (Poincaré Duality block) | Tate data, the contragredient structure, and the warning on Hom groups |
| `sk-thm-sf-kunneth-relative` | `sk-thm-product` (Poincaré Duality block) | the supported product over a general base |
| `sk-rem-sf-fullcd-scope` | `open-sf-ambient-adjoint-input` | the pointers to where the class adjoint stops |
| `sk-…--remark-…`, `sk-rem-…` remarks | `the-final-theorem--remark-1`, `the-final-theorem-the-abelian-variety-estimate--remark-1`, `the-final-theorem-the-curve-estimate--remark-1`/`-2`, `rem-picard-seams`, `rem-sf-comp-scope`, `rem-sf-feeds`, `rem-sf-typing-rule`, `rem-sf-typing`, `rem-pur-five-moves` | nothing (identical text) |

Considered but not merged, because the statements genuinely differ:

- `sk-prop-sp-et-proet` (#155) and `sk-prop-ctf-finite-comparison` (#111): #155 collects three results and adds
  a compatibility with $Rf_!\dashv f^!$.
- `sk-def-av-pic` and `sk-def-pic`: two definitions of $\Pic$ that agree only via Hilbert 90 and Riemann–Roch.
- `sk-d-ab-tate` and `sk-def-av-tate`: a general definition and an instance of it.

## Points to review

**Results the tex states twice.** These are now single merged nodes; see "Merged duplicates".

**Reused sketches that were more general than the tex.** These sketches put the tex statement first and keep the
older, more general content that other nodes cite in a "Complements" or "General form" paragraph:

- `sk-thm-picard-rr`
- `sk-thm-picard-perfect`
- `sk-thm-picard-hilb-curves`
- `sk-thm-av-final`
- `sk-def-picard-pic`
- `sk-thm-sfb-rationalization-comparison`

In these sketches the old statement was replaced outright, and its content survives in detail nodes:

- `sk-prop-cohsm`
- `sk-prop-an`
- `sk-prop-sf-existence`
- `sk-prop-sf-rf-shriek-preservation`
- `sk-thm-sf-ctf-stability`

**Tex declarations without a proof.** These keep the blueprint's proof:

- `sk-lem-nagata-sketch-elimination` (#193)
- `sk-lem-nagata-sketch-boundary` (#196)
- `sk-thm-purity-transport` (#151)

The new `sk-thm-existence` (#50) has the tex's plan of proof and two detail nodes that assemble it.

**Problems in existing nodes noticed during the work (not changed):**

- `thm-sfb-finite-proper-pushforward-left-adjoint` claims that $Rg_*$ has a right adjoint on the unbounded
  pro-étale category. The smooth-purity counterexample suggests this fails in general.
- `prop-sfb-bounded-constructible-triangulated` and `sk-def-sfb-bounded-constructible` claim that $D_{\mathrm{cons}}$ is
  triangulated for any ring object. The tex says this fails for a general condensed ring.
- In `sk-prop-sp-purity-bc` (#176), the moved node `def-pur-smooth-pullback-exchange` defines the exchange
  through the purity map. That makes `thm-pur-smooth-base-change-coherence` hold by definition. The tex uses
  the exchange defined through the counit.
- `thm-weil-pbc-stein-inputs` is tagged `latex:openproblem` and is used for #56.
- `sk-cor-picard-degree-g` says its curve "satisfies the hypotheses of `sk-thm-picard-rr`". Those hypotheses
  changed to the tex's.

**Added hypothesis.** The detail nodes of `sk-lem-formal-closed-support` (#86) assume a standing (Noetherian) scheme, so that the open immersion is quasi-compact. The tex lemma does not state this hypothesis.

**Not updated.** The prose of the block summaries still describes the previous sketch lists.


## Tex declaration → sketch node

"reused" means an existing sketch node was rewritten to the tex statement; "new" means the node was created. The detail count is the number of detail nodes now in the sketch directory.


### §2 The pro-étale site and its comparison theorems

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 1 | 439 | Def Ind-étale, pro-étale and weakly étale morphisms | `pe:morphisms` | The Pro-étale Site and Coefficients | `sk-def-pe-morphisms` | new | 3 |
| 2 | 472 | Lem Stability | `pe:weakly-etale-stability` | The Pro-étale Site and Coefficients | `sk-lem-pe-weakly-etale-stability` | new | 2 |
| 3 | 497 | Def The small pro-étale site | `pe:site` | The Pro-étale Site and Coefficients | `sk-def-pe-site` | new | 2 |
| 4 | 521 | Prop The topos and its functoriality | `pe:topos-functoriality` | The Pro-étale Site and Coefficients | `sk-def-sfb-finite-pushforward-pullback` | reused | 14 |
| 5 | 552 | Def The local hierarchy | `pe:wlocal` | The Pro-étale Site and Coefficients | `sk-def-pe-wlocal` | new | 3 |
| 6 | 578 | Prop Stonean projectivity | `pe:stonean` | The Pro-étale Site and Coefficients | `sk-prop-pe-stonean` | new | 2 |
| 7 | 600 | Prop Splitting ind-étale covers | `pe:wc-rings` | The Pro-étale Site and Coefficients | `sk-prop-pe-wc-rings` | new | 3 |
| 8 | 621 | Thm Existence of contractible covers | `pe:wc-cover` | The Pro-étale Site and Coefficients | `sk-thm-pe-wc-cover` | new | 11 |
| 9 | 661 | Thm Weakly étale maps admit pro-étale refinements | `pe:indetale-refinement` | The Pro-étale Site and Coefficients | `sk-thm-pe-indetale-refinement` | new | 7 |
| 10 | 685 | Prop A cover-dense affine presentation | `pe:affine-basis` | The Pro-étale Site and Coefficients | `sk-prop-pe-affine-basis` | new | 2 |
| 11 | 702 | Thm Enough affine weakly contractible objects | `pe:weakly-contractible-basis` | The Pro-étale Site and Coefficients | `sk-thm-pe-weakly-contractible-basis` | new | 4 |
| 12 | 728 | Cor Exact sections on contractible affines | `pe:wc-sections` | The Pro-étale Site and Coefficients | `sk-cor-pe-wc-sections` | new | 2 |
| 13 | 760 | Def Weak contractibility | `pe:weak-contractible` | The Pro-étale Site and Coefficients | `sk-def-pe-weak-contractible` | new | 1 |
| 14 | 781 | Cor A conservative family preserving all module colimits | `pe:sections` | The Pro-étale Site and Coefficients | `sk-cor-pe-sections` | new | 3 |
| 15 | 817 | Rem Evaluation is not generally a point | `pe:evaluation-not-point` | The Pro-étale Site and Coefficients | `sk-rem-pe-evaluation-not-point` | new | 0 |
| 16 | 835 | Def Repleteness | `pe:replete-def` | The Pro-étale Site and Coefficients | `sk-def-pe-replete` | new | 1 |
| 17 | 842 | Prop Repleteness of the pro-étale topos | `pe:replete` | The Pro-étale Site and Coefficients | `sk-prop-pe-replete` | new | 2 |
| 18 | 860 | Prop Exact products | `pe:products` | The Pro-étale Site and Coefficients | `sk-prop-pe-products` | new | 2 |
| 19 | 898 | Prop The Milnor sequence | `pe:milnor` | The Pro-étale Site and Coefficients | `sk-prop-pe-milnor` | new | 2 |
| 20 | 936 | Prop Left completeness | `pe:left-complete` | The Pro-étale Site and Coefficients | `sk-prop-pe-left-complete` | new | 2 |
| 21 | 970 | Prop Weakly contractible hypercovers | `pe:hypercover` | The Pro-étale Site and Coefficients | `sk-prop-pe-hypercover` | new | 2 |
| 22 | 1016 | Cor Bounded-below continuity | `pe:bounded-continuity` | The Pro-étale Site and Coefficients | `sk-cor-pe-bounded-continuity` | new | 7 |
| 23 | 1058 | Def Classical pro-étale sheaves | `pe:classical-definition` | The Pro-étale Site and Coefficients | `sk-def-pe-classical-definition` | new | 1 |
| 24 | 1071 | Prop The comparison morphism and its inverse image | `pe:comparison-morphism` | The Pro-étale Site and Coefficients | `sk-prop-pe-comparison-morphism` | new | 3 |
| 25 | 1115 | Thm Recognizing the classical part | `pe:classical-sheaves` | The Pro-étale Site and Coefficients | `sk-thm-pe-classical-sheaves` | new | 3 |
| 26 | 1139 | Ex A coefficient sheaf outside the classical part | `pe:nonclassical-example` | The Pro-étale Site and Coefficients | `sk-rem-pe-nonclassical-example` | new | 0 |
| 27 | 1165 | Lem Acyclicity of pulled-back injectives | `pe:injective-acyclicity` | The Pro-étale Site and Coefficients | `sk-lem-pe-injective-acyclicity` | new | 8 |
| 28 | 1193 | Thm Bounded-below cohomology comparison | `pe:cohomology-comparison` | The Pro-étale Site and Coefficients | `sk-prop-sf-comparison` | reused | 22 |
| 29 | 1238 | Cor The derived classical part | `pe:classical-derived` | The Pro-étale Site and Coefficients | `sk-cor-pe-classical-derived` | new | 2 |
| 30 | 1278 | Thm Direct-image comparison | `pe:direct-image-comparison` | The Pro-étale Site and Coefficients | `sk-thm-pe-direct-image-comparison` | new | 9 |
| 31 | 1345 | Lem Descent of classical-group torsors | `pe:torsor-comparison` | The Pro-étale Site and Coefficients | `sk-lem-pe-torsor-comparison` | new | 2 |
| 32 | 1365 | Prop Locally constant sheaves of finite presentation | `pe:finite-local-systems` | The Pro-étale Site and Coefficients | `sk-prop-pe-finite-local-systems` | new | 3 |
| 33 | 1386 | Thm Constructible comparison | `pe:constructible-comparison` | The Pro-étale Site and Coefficients | `sk-thm-pe-constructible-comparison` | new | 6 |
| 34 | 1415 | Cor Finite Tor amplitude under comparison | `pe:finite-tor-comparison` | The Pro-étale Site and Coefficients | `sk-cor-pe-finite-tor-comparison` | new | 9 |
| 35 | 1449 | Def Cohomological dimension | `n:def-cd` | Six Functors: Basic Constructions | `sk-def-cd` | new | 2 |
| 36 | 1471 | Lem — | `b:lem:base-field-cd` | Six Functors: Basic Constructions | `sk-lem-base-field-cd` | new | 5 |
| 37 | 1526 | Prop Unbounded comparison for finite coefficients | `pe:unbounded-classical` | Six Functors: Basic Constructions | `sk-prop-pe-unbounded-classical` | new | 6 |
| 38 | 1619 | Prop The pro-étale geometric point | `pe:condensed-point` | The Pro-étale Site and Coefficients | `sk-prop-pe-condensed-point` | new | 3 |
| 39 | 1650 | Prop Continuous cohomology as pro-étale cohomology | `pe:continuous-cohomology` | The Pro-étale Site and Coefficients | `sk-prop-pe-continuous-cohomology` | new | 3 |
| 40 | 1692 | Ex The first cohomology of a finite field | `pe:finite-field-adic` | The Pro-étale Site and Coefficients | `sk-rem-pe-finite-field-adic` | new | 0 |
| 41 | 1717 | Prop Open–closed operations on module sheaves | `pe:open-closed` | The Pro-étale Site and Coefficients | `sk-prop-sf-open-closed-triangle` | reused | 25 |
| 42 | 1780 | Def Derived adic completeness | `pe:derived-completion` | The Pro-étale Site and Coefficients | `sk-def-pe-derived-completion` | new | 3 |
| 43 | 1800 | Lem Reduction and derived Nakayama | `pe:derived-nakayama` | The Pro-étale Site and Coefficients | `sk-lem-pe-derived-nakayama` | new | 12 |

### §3 Coefficients, constructible complexes and the main theorem

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 44 | 1910 | Lem Comparison with completed coefficients | `n:coefficient-comparison` | The Pro-étale Site and Coefficients | `sk-prop-sfb-qlbar-colimit-x` | reused | 7 |
| 45 | 1964 | Def Tate twists | `def:sp-Tate-twist` | The Pro-étale Site and Coefficients | `sk-def-sp-tate-twist` | new | 1 |
| 46 | 2010 | Prop Rationalization | `n:rationalization` | The Pro-étale Site and Coefficients | `sk-thm-sfb-rationalization-comparison` | reused | 6 |
| 47 | 2049 | Def Local models and constructible sheaves | `n:def-constructible` | The Pro-étale Site and Coefficients | `sk-def-sfb-constructible` | reused | 6 |
| 48 | 2109 | Prop The integral constructibility criterion | `n:integral-criterion` | The Pro-étale Site and Coefficients | `sk-prop-integral-criterion` | new | 4 |
| 49 | 2165 | Def The localizing closure | `—` | The Pro-étale Site and Coefficients | `sk-def-localizing-closure` | new | 2 |
| 50 | 2185 | Thm The exceptional inverse image | `n:existence` | Six Functors: Basic Constructions | `sk-thm-existence` | new | 2 |
| 51 | 2209 | Cor — | `n:existence-b` | Six Functors: Basic Constructions | `sk-cor-existence-ii` | new | 4 |

### §4 Proper base change

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 52 | 2277 | Conv — | `pbc:conventions` | Proper Base Change | `sk-def-pbc-conventions` | new | 3 |
| 53 | 2353 | Def Derived exchange | `pbc:exchange` | Proper Base Change | `sk-def-exchange` | reused | 46 |
| 54 | 2394 | Lem Identity and pasting | `pbc:exchange-pasting` | Proper Base Change | `sk-lem-pbc-exchange-pasting` | new | 2 |
| 55 | 2445 | Def Torsion and the PBC property | `pbc:property` | Proper Base Change | `sk-def-pbc` | reused | 10 |
| 56 | 2477 | Thm Henselian-pair comparison in degree zero | `pbc:henselian-h0` | Proper Base Change | `sk-thm-pbc-henselian-h0` | new | 8 |
| 57 | 2502 | Prop Proper base change in degree zero | `pbc:degree-zero` | Proper Base Change | `sk-prop-pbc-degree-zero` | new | 2 |
| 58 | 2563 | Def Injective acyclicity | `pbc:ia` | Proper Base Change | `sk-def-ia` | reused | 1 |
| 59 | 2581 | Lem Acyclic resolutions | `pbc:acyclicity` | Proper Base Change | `sk-thm-acyclicity` | reused | 1 |
| 60 | 2644 | Thm PBC and injective acyclicity | `pbc:ia-equivalence` | Proper Base Change | `sk-thm-iff` | reused | 13 |
| 61 | 2738 | Rem — | `pbc:proof-division` | Proper Base Change | `sk-rem-pbc-proof-division` | new | 0 |
| 62 | 2802 | Thm Cohomology of curves | `pbc:curve-input` | Curve Estimates | `sk-thm-curve-package` | new | 6 |
| 63 | 2841 | Lem Extension of a separably closed ground field | `pbc:curve-field-extension` | Curve Estimates | `sk-cor-curve-invariance` | new | 4 |
| 64 | 2863 | Rem — | `—` | Curve Estimates | `sk-rem-curve-wild-example` | new | 0 |
| 65 | 2917 | Lem Acyclicity on the closed projective line | `pbc:p1-injective-fibre` | Proper Base Change | `sk-lem-pbc-p1-injective-fibre` | new | 10 |
| 66 | 2978 | Prop Henselian comparison for the projective line | `pbc:p1-henselian` | Proper Base Change | `sk-prop-pbc-p1-henselian` | new | 2 |
| 67 | 3030 | Prop Proper base change for the projective line | `pbc:p1` | Proper Base Change | `sk-thm-p1` | reused | 389 |
| 68 | 3107 | Rem — | `—` | Proper Base Change | `sk-rem-pbc-p1-inputs` | new | 0 |
| 69 | 3123 | Lem Finite morphisms | `pbc:finite` | Proper Base Change | `sk-lem-pbc-finite` | new | 3 |
| 70 | 3161 | Lem Composition and cancellation | `pbc:composition-cancellation` | Proper Base Change | `sk-lem-pbc-composition-cancellation` | new | 8 |
| 71 | 3234 | Lem A finite cover of projective space | `pbc:symmetric-product` | Proper Base Change | `sk-lem-pbc-symmetric-product` | new | 6 |
| 72 | 3291 | Lem Chow's lemma | `pbc:chow` | Nagata Compactification | `sk-thm-chow-projective` | reused | 24 |
| 73 | 3310 | Rem Chow's lemma over arbitrary bases | `pbc:chow-scope` | Proper Base Change | `sk-rem-pbc-chow-scope` | new | 0 |
| 74 | 3318 | Prop Reduction to the projective line | `pbc:reduction` | Proper Base Change | `sk-thm-reduction` | reused | 9 |
| 75 | 3344 | Thm Proper base change on classical pro-étale complexes | `pbc:torsion-theorem` | Proper Base Change | `sk-thm-properbasechange` | reused | 133 |
| 76 | 3406 | Cor Geometric-fibre formula | `pbc:torsion-stalk` | Proper Base Change | `sk-cor-pbc-torsion-stalk` | new | 2 |
| 77 | 3434 | Rem The role of properness | `pbc:reduction-inputs` | Proper Base Change | `sk-rem-pbc-reduction-inputs` | new | 0 |
| 78 | 3455 | Cor Classical finite coefficients on the pro-étale site | `pbc:proet-finite` | Proper Base Change | `sk-cor-pbc-proet-finite` | new | 2 |
| 79 | 3495 | Prop Proper base change for complete integral complexes | `pbc:complete` | Proper Base Change | `sk-prop-pbc-complete` | new | 8 |
| 80 | 3585 | Ex Fibrewise computation and the need for properness | `—` | Proper Base Change | `sk-rem-pbc-fibrewise-properness` | new | 0 |

### §5 Constructible sheaves and reduction to finite coefficients

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 81 | 3630 | Lem Inverse image of the coefficient sheaves | `b:lem:coefficient-pullback` | The Pro-étale Site and Coefficients | `sk-prop-sfb-cartesian-coefficients` | reused | 7 |
| 82 | 3699 | Lem Constructible sheaves | `b:lem:coefficient-heart` | Six Functors: Basic Constructions | `sk-lem-coefficient-heart` | new | 4 |
| 83 | 3718 | Ex A running example | `b:ex:running` | Six Functors: Basic Constructions | `sk-rem-running` | new | 0 |
| 84 | 3776 | Cor — | `b:lem:coefficient-heart-b` | Six Functors: Basic Constructions | `sk-cor-coefficient-heart-ii` | new | 2 |
| 85 | 3818 | Lem Continuity of cohomology | `b:lem:bounded-continuity` | The Pro-étale Site and Coefficients | `sk-cor-pe-bounded-continuity` | new | 7 |
| 86 | 3861 | Lem Sections with support in a closed subscheme | `b:lem:formal-closed-support` | Six Functors: Basic Constructions | `sk-lem-formal-closed-support` | new | 3 |
| 87 | 3931 | Lem Continuity of Ext out of a constructible complex | `b:lem:constructible-ext-continuity` | Six Functors: Basic Constructions | `sk-lem-constructible-ext-continuity` | new | 1 |
| 88 | 4004 | Lem Descent to a finite coefficient field | `b:lem:coefficient-finite-descent` | Six Functors: Basic Constructions | `sk-thm-sfb-qlbar-two-colimit` | new | 20 |
| 89 | 4109 | Lem Lattices after a finite stratification | `b:lem:stratified-lattice` | Six Functors: Basic Constructions | `sk-lem-stratified-lattice` | new | 3 |
| 90 | 4200 | Lem Integral models | `b:lem:integral-models` | Six Functors: Basic Constructions | `sk-lem-integral-models` | new | 3 |
| 91 | 4300 | Prop Proper direct image of constructible complexes | `b:prop:proper-coefficients` | Six Functors: Basic Constructions | `sk-thm-sfb-proper-base-change` | reused | 3 |

### §6 Construction of the exceptional inverse image

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 92 | 4467 | Lem — | `b:lem:formal-closed-support-b` | Six Functors: Basic Constructions | `sk-lem-formal-closed-support-ii` | new | 2 |
| 93 | 4487 | Lem Uniform Ext bound | `b:lem:uniform-constructible-ext` | Six Functors: Basic Constructions | `sk-lem-uniform-constructible-ext` | new | 4 |
| 94 | 4609 | Prop Ind-constructible sheaves | `b:prop:ind-heart` | Six Functors: Basic Constructions | `sk-prop-ind-heart` | new | 6 |
| 95 | 4709 | Cor — | `b:prop:ind-heart-b` | Six Functors: Basic Constructions | `sk-cor-ind-heart-ii` | new | 2 |
| 96 | 4728 | Cor — | `b:cor:ambient-ind-derived` | Six Functors: Basic Constructions | `sk-cor-ambient-ind-derived` | new | 2 |
| 97 | 4754 | Lem Reduction to finitely many degrees | `b:lem:finite-window` | Six Functors: Basic Constructions | `sk-lem-finite-window` | new | 3 |
| 98 | 4818 | Thm Compactness with rational coefficients | `b:thm:constructible-compactness` | Six Functors: Basic Constructions | `sk-thm-constructible-compactness` | new | 3 |
| 99 | 4862 | Cor — | `b:thm:constructible-compactness-b` | Six Functors: Basic Constructions | `sk-cor-constructible-compactness-ii` | new | 1 |
| 100 | 4906 | Lem Cohomology commutes with filtered colimits | `b:lem:proper-heart-continuity` | The Pro-étale Site and Coefficients | `sk-cor-pe-bounded-continuity` | new | 7 |
| 101 | 4942 | Lem A uniform bound for proper direct image | `b:lem:proper-heart-bound` | Six Functors: Basic Constructions | `sk-lem-proper-heart-bound` | new | 5 |
| 102 | 5031 | Lem Proper direct image of unbounded complexes | `b:lem:proper-unbounded-window` | Six Functors: Basic Constructions | `sk-lem-proper-unbounded-window` | new | 3 |
| 103 | 5101 | Lem Proper direct image preserves direct sums | `b:lem:proper-unbounded-window-b` | Six Functors: Basic Constructions | `sk-lem-proper-unbounded-window-ii` | new | 2 |
| 104 | 5144 | Prop Proper direct image and extension by zero | `b:prop:proper-image-localizing` | Six Functors: Basic Constructions | `sk-prop-proper-image-localizing` | new | 2 |
| 105 | 5181 | Lem Checking isomorphisms on constructible complexes | `b:lem:localizing-comparison` | Six Functors: Basic Constructions | `sk-lem-sf-determination` | reused | 3 |
| 106 | 5214 | Prop Proper base change on the localizing categories | `b:prop:proper-base-change-unbounded` | Six Functors: Basic Constructions | `sk-prop-proper-base-change-unbounded` | new | 2 |
| 107 | 5265 | Prop Construction and independence of $Rf_!$ | `b:prop:lower-exceptional-image` | Six Functors: Basic Constructions | `sk-prop-sf-comp-coherence` | reused | 6 |
| 108 | 5336 | Prop Composition and base change for $Rf_!$ | `b:prop:lower-composition` | Six Functors: Basic Constructions | `sk-thm-sf-comp-composition` | reused | 3 |
| 109 | 5443 | Lem Flat models and generators | `ctf:finite-models` | Six Functors: Basic Constructions | `sk-lem-sf-flat-model` | reused | 4 |
| 110 | 5483 | Prop Compactness for finite coefficients | `ctf:finite-compact` | Six Functors: Basic Constructions | `sk-prop-ctf-finite-compact` | new | 3 |
| 111 | 5534 | Prop Comparison with the étale derived category | `ctf:finite-comparison` | Six Functors: Basic Constructions | `sk-prop-ctf-finite-comparison` | new | 2 |
| 112 | 5569 | Prop Proper direct image for finite coefficients | `ctf:finite-proper` | Six Functors: Basic Constructions | `sk-prop-ctf-finite-proper` | new | 5 |
| 113 | 5645 | Lem Hypotheses of Brown representability | `b:lem:brown-hypotheses` | Six Functors: Basic Constructions | `sk-lem-brown-hypotheses` | new | 3 |
| 114 | 5677 | Thm Existence of the exceptional inverse image | `b:thm:brown-adjoint` | Six Functors: Basic Constructions | `sk-prop-sf-existence` | reused | 24 |
| 115 | 5759 | Prop Composition, open restriction and compactifications for $f^!$ | `b:prop:composition-locality` | Six Functors: Basic Constructions | `sk-lem-sf-mate` | reused | 8 |

### §7 The exceptional inverse image preserves constructibility

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 116 | 5952 | Lem The cycle class of a Cartier divisor | `b:lem:geo-cartier` | Six Functors: Basic Constructions | `sk-lem-geo-cartier` | new | 2 |
| 117 | 6024 | Lem Cohomology of the projective line and the trace | `b:lem:geo-p1-cohomology` | Six Functors: Basic Constructions | `sk-lem-geo-p1-cohomology` | new | 2 |
| 118 | 6089 | Ex Compact supports on the running example | `—` | Six Functors: Basic Constructions | `sk-rem-compact-supports-running-example` | new | 0 |
| 119 | 6113 | Prop The projective-line adjunction | `b:prop:geo-p1-adjunction` | Six Functors: Basic Constructions | `sk-prop-geo-p1-adjunction` | new | 4 |
| 120 | 6273 | Lem Affine space and étale localization | `b:lem:geo-affine-local` | Six Functors: Basic Constructions | `sk-lem-geo-affine-local` | new | 2 |
| 121 | 6330 | Prop The exceptional inverse image of a smooth morphism | `b:prop:geo-smooth-tensor` | Six Functors: Basic Constructions | `sk-prop-cohsm` | reused | 7 |
| 122 | 6430 | Lem Smooth morphisms and locally constant sheaves | `b:lem:geo-smooth-generic` | Six Functors: Basic Constructions | `sk-lem-geo-smooth-generic` | new | 1 |
| 123 | 6536 | Lem Detection by a proper direct image | `b:lem:geo-finite-boundary` | Six Functors: Basic Constructions | `sk-lem-geo-finite-boundary` | new | 2 |
| 124 | 6602 | Lem Coordinate projections | `b:lem:geo-coordinates` | Six Functors: Basic Constructions | `sk-lem-geo-coordinates` | new | 2 |
| 125 | 6661 | Thm Generic constructibility and base change for \(Rj_*\) | `b:thm:geo-generic-open` | Six Functors: Basic Constructions | `sk-thm-geo-generic-open` | new | 1 |
| 126 | 6847 | Cor Open direct image over a field | `b:cor:geo-open-finiteness` | Six Functors: Basic Constructions | `sk-cor-geo-open-finiteness` | new | 3 |
| 127 | 6889 | Cor Finite cohomological dimension of open direct image | `b:cor:geo-open-finiteness-b` | Six Functors: Basic Constructions | `sk-cor-geo-open-finiteness-ii` | new | 1 |
| 128 | 6925 | Prop Open direct image preserves finite Tor amplitude | `ctf:finite-open` | Six Functors: Basic Constructions | `sk-cor-sf-direct-image-ctf` | reused | 15 |
| 129 | 6979 | Thm $f^!$ with finite coefficients | `ctf:finite-restriction` | Six Functors: Basic Constructions | `sk-prop-sf-rf-shriek-preservation` | reused | 21 |
| 130 | 7045 | Cor The six operations on $\Dctf(-,A)$ | `ctf:finite-operations` | Six Functors: Basic Constructions | `sk-rem-sf-matrix` | reused | 1 |
| 131 | 7112 | Prop Direct image along an open immersion | `b:prop:open-coefficients` | Six Functors: Basic Constructions | `sk-prop-open-coefficients` | new | 1 |
| 132 | 7166 | Prop The $\ell$-adic cycle class of the diagonal | `b:prop:diagonal-tower` | Six Functors: Basic Constructions | `sk-prop-diagonal-tower` | new | 4 |
| 133 | 7365 | Prop Projection formula and proper base change with rational coefficients | `b:prop:pf-bc-generated` | Six Functors: Basic Constructions | `sk-thm-sf-pf-field` | reused | 7 |
| 134 | 7412 | Prop The projective line | `b:prop:p1-adjunction-rational` | Six Functors: Basic Constructions | `sk-prop-p1-adjunction-rational` | new | 2 |
| 135 | 7488 | Cor — | `b:cor:affine-space-rational` | Six Functors: Basic Constructions | `sk-cor-affine-space-rational` | new | 2 |
| 136 | 7528 | Ex — | `b:ex:closed-support` | Six Functors: Basic Constructions | `sk-rem-closed-support` | new | 0 |
| 137 | 7541 | Prop — | `b:prop:closed-adjoint-constructible` | Six Functors: Basic Constructions | `sk-prop-closed-adjoint-constructible` | new | 2 |
| 138 | 7565 | Thm $f^!$ with rational coefficients | `b:thm:restriction` | Six Functors: Basic Constructions | `sk-thm-restriction` | new | 2 |
| 139 | 7612 | Rem — | `—` | Six Functors: Basic Constructions | `sk-rem-restriction-inputs` | new | 0 |

### §8 Integral coefficients

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 140 | 7678 | Lem Structure of integral constructible complexes | `i:integral-heart` | Six Functors: Basic Constructions | `sk-lem-int-integral-heart` | new | 3 |
| 141 | 7762 | Lem Inverse image and tensor product | `i:tensor` | Six Functors: Basic Constructions | `sk-lem-int-tensor` | new | 4 |
| 142 | 7825 | Lem Continuity and boundedness of Ext | `i:ext` | Six Functors: Basic Constructions | `sk-lem-int-ext` | new | 3 |
| 143 | 7905 | Prop Compactness and proper direct image | `i:compactness` | Six Functors: Basic Constructions | `sk-prop-int-compactness` | new | 2 |
| 144 | 7973 | Cor — | `i:compactness-b` | Six Functors: Basic Constructions | `sk-cor-int-compactness-ii` | new | 1 |
| 145 | 7989 | Prop Compactly supported direct image and its adjoint | `i:brown` | Six Functors: Basic Constructions | `sk-prop-int-brown` | new | 3 |
| 146 | 8012 | Lem Open direct image and projection formula | `i:open-pf` | Six Functors: Basic Constructions | `sk-thm-sf-pf-adic` | reused | 5 |
| 147 | 8057 | Thm $f^!$ preserves integral constructible complexes | `i:restriction` | Six Functors: Basic Constructions | `sk-thm-int-restriction` | new | 3 |

### §9 The six functors on constructible complexes of finite Tor amplitude

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 148 | 8147 | Prop The six functors on $\Dctf$ | `n:six-small` | Six Functors: Basic Constructions | `sk-thm-sf-ctf-stability` | reused | 5 |
| 149 | 8224 | Prop The six operations and coefficient comparison | `n:scalar-six` | Six Functors: Basic Constructions | `sk-prop-scalar-six` | new | 6 |
| 150 | 8373 | Prop $\Dctf(X,\Qbar)$ as a $2$-colimit | `n:two-colimit` | Six Functors: Basic Constructions | `sk-thm-sfb-qlbar-two-colimit` | reused | 20 |

### §10 Smooth purity

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 151 | 8476 | Thm Smooth purity for all admissible coefficients | `thm:sp-integral` | Smooth Purity | `sk-thm-purity-transport` | reused | 6 |
| 152 | 8499 | Def Relative dualizing complex | `def:sp-dualizing` | Smooth Purity | `sk-def-sp-dualizing` | new | 1 |
| 153 | 8593 | Lem The projective-line adjunction | `lem:sp-p1` | Six Functors: Basic Constructions | `sk-prop-geo-p1-adjunction` | new | 4 |
| 154 | 8664 | Def Representing objects | `def:sp-representing-pair` | Smooth Purity | `sk-def-sp-representing-pair` | new | 2 |
| 155 | 8680 | Prop Étale and pro-étale finite coefficients | `prop:sp-et-proet` | Smooth Purity | `sk-prop-sp-et-proet` | new | 9 |
| 156 | 8702 | Lem Local computation of the finite Brown adjoint | `lem:sp-finite-existence` | Smooth Purity | `sk-lem-sp-finite-existence` | new | 2 |
| 157 | 8745 | Prop Vector-bundle purity | `prop:sp-vector` | Smooth Purity | `sk-prop-an` | reused | 36 |
| 158 | 8848 | Prop The tensor formula | `prop:sp-tensor` | Six Functors: Basic Constructions | `sk-prop-cohsm` | new | 7 |
| 159 | 8879 | Prop Exceptional base change for a smooth map | `prop:sp-exceptional-bc` | Six Functors: Basic Constructions | `sk-prop-cohsm` | new | 7 |
| 160 | 8926 | Lem A section and its normal bundle | `lem:sp-dnc` | Smooth Purity | `sk-thm-dnc` | reused | 3 |
| 161 | 9015 | Prop The relative dualizing complex | `prop:sp-orientation` | Smooth Purity | `sk-prop-sp-orientation` | new | 4 |
| 162 | 9093 | Prop Finite-coefficient smooth purity | `prop:sp-finite` | Smooth Purity | `sk-thm-smooth-purity` | reused | 7 |
| 163 | 9148 | Def Extension of coefficients | `def:sp-scalar-extension` | Smooth Purity | `sk-def-sp-scalar-extension` | new | 1 |
| 164 | 9159 | Lem Coefficient comparison | `lem:sp-reduction` | Smooth Purity | `sk-lem-sp-reduction` | new | 4 |
| 165 | 9259 | Def Coefficient towers | `def:sp-coefficient-towers` | Smooth Purity | `sk-def-sp-coefficient-towers` | new | 2 |
| 166 | 9283 | Def Constructible and normalized towers | `def:sp-normalized-towers` | Smooth Purity | `sk-def-sp-normalized-towers` | new | 2 |
| 167 | 9298 | Lem Reconstruction of a normalized tower | `lem:sp-tower` | Smooth Purity | `sk-lem-sp-tower` | new | 26 |
| 168 | 9358 | Lem Levels of the tower direct image | `lem:sp-tower-levels` | Smooth Purity | `sk-lem-sp-tower-levels` | new | 2 |
| 169 | 9407 | Lem Direct image preserves constructible towers | `lem:sp-tower-bound` | Smooth Purity | `sk-lem-sp-tower-bound` | new | 2 |
| 170 | 9424 | Prop The tower model of the smooth adjunction | `prop:sp-tower-geometric` | Smooth Purity | `sk-prop-sp-tower-geometric` | new | 4 |
| 171 | 9603 | Prop The normalized model of the integral adjunction | `prop:sp-integral-adjunction` | Smooth Purity | `sk-prop-sp-integral-adjunction` | new | 2 |
| 172 | 9655 | Prop Comparison with any other right adjoint | `prop:sp-unique-adjoint` | Smooth Purity | `sk-prop-sp-unique-adjoint` | new | 2 |
| 173 | 9722 | Prop Smooth purity with coefficients $E$ | `cor:sp-rational` | Smooth Purity | `sk-prop-sp-rational` | new | 2 |
| 174 | 9758 | Lem Compatibility with finite extensions of $E$ | `lem:sp-field-extension` | Smooth Purity | `sk-lem-sp-field-extension` | new | 2 |
| 175 | 9805 | Thm Smooth purity with algebraically closed coefficients | `thm:sp-qbar` | Smooth Purity | `sk-thm-sp-qbar` | new | 2 |
| 176 | 9934 | Prop Base change of purity | `prop:sp-purity-bc` | Smooth Purity | `sk-prop-sp-purity-bc` | new | 5 |
| 177 | 10011 | Prop Composition of purity | `prop:sp-composition` | Smooth Purity | `sk-prop-sp-composition` | new | 4 |
| 178 | 10078 | Def Smooth trace | `def:sp-trace` | Smooth Purity | `sk-def-sp-trace` | new | 2 |
| 179 | 10095 | Prop Transitivity of the smooth trace | `prop:sp-trace-composition` | Smooth Purity | `sk-prop-sp-trace-composition` | new | 2 |
| 180 | 10144 | Cor The dualizing complex of a smooth scheme | `cor:sp-all-coefficients` | Smooth Purity | `sk-cor-sp-all-coefficients` | new | 3 |
| 181 | 10248 | Def Weil structure | `def:sp-Weil-structure` | Smooth Purity | `sk-def-sf-weil-complexes` | reused | 4 |
| 182 | 10324 | Prop Smooth purity for $f^!$ | `prop:sp-comparison-brown` | Smooth Purity | `sk-thm-purity-transport` | new | 6 |

### §11 Compactification and projective domination

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 183 | 10396 | Def Compactification and refinement | `app:nagata-definition` | Nagata Compactification | `sk-def-nagata-sketch-data` | reused | 56 |
| 184 | 10410 | Thm Nagata compactification | `app:nagata-theorem` | Nagata Compactification | `sk-thm-nagata-compactification` | reused | 10 |
| 185 | 10430 | Lem Schematic closure and uniqueness | `app:nagata-closure` | Nagata Compactification | `sk-lem-nagata-sketch-closure` | reused | 23 |
| 186 | 10454 | Lem Passing to the schematic closure | `app:nagata-density-normalization` | The Pro-étale Site and Coefficients | `sk-lem-nagata-density-normalization` | new | 3 |
| 187 | 10494 | Rem — | `—` | Nagata Compactification | `sk-rem-nagata-closure-scope` | new | 0 |
| 188 | 10503 | Prop Common dense refinements | `app:nagata-refinement` | Nagata Compactification | `sk-prop-nagata-sketch-comp-category` | reused | 19 |
| 189 | 10539 | Rem Base change of a compactification | `app:nagata-base-change` | Nagata Compactification | `sk-rem-nagata-base-change` | new | 0 |
| 190 | 10559 | Def Admissible blow-up | `app:nagata-admissible` | Nagata Compactification | `sk-def-nagata-admissible` | new | 4 |
| 191 | 10588 | Lem Making an open schematically dense | `app:nagata-boundary-divisor` | Nagata Compactification | `sk-lem-nagata-boundary-divisor` | new | 5 |
| 192 | 10626 | Lem Finite refinements of blow-ups | `app:nagata-blowup-refinements` | Nagata Compactification | `sk-lem-nagata-sketch-blowups` | reused | 85 |
| 193 | 10657 | Thm Elimination of indeterminacy | `app:nagata-elimination` | Nagata Compactification | `sk-lem-nagata-sketch-elimination` | reused | 4 |
| 194 | 10684 | Cor Extension to a proper target | `app:nagata-proper-extension` | Nagata Compactification | `sk-cor-nagata-sketch-proper-extension` | reused | 3 |
| 195 | 10706 | Lem Graph extension from a compactification | `app:nagata-graph-extension` | Nagata Compactification | `sk-lem-nagata-sketch-graph` | reused | 2 |
| 196 | 10739 | Lem Separation of closures | `app:nagata-separation` | Nagata Compactification | `sk-lem-nagata-sketch-boundary` | reused | 10 |
| 197 | 10756 | Lem An isomorphism near a boundary closure | `app:nagata-near-closure` | Nagata Compactification | `sk-lem-nagata-sketch-near-closure` | reused | 5 |
| 198 | 10781 | Lem Separated common modification of two opens | `app:nagata-common-modification` | Nagata Compactification | `sk-lem-nagata-sketch-common` | reused | 7 |
| 199 | 10813 | Prop The two-open compactification construction | `app:nagata-two-open` | Nagata Compactification | `sk-thm-nagata-sketch-two-open` | reused | 21 |
| 200 | 10896 | Lem Enough compactifiable affine opens | `app:nagata-affine-opens` | Nagata Compactification | `sk-lem-nagata-sketch-affine-cover` | reused | 15 |
| 201 | 10958 | Thm Projective domination of a proper morphism | `app:chow-projective` | Nagata Compactification | `sk-thm-chow-projective` | new | 24 |

### §12 Picard schemes and Jacobians

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 202 | 11027 | Def Relative Picard functor | `—` | Picard Framework | `sk-def-picard-pic` | reused | 11 |
| 203 | 11048 | Lem Rigidification along a section | `app:picard-rigidification` | Picard Framework | `sk-prop-picard-pic-split` | reused | 8 |
| 204 | 11100 | Thm Riemann–Roch and coherent Serre duality | `app:picard-riemann-roch` | Picard Framework | `sk-thm-picard-rr` | reused | 40 |
| 205 | 11126 | Lem Coherent base change for invertible sheaves | `app:picard-coherent-base-change` | Picard Framework | `sk-thm-picard-perfect` | reused | 5 |
| 206 | 11162 | Thm Hilbert schemes of points on a smooth curve | `app:picard-hilbert-theorem` | Picard Framework | `sk-thm-picard-hilb-curves` | reused | 12 |
| 207 | 11202 | Prop Divisors of degree $g$ as an open chart | `app:picard-abel-chart` | Picard Framework | `sk-thm-picard-f-representable` | reused | 4 |
| 208 | 11238 | Lem Translating into the chart | `app:picard-twist` | Picard Framework | `sk-thm-picard-twist` | reused | 6 |
| 209 | 11273 | Thm The Picard scheme and Jacobian of a geometric curve | `app:picard-curve` | Picard Framework | `sk-thm-picard-main` | reused | 8 |
| 210 | 11342 | Cor The degree sequence | `app:picard-degree` | Picard Framework | `sk-cor-picard-degree` | new | 1 |
| 211 | 11361 | Rem Ground fields and relative representability | `app:picard-relative-scope` | Picard Framework | `sk-rem-picard-relative-scope` | new | 0 |
| 212 | 11384 | Prop Multiplication on an abelian variety | `app:abelian-multiplication` | Abelian Varieties | `sk-thm-av-final` | reused | 2 |
| 213 | 11418 | Cor Jacobian torsion and geometric extension | `app:jacobian-torsion` | Picard Framework | `sk-cor-jacobian-torsion` | new | 3 |

### §13 Cohomology of curves

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 214 | 11502 | Thm Cohomology of curves over an algebraically closed field | `app:curve-package` | Curve Estimates | `sk-thm-curve-package` | new | 6 |
| 215 | 11548 | Lem Cohomology of the multiplicative group | `app:curve-gm` | Curve Estimates | `sk-thm-br` | reused | 19 |
| 216 | 11594 | Prop Smooth proper curves with invertible torsion | `app:curve-kummer` | Curve Estimates | `sk-thm-curveestimate` | reused | 3 |
| 217 | 11650 | Rem Twists and the projective line | `app:curve-twists` | Curve Estimates | `sk-rem-curve-twists` | new | 0 |
| 218 | 11668 | Prop Cohomology of a smooth affine curve | `app:curve-affine-kummer` | Curve Estimates | `sk-prop-curve-affine-kummer` | new | 4 |
| 219 | 11749 | Prop Characteristic torsion on a smooth proper curve | `app:curve-artin-schreier` | Curve Estimates | `sk-prop-curve-artin-schreier` | new | 4 |
| 220 | 11803 | Lem Characteristic torsion on an affine curve | `app:curve-affine-artin-schreier` | Curve Estimates | `sk-lem-curve-affine-artin-schreier` | new | 1 |
| 221 | 11820 | Ex The affine line in characteristic $p$ | `app:curve-wild-example` | Curve Estimates | `sk-rem-curve-wild-example` | new | 0 |
| 222 | 11852 | Lem Finite-support sheaves and finite maps | `app:curve-finite-support` | Curve Estimates | `sk-lem-curve-finite-support` | new | 2 |
| 223 | 11875 | Lem Normalization of a constant sheaf | `app:curve-normalization` | Curve Estimates | `sk-lem-curve-normalization` | new | 23 |
| 224 | 11921 | Lem Removing finitely many points | `app:curve-dense-open` | Curve Estimates | `sk-lem-curve-dense-open` | new | 21 |
| 225 | 11965 | Lem Reduction to a unipotent local system | `app:curve-sylow-trace` | Curve Estimates | `sk-lem-curve-sylow-trace` | new | 4 |
| 226 | 12071 | Cor Proper curves over separably closed fields | `app:curve-invariance` | Curve Estimates | `sk-cor-curve-invariance` | new | 4 |

## Top-level nodes that appear only in the blueprint

These top-level nodes of the aligned blocks correspond to no declaration of the tex file. Their statements are unchanged. "Block on main" is filled in when the node now sits in a different block than on `main`; "Related tex" names tex declarations that partly overlap it.


### Nagata Compactification (13)

| Node | Kind | Title | Details | Block on main | Related tex |
|---|---|---|---:|---|---|
| `sk-def-conv` | definition | Scheme and morphism conventions | 12 |  | #52 |
| `sk-def-nagata-sketch-quasidomination` | definition | Quasi-domination | 2 |  |  |
| `sk-prop-nagata-sketch-zmt` | proposition | Zariski's Main Theorem and affine-space immersions | 20 |  | #200 |
| `sk-thm-nagata-sketch-conrad` | theorem | Extension of a partial section after an admissible blow-up | 18 |  | #193 |
| `sk-lem-nagata-sketch-image-transform` | lemma | Images under admissible blow-up | 3 |  |  |
| `sk-prop-nagata-sketch-prepared` | proposition | Prepared sides | 8 |  | #199 |
| `sk-prop-nagata-sketch-key-disjointness` | proposition | Improved comparison and key disjointness | 2 |  | #199 |
| `sk-lem-nagata-sketch-dense-valuative` | lemma | Dense-source valuative criterion | 10 |  | #199 |
| `sk-thm-nagata-sketch-noetherian` | theorem | Nagata over a Noetherian base | 4 |  | #184 |
| `sk-prop-nagata-sketch-approximation` | proposition | Absolute approximation and descent | 43 |  | #72 |
| `sk-cor-nagata-sketch-fp` | corollary | Nagata for finite presentation | 8 |  | #184 |
| `sk-prop-nagata-sketch-fp-models` | proposition | Finite-presentation models of a finite-type morphism | 11 |  |  |
| `sk-prop-nagata-sketch-envelope` | proposition | Separated finite-presentation envelope | 6 |  |  |

### The Pro-étale Site and Coefficients (22)

| Node | Kind | Title | Details | Block on main | Related tex |
|---|---|---|---:|---|---|
| `sk-def-sfb-sheaf-tensor` | definition | Tensor product of pro-étale sheaves | 5 | Six Functors: Basic Constructions |  |
| `sk-def-sfb-ring-object` | definition | Ring objects of abelian sheaves | 5 | Six Functors: Basic Constructions |  |
| `sk-def-sfb-condensed-ring` | definition | Condensed coefficient rings $\underline T$ | 6 | Six Functors: Basic Constructions | #38, #44 |
| `sk-def-sfb-qlbar-condensed` | definition | The condensed ring $\underline{\overline{\mathbf Q}}_\ell$ | 4 | Six Functors: Basic Constructions |  |
| `sk-prop-sfb-qlbar-colimit-point` | proposition | $\underline{\overline{\mathbf Q}}_\ell=\operatorname{colim}_E\underline E$ on the point | 2 | Six Functors: Basic Constructions |  |
| `sk-def-sfb-pullback-from-point` | definition | Pulling back from the point | 15 | Six Functors: Basic Constructions | #4, #38 |
| `sk-def-sfb-pulled-back-coefficients` | definition | Coefficients pulled back from the point | 2 | Six Functors: Basic Constructions | #44 |
| `sk-def-sfb-pullback-from-point-comp` | definition | $f^*\circ p_Y^*\cong p_X^*$ | 2 | Six Functors: Basic Constructions | #81 |
| `sk-def-sfb-coefficient-morphisms` | definition | The canonical coefficient morphisms $\alpha_f$, $\eta_f$ | 5 | Six Functors: Basic Constructions | #81 |
| `sk-def-sfb-module-objects` | definition | Module objects and the category $\Mod_{\Lambda_X}$ | 3 | Six Functors: Basic Constructions |  |
| `sk-prop-sfb-module-category` | proposition | Structure of $\Mod_{\mathcal R}(\mathcal C)$ | 14 | Six Functors: Basic Constructions |  |
| `sk-def-sfb-change-of-scalars` | definition | Restriction, extension and coextension of scalars | 12 | Six Functors: Basic Constructions | #163 |
| `sk-def-sfb-transport` | definition | Transport of module objects and projection formulas | 9 | Six Functors: Basic Constructions |  |
| `sk-def-sfb-derived-categories` | definition | Derived categories and derived functors | 6 | Six Functors: Basic Constructions |  |
| `sk-def-sfb-derived-tensor-hom` | definition | Derived tensor product and derived internal hom | 10 | Six Functors: Basic Constructions |  |
| `sk-def-sfb-derived-extension-of-scalars` | definition | Derived extension of scalars | 4 | Six Functors: Basic Constructions | #46, #163 |
| `sk-def-sfb-rationalization` | definition | Rationalization of a linear triangulated category | 6 | Six Functors: Basic Constructions | #46 |
| `sk-def-sfb-bounded-constructible` | definition | Bounded constructible derived category | 3 | Six Functors: Basic Constructions | #47, #48, #84, #140 |
| `sk-def-sfb-module-pushforward-pullback` | definition | Pushforward and pullback of module objects | 6 | Six Functors: Basic Constructions |  |
| `sk-prop-sfb-module-pullback-exact` | proposition | The pullback of module objects is exact | 2 | Six Functors: Basic Constructions |  |
| `sk-def-sf-setting` | definition | Coefficients and sites | 1 | Smooth Purity | #45 |
| `sk-def-sf-operations` | definition | The six operations: ambient typing | 33 | Smooth Purity | #42, #48, #107, #114 |

### Abelian Varieties (39)

| Node | Kind | Title | Details | Block on main | Related tex |
|---|---|---|---:|---|---|
| `sk-def-curve` | definition | Curves and genus | 3 |  |  |
| `sk-def-av-group-scheme` | definition | Group schemes, order, and étaleness | 5 |  |  |
| `sk-def-av` | definition | Abelian varieties | 2 |  |  |
| `sk-def-av-isogeny` | definition | Isogenies and their degree | 2 |  |  |
| `sk-def-av-mult-n` | definition | Multiplication by $n$ and $n$-torsion | 1 |  |  |
| `sk-def-av-ample-degree` | definition | Ample modules and the Hilbert degree | 4 |  |  |
| `sk-def-av-pic` | definition | $\Pic$, degree, $\Pic^0$ | 5 |  |  |
| `sk-def-av-jacobian` | definition | The Jacobian | 14 |  |  |
| `sk-d-ab-field` | definition | Finite fields, Frobenius and abelian varieties | 1 |  |  |
| `sk-d-ab-tate` | definition | Integral and rational Tate modules | 1 |  |  |
| `sk-def-av-tate` | definition | $\ell$-adic Tate module | 1 |  |  |
| `sk-prop-av-char` | proposition | Abelian varieties are the complete group varieties | 1 |  |  |
| `sk-prop-av-projective` | proposition | Abelian varieties are projective | 1 |  |  |
| `sk-prop-av-symmetric-ample` | proposition | A symmetric ample module | 1 |  |  |
| `sk-prop-av-cube` | proposition | The theorem of the cube | 1 |  |  |
| `sk-prop-av-mult-n-pullback` | proposition | Pullback of symmetric modules under multiplication by $n$ | 1 |  |  |
| `sk-prop-av-deg-pullback` | proposition | Degree of a pullback under a finite morphism | 1 |  |  |
| `sk-prop-av-const-locus` | proposition | The locus of constant fibres is closed | 1 |  |  |
| `sk-prop-av-image-open` | proposition | Finiteness of the image is open in the parameter | 1 |  |  |
| `sk-prop-av-rigidity` | proposition | The rigidity lemma | 1 |  |  |
| `sk-cor-av-commutative` | corollary | Abelian varieties are commutative | 1 |  |  |
| `sk-prop-av-mult-hom` | proposition | The $n$-fold sum is a homomorphism | 1 |  |  |
| `sk-prop-av-pqf-finite` | proposition | Proper and quasi-finite implies finite | 53 |  | #71 |
| `sk-prop-av-ample-positive` | proposition | Ample modules on proper curves have positive degree | 1 |  |  |
| `sk-prop-av-mult-finite` | proposition | Finiteness of the fibres of the multiplication map | 1 |  | #212 |
| `sk-prop-av-mult-surjective` | proposition | Surjectivity of the multiplication map | 2 |  | #212 |
| `sk-prop-av-isogeny-degree` | proposition | The degree of an isogeny is the degree of the kernel | 2 |  |  |
| `sk-prop-av-isogeny` | proposition | The multiplication-by-$n$ isogeny | 2 |  | #212 |
| `sk-prop-av-fixed-points` | proposition | Fixed points of $p$-linear maps are finite | 1 |  | #219 |
| `sk-prop-av-lang-steinberg` | proposition | Lang–Steinberg for $p$-linear maps | 2 |  | #219 |
| `sk-prop-av-fixed-base-change` | proposition | Fixed points are unchanged by algebraically closed base change | 1 |  | #219 |
| `sk-prop-av-divisible` | proposition | Surjectivity of multiplication by $n$ on points | 3 |  |  |
| `sk-prop-av-divisible-structure` | proposition | The torsion of a divisible group | 1 |  |  |
| `sk-prop-av-connected-order` | proposition | Connected finite group schemes have $p$-power order | 1 |  |  |
| `sk-prop-av-prime-p-etale` | proposition | Group schemes of order prime to $p$ are étale | 1 |  |  |
| `sk-prop-av-finite-etale-points` | proposition | Points of finite étale group schemes | 7 |  |  |
| `sk-prop-av-tate-rank` | proposition | The $\ell$-adic Tate module is free of rank $2g$ | 1 |  |  |
| `sk-the-final-theorem-the-abelian-variety-estimate--remark-1` | remark | Remark | 0 |  |  |
| `sk-prop-av-ntorsion-etale` | proposition | The $n$-torsion of an abelian variety is étale | 2 |  | #212, #213 |

### Picard Framework (28)

| Node | Kind | Title | Details | Block on main | Related tex |
|---|---|---|---:|---|---|
| `sk-def-groth-ss` | definition | Composable pair with acyclicity; the couple of a double complex | 1 |  |  |
| `sk-thm-picard-cech` | theorem | Čech-to-derived | 1 |  |  |
| `sk-thm-groth-ss` | theorem | Grothendieck spectral sequence and its Leray specialization | 3 |  | #70 |
| `sk-lem-picard-affine` | lemma | Vanishing of cohomology on affine schemes | 3 |  |  |
| `sk-lem-picard-cech-computes` | lemma | Leray's theorem for quasi-coherent sheaves | 1 |  |  |
| `sk-thm-picard-pn` | theorem | Cohomology of $\PP^n$, Serre 1954 | 10 |  |  |
| `sk-thm-picard-serre-b` | theorem | Serre's theorem B: vanishing after a twist | 7 |  |  |
| `sk-thm-picard-serre-a` | theorem | Serre's theorem A: global generation after a twist | 1 |  |  |
| `sk-thm-picard-coherence` | theorem | Coherence of the higher direct images | 27 |  | #205 |
| `sk-thm-picard-semicon` | theorem | Semicontinuity and base change | 19 |  | #3, #205 |
| `sk-thm-picard-duality` | theorem | Serre duality | 21 |  | #204 |
| `sk-cor-picard-degree-g` | corollary | The degree of the dictionary | 1 |  | #207 |
| `sk-prop-picard-dense-points` | proposition | Zariski density of rational points | 7 |  | #208 |
| `sk-thm-picard-descent` | theorem | Descent | 2 |  |  |
| `sk-the-hilbert-functor--definition-1` | definition | Hilbert functor | 5 |  | #206 |
| `sk-cor-picard-hilb-sheaf` | corollary | Hilbert functor is the fppf sheaf | 3 |  |  |
| `sk-prop-picard-schemes-criterion` | proposition | The general representability criterion | 5 |  | #209 |
| `sk-thm-picard-hilb-general` | theorem | Representability of $\Hilb^d$ — general case | 1 |  | #206 |
| `sk-cor-picard-pic-sheaf` | corollary | Picard functor is an fppf sheaf | 1 |  | #202, #203 |
| `sk-def-picard-f` | definition | The subfunctor $F$ | 2 |  | #207 |
| `sk-lem-picard-f-open` | lemma | $F$ is an open subfunctor | 3 |  | #205, #207 |
| `sk-lem-picard-zero-dictionary` | lemma | The zero-scheme dictionary | 2 |  | #207 |
| `sk-the-subsheaf-ff-and-its-representability--remark-1` | proposition | $F$ is a subfunctor of the Hilbert functor | 1 |  | #207 |
| `sk-thm-picard-criterion` | theorem | The criterion: a functor generated by a representable open subfunctor | 1 |  | #209 |
| `sk-prop-picard-degree-decomposition` | proposition | Degree decomposition of the Picard scheme | 5 |  | #209, #210 |
| `sk-prop-picard-jacobian-tangent` | proposition | The tangent space of the Jacobian | 1 |  | #209 |
| `sk-prop-jacobian-descent` | proposition | The Jacobian over a general base field, by Galois descent | 18 |  | #211 |
| `sk-rem-picard-seams` | remark | The dependencies are one-way: $\mathbf A\Rightarrow\mathbf B$ at four seams | 0 |  |  |

### Curve Estimates (17)

| Node | Kind | Title | Details | Block on main | Related tex |
|---|---|---|---:|---|---|
| `sk-def-kummer` | definition | The Kummer sequence | 1 |  | #216 |
| `sk-prop-kummer-exact` | proposition | Exactness of the Kummer sequence | 1 |  | #216 |
| `sk-prop-hilbert90` | proposition | Hilbert 90 | 6 |  | #215 |
| `sk-def-pic` | definition | Picard group, degree, $\Pic^0$ | 2 |  | #210 |
| `sk-def-br` | definition | Brauer group | 1 |  |  |
| `sk-def-cr` | definition | $C_r$ fields | 1 |  |  |
| `sk-prop-tsen` | proposition | Tsen's theorem | 3 |  | #215 |
| `sk-prop-divisor-gen` | proposition | Divisor sequence | 2 |  | #215 |
| `sk-prop-br-inj` | proposition | Generic-point injection for the Brauer group | 2 |  | #215 |
| `sk-prop-h1` | proposition | $H^1$ via Kummer | 3 |  | #216, #218 |
| `sk-prop-h2` | proposition | $H^2$ via Kummer | 39 |  | #36, #216 |
| `sk-prop-cd` | proposition | Vanishing in high degrees | 9 |  | #62, #214, #219, #222 |
| `sk-prop-cd-affine` | proposition | Affine-curve cohomological dimension | 9 |  | #62, #214, #218, #220 |
| `sk-the-final-theorem-the-curve-estimate--remark-1` | remark | Remark | 0 |  |  |
| `sk-prop-ext-invariance` | proposition | Invariance under extension of algebraically closed fields | 3 |  | #62, #63, #216, #218 |
| `sk-the-final-theorem-the-curve-estimate--remark-2` | remark | Remark | 0 |  |  |
| `sk-def-pbc-curve-assertions` | definition | The eight curve-cohomology assertions | 12 | Proper Base Change | #62, #214 |

### Proper Base Change (2)

| Node | Kind | Title | Details | Block on main | Related tex |
|---|---|---|---:|---|---|
| `sk-curve-calculations-pbc-for-the-projective-line--remark-1` | remark | Remark | 0 |  | #62, #214 |
| `sk-the-final-theorem--remark-1` | remark | Remark | 0 |  | #61, #77 |

### Six Functors: Basic Constructions (37)

| Node | Kind | Title | Details | Block on main | Related tex |
|---|---|---|---:|---|---|
| `rem-sfb-coefficient-layers` | remark | Two layers of coefficients | 0 |  | #3, #26 |
| `rem-sfb-what-lambda-x` | remark | What $\Lambda_X$ is | 0 |  | #26, #44 |
| `rem-sfb-constructible-coefficients` | remark | Constructibility over the coefficient rings | 0 |  | #47 |
| `sk-def-sfb-finite-lower-shriek` | definition | Extension by zero and lower shriek (finite coefficients) | 8 |  | #41 |
| `sk-def-sfb-finite-derived-functors` | definition | Derived pushforward and pullback (finite coefficients) | 5 |  |  |
| `sk-def-sfb-finite-derived-lower-shriek` | definition | Derived lower shriek and $R\Gamma_c$ (finite coefficients) | 6 |  |  |
| `sk-def-sfb-finite-upper-shriek` | definition | Exceptional pullback $Rf^!$ (finite coefficients) | 9 |  | #51, #114 |
| `sk-def-sfb-module-lower-shriek` | definition | Extension by zero and lower shriek of module objects | 6 |  |  |
| `sk-def-sfb-module-derived-pushpull` | definition | Derived pushforward and pullback of module objects | 2 |  |  |
| `sk-prop-sfb-module-derived-factorization` | proposition | Factorizations and levelwise descriptions of the derived functors | 8 |  |  |
| `sk-def-sfb-module-derived-lower-shriek` | definition | Derived lower shriek of module objects | 6 |  |  |
| `rem-sfb-module-upper-shriek-and-qlbar` | remark | No ambient exceptional pullback; $\Qlb$-coefficients | 0 |  |  |
| `sk-def-sfb-coefficient-change` | definition | Change of condensed coefficients | 4 |  |  |
| `sk-prop-sfb-finite-extension-compatibility` | proposition | Compatibility for $E\subseteq F$ and $E\subseteq\Qlb$ | 5 |  | #81, #88, #174 |
| `sk-def-sfb-filtered-two-colimit` | definition | Filtered 2-colimits of categories | 4 |  | #88, #150 |
| `sk-def-sfb-dc-setting` | definition | Setting for $D_{\mathrm{cons}}$: schemes of finite type over a field | 2 |  |  |
| `sk-def-sfb-dc-lower-shriek` | definition | $Rf_!$ on $D_{\mathrm{cons}}$: assembled from $i_!$ and $Rp_*$ | 2 |  | #107, #145, #186 |
| `sk-def-sfb-base-change-morphism` | definition | The base change morphism on $D_{\mathrm{cons}}$ | 3 |  |  |
| `sk-def-sfb-open-base-change` | definition | Base change for extension by zero on $D_{\mathrm{cons}}$ | 3 |  |  |
| `sk-def-sfb-shriek-base-change-morphism` | definition | Compact-support base change morphism $\mathrm{Ex}_!^c$ | 2 |  |  |
| `sk-thm-sfb-shriek-base-change` | theorem | Base change for the lower shriek on $D_{\mathrm{cons}}$ | 2 |  | #108, #133 |
| `sk-def-sfb-coefficient-comparisons` | definition | Comparison maps for a change of coefficients | 23 |  | #149, #164 |
| `sk-def-sfb-dc-restricted-functors` | definition | $Lf^*$, $Rf_*$, $j_!$, $\otimes^{\mathrm L}$, $\RHom$ on $D_{\mathrm{cons}}$: restrictions | 15 |  | #90, #91, #131, #141 |
| `sk-def-sfb-dc-upper-shriek` | definition | $Rf^!$ on $D_{\mathrm{cons}}$ | 4 |  | #50, #51, #114, #115, #138, #145, #147 |
| `sk-def-sf-exchanges` | definition | Exchange and projection transformations, typed | 3 | Smooth Purity | #53 |
| `sk-def-sf-admissible` | definition | Admissibility datum: an explicit hypothesis | 16 | Smooth Purity | #45 |
| `sk-prop-sf-cbc` | proposition | Compact-support base change | 92 | Smooth Purity | #35, #106, #108, #153 |
| `sk-prop-sf-finiteness` | proposition | Finiteness and constructibility | 1 | Smooth Purity | #91, #101, #112 |
| `sk-prop-sf-fullcd-etale-origin` | proposition | $\operatorname{FullCD}$ on the étale-origin class | 14 | Smooth Purity | #11, #14, #36, #37 |
| `sk-thm-sf-pf-finite` | theorem | Projection formula, finite coefficients | 3 | Smooth Purity |  |
| `sk-prop-sf-pf-reduction` | proposition | Projection formula: compatibility with finite reduction | 5 | Smooth Purity |  |
| `sk-def-purity-conv` | definition | Purity conventions and the rank-one datum | 13 | Smooth Purity | #45, #152, #160 |
| `sk-prop-a1-kummer` | proposition | The affine line and $\mathbf G_m$ with $\Lambda(1)$-coefficients | 46 | Smooth Purity | #40, #117, #136 |
| `sk-prop-a1` | proposition | Rank-one orientation: the fundamental class of the zero section | 3 | Smooth Purity | #136 |
| `sk-prop-sf-biduality-general` | proposition | General Verdier biduality | 18 | Six Functors | #171 |
| `sk-thm-sf-direct-image-tor-amplitude` | theorem | Direct image with finite Tor amplitude | 1 | Six Functors | #112, #128 |
| `sk-thm-sf-hom-ctf` | theorem | Internal Hom with finite Tor amplitude | 1 | Six Functors | #130 |

### Smooth Purity (13)

| Node | Kind | Title | Details | Block on main | Related tex |
|---|---|---|---:|---|---|
| `sk-prop-sf-kunneth-ordinary` | proposition | Künneth and the projection formula in ordinary étale cohomology | 116 |  |  |
| `sk-prop-sf-trace-perfectness` | proposition | Perfectness of compact cohomology and of geometric stalks | 4 |  |  |
| `sk-prop-sf-closed-unit` | proposition | Closed-immersion unit | 11 |  | #41, #86, #137 |
| `sk-prop-sf-localization` | proposition | Supported localization | 7 |  | #86, #131, #137, #146 |
| `sk-prop-sf-comp-proper` | proposition | Proper coincidence | 1 |  | #186 |
| `sk-prop-a1-inv` | proposition | Weak $\Aaf^1$-invariance | 7 |  |  |
| `sk-lem-geometry` | lemma | Geometry of the deformation of a section | 1 |  | #160 |
| `sk-lem-diag-reg` | lemma | The diagonal is a regular immersion | 1 |  | #161 |
| `sk-lem-coprojection` | lemma | Co-projection for a closed immersion | 2 |  |  |
| `sk-lem-regular-smooth` | lemma | A regular immersion of smooth schemes over a perfect field | 1 |  |  |
| `sk-thm-regular` | theorem | Purity for regular closed immersions | 2 |  |  |
| `sk-rem-split` | remark | What sits where | 0 |  |  |
| `rem-pur-status-after-completion` | remark | Dependency order of the smooth-purity proof | 0 |  |  |

### Six Functors (38)

| Node | Kind | Title | Details | Block on main | Related tex |
|---|---|---|---:|---|---|
| `sk-def-sf-categories` | definition | Ambient categories and small subcategories | 1 |  | #47 |
| `sk-rem-sf-typing-rule` | remark | The typing rule of this section | 0 |  |  |
| `sk-rem-sf-typing` | remark | Typing table: ambient definition, small-category theorem | 0 |  |  |
| `sk-def-sf-orientation` | definition | Orientation: an interface record | 3 |  | #161 |
| `sk-rem-sf-fullcd-scope` | remark | What this does and does not discharge | 0 |  |  |
| `rem-sf-fullcd-general-form` | remark | The general form of $\operatorname{FullCD}$, and the form the blueprint uses | 0 |  |  |
| `rem-sf-fullcd-counterexample` | remark | The counterexample: a pro-étale base change whose comparison direct image has infinite cohomological dimension | 0 |  |  |
| `rem-sf-fullcd-reduction` | remark | What $\operatorname{FullCD}$ supplies, and what would discharge it | 0 |  |  |
| `rem-sf-continuity-obstruction` | remark | What the recorded proof of the comparison theorem uses, and why it does not extend to arbitrary sheaves | 0 |  | #37 |
| `rem-sf-cech-truncation-obstruction` | remark | The Čech complex of a single weakly contractible covering: what its truncation is missing, and what does not supply it | 0 |  | #21 |
| `rem-ptr-weil-ambient-exceptional-adjoint-13` | remark | Pointer to the properties of [def-weil-ambient-exceptional-adjoint] | 0 |  |  |
| `rem-sf-fullcd-counterexample-locus` | remark | Where the counterexample lives, and which restricted statements survive it | 0 |  |  |
| `sk-thm-sf-pf-proetale` | theorem | Projection formula: the pro-étale realization | 1 |  |  |
| `sk-prop-sf-pf-coherence` | proposition | Coherence of the projection formula | 1 |  |  |
| `sk-rem-sf-pf-done` | theorem | The interface is discharged | 10 |  |  |
| `sk-lem-sf-open-ctf` | lemma | Extension by zero preserves the finite-Tor constructible category | 3 |  | #104, #144 |
| `sk-thm-sf-internal-hom-pullback` | theorem | Internal Hom versus pullback for a site-perfect first variable | 1 |  |  |
| `sk-thm-sf-tensor-hom` | theorem | Tensor–Hom form of the exchange | 1 |  |  |
| `sk-rem-sf-comp-scope` | remark | Scope of the coherence | 0 |  |  |
| `sk-thm-sf-verdier-exchange` | theorem | Verdier-duality exchange | 1 |  |  |
| `sk-prop-sf-dualizable-biduality` | proposition | Biduality of a perfect complex | 2 |  |  |
| `sk-lem-sf-twist-interchange` | lemma | Internal Hom with an invertible twist | 1 |  |  |
| `sk-thm-sf-dual-perfect` | theorem | The dual of a perfect complex | 1 |  |  |
| `sk-thm-sf-global-duality` | theorem | Global Verdier duality | 2 |  |  |
| `sk-thm-sf-identification` | theorem | The derived Poincaré pairing is the duality isomorphism | 4 |  |  |
| `sk-thm-sf-kunneth-relative` | theorem | Relative product theorem | 2 |  |  |
| `sk-lem-sf-kunneth-star` | lemma | Ordinary Künneth with an identity factor | 1 |  |  |
| `sk-def-sf-kv-maps` | definition | The product comparison maps | 1 |  |  |
| `sk-thm-sf-kunneth-verdier` | theorem | Künneth–Verdier isomorphism | 5 |  |  |
| `sk-rem-sf-kv-formal` | proposition | What is formal and what is not | 2 |  |  |
| `sk-thm-sf-package` | theorem | The six-operations package | 39 |  | #148, #151, #181 |
| `sk-rem-sf-ledger` | remark | Ledger: what is unconditional, what is conditional, what is open | 0 |  |  |
| `rem-sf-ledger` | remark | What this chapter settles, and what remains | 0 |  |  |
| `rem-weil-admissibility-split` | remark | Existence, preservation and geometric duality are separate | 0 |  |  |
| `rem-ptr-weil-exceptional-inverse-image-6` | remark | Pointer to the properties of the exceptional inverse image | 0 |  |  |
| `rem-sf-dualizing-ctf-hypotheses` | remark | Geometric duality and its coefficient comparisons | 0 |  |  |
| `rem-sf-preservation-class-residue` | remark | Constructible completion and the ambient boundary | 0 |  |  |
| `sk-rem-sf-feeds` | remark | Where this feeds | 0 |  |  |
