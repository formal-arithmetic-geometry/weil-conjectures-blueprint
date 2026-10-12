+++
id = "lem-sf-tensor-hom"
kind = "lemma"
title = "Tensor–Hom form of the exchange"
order = 2507
uses = ["def-sf-datum", "def-sf-pf", "def-trf-admissibility", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-inverse-image", "fix-lem-tensor-adjunction", "fix-prop-adjunctions"]
+++
In the setting of [def-sf-datum], let $f:X\to Y$ be a separated
finite-type morphism, with $Rf^!$ the constructible exceptional inverse image
of [def-weil-exceptional-inverse-image] (no admissibility datum is assumed;
every such $f$ is exceptionally admissible in the sense of
[def-trf-admissibility]), $M\in D^b_{ctf}(X,\Lambda)$ and
$N\in D^b_{ctf}(Y,\Lambda)$. Then there is a canonical isomorphism

$$
Rf_*R\mathcal H om_X(M,f^!N)\xrightarrow{\ \sim\ }
R\mathcal H om_Y(Rf_!M,N),
$$

natural in $M$ and $N$ and compatible with finite reduction, scalar
extension, and shifts.
