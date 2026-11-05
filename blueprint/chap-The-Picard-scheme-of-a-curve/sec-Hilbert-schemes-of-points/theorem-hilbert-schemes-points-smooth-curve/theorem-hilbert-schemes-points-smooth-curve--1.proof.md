+++
kind = "proof"
of = "theorem-hilbert-schemes-points-smooth-curve--1"
order = 1534002
uses = []
+++
Every finite set $A$ of points of $C$ lies in an affine open. To see
this, choose a rational function $a\in k(C)$ transcendental over $k$.
Choose a monic polynomial $P\in k[t]$ of positive degree whose value
at the residue of $a$ is nonzero at each point of $A$ where $a$ is
regular. One can take $P=t\prod\mu+1$, where the factors $\mu$ are
the minimal polynomials of the algebraic residues; a transcendental
residue cannot be a zero of $P$. The function $c=1/P(a)$ is
transcendental over $k$ and regular at every point of $A$: it is a unit
where $a$ is regular, and vanishes where $a$ has a pole. This is
`AlgebraicGeometry.exists_transcendental_mem_range_stalk`.

The function $c$ defines a finite morphism $C\to\mathbf P^1_k$.
The points of $A$ map into the affine chart with coordinate $c$, whose
inverse image is affine. Thus
`AlgebraicGeometry.exists_affineOpens_forall_mem_of_curve` gives the
affine neighbourhoods required by the general representability theorem
`AlgebraicGeometry.isRepresentable_hilbertPresheaf`, and hence every
$\operatorname{Hilb}^{d}_{C/k}$ is represented. The representing scheme
is separated: for two families of finite subschemes, each inclusion
condition is a closed condition, and their intersection is the equality
condition defining the diagonal
(`AlgebraicGeometry.isSeparated_of_representableBy_hilbertPresheaf`).

The remaining constructions work first for a separated smooth morphism
$X\to S$ of relative dimension one. A finite locally free closed
subscheme of $X_T$ has invertible ideal: on each fibre this follows
from the discrete valuation rings of the smooth curve, and flatness
and finite presentation lift the fibrewise local equations. Thus
`AlgebraicGeometry.IsHilbertSubscheme.isInvertible` makes Hilbert
points into relative effective Cartier divisors. Multiplication of
their ideals adds the divisors. The exact sequence for a product of
local equations shows that this preserves finite local freeness and
adds the ranks (`AlgebraicGeometry.IsHilbertSubscheme.mul`).

Suppose $H_d$ and $H_{d+1}$ represent the corresponding Hilbert
functors. Adding the graph of a point gives

$$
a_d:H_d\times_S X\longrightarrow H_{d+1},\qquad
(D,x)\longmapsto D+\Gamma_x.
$$

This identifies $H_d\times_S X$ with the universal divisor over
$H_{d+1}$. Indeed, if $\Gamma_x\subset E$, the colon ideal
$(I_E:I_{\Gamma_x})$ defines a finite locally free divisor $D$ of
degree $d$ with $E=D+\Gamma_x$
(`AlgebraicGeometry.IsHilbertSubscheme.exists_eq_mul`); cancellation
of an invertible ideal gives uniqueness. Consequently $a_d$ is finite
locally free of degree $d+1$
(`AlgebraicGeometry.exists_addition_hilbertPresheaf`).

The only finite locally free closed subscheme of degree zero is the
empty subscheme, so $H_0\simeq S$. If all the Hilbert functors are
represented, induction now shows that $H_d\to S$ is smooth of relative
dimension $d$. In the induction step $a_d$ is surjective because its
rank is positive, and $H_d\times_S X$ is smooth of relative dimension
$d+1$; smoothness with this dimension descends along the finite locally
free surjection
(`AlgebraicGeometry.smoothOfRelativeDimension_of_representableBy_hilbertPresheaf`).

Return to $C/k$. Iterating the addition maps gives a surjection
$C^d\to H_d$ from a proper geometrically irreducible scheme
(`AlgebraicGeometry.exists_surjective_of_representableBy_hilbertPresheaf_curve`).
Universal closedness descends along this surjection; together with
separatedness and finite type this makes $H_d$ proper. After every
field extension the same surjection proves irreducibility. Smoothness
gives geometric reducedness, so $H_d$ is geometrically integral
(`AlgebraicGeometry.isProper_and_geometricallyIntegral_of_representableBy_hilbertPresheaf_curve`).

Finally take the Hilbert point corresponding to the identity of
$H_d$. Its ideal is invertible, and it is flat over $H_d$, so it is a
relative effective Cartier divisor. Naturality of the representing
bijection identifies its pullback with the divisor classified by
$h:T\to H_d$. Pullback of relative effective Cartier divisors also
commutes with the dual of their ideals, giving the asserted
isomorphism of invertible sheaves
(`AlgebraicGeometry.isRelativeEffectiveCartier_universal_hilbertPresheaf`).
