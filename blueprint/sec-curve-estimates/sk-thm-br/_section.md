+++
id = "sk-thm-br"
kind = "lemma"
title = "Cohomology of the multiplicative group"
order = 882
uses = ["sk-def-av-pic", "sk-def-br", "sk-def-curve", "sk-prop-br-inj", "sk-prop-tsen", "sk-prop-hilbert90", "sk-prop-divisor-gen", "sk-def-cr", "sk-prop-sf-comparison"]
lean = ["AlgebraicGeometry.IsCurve.subsingleton_cohomologicalBrauerGroup"]
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
algebraically closed ground field. In particular $\Br(C)=0$ ([sk-def-br]).
