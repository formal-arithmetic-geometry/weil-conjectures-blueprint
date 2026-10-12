+++
id = "def-weil-locally-ringed-space-morphism"
kind = "definition"
title = "Morphism of locally ringed spaces (continuous map and map of structure sheaves)"
uses = ["def-pc-scheme"]
refines = "def-weil-absolute-frobenius-scheme"
lean = ["AlgebraicGeometry.LocallyRingedSpace.Hom"]
tags = ["sheaf-dag", "mathlib", "stacks-0091"]
+++
A *ringed space* is a pair $(X,\mathcal O_X)$ of a topological space $X$ and a sheaf of commutative rings $\mathcal O_X$ on $X$; it is *locally ringed* if every stalk $\mathcal O_{X,x}$ is a local ring. A *morphism of ringed spaces* $(f,f^\sharp):(X,\mathcal O_X)\to(Y,\mathcal O_Y)$ is a continuous map $f:X\to Y$ together with a map of sheaves of rings $f^\sharp:\mathcal O_Y\to f_*\mathcal O_X$, i.e. ring homomorphisms $f^\sharp_V:\mathcal O_Y(V)\to\mathcal O_X(f^{-1}V)$ for all open $V\subseteq Y$, compatible with restrictions. It is a *morphism of locally ringed spaces* if for every $x\in X$ the induced map of stalks $f^\sharp_x:\mathcal O_{Y,f(x)}\to\mathcal O_{X,x}$ is a local homomorphism (it maps the maximal ideal into the maximal ideal). Composition is $(g,g^\sharp)\circ(f,f^\sharp)=(g\circ f,\,g_*f^\sharp\circ g^\sharp)$. In particular, when $X=Y$ and $f=\mathrm{id}_X$, a morphism $(\mathrm{id}_X,\psi):X\to X$ is the same as an endomorphism $\psi:\mathcal O_X\to\mathcal O_X$ of the sheaf of rings all of whose stalk maps $\psi_x$ are local homomorphisms. A morphism of schemes is a morphism of the underlying locally ringed spaces.
