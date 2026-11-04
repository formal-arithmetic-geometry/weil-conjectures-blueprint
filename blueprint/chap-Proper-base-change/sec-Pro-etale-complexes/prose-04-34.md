+++
id = "prose-04-34"
kind = "hidden"
title = "Pro-étale complexes (1)"
order = 396
+++
The six operations live on the pro-étale site, where we also meet torsion
sheaves of modules over rings that are not torsion, such as $\mathcal O_E$. So far
$\mathrm{PBC}_\Lambda(f)$ is known on the étale site only when $\Lambda$ is
torsion
(Propositions [proposition-proper-base-change-projective-line] and [proposition-proper-base-change-etale-site]).
We therefore drop the condition on $\Lambda$, keeping torsion
cohomology sheaves, and pass to classical pro-étale complexes by the
comparison theorems of Section [chap-The-pro-etale-site].

A torsion sheaf of $\Lambda$-modules is a
filtered colimit of sheaves killed by an integer $n$. Such a sheaf
has a finite filtration with quotients killed by primes $p$, and these
quotients are modules over $\Lambda/p\Lambda$. The cohomology of a sheaf
of modules is that of its underlying abelian sheaf, so the base change
map does not depend on which ring we regard as the coefficients.

For the passage to the pro-étale site we use two facts. A classical
complex in $D^+$ is $\nu_X^*$ of an étale one
(Corollary [corollary-bounded-below-classical-complexes]). And $\nu^*$
commutes with $g^*$ and with direct images along proper maps
(Theorem [theorem-comparison-direct-images]). Taking for $g$ a geometric
point then shows that the stalks of $Rf_*K$ are the cohomology of the
geometric fibres (Corollary [corollary-cohomology-geometric-fibres]).
