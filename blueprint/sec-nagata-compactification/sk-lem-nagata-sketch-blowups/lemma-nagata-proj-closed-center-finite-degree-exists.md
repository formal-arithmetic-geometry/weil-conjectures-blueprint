+++
id = "lemma-nagata-proj-closed-center-finite-degree-exists"
kind = "lemma"
title = "Existence of finite-degree equations for a closed center in Proj"
order = 248
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteDegree_center_le_blowup"]
uses = ["def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-relative-proj", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-relative-proj-exists", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open", "thm-nagata-global-blowup-complement", "thm-nagata-global-blowup-proper"]
+++
Let $\mathcal I$ be a finite type quasi-coherent ideal on a qcqs scheme
$X$, let $b\colon X'=\operatorname{Bl}_{\mathcal I}(X)\to X$ be its blow-up
with exceptional ideal $\mathcal I_E=\mathcal I\mathcal O_{X'}$, and let
$\mathcal I_{Z'}\subseteq\mathcal O_{X'}$ be a finite type quasi-coherent
ideal, defining a finite-presentation closed immersion
$Z'\hookrightarrow X'$. Then there exist $d>0$ and a finite type
quasi-coherent ideal $\mathcal F\subseteq\mathcal I^d$ on $X$ such that

$$
\mathcal F\mathcal O_{X'}=\mathcal I_E^d\,\mathcal I_{Z'}.
$$
