+++
kind  = "proof"
of    = "lem-cbc-exact-functor-rlim"
+++
By [prop-weil-pbc-roos-triangle], $M_\bullet$ sits in the
distinguished triangle

$$
\Rlim M_\bullet\to R\!\prod_nM_n\xrightarrow{1-s}R\!\prod_nM_n
\to(\Rlim M_\bullet)[1].
$$

The functor $F$ is exact, so applying $F$ produces a
distinguished triangle with third vertex $F(\Rlim M_\bullet)$;
on the two derived products $F$ is computed levelwise, because
$F$ commutes with the evaluations of
[def-weil-pbc-derived-inverse-limit] and with the countable
products of the Roos triangle representation, so the image of
$1-s$ is $1-F(s)$. Hence $F(\Rlim M_\bullet)$ is a cone of
$1-F(s)$ over the tower $F(M_\bullet)$; and
[prop-weil-pbc-roos-triangle] applied to $F(M_\bullet)$
exhibits $\Rlim F(M_\bullet)$ as a cone of $1-F(s)$ as well.
Cones of a fixed morphism in a triangulated category are
canonically isomorphic, and the canonical map of the statement is
that comparison, so it is an isomorphism.
