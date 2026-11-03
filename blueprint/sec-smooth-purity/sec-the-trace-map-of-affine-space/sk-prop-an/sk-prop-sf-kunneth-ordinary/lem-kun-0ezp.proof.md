+++
kind  = "proof"
of    = "lem-kun-0ezp"
+++
*Step 1 (etale $L$-schemes).* An etale morphism is locally of finite
presentation, so an etale $L$-scheme is a disjoint union of affine pieces
which are etale and of finite presentation over $L$, hence etale and of
finite type. An etale finite type scheme over a field is finite over that
field, and a finite etale algebra over a field is a product of finite
separable field extensions; since $L$ is separably closed
([def-pc-separably-closed]) each of those extensions is $L$ itself.
Hence every object of the small etale site of $X$,
[def-weil-pbc-etale-site], is a disjoint
union of copies of $X$.

*Step 2 (the global sections functor is exact).* By Step 1 every object
of $X_{\Et}$ is a coproduct of copies of the terminal object $X$, and for
a coproduct the sheaf axiom gives
$F(\coprod_jX)\cong\prod_jF(X)$ for a sheaf $F$ of
[def-weil-pbc-etale-sheaves]. In particular every covering of $X$
contains a summand mapping isomorphically onto $X$, so a section of a
quotient sheaf admits a lift over $X$: the global sections functor
$\Gamma(X_{\Et},-)$ is evaluation at $X$, and the exactness of the
sequence of sheaves gives exactness after evaluation. Hence
$\Gamma(X_{\Et},-)$ is exact, and its derived functors of
[def-weil-pbc-etale-cohomology] vanish in positive degrees.

*Step 3 (higher direct images).* Let $U\to Y$ be etale. Then
$X\times_YU\to X$ is etale (base change of an etale morphism), so it is a
disjoint union of copies of $X$ by Step 1, and

$$
H^q\bigl((X\times_YU)_{\Et},F\bigr)
=\prod\nolimits_jH^q(X_{\Et},F)=0\qquad(q>0)
$$

by Step 2, cohomology of a disjoint union being the product of the
cohomologies. Hence the presheaf $U\mapsto H^q(X\times_YU,F)$ vanishes for
$q>0$, and therefore so does its sheafification, which is
$R^qf_*F$ by [def-weil-pbc-direct-image].
