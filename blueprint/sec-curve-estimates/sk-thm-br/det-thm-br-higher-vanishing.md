+++
id = "det-thm-br-higher-vanishing"
kind = "lemma"
title = "Vanishing of higher cohomology of $\\mathbf G_m$ on a smooth curve"
lean = ["AlgebraicGeometry.IsCurve.subsingleton_sheafH_gmSheaf_of_smooth", "AlgebraicGeometry.IsCurve.subsingleton_sheafH_gmSheaf_of_isIntegral"]
order = 1414
uses = ["det-thm-br-field-units", "lem-sc-divisor-sequence-general", "lem-sc-point-z-cohomology", "lem-weil-pbc-cohomology-filtered-colimit", "lem-weil-pbc-zero-dimensional-cohomology", "thm-sp-grothendieck", "lem-sc-regular-dim1-dvr"]
+++
Let $k$ be algebraically closed and let $C$ be a smooth separated curve of
finite type over $k$. Then

$$
H^q(C_{\mathrm{ét}},\mathbf G_m)=0\qquad(q\geq2).
$$
