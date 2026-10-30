# Alignment of the blueprint with `Readable Lecture Notes.tex`

This file records how the blueprint was rebuilt to follow *The Weil Conjectures: Six operations, the
trace formula and Deligne's theorem on weights* (`Readable Lecture Notes.tex`, 26,918 lines). It
replaces the record of the alignments with the earlier `DerivedCategoryAndSixFunctorsChoice_readable.tex`;
that record is in the history of this file. Line numbers below refer to `Readable Lecture Notes.tex`.

## Structure

- **Sections.** The section objects are the headings of the tex, nested as in the tex: the
  introduction, the three parts (*The six operations*, *Duality and the trace formula*, *Weights and
  the Riemann hypothesis*) and the appendices are the top level, and every `\section`, `\subsection` and
  `\subsubsection` is a section inside its parent, one directory each (202 section objects).
  The eighteen blocks of the previous blueprint are gone. Each block's id now names the tex section
  that took its place, so that links and history carry over:

  | Id | Tex section |
  |---|---|
  | `sec-proetale-coefficients` | The pro-étale site and its comparison theorems |
  | `sec-proper-base-change` | Proper base change |
  | `sec-six-functors-basics` | The exceptional inverse image via Brown representability |
  | `sec-six-functors` | The six operations on $D^b_{\mathrm{ctf}}$ |
  | `sec-smooth-base-change` | Smooth base change |
  | `sec-smooth-purity` | Smooth purity |
  | `sec-poincare-duality` | Verdier and Poincaré duality |
  | `sec-trace-formula` | The Grothendieck–Lefschetz trace formula |
  | `sec-purity-real-sheaves` | Purity of real sheaves on curves |
  | `sec-fourier-transform` | The Fourier transform on the affine line |
  | `sec-deligne-laumon-a1` | Deligne's theorem for curves |
  | `sec-deligne-laumon-general` | Deligne's theorem in general |
  | `sec-zeta-weil` | Proof of the Weil conjectures |
  | `sec-nagata-compactification` | Nagata compactification and Chow's lemma |
  | `sec-abelian-varieties` | Abelian varieties and Tate modules |
  | `sec-picard-framework` | Picard schemes and Jacobians |
  | `sec-curve-estimates` | Cohomology of curves with torsion coefficients |
  | `sec-algebraic-groups-lie-algebras` | Algebraic groups and Lie algebras in characteristic zero |

- **Sketch layer.** Every theorem-like environment of the tex (410: theorem, lemma, proposition,
  corollary, definition, convention, remark, example, question) is one sketch node, tagged `sketch`, in the
  section of its heading and in tex order. Its statement is the tex statement, and its proof the tex proof,
  converted to Markdown. A convention is a `definition`; an example and a question are `remark`s, tagged
  `latex:example` and `latex:question`.
- **Text between declarations.** Everything the tex says outside the declarations and their proofs, from
  the opening lines of a part to the paragraph between two lemmas, is a node of kind `hidden` in the
  section where it stands (389 nodes, ids `prose-<section>-<n>`, with `<section>` the tex section number,
  `A`–`F` for the appendices and `P1`–`P3`, `PA` for the parts). The abstract is `prose-00-01` and the
  bibliography `prose-references`. The document sets them in place as bare prose; the graph never draws them.

## Conventions

- **Reused nodes.** 372 tex declarations are stated by a node the blueprint already had. That node
  kept its id, `lean` names, `uses` and detail nodes, and moved with its whole directory into the tex section.
  Its statement, title and proof are now the tex's. A `*Complement.*` or `*General form.*` paragraph that an
  earlier alignment kept because the node's Lean names state it stays after the tex statement (61 nodes).
  Where the tex has no proof, the blueprint's proof is kept.
  A node was matched through the label tables of the earlier alignments (any label of the declaration,
  aliases included), else through a node id ending in one of its labels, else through the text; the
  doubtful cases were checked by hand. Two nodes changed kind with the tex:
  `sk-cor-curve-invariance` (corollary → lemma) and `sk-prop-classical-inputs` (proposition → remark).
- **New nodes.** 38 tex declarations had no counterpart. They are new sketch nodes `sk-<kind>-<label>`,
  without detail nodes (listed below).
- **Proofs.** A proof that follows its statement after some text, or that the tex gives later (`Proof of
  Theorem~\ref{…}`), is a proof of that statement; `sk-thm-existence`, for instance, is proved in §8.
  `sk-thm-curve-package` has two proofs, one in §4 and one in Appendix D.
- **Dependencies.** A tex reference in a statement or proof to another declaration is a `uses` edge of the
  statement or of the proof, added to the edges the node already had; remarks, examples and questions get
  none. Four references would close a cycle among sketch nodes. The tex marks them as pointers, not
  dependencies ("used again in the proof of", "there is therefore no circularity with … below"), and they
  are not edges: `sk-def-ops` → `sk-lem-pd-preservation`, `sk-lem-curve-dense-open` → `sk-thm-curve-package`, `sk-lem-pd-preservation` → `sk-lem-pd-generic-restriction`, `sk-lem-tf-independent-base-change` → `sk-lem-sf-kunneth-star`.
  The sketch-level graph has no cycle.
- **Section arrows.** A section uses a sibling section when a sketch node inside it uses one inside the
  other, in the direction with more such edges. So the top level reads *Duality* → *Six operations* →
  *Appendices* → *Duality*, and *Weights* → all three: Part I needs Appendices A–D, and Appendix E needs Part II.
- **Cross references.** `Theorem~\ref{x}` is `Theorem [id]`, which the site reads as "Theorem 2.3.4" in its
  own numbering; `\S\ref{x}` is `Section [id]`; a reference to a part is its title in quotes; `\eqref{e}` is
  the tex number, "(4.3)", and the display carries `\tag{4.3}`. `\stacks{T}` links the Stacks Project tag
  and `\cite{k}` is the bibliography label in parentheses.
- **Macros.** The tex macros whose `blueprint.toml` definition differs (`\RHom`, `\Mod`, `\Qbar`, `\et`,
  `\proet`, `\Ab`, `\Dctf`) are expanded in the converted text; `\Cone` was added to `blueprint.toml`.
  Every formula of the converted text renders in KaTeX with the project's macros.

## Nodes without a tex declaration

117 sketch nodes of the previous blueprint state no declaration of the tex. They are no longer in the
sketch layer: each moved, with its proof and everything below it, under one tex sketch node, and lost the
`sketch` tag. Nothing in them changed. The host is, in this order: the tex declaration one of whose labels
names the node (a result the tex merged into another), the tex declaration with the same title, the first
tex declaration that uses the node, the last one it uses, and otherwise the tex declaration of its old
block nearest to it.

