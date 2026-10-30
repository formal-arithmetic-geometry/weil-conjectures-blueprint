+++
id = "sk-lem-sp-finite-existence"
kind = "lemma"
title = "Local computation of the finite Brown adjoint"
order = 2909
uses = ["sk-prop-sf-existence", "sk-lem-geo-affine-local", "sk-prop-sp-et-proet"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$. On
$\Dctf(-_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$, the Brown adjunction
$Rf_!\dashv f^!$ has the following local form. On an open $U\subset X$ with
$f|_U=p_d\circ e$, where $e:U\to\mathbf A^d_Y$ is étale and
$p_d:\mathbf A^d_Y\to Y$ the projection,

$$
f^!K|_U\simeq e^*p_d^*K(d)[2d]\quad\text{in }\Dctf(U_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z),
$$

with counit the sum over the fibres of $e$ followed by the integration
isomorphism
$\operatorname{Tr}_{p_d}:Rp_{d!}(\mathbf Z/\ell^n\mathbf Z)_{\mathbf A^d_Y}(d)[2d]\xrightarrow{\sim}(\mathbf Z/\ell^n\mathbf Z)_Y$
tensored with $K$.

These chart counits agree with the Brown counit on overlaps by uniqueness of
the adjunction comparison. For $X=U\cup V$ and
$N\in\Dctf(X_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$ there is the open-cover triangle

$$
j_{U\cap V!}(N|_{U\cap V})\xrightarrow{\ (1,-1)\ }j_{U!}(N|_U)\oplus j_{V!}(N|_V)
\xrightarrow{\ (1,1)\ }N\longrightarrow,
$$

whose Hom sequences verify the representing property of a glued chart model
([sk-def-sp-representing-pair]); the counit-preserving comparison identifies
that model with the already constructed $f^!$.
