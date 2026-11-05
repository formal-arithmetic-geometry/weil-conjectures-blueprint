+++
kind = "proof"
of = "lemma-punctured-surface-punctured-curve--1"
order = 970002
uses = ["proposition-smooth-purity-finite-coefficients", "corollary-dualizing-complex-smooth-scheme", "theorem-smooth-base-change-classical-torsion"]
+++
Put $U=S-D_{2,S}$ and $T=D_{1,S}-z_S$. In degree zero, both schemes
are connected, so restriction of the constant sheaf induces a bijection.

For the surface, compute $H^q(U,\mathbf F_\ell)$ as the stalk at
$\bar z$ of $R^qj_*\mathbf F_\ell$, where $j:Z-D_2\hookrightarrow Z$.
On a smooth chart, smooth purity
[proposition-smooth-purity-finite-coefficients] and the transitivity of
dualizing complexes [corollary-dualizing-complex-smooth-scheme] give
$i^!\mathbf F_\ell\simeq\mathbf F_\ell(-1)[-2]$ for the divisor.
The supported localization triangle then computes the direct images:
$\mathbf F_\ell$ in degree zero, the constant sheaf on the divisor with
twist $(-1)$ in degree one, and zero in higher degrees. Smooth base
change [theorem-smooth-base-change-classical-torsion], together with
passage to the étale limit, transfers this computation to $Z$.
Taking the stalk gives groups isomorphic to the additive group
$\mathbf F_\ell$ in degrees zero and one, and zero for $q\geq2$.

For the trait, $T\simeq\operatorname{Spec}K$, where $K$ is the fraction
field of a henselian discrete valuation ring with separably closed
residue field. Its étale cohomology is the Galois cohomology of $K$.
The absolute Galois group has a quotient $\mathbf Z_\ell$ whose kernel
has all finite quotients of order prime to $\ell$. For the trivial
module $\mathbf F_\ell$, this gives $H^1(T,\mathbf F_\ell)\simeq
\mathbf F_\ell$ and $H^q(T,\mathbf F_\ell)=0$ for $q\geq2$.
Consequently restriction is bijective in all degrees $q\geq2$.

It remains to treat degree one. The local chart supplies a unit on $U$
whose restriction to $T$ is a uniformizer of the trait. Choose a
primitive $\ell$-th root of unity in $k$ to identify the constant sheaf
$\mathbf F_\ell$ with $\mu_\ell$. Naturality of the Kummer boundary
sends the class of this unit to the class of the uniformizer. The latter
is nonzero, since its valuation is one and hence it cannot be an
$\ell$-th power in $K$. Thus restriction in degree one is a nonzero
homomorphism between groups of prime order $\ell$, and is therefore
bijective.
