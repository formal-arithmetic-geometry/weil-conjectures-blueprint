+++
id = "def-nagata-elimination-indeterminacy"
kind = "definition"
title = "Elimination-of-indeterminacy construction"
order = 377
lean = ["AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap"]
uses = ["def-nagata-admissible-blowup", "def-nagata-flattening-ideal", "def-nagata-strict-transform"]
+++
Let $q\colon Z\to X$ be separated and of finite type, let $X$ be qcqs, and
let $U\subseteq X$ be quasi-compact. Fix an isomorphism
$e_U\colon q^{-1}(U)\xrightarrow{\sim}U$ over $U$.
Let $\mathcal F_U(q)$ be the selected flattening ideal of
[def-nagata-flattening-ideal]. Define

$$
X^{\mathrm{el}}(q,U)=\operatorname{Bl}_{\mathcal F_U(q)}(X),
\qquad
Z^{\mathrm{el}}(q,U)=
\operatorname{ST}_{X^{\mathrm{el}}/X}(Z),
$$

together with the strict-transform projection
$q^{\mathrm{el}}\colon Z^{\mathrm{el}}(q,U)\to X^{\mathrm{el}}(q,U)$ and
the transported open identification induced by $e_U$.
Thus $\mathcal F_U(q)$ is a labelled selected object rather than an
unspecified existential variable.
