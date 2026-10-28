+++
kind  = "proof"
of    = "prop-sf-pf-reduction"
+++
(1) Put $N=(\Lambda/J)_Y$, so $\rho_Y=-\otimes^L_\Lambda N$, and the comparison of
$Rf^c_!$ with $\rho$ is the projection map at $(-,N)$ followed by
$Lf^*N\cong(\Lambda/J)_X$ [lem-sf-reduction-compatibility]. The square therefore
expresses the associativity of the projection map: tensoring
$\operatorname{PF}_{f,K,L}$ with $N$ and then applying the projection map at
$N$ agrees, through the associativity isomorphisms of $\otimes^L_\Lambda$ and the
monoidality of $Lf^*$, with the projection map at $L\otimes^L_\Lambda N$. By
[lemma-weil-pbc-projection-formula-compactified] the projection map of $c$ is
the composite of the proper-piece map of
[lemma-weil-pbc-projection-formula-proper-piece], which is the transpose of
$\varepsilon\otimes1$ through the monoidality of the pullback, with the
open-piece isomorphism of [lemma-weil-pbc-projection-formula-open-piece].
Both pieces are compatible with associativity: for the proper piece this comes
down to the counit–tensor description and the monoidality of the derived
pullbacks, and for the open piece to its construction from the unit of
$j_!\dashv j^*$. This is an identity of the specified morphisms, proved from
their constructions and not from agreement on stalks.

(2) In the square, the left arrow, the right arrow (by
[lem-sf-reduction-compatibility] (2), $\Lambda$ being finite) and the bottom
right isomorphism are isomorphisms. Hence the top arrow is an isomorphism if and
only if $\operatorname{PF}_{f,K,\rho_YL}$ is.

(3) Since $\Lambda$ is finite, the projection map of $c$ is an isomorphism at
every pair of arguments: the open-piece map is always an isomorphism
[lemma-weil-pbc-projection-formula-open-piece], and the proper-piece map is an
isomorphism by the proper projection formula with torsion coefficients
[lem-amb-proper-coproducts-projection]. So the projection formula holds at
$(K,L)$ and at $(K,\rho_YL)$.
