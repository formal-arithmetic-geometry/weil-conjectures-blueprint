+++
kind  = "proof"
of    = "lem-fet-galois-category"
+++
We verify the axioms of [def-galois-category] for the pair
$(\mathrm{F\acute Et}(Y),F_{\bar y})$ of [def-galois-categories]
and [def-galois-fibre-functor]; the scheme-theoretic notions used
are those of [def-weil-pbc-scheme-conventions].
Axioms (1)–(3), which do not involve $F_{\bar y}$ or the connectedness
of $Y$, are [lem-fet-finite-limits].
Step 1: exactness. A scheme finite etale over the spectrum of a
separably closed field is a finite disjoint union of copies of it, so
$F_{\bar y}(P)=|P_{\bar y}|$ is the set of points of the base change of
$P$ to $\bar y$, which is finite ([lem-galois-geometric-fibre]).
Since $F_{\bar y}(P)=\operatorname{Hom}_Y(\operatorname{Spec}\Omega,P)$
is corepresented, it preserves the final object and fibre products. A
geometric point of a disjoint union factors through exactly one summand,
so $F_{\bar y}$ preserves finite coproducts. The geometric points of
$P/G$ are the $G$-orbits of geometric points of $P$ (compute affine
locally with the ring of invariants), so $F_{\bar y}$ preserves
quotients by finite groups. An epimorphism $f:P\to Q$ is surjective:
the complement $W$ of its image is open and closed (images of finite
morphisms are closed, of etale ones open), and the two maps
$Q\to Q\amalg W$ which are the identity on the image of $f$ and the two
different inclusions on $W$ agree after composition with $f$, so
$W=\emptyset$; hence $F_{\bar y}(f)$ is surjective. This gives axioms (4) and (5).
Step 2: $F_{\bar y}$ reflects isomorphisms. Let $f:P\to Q$ induce a
bijection on geometric fibres. If a morphism of finite etale
$Y$-schemes is surjective on geometric fibres at $\bar y$, it is
surjective: the complement of its image is open and closed in the target
(images of finite morphisms are closed, of etale ones open), it is
finite etale over the connected $Y$ with empty geometric fibre at
$\bar y$, and a finite etale $Y$-scheme with empty fibre at one point of
the connected $Y$ is empty, its degree being locally constant. Applying
this to the diagonal $P\to P\times_QP$, which is split by a projection
and hence a monomorphism, and which is surjective on geometric fibres
because $F_{\bar y}(f)$ is injective, shows that the diagonal is a
surjective open immersion, hence an isomorphism, so $f$ is a
monomorphism. Then $f$ is an open immersion (Step 4 of
[lem-fet-finite-limits]) which is surjective, hence an isomorphism.
This is axiom (6).
