+++
id = "def-sfb-qlbar-x-cocone"
kind = "definition"
title = "The cocone $E_X\\to\\overline{\\mathbf Q}_{\\ell,X}$"
order = 1198
uses = ["def-sfb-qlbar-coefficient-ring", "def-sfb-subfield-coefficient-ring", "det-def-sfb-pullback-from-point", "det-prop-sfb-qlbar-colimit-point"]
lean = ["AlgebraicGeometry.ProEtale.padicAlgClRingObjCocone"]
+++
Let $\ell$ be a prime and $X$ a scheme. Consider the diagram $E\mapsto E_X$
([def-sfb-subfield-coefficient-ring]), indexed by the poset of finite
subextensions $E\subseteq\Qlb$ of $\mathbb Q_\ell$. Its transition maps
$E_X\to F_X$ are $p_X^*$ of the inclusions $\underline E\to\underline F$.

The cocone over this diagram has vertex $\overline{\mathbf Q}_{\ell,X}$
([def-sfb-qlbar-coefficient-ring]) and legs $E_X\to\overline{\mathbf Q}_{\ell,X}$.
It is defined as the image under the functor $p_X^*$
([det-def-sfb-pullback-from-point]) of the cocone of inclusions
$\underline E\to\underline{\Qlb}$ of [det-prop-sfb-qlbar-colimit-point].
