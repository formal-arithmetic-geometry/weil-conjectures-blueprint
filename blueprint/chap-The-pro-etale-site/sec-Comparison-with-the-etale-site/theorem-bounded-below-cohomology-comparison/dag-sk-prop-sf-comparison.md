+++
id = "dag-sk-prop-sf-comparison"
kind = "dag-lemma"
title = "Bounded-below cohomology comparison"
name_showing = false
order = 123502
tags = ["sheaf-dag"]
split_from = "theorem-bounded-below-cohomology-comparison"
dag_id = "sk-prop-sf-comparison"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.boundedBelowComparisonGlobalSections", "AlgebraicGeometry.ProEtale.boundedBelowComparison"]
uses = ["dag-sk-def-pe-morphisms"]
+++
Let $X$ be a scheme, $\Lambda$ a ring, and $\nu_X:X_{\mathrm{proét}}\to X_{\mathrm{ét}}$
the comparison morphism. For $K\in D^+(X_{\mathrm{ét}},\Lambda)$ the unit of the
adjunction between
$\nu_X^*:D^+(X_{\mathrm{ét}},\Lambda)\to D^+(X_{\mathrm{proét}},\Lambda)$ and
$R\nu_{X,*}$ is an isomorphism

$$
K\xrightarrow{\ \sim\ }R\nu_{X,*}\nu_X^*K\quad\text{in }D^+(X_{\mathrm{ét}},\Lambda).
$$

Consequently $\nu_X^*:D^+(X_{\mathrm{ét}},\Lambda)\to D^+(X_{\mathrm{proét}},\Lambda)$ is
fully faithful, and there is a canonical isomorphism in the derived category
of $\Lambda$-modules

$$
R\Gamma(X_{\mathrm{proét}},\nu_X^*K)\simeq R\Gamma(X_{\mathrm{ét}},K).
$$

More generally, for a pro-étale affine $U=\varprojlim_iU_i$ with $U_i$
affine and étale over $X$,

$$
R\Gamma(U_{\mathrm{proét}},(\nu_X^*K)|_U)\simeq
\varinjlim_iR\Gamma((U_i)_{\mathrm{ét}},K|_{U_i}).
$$

The colimit here is a filtered derived colimit, so its cohomology is the
filtered colimit of the cohomology groups.

Coefficients are discrete, and modules are left modules. Thus module sheaves mean sheaves of left $\Lambda$-modules, equivalently modules over the constant ring sheaf `def-weil-sheaf-of-modules-category`, in a common larger universe in which the underlying site categories are small. The small sites and comparison geometric morphism are those of `def-weil-pbc-site-comparison-morphism`, with its set inverse image applied to addition and every scalar action for any ring $\Lambda$. Derived categories are the localizations at quasi-isomorphisms `def-weil-abstract-derived-category`; $D^+$ means cohomology vanishes sufficiently far below `def-weil-pbc-bounded-derived-subcategories`. The right derived functors of comparison direct image and sections at the terminal object use `lem-weil-pbc-right-derived-plus-injective`. A pro-étale affine is as in [dag-sk-def-pe-morphisms]; the presentation above is indexed by a nonempty small cofiltered category, and the colimit is over its opposite filtered category.

(SHEAF DAG node `sk-prop-sf-comparison`; machine-alignment layer.) Split from [theorem-bounded-below-cohomology-comparison]. DAG kind: statement. DAG status: split. Lean names not on master: `AlgebraicGeometry.ProEtale.comparisonSectionComplexes`, `AlgebraicGeometry.ProEtale.comparisonResolutionUnit`, `AlgebraicGeometry.ProEtale.comparisonResolutionSections`, `AlgebraicGeometry.ProEtale.affineComparisonResolutionCocone`, `AlgebraicGeometry.ProEtale.affineBoundedBelowComparison`. Statement dependencies not drawn: `def-weil-pbc-site-comparison-morphism`, `def-weil-abstract-derived-category`, `def-weil-pbc-bounded-derived-subcategories`, `lem-weil-pbc-right-derived-plus-injective`, `def-weil-sheaf-of-modules-category`.
