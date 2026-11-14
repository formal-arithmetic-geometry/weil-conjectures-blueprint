+++
id = "dag-sk-def-cd"
kind = "dag-definition"
title = "Cohomological dimension"
name_showing = false
order = 157501
tags = ["sheaf-dag"]
split_from = "definition-cohomological-dimension--1"
dag_id = "sk-def-cd"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.IsEllPowerTorsionLocal", "AlgebraicGeometry.ProEtale.ellPowerKernel", "AlgebraicGeometry.ProEtale.ellPowerKernelMap_condition", "AlgebraicGeometry.ProEtale.ellPowerKernelMap", "AlgebraicGeometry.ProEtale.ellPowerKernelFunctor_map_id", "AlgebraicGeometry.ProEtale.ellPowerKernelFunctor_map_comp", "AlgebraicGeometry.ProEtale.ellPowerKernelFunctor", "AlgebraicGeometry.ProEtale.ellPowerKernelCocone_naturality", "AlgebraicGeometry.ProEtale.ellPowerKernelCocone", "AlgebraicGeometry.ProEtale.ellPowerKernelColimitMap", "AlgebraicGeometry.ProEtale.IsEllPowerTorsion", "AlgebraicGeometry.ProEtale.isEllPowerTorsion_iff_local", "AlgebraicGeometry.ProEtale.IsClassicalAbelian", "AlgebraicGeometry.ProEtale.IsNonzeroProEtaleCohomology", "AlgebraicGeometry.ProEtale.IsNonzeroProEtaleHigherDirectImage", "AlgebraicGeometry.ProEtale.cohomologicalDimension", "AlgebraicGeometry.ProEtale.relativeCohomologicalDimension", "AlgebraicGeometry.ProEtale.etaleCohomologicalDimension", "AlgebraicGeometry.ProEtale.cohomologicalDimension_eq_etaleCohomologicalDimension", "AlgebraicGeometry.ProEtale.relativeCohomologicalDimension_eq_etale", "AlgebraicGeometry.ProEtale.relativeCohomologicalDimension_lt_top_of_finiteType", "AlgebraicGeometry.ProEtale.cohomologicalDimension_lt_top_of_finiteType"]
uses = ["dag-sk-def-pe-classical-definition", "dag-det-pe-topos-functoriality-inverse-image"]
+++
Fix a prime $\ell$. All sheaves below are sheaves of abelian groups. On either site, put $F[\ell^r]=\ker(\ell^r:F\to F)$ for $r\geq0$, and call $F$ *$\ell$-power torsion* if the canonical map $\varinjlim_{r\geq0}F[\ell^r]\to F$ is an isomorphism, with the inclusions as transition maps. This is the local torsion convention; no common exponent is required. Take the following suprema over $q\in\mathbf Z_{\geq0}$ in $\mathbf Z_{\geq0}\cup\{+\infty\}$, whose empty supremum is $0$.

For a qcqs scheme $S$ and a qcqs morphism $g:X\to Y$, the
*$\ell$-cohomological dimensions* are

$$
\begin{aligned}
\operatorname{cd}_\ell(S)&=\sup\{q: H^q(S_{\mathrm{pro}\acute{e}t},F)\neq0
\text{ for some classical $\ell$-power torsion sheaf $F$}\},\\
\operatorname{cd}_\ell(g)&=\sup\{q: R^qg_*F\neq0
\text{ for some classical $\ell$-power torsion sheaf $F$ on }X_{\mathrm{pro}\acute{e}t}\}.
\end{aligned}
$$

For a field $k'$ we write $\operatorname{cd}_\ell(k')=\operatorname{cd}_\ell(\operatorname{Spec}k')$.

Here the small pro-étale site is `sk-def-pe-site`, classical means [dag-sk-def-pe-classical-definition], and qcqs has the conventions of `def-weil-pbc-scheme-conventions`. The notation $H^q(S_{\mathrm{pro}\acute{e}t},F)$ means $\mathcal H^q(R\Gamma(S_{\mathrm{pro}\acute{e}t},F))$, where $\Gamma$ is evaluation at the terminal object $S$; $R^qg_*F$ means $\mathcal H^q(Rg_*F)$, where $(g_*F)(V)=F(V\times_YX)$ is the direct image on the small pro-étale sites [dag-det-pe-topos-functoriality-inverse-image]. Both right derived functors are as in `def-sfb-right-derived-functor`, applied to a sheaf in degree zero.

(SHEAF DAG node `sk-def-cd`; machine-alignment layer.) Split from [definition-cohomological-dimension--1]. DAG kind: definition. DAG status: split. Statement dependencies not drawn: `def-pur-abelian-sheaf-kernel`, `def-weil-pbc-category-colimit`, `def-weil-pbc-scheme-conventions`, `sk-def-pe-site`, `def-sfb-right-derived-functor`.
