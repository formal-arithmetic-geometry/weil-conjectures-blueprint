+++
id = "corollary-functional-equation--7"
kind = "corollary"
title = "Reciprocity of a determinant factor"
order = 1044008
aliases = ["bp-r320-7"]
lean = ["LinearMap.C_det_mul_charpolyRev_of_similitude"]
uses = []
+++
The global determinant form is bypassed by the Lean route; the polynomial
identity used in its place is the following.

Let $K$ be a field, let $V,W$ be finite-dimensional $K$-vector spaces, and let
$p:V\times W\to K$ be a perfect pairing. Suppose that $F\in\End_K(V)$,
$G\in\End_K(W)$ and $c\in K$ satisfy

$$
p(Fv,Gw)=c\,p(v,w).
$$

Put $b=\dim_K V$. Then, in $K[T]$,

$$
\det(F)\det(1-TG)=(-1)^b\det(cT\,\id_V-F).
$$

This identity does not require $c\ne0$.
