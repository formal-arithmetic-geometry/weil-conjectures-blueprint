+++
id = "prose-10-06"
kind = "hidden"
title = "Local form of the adjunction and gluing"
order = 3219
+++
The geometric computations with finite coefficients in
Section “Torsion coefficients: the strategy” are stated on the pro-étale site
and proved by calculations on the étale site. By
Corollary [sk-cor-pe-finite-tor-comparison], Theorem [sk-thm-pe-direct-image-comparison]
with the formula in [lem-cbc-proetale-extension-zero-comparison], and
Proposition [sk-prop-ctf-finite-comparison], the pro-étale and étale categories
$\Dctf(-,A)$, and the localizing subcategories they generate, are identified compatibly with
pullback, direct image and extension by zero; in particular
$Rf_!=R\bar f_*\circ j_!$ is computed on the étale sites.
Consequently, an adjunction between $Rf_!$ and some functor $G$ on the étale
categories $\Dctf(-_{\mathrm{\acute et}},A)$ transfers to the pro-étale categories
$\Dctf(-_{\mathrm{pro\acute et}},A)$. Indeed, the Hom groups agree by full faithfulness, and
the two functors $Rf_!$ correspond to each other.

By Proposition [sk-prop-ctf-finite-comparison], the functor $f^!$ on
$\Loc(\Dctf(-,\mathbf Z/\ell^n\mathbf Z))$ of Theorem [sk-prop-sf-existence]
is the functor $f^!$ on $D_{\mathrm{class}}$ of
Section “Torsion coefficients: the strategy”, and it preserves $\Dctf$ by
Theorem [sk-prop-sf-rf-shriek-preservation]. Hence, for $f:X\to Y$ smooth of pure
relative dimension $d$, Proposition [sk-prop-cohsm](1) gives
the local form of $Rf_!\dashv f^!$: on an open $U\subset X$ with
$f|_U=p_d\circ e$, where $e:U\to\mathbf A^d_Y$ is étale,

$$
f^!K|_U\simeq e^*p_{d}^*K(d)[2d],
$$

with counit the sum over the fibres of $e$ followed by
the trace map of affine space $\operatorname{Tr}_{p_d}$ tensored with $K$.

Since a right adjoint is unique up to a unique isomorphism preserving the
counit, these counits on charts agree on overlaps with the counit of
$Rf_!\dashv f^!$. For towers we argue in the other
direction and glue $f^!$ from models on charts. For this we use the
triangle for an open cover $X=U\cup V$ and $N\in\Dctf(X_{\mathrm{pro\acute et}},\mathbf Z/\ell^n\mathbf Z)$:

$$
j_{U\cap V!}(N|_{U\cap V})
 \xrightarrow{\ (1,-1)\ }
 j_{U!}(N|_U)\oplus j_{V!}(N|_V)
 \xrightarrow{\ (1,1)\ }N\longrightarrow{} .
$$

Suppose that $H\in\Dctf(X_{\mathrm{pro\acute et}},\mathbf Z/\ell^n\mathbf Z)$ and
$\varepsilon:Rf_!H\to K$ restrict to pairs that represent
$\operatorname{Hom}(Rf_!(-),K)$ (Definition [sk-def-sp-representing-pair])
on $U$, $V$ and $U\cap V$, where
the restriction of $\varepsilon$ to $U$ is the composite
$R(f|_U)_!(H|_U)=Rf_!j_{U!}(H|_U)\to Rf_!H\to K$. For
$M\in\Dctf(X_{\mathrm{pro\acute et}},\mathbf Z/\ell^n\mathbf Z)$ we apply
$\operatorname{Hom}(-,H)$ and $\operatorname{Hom}(Rf_!(-),K)$ to
this triangle with $N=M$. The maps
$b\mapsto\varepsilon\circ Rf_!(b)$ form a morphism between the two long exact
sequences, which is bijective on the terms coming from $U$, $V$ and $U\cap V$.
By the five lemma it is bijective on $\operatorname{Hom}(M,H)$, and so
$(H,\varepsilon)$ represents $\operatorname{Hom}(Rf_!(-),K)$. Such a pair is
unique up to a unique isomorphism compatible with $\varepsilon$, and hence
$H\simeq f^!K$ compatibly with the counits. In Section “Smooth purity with $\ell$-adic coefficients” we use this gluing to realize
the compatible counits with finite coefficients as a single map of towers.

On a vector bundle, the choice of a local trivialization transports
the trace map of affine space to a trace map, and since these maps
do not depend on the trivialization, they glue to a global map. Deformation to the
normal bundle reduces the dualizing complex of a smooth morphism to that of a
vector bundle, and so this is the model case of the orientation below.
