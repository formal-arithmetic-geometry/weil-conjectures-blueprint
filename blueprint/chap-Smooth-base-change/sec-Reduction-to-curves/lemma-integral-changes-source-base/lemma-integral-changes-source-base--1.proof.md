+++
kind = "proof"
of = "lemma-integral-changes-source-base--1"
order = 678003
uses = ["definition-underived-base-change-map", "lemma-identity-pasting", "theorem-comparison-over-henselian-pair-degree", "lemma-injectivity-base-change-map-degree"]
+++
Direct image along an integral morphism is exact and commutes with base
change. In Lean these facts are
`AlgebraicGeometry.Etale.preservesFiniteColimits_lowerStar_of_isIntegralHom`
and `AlgebraicGeometry.Etale.isIso_derivedBaseChangeMapPlus_of_isIntegralHom`.
The latter uses the underived exchange, checked on geometric stalks by
henselian comparison [theorem-comparison-over-henselian-pair-degree].
The vertical pasting law [lemma-identity-pasting], together with
$R\pi_*(N[0])\simeq(\pi_*N)[0]$, identifies $b^q_{f,\pi_*N}$ with
$b^q_{f\pi,N}$, up to isomorphisms of source and target. This is
`AlgebraicGeometry.Etale.nonempty_arrowIso_baseChangeHomologyMap_lowerStar`.
Apply it to $N=\pi^{-1}M$. By hypothesis, $b^q_{f,\pi_*\pi^{-1}M}$ is
an isomorphism.

Surjectivity of $\pi$ makes inverse image faithful, hence the adjunction
unit $M\to\pi_*\pi^{-1}M$ injective
(`AlgebraicGeometry.Etale.mono_unit_app_of_surjective`).
Lemma [lemma-injectivity-base-change-map-degree], applied with the
degree-$(q-1)$ hypothesis over $T$, gives an injection

$$
\operatorname{coker}b^q_{f,M}\hookrightarrow
\operatorname{coker}b^q_{f,\pi_*\pi^{-1}M}=0.
$$

Thus $b^q_{f,M}$ is surjective. The same lemma makes it injective, so it
is an isomorphism.
