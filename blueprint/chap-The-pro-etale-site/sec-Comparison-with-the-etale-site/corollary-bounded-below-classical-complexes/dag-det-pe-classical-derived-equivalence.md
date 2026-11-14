+++
id = "dag-det-pe-classical-derived-equivalence"
kind = "dag-lemma"
title = "The bounded-below classical equivalence"
name_showing = false
order = 129501
tags = ["sheaf-dag"]
split_from = "corollary-bounded-below-classical-complexes--2"
dag_id = "det-pe-classical-derived-equivalence"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.classicalDerivedEquivalence"]
uses = ["dag-det-pe-classical-definition-continuity-map", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $X$ be a scheme and $\Lambda$ a discrete commutative ring for which the
bounded-below derived unit $L\xrightarrow{\sim}R\nu_{X,*}\nu_X^*L$ of
[dag-sk-prop-sf-comparison] holds for $L\in D^+(X_{\Et},\Lambda)$.

1. $\nu_X^*$ maps $D^+(X_{\Et},\Lambda)$ into
   $D^+_{\mathrm{class}}(X_{\Proet},\Lambda)$, and $R\nu_{X,*}$ maps
   $D^+(X_{\Proet},\Lambda)$ into $D^+(X_{\Et},\Lambda)$.
2. For every $K\in D^+_{\mathrm{class}}(X_{\Proet},\Lambda)$ the counit
   $\nu_X^*R\nu_{X,*}K\to K$ is an isomorphism.

Hence $\nu_X^*$ and $R\nu_{X,*}$ are inverse equivalences between
$D^+(X_{\Et},\Lambda)$ and $D^+_{\mathrm{class}}(X_{\Proet},\Lambda)$.

(SHEAF DAG node `det-pe-classical-derived-equivalence`; machine-alignment layer.) Split from [corollary-bounded-below-classical-complexes--2]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-weil-abstract-derived-category`, `def-weil-pbc-bounded-derived-subcategories`, `def-weil-pbc-derived-inverse-image`, `def-weil-sheaf-of-modules-category`, `lem-coef-grothendieck-locally-presentable`, `lem-pc-derived-category-locally-small`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-proetale-sheaves-grothendieck`, `lem-trf-bounded-below-derived-adjunction`, `lem-weil-pbc-sheaf-tensor-closed`, `prop-weil-pbc-derived-inverse-image-adjunction`.
