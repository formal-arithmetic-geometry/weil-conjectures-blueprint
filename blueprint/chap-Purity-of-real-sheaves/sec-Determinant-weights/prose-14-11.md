+++
id = "prose-14-11"
kind = "hidden"
title = "Determinant weights"
order = 1116
+++
Before purity is known, the only weight we can attach to an irreducible
lisse Weil sheaf $Q$ on a curve is its determinant weight
$\operatorname{dw}_\iota(Q)$, the weight of $\det Q$ divided by the rank
(Definition [definition-determinant-weight] and
Corollary [corollary-determinant-weights]). This section proves the two facts about
determinant weights that Rankin's argument in Section [sec-Rankins-bound] needs for the
tensor and exterior powers of a real sheaf $\mathcal G$. First, every simple
factor of $\mathcal G^{\otimes2m}$ has determinant weight at most $2m$ times
the largest determinant weight of the constituents of $\mathcal G$, and this
bounds the weights of $H^2_c$. Second, the determinant weights of the simple
factors of $\bigwedge^r\mathcal G$ are known exactly, and this is what lets
exterior powers separate the constituents.

The difficulty is that a determinant only sees an average. For
irreducible $A$ and $B$ of ranks $a$ and $b$, we have
$\det(A\otimes B)=(\det A)^{\otimes b}\otimes(\det B)^{\otimes a}$. Hence the
determinant weight of $A\otimes B$ as a whole is
$\operatorname{dw}_\iota(A)+\operatorname{dw}_\iota(B)$. But $A\otimes B$
is usually reducible, and which subquotients occur depends on the
monodromy. The rank-weighted average of the determinant weights of its
simple factors is the number above, but nothing so far prevents one
factor from lying above it and another below. If the factors were pure,
the determinant weight of each would be its weight, but purity is what we are
trying to prove.

The model to keep in mind is a central character. If a group acts on
$V$ and some central element $z$ acts on $V$ by the scalar $c$, then $z$
acts on every subquotient of $V^{\otimes a}\otimes(V^\vee)^{\otimes b}$
by $c^{a-b}$, without any knowledge of how these representations
decompose. We therefore look for a central element of positive degree in the
monodromy group; its scalars will record weights.

Let $H\subseteq G$ be the Zariski closures in $\GL(V)$ of the
images of $\pi_1(U)$ and of $W(U_0)$, the geometric and arithmetic
monodromy groups. If $H$ were trivial, the image $\rho(s)$ of a
degree-one lift would itself be central. In general we use the structure
of the identity component,

$$
G^\circ=Z(G^\circ)^\circ H^\circ
$$

for $V$ semisimple (Lemma [lemma-identity-component]). The reason is that
the Lie algebra of $G^\circ$ is reductive, hence the sum of its
center and its derived algebra, and since $G/H$ is abelian, the derived algebra
lies in the Lie algebra of $H$. Accordingly, in
Proposition [proposition-central-element-arithmetic-monodromy-group] we write a power of
$\rho(s)$ as a central torus element times an element of $H$, and then we take the
product of its conjugates over $G/G^\circ$. The result is an element
$z=h\rho(s)^N$, central in $G$, with $h\in H$ and $N>0$.

On a simple factor $Q$ of any tensor construction, $z$ acts by a scalar
$c_Q$, and taking determinants gives
$c_Q^{\dim Q}=\det(h\mid Q)\det(s\mid Q)^N$. Since determinants have finite
geometric monodromy, $\det(h\mid Q)$ is a root of unity, and from this
Lemma [lemma-determinant-weight-from-central-scalar] concludes that
$\operatorname{dw}_\iota(Q)=\lambda_\iota(c_Q)/N$, where
$\lambda_\iota(a)=2\log_q|\iota(a)|$ is the additive function of
Proposition [proposition-weights-under-usual-operations].
Since scalars multiply under tensor products, we obtain
Proposition [proposition-determinant-weights-tensor-operations].

The facts on algebraic groups that we use, namely the relation between
closed subgroups, their identity components and their Lie algebras, and
the structure of a Lie algebra with a faithful semisimple
representation, are proved in Appendix [chap-Algebraic-groups-in-characteristic-zero].
