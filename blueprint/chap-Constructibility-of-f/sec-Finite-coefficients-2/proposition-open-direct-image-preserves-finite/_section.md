+++
id = "proposition-open-direct-image-preserves-finite"
kind = "proposition"
title = "Open direct image preserves finite Tor amplitude"
order = 590
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedLowerStar", "AlgebraicGeometry.ProEtale.torAmplitudeIn_rightDerivedLowerStar", "AlgebraicGeometry.ProEtale.projection_torAmplitudeIn_rightDerivedLowerStar_of_isOpenImmersion"]
uses = ["definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves"]
+++
Let $j:U\hookrightarrow X$ be an open immersion. Then
$Rj_*:D(\href{@definition-small-pro-etale-site}{U_{\mathrm{pro}\acute{e}t}},A)\to D(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},A)$ restricts to

$$
Rj_*:\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(U,A)}\longrightarrow \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,A)}.
$$

More precisely, if $K$ has [Tor amplitude](@definition-constructible-sheaves) in $[a,b]$ and $d\ge
\href{@definition-cohomological-dimension}{\operatorname{cd}_\ell(j)}$, then $Rj_*K$ has [Tor amplitude](@definition-constructible-sheaves) in $[a,b+d]$.
