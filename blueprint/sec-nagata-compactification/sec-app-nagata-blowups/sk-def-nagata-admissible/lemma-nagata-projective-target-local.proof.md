+++
kind  = "proof"
of    = "lemma-nagata-projective-target-local"
+++
Properness is a Zariski-local property on the target. Apply the verified
target-locality instance
`AlgebraicGeometry.IsProper.instIsZariskiLocalAtTarget` to the open
cover $(V_i)$; its local hypotheses are exactly the properness hypotheses in
the statement, and it returns that $f$ is proper.

*Warning.* The analogous assertion with ``projective'' in place of
``proper'' is false for the finite-projective-space definition used here;
see Stacks Project Tag 08J0. No projectivity conclusion is used below.
