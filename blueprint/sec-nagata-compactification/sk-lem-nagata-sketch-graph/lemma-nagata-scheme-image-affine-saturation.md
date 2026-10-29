+++
id = "lemma-nagata-scheme-image-affine-saturation"
kind = "lemma"
title = "Affine scheme-image saturation"
order = 241
lean = ["IsLocalization.Away.ker_lift_comp_algebraMap_eq_comap_powTorsion"]
uses = ["def-nagata-power-torsion", "lemma-nagata-power-torsion-kernel-localization", "def-nagata-strict-transform"]
+++
Let $f\colon C\to B$ be a ring map with kernel $K$, so that $C/K\to B$ is
injective, and let $a\in C$ map to a unit of $B$. Put $C_a=C[1/a]$. Then

$$
\ker(C\longrightarrow C_a\longrightarrow B)
=\{c\in C\mid \exists n,\ a^nc\in K\},
$$

and this kernel is the inverse image of
$\Gamma_{(a)}(C/K)$ under $C\to C/K$.
