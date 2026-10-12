+++
kind  = "proof"
of    = "sk-thm-sf-ctf-stability"
uses = ["sk-prop-sf-rf-shriek-preservation"]
+++
(i) pullback: the pullback of a flat model is flat, and pullback preserves
bounded constructibility (lem:weil-pbc-pullback-preserves-bounded-constructible);
the Tor clause is exactness of $Lf^*$ on a bounded flat model. (ii) tensor:
additivity
of Tor amplitude and the weak-Serre property of constructible sheaves
of Tor amplitudes; internal Hom: [sk-thm-sf-hom-ctf] on the étale
site, and on the pro-étale site the internal-Hom comparison of
the internal-Hom comparison across the sites, which is an isomorphism for
every
pair of bounded constructible étale complexes and therefore needs no
site-perfectness hypothesis. (iii) direct image: on the étale site
[sk-thm-sf-direct-image-tor-amplitude]; on the pro-étale site
[sk-cor-sf-direct-image-ctf]; for proper $f$ the same through
$Rf_!=Rf_*$. (iv) compact support: the open-immersion case
([sk-lem-sf-open-ctf]: extension by zero is exact and commutes with the
constant tensor) plus the proper case, assembled along a compactification
([sk-thm-nagata-compactification], the assembly being independent of the
choice by [sk-prop-sf-comp-coherence]), the proper case using the projection
formula of [sk-rem-sf-pf-done]. (v) prop:sf-rf-shriek-preservation.
(vi) $\mathbb D_X$ is $\RHom_X(-,\omega_X)$ with $\omega_X=Ra_X^!\Lambda\in \Dctf$ by (v) for the structure morphism, so (ii) applies; the anti-equivalence
is prop:sf-biduality-general. (vii) the amplitude intervals depend only on the
input intervals, on the dimension bound and on the coefficient-free torsion
bound, hence not on the stage; the finite-level comparison isomorphisms are
[sk-prop-sf-pf-reduction] for the projection formula and the recorded
clause of prop:functor-package otherwise.

*Conditional on* clause (vii) in the case of a reduction tower for which no single
finite étale cover trivialises all stages. Everything else in the theorem
is unconditional; in particular clauses (v) and (vi) carry no admissibility
hypothesis, the exceptional adjoint being the constructible one of
[sk-def-sf-operations] (vi) (the former residue "vanishing for pro-étale
module sheaves not of étale origin" concerned only the ambient
[sk-prop-sf-existence] (b), which is false in general and not used,
[sk-rem-sf-fullcd-scope]). The one residue is the reduction
towers with no uniform trivializing cover.
