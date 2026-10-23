+++
kind  = "proof"
of    = "lem-sf-reduction-compatibility"
+++
(1) The derived pullback is computed termwise and is strong monoidal for the
derived tensor product [def-weil-derived-pullback-tensor-hom]; applied to
$L\otimes^L_\Lambda(\Lambda/J)_Y$ this gives the first isomorphism, natural in
$L$. The pullback of a constant sheaf placed in degree $0$ is the constant sheaf
with the same value, which gives $Lf^*(\Lambda/J)_Y\cong(\Lambda/J)_X$.

(2) Naturality holds because the comparison is a composite of natural maps.
Write $N=(\Lambda/J)_Y$. By [lemma-weil-pbc-projection-formula-compactified]
the projection map of $c$ at $(K,N)$ is the composite of the projection map
$\pi_{r,j_!K,N}:Rr_*(j_!K)\otimes^L_\Lambda N\to Rr_*(j_!K\otimes^L_\Lambda Lr^*N)$
of the proper piece [lemma-weil-pbc-projection-formula-proper-piece] with
$Rr_*$ applied to the inverse of the open-piece isomorphism
$j_!(K\otimes^L_\Lambda Lj^*Lr^*N)\cong j_!K\otimes^L_\Lambda Lr^*N$
[lemma-weil-pbc-projection-formula-open-piece]. The open-piece map is an
isomorphism for every $N$. If $\Lambda$ is finite, it is torsion, and the
projection map of the proper morphism $r$ is an isomorphism for all arguments
by the proper projection formula [lem-amb-proper-coproducts-projection]. Hence
the projection map of $c$ at $(K,N)$ is an isomorphism, and so is its
composite with the isomorphism
$Rf^c_!(K\otimes^L_\Lambda Lf^*N)\cong Rf^c_!(K\otimes^L_\Lambda(\Lambda/J)_X)$
coming from (1). Taking $c$ to be the chosen compactification of $f$ gives the
last assertion.
