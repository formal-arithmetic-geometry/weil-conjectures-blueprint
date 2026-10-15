+++
id = "fix-cor-verdier-exchange"
kind = "theorem"
title = "Verdier-duality exchange"
order = 2461
tags = ["latex:corollary"]
uses = ["def-fix-six-functor-datum", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "fix-lem-tensor-adjunction", "fix-prop-adjunctions", "thm-sf-comp-composition"]
+++
In the six-functor datum of
[def-fix-six-functor-datum], assume that $f$ and the structure
morphisms $a_X$, $a_Y$ are
exceptionally
admissible, and put

$$
\omega_{Y,\Lambda}=Ra_Y^!\Lambda,\qquad
\omega_{X,\Lambda}=Ra_X^!\Lambda,\qquad
D_Y(-)=R\mathcal Hom_{\Lambda}(-,\omega_{Y,\Lambda}),\qquad
D_X(-)=R\mathcal Hom_{\Lambda}(-,\omega_{X,\Lambda}).
$$

For every $M\in D^b_{ctf}(X,\Lambda)$ there is a canonical
isomorphism

$$
D_Y(Rf_!M)\xrightarrow{\ \sim\ }Rf_*D_X(M),
$$

natural in $M$, compatible with finite reduction, scalar extension,
and shifts.
