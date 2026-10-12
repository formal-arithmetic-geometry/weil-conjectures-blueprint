+++
id = "thm-pur-td-criterion"
kind = "theorem"
title = "Trace–diagonal criterion"
order = 2260
uses = ["cor-sf-ambient-adjoint-discharge", "def-pur-conventions", "def-pur-td-datum", "def-weil-ambient-exceptional-adjoint", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-tensor", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-pbc-proetale-site"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $f:X\to Y$ be separated finite type, and let $Rf^!$ be the right adjoint
of $Rf_!$ on the bounded constructible and finite-Tor coefficients of this
chapter, which exists by [cor-sf-ambient-adjoint-discharge] (no ambient
datum of [def-weil-ambient-exceptional-adjoint] is assumed). Let
$L\in D^b_{ctf}(X,\Lambda)$ be tensor-invertible, and let
$(\operatorname{tr}_f,\operatorname{cl}_\Delta)$ be a
trace–diagonal datum. If the two
triangular composites are the identity,
naturally in $A$ and $K$, then:

$$
Rf_!\;\dashv\;G_L,
$$

i.e. $G_L$ is a right adjoint of $Rf_!$. Consequently there is a
unique isomorphism of functors

$$
Rf^!(-)\;\xrightarrow{\ \sim\ }\;Lf^*(-)\otimes^L_{\Lambda_X}L
$$

compatible with the counits; in particular

$$
\omega_f=Rf^!\Lambda_Y\;\cong\;L.
$$
