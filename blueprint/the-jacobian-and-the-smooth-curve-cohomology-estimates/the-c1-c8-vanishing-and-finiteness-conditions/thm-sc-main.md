+++
id = "thm-sc-main"
kind = "theorem"
title = "Smooth-curve calculations"
order = 4550
lean = ["AlgebraicGeometry.Curve.smoothCurveCalculations"]
uses = ["def-weil-pbc-eight-curve-assertions", "lem-sc-C1", "lem-sc-C2", "lem-sc-C3", "lem-sc-C4", "lem-sc-C5", "lem-sc-C6", "lem-sc-C7", "lem-sc-C8", "thm-sc-proper-cohomology", "thm-sc-affine-cohomology", "thm-sc-constant-invariance"]
+++
Let $k$ be algebraically closed and let $C$ be a smooth separated curve over
$k$. Let $\mathbf F_r$ be the constant sheaf and consider the assertions
$\mathcal C_1,\dots,\mathcal C_8$ of [def-weil-pbc-eight-curve-assertions].

(a) If $r\neq\operatorname{char}k$, then $\mathbf F_r$ satisfies
$\mathcal C_1$, $\mathcal C_4$, $\mathcal C_6$, and $\mathcal C_8$; it
satisfies $\mathcal C_2$ when $C$ is affine and
$\mathcal C_5,\mathcal C_7$ when $C$ is proper. Explicitly (for
$r\neq\operatorname{char}k$):
$$
H^0(C,\mathbf F_r)=\mathbf Z/r\mathbf Z,\qquad
H^2(C,\mathbf F_r)=0\ \text{if}\ C\ \text{is affine},
$$
and, after choosing the trivialization by a primitive $r$-th root of unity,
there is a short exact sequence
$$
0\longrightarrow\mathcal O_C(C)^\times/\mathcal O_C(C)^{\times\,r}
\longrightarrow H^1(C,\mathbf F_r)
\longrightarrow\operatorname{Pic}(C)[r]\longrightarrow0.
$$
If $C$ is proper of genus $g$,
$$
H^0(C,\mathbf F_r)=\mathbf Z/r\mathbf Z,\quad
H^1(C,\mathbf F_r)=(\mathbf Z/r\mathbf Z)^{2g},\quad
H^2(C,\mathbf F_r)=\mathbf Z/r\mathbf Z,\quad
H^q(C,\mathbf F_r)=0\ (q>2),
$$
and all these identifications are compatible with algebraically closed field
extension (the pullback maps are isomorphisms).

(b) If $\operatorname{char}k=p>0$, the constant sheaf $\mathbf F_p$
satisfies $\mathcal C_1$, $\mathcal C_3$, and $\mathcal C_8$; it satisfies
$\mathcal C_2$ when $C$ is affine and $\mathcal C_5,\mathcal C_7$ when $C$
is proper.

(c) The maps in $\mathcal C_6$, $\mathcal C_7$, and $\mathcal C_8$ are the
pullback and restriction maps fixed in the eight-assertion definition.

## Proof

Assertions (a) and (b) are the conjunctions, respectively, of
[lem-sc-C1], [lem-sc-C4], [lem-sc-C6], [lem-sc-C8], [lem-sc-C2] (affine
case) and [lem-sc-C5], [lem-sc-C7] (proper case) for
$r\neq\operatorname{char}k$; and of [lem-sc-C1], [lem-sc-C3], [lem-sc-C8],
[lem-sc-C2] (affine) and [lem-sc-C5], [lem-sc-C7] (proper) for
$r=\operatorname{char}k=p>0$.

The explicit identifications are [thm-sc-proper-cohomology] and
[thm-sc-affine-cohomology], and the compatibility with field extension is
[thm-sc-constant-invariance]. Assertion (c) is by the definitions of the
maps in the eight-assertion definition.

Unresolved dependencies: def:sc-constant-sheaves, def:sc-field-extension, def:sc-curves
