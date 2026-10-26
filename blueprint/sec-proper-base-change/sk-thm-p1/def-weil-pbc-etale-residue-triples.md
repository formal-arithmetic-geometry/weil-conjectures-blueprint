+++
id = "def-weil-pbc-etale-residue-triples"
kind = "definition"
title = "The category of étale algebras with a prime and a residue-field embedding"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.Scheme.EtaleResidueTriple", "AlgebraicGeometry.Scheme.EtaleResidueTriples", "AlgebraicGeometry.Scheme.etaleResidueTriplesRingDiagram"]
order = 1622
+++
Let $A$ be a commutative ring, let $p\in\operatorname{Spec}A$, let $K$ be a field, and let $\chi:\kappa(p)\to K$ be a field homomorphism. An *etale residue triple* is $(B,\alpha,q,\phi)$, where $\alpha:A\to B$ is a ring map with $\operatorname{Spec}B\to\operatorname{Spec}A$ etale, $q\in\operatorname{Spec}B$ maps to $p$, and $\phi:\kappa(q)\to K$ is compatible with $\chi$, i.e. $A\xrightarrow{\alpha}B\to\kappa(q)\xrightarrow{\phi}K$ equals $A\to\kappa(p)\xrightarrow{\chi}K$. Its associated map $\psi:B\to K$ is $B\to\kappa(q)\xrightarrow{\phi}K$. The category of etale residue triples has as morphisms $(B,\alpha,q,\phi)\to(B',\alpha',q',\phi')$ the ring maps $\beta:B\to B'$ with $\beta\circ\alpha=\alpha'$ and $\psi'\circ\beta=\psi$, equivalently $\beta^{-1}(q')=q$ and $\phi'\circ\kappa(\beta)=\phi$. The forgetful ring diagram sends a triple to $B$ and a morphism to $\beta$. Residue fields here are those of the affine schemes [def-pc-scheme].
