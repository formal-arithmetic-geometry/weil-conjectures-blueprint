+++
kind  = "proof"
of    = "lemma-nagata-strict-transform-ambient-closed"
uses = ["def-nagata-strict-transform", "thm-nagata-strict-transform-is-blowup"]
+++
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
