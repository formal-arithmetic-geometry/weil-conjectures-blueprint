+++
id = "proposition-topos-functoriality"
kind = "proposition"
title = "The topos and its functoriality"
order = 39
lean = ["AlgebraicGeometry.ProEtale.toposFunctorialityInverseImage", "AlgebraicGeometry.Scheme.ProEt.instSubcanonicalTopology"]
uses = ["lemma-stability"]
+++
The above coverings define a subcanonical site. Its category of sheaves
$\Sh(X_{\mathrm{pro}\acute{e}t})$ is a Grothendieck topos. Every scheme morphism
$f:X\to Y$ induces a geometric morphism

$$
f_{\mathrm{pro}\acute{e}t}:\Sh(X_{\mathrm{pro}\acute{e}t})\longrightarrow\Sh(Y_{\mathrm{pro}\acute{e}t}),
\qquad f^{-1}\dashv f_*.
$$

Here $f^{-1}:\Sh(Y_{\mathrm{pro}\acute{e}t})\to\Sh(X_{\mathrm{pro}\acute{e}t})$ preserves finite
limits and all colimits, and is exact on
abelian sheaves. For a second morphism $g:Y\to Z$ there is a canonical
isomorphism $(g\circ f)^{-1}\simeq f^{-1}\circ g^{-1}$.
