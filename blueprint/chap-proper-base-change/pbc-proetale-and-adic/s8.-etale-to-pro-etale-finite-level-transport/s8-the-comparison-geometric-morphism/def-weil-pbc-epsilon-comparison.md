+++
id = "def-weil-pbc-epsilon-comparison"
kind = "definition"
title = "Etale/pro-etale comparison morphism"
order = 1770
+++
The continuous left-exact functor $\iota_X$ induces the geometric morphism

$$
\epsilon_X:X_{\mathrm{proet}}\longrightarrow X_{\mathrm{et}}.
$$

For every commutative coefficient ring $A$, its inverse- and direct-image
functors have the typed source and target

$$
\epsilon_X^{-1}:\operatorname{Sh}_A(X_{\mathrm{et}})
\longrightarrow\operatorname{Sh}_A(X_{\mathrm{proet}}),
\qquad
\epsilon_{X,*}:\operatorname{Sh}_A(X_{\mathrm{proet}})
\longrightarrow\operatorname{Sh}_A(X_{\mathrm{et}}).
$$

For $G\in\operatorname{Sh}_A(X_{\mathrm{proet}})$ one has
$(\epsilon_{X,*}G)(U)=G(\iota_XU)$. For
$F\in\operatorname{Sh}_A(X_{\mathrm{et}})$, the inverse image is the
pro-etale sheafification of the left Kan extension along $\iota_X^{\mathrm{op}}$;
before sheafification its value at $W\to X$ is

$$
\underset{(W\to\iota_XU)}{\operatorname{colim}}F(U).
$$
