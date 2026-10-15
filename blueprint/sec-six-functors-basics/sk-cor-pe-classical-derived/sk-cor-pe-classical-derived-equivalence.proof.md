+++
kind = "proof"
of = "det-pe-classical-derived-equivalence"
+++
*(1).* Since $\nu_X^*$ is exact, $H^q(\nu_X^*L)\cong\nu_X^*H^q(L)$, which is
classical and vanishes for $q\ll0$. The functor $R\nu_{X,*}$ is the right
derived functor of a left exact functor, so it carries complexes concentrated in
degrees $\geq a$ to complexes concentrated in degrees $\geq a$.

*(2), one sheaf.* Let $K=G[-q]$ with $G$ a classical module sheaf, say
$G=\nu_X^*F$. The triangle identity says that the composite
$\nu_X^*F\to\nu_X^*R\nu_{X,*}\nu_X^*F\to\nu_X^*F$ of $\nu_X^*$ applied to the
unit and the counit is the identity. The unit $F\to R\nu_{X,*}\nu_X^*F$ is an
isomorphism by hypothesis, hence so is the counit. The case of a shift follows.

*(2), bounded complexes.* Induct on the number of nonzero cohomology sheaves.
If $K$ has nonzero cohomology in degrees $a<b$ only, the triangle
$\tau_{\leq a}K\to K\to\tau_{>a}K\to$ has outer terms with fewer nonzero
cohomology sheaves, all classical. The counit is a natural transformation of
triangulated functors, so the five lemma on the long exact cohomology
sequences gives the claim for $K$.

*(2), bounded below complexes.* Let $K$ be bounded below and fix $m$. For
$N\geq m$, the complex $\tau_{\leq N}K$ is bounded with classical cohomology, so
its counit is an isomorphism. In the triangle
$\tau_{\leq N}K\to K\to\tau_{>N}K\to$, the complex $\tau_{>N}K$ lies in degrees
$>N$, hence so do $R\nu_{X,*}\tau_{>N}K$ and $\nu_X^*R\nu_{X,*}\tau_{>N}K$ by (1).
Therefore $H^m$ of $\nu_X^*R\nu_{X,*}\tau_{\leq N}K\to\nu_X^*R\nu_{X,*}K$ and of
$\tau_{\leq N}K\to K$ are isomorphisms for $m\leq N$, and by naturality of the
counit $H^m$ of the counit of $K$ is an isomorphism. As $m$ is arbitrary, the
counit of $K$ is an isomorphism.

Finally, (1), (2) and the unit isomorphism show that the two functors are
mutually inverse equivalences.
