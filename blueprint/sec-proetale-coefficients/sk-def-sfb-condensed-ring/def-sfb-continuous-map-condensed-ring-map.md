+++
id = "def-sfb-continuous-map-condensed-ring-map"
kind = "definition"
title = "Functoriality of $\\underline T$ in $T$"
order = 1524
uses = ["def-sfb-continuous-map-condensed-ring", "sk-def-sfb-ring-object"]
lean = ["Profinite.continuousMapRingSheafMap"]
+++
Let $\varphi\colon T\to T'$ be a continuous ring homomorphism of topological rings. The
maps

$$
\varphi_*\colon\underline T(S)=C(S,T)\to C(S,T')=\underline{T'}(S),\qquad a\mapsto\varphi\circ a,
$$

form a morphism of condensed rings $\varphi_*\colon\underline T\to\underline{T'}$
([def-sfb-continuous-map-condensed-ring]). Hence they also form a morphism of the
underlying ring objects ([sk-def-sfb-ring-object]). This construction is strictly
functorial: $(\mathrm{id}_T)_*=\mathrm{id}$, and $(\psi\circ\varphi)_*=\psi_*\circ\varphi_*$
for a further continuous ring homomorphism $\psi\colon T'\to T''$.
