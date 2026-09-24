+++
id = "def-nagata-composition-center-ideal"
kind = "definition"
title = "Center ideal representing a second blow-up"
order = 395
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_comp"]
uses = ["cor-nagata-blowup-product-common-refinement", "def-nagata-blowup-product-comparison", "def-nagata-blowup-product-domination-maps", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-map", "def-nagata-invertible-ideal", "def-nagata-proj-closed-center-finite-degree", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "lemma-nagata-blowup-invertible-factor", "lemma-nagata-blowup-universal-unique", "lemma-nagata-invertible-ideal-tensor-power", "lemma-nagata-localization-ideal-pow", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-product-ideal", "thm-nagata-blowup-universal-property"]
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
