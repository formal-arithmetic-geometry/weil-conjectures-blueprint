+++
id = "lem-exc-closed-lift-reduction"
kind = "lemma"
title = "Reduction of the ind-etale lift"
order = 2728
lean = ["Algebra.IndEtale.closedLift_quotient_equiv"]
uses = ["def-exc-ind-etale-closed-lift", "lem-exc-closed-lift-filtered", "lem-exc-etale-algebra-lift", "lem-exc-closed-lift-units"]
+++
For the lift $C=H_A(\overline C)$ of [def-exc-ind-etale-closed-lift], the
specified map $C/IC\to\overline C$ is an isomorphism.

## Proof

The construction of [def-exc-ind-etale-closed-lift] is ind-etale by
[lem-exc-closed-lift-filtered]. Write $\overline C$ as a filtered colimit of
etale finite-presentation $A/I$-algebras. Every term lifts by
[lem-exc-etale-algebra-lift]; these lifts are objects of the indexing
category. Every element of $\overline C$ therefore comes from $C$, so
$C/IC\to\overline C$ is surjective. Both its source and target are ind-etale
over $A/I$. Their relative map is ind-etale and hence flat by the stability
lemma for ind-etale algebras.

Let $J$ be the kernel of the preceding surjection $C/IC\to\overline C$.
Flatness of the quotient implies that for each $x\in J$ one has $x=ex$ for
an $e\in J$: tensor the injection $(x)\subset C/IC$ with the quotient to
obtain $(x)\cap J=J(x)$. Lift $e$ to $C$. The element $1-e$ maps to one in
$\overline C$, so [lem-exc-closed-lift-units] makes it invertible in
$C/IC$. Thus $x=0$, proving the reduction isomorphism.

Unresolved dependencies: def:weil-pbc-ind-etale-algebra, lem:weil-pbc-ind-etale-stability
