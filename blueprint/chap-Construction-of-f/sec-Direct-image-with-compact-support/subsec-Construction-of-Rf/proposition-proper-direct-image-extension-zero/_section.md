+++
id = "proposition-proper-direct-image-extension-zero"
kind = "proposition"
title = "Proper direct image and extension by zero"
order = 502
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.localizingBoundedConstructible_lowerStar_lowerShriek_continuousMapRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.localizingBoundedConstructible_lowerStar_lowerShriek_padicAlgClRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.localizingBoundedConstructible_rightDerivedLowerStar_padicIntegersRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.localizingClosure_boundedConstructible_openImmersionLowerShriek", "AlgebraicGeometry.ProEtale.localizingClosure_constructibleFiniteTor_openImmersionLowerShriek"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-comparison-morphism-inverse-image", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "lemma-constructible-sheaves", "definition-localizing-subcategory"]
+++
For every admissible $\Lambda$, if $p:X\to Y$ is proper,
$Rp_*:D(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\Lambda)\to D(\href{@definition-small-pro-etale-site}{Y_{\mathrm{pro}\acute{e}t}},\Lambda)$ restricts to an exact functor
$\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,\Lambda)})\to\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Y,\Lambda)})$ that preserves direct
sums. If $j:U\to X$ is an open immersion,
$j_!:D(\href{@definition-small-pro-etale-site}{U_{\mathrm{pro}\acute{e}t}},\Lambda)\to D(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\Lambda)$ restricts to an exact
functor $\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(U,\Lambda)})\to\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,\Lambda)})$ that preserves
direct sums and maps [$D^b_{\mathrm{ctf}}(U,\Lambda)$](@definition-constructible-sheaves) into [$D^b_{\mathrm{ctf}}(X,\Lambda)$](@definition-constructible-sheaves).
