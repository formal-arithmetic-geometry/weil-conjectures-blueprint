+++
kind  = "proof"
of    = "thm-sf-fullcd-class"
+++
The two clauses of [def-sf-fullcd-class] are the two clauses of
[def-weil-full-cohomological-dimension] read on the blueprint's
coefficient class, and [thm-sf-fullcd-used-class] is exactly their
assertion with the coefficient sheaves of that class. Indeed the class
quantified over in that theorem is
[def-sf-fullcd-used-class], which is by its definition the class of
étale origin on the finite-type source $\overline X$, the same class that
[def-sf-fullcd-class] quantifies over; the identification of that class
with the constructible one, used only for reading the statement, is
[lem-sf-proetale-constructible-origin]. The absolute clause is
therefore the first clause of [thm-sf-fullcd-used-class], whose bound
$2\dim\overline X$ is the one of [thm-sf-fullcd-etale-origin]. The
relative clause is the second clause of [thm-sf-fullcd-used-class],
which asserts the vanishing of the base-changed direct images for every base
change $V\to Y$ and every coefficient sheaf of the class; the restriction
of such a sheaf to the base-changed source is again a coefficient sheaf of
the class there, by [lem-sf-fullcd-class-restriction], so the two
statements quantify over the same base-changed coefficients, and the second
clause of [def-sf-fullcd-class] is exactly that relative clause. The
last sentence of the statement is [prop-sf-comparison-bound-zero], the
residual $2\dim\overline X$ being the étale direction of the Leray
spectral sequence of [thm-sp-grothendieck]; the comparison morphism
that appears there is the one of
[def-weil-pbc-site-comparison-morphism].
