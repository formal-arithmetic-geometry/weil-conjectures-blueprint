+++
kind  = "proof"
of    = "prop-weil-pbc-common-stage-calculus"
+++
The relation of [def-weil-pbc-finite-stage-pair-category] is reflexive and
symmetric from the definitions, and transitive: if $(M,u)\sim(N,v)$ and
$(N,v)\sim(Q,w)$ with witnesses $P_1,P_2$, transport all to their compositum
$P$, where both equalities hold by the transport formula $(u_N)_P=u_P$ and
the unit/associator equations of [prop-weil-pbc-scalar-extension]. The same
formula shows that transport is additive and satisfies $(u_N)_P=u_P$ for
$M\subset N\subset P$ (the associator cocycle), so addition, negatives,
identities and composition, computed after transport to one common finite
field, are independent of the representatives and of the field; the
finite-stage additive category laws transported to a common field (with
$T_{F/E}$ additive) make $\mathcal P_T$ an additive category. Every finite
diagram is represented over one finite field by transporting objects and
morphisms (via the $\gamma$-isomorphisms of
[def-weil-pbc-finite-stage-pair-category]), and a finite list of asserted
equalities holds in $\mathcal P_T$ exactly when the transported equalities
hold over a further common stage, by the definition of the equivalence. For
the shift: equivalent representatives define equivalent shifted
representatives by naturality of $\sigma$ and the associator equations of
[prop-weil-pbc-scalar-extension], so $[1]$ and $[-1]$ are well-defined
additive endofunctors, $[1]$ has inverse $[-1]$ (the finite-stage shift
laws), and the inclusion $j_E$ commutes with the shifts through the
specified comparison.
