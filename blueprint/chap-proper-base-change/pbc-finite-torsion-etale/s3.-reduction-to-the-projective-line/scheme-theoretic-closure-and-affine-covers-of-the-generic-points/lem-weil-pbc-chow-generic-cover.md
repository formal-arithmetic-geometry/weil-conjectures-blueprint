+++
id = "lem-weil-pbc-chow-generic-cover"
kind = "lemma"
title = "Finite cover by affines containing the generic points"
order = 1681
uses = ["def-weil-pbc-scheme-conventions", "lem-weil-pbc-chow-affine-open-around-generics"]
+++
Let $X$ be quasi-compact and quasi-separated and assume that $X$ has only
finitely many irreducible components $Z_1,\dots,Z_r$ with generic points
$\eta_j$. Then there is a finite affine open covering

$$
 X=U_1\cup\dots\cup U_m
$$

such that $\eta_j\in U_i$ for every $i,j$. If moreover $X\to Y$ is of finite
type with $Y$ affine, one may take each $U_i$ affine of finite type over $Y$.
In particular the open subscheme $U:=U_1\cap\dots\cap U_m$ is dense in $X$.

## Proof

By [lem-weil-pbc-chow-affine-open-around-generics] applied to the finite list
$\eta_1,\dots,\eta_r$, for every $x\in X$ there is an affine open $U_x$
containing $x$ and all the $\eta_j$. Quasi-compactness of $X$ lets us pick a
finite subcover $U_1,\dots,U_m$ among them. If $X\to Y$ is of finite type, an
open subscheme of $X$ is again of finite type over $Y$ (open immersions are of
finite type), so each $U_i$ is affine of finite type over $Y$. Finally $U\cap
Z_j$ is a nonempty open subset of the irreducible space $Z_j$ (it contains
$\eta_j$), hence dense in $Z_j$; since this holds for all $j$ and
$X=Z_1\cup\dots\cup Z_r$, the open $U$ is dense in $X$.
