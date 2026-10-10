+++
kind  = "proof"
of    = "lem-weil-pbc-hypercover-free-resolution"
+++
Exactness is a local assertion about the sheaves of
[def-weil-pbc-etale-sheaves]. A local chain has finite support. Choose
locally a vertex in $U_0$, using its covering of $X$. For each of the
finitely many simplices in a given chain, including its faces, construct a
cone to this vertex. Inductively, the cone on the boundary of a simplex has
already been specified. The matching-cover condition in
[def-weil-pbc-finite-split-hypercover] supplies a simplex with exactly those
faces after an etale cover. Take a common refinement for the finitely many
choices. Denote this cone operation by $h$. The alternating-face formula
gives $\partial h+h\partial=1$ on the augmented finite collection of chains:
the faces through the new vertex cancel and the remaining face is the
original simplex. Thus every cycle is locally a boundary. In degree zero the
same construction uses the augmentation, and proves its surjectivity as well.

The defining free-sheaf adjunction gives $\operatorname{Hom}(\mathbb
Z[V],I)=I(V)$. Applying $\operatorname{Hom}(-,I)$ to the exact augmented
complex is exact because $I$ is injective, which proves the assertions about
$C^\bullet(U,I)$. Replacing free abelian groups by free modules gives the
identical proof for a constant coefficient ring.
