+++
kind = "proof"
of = "lemma-finite-morphisms--1"
order = 384004
uses = []
+++
The geometric fibre is finite: in an affine neighbourhood of the image of
$\bar w$, its points are the homomorphisms from a finite algebra to
$\Omega$ over the given point of the base.

Compute $(u_*F)_{\bar w}$ as the filtered colimit of $F(U\times_W V)$ over
pointed étale neighbourhoods $U$ of $\bar w$. The split neighbourhoods are
cofinal: over such a neighbourhood, $U\times_W V$ is a disjoint union of
open and closed pieces $P_{\bar v}$ indexed by the geometric points
$\bar v$ over $\bar w$, with each piece containing its corresponding point.
The sheaf condition gives

$$
F(U\times_W V)\simeq\prod_{u\bar v=\bar w}F(P_{\bar v}).
$$

Filtered colimits in $A$ are exact and therefore commute with these finite
products. For each $\bar v$, the pieces $P_{\bar v}$ are cofinal among its
pointed étale neighbourhoods, so the corresponding colimit is $F_{\bar v}$.
The resulting isomorphism has the restriction maps on germs as its
components; their naturality in $F$ gives the asserted naturality.
