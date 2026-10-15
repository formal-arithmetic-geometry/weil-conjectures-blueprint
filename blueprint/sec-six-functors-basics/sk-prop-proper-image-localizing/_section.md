+++
id = "sk-prop-proper-image-localizing"
kind = "proposition"
title = "Proper direct image and extension by zero"
order = 1578
uses = ["sk-def-localizing-closure", "sk-lem-proper-unbounded-window-ii", "sk-thm-sfb-proper-base-change", "sk-prop-ctf-finite-proper", "sk-prop-int-compactness"]
tags = ["sketch"]
+++
For every admissible $\Lambda$, if $p\colon X\to Y$ is proper,
$Rp_*\colon\D(X_{\mathrm{proét}},\Lambda)\to\D(Y_{\mathrm{proét}},\Lambda)$ restricts to an exact functor
$\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y,\Lambda))$ that preserves direct sums. If $j\colon U\to X$ is an open
immersion, $j_!\colon\D(U_{\mathrm{proét}},\Lambda)\to\D(X_{\mathrm{proét}},\Lambda)$ restricts to an exact functor
$\Loc(\Dctf(U,\Lambda))\to\Loc(\Dctf(X,\Lambda))$ that preserves direct sums and maps $\Dctf(U,\Lambda)$ into
$\Dctf(X,\Lambda)$.

Both statements rest on the following form of the definition of $\Loc(\Dctf(X,\Lambda))$
([sk-def-localizing-closure]): if the objects of $\Loc(\Dctf(X,\Lambda))$ with some property form a
triangulated subcategory that is closed under direct sums and contains $\Dctf(X,\Lambda)$, then every object
of $\Loc(\Dctf(X,\Lambda))$ has the property.
