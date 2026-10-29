+++
id = "thm-nagata-blowup-universal-property"
kind = "theorem"
title = "[stacks-project]"
order = 138
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_lift_blowup", "AlgebraicGeometry.Scheme.IdealSheafData.hom_ext_of_isInvertible_comap"]
uses = ["def-nagata-invertible-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-relative-proj", "def-nagata-sheaf-rees-algebra", "lemma-nagata-invertible-ideal-tensor-power", "lemma-nagata-proj-chart-ring-cocycle", "lemma-nagata-relative-proj-base-change-arbitrary", "lemma-nagata-relative-proj-invertible-tensor-powers", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open"]
+++
Let $\mathcal I$ be a quasi-coherent ideal on a scheme $X$ and let
$t\colon T\to X$ be a morphism such that the extended ideal
$\mathcal I\mathcal O_T$ is invertible. Then there is a unique morphism
$h\colon T\to\operatorname{Bl}_{\mathcal I}(X)$ with
$b_{X,\mathcal I}\circ h=t$. Thus the blow-up is final among $X$-schemes on
which the extended ideal of $\mathcal I$ is invertible.
