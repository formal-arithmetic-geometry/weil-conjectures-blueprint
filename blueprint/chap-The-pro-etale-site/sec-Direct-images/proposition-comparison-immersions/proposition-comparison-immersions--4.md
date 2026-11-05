+++
id = "proposition-comparison-immersions--4"
kind = "proposition"
title = "Comparison for immersions (4)"
name_showing = false
order = 139004
aliases = ["bp-r040-4"]
lean = []
uses = ["definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "proposition-topos-functoriality", "proposition-extension-zero-restriction-closed-subscheme"]
+++
This compactification comparison is bypassed by the Lean proof of the
main theorem; it is retained here as an informal consequence of the
open-immersion and direct-image comparisons.

Let $f:X\to Y$ be a separated morphism of finite type with a
factorization $f=\bar f\circ j$, where $j$ is an open immersion and
$\bar f$ is proper. Then there is a canonical isomorphism
$\nu_Y^*R\bar f_{\acute{e}t,*}j_{\acute{e}t,!}\simeq R\bar f_{\mathrm{pro}\acute{e}t,*}j_{\mathrm{pro}\acute{e}t,!}\nu_X^*$
of functors $D^+(X_{\acute{e}t},\Lambda)\to D^+(Y_{\mathrm{pro}\acute{e}t},\Lambda)$.
