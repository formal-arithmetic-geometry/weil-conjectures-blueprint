+++
id = "def-nagata-affine-blowup-chart-map"
kind = "definition"
title = "Canonical affine blow-up chart morphism"
order = 33
lean = ["AlgebraicGeometry.AffineBlowup.chart"]
uses = ["def-nagata-affine-blowup", "def-nagata-homogeneous-away-to-chart", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-piece", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
+++
For an element $x$ of degree one in $\mathcal R_A(I)$ (for instance $x=at$
with $a\in I$), define

$$
\chi_x\colon \operatorname{Spec}\bigl(\mathcal R_A(I)_{(x),0}\bigr)\longrightarrow \operatorname{Bl}_I(\operatorname{Spec}A)
$$

to be the standard open immersion of the spectrum of the degree-zero
homogeneous localization onto the standard open $D_+(x)$.
