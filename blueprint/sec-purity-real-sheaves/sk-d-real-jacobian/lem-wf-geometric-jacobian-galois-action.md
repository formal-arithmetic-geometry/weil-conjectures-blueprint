+++
id = "lem-wf-geometric-jacobian-galois-action"
kind = "lemma"
title = "Canonical semilinear Galois action on the geometric Jacobian"
lean = ["AlgebraicGeometry.exists_jacobian_galoisAction"]
order = 3999
uses = ["def-sc-jacobian", "def-sc-picard-functor", "def-wf-abelian-tate-module", "lem-pc-representable-unique", "lem-sc-jacobian-unique", "thm-pd-jacobian-general-field", "thm-sc-jacobian-representability"]
+++
Let $C_0/k_0$ be a smooth projective geometrically connected curve, put
$C=C_0\times_{k_0}\overline{k}_0$, and let $J$ be the
Jacobian of $C$, which exists by
[thm-sc-jacobian-representability] because $C$ is a smooth projective
curve over the separably closed field $\overline{k}_0$ and is geometrically
integral ($C_0$ is smooth, hence geometrically reduced, and geometrically
connected by hypothesis). For every
$\sigma\in\operatorname{Gal}(\overline{k}_0/k_0)$ there is a canonical
isomorphism

$$
\sigma_J:\;J\longrightarrow J
\qquad\text{over}\qquad
\sigma:\operatorname{Spec}\overline{k}_0\longrightarrow
\operatorname{Spec}\overline{k}_0,
$$

which preserves the group laws and is compatible with the identification
$\operatorname{Pic}^0(C)=J(\overline{k}_0)$; the assignment
$\sigma\mapsto\sigma_J$ is an action of
$\operatorname{Gal}(\overline{k}_0/k_0)$, so that $J(\overline{k}_0)$ is a
Galois module and $T_\ell J$ a
$\mathbf Z_\ell[\operatorname{Gal}(\overline{k}_0/k_0)]$-module for the Tate
module of [def-wf-abelian-tate-module]. Moreover, if $J_0$ is the
Jacobian of $C_0$ over $k_0$ of [thm-pd-jacobian-general-field], then
under the isomorphism $J\cong J_0\times_{k_0}\overline{k}_0$ of that
theorem one has $\sigma_J=\mathrm{id}_{J_0}\times\sigma$; hence the action
on $J(\overline{k}_0)=J_0(\overline{k}_0)$ is the one through the
$k_0$-structure of $J_0$, and the identification
$J_0[\ell^n](\overline{k}_0)\cong\operatorname{Pic}^0(C)[\ell^n]$ is
$\operatorname{Gal}(\overline{k}_0/k_0)$-equivariant for every $\ell$ and
$n$.