| Node | Title | Old block | Now under | Why |
|---|---|---|---|---|
| `sk-def-conv` | Scheme and morphism conventions | Nagata Compactification | `sk-def-pe-morphisms` | first use |
| `sk-rem-pe-topos-functoriality-lean` | Coefficients in the formalization | The Pro-étale Site and Coefficients | `sk-def-pe-wlocal` | nearest in old block |
| `sk-cor-pe-wc-sections` | Exact sections on contractible affines | The Pro-étale Site and Coefficients | `sk-cor-pe-sections` | merged by the tex |
| `rem-ptr-weil-exceptional-inverse-image-6` | Pointer to the properties of the exceptional inverse image | Six Functors | `sk-thm-existence` | last dependency |
| `sk-lem-sp-finite-existence` | Local computation of the finite Brown adjoint | Smooth Purity | `sk-thm-existence` | merged by the tex |
| `sk-thm-pbc-curve-input` | Cohomology of curves | Proper Base Change | `sk-thm-curve-package` | merged by the tex |
| `sk-lem-pbc-curve-field-extension` | Extension of a separably closed ground field | Proper Base Change | `sk-cor-curve-invariance` | merged by the tex |
| `sk-the-final-theorem-the-curve-estimate--remark-1` | Remark | Curve Estimates | `sk-cor-curve-invariance` | nearest in old block |
| `sk-the-final-theorem-the-curve-estimate--remark-2` | Remark | Curve Estimates | `sk-cor-curve-invariance` | nearest in old block |
| `sk-rem-pbc-proof-division` | Division of the proof | Proper Base Change | `sk-lem-pbc-p1-injective-fibre` | nearest in old block |
| `sk-cor-pbc-proet-finite` | Classical finite coefficients on the pro-étale site | Proper Base Change | `sk-lem-pbc-finite` | merged by the tex |
| `sk-rem-pbc-p1-inputs` | Inputs of the projective-line proof | Proper Base Change | `sk-lem-pbc-composition-cancellation` | nearest in old block |
| `rem-sf-fullcd-reduction` | What $\operatorname{FullCD}$ supplies, and what would discharge it | Six Functors | `sk-thm-reduction` | merged by the tex |
| `sk-curve-calculations-pbc-for-the-projective-line--remark-1` | Remark | Proper Base Change | `sk-rem-pbc-fibrewise-properness` | nearest in old block |
| `sk-the-final-theorem--remark-1` | Remark | Proper Base Change | `sk-rem-pbc-fibrewise-properness` | nearest in old block |
| `sk-prop-sp-et-proet` | Étale and pro-étale finite coefficients | Smooth Purity | `sk-prop-ctf-finite-comparison` | merged by the tex |
| `sk-def-bc` | The recorded base-change property | Smooth Base Change | `sk-prop-ctf-finite-proper` | first use |
| `rem-ptr-weil-ambient-exceptional-adjoint-13` | Pointer to the properties of [def-weil-ambient-exceptional-adjoint] | Six Functors | `sk-prop-sf-existence` | last dependency |
| `sk-def-smooth` | Smooth and allowed coefficients | Smooth Base Change | `sk-lem-geo-affine-local` | first use |
| `sk-prop-normal-form` | Étale-local normal form and slicing | Smooth Base Change | `sk-prop-cohsm` | first use |
| `sk-def-sf-categories` | Ambient categories and small subcategories | Six Functors | `sk-prop-qlbar-two-colimit` | last dependency |
| `sk-lem-induction` | The induction step in relative dimension one | Smooth Base Change | `sk-thm-smooth-base-change` | first use |
| `sk-prop-input-spreading` | Extension from a split generic Galois cover | Smooth Base Change | `sk-thm-smooth-base-change` | first use |
| `sk-prop-input-torsors` | Torsors and étale $H^1$ | Smooth Base Change | `sk-thm-smooth-base-change` | first use |
| `sk-lem-minimal` | Minimal counterexamples occur over a point | Smooth Base Change | `sk-lem-failure-field` | first use |
| `sk-prop-etale-normal` | Étale covers of a normal scheme with separably closed function field | Smooth Base Change | `sk-thm-vanishing` | first use |
| `rem-seams` | The seams | Smooth Base Change | `sk-thm-sbc-derived` | nearest in old block |
| `sk-rem-rest` | Classical form and the following sections | Smooth Base Change | `sk-thm-sbc-derived` | nearest in old block |
| `sk-rem-seams` | The seams | Smooth Base Change | `sk-thm-sbc-derived` | nearest in old block |
| `sk-rem-picard-relative-scope` | Ground fields and relative representability | Picard Framework | `sk-rem-sbc-scope` | merged by the tex |
| `sk-rem-sf-comp-scope` | Scope of the coherence | Six Functors | `sk-rem-sbc-scope` | merged by the tex |
| `sk-rem-sf-fullcd-scope` | What this does and does not discharge | Six Functors | `sk-rem-sbc-scope` | merged by the tex |
| `sk-def-sp-coefficient-towers` | Coefficient towers | Smooth Purity | `sk-prop-sp-integral-towers` | first use |
| `sk-def-sp-normalized-towers` | Constructible and normalized towers | Smooth Purity | `sk-prop-sp-integral-towers` | first use |
| `sk-lem-sp-field-extension` | Compatibility with finite extensions of $E$ | Smooth Purity | `sk-thm-purity-transport` | first use |
| `sk-lem-diag-reg` | The diagonal is a regular immersion | Smooth Purity | `sk-prop-an` | first use |
| `sk-prop-a1-inv` | Weak $\Aaf^1$-invariance | Smooth Purity | `sk-prop-an` | first use |
| `sk-prop-sf-kunneth-ordinary` | Künneth and the projection formula in ordinary étale cohomology | Smooth Purity | `sk-prop-an` | first use |
| `sk-lem-geometry` | Geometry of the deformation of a section | Smooth Purity | `sk-thm-dnc` | first use |
| `sk-lem-sp-tower-bound` | Direct image preserves constructible towers | Smooth Purity | `sk-prop-sp-tower-geometric` | first use |
| `sk-lem-sp-tower-levels` | Levels of the tower direct image | Smooth Purity | `sk-prop-sp-tower-geometric` | first use |
| `rem-pur-status-after-completion` | Dependency order of the smooth-purity proof | Smooth Purity | `sk-prop-sp-purity-bc` | last dependency |
| `sk-lem-coprojection` | Co-projection for a closed immersion | Smooth Purity | `sk-prop-sp-purity-bc` | first use |
| `sk-def-set` | The fixed setting | Poincaré Duality | `sk-cor-sp-all-coefficients` | last dependency |
| `sk-rem-split` | What sits where | Smooth Purity | `sk-cor-sp-all-coefficients` | nearest in old block |
| `sk-lem-tf-compact-trace` | The complexes whose traces occur | Trace Formula | `sk-lem-finite` | merged by the tex |
| `sk-prop-sf-trace-perfectness` | Perfectness of compact cohomology and of geometric stalks | Smooth Purity | `sk-lem-finite` | first use |
| `sk-thm-sf-package` | The six-operations package | Six Functors | `sk-def-ops` | first use |
| `sk-rem-sf-pf-done` | The interface is discharged | Six Functors | `sk-thm-sf-tensor-hom` | first use |
| `sk-thm-sf-pf-proetale` | Projection formula: the pro-étale realization | Six Functors | `sk-thm-sf-tensor-hom` | first use |
| `rem-sf-dualizing-ctf-hypotheses` | Geometric duality and its coefficient comparisons | Six Functors | `sk-thm-pd-verdier-duality` | last dependency |
| `rem-sf-preservation-class-residue` | Constructible completion and the ambient boundary | Six Functors | `sk-thm-pd-verdier-duality` | last dependency |
| `rem-weil-admissibility-split` | Existence, preservation and geometric duality are separate | Six Functors | `sk-thm-pd-verdier-duality` | last dependency |
| `sk-rem-sf-kv-formal` | What is formal and what is not | Six Functors | `sk-thm-sf-verdier-exchange` | last dependency |
| `sk-def-sf-orientation` | Orientation: an interface record | Six Functors | `sk-thm-sf-identification` | first use |
| `sk-lem-sf-twist-interchange` | Internal Hom with an invertible twist | Six Functors | `sk-thm-sf-identification` | first use |
| `sk-thm-poincare-duality` | Poincaré duality | Poincaré Duality | `sk-thm-sf-identification` | same title |
| `sk-def-perfect` | Perfectness at the point and on $X$ | Poincaré Duality | `sk-thm-derived-duality` | first use |
| `sk-prop-sf-comp-proper` | Proper coincidence | Smooth Purity | `sk-thm-derived-duality` | first use |
| `sk-thm-sf-dual-perfect` | The dual of a perfect complex | Six Functors | `sk-thm-derived-duality` | first use |
| `rem-feeds` | Where this feeds, and what remains | Poincaré Duality | `sk-cor-trace` | nearest in old block |
| `sk-def-pairing-data` | The pairing data | Poincaré Duality | `sk-cor-trace` | first use |
| `sk-def-trace-cup` | Trace and trace–cup pairing | Poincaré Duality | `sk-cor-trace` | first use |
| `sk-rem-feeds` | Where this feeds, and what remains | Poincaré Duality | `sk-cor-trace` | nearest in old block |
| `sk-thm-regular` | Purity for regular closed immersions | Smooth Purity | `sk-cor-trace` | first use |
| `sk-thm-transport` | Duality and change of coefficients | Poincaré Duality | `sk-thm-frobenius` | first use |
| `sk-d-setup` | Coefficients and geometric categories | Trace Formula | `sk-d-trace` | first use |
| `sk-rem-sf-typing` | Typing table: ambient definition, small-category theorem | Six Functors | `sk-lem-sf-kunneth-star` | nearest in old block |
| `sk-rem-sf-typing-rule` | The typing rule of this section | Six Functors | `sk-lem-sf-kunneth-star` | nearest in old block |
| `rem-sf-ledger` | What this chapter settles, and what remains | Six Functors | `sk-thm-sf-kunneth-verdier` | nearest in old block |
| `sk-def-sf-kv-maps` | The product comparison maps | Six Functors | `sk-thm-sf-kunneth-verdier` | first use |
| `sk-prop-sf-closed-unit` | Closed-immersion unit | Smooth Purity | `sk-thm-sf-kunneth-verdier` | first use |
| `sk-prop-sf-dualizable-biduality` | Biduality of a perfect complex | Six Functors | `sk-thm-sf-kunneth-verdier` | first use |
| `sk-prop-sf-localization` | Supported localization | Smooth Purity | `sk-thm-sf-kunneth-verdier` | first use |
| `sk-rem-sf-feeds` | Where this feeds | Six Functors | `sk-thm-sf-kunneth-verdier` | nearest in old block |
| `sk-rem-sf-ledger` | Ledger: what is unconditional, what is conditional, what is open | Six Functors | `sk-thm-sf-kunneth-verdier` | nearest in old block |
| `sk-d-corr` | Correspondences and supported classes | Trace Formula | `sk-d-trace-class` | first use |
| `sk-d-local-term` | Local terms | Trace Formula | `sk-d-trace-class` | merged by the tex |
| `sk-d-pairing` | The supported pairing recipe | Trace Formula | `sk-d-trace-class` | first use |
| `sk-d-six` | The geometric operation package | Trace Formula | `sk-d-trace-class` | first use |
| `sk-thm-sf-internal-hom-pullback` | Internal Hom versus pullback for a site-perfect first variable | Six Functors | `sk-p-pairing` | first use |
| `sk-d-integral` | Borel–Moore sections and integration | Trace Formula | `sk-d-proper-pushforward` | first use |
| `sk-thm-sf-compatibility` | Compatibility of the six operations | Six Functors | `sk-d-proper-pushforward` | first use |
| `sk-thm-sf-kunneth-relative` | Relative product theorem | Six Functors | `sk-p-proper` | first use |
| `sk-d-curve-pieces` | Curve coefficient pieces | Trace Formula | `sk-i-additivity` | first use |
| `sk-d-operator` | Global operators | Trace Formula | `sk-i-additivity` | first use |
| `sk-i-curve-zero` | Frobenius local vanishing | Trace Formula | `sk-i-additivity` | first use |
| `sk-rem-tf-main-dependencies` | Non-lisse coefficients in the local calculation | Trace Formula | `sk-rem-tf-curve-local-proof` | merged by the tex |
| `sk-c-proper-global` | Proper global trace comparison | Trace Formula | `sk-p-frob` | first use |
| `sk-p-local` | Decomposition into local terms | Trace Formula | `sk-p-frob` | first use |
| `sk-d-relative-frob` | The relative Frobenius factorization | Trace Formula | `sk-i-relative-frob` | first use |
| `sk-d-weil-push` | Weil $!$-pushforward | Trace Formula | `sk-i-global-additivity` | first use |
| `sk-d-lines` | The affine and projective lines | Trace Formula | `sk-thm-tf-coefficient-morphism-formula` | first use |
| `sk-i-topology` | Topological invariance | Trace Formula | `sk-thm-tf-coefficient-morphism-formula` | first use |
| `sk-lem-sf-open-ctf` | Extension by zero preserves the finite-Tor constructible category | Six Functors | `sk-thm-tf-coefficient-morphism-formula` | first use |
| `sk-thm-trace-formula` | Finite-ring Grothendieck–Lefschetz formula | Trace Formula | `sk-thm-tf-uniform-formula` | first use |
| `sk-def-frobmod` | Frobenius modules and their trace series | Trace Formula | `sk-prop-logdet` | first use |
| `sk-p-linear-triangular` | Triangularization | Trace Formula | `sk-prop-logdet` | first use |
| `sk-p-trace-coeff` | Finite-level coefficient change | Trace Formula | `sk-thm-trace-transport` | first use |
| `sk-rem-absent` | What is deliberately absent, and why | Fourier Transform | `sk-cor-plancherel` | nearest in old block |
| `sk-rem-layers` | The three layers, and why the order matters | Fourier Transform | `sk-cor-plancherel` | nearest in old block |
| `sk-thm-sbc-karoubian` | Bounded t-structures on the condensed constructible categories | Smooth Base Change | `sk-lem-wft-curve-heart` | first use |
| `sk-lem-wft-l2-middle` | Boundary correction for squared traces | Deligne–Laumon on the Affine Line: Proof Sketch | `sk-p-dl-a1-fourier-weight` | merged by the tex |
| `sk-cor-wft-curve-upper` | The weight bound on a curve | Deligne–Laumon on the Affine Line: Proof Sketch | `sk-thm-wft-curve-middle-upper` | merged by the tex |
| `sk-rationality-the-criterion-and-the-descent--remark-1` | Remark | Zeta Functions and the Weil Conjectures | `sk-thm-weil-final` | nearest in old block |
| `sk-audit-what-is-elementary-in-this-layer-and-what-is-not--remark-1` | Remark | Zeta Functions and the Weil Conjectures | `sk-cor-hasse` | nearest in old block |
| `sk-rem-wweil-disconnected` | Disconnected $X_0$ | Zeta Functions and the Weil Conjectures | `sk-cor-hasse` | nearest in old block |
| `sk-the-five-assembled-theorems--remark-1` | Where the final layer feeds | Zeta Functions and the Weil Conjectures | `sk-cor-hasse` | nearest in old block |
| `sk-prop-sf-pf-coherence` | Coherence of the projection formula | Six Functors | `sk-def-nagata-sketch-data` | last dependency |
| `sk-rem-nagata-density-normalization-lean` | Scope in the formalization | Nagata Compactification | `sk-rem-nagata-base-change` | nearest in old block |
| `rem-sf-fullcd-general-form` | The general form of $\operatorname{FullCD}$, and the form the blueprint uses | Six Functors | `sk-prop-av-isogeny` | last dependency |
| `sk-lem-regular-smooth` | A regular immersion of smooth schemes over a perfect field | Smooth Purity | `sk-thm-picard-rr` | last dependency |
| `rem-sf-cech-truncation-obstruction` | The Čech complex of a single weakly contractible covering: what its truncation is missing, and what does not supply it | Six Functors | `sk-thm-picard-perfect` | last dependency |
| `rem-sf-continuity-obstruction` | What the recorded proof of the comparison theorem uses, and why it does not extend to arbitrary sheaves | Six Functors | `sk-thm-picard-perfect` | last dependency |
| `rem-sf-fullcd-counterexample` | The counterexample: a pro-étale base change whose comparison direct image has infinite cohomological dimension | Six Functors | `sk-thm-picard-perfect` | last dependency |
| `rem-sf-fullcd-counterexample-locus` | Where the counterexample lives, and which restricted statements survive it | Six Functors | `sk-thm-picard-perfect` | last dependency |
| `sk-rem-picard-seams` | The dependencies are one-way: $\mathbf A\Rightarrow\mathbf B$ at four seams | Picard Framework | `sk-prop-jacobian-descent` | nearest in old block |

