+++
kind = "proof"
of = "lemma-scheme-frobenius-geometric-frobenius--4"
order = 953007
uses = ["definition-action-correspondence", "proposition-composition-base-change-rf-shriek", "proposition-composition-open-restriction-compactifications-f"]
+++
Expand the operator of the correspondence
$(X,\operatorname{id}_X,h,v)$ from [definition-action-correspondence].
Under the identity isomorphisms, the counit for
$R(\operatorname{id}_X)_!\dashv(\operatorname{id}_X)^!$ is the identity.
The composition isomorphism for $Ra_{X!}R(\operatorname{id}_X)_!$ then
removes the exceptional identity leg. This is
`AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.globalOperator_mk_id`.

The coefficient map of the graph is $v$ followed by
$K\simeq(\operatorname{id}_X)^!K$. Cancel this isomorphism with its inverse.
The remaining composite is $h^\sharp$ followed by $\RGammac(X,v)$.
