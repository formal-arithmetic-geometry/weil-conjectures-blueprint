+++
id = "lemma-nagata-strict-transform-ambient-closed"
kind = "lemma"
title = "[stacks-project]"
order = 164
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_isClosedImmersion_blowup_comap"]
uses = ["def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-strict-transform", "lemma-nagata-strict-transform-closure-characterization", "prop-nagata-global-blowup-cover-independent", "prop-nagata-strict-transform-chart-iso", "prop-nagata-strict-transform-closed-fiber-product", "thm-nagata-strict-transform-is-blowup"]
+++
Let $j\colon Z\hookrightarrow X$ be a closed immersion and let $\mathcal I$
be a quasi-coherent ideal on $X$. Then there is a closed immersion
$k\colon\operatorname{Bl}_{\mathcal I\mathcal O_Z}(Z)\hookrightarrow\operatorname{Bl}_{\mathcal I}(X)$
with $b_{X,\mathcal I}\circ k=j\circ b_{Z,\mathcal I\mathcal O_Z}$.

## Proof

By [thm-nagata-strict-transform-is-blowup], the strict transform is the
blow-up of $Z$ in the extended center ideal. On an affine chart
$X=\operatorname{Spec}(A)$ with $Z=\operatorname{Spec}(B)$, the induced
map to $Z\times_XX'$ is the quotient map
$B\otimes_AA[I/a]\twoheadrightarrow B\otimes_AA[I/a]/\Gamma_{(a)}$. The target chart of the blow-up of $Z$ is
identified with this quotient by
[prop-nagata-strict-transform-chart-iso]. It is therefore precisely
the closed immersion of the closed chart model. These identifications
commute with localization and agree on overlaps by
[prop-nagata-strict-transform-closed-fiber-product]; gluing proves
equality of the two global closed subschemes, as well as the claimed
compatibility with the induced closed immersion.
