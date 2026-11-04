+++
id = "prose-04-17"
kind = "hidden"
title = "Torsion sheaves and acyclicity (6)"
order = 348
+++
To pass from sheaves killed by an integer to all torsion sheaves, we
use continuity of étale cohomology: if $u:T\to S$ is quasi-compact
and quasi-separated, then

$$
\varinjlim_i R^qu_*F_i\xrightarrow{\sim}
R^qu_*\bigl(\varinjlim_i F_i\bigr)\qquad(q\geq0)
\tag{4.7}
$$

for every filtered system of abelian
étale sheaves on $T$. The same
holds after any base change of $u$ [Stacks, [09Z1](https://stacks.math.columbia.edu/tag/09Z1)]. Indeed,
$R^qu_*F$ is the sheafification of
$V\mapsto H^q(T\times_SV,F|_{T\times_SV})$ on affine étale $V\to S$, and
the étale cohomology of the quasi-compact and quasi-separated
scheme $T\times_SV$ commutes with filtered colimits of abelian sheaves
[Stacks, [03Q5](https://stacks.math.columbia.edu/tag/03Q5)].

The following criterion reduces proper base change in higher degrees to
injective acyclicity, a vanishing statement that can be checked on curves.
