+++
id = "lem-weil-pbc-lisse-generic-kernel"
kind = "lemma"
title = "A generic stalk detects kernels in a locally constant sheaf"
lean = ["AlgebraicGeometry.Etale.mono_of_mono_sheafFiber_of_isLocallyConstantSheaf"]
order = 1575
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-flat-lfp-open", "lemma-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-geometric-stalks-exact"]
+++
Let $S$ be an irreducible scheme with generic point $\eta$, let $\Lambda$ be a commutative ring, and fix a separably closed field $\Omega$ and a geometric point $\bar\eta:\operatorname{Spec}\Omega\to S$ with image $\eta$. Let $F$ be a locally constant sheaf of $\Lambda$-modules on the small etale site of $S$, let $G$ be any sheaf of $\Lambda$-modules on the small etale site of $S$ [def-weil-pbc-etale-sheaves], and let $\phi:F\to G$ be a morphism. If the stalk map $\phi_{\bar\eta}$ [def-weil-pbc-geometric-stalks] is injective, then $\phi$ is a monomorphism.
