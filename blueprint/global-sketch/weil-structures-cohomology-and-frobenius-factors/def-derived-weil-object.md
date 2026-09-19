+++
id = "def-derived-weil-object"
kind = "definition"
title = "Derived Weil object"
order = 77
uses = ["def-derived-pullback", "def-qbar-coefficient-category", "def-weil-base-field", "def-weil-finite-coefficient-datum", "def-weil-frobenius", "def-weil-rational-coefficients", "prop-pullback-constructibility", "thm-qbar-two-colimit-model"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum]. Let $Y_0$ be of
finite type over $k_0$, with geometric fiber $Y$, and
let $\Lambda\in\{E,\Qlb\}$. A
*derived Weil object* is precisely an object
$K\in D^b_c(Y,\Lambda)$ together with a specified isomorphism in that
underlying derived category

$$
\theta_K:Lg_Y^*K\xrightarrow{\sim}K.
$$

For $\Lambda=\Qlb$, the finite diagram consisting of $K$, $\theta_K$,
and $\theta_K^{-1}$ is represented after one finite coefficient-field
extension. This definition introduces no new category of objects, no Hom
theory, and no triangulated structure: all objects, arrows, and triangles
remain in $D^b_c(Y,\Lambda)$.
