+++
id = "sk-lem-picard-cech-computes"
kind = "lemma"
title = "Leray's theorem for quasi-coherent sheaves"
order = 706
uses = ["sk-def-av-jacobian", "sk-lem-picard-affine", "sk-thm-picard-cech"]
lean = ["AlgebraicGeometry.Scheme.Modules.nonempty_cechComplex_linearEquiv_H_of_isSeparated"]
tags = ["sketch"]
+++
Let $X$ be separated over an affine base $S=\Spec A$ and let
$\mathfrak U$ be an open affine covering. Then for every quasi-coherent
$\cO_X$-module $\cF$ and every $q\ge0$ there is an isomorphism of
$\Gamma(X,\cO_X)$-modules, hence of $A=\Gamma(S,\cO_S)$-modules (the edge
map of [sk-thm-picard-cech] is one)

$$
\Cech^q(\mathfrak U,\cF)\overset{\sim}{\longrightarrow}H^q(X,\cF)
\qquad(q\ge0);
$$

in particular it is $k$-linear when $S=\Spec k$.
