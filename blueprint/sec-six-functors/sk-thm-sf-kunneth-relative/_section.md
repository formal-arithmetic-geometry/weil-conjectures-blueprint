+++
id = "sk-thm-sf-kunneth-relative"
kind = "theorem"
title = "Relative product theorem"
order = 2513
uses = ["sk-lem-sf-mate", "sk-prop-sf-cbc", "sk-prop-sf-comp-proper", "sk-prop-sf-pf-coherence", "sk-rem-sf-pf-done", "sk-thm-sf-comp-composition"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerShriek_externalProduct"]
tags = ["sketch"]
+++
Let $B$ be a separated finite-type $k$-scheme, let $f:X\to B$ and $g:Y\to B$ be
separated of finite type, let $p,q$ be the projections of $X\times_BY$, so
that $f\times_Bg=g\circ q=f\circ p$, and put
$K\boxtimes L=p^*K\otimes^L_\Lambda q^*L$ for $K\in\Dctf(X,\Lambda)$,
$L\in\Dctf(Y,\Lambda)$. Define the *relative Künneth map*
$\kappa^{\mathrm{rel}}_{K,L}$ as the composite

$$
\begin{aligned}
R(f\times_Bg)_!\bigl(K\boxtimes L\bigr)
&\xrightarrow{\ \alpha_{g,q}^{-1}\ }Rg_!Rq_!\bigl(p^*K\otimes^L q^*L\bigr)
\xrightarrow{\ Rg_!(\operatorname{PF}_{q,p^*K,L})^{-1}\ }
Rg_!\bigl(Rq_!p^*K\otimes^L L\bigr)\\
&\xrightarrow{\ Rg_!(\operatorname{Ex}_!^{-1}\otimes1)\ }
Rg_!\bigl(Lg^*Rf_!K\otimes^L L\bigr)
\xrightarrow{\ Rg_!(\sigma)\ }
Rg_!\bigl(L\otimes^L Lg^*Rf_!K\bigr)\\
&\xrightarrow{\ (\operatorname{PF}_{g,L,Rf_!K})^{-1}\ }
Rg_!L\otimes^L_\Lambda Rf_!K
\xrightarrow{\ \sigma\ }Rf_!K\otimes^L_\Lambda Rg_!L ,
\end{aligned}
$$

where $\alpha_{g,q}$ is the composition isomorphism of
[sk-thm-sf-comp-composition], $\operatorname{PF}$ the projection
transformation and $\operatorname{Ex}_!:Lg^*Rf_!\to Rq_!Lp^*$ the exchange
transformation of [sk-def-sf-exchanges] for the Cartesian square
$(p,q,f,g)$, and $\sigma$ the symmetry of $\otimes^L$; the second variable
$Rf_!K$ of $\operatorname{PF}_{g,L,Rf_!K}$ lies in $\Dctf(B,\Lambda)$, as the
typing of [sk-def-sf-exchanges] requires, by [sk-thm-sf-ctf-stability]. Then every arrow is an isomorphism
([sk-thm-sf-comp-composition], [sk-rem-sf-pf-done],
[sk-prop-sf-cbc]), so

$$
\kappa^{\mathrm{rel}}_{K,L}:R(f\times_Bg)_!\bigl(K\boxtimes L\bigr)\xrightarrow{\ \sim\ }
Rf_!K\otimes^L_\Lambda Rg_!L
$$

is an isomorphism in the ambient category $D^+(B,\Lambda)$, natural in $K$ and
$L$, compatible with finite reduction, scalar extension, and with the
identifications $Rf_!\cong Rf_*$ for proper $f$. Moreover
$\kappa^{\mathrm{rel}}$ is coherent: (i) *symmetry* — under the swap
$X\times_BY\cong Y\times_BX$ and $\sigma$, $\kappa^{\mathrm{rel}}_{L,K}$
corresponds to $\sigma\circ\kappa^{\mathrm{rel}}_{K,L}$ (with the Koszul
signs of $\sigma$); (ii) *triple products* — for a third
$h:W\to B$ and $M\in\Dctf(W,\Lambda)$ the two iterated isomorphisms
$R(f\times_Bg\times_Bh)_!(K\boxtimes L\boxtimes M)\cong
Rf_!K\otimes^LRg_!L\otimes^LRh_!M$ agree after the associativity of
$\otimes^L$; (iii) *base change* — for $b:B'\to B$, $Lb^*$ of
$\kappa^{\mathrm{rel}}_{K,L}$ is $\kappa^{\mathrm{rel}}$ of the base-changed
data, through $\operatorname{Ex}_!$ for $f$, $g$, $f\times_Bg$ and the
monoidality of $Lb^*$; (iv) *projection formula* — for $Y=B$,
$g=\mathrm{id}_B$ one has $\kappa^{\mathrm{rel}}_{K,L}=
\operatorname{PF}_{f,K,L}^{-1}$. For $B=\mathrm{Spec}\,k$ and closed
immersions $i_Z:Z\hookrightarrow X$, $i_W:W\hookrightarrow Y$ it gives the
compact-support product on the closed subschemes
$\RG_c(Z,i_Z^*K)\otimes^L_\Lambda\RG_c(W,i_W^*L)\cong
\RG_c\bigl(Z\times_kW,(i_Z\times i_W)^*(K\boxtimes L)\bigr)$; cohomology with
supports $\RG_Z(X,K)=\RG(Z,Ri_Z^!K)$ is a different object and is not
asserted here.
