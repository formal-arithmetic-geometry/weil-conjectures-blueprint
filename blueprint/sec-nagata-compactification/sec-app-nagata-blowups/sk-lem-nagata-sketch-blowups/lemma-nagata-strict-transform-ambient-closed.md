+++
id = "lemma-nagata-strict-transform-ambient-closed"
kind = "lemma"
title = "[stacks-project]"
order = 186
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_isClosedImmersion_blowup_comap"]
uses = ["def-nagata-extended-ideal", "def-nagata-global-blowup", "prop-nagata-global-blowup-cover-independent", "prop-nagata-strict-transform-chart-iso", "prop-nagata-strict-transform-closed-fiber-product"]
+++
Let $j\colon Z\hookrightarrow X$ be a closed immersion and let $\mathcal I$
be a quasi-coherent ideal on $X$. Then there is a closed immersion
$k\colon\operatorname{Bl}_{\mathcal I\mathcal O_Z}(Z)\hookrightarrow\operatorname{Bl}_{\mathcal I}(X)$
with $b_{X,\mathcal I}\circ k=j\circ b_{Z,\mathcal I\mathcal O_Z}$.