## Summary

| Tex section | Declarations | Reused | New | Text nodes | Nodes moved in |
|---|---:|---:|---:|---:|---:|
| Introduction | 0 | 0 | 0 | 9 | 0 |
| The pro-étale site and its comparison theorems | 49 | 44 | 5 | 40 | 3 |
| Coefficients and constructible complexes | 14 | 11 | 3 | 20 | 2 |
| Proper base change | 27 | 22 | 5 | 22 | 10 |
| Constructible sheaves and reduction to finite coefficients | 14 | 14 | 0 | 13 | 0 |
| The exceptional inverse image via Brown representability | 24 | 23 | 1 | 21 | 3 |
| Constructibility of $f^!$ | 24 | 24 | 0 | 18 | 2 |
| The six operations on $D^b_{\mathrm{ctf}}$ | 4 | 4 | 0 | 8 | 1 |
| Smooth base change | 12 | 12 | 0 | 13 | 11 |
| Smooth purity | 23 | 21 | 2 | 35 | 13 |
| Verdier and Poincaré duality | 14 | 13 | 1 | 10 | 20 |
| Weil complexes and the Lefschetz–Verdier formula | 17 | 13 | 4 | 14 | 22 |
| The Grothendieck–Lefschetz trace formula | 26 | 23 | 3 | 21 | 12 |
| Weights and Deligne's theorem | 7 | 5 | 2 | 7 | 0 |
| Rank-one sheaves on curves | 8 | 7 | 1 | 4 | 0 |
| Monodromy and determinant weights | 8 | 8 | 0 | 9 | 0 |
| Purity of real sheaves on curves | 17 | 14 | 3 | 11 | 0 |
| The Fourier transform on the affine line | 11 | 10 | 1 | 10 | 3 |
| Deligne's theorem for curves | 11 | 11 | 0 | 6 | 2 |
| Deligne's theorem in general | 12 | 11 | 1 | 9 | 0 |
| Proof of the Weil conjectures | 8 | 6 | 2 | 5 | 4 |
| Nagata compactification and Chow's lemma | 22 | 19 | 3 | 17 | 2 |
| Abelian varieties and Tate modules | 10 | 10 | 0 | 7 | 1 |
| Picard schemes and Jacobians | 13 | 12 | 1 | 14 | 6 |
| Cohomology of curves with torsion coefficients | 11 | 11 | 0 | 13 | 0 |
| Specialization and contracting correspondences | 16 | 16 | 0 | 18 | 0 |
| Algebraic groups and Lie algebras in characteristic zero | 8 | 8 | 0 | 9 | 0 |
| **Total** | **410** | **372** | **38** | **383** | **117** |

The text nodes of the parts, the abstract and the bibliography are outside the sections.

## Tex declaration → sketch node

"Matched by" says how a reused node was found; "new" marks a node created for the declaration.

### The pro-étale site and its comparison theorems

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 716 | Def Ind-étale, pro-étale and weakly étale morphisms | `pe:morphisms` | `sk-def-pe-morphisms` | same label |
| 742 | Prop — | `pe:etale-implications` | `sk-prop-pe-etale-implications` | new |
| 772 | Lem Stability | `pe:weakly-etale-stability` | `sk-lem-pe-weakly-etale-stability` | same label |
| 798 | Def The small pro-étale site | `pe:site` | `sk-def-pe-site` | same label |
| 818 | Prop — | — | `sk-prop-pe-local-site` | new |
| 839 | Prop The topos and its functoriality | `pe:topos-functoriality` | `sk-def-sfb-finite-pushforward-pullback` | same label |
| 882 | Def w-local, w-strictly local and w-contractible rings | `pe:wlocal` | `sk-def-pe-wlocal` | same label |
| 901 | Prop — | — | `sk-prop-local-rings-profinite-components-and-contractible-covers` | new |
| 930 | Prop Gleason's theorem | `pe:stonean` | `sk-prop-pe-stonean` | same label |
| 955 | Prop Splitting ind-étale covers | `pe:wc-rings` | `sk-prop-pe-wc-rings` | same label |
| 984 | Thm Existence of contractible covers | `pe:wc-cover` | `sk-thm-pe-wc-cover` | same label |
| 1030 | Thm Pro-étale refinements of weakly étale maps | `pe:indetale-refinement` | `sk-thm-pe-indetale-refinement` | same label |
| 1081 | Prop Pro-étale affines form a basis | `pe:affine-basis` | `sk-prop-pe-affine-basis` | same label |
| 1100 | Thm Enough affine weakly contractible objects | `pe:weakly-contractible-basis` | `sk-thm-pe-weakly-contractible-basis` | same label |
| 1159 | Def Weak contractibility | `pe:weak-contractible` | `sk-def-pe-weak-contractible` | same label |
| 1182 | Cor Evaluation on weakly contractible objects | `pe:sections` | `sk-cor-pe-sections` | same label |
| 1235 | Rem Evaluation is in general not a point | `pe:evaluation-not-point` | `sk-rem-pe-evaluation-not-point` | same label |
| 1269 | Def Repleteness | `pe:replete-def` | `sk-def-pe-replete` | same label |
| 1276 | Prop Repleteness of the pro-étale topos | `pe:replete` | `sk-prop-pe-replete` | same label |
| 1295 | Prop Exact products | `pe:products` | `sk-prop-pe-products` | same label |
| 1338 | Prop The Milnor sequence | `pe:milnor` | `sk-prop-pe-milnor` | same label |
| 1404 | Prop Left completeness | `pe:left-complete` | `sk-prop-pe-left-complete` | same label |
| 1428 | Prop — | — | `sk-prop-left-completeness-and-hypercovers` | new |
| 1446 | Prop Weakly contractible hypercovers | `pe:hypercover` | `sk-prop-pe-hypercover` | same label |
| 1495 | Cor Continuity of cohomology | `pe:bounded-continuity` | `sk-cor-pe-bounded-continuity` | same label |
| 1549 | Def Classical pro-étale sheaves | `pe:classical-definition` | `sk-def-pe-classical-definition` | same label |
| 1561 | Prop The comparison morphism and its inverse image | `pe:comparison-morphism` | `sk-prop-pe-comparison-morphism` | same label |
| 1605 | Thm Classical sheaves as the essential image | `pe:classical-sheaves` | `sk-thm-pe-classical-sheaves` | same label |
| 1630 | Ex A coefficient sheaf outside the classical part | `pe:nonclassical-example` | `sk-rem-pe-nonclassical-example` | same label |
| 1673 | Lem Acyclicity of pulled-back injectives | `pe:injective-acyclicity` | `sk-lem-pe-injective-acyclicity` | same label |
| 1709 | Thm Bounded-below cohomology comparison | `pe:cohomology-comparison` | `sk-prop-sf-comparison` | same label |
| 1740 | Cor Cohomology of a pro-étale affine | `pe:affine-continuity` | `sk-cor-pe-affine-continuity` | label in the id |
| 1765 | Cor Bounded-below classical complexes | `pe:classical-derived` | `sk-cor-pe-classical-derived` | same label |
| 1835 | Thm Comparison of direct images | `pe:direct-image-comparison` | `sk-thm-pe-direct-image-comparison` | same label |
| 1882 | Prop — | — | `sk-prop-pe-functor-comparison` | new |
| 1947 | Lem Torsors under classical groups | `pe:torsor-comparison` | `sk-lem-pe-torsor-comparison` | same label |
| 1972 | Prop Locally constant sheaves of finite presentation | `pe:finite-local-systems` | `sk-prop-pe-finite-local-systems` | same label |
| 1994 | Thm Comparison for constructible sheaves | `pe:constructible-comparison` | `sk-thm-pe-constructible-comparison` | same label |
| 2024 | Cor Finite Tor amplitude under comparison | `pe:finite-tor-comparison` | `sk-cor-pe-finite-tor-comparison` | same label |
| 2078 | Def Cohomological dimension | `n:def-cd` | `sk-def-cd` | same label |
| 2100 | Lem Cohomological dimension of the base field | `b:lem:base-field-cd` | `sk-lem-base-field-cd` | same label |
| 2112 | Prop Unbounded comparison for finite coefficients | `pe:unbounded-classical` | `sk-prop-pe-unbounded-classical` | same label |
| 2236 | Prop The pro-étale site of a separably closed field | `pe:condensed-point` | `sk-prop-pe-condensed-point` | same label |
| 2278 | Prop Continuous cohomology as pro-étale cohomology | `pe:continuous-cohomology` | `sk-prop-pe-continuous-cohomology` | same label |
| 2295 | Cor Continuous étale cohomology | `pe:continuous-etale` | `sk-cor-pe-continuous-etale` | label in the id |
| 2330 | Ex The first cohomology of a finite field | `pe:finite-field-adic` | `sk-rem-pe-finite-field-adic` | same label |
| 2380 | Prop Extension by zero and restriction to a closed subscheme | `pe:open-closed` | `sk-prop-sf-open-closed-triangle` | same label |
| 2470 | Def Derived adic completeness | `pe:derived-completion` | `sk-def-pe-derived-completion` | same label |
| 2490 | Lem Reduction and derived Nakayama | `pe:derived-nakayama` | `sk-lem-pe-derived-nakayama` | same label |

