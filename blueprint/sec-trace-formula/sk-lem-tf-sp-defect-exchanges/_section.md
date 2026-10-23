+++
id = "sk-lem-tf-sp-defect-exchanges"
kind = "lemma"
title = "Exchanges for the defect"
order = 3574
uses = ["sk-lem-tf-sp-constant-family", "sk-lem-tf-sp-dnc-functorial"]
tags = ["sketch"]
+++
Let $X$ be a separated finite-type $k$-scheme and $i\colon Z\hookrightarrow X$ a closed subscheme
with ideal $I$, with deformation $\mathcal D_ZX$ and special fibre $N_ZX$ as in
[sk-lem-tf-sp-dnc-functorial]. The quotient killing $I$ and every $a/t$ gives a closed immersion
$\widetilde e\colon Z\times S\hookrightarrow\mathcal D_ZX$; its special fibre
$e\colon Z\hookrightarrow N_ZX$ is the zero section. For $L$ on $X$ with pullback $L_\eta$ to the generic fibre $X_\eta$
of $\mathcal D_ZX$, the specialization functor is
$\operatorname{Sp}_{X,Z}(L)=R\Psi_{\mathcal D_ZX}(L_\eta)$, with the nearby cycles of
[sk-lem-tf-sp-constant-family]. Pullback exchange along $\widetilde e$, followed by the inverse of
[sk-lem-tf-sp-constant-family], gives a natural transformation of functors
$D^b_c(X_{\mathrm{\acute et}},A)\to D^b_c(Z_{\mathrm{\acute et}},A)$,

$$
\epsilon_{X,Z}(L):e^*\operatorname{Sp}_{X,Z}(L)
\longrightarrow R\Psi_{Z\times S}((i^*L)_\eta)\xrightarrow{\sim}i^*L,
\tag{1}
$$

and the *defect* $C_{X,Z}(L)=\operatorname{cofib}(\epsilon_{X,Z}(L))$ in
$D^b_c(Z_{\mathrm{\acute et}},A)$, computed in an enhancement, is an exact functor.

Let $f:X'\to X$ be a morphism of separated finite-type $k$-schemes, let $Z'=f^{-1}Z$
schematically, and let $f_Z:Z'\to Z$ be the restriction of $f$. There are isomorphisms in
$D^b_c(Z_{\mathrm{\acute et}},A)$ and $D^b_c(Z'_{\mathrm{\acute et}},A)$

$$
\begin{aligned}
C_{X,Z}(Rf_*L')&\simeq Rf_{Z*}C_{X',Z'}(L') &&(f\text{ proper}),\\
C_{X',Z'}(f^*L)&\simeq f_Z^*C_{X,Z}(L) &&(f\text{ smooth}).
\end{aligned}
$$

Also $C_{X,Z}(i_*M)=0$ for every $M\in D^b_c(Z_{\mathrm{\acute et}},A)$. Consequently, writing
$j:X\setminus Z\hookrightarrow X$,

$$
C_{X,Z}(j_!j^*L)\xrightarrow{\sim}C_{X,Z}(L).
$$
