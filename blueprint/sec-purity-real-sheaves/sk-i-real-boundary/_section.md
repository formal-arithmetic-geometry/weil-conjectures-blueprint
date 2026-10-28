+++
id = "sk-i-real-boundary"
kind = "lemma"
title = "The boundary stalk"
order = 4103
uses = ["sk-d-real-weil", "sk-lem-finite", "sk-p-real-integral", "sk-thm-sf-ctf-stability"]
lean = ["AlgebraicGeometry.Scheme.isConstructibleSheaf_lowerStar", "AlgebraicGeometry.Scheme.isIso_unit_upperStarLowerStarAdjunction"]
tags = ["sketch"]
+++
Let $j:U_0\hookrightarrow X_0$ be a dense open in a smooth curve and
let $\mathcal F$ be a lisse Weil sheaf on $U_0$. At a missing geometric point
$\bar s$, with local inertia $I_s$ acting on the local generic fibre
$V$, there is a canonical Frobenius-equivariant identification

$$
 (j_*\mathcal F)_{\bar s}=V^{I_s}.
$$

Here $j_*$ is the ordinary direct image of sheaves. If $\mathcal F$
extends lisse to $X_0$, the adjunction from that extension to
$j_*\mathcal F$ is an isomorphism.

*Complement.* For a missing point $s$, let $K_s$ be the fraction field of the
henselization of $\mathcal O_{X_0,s}$ and
$I_s=\ker(\Gal(\overline K_s/K_s)\to\Gal(\overline{\kappa(s)}/\kappa(s)))$; a
path from a geometric point over $\operatorname{Spec}K_s$ to the base point
gives a decomposition-group map into $\pi_1(U_0)$ carrying $I_s$ into
$\pi_1(U)$, residue Frobenius lifts act unambiguously on $V^{I_s}$, and the
result is independent of the path up to Frobenius-equivariant isomorphism
([d-real-boundary]). The sheaf $j_*\mathcal F=\mathcal H^0(Rj_*\mathcal F)$ is
constructible, for $\mathcal F$ finite locally constant over a finite ring
and for $\mathcal F$ a lisse $\overline{\mathbf Q}_\ell$-sheaf
([lem-wf-boundary-stalk-invariants], [sk-thm-sf-ctf-stability]). For a
finite locally constant $\mathcal G$ on $X_0$ the unit
$\mathcal G\to j_*j^*\mathcal G$ is an isomorphism
([lem-wf-dense-open-pi1-surjective] (3)), and for a lisse
$\overline{\mathbf Q}_\ell$-sheaf this is the last assertion
([lem-a1-lisse-middle-extension]).
