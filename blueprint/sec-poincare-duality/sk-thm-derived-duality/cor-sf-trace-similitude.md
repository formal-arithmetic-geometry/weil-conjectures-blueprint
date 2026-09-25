+++
id = "cor-sf-trace-similitude"
kind = "theorem"
title = "Frobenius similitudes for the constant sheaf"
order = 2580
tags = ["latex:corollary"]
uses = ["cor-sf-trace", "cor-sf-trace-pairing", "def-sf-datum", "def-sf-orientation", "rem-sf-orientation-pointer", "thm-sf-verdier-exchange"]
+++
In the setting of [def-sf-datum] and [def-sf-orientation], let
$X$ be smooth, proper and geometrically connected of pure dimension $d$.
Then, for the constant sheaf, $\langle Fx,Fy\rangle_i= q^d\langle x,y\rangle_i$ and the eigenvalues of $F$ on
$H^{2d-i}(X,\Lambda)$ are the $q^d/\alpha$ for the eigenvalues $\alpha$ on
$H^i(X,\Lambda)$, with multiplicity.

## Proof

The duality isomorphism of [cor-sf-trace] is
equivariant for the geometric Frobenius once the orientation is, by
[thm-sf-verdier-exchange]; the operator on the
second factor is therefore $q^d(F^{-1})^{\mathsf t}$ relative to the pairing
of [cor-sf-trace-pairing], which gives the similitude and, by comparing
characteristic polynomials of an operator and its transpose-inverse, the
reciprocal eigenvalue statement. (The equivariance of the orientation is
the Weil structure of purity, proved in the purity chapter; see
[rem-sf-orientation-pointer].)