### Coefficients and constructible complexes

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 2731 | Lem Comparison with completed coefficients | `n:coefficient-comparison` | `sk-prop-sfb-qlbar-colimit-x` | same label |
| 2764 | Cor Finite quotients and their transition maps | `n:coefficient-quotients` | `sk-cor-n-coefficient-quotients` | new |
| 2831 | Def Tate twists | `def:sp-Tate-twist` | `sk-def-sp-tate-twist` | same label |
| 2878 | Prop Inverting $\ell$ on the full derived categories | `n:rationalization-full` | `sk-prop-sfb-rationalization-full` | label in the id |
| 2903 | Prop Inverting $\ell$ | `n:rationalization` | `sk-thm-sfb-rationalization-comparison` | same label |
| 2963 | Def Constructible sheaves | `n:def-constructible` | `sk-def-sfb-constructible` | same label |
| 2995 | Rem — | — | `sk-rem-n-constructible` | new |
| 3054 | Lem Bounds for the finite reductions | `n:integral-finite-levels` | `sk-lem-integral-finite-levels` | label in the id |
| 3109 | Lem Perfect complexes over $\mathcal O_E$ | `n:integral-scalar-towers` | `sk-lem-integral-scalar-towers` | label in the id |
| 3172 | Prop Local structure of integral constructible complexes | `n:integral-local-structure` | `sk-prop-integral-local-structure` | label in the id |
| 3288 | Prop The integral constructibility criterion | `n:integral-criterion` | `sk-prop-integral-criterion` | same label |
| 3371 | Prop — | `n:ctf-equals-bc` | `sk-prop-n-ctf-equals-bc` | new |
| 3413 | Def The localizing subcategory generated by $D^b_{\mathrm{ctf}}(X,\Lambda)$ | — | `sk-def-localizing-closure` | same text |
| 3438 | Thm The exceptional inverse image | `n:existence` | `sk-thm-existence` | same label |

### Proper base change

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 3516 | Question — | — | `sk-q-proper-base-change` | new |
| 3585 | Conv — | `pbc:conventions` | `sk-def-pbc-conventions` | same label |
| 3655 | Def Derived base change map | `pbc:exchange` | `sk-def-exchange` | same label |
| 3697 | Lem Identity and pasting | `pbc:exchange-pasting` | `sk-lem-pbc-exchange-pasting` | same label |
| 3775 | Def Torsion and the PBC property | `pbc:property` | `sk-def-pbc` | same label |
| 3816 | Thm Comparison over a henselian pair in degree zero | `pbc:henselian-h0` | `sk-thm-pbc-henselian-h0` | same label |
| 3841 | Prop Proper base change in degree zero | `pbc:degree-zero` | `sk-prop-pbc-degree-zero` | same label |
| 3921 | Def Injective acyclicity | `pbc:ia` | `sk-def-ia` | same label |
| 3935 | Lem Acyclic resolutions | `pbc:acyclicity` | `sk-thm-acyclicity` | same label |
| 3980 | Thm PBC and injective acyclicity | `pbc:ia-equivalence` | `sk-thm-iff` | same label |
| 4070 | Rem — | — | `sk-rem-henselian-pairs-and-curves` | new |
| 4114 | Thm Cohomology of curves | `pbc:curve-input` | `sk-thm-curve-package` | same label |
| 4157 | Lem Extension of a separably closed ground field | `pbc:curve-field-extension` | `sk-cor-curve-invariance` | same label |
| 4180 | Rem — | — | `sk-rem-henselian-pairs-and-curves-2` | new |
| 4218 | Rem — | — | `sk-rem-restriction-of-injectives-to-the-closed-fibre` | new |
| 4254 | Lem Acyclicity on the closed fibre | `pbc:p1-injective-fibre` | `sk-lem-pbc-p1-injective-fibre` | same label |
| 4324 | Prop Cohomology of $\mathbf P^1$ over a henselian local ring | `pbc:p1-henselian` | `sk-prop-pbc-p1-henselian` | same label |
| 4393 | Prop Proper base change for the projective line | `pbc:p1` | `sk-thm-p1` | same label |
| 4486 | Lem Finite morphisms | `pbc:finite` | `sk-lem-pbc-finite` | same label |
| 4526 | Lem Composition and cancellation | `pbc:composition-cancellation` | `sk-lem-pbc-composition-cancellation` | same label |
| 4604 | Lem A finite cover of projective space | `pbc:symmetric-product` | `sk-lem-pbc-symmetric-product` | same label |
| 4663 | Prop Proper base change on the étale site | `pbc:reduction` | `sk-thm-reduction` | same label |
| 4725 | Thm Proper base change on classical pro-étale complexes | `pbc:torsion-theorem` | `sk-thm-properbasechange` | same label |
| 4783 | Cor Cohomology of geometric fibres | `pbc:torsion-stalk` | `sk-cor-pbc-torsion-stalk` | same label |
| 4848 | Prop Proper base change for complete integral complexes | `pbc:complete` | `sk-prop-pbc-complete` | same label |
| 4925 | Rem — | `pbc:complete-ordinary` | `sk-rem-pbc-complete-ordinary` | new |
| 4956 | Ex Fibrewise computation and the need for properness | — | `sk-rem-pbc-fibrewise-properness` | checked by hand |

### Constructible sheaves and reduction to finite coefficients

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 5070 | Lem Inverse image of the coefficient sheaves | `b:lem:coefficient-pullback` | `sk-prop-sfb-cartesian-coefficients` | same label |
| 5144 | Lem Lattices in lisse $E$-sheaves | `b:lem:lattice-atlas` | `sk-lem-lattice-atlas` | label in the id |
| 5194 | Lem Descent of lisse $\overline{\mathbf Q}_\ell$-sheaves to a finite extension $E$ | `b:lem:lisse-finite-descent` | `sk-lem-lisse-finite-descent` | label in the id |
| 5216 | Lem Constructible sheaves | `b:lem:coefficient-heart` | `sk-lem-coefficient-heart` | same label |
| 5303 | Ex A running example | `b:ex:running` | `sk-rem-running` | same label |
| 5328 | Cor — | `b:lem:coefficient-heart-b` | `sk-cor-coefficient-heart-ii` | same label |
| 5389 | Lem Sections with support in a closed subscheme | `b:lem:formal-closed-support` | `sk-lem-formal-closed-support` | same label |
| 5478 | Lem Continuity of Ext out of a constructible complex | `b:lem:constructible-ext-continuity` | `sk-lem-constructible-ext-continuity` | same label |
| 5562 | Lem Descent to a finite coefficient field | `b:lem:coefficient-finite-descent` | `sk-thm-sfb-qlbar-two-colimit` | same label |
| 5654 | Lem Lattices after a finite stratification | `b:lem:stratified-lattice` | `sk-lem-stratified-lattice` | same label |
| 5704 | Lem Geometric coverings of a normal scheme | `wrp:normal-geometric-cover` | `sk-lem-wrp-normal-geometric-cover` | label in the id |
| 5766 | Prop Lattices and representations on a normal scheme | `wrp:normal-lattice-representation` | `sk-p-real-integral` | same text |
| 5910 | Lem Integral models | `b:lem:integral-models` | `sk-lem-integral-models` | same label |
| 6030 | Prop Proper direct image of constructible complexes | `b:prop:proper-coefficients` | `sk-thm-sfb-proper-base-change` | same label |

