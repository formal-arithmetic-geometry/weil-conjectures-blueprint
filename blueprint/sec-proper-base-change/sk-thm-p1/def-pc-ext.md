+++
id = "def-pc-ext"
kind = "definition"
title = "Extensions"
order = 1211
lean = ["CategoryTheory.Abelian.Ext", "CategoryTheory.ProjectiveResolution.isoExt", "isZero_Ext_succ_of_projective"]
+++
Let $\mathcal A$ be an abelian category (for a scheme $X$: the category
of $\mathcal{O}_X$-modules, or any abelian subcategory of it closed under the
operations below) and let $F,G$ be objects of $\mathcal A$ and
$i\ge0$. The *$i$-th Ext group* is

$$
\operatorname{Ext}^{i}_{\mathcal A}(F,G)
\;:=\;\Hom_{D(\mathcal A)}\bigl(F,\;G[i]\bigr),
$$

the group of morphisms from $F$ to the $i$-fold shift of $G$ in the
derived category ([def-pc-derived-category]); equivalently, it is the
$i$-th cohomology of $\mathbf R\Hom(F,G)$, computed classically by an
injective resolution of $G$ when $\mathcal A$ has enough injectives. When $\mathcal A$ has
enough projectives, $\operatorname{Ext}^i_{\mathcal A}(F,G)$ is computed by a
projective resolution $P_\bullet\to F$: it is the $i$-th cohomology of the
complex $\Hom_{\mathcal A}(P_\bullet,G)$. In particular, if $F$ is
projective then $\operatorname{Ext}^{i}_{\mathcal A}(F,G)=0$ for all $i\ge1$.
For sheaves on a
scheme $X$ one writes $\operatorname{Ext}^{i}_{\mathcal{O}_X}(-,-)$ (or
$\operatorname{Ext}^{i}_X(-,-)$) for the case
$\mathcal A$ the category of $\mathcal{O}_X$-modules, and

$$
\mathcal{E}xt^{i}_{\mathcal{O}_X}(F,G):=H^i\mathcal{H}om^{\bullet}_{\mathcal{O}_X}(F,G)
$$

denotes the associated sheaf ($\mathcal{H}om^{\bullet}$ the derived
inner hom of sheaves).
