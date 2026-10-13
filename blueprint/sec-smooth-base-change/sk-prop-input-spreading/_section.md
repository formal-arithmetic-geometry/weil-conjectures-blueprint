+++
id = "sk-prop-input-spreading"
kind = "proposition"
title = "Spreading a finite étale Galois cover"
order = 1459
uses = ["sk-def-smooth"]
lean = ["AlgebraicGeometry.Scheme.EtaleTorsor.exists_isPullback_of_genericFibre"]
tags = ["sketch"]
+++
Let $S$ be a qcqs integral normal scheme with generic point $\eta$,
let $C\to S$ be a qcqs smooth morphism with geometrically connected
fibres, and fix a section $\sigma:S\to C$. Let $M$ be a finite abelian
group with $|M|$ invertible on $S$, let $Z\to C_\eta$ be an $M$-torsor,
i.e. a finite étale Galois cover with group $M$ (not necessarily
connected), and assume $Z$ carries a $\kappa(\eta)$-rational
point above $\sigma(\eta)$. Then there is an $M$-torsor
$\widetilde Z\to C$ whose restriction to $C_\eta$ is the given torsor
$Z\to C_\eta$: there is an $M$-equivariant morphism $Z\to\widetilde Z$
over $C_\eta\to C$ making the resulting square Cartesian.
