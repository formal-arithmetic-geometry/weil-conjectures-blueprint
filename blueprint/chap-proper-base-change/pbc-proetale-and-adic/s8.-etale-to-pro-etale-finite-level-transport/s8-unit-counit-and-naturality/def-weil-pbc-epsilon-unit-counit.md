+++
id = "def-weil-pbc-epsilon-unit-counit"
kind = "definition"
title = "Unit and counit of the comparison"
order = 1780
uses = ["def-weil-pbc-epsilon-comparison"]
+++
Write the unit and counit of the preceding adjunction as

$$
\eta^X:\operatorname{id}_{\operatorname{Sh}_A(X_{\mathrm{et}})}
\longrightarrow\epsilon_{X,*}\epsilon_X^{-1},
\qquad
\varepsilon^X:\epsilon_X^{-1}\epsilon_{X,*}
\longrightarrow\operatorname{id}_{\operatorname{Sh}_A(X_{\mathrm{proet}})}.
$$

For $F\in\operatorname{Sh}_A(X_{\mathrm{et}})$, the component
$\eta^X_{F,U}$ sends $s\in F(U)$ to the class represented by
$(1_{\iota_XU}:\iota_XU\to\iota_XU,s)$. For
$G\in\operatorname{Sh}_A(X_{\mathrm{proet}})$, the component
$\varepsilon^X_{G,W}$ sends a representative
$(W\xrightarrow{a}\iota_XU,s)$ to the restriction $G(a)(s)\in G(W)$.
This map on the Kan-extension presheaf factors uniquely through pro-etale
sheafification.
