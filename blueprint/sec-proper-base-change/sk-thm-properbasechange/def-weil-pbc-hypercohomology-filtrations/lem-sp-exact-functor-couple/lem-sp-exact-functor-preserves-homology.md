+++
id = "lem-sp-exact-functor-preserves-homology"
kind = "lemma"
title = "Exact functors preserve kernels, cokernels, images, inverse images and homology"
uses = ["def-sp-abelian"]
refines = "proof/lem-sp-exact-functor-couple"
lean = ["CategoryTheory.Functor.preservesHomologyOfExact"]
tags = ["sheaf-dag", "mathlib", "stacks-010N"]
+++
Let $\mathcal A,\mathcal B$ be abelian categories [def-sp-abelian] and $\Phi:\mathcal A\to\mathcal B$ an exact functor, i.e. an additive functor carrying short exact sequences to short exact sequences, equivalently one commuting with finite limits and finite colimits (Stacks Project, Lemma 12.7.2, Tag 010N). Then:

(a) $\Phi$ carries monomorphisms to monomorphisms and epimorphisms to epimorphisms, and for $u:X\to Y$ the map $\Phi(\ker u)\to\Phi X$ is a kernel of $\Phi u$ and $\Phi Y\to\Phi(\operatorname{coker}u)$ is a cokernel of $\Phi u$; in particular for a subobject $S\subseteq X$ one has $\Phi(X/S)\cong\Phi X/\Phi S$ compatibly with the projections, and if $S\subseteq T\subseteq X$ then $\Phi S\subseteq\Phi T$ as subobjects of $\Phi X$ and $\Phi(T/S)\cong\Phi T/\Phi S$.

(b) For $u:X\to Y$ with image factorization $X\twoheadrightarrow\operatorname{im}u\hookrightarrow Y$, the factorization $\Phi X\twoheadrightarrow\Phi(\operatorname{im}u)\hookrightarrow\Phi Y$ is an image factorization of $\Phi u$: there is a unique isomorphism $\operatorname{im}(\Phi u)\cong\Phi(\operatorname{im}u)$ compatible with the maps from $\Phi X$ and to $\Phi Y$, so $\operatorname{im}(\Phi u)=\Phi(\operatorname{im}u)$ as subobjects of $\Phi Y$.

(c) For a complex $X\xrightarrow{u}Y\xrightarrow{v}Z$ ($vu=0$) with homology $H=\ker v/\operatorname{im}u$, the complex $\Phi X\xrightarrow{\Phi u}\Phi Y\xrightarrow{\Phi v}\Phi Z$ has homology $\ker\Phi v/\operatorname{im}\Phi u\cong\Phi H$, the isomorphism being induced by $\ker\Phi v=\Phi(\ker v)$ and $\operatorname{im}\Phi u=\Phi(\operatorname{im}u)$ of (a), (b) (so compatible with the inclusion of cycles and the projection to homology) and natural in morphisms of such complexes. In particular $\Phi$ carries exact sequences $X\to Y\to Z$ to exact sequences.
