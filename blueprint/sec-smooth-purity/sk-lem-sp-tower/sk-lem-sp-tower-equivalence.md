+++
id = "det-sp-normalized-equivalence"
kind = "proposition"
title = "Integral constructible complexes are normalized constructible towers"
order = 3011
uses = ["det-sp-reduction-tower-normalized", "lem-coef-normalized-dvr-effectivity", "def-pe-derived-complete"]
+++
The reduction functor
$\operatorname{red}_T:D(T_{\mathrm{proét}},\mathcal O_E)\to D(\operatorname{Tow}(T,\mathcal O_E))$,
$M\mapsto(M/\ell^n)_n$, is left adjoint to
$R\varprojlim:D(\operatorname{Tow}(T,\mathcal O_E))\to D(T_{\mathrm{proét}},\mathcal O_E)$
(Bhatt–Scholze, Lemma 3.5.7). The unit is an isomorphism on derived complete
complexes [def-pe-derived-complete] and the counit is an isomorphism on normalized towers, so the
adjunction restricts to mutually inverse equivalences

$$
\operatorname{red}_T:\Dbc(T,\mathcal O_E)
\ \rightleftarrows\
\Dctf(T_{\mathrm{proét}},\mathcal O_E/\ell^\bullet)_{\mathrm{norm}}
:R\varprojlim_n .
$$
