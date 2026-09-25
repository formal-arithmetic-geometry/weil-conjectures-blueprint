+++
id = "prop-trf-exceptional-kunneth"
kind = "theorem"
title = "Exceptional Kunneth; the $\\alpha$ map"
order = 2226
tags = ["latex:proposition"]
uses = ["def-sf-kv-maps", "def-trf-admissibility", "lem-sf-triangle-two-out-of-three", "lem-trf-devissage-generation", "lem-trf-ordinary-kunneth", "thm-pur-affine-line-purity"]
+++
For $i=1,2$, let $f_i:X_i\to Y_i$ be morphisms of separated
finite-type schemes satisfying the
exceptional-adjoint admissibility of
[def-trf-admissibility], and let $L_i\in D^b_{ctf}(Y_i,A)$. The
canonical comparison of [def-sf-kv-maps] (ii), formed with the geometric operations,

$$
\alpha:f_1^!L_1\boxtimes_A^{\mathrm L} f_2^!L_2
\longrightarrow
(f_1\times f_2)^!\bigl(L_1\boxtimes_A^{\mathrm L} L_2\bigr)
$$

is an isomorphism, natural in the $L_i$.

## Proof

First, shriek Kunneth: by $!$-base change and the projection formula
for the exceptional adjoint pair of [def-trf-admissibility], the
comparison

$$
(f_1\times f_2)_!\bigl(f_1^!L_1\boxtimes_A^{\mathrm L} f_2^!L_2\bigr)
\xrightarrow{\ \sim\ }
(f_1)_!f_1^!L_1\boxtimes_A^{\mathrm L}(f_2)_!f_2^!L_2
$$

is invertible. Evaluating it on the $f_i^!L_i$ and composing with the
two exceptional counits of [def-trf-admissibility] produces a map
to $L_1\boxtimes_A^{\mathrm L}L_2$; the exceptional adjoint of this
composite defines $\alpha$.

It remains to see that $\alpha$ is invertible. For a constant auxiliary
coefficient, smooth maps are handled by smooth purity with compatibility
of the smooth trace under base change [thm-pur-affine-line-purity],
and closed immersions by localization together with the
open-product base change, which is the case $Q=\underline A_Z$ of
[lem-trf-ordinary-kunneth]. An affine factorization of a general
$f_i$ into a closed immersion followed by a smooth projection
therefore gives the local case, and the finite-pushforward and
open-localization reductions together with the generation
[lem-trf-devissage-generation] and the two-out-of-three property
[lem-sf-triangle-two-out-of-three] remove the
constant-coefficient restriction. Thus $\alpha$ is an
isomorphism.
