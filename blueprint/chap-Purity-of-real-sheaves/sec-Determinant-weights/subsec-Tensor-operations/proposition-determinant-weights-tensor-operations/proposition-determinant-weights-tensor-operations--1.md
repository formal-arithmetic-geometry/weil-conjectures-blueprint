+++
id = "proposition-determinant-weights-tensor-operations--1"
kind = "proposition"
title = "Weights of constituents of a tensor product"
name_showing = false
order = 1145002
aliases = ["bp-r352-1"]
lean = ["Representation.exists_detWeight_eq_add_of_subquotient_tprod"]
uses = ["definition-determinant-weight", "definition-weil-representation"]
+++
Let $k$ be an algebraically closed field of characteristic zero, $W$ a group,
$\deg:W\to\mathbf Z$ a homomorphism, $\chi:k^\times\to(\mathbf R,+)$ a
homomorphism, and $\gamma\in W$. For a nonzero finite-dimensional representation $M$
write

$$
\operatorname{dw}_{\chi,\gamma}(M)
=\frac{\chi(\det(\gamma\mid M))}{\dim M}.
$$

Say that $M$ has finite geometric determinant if its determinant character
has finite image on $\ker\deg$. Let $V$ and $V'$ be finite-dimensional
$k$-representations of $W$ such that every irreducible subquotient of either
has finite geometric determinant. If $Q=S/U$ is an irreducible subquotient
of $V\otimes V'$ with finite geometric determinant, there are irreducible
subquotients $A$ of $V$ and $B$ of $V'$, both with finite geometric determinant,
such that

$$
\operatorname{dw}_{\chi,\gamma}(Q)
=\operatorname{dw}_{\chi,\gamma}(A)+\operatorname{dw}_{\chi,\gamma}(B).
$$

The degree map need not be surjective, and $\gamma$ need not have degree one.
For Weil representations, take $k=\overline{\mathbf Q}_\ell$,
$W=W(U_0)$, $\chi=\lambda_\iota$, and $\gamma$ of degree one. This gives

$$
\operatorname{DW}(V\otimes V')\subseteq
\operatorname{DW}(V)+\operatorname{DW}(V').
$$

The reverse inclusion in the human statement has no corresponding theorem
in the mainline.
