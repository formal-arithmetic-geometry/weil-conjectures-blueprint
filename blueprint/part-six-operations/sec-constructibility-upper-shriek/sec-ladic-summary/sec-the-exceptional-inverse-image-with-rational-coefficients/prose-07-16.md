+++
id = "prose-07-16"
kind = "hidden"
title = "The exceptional inverse image with rational coefficients"
order = 362
+++
The argument of Section [sec-ctf-finite-geometric-restriction] applies. Locally
$f^!$ is $i^!p^!$ for a projection $p:\mathbf A^d_V\to V$ and a closed
immersion $i$. By Proposition [sk-prop-p1-adjunction-rational], the
adjunction $j_!\dashv j^*$ for $\mathbf A^1_V\subset\mathbf P^1_V$ and
Proposition [sk-lem-sf-mate] applied $d$ times, we get
$p^!\simeq p^*(d)[2d]$, which preserves $\Dbc$. For
$i:Z\hookrightarrow X$ with complement $j$, the local cohomology functor
$R\underline\Gamma_Z$ is right adjoint to $i_*=Ri_!$
(Lemma [sk-lem-formal-closed-support](1)), so $i^!\simeq R\underline\Gamma_Z$, and the localization triangle

$$
i_*R\underline\Gamma_ZK\longrightarrow K\longrightarrow Rj_*j^*K
\longrightarrow i_*R\underline\Gamma_ZK[1]
$$

shows that $i^!K\in\Dbc(Z,\Lambda)$ for $K\in\Dbc(X,\Lambda)$, since the
third term is in $\Dbc$ by Proposition [sk-prop-open-coefficients] and
$i^*i_*=\mathrm{id}$.
