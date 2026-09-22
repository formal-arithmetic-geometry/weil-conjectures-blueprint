+++
id = "lem-sc-riemann-roch"
kind = "lemma"
title = "Riemann-Roch on a proper smooth curve"
order = 3639
lean = ["AlgebraicGeometry.Curve.eulerChar_eq_degree_add_one_sub_genus"]
+++
Let $k$ be algebraically closed, $C$ a proper smooth curve of genus $g$
over $k$, and $\mathcal L$ a line bundle on $C$. Then
$$
 \chi(C,\mathcal L)=\deg\mathcal L+1-g.
$$

*Stacks Project, Algebraic Curves, Lemma 53.5.2, [Tag
0BS6](https://stacks.math.columbia.edu/tag/0BS6).*

## Proof

This is the recorded classical input of the statement, Stacks Project,
Algebraic Curves, Lemma 53.5.2 ([Tag
0BS6](https://stacks.math.columbia.edu/tag/0BS6)), used in the displayed
form $\chi(C,\mathcal L)=\deg\mathcal L+1-g$, where
$\chi(C,\mathcal L)=\dim H^0(C,\mathcal L)-\dim H^1(C,\mathcal L)$ and
$g=\dim H^1(C,\mathcal O_C)$. No separate proof is given.

Unresolved dependencies: def:sc-curves
