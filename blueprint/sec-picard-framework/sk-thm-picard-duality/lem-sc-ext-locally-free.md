+++
id = "lem-sc-ext-locally-free"
kind = "lemma"
title = "Ext of a finite locally free module"
order = 695
uses = ["def-sc-ext-sheaf"]
+++
Let $X$ be a scheme, $\mathcal F$ a finite locally free
$\mathcal O_X$-module and $\mathcal G$ an $\mathcal O_X$-module,
with $\operatorname{Ext}$ as in [def-sc-ext-sheaf] and
$\mathcal F^{\vee}=\mathcal{H}om_{\mathcal O_X}(\mathcal F,\mathcal O_X)$. Then there are canonical isomorphisms

$$
\operatorname{Ext}^i_X(\mathcal F,\mathcal G)\;\cong\;
\mathrm H^i\bigl(X,\mathcal F^{\vee}\otimes_{\mathcal O_X}
\mathcal G\bigr)\qquad(i\geq0),
$$

in particular
$\operatorname{Ext}^i_X(\mathcal O_X,\mathcal G)=\mathrm H^i(X,\mathcal G)$.
