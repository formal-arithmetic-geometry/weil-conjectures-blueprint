+++
kind = "proof"
of = "corollary-finite-quotients-their-transition-maps--1"
order = 181004
uses = ["prose-02-50", "prose-02-51", "proposition-topos-functoriality"]
+++
Work first on the point. The uniformizer is nonzero, so multiplication
by $\pi_E^n$ is injective on continuous functions from any profinite set
$S$. The uniformizer-power ideals are open, hence their quotient
topologies are discrete. A choice of representatives therefore gives
a continuous lift of every continuous map
$S\to\mathcal O_E/\pi_E^n$.

If a continuous function reduces to zero, each value is divisible by
$\pi_E^n$. Multiplication by $\pi_E^n$ is a homeomorphism onto its image,
so division gives a continuous function with values in $\mathcal O_E$.
This proves exactness on sections. Kernels of sheaves are computed
sectionwise, and the sectionwise surjection is an epimorphism of sheaves;
the forgetful functor from internal modules reflects exactness.

Apply the exact inverse image $p_X^*$ from [prose-02-51]. Its induced
functor on internal modules preserves finite limits and finite colimits,
and takes the regular module to $\mathcal O_{E,X}$. The transported
sequence is the one asserted.
