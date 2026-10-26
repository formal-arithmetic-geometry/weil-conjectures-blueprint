+++
id = "sk-prop-pe-left-complete"
kind = "proposition"
title = "Left completeness"
order = 949
lean = ["DerivedCategory.isHomotopyLimit_truncGECone"]
uses = ["sk-prop-pe-milnor"]
tags = ["sketch"]
+++
The standard $t$-structure on $D(X_{\mathrm{proét}},\mathcal R)$ is left complete: for every
complex $K$ the natural map

$$
K\longrightarrow R\varprojlim_{n\geq0}\tau_{\geq-n}K
$$

is an isomorphism.

K-injective resolutions of arbitrary complexes exist in the Grothendieck category of
$\mathcal R$-modules (Stacks, Tag 079P), so $R\Gamma(U,-)$ and $Rf_*$ are defined on the
unbounded derived categories: for $f\colon X\to Y$, $Rf_*$ goes from
$D(X_{\mathrm{proét}},\mathcal R)$ to the derived category of $f_*\mathcal R$-module sheaves
on $Y_{\mathrm{proét}}$. As derived right adjoints they preserve products, and hence the
derived inverse limits of [sk-prop-pe-milnor] (Stacks, Tag 0940). An unbounded calculation
can therefore be carried out on bounded-below truncations followed by a derived limit; the
passage to individual cohomology groups then involves the Milnor $R^1$ term.
