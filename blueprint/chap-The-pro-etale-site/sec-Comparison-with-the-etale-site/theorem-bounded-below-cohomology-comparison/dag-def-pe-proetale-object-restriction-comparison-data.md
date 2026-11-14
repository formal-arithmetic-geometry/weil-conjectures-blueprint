+++
id = "dag-def-pe-proetale-object-restriction-comparison-data"
kind = "dag-definition"
title = "Canonical pro-étale object restriction comparison data"
name_showing = false
order = 123501
tags = ["sheaf-dag"]
split_from = "theorem-bounded-below-cohomology-comparison"
dag_id = "def-pe-proetale-object-restriction-comparison-data"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.ProEtaleObjectRestrictionComparison", "AlgebraicGeometry.Scheme.proEtaleObjectInverseImageIndexPoint"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-def-weil-pbc-sheafification"]
+++
Let $X$ be a scheme and $r:W\to X$ an object of the small pro-étale site [dag-def-weil-pbc-proetale-site], with schemes in universe $u$, site objects in $u+1$ and site morphisms in $u$. Let $D$ be a category with object universe $v$, morphism universe $u+1$, colimits of size $(u+1,u+1)$ and weak sheafification on $W_{\mathrm{proét}}$ [dag-def-weil-pbc-sheafification]. Write $R_r$ for sectionwise restriction to $W$, $R_rG(U\to W)=G(U\to W\to X)$ [dag-def-pur-localized-ringed-site], $u_r$ for base change, $L_r=(-)\circ u_r^{\mathrm{op}}$'s left adjoint (left Kan extension), and $r^{-1}G=(L_rG)^\#$ `def-weil-proetale-inverse-image`. For $U\to W$, define $q_{W,U}$ in the inverse-image index $\mathcal I_U$ to be $(U\to W\to X,\varphi_0)$, where $\varphi_0:U\to U\times_X W$ is the pair $(\mathrm{id}_U,\mathrm{str})$, with this factor order for the chosen pullback. Define $\mathrm{ProEtaleObjectRestrictionComparison}(W,D)$ to be the type of data consisting of: (i) a natural isomorphism $p:\iota_W\circ R_r\cong L_r\circ\iota_X$, where $\iota_X,\iota_W$ forget the sheaf conditions; (ii) for every sheaf $G$ and object $U\to W$, the component $p_G(U)$ equals the distinguished Kan coprojection indexed by $q_{W,U}$, namely the Kan unit at $U\to X$ followed by the map along $\varphi_0^{\mathrm{op}}$; (iii) for every $G$, an assertion that the actual sheafification unit $L_rG\to(L_rG)^\#$ is invertible; (iv) a natural isomorphism $s:r^{-1}\cong R_r$; and (v) the equation that the underlying presheaf map of $s_G^{-1}$ is $p_G$ followed by the sheafification unit, for every $G$. These definitions do not assert that the comparison-data type is inhabited.

(SHEAF DAG node `def-pe-proetale-object-restriction-comparison-data`; machine-alignment layer.) Split from [theorem-bounded-below-cohomology-comparison]. DAG kind: definition. Placed through `sk-prop-sf-comparison` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-pur-localized-ringed-site`, `def-weil-proetale-inverse-image`.
