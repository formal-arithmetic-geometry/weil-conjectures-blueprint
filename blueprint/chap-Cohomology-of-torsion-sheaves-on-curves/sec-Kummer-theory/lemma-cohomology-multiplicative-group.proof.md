+++
kind = "proof"
of = "lemma-cohomology-multiplicative-group"
order = 1566
uses = ["theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "lemma-acyclic-resolutions", "lemma-finite-morphisms", "definition-compactification-refinement", "lemma-p-torsion-affine-curve-characteristic"]
+++
We compute on $C_{\acute{e}t}$. In degree one, descent for invertible modules
identifies $\mathbf G_m$-torsors with line bundles. In degrees at least
two the vanishing comes from Tsen's theorem, which we prove first (see
also [Stacks, [03RM](https://stacks.math.columbia.edu/tag/03RM)]). There are three steps: Tsen's theorem,
proved by counting dimensions with Riemann–Roch; the vanishing of the
Brauer group and of the Galois cohomology of $k(C)$; and the passage from
the generic point to $C$ by the divisor sequence.

Tsen's theorem says that $k(C)$ is $C_1$, that is, a homogeneous form
of degree $d$ in $m>d$ variables with coefficients in $k(C)$ has a
nonzero zero.  To see this, let $\overline C$ be the smooth proper model
of $k(C)$, of genus $g$, choose an effective divisor $D$ on
$\overline C$ bounding the poles of all coefficients, and let the
unknowns range over $H^0(\overline C,\mathcal O(NH))$ for an effective divisor
$H$ of positive degree.  The value of the form then lies in
$H^0(\overline C,\mathcal O(dNH+D))$.  Once $N\deg H>2g-2$, we know both
dimensions by Theorem [theorem-riemann-roch-coherent-serre-duality].  In
terms of bases, the $m$ unknowns amount to $m(N\deg H+1-g)$ unknowns in
$k$. Each coordinate of the value, in a basis of the target space, is a
homogeneous polynomial of degree $d$ in these unknowns, so the vanishing
of the value amounts to $dN\deg H+\deg D+1-g$
homogeneous polynomial equations in them.  The number of unknowns minus the number of equations is
$(m-d)N\deg H+(m-1)(1-g)-\deg D$, which is positive for large $N$
because $m>d$.  Since $k$ is algebraically closed, homogeneous equations
in more unknowns than equations have a nonzero solution [Stacks, [03RD](https://stacks.math.columbia.edu/tag/03RD)].

The reduced norm form of a division algebra of degree $d>1$ over $k(C)$
has degree $d$ in $d^2>d$ variables and does not vanish on a nonzero
element.  Therefore Tsen's theorem implies that $\operatorname{Br}(k(C))=0$
[Stacks, [03RF](https://stacks.math.columbia.edu/tag/03RF)].  The same holds for every finite extension of $k(C)$,
since it is again the function field of a curve over $k$. A field all of
whose finite extensions have trivial Brauer group has
$H^q(K,(K^{\mathrm{sep}})^\times)=0$ for all $q\geq1$ [Stacks, [03R8](https://stacks.math.columbia.edu/tag/03R8)]; hence
this holds for $K=k(C)$. The divisor
sequence relates $\mathbf G_m$ on $C_{\acute{e}t}$ to the pushforward of the
multiplicative group at the generic point and to skyscraper sheaves
$\mathbf Z$ at the closed points. The former has no higher cohomology by
this Galois vanishing, and the latter have none because the residue
fields are algebraically closed. From the long exact cohomology sequence
we conclude that $H^q(C_{\acute{e}t},\mathbf G_m)=0$ for $q\geq2$.

By Theorem [theorem-bounded-below-cohomology-comparison] these
identifications carry over to $C_{\mathrm{pro}\acute{e}t}$, and they are natural because
the comparison maps, the identification of torsors and the restriction
maps are functorial.
