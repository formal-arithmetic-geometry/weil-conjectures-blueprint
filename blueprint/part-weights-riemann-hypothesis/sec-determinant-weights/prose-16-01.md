+++
id = "prose-16-01"
kind = "hidden"
title = "Monodromy and determinant weights"
order = 658
+++
Before purity is known, the only weight we can attach to an irreducible
lisse Weil sheaf $Q$ on a curve is its determinant weight
$\operatorname{dw}_\iota(Q)$, the weight of $\det Q$ divided by the rank
(Corollary [sk-d-real-detweights]). Rankin's argument in
Section [sec-purity-real-sheaves] applies this to the simple factors of
tensor and exterior powers of a real sheaf $\mathcal G$. It uses two
facts: every simple factor of $\mathcal G^{\otimes2m}$ has determinant
weight at most $2m$ times the largest determinant weight of the
constituents of $\mathcal G$, which bounds the weights of $H^2_c$, and the
determinant weights of the simple factors of $\bigwedge^r\mathcal G$ are
known exactly, which lets exterior powers separate the constituents.
This section proves both.

The difficulty is that a determinant only sees an average. For
irreducible $A$ and $B$ of ranks $a$ and $b$, we have
$\det(A\otimes B)=(\det A)^{\otimes b}\otimes(\det B)^{\otimes a}$, so the
determinant weight of $A\otimes B$ as a whole is
$\operatorname{dw}_\iota(A)+\operatorname{dw}_\iota(B)$. But $A\otimes B$
is usually reducible, and which subquotients occur depends on the
monodromy. The rank-weighted average of the determinant weights of its
simple factors is the number above, but nothing so far prevents one
factor from lying above it and another below. If the factors were known
to be pure there would be no problem, since then the determinant weight
of each factor is its weight; but purity is what we are trying to prove.

The model to keep in mind is a central character. If a group acts on
$V$ and some central element $z$ acts on $V$ by the scalar $c$, then $z$
acts on every subquotient of $V^{\otimes a}\otimes(V^\vee)^{\otimes b}$
by $c^{a-b}$, without any knowledge of how these representations
decompose. In Hodge theory the weight of a tensor construction on a
Hodge structure is read off in exactly this way, from the action of the
weight cocharacter, which is central in the Mumford–Tate group. Here we look for a central element of the
monodromy group that has positive degree, so that its scalars record
weights. Let $H\subseteq G$ be the Zariski closures in $\GL(V)$ of the
images of $\pi_1(U)$ and of $W(U_0)$, the geometric and arithmetic
monodromy groups. If $H$ were trivial, the image $\rho(s)$ of a
degree-one lift would itself be central. In general we use the structure
of the identity component,

$$
G^\circ=Z(G^\circ)^\circ H^\circ
$$

for $V$ semisimple (Lemma [sk-p-product]), which holds
because the Lie algebra of $G^\circ$ is reductive, hence the sum of its
center and its derived algebra, and the derived algebra lies in the Lie
algebra of $H$ since $G/H$ is abelian. Writing a power of $\rho(s)$ as a
central torus element times an element of $H$, and taking the product
of its conjugates (a norm) over $G/G^\circ$, we obtain $z=h\rho(s)^N$, central in
$G$, with $h\in H$ and $N>0$
(Proposition [sk-p-central]).

On a simple factor $Q$ of any tensor construction, $z$ acts by a scalar
$c_Q$. Taking determinants gives
$c_Q^{\dim Q}=\det(h\mid Q)\det(s\mid Q)^N$, and $\det(h\mid Q)$ is a root of
unity because determinants have finite geometric monodromy. Hence
$\operatorname{dw}_\iota(Q)=\lambda_\iota(c_Q)/N$, where
$\lambda_\iota(a)=2\log_q|\iota(a)|$ is the additive function of
Proposition [sk-r-real-linear] (Lemma [sk-p-readout]).
Since scalars multiply under tensor products, we obtain
(Proposition [sk-prop-walg-determinant-weights]), for $V$ and $V'$ tensor
constructions on one and the same semisimple sheaf, with
$\operatorname{DW}(V)$ the set of determinant weights of the simple
factors of $V$ and
$\gamma_a$ the determinant weight of the factor $A_a$ of $V$,

$$
\operatorname{DW}(V\otimes V')=\operatorname{DW}(V)+\operatorname{DW}(V'),
\qquad
\operatorname{DW}\bigl(\textstyle\bigwedge^rV\bigr)
=\bigl\{\textstyle\sum_an_a\gamma_a:0\le n_a\le\dim A_a,\ \sum_an_a=r\bigr\}.
$$

For instance, if $V=A_1\oplus A_2$ with $\gamma_1>\gamma_2$, every simple
factor of $\bigwedge^{\dim A_1+1}V$ has determinant weight at most
$\dim(A_1)\gamma_1+\gamma_2$, with equality for the factors of
$\det A_1\otimes A_2$; this is how $A_2$ is isolated in the proof of
Theorem [sk-p-real-purity].

The facts on algebraic groups that we use, namely the relation between
closed subgroups, their identity components and their Lie algebras, and
the structure of a Lie algebra with a faithful semisimple
representation, are proved in Appendix [sec-algebraic-groups-lie-algebras].
