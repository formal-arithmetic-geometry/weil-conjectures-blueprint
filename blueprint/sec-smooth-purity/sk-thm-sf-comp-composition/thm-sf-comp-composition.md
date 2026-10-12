+++
id = "thm-sf-comp-composition"
kind = "theorem"
title = "The composition law for $Rf_!$"
order = 1858
uses = ["cor-weil-pbc-geometric-fiber-finite", "def-compact-support-direct-image-detailed", "def-weil-compactifications-refinements", "lem-weil-derived-direct-image-composition", "prop-compactification-coherence-detailed", "prop-compactification-refinement", "thm-nagata-compactification", "thm-weil-pbc-finite-level-proetale"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerShriek_comp"]
+++
Let $f:X\to Y$ and $g:Y\to S$ be separated of finite type between finite-type
$k$-schemes. There is a canonical isomorphism

$$
\alpha_{g,f}:\ Rg_!Rf_!\ \xrightarrow{\ \sim\ }\ R(g\circ f)_!
$$

of functors $D^+(X,\Lambda)\to D^+(S,\Lambda)$ on étale-origin complexes,
where $Rf_!$ is the compact-support direct image of
[def-compact-support-direct-image-detailed],
independent of all compactification choices by [prop-compactification-coherence-detailed],
equal to the identity when $f$ or $g$ is an identity, and associative:
for a third $h:S\to T$ the two composites
$Rh_!Rg_!Rf_!\to R(hgf)_!$ agree.
