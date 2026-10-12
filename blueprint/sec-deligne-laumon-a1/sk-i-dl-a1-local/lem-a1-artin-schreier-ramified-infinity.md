+++
id = "lem-a1-artin-schreier-ramified-infinity"
kind = "lemma"
title = "Linear Artin–Schreier sheaves are ramified at infinity"
order = 3032
uses = ["d-real-boundary", "def-fd-additive-character", "def-fd-artin-schreier-sheaf", "lem-fd-as-characters", "lem-fd-as-cover", "lemma-weil-pbc-finite-stalk-formula", "rem-dl-a1-conventions"]
lean = ["AlgebraicGeometry.not_isUnramifiedAtInfinity_artinSchreier"]
+++
Let $\psi=\Psi\circ\operatorname{Tr}$ be the additive character of
[def-fd-additive-character], with $\Psi:\mathbf F_p\to\Qlb^\times$ the fixed
nontrivial character, let $k_1\subseteq k$ be a finite
field, and let $a\in k_1^\times$. Let
$\mathcal L_{\psi(ax)}:=\mathcal L_{\psi,ax}$ be the Artin–Schreier
sheaf of [def-fd-artin-schreier-sheaf] on
$\mathbf A^1_{k_1}=\operatorname{Spec}k_1[x]$ for $f=ax$; explicitly, it is the
$\Psi$-isotypic part

$$
\mathcal L_{\psi(ax)}=e_\Psi\cdot\pi_*\Qlb,\qquad
e_\Psi=\frac1p\sum_{c\in\mathbf F_p}\Psi(-c)\,\sigma_c,
$$

for the Artin–Schreier cover
$\pi:Y=\operatorname{Spec}k_1[x][u]/(u^p-u-ax)\to\mathbf A^1_{k_1}$
with $\mathbf F_p$-action $\sigma_c:u\mapsto u+c$. Then
$\mathcal L_{\psi(ax)}$ is lisse of rank one and ramified at infinity
in the sense of [rem-dl-a1-conventions]: the inertia group $I_\infty$
at $\infty\in\mathbf P^1_k$ acts on its geometric generic stalk through
a character of exact order $p$.
