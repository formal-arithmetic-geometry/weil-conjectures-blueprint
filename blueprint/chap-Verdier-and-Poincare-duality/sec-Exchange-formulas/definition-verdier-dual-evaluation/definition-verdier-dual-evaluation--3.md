+++
id = "definition-verdier-dual-evaluation--3"
kind = "lemma"
title = "Verdier dual and evaluation (3)"
name_showing = false
order = 827003
aliases = ["bp-r247-3"]
lean = ["AlgebraicGeometry.Etale.exists_distTriang_derivedHom_left"]
uses = ["definition-verdier-dual-evaluation--1", "definition-verdier-dual-evaluation--2"]
+++
Let $X$ be a scheme and $\mathcal A$ a symmetric monoidal closed
Grothendieck abelian coefficient category whose tensor product is additive
in each variable and which has functorial flat resolutions. For
$M\in D(X_{\acute{e}t},\mathcal A)$ and a distinguished triangle

$$
K'\xrightarrow{u}K\xrightarrow{v}K''\longrightarrow K'[1],
$$

there is a morphism $w$ for which

$$
\cHom(K'',M)\xrightarrow{\cHom(v,M)}\cHom(K,M)
\xrightarrow{\cHom(u,M)}\cHom(K',M)
\xrightarrow{w}\cHom(K'',M)[1]
$$

is distinguished. In particular, for a finite commutative coefficient
ring $\Lambda$ and a structure morphism $a_X:X\to s$ admitting a
compactification, take $M=\omega_X$ as in
[definition-verdier-dual-evaluation--1]. The first two Verdier-dual maps
then extend to a distinguished triangle

$$
\mathbb D_XK''\longrightarrow\mathbb D_XK\longrightarrow
\mathbb D_XK'\longrightarrow(\mathbb D_XK'')[1]
$$

on the étale site. The connecting morphism is asserted to exist; this
statement does not choose a shift isomorphism for $\mathbb D_X$.
