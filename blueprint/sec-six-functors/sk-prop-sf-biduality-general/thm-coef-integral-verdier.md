+++
id = "thm-coef-integral-verdier"
kind = "theorem"
title = "Integral Verdier biduality"
order = 2486
uses = ["def-weil-derived-complete", "lem-coef-integral-hom-reduction", "lem-coef-integral-residue-tor", "lem-weil-duality-pairing", "lem-weil-finite-duality-site-comparison", "lem-weil-verdier-preservation-strata", "prop-coef-integral-dualizing", "thm-fix-general-biduality"]
+++
Set

$$
D_{X,R}K=R\mathcal Hom_R(K,\omega_{X,R}).
$$

This is an exact contravariant anti-equivalence of
$D^b_c(X,R)=D^b_{ctf}(X,R)$. Its canonical comparisons satisfy

$$
(D_{X,R}K)\otimes_R^L A_n\cong D_{X,n}K_n,
\qquad D_{X,R}K\cong R\varprojlim_n\operatorname{Res}_nD_{X,n}K_n.
$$

If $\dim X\leq d$ and the reductions of $K$ have Tor interval
$[a,b]$, those of $D_{X,R}K$ have interval
$[-b-2d,-a]$. The comparisons preserve evaluation and identify
the reduction of the actual double-dual map
$\delta_K:K\to D_{X,R}D_{X,R}K$ with $\delta_{K_n}$.
In particular $\delta_K$ is an isomorphism.
