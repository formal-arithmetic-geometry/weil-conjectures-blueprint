+++
id = "proposition-proper-direct-image-constructible-complexes--11"
kind = "proposition"
title = "Finite extension of $\\Ql$"
order = 425022
aliases = ["bp-r129-11"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_projectionMap_app_app_padicSubfield_of_padicIntegers"]
uses = ["definition-projection-formula-map", "definition-change-of-coefficients-maps"]
+++
The Lean route uses the following coefficient-change statement in place of a
separate projection-formula theorem for arbitrary $E$-complexes.

Let $\ell$ be prime, let $E\subset\overline{\mathbf Q}_\ell$ be finite over
$\Ql$, and let $p:X\to Y$ be a quasi-compact quasi-separated morphism of schemes.
Let $K_0\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ and
$M_0\in D(Y_{\mathrm{pro}\acute{e}t},\mathcal O_E)$. Suppose that $K_0$ and
$K_0\otimes^{\mathbf L}_{\mathcal O_E}p^*M_0$ are bounded below, and that the
integral projection formula map at $(K_0,M_0)$ is an isomorphism. Then the
$E$-coefficient projection formula map at
$$
K=E_X\otimes^{\mathbf L}_{\mathcal O_{E,X}}K_0,\qquad
M=E_Y\otimes^{\mathbf L}_{\mathcal O_{E,Y}}M_0
$$
is an isomorphism. Properness and constructibility are not assumptions of this
coefficient-change statement.
