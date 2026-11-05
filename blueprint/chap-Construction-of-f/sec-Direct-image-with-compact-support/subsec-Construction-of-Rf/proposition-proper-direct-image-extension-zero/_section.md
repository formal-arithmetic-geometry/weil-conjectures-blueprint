+++
id = "proposition-proper-direct-image-extension-zero"
kind = "proposition"
title = "Proper direct image and extension by zero"
order = 502
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.localizingBoundedConstructible_lowerStar_lowerShriek_continuousMapRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.localizingBoundedConstructible_lowerStar_lowerShriek_padicAlgClRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.localizingBoundedConstructible_rightDerivedLowerStar_padicIntegersRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.localizingClosure_boundedConstructible_openImmersionLowerShriek", "AlgebraicGeometry.ProEtale.localizingClosure_constructibleFiniteTor_openImmersionLowerShriek"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-localizing-subcategory"]
+++
For every admissible $\Lambda$, if $p:X\to Y$ is proper,
$Rp_*:D(X_{\mathrm{pro}\acute{e}t},\Lambda)\to D(Y_{\mathrm{pro}\acute{e}t},\Lambda)$ restricts to an exact functor
$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))\to\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$ that preserves direct
sums. If $j:U\to X$ is an open immersion,
$j_!:D(U_{\mathrm{pro}\acute{e}t},\Lambda)\to D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ restricts to an exact
functor $\Loc(D^b_{\mathrm{ctf}}(U,\Lambda))\to\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ that preserves
direct sums and maps $D^b_{\mathrm{ctf}}(U,\Lambda)$ into $D^b_{\mathrm{ctf}}(X,\Lambda)$.
