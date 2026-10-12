+++
id = "def-pur-sheaf-tensor-product"
kind = "definition"
title = "Tensor product of sheaves of modules on a site"
tags = ["sheaf-dag", "stacks-03EK"]
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
