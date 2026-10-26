+++
id = "prop-coef-integral-dualizing"
kind = "theorem"
title = "The integral dualizing object and its adjunction"
order = 2980
tags = ["latex:proposition"]
uses = ["sk-thm-existence", "sk-prop-sf-existence", "sk-prop-scalar-six", "sk-prop-integral-criterion", "lem-coef-finite-dualizing", "lem-coef-integral-compact-support", "lem-weil-finite-duality-site-comparison", "lem-weil-verdier-preservation-strata", "prop-asd-internal-adjunction", "thm-sf-ambient-adjoint-class"]
+++
Let $R=\mathcal O_E$ and $A_n=A_{E,n}$. Write $a:X\to\operatorname{Spec}k$,
$\dim X\leq d$, $\omega_{X,n}=Ra_n^!A_n$, and

$$
\omega_{X,R}=Ra^!_R R\in D^b_c(X,R),
$$

the value at $R$ of the right adjoint of $Ra_!$ on $D^b_c(-,R)$
([sk-thm-existence], [sk-prop-sf-existence]). Then

$$
\omega_{X,R}\otimes_R^L A_n\cong\omega_{X,n},
\qquad
\omega_{X,R}\cong R\varprojlim_n\omega_{X,n},
$$

and $\omega_{X,R}$ has uniform reduction Tor interval $[-2d,0]$. For
$K\in D^b_c(X,R)$ there is a natural isomorphism of derived mapping complexes

$$
R\operatorname{Hom}_X(K,\omega_{X,R})
\cong R\operatorname{Hom}_R(Ra_!K,R).
$$
