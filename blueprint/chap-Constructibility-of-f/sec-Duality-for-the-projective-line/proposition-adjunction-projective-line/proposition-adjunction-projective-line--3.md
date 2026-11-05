+++
id = "proposition-adjunction-projective-line--3"
kind = "proposition"
title = "Base change for the counit"
order = 553004
aliases = ["bp-r167-3"]
lean = ["AlgebraicGeometry.Etale.projectiveLineCounit_baseChange"]
uses = ["proposition-adjunction-projective-line--1", "proposition-composition-base-change-rf-shriek"]
+++
Let $\Lambda$ be a finite commutative ring with a normalized Kummer class
and its Tate twists. Let $g:S'\to S$ be a morphism of schemes on which the
exponent of $\Lambda$ is invertible. Write $p:\mathbf P^1_S\to S$ and
$p':\mathbf P^1_{S'}\to S'$ for the projections, and
$g':\mathbf P^1_{S'}\to\mathbf P^1_S$ for the induced map. For
$K\in D(S_{\acute{e}t},\Lambda)$, let

$$
c_K:g'^*\bigl(p^*K(1)[2]\bigr)
\xrightarrow{\ \sim\ }p'^*g^*K(1)[2]
$$

be the canonical isomorphism, obtained by commuting pullback with the
Tate twist and shift and then composing inverse images. If $\varepsilon$
and $\varepsilon'$ are the trace counits of
[proposition-adjunction-projective-line--1], then

$$
\varepsilon'_{g^*K}\circ Rp'_!(c_K)\circ
\operatorname{Ex}_{!,p^*K(1)[2]}
=g^*(\varepsilon_K),
$$

where $\operatorname{Ex}_!:g^*Rp_!\to Rp'_!g'^*$ is compact-support base
change. Thus the trace counits are compatible with every base change.
