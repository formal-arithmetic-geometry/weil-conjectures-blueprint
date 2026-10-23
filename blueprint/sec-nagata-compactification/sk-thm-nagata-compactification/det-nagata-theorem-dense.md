+++
id = "det-nagata-theorem-dense"
kind = "theorem"
title = "Nagata compactification with a dense open immersion"
lean = ["AlgebraicGeometry.exists_isDense_compactification"]
order = 103
uses = ["thm-nagata-compactification", "def-nagata-dense-compactification"]
+++
Let $S$ be quasi-compact and quasi-separated and let $f:X\to S$ be separated
and of finite type. Then $f$ has a compactification
$X\xrightarrow{j}\overline X\xrightarrow{p}S$ in which $j$ is a quasi-compact
open immersion and is scheme-theoretically dense, i.e.
$\mathcal O_{\overline X}\to j_*\mathcal O_X$ is injective
([def-nagata-dense-compactification]).
