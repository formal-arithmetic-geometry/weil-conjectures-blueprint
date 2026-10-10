+++
id = "sk-prop-av-isogeny"
kind = "proposition"
title = "The multiplication-by-$n$ isogeny"
lean = ["AlgebraicGeometry.isIsogeny_npow_id"]
order = 559
uses = ["sk-def-av", "sk-def-av-ample-degree", "sk-def-av-isogeny", "sk-def-av-mult-n", "sk-prop-av-deg-pullback", "sk-prop-av-isogeny-degree", "sk-prop-av-mult-finite", "sk-prop-av-mult-hom", "sk-prop-av-mult-n-pullback", "sk-prop-av-mult-surjective", "sk-prop-av-projective", "sk-prop-av-symmetric-ample"]
tags = ["sketch"]
+++
Let $A$ be an abelian variety of dimension $g$ over a field $k$ and let
$n\ge1$. Then $[n]:A\to A$ of [sk-def-av-mult-n] is a finite flat
surjective homomorphism, hence an isogeny, of degree $n^{2g}$, and its
kernel $A[n]$ is a finite flat group scheme over $k$ of order $n^{2g}$.
