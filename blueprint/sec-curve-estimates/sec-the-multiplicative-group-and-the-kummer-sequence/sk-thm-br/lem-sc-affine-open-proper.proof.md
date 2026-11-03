+++
kind  = "proof"
of    = "lem-sc-affine-open-proper"
+++
The complement $S:=\overline C\setminus U$ is a nonempty closed
subset of dimension at most zero, hence a finite nonempty set of
closed points ([lem-sc-dim0-finite]), and
$U=\overline C\setminus S$. By [lem-sc-point-cartier] each
$P\in S$ is an effective Cartier divisor, so
$D:=\sum_{P\in S}[P]$ is an effective Cartier divisor with support
$S$ ([def-nagata-invertible-ideal]); its degree is
$\deg D=|S|\geq1$ ([def-sc-divisor]), and
$\deg\mathcal O(D)=\deg D>0$ by the well-definedness of the degree
on $\operatorname{Pic}$ ([lem-sc-deg-principal-zero]), so
$\mathcal O(D)$ is ample by [lem-sc-positive-degree-ample].
By [lem-sc-ample-complement-affine],
$U=\overline C\setminus D$ is affine.
