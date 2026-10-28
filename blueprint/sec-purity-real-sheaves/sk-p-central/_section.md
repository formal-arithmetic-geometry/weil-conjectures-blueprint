+++
id = "sk-p-central"
kind = "proposition"
title = "A central element of the arithmetic monodromy group"
lean = ["AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.exists_isPositiveCentralPair"]
order = 4057
uses = ["sk-d-real-weil", "sk-r-real-linear", "sk-i-restriction", "sk-lem-walg-normal-commutator", "sk-p-product", "sk-p-geometry", "sec-algebraic-groups-lie-algebras"]
tags = ["sketch"]
+++
By a *tensor construction* on a representation $V$ we mean a
representation obtained from $V$ and $V^\vee$ by finitely many tensor
products, direct sums, exterior powers and subquotients by $W(U_0)$-stable
subspaces. Since the stabilizer of a subspace is closed, a $W(U_0)$-stable
subspace is $G$-stable, and so $G$ acts on every tensor construction
through its action on $V$.

Let $V_1,\ldots,V_n$ be semisimple Weil representations and form the
monodromy groups $H\subseteq G$ of $V=\bigoplus_iV_i$, and let
$s\in W(U_0)$ have degree one. There are an integer $N>0$ and
$h\in H(\overline{\mathbf Q}_\ell)$ such that

$$
z=h\,\rho(s)^N\in Z(G)(\overline{\mathbf Q}_\ell).
$$

The action of $z$ on each tensor construction on $V$ preserves every
$W(U_0)$-stable subquotient and is scalar on each simple subquotient.

*Complement.* For a semisimple representation $\rho\colon W\to\GL_n(k)$
of a group $W=P\rtimes\langle s\rangle$ over any algebraically closed
field $k$ of characteristic zero, with $F=\rho(s)$, a *positive central
pair* is $(N,z)$ with $N\in\mathbf Z_{>0}$ and
$z\in Z(G)(k)\cap H(k)F^N$; the argument below shows that one exists. The
coset condition does not assert that $G/H$ is infinite cyclic or that the
cosets $HF^N$ for different $N$ are distinct.