### The exceptional inverse image via Brown representability

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 6272 | Lem Limits and sections with support | `b:lem:formal-closed-support-b` | `sk-lem-formal-closed-support-ii` | same label |
| 6295 | Lem Uniform Ext bound | `b:lem:uniform-constructible-ext` | `sk-lem-uniform-constructible-ext` | same label |
| 6442 | Prop Ind-constructible sheaves | `b:prop:ind-heart` | `sk-prop-ind-heart` | same label |
| 6549 | Cor — | `b:prop:ind-heart-b` | `sk-cor-ind-heart-ii` | same label |
| 6571 | Cor — | `b:cor:ambient-ind-derived` | `sk-cor-ambient-ind-derived` | same label |
| 6605 | Lem Reduction to finitely many degrees | `b:lem:finite-window` | `sk-lem-finite-window` | same label |
| 6670 | Thm Compactness with rational coefficients | `b:thm:constructible-compactness` | `sk-thm-constructible-compactness` | same label |
| 6768 | Lem Cohomology commutes with filtered colimits | `b:lem:proper-heart-continuity` | `sk-lem-proper-heart-continuity` | label in the id |
| 6805 | Lem A uniform bound for proper direct image | `b:lem:proper-heart-bound` | `sk-lem-proper-heart-bound` | same label |
| 6902 | Lem Proper direct image of unbounded complexes | `b:lem:proper-unbounded-window` | `sk-lem-proper-unbounded-window` | same label |
| 7023 | Prop Proper direct image and extension by zero | `b:prop:proper-image-localizing` | `sk-prop-proper-image-localizing` | same label |
| 7062 | Lem Checking isomorphisms on constructible complexes | `b:lem:localizing-comparison` | `sk-lem-sf-determination` | same label |
| 7092 | Prop Proper base change on the localizing categories | `b:prop:proper-base-change-unbounded` | `sk-prop-proper-base-change-unbounded` | same label |
| 7123 | Rem Compactifications | — | `sk-rem-compactifications` | same text |
| 7144 | Prop Construction and independence of $Rf_!$ | `b:prop:lower-exceptional-image` | `sk-prop-sf-comp-coherence` | same label |
| 7217 | Prop Composition and base change for $Rf_!$ | `b:prop:lower-composition` | `sk-thm-sf-comp-composition` | same label |
| 7324 | Prop Forgetting supports and composition | `b:prop:forget-supports-composition` | `sk-prop-b-prop-forget-supports-composition` | new |
| 7390 | Lem Flat models and generators | `ctf:finite-models` | `sk-lem-sf-flat-model` | same label |
| 7432 | Prop Compactness for finite coefficients | `ctf:finite-compact` | `sk-prop-ctf-finite-compact` | same label |
| 7490 | Prop Comparison with the étale derived category | `ctf:finite-comparison` | `sk-prop-ctf-finite-comparison` | same label |
| 7530 | Prop Proper direct image for finite coefficients | `ctf:finite-proper` | `sk-prop-ctf-finite-proper` | same label |
| 7591 | Lem Hypotheses of Brown representability | `b:lem:brown-hypotheses` | `sk-lem-brown-hypotheses` | same label |
| 7624 | Thm Existence of the exceptional inverse image | `b:thm:brown-adjoint` | `sk-prop-sf-existence` | same label |
| 7687 | Prop Composition, open restriction and compactifications for $f^!$ | `b:prop:composition-locality` | `sk-lem-sf-mate` | same label |

### Constructibility of $f^!$

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 7940 | Rem Results from the étale theory | `b:rem:classical-inputs` | `sk-prop-classical-inputs` | same text |
| 7998 | Lem The cycle class of a Cartier divisor | `b:lem:geo-cartier` | `sk-lem-geo-cartier` | same label |
| 8065 | Lem Cohomology of the projective line and the trace | `b:lem:geo-p1-cohomology` | `sk-lem-geo-p1-cohomology` | same label |
| 8132 | Ex Compact supports on the running example | — | `sk-rem-compact-supports-running-example` | same text |
| 8158 | Prop The adjunction for the projective line | `b:prop:geo-p1-adjunction` | `sk-prop-geo-p1-adjunction` | same label |
| 8349 | Lem Affine space and étale localization | `b:lem:geo-affine-local` | `sk-lem-geo-affine-local` | same label |
| 8409 | Prop The exceptional inverse image of a smooth morphism | `b:prop:geo-smooth-tensor` | `sk-prop-cohsm` | same label |
| 8530 | Lem Smooth morphisms and locally constant sheaves | `b:lem:geo-smooth-generic` | `sk-lem-geo-smooth-generic` | same label |
| 8644 | Lem Detection by a proper direct image | `b:lem:geo-finite-boundary` | `sk-lem-geo-finite-boundary` | same label |
| 8703 | Lem Coordinate projections | `b:lem:geo-coordinates` | `sk-lem-geo-coordinates` | same label |
| 8787 | Thm Generic constructibility and base change for $Rj_*$ | `b:thm:geo-generic-open` | `sk-thm-geo-generic-open` | same label |
| 8973 | Cor Open direct image over a field | `b:cor:geo-open-finiteness` | `sk-cor-geo-open-finiteness` | same label |
| 9034 | Prop Open direct image preserves finite Tor amplitude | `ctf:finite-open` | `sk-cor-sf-direct-image-ctf` | same label |
| 9094 | Thm $f^!$ with finite coefficients | `ctf:finite-restriction` | `sk-prop-sf-rf-shriek-preservation` | same label |
| 9175 | Prop Direct image along an open immersion | `b:prop:open-coefficients` | `sk-prop-open-coefficients` | same label |
| 9209 | Prop The $\ell$-adic cycle class of the diagonal | `b:prop:diagonal-tower` | `sk-prop-diagonal-tower` | same label |
| 9247 | Prop Projection formula with rational coefficients | `b:prop:pf-bc-generated` | `sk-thm-sf-pf-field` | same label |
| 9264 | Prop The projective line, rational coefficients | `b:prop:p1-adjunction-rational` | `sk-prop-p1-adjunction-rational` | same label |
| 9304 | Ex — | `b:ex:closed-support` | `sk-rem-closed-support` | same label |
| 9326 | Lem Structure of integral constructible complexes | `i:integral-heart` | `sk-lem-int-integral-heart` | same label |
| 9354 | Lem Inverse image and tensor product | `i:tensor` | `sk-lem-int-tensor` | same label |
| 9368 | Prop Compactness and proper direct image | `i:compactness` | `sk-prop-int-compactness` | same label |
| 9394 | Lem Projection formula with integral coefficients | `i:open-pf` | `sk-thm-sf-pf-adic` | same label |
| 9407 | Thm $f^!$ with $\ell$-adic coefficients | `i:restriction` | `sk-thm-restriction` | same label |

### The six operations on $D^b_{\mathrm{ctf}}$

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 9565 | Prop The six operations on $D^b_{\mathrm{ctf}}$ | `n:six-small` | `sk-thm-sf-ctf-stability` | same label |
| 9663 | Prop The six operations and change of coefficients | `n:scalar-six` | `sk-prop-scalar-six` | same label |
| 9822 | Prop $D^b_{\mathrm{ctf}}(X,\overline{\mathbf Q}_\ell)$ as a $2$-colimit | `n:two-colimit` | `sk-prop-qlbar-two-colimit` | label in the id |
| 9878 | Prop Isomorphisms reduce to finite coefficients | `n:reduction-to-finite` | `sk-prop-reduction-to-finite` | label in the id |

### Smooth base change

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 10071 | Lem Naturality, pasting and comparison | `sbc:exchange-compatibility` | `sk-lem-sbc-exchange-compatibility` | same label |
| 10108 | Thm Smooth base change for classical torsion sheaves | `app:sbc-geometric-theorem` | `sk-thm-smooth-base-change` | same label |
| 10175 | Lem The degree-zero calculation | `app:sbc-degree-zero` | `sk-prop-deg0` | same label |
| 10273 | Lem Injectivity of the base change map in degree $q$ | `app:sbc-injectivity` | `sk-prop-injectivity` | same label |
| 10312 | Lem Reduction to a field | `app:sbc-minimal-failure` | `sk-lem-failure-field` | same label |
| 10358 | Lem Integral changes of source and base | `app:sbc-integral-tests` | `sk-lem-sbc-integral-tests` | same label |
| 10386 | Lem Reduction to a curve over a normal base | `app:sbc-universal-datum` | `sk-lem-universal-datum` | same label |
| 10466 | Prop Base change to a larger algebraically closed field | `app:sbc-curve-test` | `sk-thm-vanishing` | same label |
| 10582 | Thm Smooth base change for classical torsion complexes | `sbc:torsion` | `sk-thm-sbc-derived` | same label |
| 10622 | Rem The invertibility and boundedness hypotheses | — | `sk-rem-sbc-hypotheses` | checked by hand |
| 10651 | Thm Smooth base change for all admissible coefficients | `sbc:uniform` | `sk-thm-sbc-coefficients` | same label |
| 10692 | Rem Smooth base change, proper base change and base change for $f^!$ | `sbc:scope` | `sk-rem-sbc-scope` | same label |

### Smooth purity

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 10906 | Prop — | `prop:sp-integral-towers` | `sk-prop-sp-integral-towers` | label in the id |
| 10947 | Thm Smooth purity for all admissible coefficients | `thm:sp-integral` | `sk-thm-purity-transport` | same label |
| 10987 | Def Relative dualizing complex | `def:sp-dualizing` | `sk-def-sp-dualizing` | same label |
| 11206 | Def Representing objects | `def:sp-representing-pair` | `sk-def-sp-representing-pair` | same label |
| 11279 | Prop Purity for vector bundles | `prop:sp-vector` | `sk-prop-an` | same label |
| 11459 | Lem A section and its normal bundle | `lem:sp-dnc` | `sk-thm-dnc` | same label |
| 11549 | Lem Naturality under base change and étale maps | `lem:sp-dnc-naturality` | `sk-lem-lem-sp-dnc-naturality` | new |
| 11665 | Prop The relative dualizing complex | `prop:sp-orientation` | `sk-prop-sp-orientation` | same label |
| 11761 | Prop Smooth purity with finite coefficients | `prop:sp-finite` | `sk-thm-smooth-purity` | same label |
| 11829 | Def — | `def:sp-scalar-extension` | `sk-def-sp-scalar-extension` | same label |
| 11836 | Lem — | `lem:sp-reduction` | `sk-lem-sp-reduction` | same label |
| 11899 | Lem — | `lem:sp-tower-adjunction-foundation` | `sk-lem-sp-tower` | same text |
| 11935 | Prop — | `prop:sp-tower-geometric` | `sk-prop-sp-tower-geometric` | same label |
| 11994 | Prop — | `prop:sp-integral-adjunction` | `sk-prop-sp-integral-adjunction` | same label |
| 12034 | Prop — | `prop:sp-unique-adjoint` | `sk-prop-sp-unique-adjoint` | same label |
| 12065 | Prop — | `cor:sp-rational` | `sk-prop-sp-rational` | same label |
| 12097 | Thm — | `thm:sp-qbar` | `sk-thm-sp-qbar` | same label |
| 12245 | Prop Compatibility of purity with base change | `prop:sp-purity-bc` | `sk-prop-sp-purity-bc` | same label |
| 12326 | Prop Compatibility of purity with composition | `prop:sp-composition` | `sk-prop-sp-composition` | same label |
| 12407 | Def Trace map | `def:sp-trace` | `sk-def-sp-trace` | same label |
| 12418 | Rem — | — | `sk-rem-the-trace-map` | new |
| 12430 | Prop Transitivity of the trace map | `prop:sp-trace-composition` | `sk-prop-sp-trace-composition` | same label |
| 12481 | Cor The dualizing complex of a smooth scheme | `cor:sp-all-coefficients` | `sk-cor-sp-all-coefficients` | same label |

