+++
id = "sk-thm-sf-comp-composition"
kind = "proposition"
title = "Composition and base change for $Rf_!$"
order = 1814
uses = ["sec-nagata-compactification", "sec-proper-base-change", "sk-prop-nagata-sketch-comp-category", "sk-prop-sf-comp-coherence", "sk-thm-properbasechange", "sk-def-localizing-closure"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerShriek_comp"]
tags = ["sketch"]
+++
For every admissible $\Lambda$ the following statements hold on
$\Loc(\Dctf(-,\Lambda))$ and restrict to $\Dctf(-,\Lambda)$.

1. For separated morphisms of finite type $X\xrightarrow{f}Y\xrightarrow{g}Z$
there is a canonical isomorphism $Rg_!\circ Rf_!\simeq R(gf)_!$ of functors
$\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Z,\Lambda))$. These isomorphisms are
associative and compatible with the identity $R(\mathrm{id})_!=\mathrm{id}$.
2. Let $v:Y'\to Y$ be a morphism, $f':X'\to Y'$ the base change of $f$ along
$v$, and $u:X'\to X$ the projection. The base change map
$v^*Rf_!\to Rf'_!u^*$, a natural transformation of functors
$\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y',\Lambda))$, is an isomorphism.
