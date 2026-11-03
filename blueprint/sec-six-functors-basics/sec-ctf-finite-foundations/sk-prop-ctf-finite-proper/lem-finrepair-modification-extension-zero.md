+++
id = "lem-finrepair-modification-extension-zero"
kind = "lemma"
title = "Extension by zero under a proper modification"
lean = ["AlgebraicGeometry.Etale.nonempty_rightDerivedLowerStar_openImmersionLowerShriek_iso"]
order = 2355
uses = ["cor-weil-pbc-geometric-fiber-finite", "def-weil-pbc-extension-by-zero", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $\pi:Y\to X$ be proper and let $j:U\hookrightarrow X$ be open
such that $\pi^{-1}(U)\to U$ is an isomorphism, with morphisms as in
[def-weil-pbc-scheme-conventions].
Write $j':U'=\pi^{-1}(U)\hookrightarrow Y$.
For an etale $\Lambda$-sheaf $G$ on $U$, let $G'$ be its
pullback to $U'$. Then

$$
\pi_*j'_!G'\simeq j_!G,\qquad R^q\pi_*j'_!G'=0\quad(q>0),
$$

using the inverse image and extension by zero of
[def-weil-pbc-inverse-image], [def-weil-pbc-extension-by-zero].
