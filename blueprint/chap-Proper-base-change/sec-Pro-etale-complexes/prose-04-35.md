+++
id = "prose-04-35"
kind = "hidden"
title = "Pro-étale complexes (1)"
order = 401
+++
The six operations live on the [pro-étale site](@definition-small-pro-etale-site), where we also meet [torsion](@definition-torsion-sheaves)
sheaves of modules over rings that are not torsion, such as $\mathcal O_E$. So far
[$\mathrm{PBC}_\Lambda(f)$](@definition-torsion-pbc-property) is known on the étale site only when $\Lambda$ is
torsion
(Propositions [proposition-proper-base-change-projective-line] and [proposition-proper-base-change-etale-site]).
We therefore drop the condition on $\Lambda$, keeping [torsion](@definition-torsion-sheaves)
cohomology sheaves, and pass to [classical](@definition-classical-pro-etale-sheaves) pro-étale complexes by the
comparison theorems of Chapter [chap-The-pro-etale-site].

The reduction to torsion rings is possible because a [torsion](@definition-torsion-sheaves) sheaf of $\Lambda$-modules is a
filtered colimit of sheaves killed by an integer $n$. Such a sheaf
has a finite filtration with quotients killed by primes $p$, and these
quotients are modules over $\Lambda/p\Lambda$. Moreover, the cohomology of a sheaf
of modules is that of its underlying abelian sheaf, so the [base change
map](@definition-derived-base-change-map) does not depend on which ring we regard as the coefficients.

For the passage to the [pro-étale site](@definition-small-pro-etale-site) we use two facts: a [classical](@definition-classical-pro-etale-sheaves)
complex in $D^+$ is [$\nu_X^*$](@proposition-comparison-morphism-inverse-image) of an étale one
(Corollary [corollary-bounded-below-classical-complexes]), and [$\nu^*$](@proposition-comparison-morphism-inverse-image)
commutes with $g^*$ and with direct images along proper maps
(Theorem [theorem-comparison-direct-images]). Taking for $g$ a geometric
point then shows that the stalks of $Rf_*K$ are the cohomology of the
geometric fibres (Corollary [corollary-cohomology-geometric-fibres]).
