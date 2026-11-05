+++
id = "definition-pushforward-correspondence--1"
kind = "definition"
title = "Pushforward of a correspondence (1)"
name_showing = false
order = 923001
aliases = ["bp-r280-1"]
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
