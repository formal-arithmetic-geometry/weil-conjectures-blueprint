+++
id = "lemma-kunneth-map-slice"
kind = "lemma"
title = "The Künneth map on a slice"
order = 1659
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_map_kunnethMap_of_isIso_sliceFst_residueField", "AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.isIso_map_kunnethMap_of_isIso_sliceFst_padicIntegers", "AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.exists_subgroup_pullbackExchange_baseChangeHom_traitSlice"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "lemma-extremally-disconnected-covers", "proposition-comparison-morphism-inverse-image", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves"]
+++
In the situation just described, let $L\in D^b_{\mathrm{ctf}}(X_\eta,A)$
and $M\in D^b_{\mathrm{ctf}}(Y_\eta,A)$. Identify the restrictions over
$s'$ of the nearby cycles of $L$, $M$ and $L\boxtimes M$ by

$$
\begin{aligned}
R\Psi_{X/S}L|_{s'}&\simeq(R\Psi_{X'/S'}L')^P,\\
R\Psi_{Y/S}M|_{s'}&\simeq R\Psi_{Y'/S'}M',\\
R\Psi_{(X\times Y)/S}(L\boxtimes M)|_{s'}
&\simeq
(R\Psi_{(X'\times Y')/S'}(L'\boxtimes M'))^P,
\end{aligned}
$$

given by (E.2) for $b$, by invariance of
nearby cycles under change of trait, and by
(E.2) for $b\circ\operatorname{pr}_1$. Then
the restriction of $\Pi_{L,M}$ over $s'$ is $(\Pi_{L',M'})^P$. In
particular, if $\Pi_{L',M'}$ is an isomorphism, then so is the
restriction of $\Pi_{L,M}$ over $s'$.
