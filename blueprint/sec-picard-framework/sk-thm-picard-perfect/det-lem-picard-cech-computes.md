+++
id = "det-lem-picard-cech-computes"
kind = "lemma"
title = "Leray's theorem for quasi-coherent sheaves"
order = 787
uses = ["det-lem-picard-affine", "det-thm-picard-cech"]
lean = ["AlgebraicGeometry.Scheme.Modules.nonempty_cechComplex_linearEquiv_H_of_isSeparated"]
+++
Let $X$ be separated over an affine base $S=\Spec A$ and let
$\mathfrak U$ be an open affine covering. Then for every quasi-coherent
$\cO_X$-module $\cF$ and every $q\ge0$ there is an isomorphism of
$\Gamma(X,\cO_X)$-modules, hence of $A=\Gamma(S,\cO_S)$-modules (the edge
map of [det-thm-picard-cech] is one)

$$
\Cech^q(\mathfrak U,\cF)\overset{\sim}{\longrightarrow}H^q(X,\cF)
\qquad(q\ge0);
$$

in particular it is $k$-linear when $S=\Spec k$.