### Verdier and Poincaré duality

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 12648 | Lem Perfect complexes at the geometric point | `pd:point-perfect` | `sk-lem-finite` | same label |
| 12687 | Def Verdier dual and evaluation | `pd:definition` | `sk-def-ops` | same label |
| 12710 | Lem Internal adjunction and two exchange formulas | `pd:formal-exchange` | `sk-thm-sf-tensor-hom` | same label |
| 12844 | Lem Verdier duality preserves constructibility | `pd:preservation` | `sk-lem-pd-preservation` | same label |
| 12882 | Lem Restriction to a geometric generic fibre | `pd:generic-restriction` | `sk-lem-pd-generic-restriction` | same label |
| 12998 | Thm Verdier biduality | `pd:verdier-duality` | `sk-thm-pd-verdier-duality` | same label |
| 13079 | Cor Verdier exchange formulas | `pd:verdier-exchanges` | `sk-thm-sf-verdier-exchange` | same label |
| 13132 | Thm Global Verdier duality | `pd:global-duality` | `sk-thm-sf-global-duality` | same label |
| 13170 | Def Perfect pairing | `pd:perfect-pairing` | `sk-def-pairing` | same label |
| 13185 | Thm Poincaré duality | `pd:smooth-duality` | `sk-thm-sf-identification` | same label |
| 13248 | Cor Degreewise duality over fields | `pd:degreewise` | `sk-thm-derived-duality` | same label |
| 13274 | Rem Duality on cohomology groups over $\mathcal O_E$ and finite rings | `pd:integral-corrections` | `sk-rem-pd-integral-corrections` | same label |
| 13329 | Thm The trace isomorphism in top degree | `pd:top-trace` | `sk-cor-trace` | same label |
| 13401 | Cor The cup product pairing | `pd:cup-product` | `sk-cor-pd-cup-product` | new |

### Weil complexes and the Lefschetz–Verdier formula

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 13586 | Def Weil structure | `def:sp-Weil-structure` | `sk-def-sf-weil-complexes` | same label |
| 13696 | Prop Purity and trace commute with Frobenius | `prop:sp-frobenius-purity` | `sk-prop-prop-sp-frobenius-purity` | new |
| 13753 | Thm Poincaré duality and Frobenius | `pd:frobenius` | `sk-thm-frobenius` | same label |
| 13813 | Ex The running example: duality | `ex:run-duality` | `sk-ex-ex-run-duality` | new |
| 13857 | Def Categorical trace | `tf:categorical-trace` | `sk-d-trace` | same label |
| 13872 | Prop Properties of the trace | `tf:trace-laws` | `sk-p-trace` | same label |
| 13911 | Rem — | `tf:coherent-additivity` | `sk-rem-tf-coherent-additivity` | same label |
| 13920 | Ex A trace not determined by cohomology | `tf:trace-example` | `sk-ex-tf-trace-example` | new |
| 14038 | Lem Base change along a product projection | `tf:independent-base-change` | `sk-lem-tf-independent-base-change` | same label |
| 14083 | Prop Ordinary external Künneth | `tf:ordinary-external-kunneth` | `sk-lem-sf-kunneth-star` | same label |
| 14270 | Prop Exceptional external Künneth | `tf:exceptional-external-kunneth` | `sk-prop-tf-exceptional-external-kunneth` | new |
| 14331 | Lem External duality and the trace morphism | `tf:external-duality` | `sk-thm-sf-kunneth-verdier` | same label |
| 14429 | Def Trace class and local terms | `tf:local-term` | `sk-d-trace-class` | same label |
| 14454 | Lem Local terms on the point | `tf:point-normalization` | `sk-p-pairing` | same label |
| 14507 | Def Pushforward of a correspondence | `tf:pushforward-def` | `sk-d-proper-pushforward` | same label |
| 14531 | Thm Proper pushforward and Lefschetz–Verdier | `tf:proper-localization` | `sk-p-proper` | same label |
| 14657 | Prop Additivity of trace classes | `tf:trace-class-additivity` | `sk-i-additivity` | same label |

### The Grothendieck–Lefschetz trace formula

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 14846 | Question — | — | `sk-q-trace-formula` | new |
| 14969 | Def Frobenius correspondences and their operators | `tf:weildatum` | `sk-d-weil` | same label |
| 15002 | Lem Scheme Frobenius and geometric Frobenius | `tf:frobenius-convention` | `sk-lem-tf-frobenius-convention` | same label |
| 15088 | Lem The Frobenius fixed scheme | `tf:fixed-points` | `sk-lem-tf-fixed-points` | same label |
| 15114 | Rem Outline of the local computation | `tf:curve-local-proof` | `sk-rem-tf-curve-local-proof` | same label |
| 15162 | Lem The local term as a restriction map | `tf:curve-supported-pairing` | `sk-lem-tf-curve-supported-pairing` | same label |
| 15231 | Lem Vanishing of the local term at a zero stalk | `tf:curve-restriction-zero` | `sk-lem-tf-curve-restriction-zero` | same label |
| 15407 | Lem Cohomology near two transverse divisors | `tf:transverse-boundary` | `sk-lem-tf-transverse-boundary` | same label |
| 15530 | Lem Restriction to a punctured curve | `tf:punctured-restriction` | `sk-lem-tf-punctured-restriction` | same label |
| 15552 | Lem Vanishing of restrictions after blowing up | `tf:blowup-restriction` | `sk-lem-tf-blowup-restriction` | same label |
| 15602 | Prop The Frobenius local term on a curve | `tf:frobenius-local-term` | `sk-p-frob` | same label |
| 15657 | Rem — | `tf:locality-warning` | `sk-rem-tf-locality-warning` | same label |
| 15689 | Lem Comparison via relative Frobenius | `tf:relative-frobenius` | `sk-i-relative-frob` | same label |
| 15788 | Lem Additivity for an open subscheme and its complement | `tf:localization-additivity` | `sk-i-global-additivity` | same label |
| 15850 | Thm Trace formula for a Frobenius correspondence | `tf:coefficient-morphism-formula` | `sk-thm-tf-coefficient-morphism-formula` | same label |
| 15976 | Prop Integral trace formula | `tf:transport-integral` | `sk-prop-tf-transport-integral` | same label |
| 16034 | Lem Integral models for rational Frobenius correspondences | `tf:rational-model` | `sk-lem-tf-rational-model` | same label |
| 16085 | Rem Integral Frobenius correspondences need not be invertible | — | `sk-rem-tf-weil-lattices` | checked by hand |
| 16103 | Thm Grothendieck–Lefschetz trace formula | `tf:uniform-formula` | `sk-thm-tf-uniform-formula` | same label |
| 16202 | Cor Trace functions and direct image with compact support | `tf:trace-function-pushforward` | `sk-cor-tf-trace-function-pushforward` | new |
| 16261 | Lem Logarithm of a determinant | `tf:determinant-formula` | `sk-prop-logdet` | same label |
| 16303 | Thm The trace formula as an Euler product | `tf:euler-product` | `sk-thm-trace-transport` | same label |
| 16383 | Cor Point counting and the zeta function | `tf:point-counting` | `sk-cor-tf-point-counting` | same label |
| 16447 | Ex The running example: the trace formula | `ex:run-trace` | `sk-ex-ex-run-trace` | new |
| 16472 | Cor Functional equation | `tf:functional-equation` | `sk-cor-tf-functional-equation` | label in the id |
| 16521 | Rem The sign of the functional equation and weights | — | `sk-rem-tf-rationality` | same text |

### Weights and Deligne's theorem

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 16709 | Conv — | `wrp:weil` | `sk-d-real-weil` | label in the id |
| 16756 | Rem — | — | `sk-rem-wdef-weights` | new |
| 16790 | Def — | `wrp:weights` | `sk-d-real-weights` | checked by hand |
| 16814 | Rem — | — | `sk-rem-wdef-weights-2` | new |
| 16846 | Lem Filtrations and spectra | `walg:filtration-spectra` | `sk-p-linear-filtration` | same text |
| 16871 | Prop Weights under the usual operations | `wrp:operations` | `sk-r-real-linear` | same text |
| 16930 | Thm Weights of $Rf_!$ | `wgen:derived-direct-image` | `sk-cor-dl-general-complex` | same text |

### Rank-one sheaves on curves

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 17080 | Lem A proper smooth model | `wrp:compactification` | `sk-i-real-compactification` | label in the id |
| 17105 | Prop Kummer, duality and the integral Tate module | `wrp:kummer-tate` | `sk-d-real-jacobian` | same text |
| 17177 | Prop No fixed class in degree one | `wrp:h1-no-fixed` | `sk-prop-wrp-h1-no-fixed` | label in the id |
| 17268 | Lem Invariant additive characters | `wrp:additive` | `sk-lem-wrp-additive` | label in the id |
| 17297 | Thm Rank-one sheaves have finite geometric monodromy | `wrp:rankone-finite` | `sk-p-real-rankone` | same text |
| 17340 | Cor Rank-one weights | `wrp:rankone-pure` | `sk-cor-wrp-rankone-pure` | label in the id |
| 17372 | Cor Determinant weights | `wrp:determinant` | `sk-d-real-detweights` | same text |
| 17403 | Rem — | — | `sk-rem-logarithms-and-rank-one-purity` | new |

