+++
id = "sk-prop-sp-integral-adjunction"
kind = "proposition"
title = "The normalized model of the integral adjunction"
order = 1827
uses = ["sk-prop-sp-tower-geometric", "sk-lem-sp-tower", "sk-prop-sf-existence", "sk-prop-sp-unique-adjoint"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$ and $E/\Ql$ finite.
For $K\in\Dbc(Y,\mathcal O_E)$ the tower $f_\bullet^!\operatorname{red}_YK$ of
[sk-prop-sp-tower-geometric] is normalized; its derived limit defines the
functor $H_{f,\mathcal O_E}:\Dbc(Y,\mathcal O_E)\to\Dbc(X,\mathcal O_E)$,

$$
H_{f,\mathcal O_E}(K):=R\varprojlim_n f_{\mathcal O_E/\ell^n}^!(K/\ell^n)\in\Dbc(X,\mathcal O_E).
$$

The tower unit and counit make $H_{f,\mathcal O_E}$ a right adjoint of
$Rf_{!,\mathcal O_E}$ on $\Dbc(-,\mathcal O_E)$. Consequently there is a unique
counit-preserving isomorphism $H_{f,\mathcal O_E}\simeq f_{\mathcal O_E}^!$ of
functors $\Dbc(Y,\mathcal O_E)\to\Dbc(X,\mathcal O_E)$, where
$f_{\mathcal O_E}^!$ is the right adjoint of [sk-prop-sf-existence].
