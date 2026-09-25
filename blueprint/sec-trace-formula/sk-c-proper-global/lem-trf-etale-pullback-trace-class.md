+++
id = "lem-trf-etale-pullback-trace-class"
kind = "theorem"
title = "Etale pullback compatibility of trace maps"
order = 2503
uses = ["def-trf-etale-base-change", "def-trf-trace-class", "lem-trf-trace-map-etale-pullback", "lem-trf-trace-source-etale-pullback"]
+++
In the situation of [def-trf-etale-base-change], the Verdier trace
classes of [def-trf-trace-class] satisfy

$$
\operatorname{Tr}_{c'}(e^*u)
=
Le_F^*\operatorname{Tr}_c(u).
$$

## Proof

By [def-trf-trace-class] the trace class is the composite of the
mate $\widetilde u:A_C\to\mathcal H_c(K)$ with the trace morphism
$\mathfrak t_{c,K}$, and likewise for $c'$ and $e^*u$: the mate of
$e^*u$ is the pullback of the mate of $u$, which is the
compatibility of the tensor–internal-Hom adjunction with pullback
used in [lem-trf-trace-source-etale-pullback], and the
compatibility of the trace morphisms is
[lem-trf-trace-map-etale-pullback]. Composing the two
compatibilities gives the displayed identity.
