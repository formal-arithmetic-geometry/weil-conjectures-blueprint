+++
id = "sk-thm-br"
kind = "lemma"
title = "Cohomology of the multiplicative group"
order = 912
lean = ["AlgebraicGeometry.IsCurve.sheafH_gmSheaf_of_smooth", "AlgebraicGeometry.IsCurve.rightDerived_globalSections_comparisonUpperStar_gmSheaf", "AlgebraicGeometry.IsCurve.subsingleton_cohomologicalBrauerGroup_of_smooth"]
uses = ["sk-lem-abelian-seesaw", "sk-prop-av-isogeny", "sk-def-picard-pic", "sk-prop-sf-comparison"]
tags = ["sketch"]
+++
For a smooth separated curve $C$ of finite type over an algebraically
closed field, one has

$$
H^1(C,\nu_C^*\mathbf G_m)=\operatorname{Pic}(C),
\qquad
H^q(C,\nu_C^*\mathbf G_m)=0\quad(q\geq2).
$$

The identifications are natural under restriction and extension of
the algebraically closed ground field. In particular
$\operatorname{Br}(C)=H^2(C_{\acute{e}t},\mathbf G_m)=0$.
