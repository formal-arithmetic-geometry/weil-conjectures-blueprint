+++
kind = "proof"
of = "lemma-integral-changes-source-base--2"
order = 678004
uses = ["definition-underived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree"]
+++
The base change $\pi'$ of $\pi$ is integral. Direct image along $\pi'$
is exact, and the derived base change map for $\pi$ is an isomorphism
(`AlgebraicGeometry.Etale.preservesFiniteColimits_lowerStar_of_isIntegralHom`
and `AlgebraicGeometry.Etale.isIso_derivedBaseChangeMapPlus_of_isIntegralHom`).
The underived exchange is checked on geometric stalks using henselian comparison
[theorem-comparison-over-henselian-pair-degree].

Apply the vertical pasting law [lemma-identity-pasting] to the square for
$f_1$ and the square for $\pi$. Since exactness of $\pi'_*$ identifies
$H^qR\pi'_*K$ with $\pi'_*H^qK$, taking degree-$q$ cohomology identifies
$b^q_{f,M}$ with $\pi'_*b^q_{f_1,M}$, up to isomorphisms of source and
target. This is
`AlgebraicGeometry.Etale.nonempty_arrowIso_baseChangeHomologyMap_comp`.

The functor $\pi'_*$ preserves isomorphisms and reflects them, even when
$\pi'$ is not surjective
(`AlgebraicGeometry.Etale.reflectsIsomorphisms_lowerStar_of_isIntegralHom`).
The two base change maps are therefore isomorphisms simultaneously.
