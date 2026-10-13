+++
id = "sk-thm-sf-comp-composition"
kind = "theorem"
title = "The composition law for $Rf_!$"
order = 1874
uses = ["sec-nagata-compactification", "sec-proper-base-change", "sk-prop-nagata-sketch-comp-category", "sk-prop-sf-comp-coherence", "sk-thm-properbasechange"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerShriek_comp"]
tags = ["sketch"]
+++
Let $f:X\to Y$ and $g:Y\to S$ be separated of finite type between finite-type
$k$-schemes. There is a canonical isomorphism

$$
\alpha_{g,f}:\ Rg_!Rf_!\ \xrightarrow{\ \sim\ }\ R(g\circ f)_!
$$

of functors $D^+(X,\Lambda)\to D^+(S,\Lambda)$ on étale-origin complexes,
independent of all compactification choices by [sk-prop-sf-comp-coherence],
equal to the identity when $f$ or $g$ is an identity, and associative:
for a third $h:S\to T$ the two composites
$Rh_!Rg_!Rf_!\to R(hgf)_!$ agree.
