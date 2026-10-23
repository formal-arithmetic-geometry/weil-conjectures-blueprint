+++
id = "sk-prop-input-spreading"
kind = "theorem"
title = "Extension from a split generic Galois cover"
order = 2083
uses = ["sk-def-smooth"]
lean = ["AlgebraicGeometry.Scheme.EtaleTorsor.exists_isPullback_of_genericFibre"]
tags = ["sketch"]
+++
Let $S$ be an integral normal qcqs scheme with generic point
$\eta$. Let $a:C\to S$ be qcqs and smooth with geometrically
connected fibres, and let $\sigma:S\to C$ be a section.
Let $Z\to C_\eta$ be a finite étale Galois cover with
group $G$, where $|G|$ is invertible on $S$. Suppose $Z$ has
a $\kappa(\eta)$-rational point over $\sigma(\eta)$.
Then $Z$ extends to a finite étale Galois cover
$\widetilde Z\to C$ with group $G$.

*Complement.* The same holds for torsors under a finite abelian group, not necessarily
connected:
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
