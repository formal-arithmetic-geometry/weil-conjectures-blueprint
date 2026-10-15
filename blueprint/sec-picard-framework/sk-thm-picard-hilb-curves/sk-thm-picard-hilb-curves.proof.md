+++
kind  = "proof"
of    = "sk-thm-picard-hilb-curves"
uses = ["sk-thm-picard-hilb-general", "sk-thm-picard-rr"]
+++
*Representability.* This is Grothendieck's theorem that the Hilbert
functor of a projective scheme with fixed Hilbert polynomial is
represented by a projective scheme ([sk-thm-picard-hilb-general]),
applied with constant polynomial $d$; Stacks Project, Tags 0B9A and 0B9I
give the construction for curves. (Its hypothesis that finitely many
points of $C$ lie in an affine open follows from [sk-thm-picard-rr]
(G)+(H): an effective divisor $D_0$ through the points has positive
degree, so $\cO_C(D_0)$ is ample and $C\setminus\operatorname{Supp}D_0$ is
affine.) $H_0=\Spec k$, since the only closed subscheme finite locally
free of rank $0$ is empty.

*Objects are Cartier divisors.* On a smooth fibre, local rings at closed
points are discrete valuation rings, so a zero-dimensional closed
subscheme is an effective Cartier divisor. The flatness criterion for
Cartier divisors ($C_T\to T$ flat, $D$ flat over $T$ and Cartier on
fibres) gives the relative assertion. Conversely a relative effective
Cartier divisor finite over $T$ is flat and finitely presented, hence
finite locally free. The universal closed subscheme $D_d$ is therefore a
relative effective Cartier divisor, with invertible sheaf $\cO(D_d)$, and
by the Yoneda lemma the point classified by $h:T\to H_d$ is its pullback.

*Smoothness.* At a divisor $D$ over a field, the Hilbert tangent space is
$\Hom(\mathcal I_D,\cO_D)$, of dimension $d$ ($\mathcal I_D$ invertible,
$\cO_D$ of length $d$), and the obstruction group
$\Ext^1(\mathcal I_D,\cO_D)=H^1(C,\mathcal I_D^{-1}\otimes\cO_D)$ vanishes
because $\mathcal I_D$ is invertible and $D$ is finite. Hence $H_d$ is
smooth of dimension $d$. (The detailed nodes give an alternative route:
the addition morphism $H_d\times_kC\to H_{d+1}$ is finite locally free
of degree $d+1$, hence faithfully flat, so smoothness descends by
induction on $d$, starting from $H_1\cong C$.)

*Geometric integrality.* The addition map $C^d\to H_d$ is surjective on
geometric points: an effective divisor over an algebraically closed
field is a sum of points with multiplicities. The image of the
geometrically integral $C^d$ is therefore geometrically irreducible, and
$H_d$, being smooth, is geometrically reduced; so $H_d$ is geometrically
integral. Properness follows from projectivity (or as the image of the
proper $C^d$).

*Complements.* The $k'$-points are, by the Cartier criterion, the
effective Cartier divisors of degree $d$ on $C_{k'}$, and the fibre of
$\cO(D_d)$ over $[D]$ is $\cO_C(D)$ by pullback of the universal
divisor. The addition morphism multiplies ideal sheaves of relative
effective Cartier divisors; its finiteness and local freeness of degree
$\binom{d_1+d_2}{d_1}$ are the detailed node `lem-pc-hilb-addition`.
