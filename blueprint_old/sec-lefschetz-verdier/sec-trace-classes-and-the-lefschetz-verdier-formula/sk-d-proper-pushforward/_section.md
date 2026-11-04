+++
id = "sk-d-proper-pushforward"
kind = "definition"
title = "Pushforward of a correspondence"
order = 561
uses = ["sk-d-corr", "sk-d-integral", "sk-d-six", "sk-d-trace-class"]
tags = ["sketch"]
+++
Let $f:X\to Y$ and $g:C\to C'$ be proper morphisms, and let
$c'=(c'_1,c'_2):C'\to Y\times Y$ be a correspondence with $c'_ig=fc_i$ for
$i=1,2$. Put $K'=Rf_*K\in D^b_{\mathrm{ctf}}(Y,A)$. For a cohomological
correspondence $u$ on $(X,K)$, the *pushforward*
$u':c_2'^*K'\to c_1'^!K'$ of $u$ is the composite
$u'=\beta\,Rg_*u\,\alpha$, where $\alpha$ is built from the unit and counit
of $(\,)^*\dashv R(\,)_*$,

$$
\alpha:c_2'^*Rf_*K\xrightarrow{\eta_g}
Rg_*c_2^*f^*Rf_*K\xrightarrow{\varepsilon_f}Rg_*c_2^*K,
$$

and $\beta:Rg_*c_1^!K\to c_1'^!Rf_*K$ is built from the counit of
$R(\,)_!\dashv(\,)^!$: it is adjoint to

$$
Rc'_{1!}Rg_*c_1^!K\simeq Rf_*Rc_{1!}c_1^!K
\xrightarrow{Rf_*\varepsilon_{c_1}}Rf_*K.
$$

The map $g$ induces a proper morphism $h:\Fix(c)\to \Fix(c')$ of fixed loci,
and $h_*:H^0(\Fix(c),\omega_{\Fix(c)})\to H^0(\Fix(c'),\omega_{\Fix(c')})$ denotes the
map given by the ordinary unit, proper pushforward and the exceptional
counit.
