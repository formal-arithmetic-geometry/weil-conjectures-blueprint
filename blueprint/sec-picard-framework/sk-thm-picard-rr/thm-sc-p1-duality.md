+++
id = "thm-sc-p1-duality"
kind = "theorem"
title = "Duality on the projective line"
lean = ["AlgebraicGeometry.Scheme.Modules.yonedaDualMap", "AlgebraicGeometry.ProjectiveLine.nonempty_dual_H_one_iso", "AlgebraicGeometry.ProjectiveLine.bijective_yonedaDualMap", "AlgebraicGeometry.ProjectiveLine.dualHZeroLinearEquivExt", "AlgebraicGeometry.ProjectiveLine.extIsoDualHZero", "AlgebraicGeometry.ProjectiveLine.nonempty_dual_H_zero_iso_ext", "AlgebraicGeometry.ProjectiveLine.nonempty_dual_H_zero_addEquiv_ext", "AlgebraicGeometry.ProjectiveLine.nonempty_dual_H_zero_linearEquiv_ext"]
order = 702
uses = ["def-sc-ext-sheaf", "def-sc-kahler-differentials", "def-sc-p1-standard", "lem-pc-projective-space-serre-pairing", "lem-sc-ext-locally-free", "lem-sc-four-lemma", "lem-sc-p1-graded-resolution", "lem-sc-p1-hi-vanishing", "lem-sc-p1-monomial", "lem-sc-p1-twist-exists"]
+++
Let $k$ be a field. For every coherent
$\mathcal O_{\mathbf P^1_k}$-module $\mathcal G$, with

$$
\omega_{\mathbf P^1}:=\Omega^1_{\mathbf P^1_k/k}\cong\mathcal O(-2)
$$

([def-sc-kahler-differentials],
[lem-sc-p1-monomial](iii)), there are canonical isomorphisms,
natural in $\mathcal G$,

$$
H^1(\mathbf P^1_k,\mathcal G)^{\vee}\;\cong\;
\operatorname{Hom}_{\mathcal O_{\mathbf P^1}}\bigl(\mathcal G,
\omega_{\mathbf P^1}\bigr),
$$

$$
H^0(\mathbf P^1_k,\mathcal G)^{\vee}\;\cong\;
\operatorname{Ext}^1_{\mathbf P^1}\bigl(\mathcal G,
\omega_{\mathbf P^1}\bigr)
$$

(with $\operatorname{Ext}$ of [def-sc-ext-sheaf]; all groups
involved are finite-dimensional, the cohomology of coherent modules
on a proper scheme over a field being finite-dimensional).
