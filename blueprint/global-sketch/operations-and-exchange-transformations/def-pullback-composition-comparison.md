+++
id = "def-pullback-composition-comparison"
kind = "definition"
title = "Pullback composition comparison"
order = 38
uses = ["def-derived-pullback", "def-weil-finite-coefficient-datum"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum].
For composable morphisms $X\xrightarrow{f}Y\xrightarrow{h}Z$, define

$$
c^*_{f,h}:L(h\circ f)^*\xrightarrow{\sim}Lf^*Lh^*.
$$

At finite level this is the identity comparison for inverse image; at the
integral level it is induced termwise on finite reductions and then by
$R\varprojlim$; at the rational level it is derived-tensor associativity;
over $\Qlb$ it is represented at one common finite stage.
