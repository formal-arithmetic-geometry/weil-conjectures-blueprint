+++
id = "lem-exc-closed-lift-adjunction"
kind = "lemma"
title = "Adjunction for the ind-etale closed lift"
lean = ["Algebra.ClosedLift.exists_natural_homEquiv"]
order = 1088
uses = ["def-exc-ind-etale-closed-lift", "def-weil-pbc-ind-etale-algebra", "lem-exc-closed-lift-filtered", "lem-exc-closed-lift-reduction"]
+++
Let $I\subset A$ be an ideal and $\overline C$ an ind-etale $A/I$-algebra.
For every ind-etale $A$-algebra $D$, the reduction $D/ID$ is ind-etale over
$A/I$, and reduction induces a bijection, natural in $D$ and in $\overline C$,
$$
 \operatorname{Hom}_A(D,H_A(\overline C))
 \xrightarrow{\sim}
 \operatorname{Hom}_{A/I}(D/ID,\overline C).
$$
This identifies $H_A$ as right adjoint to reduction on ind-etale algebras.