### Monodromy and determinant weights

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 17523 | Lem Restriction to a normal subgroup | `walg:normal-restriction` | `sk-i-restriction` | same text |
| 17542 | Lem Tensor and exterior powers of filtered representations | `walg:filtered-transfer` | `sk-r-linear-library` | same text |
| 17627 | Lem — | — | `sk-lem-walg-normal-commutator` | same text |
| 17647 | Lem The identity component | `walg:identity-product` | `sk-p-product` | same text |
| 17705 | Prop A central element of the arithmetic monodromy group | `walg:central-representative` | `sk-p-central` | same text |
| 17766 | Def Determinant weight | `walg:determinant-weight` | `sk-d-weights` | checked by hand |
| 17781 | Lem Determinant weight from a central scalar | `walg:scalar-readout` | `sk-p-readout` | same text |
| 17806 | Prop Determinant weights of tensor operations | `walg:determinant-weights` | `sk-prop-walg-determinant-weights` | label in the id |

### Purity of real sheaves on curves

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 17963 | Lem Degree zero and top cohomology | `wrp:hc2` | `sk-lem-wrp-hc2` | label in the id |
| 18038 | Def Real sheaves | `wrp:real-definition` | `sk-def-wrp-real-definition` | label in the id |
| 18047 | Rem — | — | `sk-rem-top-cohomology-and-positive-euler-products` | new |
| 18059 | Lem Positivity and convergence | `wrp:positive-euler` | `sk-lem-wrp-positive-euler` | label in the id |
| 18096 | Prop A bound by the largest determinant weight | `wrp:rankin-bound` | `sk-p-real-rankin` | same text |
| 18191 | Thm Purity of real sheaves on curves | `wrp:real-purity` | `sk-p-real-purity` | label in the id |
| 18297 | Lem The boundary stalk | `wrp:boundary-stalk` | `sk-i-real-boundary` | checked by hand |
| 18340 | Lem A point-count bound | `wrp:point-count` | `sk-lem-wrp-point-count` | label in the id |
| 18362 | Prop Weights of $j_*$ at the boundary points | `wrp:boundary-bound` | `sk-p-real-semi` | same text |
| 18453 | Cor An unramified boundary point | `wrp:unramified-purity` | `sk-cor-wrp-unramified-purity` | label in the id |
| 18497 | Prop Twisting to weight zero and adding the dual | `wrp:real-envelope` | `sk-prop-wrp-real-envelope` | label in the id |
| 18530 | Lem — | `wrp:twisted-envelope` | `sk-lem-wrp-twisted-envelope` | new |
| 18568 | Def Growth of squared traces | `wrp:l2-definition` | `sk-def-wrp-l2-definition` | label in the id |
| 18587 | Rem — | — | `sk-rem-weights-and-the-growth-of-squared-traces` | new |
| 18609 | Lem Growth and finite corrections | `wrp:l2-growth` | `sk-lem-wrp-l2-growth` | label in the id |
| 18655 | Thm Weights and sums of squared traces | `wrp:l2-dictionary` | `sk-thm-wrp-l2-dictionary` | label in the id |
| 18719 | Cor Sums of squared traces of $j_!$ and $j_*$ | `wrp:l2-real-blocks` | `sk-cor-wrp-l2-real-blocks` | label in the id |

### The Fourier transform on the affine line

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 18849 | Lem The Artin–Schreier character sheaf | `wft:character-sheaf` | `sk-lem-as-properties` | same text |
| 18908 | Ex A Gauss sum over $\mathbf F_3$ | `ex:gauss-sum` | `sk-ex-ex-gauss-sum` | new |
| 18935 | Lem Künneth formula for compact supports | `wft:compact-kunneth` | `sk-lem-wft-compact-kunneth` | label in the id |
| 18967 | Lem The integral of a linear character | `wft:character-integral` | `sk-lem-wft-character-integral` | label in the id |
| 19053 | Prop Base change and Fourier inversion | `wft:fourier-formal` | `sk-thm-inversion` | same text |
| 19162 | Cor Plancherel | `wft:plancherel` | `sk-cor-plancherel` | label in the id |
| 19262 | Lem Perverse sheaves on a curve | `wft:curve-heart` | `sk-lem-wft-curve-heart` | label in the id |
| 19346 | Lem The simple objects | `wft:curve-simples` | `sk-lem-wft-curve-simples` | label in the id |
| 19441 | Lem The extreme degrees on an affine curve | `wft:affine-endpoints` | `sk-l-dl-a1-endpoints` | same text |
| 19467 | Prop Fourier transform and the perverse heart | `wft:fourier-perverse` | `sk-p-dl-a1-perverse` | checked by hand |
| 19567 | Prop The Fourier transform of a middle extension | `wft:fourier-partner` | `sk-p-dl-a1-middle` | same text |

### Deligne's theorem for curves

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 19735 | Lem Fourier transform of the boundary sequence | `wft:zero-correction` | `sk-p-dl-a1-correction` | same text |
| 19797 | Prop Purity of the lisse part of the Fourier transform | `wft:fourier-some-weight` | `sk-p-dl-a1-some-weight` | same text |
| 19875 | Thm The weight of the Fourier transform | `wft:fourier-weight-shift` | `sk-p-dl-a1-fourier-weight` | checked by hand |
| 19896 | Cor $H^1_c$ as a stalk of the Fourier transform | `wft:factor-hc1` | `sk-c-dl-a1-hc1` | same text |
| 19954 | Lem Local duality at a point of $C\setminus U$ | `wft:boundary-duality` | `sk-i-dl-a1-local` | same text |
| 19991 | Prop Exactness at a fixed pure weight | `wft:middle-exact` | `sk-p-dl-a1-exact` | same text |
| 20019 | Thm The weight bound on the affine line | `wft:line-upper` | `sk-thm-dl-a1-upper` | same text |
| 20077 | Lem Finite extension of the base field and moving a lisse point to infinity | `wft:infinity-reduction` | `sk-lem-wft-infinity-reduction` | label in the id |
| 20110 | Lem A finite generically étale map to the line | `wft:finite-map` | `sk-lem-wft-finite-map` | label in the id |
| 20166 | Thm The weight bound on an affine curve | `wft:affine-curve-upper` | `sk-thm-wft-affine-curve-upper` | label in the id |
| 20205 | Thm The weight bound on a curve | `wft:curve-upper` | `sk-thm-wft-curve-middle-upper` | checked by hand |

### Deligne's theorem in general

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 20354 | Lem Finite and quasi-finite direct images | `wgen:quasi-finite` | `sk-l-dl-general-quasifinite` | same text |
| 20402 | Lem Detecting irreducibility in a finite quotient | `wgen:finite-witness` | `sk-lem-wgen-finite-witness` | label in the id |
| 20440 | Lem A curve preserving a finite cover | `wgen:bertini-cover` | `sk-lem-wgen-bertini-cover` | label in the id |
| 20491 | Cor A curve preserving geometric irreducibility | `wgen:bertini-irreducible` | `sk-cor-wgen-bertini-irreducible` | label in the id |
| 20540 | Lem Geometric constituents after a constant extension | `wgen:geometric-constituents` | `sk-lem-wgen-geometric-constituents` | label in the id |
| 20574 | Thm Real constructible sheaves are mixed | `wgen:real-mixed` | `sk-i-dl-general-real` | same text |
| 20673 | Lem Bounding the weights of a mixed sheaf | `wgen:punctual-cutoff` | `sk-lem-wgen-punctual-cutoff` | label in the id |
| 20688 | Thm Pure lisse sheaves over relative affine curves | `wgen:curve-pushforward` | `sk-p-dl-general-relative-line` | same text |
| 20790 | Lem Weights in an exact sequence | `wgen:triangle-weights` | `sk-lem-wgen-triangle-weights` | new |
| 20819 | Prop A relative affine line | `wgen:relative-line` | `sk-prop-wgen-relative-line` | label in the id |
| 20869 | Lem Relative Noether normalization over a stratification | `wgen:relative-normalization` | `sk-l-dl-general-normalization` | same text |
| 20908 | Thm Direct image of a mixed sheaf | `wgen:sheaf-direct-image` | `sk-thm-dl-general-sheaf` | same text |

### Proof of the Weil conjectures

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 21043 | Thm Purity of higher direct images under a smooth proper morphism | `wweil:smooth-proper-purity` | `sk-prop-smooth-proper-purity` | label in the id |
| 21092 | Cor Purity of the cohomology of a smooth proper variety | `wweil:cohomology-pure` | `sk-input-weights` | same text |
| 21134 | Lem Hankel rank and rationality | `wweil:hankel` | `sk-prop-criterion` | same text |
| 21180 | Lem Reduced fractions with integer coefficients | `wweil:integer-rationality` | `sk-lem-wweil-integer-rationality` | label in the id |
| 21249 | Thm The Weil conjectures for smooth proper schemes | `wweil:weil-conjectures` | `sk-thm-weil-final` | same text |
| 21359 | Ex — | — | `sk-ex-integrality-and-independence-of` | new |
| 21374 | Ex The running example: purity | `ex:run-end` | `sk-ex-ex-run-end` | new |
| 21388 | Cor Point-count estimates | `wweil:point-estimate` | `sk-cor-hasse` | same text |

