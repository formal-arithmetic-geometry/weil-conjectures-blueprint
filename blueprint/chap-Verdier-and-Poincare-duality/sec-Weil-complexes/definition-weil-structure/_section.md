+++
id = "definition-weil-structure"
kind = "definition"
title = "Weil structure"
order = 876
lean = ["AlgebraicGeometry.Etale.WeilComplex", "AlgebraicGeometry.Etale.WeilComplex.Hom", "AlgebraicGeometry.ProEtale.StrictWeilComplex", "AlgebraicGeometry.ProEtale.StrictWeilComplex.Hom"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image"]
+++
For $K\in D^b_{\mathrm{ctf}}(T,\Lambda)$, a *Weil structure*
is an isomorphism

$$
\phi_K:\operatorname{Fr}_T^*K\xrightarrow{\sim}K.
$$

A *Weil complex* is a pair $(K,\phi_K)$ with this structure.
A morphism $(K,\phi_K)\to(L,\phi_L)$ is a morphism
$h:K\to L$ satisfying

$$
h\circ\phi_K=\phi_L\circ\operatorname{Fr}_T^*(h).
$$
