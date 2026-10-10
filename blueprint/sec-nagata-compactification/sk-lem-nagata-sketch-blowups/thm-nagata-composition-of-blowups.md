+++
id = "thm-nagata-composition-of-blowups"
kind = "theorem"
title = "[stacks-project]"
order = 135
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_comp"]
uses = ["cor-nagata-blowup-cartier-iso", "cor-nagata-blowup-product-common-refinement", "def-nagata-blowup-product-comparison", "def-nagata-blowup-product-domination-maps", "def-nagata-composition-of-blowups-comparison", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-invertible-ideal", "def-nagata-proj-closed-center-finite-degree", "lemma-nagata-blowup-invertible-factor", "lemma-nagata-composition-center-ideal", "lemma-nagata-composition-extended-ideal-equality", "lemma-nagata-invertible-ideal-tensor-power", "lemma-nagata-product-ideal-common-blowup", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-product-ideal", "thm-nagata-blowup-universal-property"]
+++
Let $X$ be qcqs, let $\mathcal I\subseteq\mathcal O_X$ be a finite-type
quasi-coherent ideal with blow-up $b\colon X'=\operatorname{Bl}_{\mathcal I}(X)\to X$,
and let $Z'\hookrightarrow X'$ be the closed subscheme defined by a
finite-type quasi-coherent ideal $\mathcal I_{Z'}$; put $Z=V(\mathcal I)$.
Then there are a finite-type quasi-coherent ideal $\mathcal K$ on $X$ with

$$
|V(\mathcal K)|=|Z|\cup b(|Z'|)
$$

and an isomorphism
$\operatorname{Bl}_{\mathcal I_{Z'}}(X')\cong\operatorname{Bl}_{\mathcal K}(X)$
over $X$. One can take $\mathcal K=\mathcal K(Z')$, the isomorphism being
$\Omega_{Z,Z'}$.
