+++
id = "sk-prop-diagonal-tower"
kind = "proposition"
title = "The $\\ell$-adic cycle class of the diagonal"
order = 2410
uses = ["sk-lem-geo-cartier", "sk-lem-geo-p1-cohomology", "sk-prop-geo-p1-adjunction"]
tags = ["sketch"]
+++
Let $q:\mathbf P^1_Y\to Y$ be the projection and
$\Delta:\mathbf P^1_Y\hookrightarrow\mathbf P^1_Y\times_Y\mathbf P^1_Y$ the
diagonal. There is a morphism

$$
\delta_{\mathcal O_E}:\Delta_*\mathcal O_{E,\mathbf P^1_Y}
\longrightarrow
\mathcal O_{E,\mathbf P^1_Y\times_Y\mathbf P^1_Y}(1)[2]
$$

in $D((\mathbf P^1_Y\times_Y\mathbf P^1_Y)_{\mathrm{proét}},\mathcal O_E)$ whose
reductions are the cycle classes of $\Delta$ with torsion coefficients
([sk-lem-geo-cartier]), and a trace
$\operatorname{Tr}_q:Rq_*\mathcal O_{E,\mathbf P^1_Y}(1)[2]\to\mathcal O_{E,Y}$
in $D(Y_{\mathrm{proét}},\mathcal O_E)$ lifting the torsion traces of
[sk-lem-geo-p1-cohomology]. The two integration identities of
[sk-prop-geo-p1-adjunction],

$$
\operatorname{Tr}_{p_i}\circ Rp_{i*}(\delta_{\mathcal O_E})
=1_{\mathcal O_{E,\mathbf P^1_Y}}\qquad(i=1,2),
$$

hold in $D((\mathbf P^1_Y)_{\mathrm{proét}},\mathcal O_E)$ for these morphisms,
with
$Rp_{i*}\colon D((\mathbf P^1_Y\times_Y\mathbf P^1_Y)_{\mathrm{proét}},\mathcal O_E)\to D((\mathbf P^1_Y)_{\mathrm{proét}},\mathcal O_E)$,
where $p_1,p_2$ are the two projections of
$\mathbf P^1_Y\times_Y\mathbf P^1_Y$, each a projective line over
$\mathbf P^1_Y$. Extending scalars gives $E$- and $\Qlb$-linear morphisms
$\delta_\Lambda$ and $\operatorname{Tr}_q$ with the same identities. All of
these are compatible with base change along separated morphisms of finite type
$Y'\to Y$ between schemes of the standing setting.