### Nagata compactification and Chow's lemma

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 21554 | Def Compactification and refinement | `app:nagata-definition` | `sk-def-nagata-sketch-data` | same label |
| 21568 | Thm Nagata's compactification theorem | `app:nagata-theorem` | `sk-thm-nagata-compactification` | same label |
| 21586 | Lem Schematic closure and uniqueness | `app:nagata-closure` | `sk-lem-nagata-sketch-closure` | same label |
| 21612 | Lem Passing to the schematic closure | `app:nagata-density-normalization` | `sk-lem-nagata-density-normalization` | same label |
| 21649 | Rem — | — | `sk-rem-nagata-closure-scope` | checked by hand |
| 21658 | Prop Dense compactifications form a cofiltered category | `app:nagata-refinement` | `sk-prop-nagata-sketch-comp-category` | same label |
| 21699 | Rem Base change of a compactification | `app:nagata-base-change` | `sk-rem-nagata-base-change` | same label |
| 21736 | Def Admissible blow-up | `app:nagata-admissible` | `sk-def-nagata-admissible` | same label |
| 21767 | Lem Making an open schematically dense | `app:nagata-boundary-divisor` | `sk-lem-nagata-boundary-divisor` | same label |
| 21812 | Lem Products and composites of $U$-admissible blow-ups | `app:nagata-blowup-refinements` | `sk-lem-nagata-sketch-blowups` | same label |
| 21862 | Def Quasi-domination | `app:nagata-quasidomination` | `sk-def-app-nagata-quasidomination` | new |
| 21877 | Prop The relative form of Zariski's Main Theorem | `app:nagata-zmt` | `sk-prop-app-nagata-zmt` | new |
| 21894 | Thm Extension of a partial section | `app:nagata-conrad` | `sk-thm-app-nagata-conrad` | new |
| 21945 | Cor Extension to a proper target | `app:nagata-proper-target` | `sk-cor-nagata-sketch-proper-extension` | checked by hand |
| 21963 | Thm Elimination of indeterminacy | `app:nagata-elimination` | `sk-lem-nagata-sketch-elimination` | same label |
| 22015 | Lem Extending a graph from a compactification | `app:nagata-graph-extension` | `sk-lem-nagata-sketch-graph` | same label |
| 22064 | Lem Separation of closures | `app:nagata-separation` | `sk-lem-nagata-sketch-boundary` | same label |
| 22094 | Lem Extending an isomorphism over the closure of a closed subset | `app:nagata-near-closure` | `sk-lem-nagata-sketch-near-closure` | same label |
| 22122 | Lem Gluing after admissible blow-ups | `app:nagata-common-modification` | `sk-lem-nagata-sketch-common` | same label |
| 22157 | Prop Compactifying a union of two opens | `app:nagata-two-open` | `sk-thm-nagata-sketch-two-open` | same label |
| 22270 | Lem Affine covers with dense intersection | `app:nagata-affine-opens` | `sk-lem-nagata-sketch-affine-cover` | same label |
| 22351 | Thm Chow's lemma, projective form | `app:chow-projective` | `sk-thm-chow-projective` | same label |

### Abelian varieties and Tate modules

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 22448 | Lem Triviality on fibres | `app:abelian-seesaw` | `sk-lem-abelian-seesaw` | label in the id |
| 22473 | Cor Triviality over an open cover of the base | `app:abelian-seesaw-descent` | `sk-cor-abelian-seesaw-descent` | label in the id |
| 22491 | Lem Triviality near a fibre | `app:abelian-cube-open` | `sk-lem-abelian-cube-open` | label in the id |
| 22574 | Thm Theorem of the cube | `app:abelian-cube-theorem` | `sk-prop-av-cube` | same text |
| 22609 | Lem Rigidity | `app:abelian-rigidity` | `sk-prop-av-rigidity` | same text |
| 22655 | Def — | — | `sk-def-av` | same text |
| 22662 | Prop Commutativity, projectivity and the cube | `app:abelian-cube` | `sk-prop-av-mult-n-pullback` | same text |
| 22729 | Prop Multiplication by $n$ | `app:abelian-general-multiplication` | `sk-prop-av-isogeny` | same text |
| 22816 | Prop The integral Tate module | `app:abelian-tate` | `sk-prop-av-tate-rank` | same text |
| 22865 | Prop No Frobenius-fixed vector | `app:abelian-frobenius` | `sk-p-tate` | same text |

### Picard schemes and Jacobians

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 22977 | Def Relative Picard functor | — | `sk-def-picard-pic` | same text |
| 23000 | Lem Rigidification along a section | `app:picard-rigidification` | `sk-prop-picard-pic-split` | same label |
| 23079 | Thm Riemann–Roch and coherent Serre duality | `app:picard-riemann-roch` | `sk-thm-picard-rr` | same label |
| 23107 | Cor Serre duality and field extension | `app:picard-duality-base-change` | `sk-cor-picard-duality-base-change` | label in the id |
| 23136 | Lem Coherent base change for invertible sheaves | `app:picard-coherent-base-change` | `sk-thm-picard-perfect` | same label |
| 23192 | Thm Hilbert schemes of points on a smooth curve | `app:picard-hilbert-theorem` | `sk-thm-picard-hilb-curves` | same label |
| 23256 | Prop Divisors of degree $g$ as an open chart | `app:picard-abel-chart` | `sk-thm-picard-f-representable` | same label |
| 23301 | Lem Twisting to $h^0=1$ and $h^1=0$ | `app:picard-twist` | `sk-thm-picard-twist` | same label |
| 23358 | Thm The Picard scheme and the Jacobian over a separably closed field | `app:picard-curve` | `sk-thm-picard-main` | same label |
| 23460 | Cor Degree and the Jacobian | `app:picard-degree` | `sk-cor-picard-degree` | same label |
| 23498 | Cor Torsion of the Jacobian and field extension | `app:jacobian-torsion` | `sk-cor-jacobian-torsion` | same label |
| 23563 | Prop The Jacobian over the ground field | `app:jacobian-finite-field-descent` | `sk-prop-jacobian-descent` | checked by hand |
| 23644 | Prop $H^1$ of a curve and the Tate module of its Jacobian | `app:jacobian-equivariant-kummer` | `sk-prop-app-jacobian-equivariant-kummer` | new |

### Cohomology of curves with torsion coefficients

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 23807 | Lem Cohomology of the multiplicative group | `app:curve-gm` | `sk-thm-br` | same label |
| 23867 | Prop Smooth proper curves, torsion prime to the characteristic | `app:curve-kummer` | `sk-thm-curveestimate` | same label |
| 23926 | Rem Twists and the projective line | `app:curve-twists` | `sk-rem-curve-twists` | same label |
| 23962 | Prop Cohomology of a smooth affine curve | `app:curve-affine-kummer` | `sk-prop-curve-affine-kummer` | same label |
| 24074 | Prop $p$-torsion on a smooth proper curve in characteristic $p$ | `app:curve-artin-schreier` | `sk-prop-curve-artin-schreier` | same label |
| 24138 | Lem $p$-torsion on an affine curve in characteristic $p$ | `app:curve-affine-artin-schreier` | `sk-lem-curve-affine-artin-schreier` | same label |
| 24156 | Ex The affine line in characteristic $p$ | `app:curve-wild-example` | `sk-rem-curve-wild-example` | same label |
| 24204 | Lem Sheaves with finite support and finite morphisms | `app:curve-finite-support` | `sk-lem-curve-finite-support` | same label |
| 24231 | Lem Normalization of a constant sheaf | `app:curve-normalization` | `sk-lem-curve-normalization` | same label |
| 24290 | Lem Removing finitely many points | `app:curve-dense-open` | `sk-lem-curve-dense-open` | same label |
| 24364 | Lem Reduction to a unipotent local system | `app:curve-sylow-trace` | `sk-lem-curve-sylow-trace` | same label |

### Specialization and contracting correspondences

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 24662 | Lem Nearby cycles of a constant family | `tf:sp-constant-family` | `sk-lem-tf-sp-constant-family` | same label |
| 24788 | Lem Functoriality of the deformation | `tf:sp-dnc-functorial` | `sk-lem-tf-sp-dnc-functorial` | same label |
| 24831 | Lem Base change for the cone of $\tau_{X,Z}$ | `tf:sp-defect-exchanges` | `sk-lem-tf-sp-defect-exchanges` | same label |
| 24867 | Lem The case $Z=V(x^m)\subset\mathbf A^1$ | `tf:sp-thick-origin` | `sk-lem-tf-sp-thick-origin` | same label |
| 24926 | Lem Vanishing at the generic points of a principal divisor | `tf:sp-generic-divisor` | `sk-lem-tf-sp-generic-divisor` | same label |
| 24991 | Thm Verdier's theorem on specialization to the zero section | `tf:sp-zero-section` | `sk-thm-tf-sp-zero-section` | same label |
| 25164 | Prop External Künneth formula for nearby cycles | `tf:nearby-external-kunneth` | `sk-prop-tf-nearby-external-kunneth` | same label |
| 25411 | Lem Compatibilities of the base change maps | `tf:nearby-mate-coherences` | `sk-lem-tf-nearby-mate-coherences` | same label |
| 25581 | Prop Nearby cycles commute with Verdier duality | `tf:nearby-duality-foundation` | `sk-prop-tf-nearby-duality-foundation` | same label |
| 25799 | Prop Specialization of the trace class | `tf:trace-specialization` | `sk-prop-tf-trace-specialization` | same label |
| 25947 | Cor Specialization when the fixed point scheme is a constant family | `tf:sp-fixed-constant` | `sk-cor-tf-sp-fixed-constant` | same label |
| 26005 | Lem Normal cones and contracting ideals | `tf:contracting-cone-geometry` | `sk-lem-tf-contracting-cone-geometry` | same label |
| 26068 | Lem The fixed point scheme of the deformation | `tf:contracting-fixed-geometry` | `sk-lem-tf-contracting-fixed-geometry` | same label |
| 26125 | Rem Reduction to a connected fixed point scheme | `tf:contracting-neighbourhood` | `sk-rem-tf-contracting-neighbourhood` | same label |
| 26137 | Thm Contracting correspondences and local terms | `tf:contracting-local-term` | `sk-thm-tf-contracting-local-term` | same label |
| 26255 | Cor Contracting local terms at a point | `tf:contracting-input` | `sk-cor-tf-contracting-input` | same label |

### Algebraic groups and Lie algebras in characteristic zero

| Tex line | Declaration | Label | Sketch node | Matched by |
|---:|---|---|---|---|
| 26362 | Prop Cartier's theorem | `app:walg:cartier` | `sk-i-cartier` | checked by hand |
| 26439 | Lem Connected components and images of homomorphisms | `app:walg:group-geometry` | `sk-p-geometry` | same text |
| 26530 | Lem Stable subspaces and the center | `app:walg:group-lie` | `sk-p-comparison` | same text |
| 26603 | Lem Lie's theorem | `app:walg:lie-eigenvector` | `sk-lem-walg-lie-eigenvector` | label in the id |
| 26616 | Lem Engel's theorem | `app:walg:engel` | `sk-lem-walg-engel` | label in the id |
| 26630 | Lem Cartan's criterion | `app:walg:trace-criterion` | `sk-lem-walg-trace-criterion` | label in the id |
| 26671 | Lem — | `app:walg:killing` | `sk-lem-walg-killing` | label in the id |
| 26706 | Prop Lie algebras with a faithful semisimple representation | `app:walg:central-radical` | `sk-p-lie` | same text |
