# Alignment of the sketch layer with `DerivedCategoryAndSixFunctorsChoice_readable.tex`

This file records how the sketch layer of blocks 1–5 and 7–9 of the blueprint was aligned with the declarations of `DerivedCategoryAndSixFunctorsChoice_readable.tex`, and lists the sketch nodes that exist only in the blueprint.

## Scope and conventions

- **Blocks.** Blocks are numbered by their `order`: 1 Nagata Compactification, 2 Abelian Varieties, 3 Picard Framework, 4 Curve Estimates, 5 Proper Base Change, 7 Six Functors: Basic Constructions, 8 Smooth Purity, 9 Six Functors. Block 6 (Smooth Base Change) has no counterpart in the tex file and was not touched.
- **One node per declaration.** Every `definition`, `lemma`, `proposition`, `theorem`, `corollary`, `convention`, `remark` and `example` environment of the tex file (226 in total) has exactly one sketch node, and no sketch node stands for two declarations. The introduction (§1) has no declarations.
- **Kinds.** The node kind follows the tex environment; a convention is a `definition`, an example is a `remark`.
- **Statements.** The sketch statement and its proof are the tex statement and proof converted to Markdown. Where an existing sketch was reused, its id, `lean` names, `uses` and detail nodes were kept.
- **Detail nodes.** Every sketch node of a definition, lemma, proposition, theorem, corollary or convention is a directory with at least one detail node covering it. These are existing detail nodes moved in from where they were, or new nodes written from the tex proof (ids `det-…`). Remarks and examples are single leaf files, without detail nodes or `uses`, following the existing rule that remarks are leaves.
- **Order.** Inside each block the tex-aligned sketches come first, in tex order. They are followed by the blueprint-only sketches listed below, in their previous relative order.
- **Default block.** A declaration with no existing sketch went to the default block of its tex section: §2, §3, §5, §6 → block 7; §4 → block 5; §7, §8, §9 → block 9; §10 → block 8; §11 → block 1; §12 → block 3 (subsection "Torsion points of the Jacobian" → block 2); §13 → block 4. A declaration whose content already had a sketch node stayed with that node, wherever it was.
- **Arrows.** `uses` arrows were not made consistent. Only the obvious ones were added.
- **Macros.** Macros of the tex preamble that KaTeX lacked were added to `blueprint.toml`. Five tex macros mean something else in `blueprint.toml` (`\RHom`, `\Qbar`, `\et`, `\proet`, `\Ob`) and were expanded inline instead.

## Summary

| Block | Tex declarations | Existing sketch reused | New sketch node | Blueprint-only sketch nodes |
|---|---:|---:|---:|---:|
| 1 Nagata Compactification | 19 | 13 | 6 | 13 |
| 2 Abelian Varieties | 2 | 2 | 0 | 39 |
| 3 Picard Framework | 10 | 8 | 2 | 30 |
| 4 Curve Estimates | 13 | 2 | 11 | 18 |
| 5 Proper Base Change | 29 | 9 | 20 | 4 |
| 7 Six Functors: Basic Constructions | 81 | 10 | 71 | 41 |
| 8 Smooth Purity | 40 | 13 | 27 | 26 |
| 9 Six Functors | 32 | 7 | 25 | 47 |
| **Total** | **226** | **64** | **162** | **218** |

## Points to review

**Source.** The alignment follows the version of `DerivedCategoryAndSixFunctorsChoice_readable.tex` (12,187 lines)
committed together with it. That version includes §11 Compactification and projective domination, §12 Picard schemes
and Jacobians and §13 Cohomology of curves.

**Results the tex states twice.** Each has its own sketch node, as the one-to-one rule requires:
- #62 `pbc:curve-input` (`sk-thm-pbc-curve-input`) and #214 `app:curve-package` (`sk-thm-curve-package`);
- #63 `pbc:curve-field-extension` (`sk-lem-pbc-curve-field-extension`) and #226 `app:curve-invariance` (`sk-cor-curve-invariance`);
- #119 `b:prop:geo-p1-adjunction` (`sk-prop-geo-p1-adjunction`) and #153 `lem:sp-p1` (`sk-lem-sp-p1`).

**Reused sketches that were more general than the tex.** The tex statement comes first. The older, more general
content that other nodes cite is kept after it, in a "Complements" or "General form" paragraph:
- `sk-thm-picard-rr`;
- `sk-thm-picard-perfect`;
- `sk-thm-picard-hilb-curves`;
- `sk-thm-av-final`;
- `sk-prop-av-ntorsion-etale`;
- `sk-def-picard-pic`;
- `sk-thm-sfb-rationalization-comparison`.

In these sketches the old statement was replaced outright, and the old content now survives only in their detail nodes:
- `sk-prop-cohsm`;
- `sk-prop-an`;
- `sk-prop-sf-existence`;
- `sk-prop-sf-rf-shriek-preservation`;
- `sk-thm-sf-ctf-stability`.

References elsewhere to lettered parts of the old statements were redirected to the new labels or to the detail
nodes that state them.

