+++
id = "cor-av-seesaw-descent"
kind = "proposition"
title = "Invertible sheaves trivial over an open cover of the base"
order = 463
tags = ["not-formalized"]
uses = ["def-sc-invertible-module"]
+++
Let $P$ be a proper geometrically integral $k$-scheme, let $T$ be a
$k$-scheme of finite type, let $f:P\times T\to T$ be the projection,
and let $\mathcal L$ be an invertible sheaf on $P\times T$. If $\mathcal L$ is trivial
on $P\times U_\alpha$ for an open cover $(U_\alpha)$ of $T$, then
$\mathcal L\simeq f^*\mathcal M$ with $\mathcal M=f_*\mathcal L$ invertible.

*Not formalized in Lean.* This is Corollary app:abelian-seesaw-descent of the tex, split off
from the lemma "Triviality on fibres" (app:abelian-seesaw). Nothing uses it: the last step of
the proof of the theorem of the cube glues along a section instead, as Lean does. It is
recorded here and will not be formalized.
