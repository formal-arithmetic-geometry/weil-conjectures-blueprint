+++
id = "prose-04-20"
kind = "hidden"
title = "Proper base change and geometric fibres"
order = 219
+++
By Propositions [sk-thm-p1] and [sk-thm-reduction], $\mathrm{PBC}_\Lambda(f)$
holds on the étale site for every proper $f$ and every ring $\Lambda$
that is torsion as an abelian group. The six operations are defined on the
pro-étale site and need arbitrary rings. We now drop the condition on
$\Lambda$, keeping torsion cohomology sheaves, and pass to classical
pro-étale complexes by the comparison theorems of
Section [sec-proetale-coefficients].

Both steps are formal. A torsion sheaf of $\Lambda$-modules is a
filtered colimit of sheaves killed by an integer $n$, and such a sheaf
has a finite filtration with quotients killed by primes $p$, which are
modules over $\Lambda/p\Lambda$. Since cohomology of a sheaf of modules
is that of its underlying abelian sheaf, the base change map does not
depend on which ring we regard as the coefficients. The passage to the
pro-étale site uses that a classical complex in $D^+$ is $\nu_X^*$ of
an étale one (Corollary [sk-cor-pe-classical-derived]) and that $\nu^*$
commutes with $g^*$ and with direct images along proper maps
(Theorem [sk-thm-pe-direct-image-comparison]). Taking for $g$ a geometric
point gives the answer to the question at the start of this section:
the stalks of $Rf_*K$ are the cohomology of the geometric fibres
(Corollary [sk-cor-pbc-torsion-stalk]). On the pro-étale site the stalk
is the value of $\bar y^*Rf_*K$ on the point $\operatorname{Spec}\Omega$,
whose topos is that of condensed sets, so we also check that for a
classical complex this value is the étale stalk.
