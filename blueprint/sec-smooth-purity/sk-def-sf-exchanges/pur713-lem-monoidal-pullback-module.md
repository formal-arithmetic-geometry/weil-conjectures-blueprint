+++
id = "pur713-lem-monoidal-pullback-module"
kind = "lemma"
title = "Monoidal comparison for module-object derived inverse image"
order = 1875
tags = ["latex:bplemma"]
uses = ["pur713-def-tensor-module", "pur713-lem-pull-composition-module"]
+++
Under the inputs of Lemma [pur713-lem-pull-composition-module], for $f:X\to Y$ and $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$, the functor $Lf^*_T:D(Y_{\Proet},T)\to D(X_{\Proet},T)$ carries a strong symmetric monoidal structure for the derived tensor products of Definition [pur713-def-tensor-module]: there are natural isomorphisms

$$
Lf^*_T(M\otimes^L_{\mathcal R_{Y,T}}N)
\xrightarrow{\sim}Lf^*_TM\otimes^L_{\mathcal R_{X,T}}Lf^*_TN,
\qquad
Lf^*_T\mathcal R_{Y,T}\cong\mathcal R_{X,T},
$$

satisfying the associativity, symmetry and unit coherence equations.
