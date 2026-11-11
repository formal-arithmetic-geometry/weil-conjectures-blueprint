+++
id = "proposition-open-direct-image-preserves-finite--1"
kind = "proposition"
title = "Open direct image preserves finite Tor amplitude (1)"
name_showing = false
order = 590001
aliases = ["bp-r179-1"]
lean = ["AlgebraicGeometry.ProEtale.boundedConstructible_rightDerivedLowerStar", "AlgebraicGeometry.ProEtale.projection_torAmplitudeIn_rightDerivedLowerStar_of_isOpenImmersion"]
uses = ["definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "proposition-comparison-morphism-inverse-image--1", "proposition-comparison-morphism-inverse-image--2", "definition-constructible-sheaves--5"]
+++
Let $j:U\hookrightarrow X$ be an open immersion. Then
$Rj_*:D(U_{\mathrm{pro}\acute{e}t},A)\to D(X_{\mathrm{pro}\acute{e}t},A)$ restricts to

$$
Rj_*:D^b_{\mathrm{ctf}}(U,A)\longrightarrow D^b_{\mathrm{ctf}}(X,A).
$$

More precisely, if $K$ has Tor amplitude in $[a,b]$ and $d\ge
\operatorname{cd}_\ell(j)$, then $Rj_*K$ has Tor amplitude in $[a,b+d]$.
