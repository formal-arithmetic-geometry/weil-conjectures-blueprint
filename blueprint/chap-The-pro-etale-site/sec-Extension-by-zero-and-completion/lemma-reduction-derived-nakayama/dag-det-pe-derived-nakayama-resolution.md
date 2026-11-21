+++
id = "dag-det-pe-derived-nakayama-resolution"
kind = "dag-lemma"
title = "The two-term resolution of the finite coefficient sheaves"
name_showing = false
order = 210501
tags = ["sheaf-dag"]
split_from = "lemma-reduction-derived-nakayama--1"
dag_id = "det-pe-derived-nakayama-resolution"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.DerivedNakayama.integerRingSheaf", "AlgebraicGeometry.ProEtale.DerivedNakayama.quotientRingSheaf", "AlgebraicGeometry.ProEtale.DerivedNakayama.reductionRingSheaf", "AlgebraicGeometry.ProEtale.DerivedNakayama.integerRing", "AlgebraicGeometry.ProEtale.DerivedNakayama.integerRing_isCommMonObj", "AlgebraicGeometry.ProEtale.DerivedNakayama.quotientRing", "AlgebraicGeometry.ProEtale.DerivedNakayama.reductionRing", "AlgebraicGeometry.ProEtale.DerivedNakayama.quotientModule", "AlgebraicGeometry.ProEtale.DerivedNakayama.pullback", "AlgebraicGeometry.ProEtale.DerivedNakayama.Derived", "AlgebraicGeometry.ProEtale.DerivedNakayama.reductionFunctor", "AlgebraicGeometry.ProEtale.DerivedNakayama.reductionMap", "AlgebraicGeometry.ProEtale.DerivedNakayama.pullback_regular", "AlgebraicGeometry.ProEtale.DerivedNakayama.regularPullbackIso", "AlgebraicGeometry.ProEtale.DerivedNakayama.scalarOnModules", "AlgebraicGeometry.ProEtale.DerivedNakayama.scalarOnComplex", "AlgebraicGeometry.ProEtale.DerivedNakayama.coneFunctor", "AlgebraicGeometry.ProEtale.DerivedNakayama.derived_nakayama_resolution"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $E/\Ql$ be finite with uniformizer $\pi_E$ and $n\geq1$. For every scheme $X$
the sequence of $\mathcal O_{E,X}$-module sheaves on $X_{\Proet}$

$$
0\to\mathcal O_{E,X}\xrightarrow{\ \pi_E^n\ }\mathcal O_{E,X}\to(\mathcal O_E/\pi_E^n)_X\to0
$$

is exact. Consequently, for $K\in D(X_{\Proet},\mathcal O_E)$,
$K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X$ is
isomorphic to the cone of $\pi_E^n\colon K\to K$, naturally in $K$, and for
$1\leq m\leq n$ there are triangles
$K_m\xrightarrow{\pi_E^{n}}K_{n+m}\to K_n\to$, in particular
$K_1\to K_{n+1}\to K_n\to$.

(SHEAF DAG node `det-pe-derived-nakayama-resolution`; machine-alignment layer.) Split from [lemma-reduction-derived-nakayama--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-sfb-qlbar-coefficient-ring`, `def-sfb-upper-star-from-point`, `def-weil-abstract-derived-category`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-sheaf-tensor-presheaf`, `lem-coef-grothendieck-locally-presentable`, `lem-pc-derived-category-locally-small`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-modobj-abelian`, `lem-sfb-modobj-grothendieck`, `lem-sfb-proetale-sheaves-grothendieck`, `lem-weil-l-adic-extension-integers-dvr`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `sk-def-sfb-module-objects`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`.
