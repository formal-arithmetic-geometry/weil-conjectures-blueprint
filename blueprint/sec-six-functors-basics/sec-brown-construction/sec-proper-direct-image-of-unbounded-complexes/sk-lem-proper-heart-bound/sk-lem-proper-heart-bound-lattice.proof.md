+++
kind = "proof"
of = "det-proper-heart-bound-lattice"
+++
*Completeness.* $L_0$ is finite free locally over $\mathcal O_{E,S}$, hence derived $\pi_E$-complete:
$L_0=R\varprojlim_nL_0/\pi_E^n$. Write $a=i\circ u$ with $u$ a quasi-compact open immersion and $i$ a closed
immersion. Closed pushforward is exact and preserves products ([Stacks, Tag 09BM](https://stacks.math.columbia.edu/tag/09BM)); extension by zero is
exact and preserves limits ([Stacks, Tag 09BP](https://stacks.math.columbia.edu/tag/09BP)). An exact functor preserving products preserves derived
inverse limits of sequences (fiber of $1-\mathrm{shift}$ on a product), so
$a_!L_0=R\varprojlim_na_!(L_0/\pi_E^n)$. Restriction to $X_V$ is exact and preserves products, so the same
holds after restriction.

*Sections.* $R\Gamma(X_V,-)$ preserves products (a product of K-injective complexes is K-injective, and
sections preserve products) and cones, hence derived limits of sequences:

$$
R\Gamma(X_V,a_!L_0)=R\varprojlim_nR\Gamma\bigl(X_V,a_!(L_0/\pi_E^n)\bigr).
$$

*Milnor.* The Milnor sequence ([sk-prop-pe-milnor], or its version for abelian groups)

$$
0\to\varprojlim^1_nH^{q-1}\bigl(X_V,a_!(L_0/\pi_E^n)\bigr)\to H^q(X_V,a_!L_0)\to\varprojlim_nH^q\bigl(X_V,a_!(L_0/\pi_E^n)\bigr)\to0
$$

has vanishing outer terms when $q-1>2d$, by [det-proper-heart-bound-torsion]. Hence $H^q(X_V,a_!L_0)=0$ for
$q>2d+1$.
