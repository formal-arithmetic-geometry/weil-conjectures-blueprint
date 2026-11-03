+++
kind  = "proof"
of    = "thm-coef-finite-hom"
+++
Define $v_{K,M}$ by tensoring evaluation
$R\mathcal Hom_A(K,M)\otimes_A^LK\to M$ with $B$,
reassociating, and transposing over $B$.
Finite-Tor constructible preservation of its source and target
is [cor-weil-finite-constructible-hom].

Choose a finite stratification on which the cohomology of $K$
is finite locally constant. Its restrictions $P=s^*K$ are
site-perfect, by the finite-free-resolution truncation argument
of [lem-weil-bounded-finite-tor-perfect] and the notion in
[def-weil-site-perfect-complex]. The localization triangles
of [def-weil-open-closed-recollement] reduce the assertion
in the first argument to $K=Rs_!P$. On this generator
[lem-weil-stratum-ambient-hom] identifies the left side
before coefficient change with

$$
Rs_{*,A}R\mathcal Hom_A(P,Rs_A^!M).
$$

The inner complex is finite-Tor constructible: the closed
exceptional inverse images in $s^!$ have that property by
[lem-coef-finite-closed-shriek], and internal Hom from a
site-perfect complex is its finite-projective dual tensor the
second argument. Move coefficient change through $Rs_*$
by [lem-coef-finite-direct-image], through $Rs^!$ by
[lem-coef-finite-closed-shriek], and through internal Hom
from $P$ by its finite-projective model. The result is

$$
Rs_{*,B}R\mathcal Hom_B(P_B,Rs_B^!M_B)
=R\mathcal Hom_B(Rs_{!,B}P_B,M_B).
$$

Extension by zero commutes with coefficient tensor, so this is
the required target. Every comparison used is defined by the
same evaluations and adjunction counits; transposing identifies
their composite with $v_{K,M}$. Exactness in the first
argument now proves it for $K$. The comparison maps respect
evaluation by their definition; associativity of tensor product
and uniqueness of its transpose give the successive-quotient
and composition identities. Finally
[lem-weil-finite-duality-site-comparison] transports the
specified internal-Hom comparison to the pro-etale site.
