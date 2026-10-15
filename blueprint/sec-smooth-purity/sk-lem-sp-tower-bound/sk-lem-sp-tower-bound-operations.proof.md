+++
kind = "proof"
of = "det-sp-tower-shriek-levels"
+++
(1) $j_{!,\bullet}$ is levelwise extension by zero, exact, so
$(j_{!,\bullet}C_\bullet)_n=j_!C_n$. By [det-sp-tower-injective-components],
$(R\bar f_{*,\bullet}D_\bullet)_n\simeq R\bar f_*D_n$ for every bounded below
$D_\bullet$; apply it to $D_\bullet=j_{!,\bullet}C_\bullet$.

(3) Evaluation functors are exact and jointly conservative on the abelian
category of towers (kernels and cokernels are levelwise), so a map of complexes
of towers is a quasi-isomorphism iff it is so at every level, i.e. iff its cone
is acyclic at every level.

(2) Each of these maps is defined in the tower category by the same recipe as
in the finite case (transposes of units and counits of the levelwise adjunctions,
associativity of tensor products — flatness and tensor products of towers being
levelwise), so by (1) and exactness of evaluation it evaluates at level $n$ to
the corresponding finite map, which is an isomorphism; by (3) the tower map is
an isomorphism. For the localization triangle, the levelwise sequences
$0\to j_!j^*C_n\to C_n\to i_*i^*C_n\to0$ are exact and compatible with the
transitions, giving a short exact sequence of towers and hence a triangle.
