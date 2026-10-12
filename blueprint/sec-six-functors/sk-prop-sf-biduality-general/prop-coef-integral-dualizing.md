+++
id = "prop-coef-integral-dualizing"
kind = "theorem"
title = "The integral dualizing object and its adjunction"
order = 2485
tags = ["latex:proposition"]
uses = ["lem-coef-finite-dualizing", "lem-coef-integral-compact-support", "lem-coef-normalized-dvr-effectivity", "lem-weil-finite-duality-site-comparison", "lem-weil-verdier-preservation-strata", "prop-asd-internal-adjunction", "thm-sf-ambient-adjoint-class"]
+++
Write $a:X\to\operatorname{Spec}k$, $\dim X\leq d$, and
$\omega_{X,n}=Ra_n^!A_n$. There is a canonical derived-complete
object

$$
\omega_{X,R}=R\varprojlim_n\operatorname{Res}_n\omega_{X,n},
\qquad \omega_{X,R}\otimes_R^L A_n\cong\omega_{X,n}.
$$

It is in $D^b_c(X,R)$, with uniform reduction Tor interval
$[-2d,0]$. For $K\in D^b_c(X,R)$ there is a natural
isomorphism of derived mapping complexes

$$
R\operatorname{Hom}_X(K,\omega_{X,R})
\cong R\operatorname{Hom}_R(Ra_!K,R).
$$

Thus $\omega_{X,R}$ is the value at $R$ of the exceptional
right adjoint on the constructible coefficient category.
