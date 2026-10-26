+++
id = "lem-trf-exceptional-internal-hom-exchange"
kind = "lemma"
title = "Exceptional internal Hom versus exceptional pullback"
lean = ["CategoryTheory.Verdier.isIso_exceptionalHomMap_of_isIso", "CategoryTheory.Verdier.exceptionalHomMap"]
order = 3457
uses = ["def-trf-admissibility", "def-trf-coefficient-conventions", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-tor-amplitude", "prop-functor-package"]
+++
Fix the coefficient
conventions, $A=A_{E,n}$, and let $c:C\to Z$ be a separated
finite-type morphism of finite-type $k$-schemes which is admissible at
$A$ ([def-trf-admissibility]). For
$M,N\in D^b_{ctf}(Z,A)$ the canonical comparison

$$
R\mathcal Hom_A\bigl(c^*M,c^!N\bigr)\xrightarrow{\ \sim\ }
c^!R\mathcal Hom_A(M,N)
$$

is an isomorphism, natural in $M$ and $N$. Its first variable is
required to be an ordinary pullback and its second an exceptional one;
the analogous statement with $c^!$ in the first variable is false, as
recorded in [def-trf-admissibility].
