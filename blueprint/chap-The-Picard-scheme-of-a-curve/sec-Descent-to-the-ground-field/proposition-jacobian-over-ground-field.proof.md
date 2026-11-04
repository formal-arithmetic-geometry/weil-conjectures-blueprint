+++
kind = "proof"
of = "proposition-jacobian-over-ground-field"
order = 1557
uses = ["lemma-rigidification-along-section", "theorem-picard-scheme-jacobian-over-separably"]
+++
We descend the Jacobian of $C_{0,k_s}$, where $k_s\subseteq\bar
k$ is a separable closure of $k$. In general $k_s/k$ is infinite, hence
not an fppf cover. For this reason we move the descent datum on the
Jacobian over $k_s$ by limit arguments to a finite Galois extension, and
descend along that extension. A second limit argument shows that the
descended scheme represents the degree-zero Picard sheaf.

Let $F=\operatorname{Pic}^0_{C_0/k}$ be the degree-zero part of the
fppf Picard sheaf. Here we use that the fibrewise degree is locally
constant, by coherent base change and Riemann–Roch. The Picard
sheaf and the degree commute with base change. Hence
Theorem [theorem-picard-scheme-jacobian-over-separably] gives an
abelian variety $J_s$ over $k_s$ representing the restriction of $F$ to
$k_s$-schemes; $J_s$ is projective. Over $k_s\otimes_kk_s$ the two
pullbacks of $J_s$ represent the same functor, so by the Yoneda lemma we
get an isomorphism between them. All identifications are induced by $F$.
Hence this isomorphism satisfies the cocycle condition over
$k_s\otimes_kk_s\otimes_kk_s$ and respects the group structures.

To move this descent datum to a finite extension, note that $k_s$ is
the filtered union of its finite separable subextensions, and
$k_s\otimes_kk_s$ and the triple tensor product are the corresponding
unions. By the limit theorems for schemes of finite
presentation [Stacks, [01ZM](https://stacks.math.columbia.edu/tag/01ZM)], the defining equations of $J_s$ in a
projective space, the descent isomorphism, its inverse and the group
operations are defined over some finite stage. The finitely many
identities among them (inverse, cocycle, group axioms) hold after
enlarging the stage. We enlarge it further to a Galois extension. In
this way we obtain a finite Galois extension $K/k$ in $k_s$ and a
projective $K$-scheme $J_K$ with a group structure and a compatible
descent datum for $K/k$, whose base change to $k_s$ is the datum on $J_s$.
Since $\operatorname{Spec}K\to\operatorname{Spec}k$ is finite locally free
and surjective, the descent datum on the projective scheme $J_K$ is
effective [Stacks, [0CCJ](https://stacks.math.columbia.edu/tag/0CCJ)]. This gives a commutative group scheme $J_0$ over
$k$ with $J_0\times_kk_s\simeq J_s$. Properness and smoothness descend
along $K/k$, and connectedness and dimension may be checked over $\bar
k$. Hence $J_0$ is an abelian variety of dimension $g$.

The functors $J_0$ and $F$ are fppf sheaves that agree after base
change to $k_s$. Since $k_s/k$ is not finite, we need a limit argument
to show that they agree. Both functors are
locally of finite presentation. For $J_0$ this is [Stacks, [01ZC](https://stacks.math.columbia.edu/tag/01ZC)]. For $F$
it follows from Lemma [lemma-rigidification-along-section] once the
finite stages contain a field of definition of a point of $C_0$,
because invertible sheaves, rigidifications and their isomorphisms are
of finite presentation. Hence, for affine $T$ over $k$, a section of
either functor over $T_{k_s}$, or over $T_{k_s\otimes_kk_s}$, comes from
a finite stage. Likewise, two sections that agree over $T_{k_s}$ agree over
a finite stage.

The identification $J_0(T_{k_s})\simeq F(T_{k_s})$ is compatible with the
descent data. Let a section of one functor over $T$ be given. We
transport its image over $T_{k_s}$ and descend the result to some
$T_L$ with $L/k$ finite. After enlarging $L$, its two pullbacks to
$T_{L\otimes_kL}$ agree. Since both functors are fppf sheaves, it then
descends to $T$. The same argument applied to equalities shows that the
result is unique. We obtain inverse bijections $J_0(T)\simeq F(T)$,
natural in affine $T$, and hence an isomorphism of sheaves.

The Picard sheaf and the degree commute with field extension. Hence
$J_0\times_kk'$ represents the degree-zero Picard sheaf of
$C_0\times_kk'$ for every $k'/k$. Over $\bar k$ the value of the Picard
sheaf is the Picard group, by rigidification and
$\operatorname{Pic}(\bar k)=0$. This gives the displayed identification.
For $\gamma\in\operatorname{Gal}(\bar k/k)$, naturality with respect to
$\operatorname{Spec}(\gamma)$ says that this group isomorphism
intertwines the Galois action on points with pullback of invertible
sheaves. Here $\operatorname{Gal}(\bar k/k)=\operatorname{Gal}(k_s/k)$
because $\bar k/k_s$ is purely inseparable.
