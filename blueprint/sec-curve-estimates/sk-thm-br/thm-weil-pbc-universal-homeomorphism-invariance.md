+++
id = "thm-weil-pbc-universal-homeomorphism-invariance"
kind = "theorem"
title = "Universal-homeomorphism invariance"
lean = ["AlgebraicGeometry.Etale.universalHomeomorphism_invariance"]
order = 1367
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-inverse-image", "def-sp-kinjective-bridge", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-universal-homeomorphism-base-change", "prop-weil-pbc-kinjective-resolutions-exist"]
+++
If $u:X'\to X$ is a universal homeomorphism
[def-weil-pbc-scheme-conventions], then the morphisms of small etale sites
[def-weil-pbc-etale-site] induced by $u$ give an equivalence of small etale
topoi, i.e. an equivalence of the categories of etale sheaves

$$
 \operatorname{Sh}(X_{\Et})\xrightarrow{\ \sim\ }\operatorname{Sh}(X'_{\Et}),
$$

compatible with the inverse and direct image functors and with cohomology.
The equivalence preserves and reflects covering families and is compatible
with identities, composition, and pullback of sheaves and cohomology.
