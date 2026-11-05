+++
id = "lemma-injectivity-base-change-map-degree--1"
kind = "lemma"
title = "Injectivity of the base change map in degree $q$ (1)"
name_showing = false
order = 673001
aliases = ["bp-r202-1"]
lean = ["AlgebraicGeometry.Etale.mono_baseChangeHomologyMap"]
+++
Let $\Lambda$ be a commutative ring, $g:Y'\to Y$ a morphism of schemes,
and $q\in\mathbf Z$ with $q\geq1$. For a cartesian square

$$
\begin{CD}
Z' @>{g'}>> Z\\
@V{f'}VV @VV{f}V\\
Y' @>{g}>> Y
\end{CD}
$$

and a sheaf $M$ of $\Lambda$-modules on $Z_{\acute{e}t}$, write

$$
b_M^r:H^r(g^*Rf_*(M[0]))\longrightarrow H^r(Rf'_*g'^*(M[0]))
$$

for the map on cohomology induced by
[definition-derived-base-change-map]. Since inverse image is exact, its
source and target are written $g^{-1}R^rf_*M$ and
$R^rf'_*g'^{-1}M$.

Suppose that $b_M^{q-1}$ is an isomorphism for every such square with
$f$ qcqs and every sheaf $M$ of $\Lambda$-modules. Then $b_M^q$ is
injective for every such square with $f$ qcqs and every $M$.
