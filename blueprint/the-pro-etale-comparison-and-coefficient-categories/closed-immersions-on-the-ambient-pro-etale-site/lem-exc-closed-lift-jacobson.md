+++
id = "lem-exc-closed-lift-jacobson"
kind = "lemma"
title = "The closed ideal in the lifted algebra"
order = 2729
lean = ["Algebra.IndEtale.closedLift_le_jacobson"]
uses = ["def-exc-ind-etale-closed-lift", "lem-exc-closed-lift-units"]
+++
For $C=H_A(\overline C)$ in [def-exc-ind-etale-closed-lift], the ideal $IC$
is contained in the Jacobson radical of $C$.

## Proof

The specified map of [def-exc-ind-etale-closed-lift] kills $IC$. Hence for
$z\in IC$ and $c\in C$ the element $1-cz$ maps to one and is invertible by
[lem-exc-closed-lift-units]. The elementary Jacobson-radical criterion now
gives the assertion: if a maximal ideal omitted $z$, then $cz=1$ in its
residue field for some $c$, contradicting invertibility of $1-cz$.
