+++
id = "proposition-weights-under-usual-operations--8"
kind = "proposition"
title = "Punctual upper bounds for tensor products"
order = 1070009
aliases = ["bp-r329-8"]
lean = ["AlgebraicGeometry.WeilSheaf.HasWeightsAtMost.tensorObj"]
uses = ["definition-weights"]
+++
The general assertion that tensor products of mixed sheaves are mixed
is bypassed by the Lean route. The available tensor estimate is punctual:
let $\mathcal F$ be lisse and let $\mathcal G$ be a Weil sheaf. If
$\mathcal F$ and $\mathcal G$ are punctually of weights at most $a$
and $b$, respectively, then $\mathcal F\otimes\mathcal G$ is
punctually of weights at most $a+b$. This conclusion does not assert
the existence of a mixed filtration.
