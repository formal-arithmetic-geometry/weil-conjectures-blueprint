+++
id = "fix-lem-tensor-adjunction"
kind = "lemma"
title = "Tensor–adjunction form of the exchange"
order = 2456
uses = ["def-fix-six-functor-datum", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-adjoint-admissibility", "fix-prop-adjunctions", "fix-prop-projection-formula", "lemma-weil-pbc-geometric-stalk-conservative", "thm-weil-pbc-site-comparison"]
+++
In the six-functor datum of
[def-fix-six-functor-datum], let $f$ be
exceptionally
admissible, and let $M\in D^b_{ctf}(X,\Lambda)$ and
$N\in D^b_{ctf}(Y,\Lambda)$. There is a canonical isomorphism

$$
Rf_*R\mathcal Hom_X\bigl(M,f^!N\bigr)
\xrightarrow{\ \sim\ }
R\mathcal Hom_Y\bigl(Rf_!M,N\bigr),
$$

natural in $M$ and $N$, compatible with finite reduction, scalar
extension, and shifts.
