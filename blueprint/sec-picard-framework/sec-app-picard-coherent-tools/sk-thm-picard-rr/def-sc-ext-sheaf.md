+++
id = "def-sc-ext-sheaf"
kind = "definition"
title = "Ext groups of $\\mathcal O_X$-modules"
lean = ["AlgebraicGeometry.Scheme.Modules.Ext"]
order = 680
+++
Let $X$ be a scheme and $\mathcal F,\mathcal G$ be
$\mathcal O_X$-modules. The *Ext groups* are the morphism groups
in the derived category $D(\mathcal O_X)$ of the abelian category
of $\mathcal O_X$-modules:

$$
\operatorname{Ext}^i_X(\mathcal F,\mathcal G)
:=\operatorname{Hom}_{D(\mathcal O_X)}(\mathcal F,\mathcal G[i])
\qquad(i\geq0).
$$

Since the category of $\mathcal O_X$-modules has enough injectives,
these are the right derived functors of the covariant functor
$\operatorname{Hom}_{\mathcal O_X}(\mathcal F,-)$ evaluated at
$\mathcal G$, i.e.
$\operatorname{Ext}^i_X(\mathcal F,\mathcal G)
=H^i\bigl(\operatorname{Hom}_{\mathcal O_X}(\mathcal F,\mathcal I^\bullet)\bigr)$
for any injective resolution $\mathcal G\to\mathcal I^\bullet$; they
are functorial (contravariantly) in $\mathcal F$ as well. In particular
$\operatorname{Ext}^0_X(\mathcal F,\mathcal G) =\operatorname{Hom}_{\mathcal O_X}(\mathcal F,\mathcal G)$.
