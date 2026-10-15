+++
id = "det-geo-open-finiteness-base-change"
kind = "lemma"
title = "Base change for open direct images over a field"
uses = ["thm-fin-deligne-generic-open", "cor-fin-deligne-open-finite-coefficients", "lem-fin-coefficients-forgetful-direct-image", "sbc-def-base-change-map", "thm-constructible-serre"]
+++
Let $k$ be a field, let $\ell\ne\operatorname{char}(k)$, let $\Lambda$ be a
finite ring with $\ell^r\Lambda=0$ for some $r\ge1$, and let
$j:X\hookrightarrow Y$ be an open immersion of finite-type $k$-schemes. Let
$T$ be a finite-type $k$-scheme, write $X_T=X\times_kT$, $Y_T=Y\times_kT$, let
$j_T:X_T\hookrightarrow Y_T$ be the base change of $j$, and let
$g_X:X_T\to X$, $g_Y:Y_T\to Y$ be the projections. Then for every
$K\in\Dbc(X_{\mathrm{ét}},\Lambda)$ the derived base-change map of
[sbc-def-base-change-map]

$$
\operatorname{BC}(K):g_Y^*Rj_*K\longrightarrow Rj_{T,*}\,g_X^*K
\quad\text{in }D^+((Y_T)_{\mathrm{ét}},\Lambda)
$$

is an isomorphism. In particular $Rj_{T,*}g_X^*K$ is bounded constructible.
