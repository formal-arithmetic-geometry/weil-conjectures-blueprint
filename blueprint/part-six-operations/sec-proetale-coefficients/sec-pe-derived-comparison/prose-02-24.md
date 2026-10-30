+++
id = "prose-02-24"
kind = "hidden"
title = "Cohomology comparison"
order = 83
+++
For a bounded-below complex $K$ on $X_{\acute{e}t}$, the pro-étale
cohomology of $\nu_X^*K$ is the étale cohomology of $K$; bounds on
cohomological dimension are needed only for unbounded complexes (Section [sec-pe-unbounded]). The proof
uses the following acyclicity statement for the direct image
$\nu_{X,*}:\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)\to \operatorname{Mod}(X_{\acute{e}t},\Lambda)$.

This is the theorem that makes the pro-étale site usable for torsion
coefficients: statements of SGA 4 about the cohomology of torsion
sheaves, such as $\mathbf Z/\ell^n$ on a variety, can be quoted. The
reason it holds is that a pro-étale cover of an affine can be refined
to a limit of étale covers, and sections of a classical sheaf on
a limit are the colimit of sections. Hence the Čech complex of a
pro-étale cover is a filtered colimit of étale Čech complexes,
and an injective étale sheaf stays acyclic after pullback
(Lemma [sk-lem-pe-injective-acyclicity]). The theorem itself
(Theorem [sk-prop-sf-comparison]) then follows by resolving. The
comparison fails for non-classical coefficients, as the computation
$H^1(\operatorname{Spec}\mathbf F_q,-)$ at the start of this section
shows. We deduce two consequences: cohomology of a pro-étale affine is
the colimit of the cohomology of its étale approximations, and
classical complexes in $D^+$ are exactly the pullbacks of étale ones.
The second is what proper base change on the pro-étale site needs.
