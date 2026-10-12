+++
kind  = "proof"
of    = "lem-sfb-compactification-over-base"
uses = ["sk-thm-nagata-compactification"]
+++
Write $a_X\colon X\to S$ and $a_Y\colon Y\to S$ for the structure morphisms, so $a_X=a_Y\circ f$.
Since $a_X$ is separated, so is $f$. Since $a_X$ is locally of finite type, so is $f$. Since $a_X$
is quasi-compact and $a_Y$ is separated (in particular quasi-separated), $f$ is quasi-compact.
Hence $f$ is separated and of finite type. Moreover $Y$ is quasi-compact, because $a_Y$ is
quasi-compact and $S$ is quasi-compact. And $Y$ is quasi-separated, because $a_Y$ is
quasi-separated and $S$ is quasi-separated. So [sk-thm-nagata-compactification], applied to
$f\colon X\to Y$ over the qcqs base $Y$, gives a compactification of $f$.
