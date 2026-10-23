+++
id = "det-sp-integral-adjunction-bijection"
kind = "lemma"
title = "The derived limit of the tower adjunction is an integral adjunction"
order = 3025
uses = ["det-sp-integral-direct-image-tower", "det-sp-normalized-equivalence", "det-sp-tower-gluing", "det-sp-tower-gamma"]
+++
For $K\in\Dbc(Y,\mathcal O_E)$ the tower $f_\bullet^!\operatorname{red}_YK$ is normalized
constructible, so
$H_{f,\mathcal O_E}(K)=R\varprojlim_nf^!_{\mathcal O_E/\ell^n}(K/\ell^n)\in\Dbc(X,\mathcal O_E)$
and $\operatorname{red}_XH_{f,\mathcal O_E}(K)\simeq f_\bullet^!\operatorname{red}_YK$. For
$M\in\Dbc(X,\mathcal O_E)$ there are bijections, natural in $M$ and $K$,

$$
\operatorname{Hom}(Rf_{!,\mathcal O_E}M,K)\simeq\operatorname{Hom}(Rf_{!,\bullet}\operatorname{red}_XM,\operatorname{red}_YK)
\simeq\operatorname{Hom}(\operatorname{red}_XM,f_\bullet^!\operatorname{red}_YK)\simeq\operatorname{Hom}(M,H_{f,\mathcal O_E}(K)),
$$

so $Rf_{!,\mathcal O_E}\dashv H_{f,\mathcal O_E}$, with unit and counit the derived
limits of the tower unit and counit, whose reductions are the finite units and
counits. Moreover
$\gamma_{f,\mathcal O_E}^H(K)=R\varprojlim\gamma_{f,\bullet}(\operatorname{red}_YK):
f^*_{\mathcal O_E}K(d)[2d]\xrightarrow{\sim}H_{f,\mathcal O_E}(K)$ is an isomorphism.
