+++
id = "def-nagata-composition-center-ideal"
kind = "definition"
title = "Center ideal representing a second blow-up"
order = 301
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_comp"]
uses = ["def-nagata-proj-closed-center-finite-degree"]
+++
Let $X$ be qcqs, let $\mathcal I\subseteq\mathcal O_X$ be a finite-type
quasi-coherent ideal, put
$X'=\operatorname{Bl}_{\mathcal I}(X)$ with structure map
$b\colon X'\to X$, and let $Z'\hookrightarrow X'$ be a
finite-presentation closed immersion. Write
$Z=V(\mathcal I)\hookrightarrow X$. With
$\mathsf{FD}(Z')=(d,\mathcal F)$, define

$$
\mathcal J(Z')=\mathcal F\subseteq\mathcal I^d\subseteq\mathcal O_X,
\qquad
\mathcal K(Z')=\mathcal I\mathcal J(Z'),
\qquad
Y(Z')=V(\mathcal K(Z')).
$$
