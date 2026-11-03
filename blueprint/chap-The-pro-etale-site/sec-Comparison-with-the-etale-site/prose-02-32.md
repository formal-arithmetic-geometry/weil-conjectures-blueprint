+++
id = "prose-02-32"
kind = "hidden"
title = "Comparison with the étale site (1)"
order = 119
+++
For a bounded-below complex $K$ on $X_{\acute{e}t}$, the pro-étale
cohomology of $\nu_X^*K$ is the étale cohomology of $K$
(Theorem [theorem-bounded-below-cohomology-comparison]). Bounds on
cohomological dimension are needed only for unbounded complexes
(Section [sec-Unbounded-complexes]). With this theorem, statements of SGA 4
about the cohomology of torsion sheaves, such as $\mathbf Z/\ell^n$ on a
variety, can be quoted on the pro-étale site.

The theorem rests on two facts. A pro-étale cover of an affine can be
refined to a limit of étale covers, and sections of a classical sheaf on
a limit are the colimit of sections. It follows that the Čech complex
of a pro-étale cover is a filtered colimit of étale Čech
complexes. Because of this, an injective étale sheaf stays acyclic after
pullback (Lemma [lemma-acyclicity-pulled-back-injectives]), and
resolving by injectives gives the theorem. For non-classical coefficients
the comparison fails, as the computation of
$H^1(\operatorname{Spec}\mathbf F_q,\mathbf Z_\ell)$ in Section [sec-Weil-cohomology]
shows.

It follows that the cohomology of a pro-étale affine is the colimit of the
cohomology of its étale approximations
(Corollary [corollary-cohomology-pro-etale-affine]). Moreover, classical
complexes in $D^+$ are exactly the pullbacks of étale ones
(Corollary [corollary-bounded-below-classical-complexes]), and this is
what we need for proper base change on the pro-étale site.
