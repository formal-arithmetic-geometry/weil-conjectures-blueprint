+++
kind  = "proof"
of    = "prop-exc-finite-etale-adjoint"
+++
By [lem-fet-locally-trivial], there is an etale covering of $X$
over which $V$ is a finite disjoint union of copies of the base.
This is also a covering for [def-weil-pbc-proetale-site].
On such a member, write the sheets as $1,\ldots,r$. A sheaf on $V$
is a tuple $(M_1,\ldots,M_r)$; direct image and inverse image of
[def-weil-derived-direct-image], [def-weil-derived-pullback-tensor-hom]
are respectively

$$
(M_1,\ldots,M_r)\longmapsto\bigoplus_{s=1}^r M_s,
\qquad N\longmapsto(N,\ldots,N).
$$

Finite sums of modules are exact. Moreover,
$\operatorname{Hom}(\bigoplus_s M_s,N) =\prod_s\operatorname{Hom}(M_s,N)$.
These formulas commute with permutations of the sheets; therefore the
adjunction maps glue on overlaps. Both functors are exact, so their unit,
counit, and triangular identities descend from complexes to the ordinary
derived categories. Finally $e$ is proper, so its proper
compactification is itself and $Re_!=Re_*$.
