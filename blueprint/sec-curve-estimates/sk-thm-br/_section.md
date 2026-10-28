+++
id = "sk-thm-br"
kind = "lemma"
title = "Cohomology of the multiplicative group"
order = 1423
uses = ["sk-lem-abelian-seesaw", "sk-prop-av-isogeny", "sk-def-picard-pic", "sk-prop-sf-comparison"]
lean = ["AlgebraicGeometry.IsCurve.sheafH_gmSheaf_of_smooth", "AlgebraicGeometry.IsCurve.rightDerived_globalSections_comparisonUpperStar_gmSheaf", "AlgebraicGeometry.IsCurve.subsingleton_cohomologicalBrauerGroup_of_smooth"]
tags = ["sketch"]
+++
On a smooth connected curve $C$ over an algebraically closed field let
$\mathcal G_m^{\mathrm{cl}}=\nu_C^*\mathbf G_{m,C_{\mathrm{ét}}}$ be the
classical multiplicative sheaf on $C_{\mathrm{proét}}$.

For a smooth separated curve $C$ of finite type over an algebraically closed
field, one has

$$
H^1(C,\mathcal G_m^{\mathrm{cl}})=\operatorname{Pic}(C),
\qquad
H^q(C,\mathcal G_m^{\mathrm{cl}})=0\quad(q\geq2).
$$

The identifications are natural under restriction and extension of the
algebraically closed ground field. In particular $\Br(C)=0$ ([def-br]).
