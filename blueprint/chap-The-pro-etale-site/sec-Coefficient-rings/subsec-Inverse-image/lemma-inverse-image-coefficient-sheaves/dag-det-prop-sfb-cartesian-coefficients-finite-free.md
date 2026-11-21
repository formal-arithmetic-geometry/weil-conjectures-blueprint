+++
id = "dag-det-prop-sfb-cartesian-coefficients-finite-free"
kind = "dag-lemma"
title = "$\\mathcal O_{F,X}$ is finite free over $\\mathcal O_{E,X}$"
name_showing = false
order = 187552
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--3"
dag_id = "det-prop-sfb-cartesian-coefficients-finite-free"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.finiteCoefficientIntegersMap", "AlgebraicGeometry.ProEtale.finiteCoefficientDegree", "AlgebraicGeometry.ProEtale.finiteCoefficientIntegralBasis", "AlgebraicGeometry.ProEtale.finiteCoefficientIntegersPointMap", "AlgebraicGeometry.ProEtale.isMonHom_finiteCoefficientIntegersPointMap", "AlgebraicGeometry.ProEtale.finiteCoefficientPointSummand", "AlgebraicGeometry.ProEtale.finiteCoefficientIntegralSummand", "AlgebraicGeometry.ProEtale.finiteCoefficientRationalSummand", "AlgebraicGeometry.ProEtale.finiteCoefficientIntegralLeg", "AlgebraicGeometry.ProEtale.finiteCoefficientRationalLeg", "AlgebraicGeometry.ProEtale.cartesianCoefficients_finiteFree"]
uses = ["dag-def-sfb-finite-upper-star", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $E\subset F$ be finite extensions of $\mathbf Q_\ell$ inside $\Qlb$, of degree $d=[F:E]$, and
let $X$ be a scheme. Then a choice of $\cO_E$-basis $b_1,\dots,b_d$ of $\cO_F$ induces
isomorphisms of $\cO_{E,X}$-modules, resp. $E_X$-modules,
$$
\cO_{E,X}^{\,d}\xrightarrow{\ \sim\ }\cO_{F,X},\qquad E_X^{\,d}\xrightarrow{\ \sim\ }F_X,
\qquad (a_i)\mapsto\textstyle\sum_ia_ib_i ,
$$
compatible with the maps $\cO_{E,X}\to E_X$ and $\cO_{F,X}\to F_X$ and with inverse image
along morphisms of schemes. In particular $\cO_{F,X}$ and $F_X$ are flat
(`lem-sfb-subfield-flat`).

(SHEAF DAG node `det-prop-sfb-cartesian-coefficients-finite-free`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--3]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-sfb-alpha`, `def-sfb-coefficient-map`, `def-sfb-finitely-presented-module`, `def-sfb-integers-to-subfield`, `def-sfb-integers-to-subfield-point`, `def-sfb-modobj-extension`, `def-sfb-padic-condensed-ring`, `def-sfb-padic-int-condensed-ring`, `def-sfb-padic-integers-condensed-ring`, `def-sfb-padic-subfield-condensed-ring`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-qlbar-subextension-map`, `def-sfb-subfield-coefficient-map`, `def-sfb-subfield-coefficient-ring`, `def-sfb-upper-star-from-point`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-sheaf-tensor-presheaf`, `lem-coef-grothendieck-locally-presentable`, `lem-sfb-modobj-forget-creates`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `sk-def-sfb-change-of-scalars`, `sk-def-sfb-coefficient-change`, `sk-def-sfb-coefficient-morphisms`, `sk-def-sfb-module-objects`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`, `sk-def-sfb-sheaf-tensor`.
