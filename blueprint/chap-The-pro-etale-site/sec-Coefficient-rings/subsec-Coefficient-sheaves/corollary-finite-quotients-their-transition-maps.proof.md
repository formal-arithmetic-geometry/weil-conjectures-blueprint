+++
kind = "proof"
of = "corollary-finite-quotients-their-transition-maps"
order = 182
uses = ["corollary-finite-quotients-their-transition-maps--1", "corollary-finite-quotients-their-transition-maps--2", "corollary-finite-quotients-their-transition-maps--3"]
+++
It suffices to prove exactness on the point, since $p_X^*$ is exact and
inverse image along $f:X\to Y$ satisfies $p_Y\circ f=p_X$. Now, on a profinite
set $S$, multiplication by $\pi_E^n$ is injective on continuous functions
$S\to\mathcal O_E$, and its image is the kernel of reduction. Moreover, reduction is
surjective because a continuous function $S\to\mathcal O_E/\pi_E^n$ takes
finitely many values, and choosing a representative of each gives a
continuous lift. Finally, the chain map $(\pi_E,\mathrm{id})$ commutes with the
differentials because $\pi_E^{n}\pi_E=\pi_E^{n+1}$, and its degree-zero
component is the identity, so it induces the quotient projection.
