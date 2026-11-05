+++
id = "proposition-central-element-arithmetic-monodromy-group--2"
kind = "proposition"
title = "A central element of the arithmetic monodromy group (2)"
name_showing = false
order = 1138002
aliases = ["bp-r350-2"]
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.IsPositiveCentralPair.map", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.mulVec_mem_of_mem_zeroLocus_arithmeticMonodromy", "Subrepresentation.exists_apply_sub_smul_mem_of_isIrreducible"]
uses = ["definition-monodromy-groups"]
+++
Let $k$ be a field, let $W$ be a group with a surjective degree map
$\deg:W\to\Z$ and a chosen element $s$ of degree one, and let
$\rho:W\to\GL(k^n)$ be a representation. Write $G$ and $H$ for its
arithmetic and geometric monodromy groups. Suppose that $N>0$ and
$z\in Z(G(k))\cap H(k)\rho(s)^N$.

Let $r:\GL_n(k)\to\GL_m(k)$ be a group homomorphism given by a
$k$-algebra homomorphism of coordinate rings

$$
\varphi:k[\GL_m]\longrightarrow k[\GL_n],\qquad
\operatorname{ev}_{r(g)}=\operatorname{ev}_g\circ\varphi
\quad(g\in\GL_n(k)).
$$

If $G'$ and $H'$ are the monodromy groups of $\rho'=r\circ\rho$, then

$$
r(z)\in Z(G'(k))\cap H'(k)r(\rho(s))^N.
$$

Every element of $G'(k)$ preserves every $W$-stable subspace of $k^m$.
In particular, $r(z)$ acts on every $W$-stable subquotient.

The scalar assertion uses the following form of Schur's lemma. If $k$
is algebraically closed, $E$ is a finite-dimensional $W$-representation,
$U,S\subseteq E$ are subrepresentations, and $f:E\to E$ is a linear
endomorphism commuting with $W$ and preserving $U$ and $S$, then, whenever
$S/(S\cap U)$ is simple, there is $c\in k$ such that

$$
f(x)-cx\in U\qquad(x\in S).
$$

For $U\subseteq S$ this says that $f$ acts on $S/U$ by a scalar.
Applied to $f=r(z)$, it gives the scalar action on each simple subquotient
of $\rho'$. Neither the transport nor the preservation assertion requires
semisimplicity or characteristic zero; algebraic closedness is needed
only for the scalar assertion.
