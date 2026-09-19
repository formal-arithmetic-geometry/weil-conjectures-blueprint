+++
id = "def-nagata-final-basechanged-compactification"
kind = "definition"
title = "Base-changed compactification of the finite-presentation envelope"
order = 565
uses = ["def-nagata-compactification-base-change", "def-nagata-final-descended-model", "def-nagata-final-noetherian-compactification", "lemma-nagata-final-descended-model", "lemma-nagata-final-noetherian-compactification"]
+++
**Status.** Bypassed by the formalized route: the final assembly is carried
out inside `AlgebraicGeometry.NagataCompactification` and
`AlgebraicGeometry.nagataCompactification_of_locallyOfFinitePresentation`,
which produce the factorization and its three properties directly, without
separately named intermediate objects.

Let $\overline X_{f,\lambda_f}$ be the ambient term of
$C_{f,\lambda_f}$ and let
$j_{f,\lambda_f}\colon X_{f,\lambda_f}^{\mathrm{fp}} \hookrightarrow\overline X_{f,\lambda_f}$ be its open immersion. Base
change this factorization along $S\to S_{\lambda_f}$ and set
$\epsilon_f^{-1}\colon X_f^{\mathrm{fp}}\xrightarrow{\sim} X_{f,\lambda_f}^{\mathrm{fp}}\times_{S_{\lambda_f}}S$. Define the source
map of the resulting factorization to be
$j_{f,\lambda_f,S}\circ\epsilon_f^{-1}$, and define the resulting
factorization to be

$$
C_f^{\mathrm{fp}}
=\bigl(X_f^{\mathrm{fp}}\hookrightarrow
\overline X_f^{\mathrm{fp}}\longrightarrow S\bigr).
$$
