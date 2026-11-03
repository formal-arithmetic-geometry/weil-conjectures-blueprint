+++
id = "det-prop-closed-adjoint-constructible"
kind = "proposition"
title = "Exceptional inverse image along a closed immersion"
order = 2770
uses = ["sk-lem-formal-closed-support", "sk-prop-open-coefficients", "sk-prop-sf-existence"]
+++
Let $\Lambda=E$ or $\Qlb$ and let $i:Z\hookrightarrow X$ be a closed immersion,
with open complement $j:U\hookrightarrow X$. Recall that the functor
$R\underline\Gamma_Z$ of sections with support in $Z$ is a functor
$D(X_{\mathrm{proét}},\Lambda)\to D(Z_{\mathrm{proét}},\Lambda)$ right adjoint to
$i_*\colon D(Z_{\mathrm{proét}},\Lambda)\to D(X_{\mathrm{proét}},\Lambda)$
([sk-lem-formal-closed-support](1)), and that it sits in the triangle in
$D(X_{\mathrm{proét}},\Lambda)$

$$
i_*R\underline\Gamma_ZK\longrightarrow K\longrightarrow Rj_*j^*K
\longrightarrow i_*R\underline\Gamma_ZK[1].
$$

For $K\in\Dbc(X,\Lambda)$ there is an isomorphism
$i^!K\simeq R\underline\Gamma_ZK$ in $\Loc(\Dbc(Z,\Lambda))$, natural in $K$.
In particular $i^!$ maps $\Dbc(X,\Lambda)$ into $\Dbc(Z,\Lambda)$.
