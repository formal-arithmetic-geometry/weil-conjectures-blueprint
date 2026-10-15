+++
id = "pur713-def-rationalization"
kind = "definition"
title = "Rationalization functor"
order = 1819
uses = ["pur713-def-continuous-rings", "pur713-def-extension", "pur713-def-kflat-module", "sk-def-sf-setting"]
+++
For a scheme $X$, let $\phi_X:\mathcal R_{X,\mathcal O_E}\to\mathcal R_{X,E}$ be $p_X^*$ (Input “Pullback from the point” (`pur713-input-point-pullback`, in [sk-def-sf-setting])) of the morphism of condensed rings $\underline{\mathcal O}_E\to\underline E$ induced by the inclusion $\mathcal O_E\subseteq E$ (Definition [pur713-def-continuous-rings]); it is a morphism of commutative ring objects. Define

$$
E\otimes^L_{\mathcal O_E}-:=L(\operatorname{Ext}_{\phi_X}):D(X_{\Proet},\mathcal O_E)\longrightarrow D(X_{\Proet},E),
$$

the total left derived functor of the extension of scalars of Definition [pur713-def-extension], computed on K-flat resolutions (Definition [pur713-def-kflat-module]). Source: governing reference, §§4.2 and 5.1.
