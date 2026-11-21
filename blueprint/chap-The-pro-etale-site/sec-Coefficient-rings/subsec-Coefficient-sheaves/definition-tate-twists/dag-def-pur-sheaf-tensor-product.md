+++
id = "dag-def-pur-sheaf-tensor-product"
kind = "dag-definition"
title = "Tensor product of sheaves of modules on a site"
name_showing = false
order = 184511
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "def-pur-sheaf-tensor-product"
dag_kind = "definition"
dag_status = "split"
serial = false
uses = ["dag-def-pur-presheaf-tensor-product"]
+++
Let $\mathcal C$ be a site, $\mathcal O$ a sheaf of commutative rings on
$\mathcal C$, and $\mathcal F,\mathcal G$ sheaves of $\mathcal O$-modules. The
*presheaf tensor product* is

$$
 (\mathcal F\otimes_{p,\mathcal O}\mathcal G)(U)
 =\mathcal F(U)\otimes_{\mathcal O(U)}\mathcal G(U)
 \qquad(U\in\mathcal C),
$$

with the restriction maps induced by those of $\mathcal F$, $\mathcal G$ and
$\mathcal O$, and the *tensor product* $\mathcal F\otimes_{\mathcal O}\mathcal G$
is the sheaf of $\mathcal O$-modules associated to it (its sheafification).
For a morphism of sheaves of rings $\mathcal O_1\to\mathcal O_2$ and a sheaf of
$\mathcal O_1$-modules $\mathcal F$, the sheaf of $\mathcal O_2$-modules
$\mathcal F\otimes_{\mathcal O_1}\mathcal O_2$ is the *change of rings* of
$\mathcal F$. For $m\in\mathbf Z_{\geq1}$ the $m$-fold *tensor power* is
$\mathcal F^{\otimes_{\mathcal O}1}=\mathcal F$ and
$\mathcal F^{\otimes_{\mathcal O}(m+1)}
=\mathcal F^{\otimes_{\mathcal O}m}\otimes_{\mathcal O}\mathcal F$.

(SHEAF DAG node `def-pur-sheaf-tensor-product`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: definition. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Lean names not on master: `SheafOfModules.presheafTensorProduct`, `SheafOfModules.sheafTensorProduct`. Statement dependencies not drawn: `def-weil-presheaf-modules-sheafification`.
