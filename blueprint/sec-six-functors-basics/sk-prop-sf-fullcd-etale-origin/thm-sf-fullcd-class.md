+++
id = "thm-sf-fullcd-class"
kind = "theorem"
title = "The blueprint's coefficient class supplies the restricted datum, with $c=2\\dim\\overline X$"
lean = ["AlgebraicGeometry.ProEtale.hasCohomologicalDimensionLEOnEtaleOrigin"]
order = 2763
uses = ["def-sf-fullcd-class", "def-sf-fullcd-used-class", "def-weil-full-cohomological-dimension", "def-weil-pbc-site-comparison-morphism", "def-weil-scheme-morphism-properties", "lem-sf-fullcd-class-restriction", "lem-sf-proetale-constructible-origin", "prop-sf-comparison-bound-zero", "thm-sf-fullcd-etale-origin", "thm-sf-fullcd-used-class", "thm-sp-grothendieck"]
+++
In the setting of [thm-sf-fullcd-used-class] — $k=\Fbar$,
finite-type $k$-schemes $Y$ and $\overline X$ with
$\dim\overline X\leq d$, and a
proper finite-type morphism
$p:\overline X\to Y$ — the class-restricted datum of
[def-sf-fullcd-class] holds for $p$ with the bound $2d$:

$$
\operatorname{FullCD}_{\mathrm{cls}}(p,A;2d).
$$

The bound is $2\dim\overline X\leq2d$ and it is uniform over all base
changes $V\to Y$ of $Y_{\Proet}$; the comparison bound on the class is
moreover the sharp $M=0$ of [prop-sf-comparison-bound-zero], so that
the residual $2\dim\overline X$ is the étale direction of the Leray
spectral sequence of [thm-sp-grothendieck] and not a lower bound on
$R^q\nu_{\overline X,*}$.
