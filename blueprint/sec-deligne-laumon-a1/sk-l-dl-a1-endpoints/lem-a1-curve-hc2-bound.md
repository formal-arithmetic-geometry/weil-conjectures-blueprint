+++
id = "lem-a1-curve-hc2-bound"
kind = "lemma"
title = "Top compact-support bound on a curve"
order = 2734
uses = ["def-weil-ordinary-compact-cohomology", "def-weil-punctual-weights", "lem-a1-affine-hc2", "lem-a1-subquotient-extension-bounds", "lem-tw-tate-twist-weight-shift"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.hasWeightsAtMostOver_compactlySupportedCohomology_two"]
+++
If $C_0$ is a smooth affine curve over $k_0$ (affine and smooth of
relative dimension one, not necessarily connected) and $\mathcal F$ is a
lisse Weil sheaf on $C_0$,
punctually $\iota$-pure of weight $w$, then
$H_c^2(C,\mathcal F)$ has weights at most $w+2$.

## Proof
*Step 1: $C_0$ geometrically connected.* The coinvariant description
[lem-a1-affine-hc2] realizes the group
as a quotient of the local generic fiber $V=\mathcal F_{\bar\eta}$
followed by the twist $(-1)$. The quotient does not increase weights
by [lem-a1-subquotient-extension-bounds] (every eigenvalue of a
quotient is an eigenvalue of the pure module $V$ of weight $w$), and
the twist $(-1)$ in [lem-tw-tate-twist-weight-shift] raises
weights by two, giving weights at most $w+2$.

*Step 2: the general case.* The affine scheme $C_0$ is noetherian, so it
has finitely many connected components $C_{0,1},\dots,C_{0,m}$, each open
and closed, and $H_c^2(C,\mathcal F)=\bigoplus_iH_c^2(C_i,\mathcal F|_{C_i})$
Frobenius-equivariantly; an eigenvalue of Frobenius on the sum is an
eigenvalue on a summand, so we may assume $C_0$ connected. Being smooth
and connected, $C_0$ is irreducible; let $k_1$ be the algebraic closure
of $k_0$ in its function field, of degree $d$ over $k_0$. Then $C_0$ is a
smooth geometrically connected affine curve over $k_1$, and
$C=C_0\otimes_{k_0}k$ is the disjoint union of the $d$ curves
$C_\sigma=C_0\otimes_{k_1,\sigma}k$, $\sigma\in\operatorname{Hom}_{k_0}(k_1,k)$,
which the Frobenius $F$ permutes cyclically. Hence
$H_c^2(C,\mathcal F)=\bigoplus_\sigma H_c^2(C_\sigma,\mathcal F)$ with $F$
permuting the summands cyclically, and $F^d$ preserves each summand and
acts on it as the Frobenius of $C_0$ over $k_1$. Over $k_1$ (with
$q_1=q^d$) the sheaf $\mathcal F$ is still punctually $\iota$-pure of
weight $w$, since the local Frobenius $F_x$ and $q_x=|\kappa(x)|$ at a
closed point do not depend on the base field. By Step 1 every
eigenvalue $\mu$ of $F^d$ on a summand satisfies
$|\iota(\mu)|^2\le q_1^{w+2}=q^{d(w+2)}$. If $\alpha$ is an eigenvalue of
$F$ with eigenvector $v=(v_\sigma)$ and $v_\sigma\ne0$, then comparing
the $\sigma$-components of $F^dv=\alpha^dv$ shows that $\alpha^d$ is an
eigenvalue of $F^d$ on $H_c^2(C_\sigma,\mathcal F)$, so
$|\iota(\alpha)|^{2d}\le q^{d(w+2)}$, that is, $|\iota(\alpha)|^2\le q^{w+2}$.
