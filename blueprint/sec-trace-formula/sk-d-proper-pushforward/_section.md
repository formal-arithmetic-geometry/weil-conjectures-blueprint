+++
id = "sk-d-proper-pushforward"
kind = "definition"
title = "Pushforward of a correspondence"
order = 2616
uses = ["sk-d-corr", "sk-d-integral", "sk-d-six", "sk-d-trace-class"]
lean = ["AlgebraicGeometry.ProEtale.ProperPushforwardDiagram"]
tags = ["sketch"]
+++
Let $c=(c_1,c_2):C\to X\times X$ be a correspondence on $X$, with fixed locus
$F_c$, and let $K\in\Dctf(X,A)$.
Let $f:X\to Y$ and $g:C\to D$ be proper morphisms, and let
$b=(b_1,b_2):D\to Y\times Y$ be a correspondence with $b_ig=fc_i$ for
$i=1,2$. Put $K'=Rf_*K\in\Dctf(Y,A)$. For a cohomological correspondence $u$
on $(X,K)$, the *pushed correspondence* $u'=[f,g]_!u:b_2^*K'\to b_1^!K'$ is
$u'=\delta\,Rg_*u\,\gamma$, built from an ordinary half

$$
\gamma:b_2^*Rf_*K\xrightarrow{\eta_g}
Rg_*c_2^*f^*Rf_*K\xrightarrow{\varepsilon_f}Rg_*c_2^*K
$$

and an exceptional half $\delta:Rg_*c_1^!K\to b_1^!Rf_*K$, adjoint to

$$
Rb_{1!}Rg_*c_1^!K\simeq Rf_*Rc_{1!}c_1^!K
\xrightarrow{Rf_*\varepsilon_{c_1}}Rf_*K.
$$

The map $g$ induces a proper morphism $h:F_c\to F_b$ of fixed loci, and
$h_*:H^0(F_c,\omega_{F_c})\to H^0(F_b,\omega_{F_b})$ denotes the map given by
the ordinary unit, proper pushforward and the exceptional counit.
