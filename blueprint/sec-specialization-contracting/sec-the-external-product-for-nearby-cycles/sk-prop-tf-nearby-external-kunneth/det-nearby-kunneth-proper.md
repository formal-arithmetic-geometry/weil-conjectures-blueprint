+++
id = "det-nearby-kunneth-proper"
kind = "lemma"
title = "The nearby-cycle Künneth map and proper direct images"
order = 3669
uses = ["det-sp-nearby-cycles-exchanges", "lem-trf-ordinary-kunneth"]
+++
Let $S$ be a strictly henselian trait with separably closed residue field $k$ and geometric generic
point $\bar\eta$, let $A$ be a finite commutative $\ell$-primary ring with $\ell$ invertible on $S$,
and let $R\Psi$ be the nearby cycles of [det-sp-nearby-cycles-exchanges]. For $X,Y$ separated of
finite type over $S$, $L\in D^b_{\mathrm{ctf}}(X_\eta,A)$ and $M\in D^b_{\mathrm{ctf}}(Y_\eta,A)$,
let $\Pi_{L,M}\colon R\Psi_{X/S}L\boxtimes R\Psi_{Y/S}M\to R\Psi_{(X\times_SY)/S}(L\boxtimes M)$ be
the restriction to the special fibre of the map
$R\bar j_{X*}L_{\bar\eta}\boxtimes R\bar j_{Y*}M_{\bar\eta}\to R\bar j_{X\times Y,*}(L_{\bar\eta}\boxtimes M_{\bar\eta})$
defined by the pullback exchanges and the lax tensor map of direct image.

Let $f\colon X\to X_1$ and $g\colon Y\to Y_1$ be proper morphisms of separated finite-type
$S$-schemes. Identify $R(f_s\times g_s)_*(R\Psi_{X/S}L\boxtimes R\Psi_{Y/S}M)$ with
$Rf_{s*}R\Psi_{X/S}L\boxtimes Rg_{s*}R\Psi_{Y/S}M$ by ordinary Künneth
[lem-trf-ordinary-kunneth], and the nearby direct images by the proper exchange of
[det-sp-nearby-cycles-exchanges]. Under these identifications

$$
R(f_s\times g_s)_*\Pi_{L,M}=\Pi_{Rf_{\eta*}L,\,Rg_{\eta*}M}.
$$
