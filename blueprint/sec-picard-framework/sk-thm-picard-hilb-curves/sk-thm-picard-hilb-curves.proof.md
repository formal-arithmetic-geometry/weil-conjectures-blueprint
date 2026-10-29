+++
kind  = "proof"
of    = "sk-thm-picard-hilb-curves"
uses = ["sk-thm-picard-rr"]
+++
*Representability.* This is the representability of Hilbert functors of
points ([det-thm-picard-hilb-general], Stacks Project, Tag 0B9A): for a
separated morphism such that any finitely many points of a fibre lie in an
affine open, $\Hilb^d$ is a scheme. The hypothesis on affine opens follows from [sk-thm-picard-rr]
(G)+(H): an effective divisor $D_0$ through the points has positive
degree, so $\cO_C(D_0)$ is ample and $C\setminus\operatorname{Supp}D_0$ is
affine. $H_0=\Spec k$, since the only closed subscheme finite locally
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

*Smoothness, properness, integrality.* $H_0=\Spec k$ and $H_1\cong C$,
and the addition map $H_d\times_kC\to H_{d+1}$, $(D,x)\mapsto D+x$, is
finite locally free of degree $d+1$ ([lem-pc-hilb-addition]), so
smoothness of relative dimension $d+1$ descends from $H_d\times_kC$ to
$H_{d+1}$ (Stacks Project, Tag 0B9H; [lem-pc-hilb-smooth]). Iterating,
the addition map $C^d\to H_d$ is finite locally free and surjective, so
$H_d$ is proper, being the image of the proper scheme $C^d$, and
geometrically irreducible, being the image of the geometrically integral
$C^d$; a smooth geometrically irreducible scheme is geometrically
integral (Stacks Project, Tag 0B9I).

The detailed form [thm-pc-hilb-curves] also identifies the $k'$-points of
$H_d$ for a field extension $k'/k$ with the effective Cartier divisors of
degree $d$ on $C_{k'}$, and gives the addition morphisms
$H_{d_1}\times_kH_{d_2}\to H_{d_1+d_2}$, finite locally free of degree
$\binom{d_1+d_2}{d_1}$ ([lem-pc-hilb-addition]).
