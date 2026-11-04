+++
id = "prose-09-09"
kind = "hidden"
title = "The trace map of affine space (2)"
order = 733
+++
The geometric computations with finite coefficients in
Section [sec-Conventions-2] are stated on the pro-étale site
and proved by calculations on the étale site. By
Corollary [corollary-finite-tor-amplitude-under-comparison], Theorem [theorem-comparison-direct-images]
with (2.10), and
Proposition [proposition-comparison-etale-derived-category], the pro-étale and étale categories
$D^b_{\mathrm{ctf}}(-,A)$, and the localizing subcategories they generate, are identified compatibly with
pullback, direct image and extension by zero. In particular
$Rf_!=R\bar f_*\circ j_!$ is computed on the étale sites.
Consequently, an adjunction between $Rf_!$ and some functor $G$ on the étale
categories $D^b_{\mathrm{ctf}}(-_{\acute{e}t},A)$ transfers to the pro-étale categories
$D^b_{\mathrm{ctf}}(-_{\mathrm{pro}\acute{e}t},A)$. Indeed, the Hom groups agree by full faithfulness, and
the two functors $Rf_!$ correspond to each other.

By Proposition [proposition-comparison-etale-derived-category], the functor $f^!$ on
$\Loc(D^b_{\mathrm{ctf}}(-,\mathbf Z/\ell^n\mathbf Z))$ of Theorem [theorem-existence-exceptional-inverse-image]
is the functor $f^!$ on $D_{\mathrm{class}}$ of
Section [sec-Conventions-2], and it preserves $D^b_{\mathrm{ctf}}$ by
Theorem [theorem-f-shriek-finite-coefficients]. Hence, for $f:X\to Y$ smooth of pure
relative dimension $d$, Proposition [proposition-exceptional-inverse-image-smooth-morphism](1) gives
the local form of $Rf_!\dashv f^!$: on an open $U\subset X$ with
$f|_U=p_d\circ e$, where $e:U\to\mathbf A^d_Y$ is étale,

$$
f^!K|_U\simeq e^*p_{d}^*K(d)[2d],
$$

with counit the sum over the fibres of $e$ followed by
(9.11) tensored with $K$.

Since a right adjoint is unique up to a unique isomorphism preserving the
counit, these counits on charts agree on overlaps with the counit of
$Rf_!\dashv f^!$. With finite coefficients, then, $f^!$ exists first and
the charts describe it. For towers there is no global functor yet, and we
glue $f^!$ from models on charts by a Mayer–Vietoris argument. It uses the
triangle for an open cover $X=U\cup V$ and $N\in D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},\mathbf Z/\ell^n\mathbf Z)$:

$$
j_{U\cap V!}(N|_{U\cap V})
\xrightarrow{\ (1,-1)\ }
j_{U!}(N|_U)\oplus j_{V!}(N|_V)
\xrightarrow{\ (1,1)\ }N\longrightarrow{} .
\tag{9.12}
$$

Suppose that $H\in D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},\mathbf Z/\ell^n\mathbf Z)$ and
$\varepsilon:Rf_!H\to K$ restrict to pairs that represent
$\operatorname{Hom}(Rf_!(-),K)$ (Definition [definition-representing-objects])
on $U$, $V$ and $U\cap V$, where
the restriction of $\varepsilon$ to $U$ is the composite
$R(f|_U)_!(H|_U)=Rf_!j_{U!}(H|_U)\to Rf_!H\to K$. For
$M\in D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},\mathbf Z/\ell^n\mathbf Z)$ we apply
$\operatorname{Hom}(-,H)$ and $\operatorname{Hom}(Rf_!(-),K)$ to
(9.12) with $N=M$. The maps
$b\mapsto\varepsilon\circ Rf_!(b)$ form a morphism between the two long exact
sequences, which is bijective on the terms coming from $U$, $V$ and $U\cap V$.
By the five lemma it is bijective on $\operatorname{Hom}(M,H)$. This means
that $(H,\varepsilon)$ represents $\operatorname{Hom}(Rf_!(-),K)$. Such a
pair is unique up to a unique isomorphism compatible with $\varepsilon$,
so $H\simeq f^!K$ compatibly with the counits. In Section [sec-ell-adic-coefficients-4] we use this gluing to realize
the compatible counits with finite coefficients as a single map of towers.

On a vector bundle, the choice of a local trivialization transports
(9.11) to a trace map. These maps do not
depend on the trivialization, so they glue to a global map. This is the
model case of the orientation below, because deformation to the normal
bundle will reduce the dualizing complex of a smooth morphism to that of a
vector bundle.