**Tex declarations without a proof.** These reused sketches keep their existing proof:
- `sk-def-sfb-dc-upper-shriek` (#50), with the tex's plan of proof put in front of it;
- `sk-lem-nagata-sketch-elimination` (#193);
- `sk-lem-nagata-sketch-boundary` (#196);
- `sk-thm-purity-transport` (#151).

**Problems in existing nodes noticed during the work (not changed):**
- **`thm-sfb-finite-proper-pushforward-left-adjoint`** claims that $Rg_*$ has a right adjoint on the unbounded
  pro-étale category. The smooth-purity block's own counterexample suggests this fails in general.
- **`prop-sfb-bounded-constructible-triangulated`** claims that $D_{\mathrm{cons}}$ is triangulated for any ring
  object. The tex says this fails for a general condensed ring. The sketch `sk-def-sfb-bounded-constructible` makes the
  same claim.
- **#176 (`sk-prop-sp-purity-bc`).** The moved node `def-pur-smooth-pullback-exchange` defines the base-change exchange
  through the purity map $\gamma$. That makes `thm-pur-smooth-base-change-coherence` hold by definition. The tex, and
  the new detail nodes of the sketch, use the exchange defined through the counit.
- **`sk-thm-chow`.** `cor-chow-lemma-proper` moved to `sk-thm-chow-projective` (#201). No detail node left in
  `sk-thm-chow` covers the clause "if $f$ is proper, $i$ is a closed immersion".
- **`thm-weil-pbc-stein-inputs`.** It is used for #56 (`sk-thm-pbc-henselian-h0`) and is tagged `latex:openproblem`.
- **`sk-cor-picard-degree-g`** says its curve "satisfies the hypotheses of `sk-thm-picard-rr`". Those hypotheses are
  now the tex's (smooth, projective, geometrically connected), so the sentence should be checked.
- **`sk-def-pbc-curve-assertions`** is blueprint-only. It defines the assertions (C1)–(C8) that #62 and #214 prove.
  It keeps its detail nodes, so the (C1)–(C8) family is not split.

**Detail nodes.** In the existing blueprint, many tex results were proved only as detail nodes buried in large sketch
directories, mostly `sk-thm-p1`, `sk-thm-properbasechange`, `sk-prop-sf-cbc` and `sk-thm-smooth-purity`. Those nodes
were moved into the new sketch of the declaration they prove. That is 396 file moves (statement and proof files), 181
of them across blocks: for example, the pro-étale comparison nodes went from proper base change to block 7. Ids never
change, so every reference still resolves.

Candidates that turned out to state something else were left where they were. The 11 blueprint-only sketches of block
7 that had no detail node received detail nodes. Every sketch directory in blocks 1–5 and 7–9 now has at least one
detail node.

**Not updated.** The block summaries (`sec-*/_section.md`) still describe the previous sketch lists.

## Tex declaration → sketch node

"reused" means an existing sketch node was rewritten to the tex statement; "new" means the node was created. The detail count is the number of detail nodes now in the sketch directory.


### §2 The pro-étale site and its comparison theorems

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 1 | 439 | Def Ind-étale, pro-étale and weakly étale morphisms | `pe:morphisms` | 7 | `sk-def-pe-morphisms` | new | 3 |
| 2 | 472 | Lem Stability | `pe:weakly-etale-stability` | 7 | `sk-lem-pe-weakly-etale-stability` | new | 2 |
| 3 | 497 | Def The small pro-étale site | `pe:site` | 7 | `sk-def-pe-site` | new | 3 |
| 4 | 521 | Prop The topos and its functoriality | `pe:topos-functoriality` | 7 | `sk-def-sfb-finite-pushforward-pullback` | reused | 14 |
| 5 | 552 | Def The local hierarchy | `pe:wlocal` | 7 | `sk-def-pe-wlocal` | new | 3 |
| 6 | 578 | Prop Stonean projectivity | `pe:stonean` | 7 | `sk-prop-pe-stonean` | new | 2 |
| 7 | 600 | Prop Splitting ind-étale covers | `pe:wc-rings` | 7 | `sk-prop-pe-wc-rings` | new | 3 |
| 8 | 621 | Thm Existence of contractible covers | `pe:wc-cover` | 7 | `sk-thm-pe-wc-cover` | new | 9 |
| 9 | 661 | Thm Weakly étale maps admit pro-étale refinements | `pe:indetale-refinement` | 7 | `sk-thm-pe-indetale-refinement` | new | 4 |
| 10 | 685 | Prop A cover-dense affine presentation | `pe:affine-basis` | 7 | `sk-prop-pe-affine-basis` | new | 2 |
| 11 | 702 | Thm Enough affine weakly contractible objects | `pe:weakly-contractible-basis` | 7 | `sk-thm-pe-weakly-contractible-basis` | new | 4 |
| 12 | 728 | Cor Exact sections on contractible affines | `pe:wc-sections` | 7 | `sk-cor-pe-wc-sections` | new | 2 |
| 13 | 760 | Def Weak contractibility | `pe:weak-contractible` | 7 | `sk-def-pe-weak-contractible` | new | 1 |
| 14 | 781 | Cor A conservative family preserving all module colimits | `pe:sections` | 7 | `sk-cor-pe-sections` | new | 3 |
| 15 | 817 | Rem Evaluation is not generally a point | `pe:evaluation-not-point` | 7 | `sk-rem-pe-evaluation-not-point` | new | 0 |
| 16 | 835 | Def Repleteness | `pe:replete-def` | 7 | `sk-def-pe-replete` | new | 1 |
| 17 | 842 | Prop Repleteness of the pro-étale topos | `pe:replete` | 7 | `sk-prop-pe-replete` | new | 2 |
| 18 | 860 | Prop Exact products | `pe:products` | 7 | `sk-prop-pe-products` | new | 2 |
| 19 | 898 | Prop The Milnor sequence | `pe:milnor` | 7 | `sk-prop-pe-milnor` | new | 3 |
| 20 | 936 | Prop Left completeness | `pe:left-complete` | 7 | `sk-prop-pe-left-complete` | new | 2 |
| 21 | 970 | Prop Weakly contractible hypercovers | `pe:hypercover` | 7 | `sk-prop-pe-hypercover` | new | 2 |
| 22 | 1016 | Cor Bounded-below continuity | `pe:bounded-continuity` | 7 | `sk-cor-pe-bounded-continuity` | new | 2 |
| 23 | 1058 | Def Classical pro-étale sheaves | `pe:classical-definition` | 7 | `sk-def-pe-classical-definition` | new | 1 |
| 24 | 1071 | Prop The comparison morphism and its inverse image | `pe:comparison-morphism` | 7 | `sk-prop-pe-comparison-morphism` | new | 3 |
| 25 | 1115 | Thm Recognizing the classical part | `pe:classical-sheaves` | 7 | `sk-thm-pe-classical-sheaves` | new | 3 |
| 26 | 1139 | Ex A coefficient sheaf outside the classical part | `pe:nonclassical-example` | 7 | `sk-rem-pe-nonclassical-example` | new | 0 |
| 27 | 1165 | Lem Acyclicity of pulled-back injectives | `pe:injective-acyclicity` | 7 | `sk-lem-pe-injective-acyclicity` | new | 4 |
| 28 | 1193 | Thm Bounded-below cohomology comparison | `pe:cohomology-comparison` | 8 | `sk-prop-sf-comparison` | reused | 5 |
| 29 | 1238 | Cor The derived classical part | `pe:classical-derived` | 7 | `sk-cor-pe-classical-derived` | new | 2 |
| 30 | 1278 | Thm Direct-image comparison | `pe:direct-image-comparison` | 7 | `sk-thm-pe-direct-image-comparison` | new | 3 |
| 31 | 1345 | Lem Descent of classical-group torsors | `pe:torsor-comparison` | 7 | `sk-lem-pe-torsor-comparison` | new | 2 |
| 32 | 1365 | Prop Locally constant sheaves of finite presentation | `pe:finite-local-systems` | 7 | `sk-prop-pe-finite-local-systems` | new | 3 |
| 33 | 1386 | Thm Constructible comparison | `pe:constructible-comparison` | 7 | `sk-thm-pe-constructible-comparison` | new | 3 |
| 34 | 1415 | Cor Finite Tor amplitude under comparison | `pe:finite-tor-comparison` | 7 | `sk-cor-pe-finite-tor-comparison` | new | 4 |
| 35 | 1449 | Def Cohomological dimension | `n:def-cd` | 7 | `sk-def-cd` | new | 2 |
| 36 | 1471 | Lem — | `b:lem:base-field-cd` | 7 | `sk-lem-base-field-cd` | new | 5 |
| 37 | 1526 | Prop Unbounded comparison for finite coefficients | `pe:unbounded-classical` | 7 | `sk-prop-pe-unbounded-classical` | new | 6 |
| 38 | 1619 | Prop The pro-étale geometric point | `pe:condensed-point` | 7 | `sk-prop-pe-condensed-point` | new | 3 |
| 39 | 1650 | Prop Continuous cohomology as pro-étale cohomology | `pe:continuous-cohomology` | 7 | `sk-prop-pe-continuous-cohomology` | new | 3 |
| 40 | 1692 | Ex The first cohomology of a finite field | `pe:finite-field-adic` | 7 | `sk-rem-pe-finite-field-adic` | new | 0 |
| 41 | 1717 | Prop Open–closed operations on module sheaves | `pe:open-closed` | 8 | `sk-prop-sf-open-closed-triangle` | reused | 21 |
| 42 | 1780 | Def Derived adic completeness | `pe:derived-completion` | 7 | `sk-def-pe-derived-completion` | new | 3 |
| 43 | 1800 | Lem Reduction and derived Nakayama | `pe:derived-nakayama` | 7 | `sk-lem-pe-derived-nakayama` | new | 4 |

### §3 Coefficients, constructible complexes and the main theorem

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 44 | 1910 | Lem Comparison with completed coefficients | `n:coefficient-comparison` | 7 | `sk-prop-sfb-qlbar-colimit-x` | reused | 7 |
| 45 | 1964 | Def Tate twists | `def:sp-Tate-twist` | 7 | `sk-def-sp-tate-twist` | new | 4 |
| 46 | 2010 | Prop Rationalization | `n:rationalization` | 7 | `sk-thm-sfb-rationalization-comparison` | reused | 6 |
| 47 | 2049 | Def Local models and constructible sheaves | `n:def-constructible` | 7 | `sk-def-sfb-constructible` | reused | 5 |
| 48 | 2109 | Prop The integral constructibility criterion | `n:integral-criterion` | 7 | `sk-prop-integral-criterion` | new | 4 |
| 49 | 2165 | Def The localizing closure | `—` | 7 | `sk-def-localizing-closure` | new | 2 |
| 50 | 2185 | Thm The exceptional inverse image | `n:existence` | 7 | `sk-def-sfb-dc-upper-shriek` | reused | 4 |
| 51 | 2209 | Cor — | `n:existence-b` | 7 | `sk-cor-existence-ii` | new | 4 |

### §4 Proper base change

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 52 | 2277 | Conv — | `pbc:conventions` | 5 | `sk-def-pbc-conventions` | new | 4 |
| 53 | 2353 | Def Derived exchange | `pbc:exchange` | 5 | `sk-def-exchange` | reused | 49 |
| 54 | 2394 | Lem Identity and pasting | `pbc:exchange-pasting` | 5 | `sk-lem-pbc-exchange-pasting` | new | 2 |
| 55 | 2445 | Def Torsion and the PBC property | `pbc:property` | 5 | `sk-def-pbc` | reused | 11 |
| 56 | 2477 | Thm Henselian-pair comparison in degree zero | `pbc:henselian-h0` | 5 | `sk-thm-pbc-henselian-h0` | new | 9 |
| 57 | 2502 | Prop Proper base change in degree zero | `pbc:degree-zero` | 5 | `sk-prop-pbc-degree-zero` | new | 3 |
| 58 | 2563 | Def Injective acyclicity | `pbc:ia` | 5 | `sk-def-ia` | reused | 1 |
| 59 | 2581 | Lem Acyclic resolutions | `pbc:acyclicity` | 5 | `sk-thm-acyclicity` | reused | 1 |
| 60 | 2644 | Thm PBC and injective acyclicity | `pbc:ia-equivalence` | 5 | `sk-thm-iff` | reused | 15 |
| 61 | 2738 | Rem — | `pbc:proof-division` | 5 | `sk-rem-pbc-proof-division` | new | 0 |
| 62 | 2802 | Thm Cohomology of curves | `pbc:curve-input` | 5 | `sk-thm-pbc-curve-input` | new | 6 |
| 63 | 2841 | Lem Extension of a separably closed ground field | `pbc:curve-field-extension` | 5 | `sk-lem-pbc-curve-field-extension` | new | 4 |
| 64 | 2863 | Rem — | `—` | 5 | `sk-rem-pbc-characteristic-torsion` | new | 0 |
| 65 | 2917 | Lem Acyclicity on the closed projective line | `pbc:p1-injective-fibre` | 5 | `sk-lem-pbc-p1-injective-fibre` | new | 10 |
| 66 | 2978 | Prop Henselian comparison for the projective line | `pbc:p1-henselian` | 5 | `sk-prop-pbc-p1-henselian` | new | 2 |
| 67 | 3030 | Prop Proper base change for the projective line | `pbc:p1` | 5 | `sk-thm-p1` | reused | 428 |
| 68 | 3107 | Rem — | `—` | 5 | `sk-rem-pbc-p1-inputs` | new | 0 |
| 69 | 3123 | Lem Finite morphisms | `pbc:finite` | 5 | `sk-lem-pbc-finite` | new | 6 |
| 70 | 3161 | Lem Composition and cancellation | `pbc:composition-cancellation` | 5 | `sk-lem-pbc-composition-cancellation` | new | 7 |
| 71 | 3234 | Lem A finite cover of projective space | `pbc:symmetric-product` | 5 | `sk-lem-pbc-symmetric-product` | new | 6 |
| 72 | 3291 | Lem Chow's lemma | `pbc:chow` | 5 | `sk-thm-chow` | reused | 14 |
| 73 | 3310 | Rem Chow's lemma over arbitrary bases | `pbc:chow-scope` | 5 | `sk-rem-pbc-chow-scope` | new | 0 |
| 74 | 3318 | Prop Reduction to the projective line | `pbc:reduction` | 5 | `sk-thm-reduction` | reused | 8 |
| 75 | 3344 | Thm Proper base change on classical pro-étale complexes | `pbc:torsion-theorem` | 5 | `sk-thm-properbasechange` | reused | 148 |
| 76 | 3406 | Cor Geometric-fibre formula | `pbc:torsion-stalk` | 5 | `sk-cor-pbc-torsion-stalk` | new | 2 |
| 77 | 3434 | Rem The role of properness | `pbc:reduction-inputs` | 5 | `sk-rem-pbc-reduction-inputs` | new | 0 |
| 78 | 3455 | Cor Classical finite coefficients on the pro-étale site | `pbc:proet-finite` | 5 | `sk-cor-pbc-proet-finite` | new | 2 |
| 79 | 3495 | Prop Proper base change for complete integral complexes | `pbc:complete` | 5 | `sk-prop-pbc-complete` | new | 8 |
| 80 | 3585 | Ex Fibrewise computation and the need for properness | `—` | 5 | `sk-rem-pbc-fibrewise-properness` | new | 0 |

### §5 Constructible sheaves and reduction to finite coefficients

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 81 | 3630 | Lem Inverse image of the coefficient sheaves | `b:lem:coefficient-pullback` | 7 | `sk-prop-sfb-cartesian-coefficients` | reused | 6 |
| 82 | 3699 | Lem Constructible sheaves | `b:lem:coefficient-heart` | 7 | `sk-lem-coefficient-heart` | new | 4 |
| 83 | 3718 | Ex A running example | `b:ex:running` | 7 | `sk-rem-running` | new | 0 |
| 84 | 3776 | Cor — | `b:lem:coefficient-heart-b` | 7 | `sk-cor-coefficient-heart-ii` | new | 2 |
| 85 | 3818 | Lem Continuity of cohomology | `b:lem:bounded-continuity` | 7 | `sk-lem-bounded-continuity` | new | 2 |
| 86 | 3861 | Lem Sections with support in a closed subscheme | `b:lem:formal-closed-support` | 7 | `sk-lem-formal-closed-support` | new | 5 |
| 87 | 3931 | Lem Continuity of Ext out of a constructible complex | `b:lem:constructible-ext-continuity` | 7 | `sk-lem-constructible-ext-continuity` | new | 2 |
| 88 | 4004 | Lem Descent to a finite coefficient field | `b:lem:coefficient-finite-descent` | 7 | `sk-lem-coefficient-finite-descent` | new | 4 |
| 89 | 4109 | Lem Lattices after a finite stratification | `b:lem:stratified-lattice` | 7 | `sk-lem-stratified-lattice` | new | 3 |
| 90 | 4200 | Lem Integral models | `b:lem:integral-models` | 7 | `sk-lem-integral-models` | new | 3 |
| 91 | 4300 | Prop Proper direct image of constructible complexes | `b:prop:proper-coefficients` | 7 | `sk-thm-sfb-proper-base-change` | reused | 3 |

### §6 Construction of the exceptional inverse image

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 92 | 4467 | Lem — | `b:lem:formal-closed-support-b` | 7 | `sk-lem-formal-closed-support-ii` | new | 2 |
| 93 | 4487 | Lem Uniform Ext bound | `b:lem:uniform-constructible-ext` | 7 | `sk-lem-uniform-constructible-ext` | new | 4 |
| 94 | 4609 | Prop Ind-constructible sheaves | `b:prop:ind-heart` | 7 | `sk-prop-ind-heart` | new | 6 |
| 95 | 4709 | Cor — | `b:prop:ind-heart-b` | 7 | `sk-cor-ind-heart-ii` | new | 2 |
| 96 | 4728 | Cor — | `b:cor:ambient-ind-derived` | 7 | `sk-cor-ambient-ind-derived` | new | 2 |
| 97 | 4754 | Lem Reduction to finitely many degrees | `b:lem:finite-window` | 7 | `sk-lem-finite-window` | new | 3 |
| 98 | 4818 | Thm Compactness with rational coefficients | `b:thm:constructible-compactness` | 7 | `sk-thm-constructible-compactness` | new | 3 |
| 99 | 4862 | Cor — | `b:thm:constructible-compactness-b` | 7 | `sk-cor-constructible-compactness-ii` | new | 1 |
| 100 | 4906 | Lem Cohomology commutes with filtered colimits | `b:lem:proper-heart-continuity` | 7 | `sk-lem-proper-heart-continuity` | new | 3 |
| 101 | 4942 | Lem A uniform bound for proper direct image | `b:lem:proper-heart-bound` | 7 | `sk-lem-proper-heart-bound` | new | 5 |
| 102 | 5031 | Lem Proper direct image of unbounded complexes | `b:lem:proper-unbounded-window` | 7 | `sk-lem-proper-unbounded-window` | new | 3 |
| 103 | 5101 | Lem Proper direct image preserves direct sums | `b:lem:proper-unbounded-window-b` | 7 | `sk-lem-proper-unbounded-window-ii` | new | 2 |
| 104 | 5144 | Prop Proper direct image and extension by zero | `b:prop:proper-image-localizing` | 7 | `sk-prop-proper-image-localizing` | new | 4 |
| 105 | 5181 | Lem Checking isomorphisms on constructible complexes | `b:lem:localizing-comparison` | 8 | `sk-lem-sf-determination` | reused | 3 |
| 106 | 5214 | Prop Proper base change on the localizing categories | `b:prop:proper-base-change-unbounded` | 7 | `sk-prop-proper-base-change-unbounded` | new | 2 |
| 107 | 5265 | Prop Construction and independence of $Rf_!$ | `b:prop:lower-exceptional-image` | 8 | `sk-prop-sf-comp-coherence` | reused | 5 |
| 108 | 5336 | Prop Composition and base change for $Rf_!$ | `b:prop:lower-composition` | 8 | `sk-thm-sf-comp-composition` | reused | 3 |
| 109 | 5443 | Lem Flat models and generators | `ctf:finite-models` | 8 | `sk-lem-sf-flat-model` | reused | 3 |
| 110 | 5483 | Prop Compactness for finite coefficients | `ctf:finite-compact` | 7 | `sk-prop-ctf-finite-compact` | new | 3 |
| 111 | 5534 | Prop Comparison with the étale derived category | `ctf:finite-comparison` | 7 | `sk-prop-ctf-finite-comparison` | new | 2 |
| 112 | 5569 | Prop Proper direct image for finite coefficients | `ctf:finite-proper` | 7 | `sk-prop-ctf-finite-proper` | new | 5 |
| 113 | 5645 | Lem Hypotheses of Brown representability | `b:lem:brown-hypotheses` | 7 | `sk-lem-brown-hypotheses` | new | 3 |
| 114 | 5677 | Thm Existence of the exceptional inverse image | `b:thm:brown-adjoint` | 8 | `sk-prop-sf-existence` | reused | 21 |
| 115 | 5759 | Prop Composition, open restriction and compactifications for $f^!$ | `b:prop:composition-locality` | 8 | `sk-lem-sf-mate` | reused | 7 |

### §7 The exceptional inverse image preserves constructibility

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 116 | 5952 | Lem The cycle class of a Cartier divisor | `b:lem:geo-cartier` | 9 | `sk-lem-geo-cartier` | new | 2 |
| 117 | 6024 | Lem Cohomology of the projective line and the trace | `b:lem:geo-p1-cohomology` | 9 | `sk-lem-geo-p1-cohomology` | new | 2 |
| 118 | 6089 | Ex Compact supports on the running example | `—` | 9 | `sk-rem-compact-supports-running-example` | new | 0 |
| 119 | 6113 | Prop The projective-line adjunction | `b:prop:geo-p1-adjunction` | 9 | `sk-prop-geo-p1-adjunction` | new | 2 |
| 120 | 6273 | Lem Affine space and étale localization | `b:lem:geo-affine-local` | 9 | `sk-lem-geo-affine-local` | new | 2 |
| 121 | 6330 | Prop The exceptional inverse image of a smooth morphism | `b:prop:geo-smooth-tensor` | 8 | `sk-prop-cohsm` | reused | 4 |
| 122 | 6430 | Lem Smooth morphisms and locally constant sheaves | `b:lem:geo-smooth-generic` | 9 | `sk-lem-geo-smooth-generic` | new | 1 |
| 123 | 6536 | Lem Detection by a proper direct image | `b:lem:geo-finite-boundary` | 9 | `sk-lem-geo-finite-boundary` | new | 2 |
| 124 | 6602 | Lem Coordinate projections | `b:lem:geo-coordinates` | 9 | `sk-lem-geo-coordinates` | new | 2 |
| 125 | 6661 | Thm Generic constructibility and base change for \(Rj_*\) | `b:thm:geo-generic-open` | 9 | `sk-thm-geo-generic-open` | new | 1 |
| 126 | 6847 | Cor Open direct image over a field | `b:cor:geo-open-finiteness` | 9 | `sk-cor-geo-open-finiteness` | new | 3 |
| 127 | 6889 | Cor Finite cohomological dimension of open direct image | `b:cor:geo-open-finiteness-b` | 9 | `sk-cor-geo-open-finiteness-ii` | new | 1 |
| 128 | 6925 | Prop Open direct image preserves finite Tor amplitude | `ctf:finite-open` | 9 | `sk-cor-sf-direct-image-ctf` | reused | 3 |
| 129 | 6979 | Thm $f^!$ with finite coefficients | `ctf:finite-restriction` | 9 | `sk-prop-sf-rf-shriek-preservation` | reused | 33 |
| 130 | 7045 | Cor The six operations on $\Dctf(-,A)$ | `ctf:finite-operations` | 9 | `sk-rem-sf-matrix` | reused | 2 |
| 131 | 7112 | Prop Direct image along an open immersion | `b:prop:open-coefficients` | 9 | `sk-prop-open-coefficients` | new | 2 |
| 132 | 7166 | Prop The $\ell$-adic cycle class of the diagonal | `b:prop:diagonal-tower` | 9 | `sk-prop-diagonal-tower` | new | 4 |
| 133 | 7365 | Prop Projection formula and proper base change with rational coefficients | `b:prop:pf-bc-generated` | 9 | `sk-thm-sf-pf-field` | reused | 5 |
| 134 | 7412 | Prop The projective line | `b:prop:p1-adjunction-rational` | 9 | `sk-prop-p1-adjunction-rational` | new | 2 |
| 135 | 7488 | Cor — | `b:cor:affine-space-rational` | 9 | `sk-cor-affine-space-rational` | new | 2 |
| 136 | 7528 | Ex — | `b:ex:closed-support` | 9 | `sk-rem-closed-support` | new | 0 |
| 137 | 7541 | Prop — | `b:prop:closed-adjoint-constructible` | 9 | `sk-prop-closed-adjoint-constructible` | new | 2 |
| 138 | 7565 | Thm $f^!$ with rational coefficients | `b:thm:restriction` | 9 | `sk-thm-restriction` | new | 3 |
| 139 | 7612 | Rem — | `—` | 9 | `sk-rem-restriction-inputs` | new | 0 |

### §8 Integral coefficients

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 140 | 7678 | Lem Structure of integral constructible complexes | `i:integral-heart` | 9 | `sk-lem-int-integral-heart` | new | 3 |
| 141 | 7762 | Lem Inverse image and tensor product | `i:tensor` | 7 | `sk-def-sfb-dc-restricted-functors` | reused | 15 |
| 142 | 7825 | Lem Continuity and boundedness of Ext | `i:ext` | 9 | `sk-lem-int-ext` | new | 3 |
| 143 | 7905 | Prop Compactness and proper direct image | `i:compactness` | 9 | `sk-prop-int-compactness` | new | 3 |
| 144 | 7973 | Cor — | `i:compactness-b` | 9 | `sk-cor-int-compactness-ii` | new | 1 |
| 145 | 7989 | Prop Compactly supported direct image and its adjoint | `i:brown` | 9 | `sk-prop-int-brown` | new | 3 |
| 146 | 8012 | Lem Open direct image and projection formula | `i:open-pf` | 9 | `sk-thm-sf-pf-adic` | reused | 5 |
| 147 | 8057 | Thm $f^!$ preserves integral constructible complexes | `i:restriction` | 9 | `sk-thm-int-restriction` | new | 4 |

### §9 The six functors on constructible complexes of finite Tor amplitude

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 148 | 8147 | Prop The six functors on $\Dctf$ | `n:six-small` | 9 | `sk-thm-sf-ctf-stability` | reused | 15 |
| 149 | 8224 | Prop The six operations and coefficient comparison | `n:scalar-six` | 7 | `sk-def-sfb-coefficient-comparisons` | reused | 29 |
| 150 | 8373 | Prop $\Dctf(X,\Qbar)$ as a $2$-colimit | `n:two-colimit` | 7 | `sk-thm-sfb-qlbar-two-colimit` | reused | 16 |

### §10 Smooth purity

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 151 | 8476 | Thm Smooth purity for all admissible coefficients | `thm:sp-integral` | 8 | `sk-thm-purity-transport` | reused | 4 |
| 152 | 8499 | Def Relative dualizing complex | `def:sp-dualizing` | 8 | `sk-def-sp-dualizing` | new | 1 |
| 153 | 8593 | Lem The projective-line adjunction | `lem:sp-p1` | 8 | `sk-lem-sp-p1` | new | 2 |
| 154 | 8664 | Def Representing objects | `def:sp-representing-pair` | 8 | `sk-def-sp-representing-pair` | new | 2 |
| 155 | 8680 | Prop Étale and pro-étale finite coefficients | `prop:sp-et-proet` | 8 | `sk-prop-sp-et-proet` | new | 2 |
| 156 | 8702 | Lem Local computation of the finite Brown adjoint | `lem:sp-finite-existence` | 8 | `sk-lem-sp-finite-existence` | new | 3 |
| 157 | 8745 | Prop Vector-bundle purity | `prop:sp-vector` | 8 | `sk-prop-an` | reused | 26 |
| 158 | 8848 | Prop The tensor formula | `prop:sp-tensor` | 8 | `sk-prop-sp-tensor` | new | 1 |
| 159 | 8879 | Prop Exceptional base change for a smooth map | `prop:sp-exceptional-bc` | 8 | `sk-prop-sp-exceptional-bc` | new | 1 |
| 160 | 8926 | Lem A section and its normal bundle | `lem:sp-dnc` | 8 | `sk-thm-dnc` | reused | 3 |
| 161 | 9015 | Prop The relative dualizing complex | `prop:sp-orientation` | 8 | `sk-prop-sp-orientation` | new | 4 |
| 162 | 9093 | Prop Finite-coefficient smooth purity | `prop:sp-finite` | 8 | `sk-thm-smooth-purity` | reused | 7 |
| 163 | 9148 | Def Extension of coefficients | `def:sp-scalar-extension` | 8 | `sk-def-sp-scalar-extension` | new | 1 |
| 164 | 9159 | Lem Coefficient comparison | `lem:sp-reduction` | 8 | `sk-lem-sp-reduction` | new | 5 |
| 165 | 9259 | Def Coefficient towers | `def:sp-coefficient-towers` | 8 | `sk-def-sp-coefficient-towers` | new | 2 |
| 166 | 9283 | Def Constructible and normalized towers | `def:sp-normalized-towers` | 8 | `sk-def-sp-normalized-towers` | new | 3 |
| 167 | 9298 | Lem Reconstruction of a normalized tower | `lem:sp-tower` | 8 | `sk-lem-sp-tower` | new | 3 |
| 168 | 9358 | Lem Levels of the tower direct image | `lem:sp-tower-levels` | 8 | `sk-lem-sp-tower-levels` | new | 2 |
| 169 | 9407 | Lem Direct image preserves constructible towers | `lem:sp-tower-bound` | 8 | `sk-lem-sp-tower-bound` | new | 2 |
| 170 | 9424 | Prop The tower model of the smooth adjunction | `prop:sp-tower-geometric` | 8 | `sk-prop-sp-tower-geometric` | new | 4 |
| 171 | 9603 | Prop The normalized model of the integral adjunction | `prop:sp-integral-adjunction` | 8 | `sk-prop-sp-integral-adjunction` | new | 2 |
| 172 | 9655 | Prop Comparison with any other right adjoint | `prop:sp-unique-adjoint` | 8 | `sk-prop-sp-unique-adjoint` | new | 2 |
| 173 | 9722 | Prop Smooth purity with coefficients $E$ | `cor:sp-rational` | 8 | `sk-prop-sp-rational` | new | 2 |
| 174 | 9758 | Lem Compatibility with finite extensions of $E$ | `lem:sp-field-extension` | 8 | `sk-lem-sp-field-extension` | new | 2 |
| 175 | 9805 | Thm Smooth purity with algebraically closed coefficients | `thm:sp-qbar` | 8 | `sk-thm-sp-qbar` | new | 2 |
| 176 | 9934 | Prop Base change of purity | `prop:sp-purity-bc` | 8 | `sk-prop-sp-purity-bc` | new | 5 |
| 177 | 10011 | Prop Composition of purity | `prop:sp-composition` | 8 | `sk-prop-sp-composition` | new | 4 |
| 178 | 10078 | Def Smooth trace | `def:sp-trace` | 8 | `sk-def-sp-trace` | new | 2 |
| 179 | 10095 | Prop Transitivity of the smooth trace | `prop:sp-trace-composition` | 8 | `sk-prop-sp-trace-composition` | new | 2 |
| 180 | 10144 | Cor The dualizing complex of a smooth scheme | `cor:sp-all-coefficients` | 8 | `sk-cor-sp-all-coefficients` | new | 2 |
| 181 | 10248 | Def Weil structure | `def:sp-Weil-structure` | 9 | `sk-def-sf-weil-complexes` | reused | 2 |
| 182 | 10324 | Prop Smooth purity for $f^!$ | `prop:sp-comparison-brown` | 8 | `sk-prop-sp-comparison-brown` | new | 2 |

### §11 Compactification and projective domination

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 183 | 10396 | Def Compactification and refinement | `app:nagata-definition` | 1 | `sk-def-nagata-sketch-data` | reused | 56 |
| 184 | 10410 | Thm Nagata compactification | `app:nagata-theorem` | 1 | `sk-thm-nagata-compactification` | reused | 10 |
| 185 | 10430 | Lem Schematic closure and uniqueness | `app:nagata-closure` | 1 | `sk-lem-nagata-sketch-closure` | reused | 23 |
| 186 | 10454 | Lem Passing to the schematic closure | `app:nagata-density-normalization` | 1 | `sk-lem-nagata-density-normalization` | new | 3 |
| 187 | 10494 | Rem — | `—` | 1 | `sk-rem-nagata-closure-scope` | new | 0 |
| 188 | 10503 | Prop Common dense refinements | `app:nagata-refinement` | 1 | `sk-prop-nagata-sketch-comp-category` | reused | 19 |
| 189 | 10539 | Rem Base change of a compactification | `app:nagata-base-change` | 1 | `sk-rem-nagata-base-change` | new | 0 |
| 190 | 10559 | Def Admissible blow-up | `app:nagata-admissible` | 1 | `sk-def-nagata-admissible` | new | 4 |
| 191 | 10588 | Lem Making an open schematically dense | `app:nagata-boundary-divisor` | 1 | `sk-lem-nagata-boundary-divisor` | new | 5 |
| 192 | 10626 | Lem Finite refinements of blow-ups | `app:nagata-blowup-refinements` | 1 | `sk-lem-nagata-sketch-blowups` | reused | 85 |
| 193 | 10657 | Thm Elimination of indeterminacy | `app:nagata-elimination` | 1 | `sk-lem-nagata-sketch-elimination` | reused | 4 |
| 194 | 10684 | Cor Extension to a proper target | `app:nagata-proper-extension` | 1 | `sk-cor-nagata-sketch-proper-extension` | reused | 3 |
| 195 | 10706 | Lem Graph extension from a compactification | `app:nagata-graph-extension` | 1 | `sk-lem-nagata-sketch-graph` | reused | 2 |
| 196 | 10739 | Lem Separation of closures | `app:nagata-separation` | 1 | `sk-lem-nagata-sketch-boundary` | reused | 10 |
| 197 | 10756 | Lem An isomorphism near a boundary closure | `app:nagata-near-closure` | 1 | `sk-lem-nagata-sketch-near-closure` | reused | 5 |
| 198 | 10781 | Lem Separated common modification of two opens | `app:nagata-common-modification` | 1 | `sk-lem-nagata-sketch-common` | reused | 7 |
| 199 | 10813 | Prop The two-open compactification construction | `app:nagata-two-open` | 1 | `sk-thm-nagata-sketch-two-open` | reused | 21 |
| 200 | 10896 | Lem Enough compactifiable affine opens | `app:nagata-affine-opens` | 1 | `sk-lem-nagata-sketch-affine-cover` | reused | 15 |
| 201 | 10958 | Thm Projective domination of a proper morphism | `app:chow-projective` | 1 | `sk-thm-chow-projective` | new | 3 |

### §12 Picard schemes and Jacobians

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 202 | 11027 | Def Relative Picard functor | `—` | 3 | `sk-def-picard-pic` | reused | 11 |
| 203 | 11048 | Lem Rigidification along a section | `app:picard-rigidification` | 3 | `sk-prop-picard-pic-split` | reused | 8 |
| 204 | 11100 | Thm Riemann–Roch and coherent Serre duality | `app:picard-riemann-roch` | 3 | `sk-thm-picard-rr` | reused | 40 |
| 205 | 11126 | Lem Coherent base change for invertible sheaves | `app:picard-coherent-base-change` | 3 | `sk-thm-picard-perfect` | reused | 5 |
| 206 | 11162 | Thm Hilbert schemes of points on a smooth curve | `app:picard-hilbert-theorem` | 3 | `sk-thm-picard-hilb-curves` | reused | 12 |
| 207 | 11202 | Prop Divisors of degree $g$ as an open chart | `app:picard-abel-chart` | 3 | `sk-thm-picard-f-representable` | reused | 4 |
| 208 | 11238 | Lem Translating into the chart | `app:picard-twist` | 3 | `sk-thm-picard-twist` | reused | 6 |
| 209 | 11273 | Thm The Picard scheme and Jacobian of a geometric curve | `app:picard-curve` | 3 | `sk-thm-picard-main` | reused | 6 |
| 210 | 11342 | Cor The degree sequence | `app:picard-degree` | 3 | `sk-cor-picard-degree` | new | 1 |
| 211 | 11361 | Rem Ground fields and relative representability | `app:picard-relative-scope` | 3 | `sk-rem-picard-relative-scope` | new | 0 |
| 212 | 11384 | Prop Multiplication on an abelian variety | `app:abelian-multiplication` | 2 | `sk-thm-av-final` | reused | 2 |
| 213 | 11418 | Cor Jacobian torsion and geometric extension | `app:jacobian-torsion` | 2 | `sk-prop-av-ntorsion-etale` | reused | 3 |

### §13 Cohomology of curves

| # | Tex line | Declaration | Label | Block | Sketch node | | Details |
|---:|---:|---|---|---|---|---|---:|
| 214 | 11502 | Thm Cohomology of curves over an algebraically closed field | `app:curve-package` | 4 | `sk-thm-curve-package` | new | 2 |
| 215 | 11548 | Lem Cohomology of the multiplicative group | `app:curve-gm` | 4 | `sk-thm-br` | reused | 25 |
| 216 | 11594 | Prop Smooth proper curves with invertible torsion | `app:curve-kummer` | 4 | `sk-thm-curveestimate` | reused | 2 |
| 217 | 11650 | Rem Twists and the projective line | `app:curve-twists` | 4 | `sk-rem-curve-twists` | new | 0 |
| 218 | 11668 | Prop Cohomology of a smooth affine curve | `app:curve-affine-kummer` | 4 | `sk-prop-curve-affine-kummer` | new | 4 |
| 219 | 11749 | Prop Characteristic torsion on a smooth proper curve | `app:curve-artin-schreier` | 4 | `sk-prop-curve-artin-schreier` | new | 4 |
| 220 | 11803 | Lem Characteristic torsion on an affine curve | `app:curve-affine-artin-schreier` | 4 | `sk-lem-curve-affine-artin-schreier` | new | 1 |
| 221 | 11820 | Ex The affine line in characteristic $p$ | `app:curve-wild-example` | 4 | `sk-rem-curve-wild-example` | new | 0 |
| 222 | 11852 | Lem Finite-support sheaves and finite maps | `app:curve-finite-support` | 4 | `sk-lem-curve-finite-support` | new | 2 |
| 223 | 11875 | Lem Normalization of a constant sheaf | `app:curve-normalization` | 4 | `sk-lem-curve-normalization` | new | 4 |
| 224 | 11921 | Lem Removing finitely many points | `app:curve-dense-open` | 4 | `sk-lem-curve-dense-open` | new | 2 |
| 225 | 11965 | Lem Reduction to a unipotent local system | `app:curve-sylow-trace` | 4 | `sk-lem-curve-sylow-trace` | new | 3 |
| 226 | 12071 | Cor Proper curves over separably closed fields | `app:curve-invariance` | 4 | `sk-cor-curve-invariance` | new | 2 |

## Sketch nodes that appear only in the blueprint

These top-level nodes of blocks 1–5 and 7–9 correspond to no declaration of the tex file. They are kept unchanged (apart from their `order`, which now places them after the tex-aligned nodes). "Related tex" names the tex declarations whose matching pointed at the node as partly overlapping.


### Block 1: Nagata Compactification (13)

| Sketch node | Kind | Title | Details | Related tex |
|---|---|---|---:|---|
| `sk-cor-nagata-sketch-fp` | corollary | Nagata for finite presentation | 8 | #184 |
| `sk-def-conv` | definition | Scheme and morphism conventions | 12 | #52 |
| `sk-def-nagata-sketch-quasidomination` | definition | Quasi-domination | 2 |  |
| `sk-lem-nagata-sketch-dense-valuative` | lemma | Dense-source valuative criterion | 10 | #199 |
| `sk-lem-nagata-sketch-image-transform` | lemma | Images under admissible blow-up | 3 |  |
| `sk-prop-nagata-sketch-approximation` | proposition | Absolute approximation and descent | 43 | #72 |
| `sk-prop-nagata-sketch-envelope` | proposition | Separated finite-presentation envelope | 6 |  |
| `sk-prop-nagata-sketch-fp-models` | proposition | Finite-presentation models of a finite-type morphism | 11 |  |
| `sk-prop-nagata-sketch-key-disjointness` | proposition | Improved comparison and key disjointness | 2 | #199 |
| `sk-prop-nagata-sketch-prepared` | proposition | Prepared sides | 8 | #199 |
| `sk-prop-nagata-sketch-zmt` | proposition | Zariski's Main Theorem and affine-space immersions | 20 | #200 |
| `sk-thm-nagata-sketch-conrad` | theorem | Extension of a partial section after an admissible blow-up | 18 | #193 |
| `sk-thm-nagata-sketch-noetherian` | theorem | Nagata over a Noetherian base | 4 | #184 |

### Block 2: Abelian Varieties (39)

| Sketch node | Kind | Title | Details | Related tex |
|---|---|---|---:|---|
| `sk-cor-av-commutative` | corollary | Abelian varieties are commutative | 1 |  |
| `sk-d-ab-field` | definition | Finite fields, Frobenius and abelian varieties | 1 |  |
| `sk-d-ab-tate` | definition | Integral and rational Tate modules | 1 |  |
| `sk-def-av` | definition | Abelian varieties | 2 |  |
| `sk-def-av-ample-degree` | definition | Ample modules and the Hilbert degree | 4 |  |
| `sk-def-av-group-scheme` | definition | Group schemes, order, and étaleness | 5 |  |
| `sk-def-av-isogeny` | definition | Isogenies and their degree | 2 |  |
| `sk-def-av-jacobian` | definition | The Jacobian | 14 |  |
| `sk-def-av-mult-n` | definition | Multiplication by $n$ and $n$-torsion | 1 |  |
| `sk-def-av-pic` | definition | $\Pic$, degree, $\Pic^0$ | 5 |  |
| `sk-def-av-tate` | definition | $\ell$-adic Tate module | 1 |  |
| `sk-def-curve` | definition | Curves and genus | 3 |  |
| `sk-prop-av-ample-positive` | proposition | Ample modules on proper curves have positive degree | 1 |  |
| `sk-prop-av-char` | proposition | Abelian varieties are the complete group varieties | 1 |  |
| `sk-prop-av-connected-order` | proposition | Connected finite group schemes have $p$-power order | 1 |  |
| `sk-prop-av-const-locus` | proposition | The locus of constant fibres is closed | 1 |  |
| `sk-prop-av-cube` | proposition | The theorem of the cube | 1 |  |
| `sk-prop-av-deg-pullback` | proposition | Degree of a pullback under a finite morphism | 1 |  |
| `sk-prop-av-divisible` | proposition | Surjectivity of multiplication by $n$ on points | 3 | #213 |
| `sk-prop-av-divisible-structure` | proposition | The torsion of a divisible group | 1 | #213 |
| `sk-prop-av-finite-etale-points` | proposition | Points of finite étale group schemes | 6 |  |
| `sk-prop-av-fixed-base-change` | proposition | Fixed points are unchanged by algebraically closed base change | 1 | #219 |
| `sk-prop-av-fixed-points` | proposition | Fixed points of $p$-linear maps are finite | 1 | #219 |
| `sk-prop-av-image-open` | proposition | Finiteness of the image is open in the parameter | 1 |  |
| `sk-prop-av-isogeny` | proposition | The multiplication-by-$n$ isogeny | 2 | #212 |
| `sk-prop-av-isogeny-degree` | proposition | The degree of an isogeny is the degree of the kernel | 2 |  |
| `sk-prop-av-lang-steinberg` | proposition | Lang–Steinberg for $p$-linear maps | 2 | #219 |
| `sk-prop-av-mult-finite` | proposition | Finiteness of the fibres of the multiplication map | 1 | #212 |
| `sk-prop-av-mult-hom` | proposition | The $n$-fold sum is a homomorphism | 1 |  |
| `sk-prop-av-mult-n-pullback` | proposition | Pullback of symmetric modules under multiplication by $n$ | 1 |  |
| `sk-prop-av-mult-surjective` | proposition | Surjectivity of the multiplication map | 2 | #212 |
| `sk-prop-av-pqf-finite` | proposition | Proper and quasi-finite implies finite | 53 | #71 |
| `sk-prop-av-prime-p-etale` | proposition | Group schemes of order prime to $p$ are étale | 1 |  |
| `sk-prop-av-projective` | proposition | Abelian varieties are projective | 1 |  |
| `sk-prop-av-rigidity` | proposition | The rigidity lemma | 1 |  |
| `sk-prop-av-symmetric-ample` | proposition | A symmetric ample module | 3 |  |
| `sk-prop-av-tate-rank` | proposition | The $\ell$-adic Tate module is free of rank $2g$ | 1 | #213 |
| `sk-the-final-theorem-the-abelian-variety-estimate--remark-1` | remark | Remark | 0 |  |
| `the-final-theorem-the-abelian-variety-estimate--remark-1` | remark |  | 0 |  |

### Block 3: Picard Framework (30)

| Sketch node | Kind | Title | Details | Related tex |
|---|---|---|---:|---|
| `rem-picard-seams` | remark | The dependencies are one-way: $\mathbf A\Rightarrow\mathbf B$ at four seams | 0 |  |
| `sk-cor-picard-degree-g` | corollary | The degree of the dictionary | 1 | #207 |
| `sk-cor-picard-hilb-sheaf` | corollary | Hilbert functor is the fppf sheaf | 3 |  |
| `sk-cor-picard-pic-sheaf` | corollary | Picard functor is an fppf sheaf | 1 | #202, #203 |
| `sk-def-groth-ss` | definition | Composable pair with acyclicity; the couple of a double complex | 1 |  |
| `sk-def-picard-f` | definition | The subfunctor $F$ | 2 | #207 |
| `sk-lem-picard-affine` | lemma | Vanishing of cohomology on affine schemes | 3 |  |
| `sk-lem-picard-cech-computes` | lemma | Leray's theorem for quasi-coherent sheaves | 1 |  |
| `sk-lem-picard-f-open` | lemma | $F$ is an open subfunctor | 3 | #205, #207 |
| `sk-lem-picard-zero-dictionary` | lemma | The zero-scheme dictionary | 2 | #207 |
| `sk-prop-jacobian` | proposition | The Jacobian is an abelian variety | 2 | #209, #210, #211 |
| `sk-prop-jacobian-descent` | proposition | The Jacobian over a general base field, by Galois descent | 18 | #211 |
| `sk-prop-picard-degree-decomposition` | proposition | Degree decomposition of the Picard scheme | 5 | #209, #210 |
| `sk-prop-picard-dense-points` | proposition | Zariski density of rational points | 7 | #208 |
| `sk-prop-picard-jacobian-tangent` | proposition | The tangent space of the Jacobian | 1 | #209 |
| `sk-prop-picard-schemes-criterion` | proposition | The general representability criterion | 5 | #209 |
| `sk-rem-picard-seams` | remark | The dependencies are one-way: $\mathbf A\Rightarrow\mathbf B$ at four seams | 0 |  |
| `sk-the-hilbert-functor--definition-1` | definition | Hilbert functor | 5 | #206 |
| `sk-the-subsheaf-ff-and-its-representability--remark-1` | proposition | $F$ is a subfunctor of the Hilbert functor | 1 | #207 |
| `sk-thm-groth-ss` | theorem | Grothendieck spectral sequence and its Leray specialization | 3 | #70 |
| `sk-thm-picard-cech` | theorem | Čech-to-derived | 1 |  |
| `sk-thm-picard-coherence` | theorem | Coherence of the higher direct images | 27 | #205 |
| `sk-thm-picard-criterion` | theorem | The criterion: a functor generated by a representable open subfunctor | 1 | #209 |
| `sk-thm-picard-descent` | theorem | Descent | 2 |  |
| `sk-thm-picard-duality` | theorem | Serre duality | 21 | #204 |
| `sk-thm-picard-hilb-general` | theorem | Representability of $\Hilb^d$ — general case | 1 | #206 |
| `sk-thm-picard-pn` | theorem | Cohomology of $\PP^n$, Serre 1954 | 10 |  |
| `sk-thm-picard-semicon` | theorem | Semicontinuity and base change | 18 | #3, #205 |
| `sk-thm-picard-serre-a` | theorem | Serre's theorem A: global generation after a twist | 1 |  |
| `sk-thm-picard-serre-b` | theorem | Serre's theorem B: vanishing after a twist | 7 |  |

### Block 4: Curve Estimates (18)

| Sketch node | Kind | Title | Details | Related tex |
|---|---|---|---:|---|
| `sk-def-br` | definition | Brauer group | 1 |  |
| `sk-def-cr` | definition | $C_r$ fields | 1 |  |
| `sk-def-kummer` | definition | The Kummer sequence | 1 | #216 |
| `sk-def-pic` | definition | Picard group, degree, $\Pic^0$ | 2 | #210 |
| `sk-prop-br-inj` | proposition | Generic-point injection for the Brauer group | 2 | #215 |
| `sk-prop-cd` | proposition | Vanishing in high degrees | 16 | #62, #214, #219, #222 |
| `sk-prop-cd-affine` | proposition | Affine-curve cohomological dimension | 9 | #62, #214, #218, #220 |
| `sk-prop-divisor-gen` | proposition | Divisor sequence | 2 | #215 |
| `sk-prop-ext-invariance` | proposition | Invariance under extension of algebraically closed fields | 3 | #62, #63, #216, #218 |
| `sk-prop-h1` | proposition | $H^1$ via Kummer | 3 | #216, #218 |
| `sk-prop-h2` | proposition | $H^2$ via Kummer | 56 | #36, #216 |
| `sk-prop-hilbert90` | proposition | Hilbert 90 | 6 | #215 |
| `sk-prop-kummer-exact` | proposition | Exactness of the Kummer sequence | 1 | #216 |
| `sk-prop-tsen` | proposition | Tsen's theorem | 3 | #215 |
| `sk-the-final-theorem-the-curve-estimate--remark-1` | remark | Remark | 0 |  |
| `sk-the-final-theorem-the-curve-estimate--remark-2` | remark | Remark | 0 |  |
| `the-final-theorem-the-curve-estimate--remark-1` | remark |  | 0 |  |
| `the-final-theorem-the-curve-estimate--remark-2` | remark |  | 0 |  |

### Block 5: Proper Base Change (4)

| Sketch node | Kind | Title | Details | Related tex |
|---|---|---|---:|---|
| `sk-curve-calculations-pbc-for-the-projective-line--remark-1` | remark | Remark | 0 | #62, #214 |
| `sk-def-pbc-curve-assertions` | definition | The eight curve-cohomology assertions | 12 | #62, #214 |
| `sk-the-final-theorem--remark-1` | remark | Remark | 0 | #61, #77 |
| `the-final-theorem--remark-1` | remark |  | 0 | #61, #77 |

### Block 7: Six Functors: Basic Constructions (41)

| Sketch node | Kind | Title | Details | Related tex |
|---|---|---|---:|---|
| `rem-sfb-coefficient-layers` | remark | Two layers of coefficients | 0 | #3, #26 |
| `rem-sfb-constructible-coefficients` | remark | Constructibility over the coefficient rings | 0 | #47 |
| `rem-sfb-module-upper-shriek-and-qlbar` | remark | No ambient exceptional pullback; $\Qlb$-coefficients | 0 |  |
| `rem-sfb-what-lambda-x` | remark | What $\Lambda_X$ is | 0 | #26, #44 |
| `sk-def-sfb-base-change-morphism` | definition | The base change morphism on $D_{\mathrm{cons}}$ | 3 |  |
| `sk-def-sfb-bounded-constructible` | definition | Bounded constructible derived category | 3 | #47, #48, #84, #140 |
| `sk-def-sfb-change-of-scalars` | definition | Restriction, extension and coextension of scalars | 12 | #163 |
| `sk-def-sfb-coefficient-change` | definition | Change of condensed coefficients | 5 |  |
| `sk-def-sfb-coefficient-morphisms` | definition | The canonical coefficient morphisms $\alpha_f$, $\eta_f$ | 5 | #81 |
| `sk-def-sfb-condensed-ring` | definition | Condensed coefficient rings $\underline T$ | 6 | #38, #44 |
| `sk-def-sfb-dc-lower-shriek` | definition | $Rf_!$ on $D_{\mathrm{cons}}$: assembled from $i_!$ and $Rp_*$ | 2 | #50, #107, #145, #186 |
| `sk-def-sfb-dc-setting` | definition | Setting for $D_{\mathrm{cons}}$: schemes of finite type over a field | 2 | #141 |
| `sk-def-sfb-derived-categories` | definition | Derived categories and derived functors | 6 |  |
| `sk-def-sfb-derived-extension-of-scalars` | definition | Derived extension of scalars | 4 | #46, #163 |
| `sk-def-sfb-derived-tensor-hom` | definition | Derived tensor product and derived internal hom | 10 |  |
| `sk-def-sfb-filtered-two-colimit` | definition | Filtered 2-colimits of categories | 4 | #88, #150 |
| `sk-def-sfb-finite-derived-functors` | definition | Derived pushforward and pullback (finite coefficients) | 5 |  |
| `sk-def-sfb-finite-derived-lower-shriek` | definition | Derived lower shriek and $R\Gamma_c$ (finite coefficients) | 6 |  |
| `sk-def-sfb-finite-lower-shriek` | definition | Extension by zero and lower shriek (finite coefficients) | 8 | #41 |
| `sk-def-sfb-finite-upper-shriek` | definition | Exceptional pullback $Rf^!$ (finite coefficients) | 9 | #51, #114 |
| `sk-def-sfb-module-derived-lower-shriek` | definition | Derived lower shriek of module objects | 6 |  |
| `sk-def-sfb-module-derived-pushpull` | definition | Derived pushforward and pullback of module objects | 2 |  |
| `sk-def-sfb-module-lower-shriek` | definition | Extension by zero and lower shriek of module objects | 6 |  |
| `sk-def-sfb-module-objects` | definition | Module objects and the category $\Mod_{\Lambda_X}$ | 3 |  |
| `sk-def-sfb-module-pushforward-pullback` | definition | Pushforward and pullback of module objects | 6 |  |
| `sk-def-sfb-open-base-change` | definition | Base change for extension by zero on $D_{\mathrm{cons}}$ | 3 |  |
| `sk-def-sfb-pullback-from-point` | definition | Pulling back from the point | 15 | #4, #38 |
| `sk-def-sfb-pullback-from-point-comp` | definition | $f^*\circ p_Y^*\cong p_X^*$ | 2 | #81 |
| `sk-def-sfb-pulled-back-coefficients` | definition | Coefficients pulled back from the point | 2 | #44 |
| `sk-def-sfb-qlbar-condensed` | definition | The condensed ring $\underline{\overline{\mathbf Q}}_\ell$ | 4 |  |
| `sk-def-sfb-rationalization` | definition | Rationalization of a linear triangulated category | 6 | #46 |
| `sk-def-sfb-ring-object` | definition | Ring objects of abelian sheaves | 5 |  |
| `sk-def-sfb-sheaf-tensor` | definition | Tensor product of pro-étale sheaves | 5 |  |
| `sk-def-sfb-shriek-base-change-morphism` | definition | Compact-support base change morphism $\mathrm{Ex}_!^c$ | 2 |  |
| `sk-def-sfb-transport` | definition | Transport of module objects and projection formulas | 9 |  |
| `sk-prop-sfb-finite-extension-compatibility` | proposition | Compatibility for $E\subseteq F$ and $E\subseteq\Qlb$ | 6 | #81, #88, #149, #174 |
| `sk-prop-sfb-module-category` | proposition | Structure of $\Mod_{\mathcal R}(\mathcal C)$ | 14 |  |
| `sk-prop-sfb-module-derived-factorization` | proposition | Factorizations and levelwise descriptions of the derived functors | 8 |  |
| `sk-prop-sfb-module-pullback-exact` | proposition | The pullback of module objects is exact | 2 |  |
| `sk-prop-sfb-qlbar-colimit-point` | proposition | $\underline{\overline{\mathbf Q}}_\ell=\operatorname{colim}_E\underline E$ on the point | 2 |  |
| `sk-thm-sfb-shriek-base-change` | theorem | Base change for the lower shriek on $D_{\mathrm{cons}}$ | 2 | #108, #133 |

### Block 8: Smooth Purity (26)

| Sketch node | Kind | Title | Details | Related tex |
|---|---|---|---:|---|
| `rem-pur-five-moves` | remark | The five moves of the purity proof | 0 |  |
| `rem-pur-status-after-completion` | remark | Dependency order of the smooth-purity proof | 0 |  |
| `sk-def-purity-conv` | definition | Purity conventions and the rank-one datum | 12 | #45, #152, #160 |
| `sk-def-sf-admissible` | definition | Admissibility datum: an explicit hypothesis | 15 | #45 |
| `sk-def-sf-exchanges` | definition | Exchange and projection transformations, typed | 2 | #53 |
| `sk-def-sf-operations` | definition | The six operations: ambient typing | 40 | #42, #48, #50, #107, #114 |
| `sk-def-sf-setting` | definition | Coefficients and sites | 1 | #45 |
| `sk-lem-coprojection` | lemma | Co-projection for a closed immersion | 2 |  |
| `sk-lem-diag-reg` | lemma | The diagonal is a regular immersion | 1 | #161 |
| `sk-lem-geometry` | lemma | Geometry of the deformation of a section | 1 | #160 |
| `sk-lem-regular-smooth` | lemma | A regular immersion of smooth schemes over a perfect field | 1 |  |
| `sk-prop-a1` | proposition | Rank-one orientation: the fundamental class of the zero section | 3 | #136 |
| `sk-prop-a1-inv` | proposition | Weak $\Aaf^1$-invariance | 7 |  |
| `sk-prop-a1-kummer` | proposition | The affine line and $\mathbf G_m$ with $\Lambda(1)$-coefficients | 49 | #40, #117, #136 |
| `sk-prop-sf-cbc` | proposition | Compact-support base change | 93 | #35, #106, #108, #153 |
| `sk-prop-sf-closed-unit` | proposition | Closed-immersion unit | 6 | #41, #86, #137 |
| `sk-prop-sf-comp-proper` | proposition | Proper coincidence | 1 | #186 |
| `sk-prop-sf-finiteness` | proposition | Finiteness and constructibility | 1 | #91, #101, #112 |
| `sk-prop-sf-fullcd-etale-origin` | proposition | $\operatorname{FullCD}$ on the étale-origin class | 11 | #11, #14, #36, #37 |
| `sk-prop-sf-kunneth-ordinary` | proposition | Künneth and the projection formula in ordinary étale cohomology | 131 |  |
| `sk-prop-sf-localization` | proposition | Supported localization | 1 | #86, #131, #137, #146 |
| `sk-prop-sf-pf-reduction` | proposition | Projection formula: compatibility with finite reduction | 5 |  |
| `sk-prop-sf-trace-perfectness` | proposition | Perfectness of compact cohomology and of geometric stalks | 5 |  |
| `sk-rem-split` | remark | What sits where | 0 |  |
| `sk-thm-regular` | theorem | Purity for regular closed immersions | 2 |  |
| `sk-thm-sf-pf-finite` | theorem | Projection formula, finite coefficients | 2 |  |

### Block 9: Six Functors (47)

| Sketch node | Kind | Title | Details | Related tex |
|---|---|---|---:|---|
| `open-sf-ambient-adjoint-input` | remark | Adjunction outside the bounded comparison class | 0 |  |
| `rem-ptr-weil-ambient-exceptional-adjoint-13` | remark | Pointer to the properties of [def-weil-ambient-exceptional-adjoint] | 0 |  |
| `rem-ptr-weil-exceptional-inverse-image-6` | remark | Pointer to the properties of the exceptional inverse image | 0 |  |
| `rem-sf-cech-truncation-obstruction` | remark | The Čech complex of a single weakly contractible covering: what its truncation is missing, and what does not supply it | 0 | #21 |
| `rem-sf-comp-scope` | remark | Scope of the coherence | 0 |  |
| `rem-sf-continuity-obstruction` | remark | What the recorded proof of the comparison theorem uses, and why it does not extend to arbitrary sheaves | 0 | #37 |
| `rem-sf-dualizing-ctf-hypotheses` | remark | Geometric duality and its coefficient comparisons | 0 |  |
| `rem-sf-feeds` | remark | Where this feeds | 0 |  |
| `rem-sf-fullcd-counterexample` | remark | The counterexample: a pro-étale base change whose comparison direct image has infinite cohomological dimension | 0 |  |
| `rem-sf-fullcd-counterexample-locus` | remark | Where the counterexample lives, and which restricted statements survive it | 0 |  |
| `rem-sf-fullcd-general-form` | remark | The general form of $\operatorname{FullCD}$, and the form the blueprint uses | 0 |  |
| `rem-sf-fullcd-reduction` | remark | What $\operatorname{FullCD}$ supplies, and what would discharge it | 0 |  |
| `rem-sf-ledger` | remark | What this chapter settles, and what remains | 0 |  |
| `rem-sf-preservation-class-residue` | remark | Constructible completion and the ambient boundary | 0 |  |
| `rem-sf-typing` | remark | Typing table: ambient definition, small-category theorem | 0 |  |
| `rem-sf-typing-rule` | remark | The typing rule of this section | 0 |  |
| `rem-weil-admissibility-split` | remark | Existence, preservation and geometric duality are separate | 0 |  |
| `sk-def-sf-categories` | definition | Ambient categories and small subcategories | 1 | #47 |
| `sk-def-sf-kv-maps` | definition | The product comparison maps | 1 |  |
| `sk-def-sf-orientation` | definition | Orientation: an interface record | 3 | #161 |
| `sk-lem-sf-ctf-generation` | lemma | Finite/open generation of $\Dctf$ | 2 | #82, #84, #109 |
| `sk-lem-sf-kunneth-star` | lemma | Ordinary Künneth with an identity factor | 1 |  |
| `sk-lem-sf-open-ctf` | lemma | Extension by zero preserves the finite-Tor constructible category | 1 | #104, #144 |
| `sk-lem-sf-twist-interchange` | lemma | Internal Hom with an invertible twist | 1 |  |
| `sk-prop-sf-biduality-general` | proposition | General Verdier biduality | 37 | #171 |
| `sk-prop-sf-dualizable-biduality` | proposition | Biduality of a perfect complex | 2 |  |
| `sk-prop-sf-pf-coherence` | proposition | Coherence of the projection formula | 1 |  |
| `sk-rem-sf-comp-scope` | remark | Scope of the coherence | 0 |  |
| `sk-rem-sf-feeds` | remark | Where this feeds | 0 |  |
| `sk-rem-sf-fullcd-scope` | remark | What this does and does not discharge | 0 |  |
| `sk-rem-sf-kv-formal` | proposition | What is formal and what is not | 2 |  |
| `sk-rem-sf-ledger` | remark | Ledger: what is unconditional, what is conditional, what is open | 0 |  |
| `sk-rem-sf-pf-done` | theorem | The interface is discharged | 9 |  |
| `sk-rem-sf-typing` | remark | Typing table: ambient definition, small-category theorem | 0 |  |
| `sk-rem-sf-typing-rule` | remark | The typing rule of this section | 0 |  |
| `sk-thm-sf-direct-image-tor-amplitude` | theorem | Direct image with finite Tor amplitude | 1 | #112, #128 |
| `sk-thm-sf-dual-perfect` | theorem | The dual of a perfect complex | 1 |  |
| `sk-thm-sf-global-duality` | theorem | Global Verdier duality | 2 |  |
| `sk-thm-sf-hom-ctf` | theorem | Internal Hom with finite Tor amplitude | 5 | #130 |
| `sk-thm-sf-identification` | theorem | The derived Poincaré pairing is the duality isomorphism | 4 |  |
| `sk-thm-sf-internal-hom-pullback` | theorem | Internal Hom versus pullback for a site-perfect first variable | 1 |  |
| `sk-thm-sf-kunneth-relative` | theorem | Relative product theorem | 2 |  |
| `sk-thm-sf-kunneth-verdier` | theorem | Künneth–Verdier isomorphism | 4 |  |
| `sk-thm-sf-package` | theorem | The six-operations package | 23 | #50, #148, #151, #181 |
| `sk-thm-sf-pf-proetale` | theorem | Projection formula: the pro-étale realization | 1 |  |
| `sk-thm-sf-tensor-hom` | theorem | Tensor–Hom form of the exchange | 1 |  |
| `sk-thm-sf-verdier-exchange` | theorem | Verdier-duality exchange | 1 |  |
