+++
id = "lem-sc-pic-proper-decomposition"
kind = "lemma"
title = "Structure of the Picard group of a proper curve"
order = 3634
lean = ["AlgebraicGeometry.Curve.picardGroupEquivProdPic0"]
uses = ["def-sc-pic0"]
+++
Let $C$ be a proper smooth curve over algebraically closed $k$. The degree
sequence
$$
 0\longrightarrow\operatorname{Pic}^0(C)\longrightarrow
 \operatorname{Pic}(C)\xrightarrow{\ \deg\ }\mathbf Z\longrightarrow0
$$
splits (the degree map is surjective since a $k$-rational point gives a
degree-one class), hence
$$
 \operatorname{Pic}(C)\cong\mathbf Z\oplus\operatorname{Pic}^0(C).
$$

## Proof

The degree map is surjective: a nonempty proper scheme over $k$ has a
closed point $P$, whose residue field is finite over $k$, hence equal to
$k$ (Hilbert's Nullstellensatz: *reference: Stacks Project, Algebra: the
Nullstellensatz*), and $\mathcal O([P])$ is a class of degree $1$
[def-sc-pic0]. The short exact sequence of abelian groups splits over the
free group $\mathbf Z$, giving the direct-sum decomposition.

Unresolved dependencies: def:sc-curves, def:sc-picard-group
