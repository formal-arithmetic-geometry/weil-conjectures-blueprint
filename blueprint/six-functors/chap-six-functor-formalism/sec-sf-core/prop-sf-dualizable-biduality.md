+++
id = "prop-sf-dualizable-biduality"
kind = "theorem"
title = "Biduality of a perfect complex"
order = 3382
tags = ["latex:proposition"]
uses = ["def-sf-datum", "def-weil-derived-pullback-tensor-hom", "lem-sf-hom-finite-projective", "prop-sf-dualizable-hom"]
+++
In the setting of [def-sf-datum], let $K\in D^b_{ctf}(X,\Lambda)$ be
quasi-isomorphic, locally on the site of $X$, to a bounded complex of finite
projective $\Lambda_X$-modules. Then $K\to K^{\vee\vee}$ is an
isomorphism, evaluation and coevaluation
being the unit and counit of the tensor–internal-Hom adjunction.

## Proof

Applying [prop-sf-dualizable-hom] twice, with
$P^\bullet$ a bounded complex of finite projective
$\Lambda_X$-modules quasi-isomorphic to $K$, gives
$K^{\vee\vee}\cong(P^{\bullet\vee})^\vee\cong P^\bullet\cong K$, the middle
identification being the termwise double-dual isomorphism of
[lem-sf-hom-finite-projective], and the counit and coevaluation are the
adjunction unit and counit, whose composite is the identity by the triangle
identities.
