+++
id = "lem-weil-pbc-clopen-section-direct-image"
kind = "lemma"
title = "Direct image from an open and closed section"
order = 2258
lean = ["AlgebraicGeometry.Etale.clopenSectionDirectImageIso", "AlgebraicGeometry.Etale.isIso_openImmersionLowerShriekToLowerStarPlus_app_of_isClosed_range"]
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-extension-by-zero", "def-weil-pbc-scheme-conventions", "prop-weil-pbc-kinjective-resolutions-exist"]
+++
Let $p:V\to X$ be a scheme morphism and
$s:X\hookrightarrow V$ an
open immersion with
closed image and $p s=\operatorname{id}_X$.
For a commutative ring $\Lambda$ and
$K\in\hyperref[def-weil-pbc-derived-categories]{D^+(X_{\Et},\Lambda)}$,
restriction to this component gives a canonical isomorphism

$$
Rp_*s_!K\xrightarrow{\sim}K,
$$

where $Rp_*$ and $s_!$ are the
derived direct image and
extension by zero.
