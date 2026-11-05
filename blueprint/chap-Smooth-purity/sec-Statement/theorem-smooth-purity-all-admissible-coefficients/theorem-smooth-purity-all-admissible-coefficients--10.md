+++
id = "theorem-smooth-purity-all-admissible-coefficients--10"
kind = "theorem"
title = "Composition"
order = 730019
aliases = ["bp-r220-10"]
lean = []
uses = ["definition-tate-twists", "theorem-existence-exceptional-inverse-image", "proposition-composition-open-restriction-compactifications-f"]
+++
This compatibility is bypassed by the Lean route: transporting the chosen orientation through an open image does not establish its compatibility with composition of arbitrary smooth morphisms.

The retained blueprint assertion is the following. For a smooth morphism $h:Y\to Z$ of pure relative dimension $e$ and
$K\in D^b_{\mathrm{ctf}}(Z,\Lambda)$, the map $\gamma_{h\circ f}(K)$ is the composite of
$f^*(\gamma_h(K))(d)[2d]$ and $\gamma_f(h^!K)$, the sources being identified
by $(h\circ f)^*\simeq f^*h^*$ and the targets by the composition
isomorphism $f^!h^!\simeq(h\circ f)^!$ of
Proposition [proposition-composition-open-restriction-compactifications-f](1).
