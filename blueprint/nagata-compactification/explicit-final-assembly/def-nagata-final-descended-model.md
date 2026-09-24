+++
id = "def-nagata-final-descended-model"
kind = "definition"
title = "Separated descended model used in the final assembly"
order = 597
uses = ["def-nagata-final-fp-envelope", "def-nagata-final-noetherian-base-system", "def-nagata-separated-descent-stage", "lemma-nagata-final-fp-envelope", "lemma-nagata-final-noetherian-base-system"]
+++
**Status.** Bypassed by the formalized route: the final assembly is carried
out inside `AlgebraicGeometry.NagataCompactification` and
`AlgebraicGeometry.nagataCompactification_of_locallyOfFinitePresentation`,
which produce the factorization and its three properties directly, without
separately named intermediate objects.

Apply the separated-descent construction to
$X_f^{\mathrm{fp}}\to S$ relative to $\mathsf N_f$. Define

$$
\lambda_f=\lambda_{\mathrm{sep}}(X_f^{\mathrm{fp}}/S),
\qquad
X_{f,\lambda_f}^{\mathrm{fp}}
=(X_f^{\mathrm{fp}})^{\mathrm{sep}}_{\lambda_f},
$$

and let

$$
\epsilon_f\colon
X_{f,\lambda_f}^{\mathrm{fp}}
\times_{S_{\lambda_f}}S
\longrightarrow X_f^{\mathrm{fp}}
$$

be the constructed base-change comparison.
