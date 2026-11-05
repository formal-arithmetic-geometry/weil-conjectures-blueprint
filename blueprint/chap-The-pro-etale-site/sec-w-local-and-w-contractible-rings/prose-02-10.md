+++
id = "prose-02-10"
kind = "hidden"
title = "w-local and w-contractible rings (4)"
order = 49
+++
The constructions below change the set of components while keeping the
local rings, and for this we use the following class of maps. A ring map
$R\to A$ is a *local isomorphism* if $\operatorname{Spec}(A)$ is
covered by principal opens $D(g)$, each mapping isomorphically onto an
open subscheme of $\operatorname{Spec}(R)$ [Stacks, [096E](https://stacks.math.columbia.edu/tag/096E)], and it is
*ind-Zariski* if it is a filtered colimit of local isomorphisms
[Stacks, [096M](https://stacks.math.columbia.edu/tag/096M)]. For instance,
$R\to R\times R$ is a local isomorphism. Taking the colimit over the finite
quotients $S_i$ of a profinite set $S$, we see that
$R\to\varinjlim_iR^{S_i}=LC(S,R)$ is ind-Zariski. Its spectrum is
$\operatorname{Spec}(R)\times S$. A localization $R\to R_{\mathfrak p}$ at a
prime is ind-Zariski as well, as the colimit of the $R_f$ with
$f\notin\mathfrak p$. The property we use is that an ind-Zariski map does
not change local rings: each local ring of $A$ is a local ring of $R$.

We use extremally disconnected spaces through their projectivity. In
Proposition [proposition-splitting-ind-etale-covers] we use it to split a surjection of component
spaces, and in Theorem [theorem-existence-contractible-covers] we cover a profinite component
space by an extremally disconnected one
(Lemma [lemma-extremally-disconnected-covers]).
