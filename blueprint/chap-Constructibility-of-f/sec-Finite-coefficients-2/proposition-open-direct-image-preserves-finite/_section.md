+++
id = "proposition-open-direct-image-preserves-finite"
kind = "proposition"
title = "Open direct image preserves finite Tor amplitude"
order = 590
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedLowerStar", "AlgebraicGeometry.ProEtale.torAmplitudeIn_rightDerivedLowerStar", "AlgebraicGeometry.ProEtale.projection_torAmplitudeIn_rightDerivedLowerStar_of_isOpenImmersion"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image"]
+++
Let $j:U\hookrightarrow X$ be an open immersion. Then
$Rj_*:D(U_{\mathrm{pro}\acute{e}t},A)\to D(X_{\mathrm{pro}\acute{e}t},A)$ restricts to

$$
Rj_*:D^b_{\mathrm{ctf}}(U,A)\longrightarrow D^b_{\mathrm{ctf}}(X,A).
$$

More precisely, if $K$ has Tor amplitude in $[a,b]$ and $d\ge
\operatorname{cd}_\ell(j)$, then $Rj_*K$ has Tor amplitude in $[a,b+d]$.
