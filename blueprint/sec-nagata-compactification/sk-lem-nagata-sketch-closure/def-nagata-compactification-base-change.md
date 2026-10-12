+++
id = "def-nagata-compactification-base-change"
kind = "definition"
title = "Base-change construction for a compactification"
order = 83
lean = ["AlgebraicGeometry.Compactification.baseChange", "AlgebraicGeometry.Compactification.ofIsPullback"]
uses = ["def-nagata-compactification"]
+++
Given a compactification $C=(X\to\overline X\to S)$ and $S'\to S$, define
$C_{S'}$ to be

$$
X\times_SS'\longrightarrow\overline X\times_SS'\longrightarrow S'.
$$

More generally, if $u\colon X'\to S'$ is the base change of $f$ along
$S'\to S$ (a cartesian square with top map $h\colon X'\to X$), define the
base-changed factorization of $u$ to be

$$
X'\longrightarrow\overline X\times_SS'\longrightarrow S',
$$

whose first map is induced by $X'\xrightarrow{h}X\to\overline X$ and $u$.
