+++
id = "prose-02-59"
kind = "hidden"
title = "Extension by zero and completion (1)"
order = 200
+++
The integral coefficient sheaves are inverse limits. To restrict integral
complexes to the strata of a stratification, and to extend them by zero,
we therefore need the functors $j_!$, $j^*$, $i^*$ and $i_*$ to commute
with limits. On the pro-étale site this holds, even for inverse image
along a closed immersion. From this we deduce the localization triangles
and construct the local cohomology functor. With them we can argue with
closed supports before the exceptional inverse image and proper base
change are available.

That $i^*$ commutes with limits is special to the pro-étale site. On
$X_{\acute{e}t}$ the stalk of $i^*F$ at a point of $Z$ is the stalk of $F$. This
is a colimit, and colimits do not commute with infinite products. On
$X_{\mathrm{pro}\acute{e}t}$, the value of $i^*M$ on a weakly contractible affine over $Z$
is the value of $M$ on one affine object of $X_{\mathrm{pro}\acute{e}t}$, henselian along
$Z$ (Proposition [proposition-extension-zero-restriction-closed-subscheme]).
Evaluation on one object preserves limits.
For $\mathcal O_{E,X}=\varprojlim(\mathcal O_E/\pi_E^n)_X$ this means that
$i^*$ applied to the limit is the limit of the restrictions
$(\mathcal O_E/\pi_E^n)_Z$. The same holds for any integral complex given
as a derived limit of its reductions.

A complex over $\mathcal O_E$ is determined by its reductions modulo
$\pi_E^n$ when it is derived complete
(Definition [definition-derived-adic-completeness] below). Combined
with the computation of the cohomology of these reductions on the étale
site, this is how we reduce integral statements to finite coefficients
throughout the notes.
