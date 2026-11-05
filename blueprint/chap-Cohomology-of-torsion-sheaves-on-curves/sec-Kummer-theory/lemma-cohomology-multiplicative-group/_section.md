+++
id = "lemma-cohomology-multiplicative-group"
kind = "lemma"
title = "Cohomology of the multiplicative group"
order = 1571
lean = ["AlgebraicGeometry.IsCurve.subsingleton_cohomologicalBrauerGroup_of_smooth"]
uses = ["definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "lemma-cohomology-multiplicative-group--5"]
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
