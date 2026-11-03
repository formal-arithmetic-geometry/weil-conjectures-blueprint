+++
id = "lem-weil-heart-short-exact-triangles"
kind = "lemma"
title = "Short exact sequences in the heart are triangles"
lean = ["CategoryTheory.Triangulated.TStructure.triangle_hom_ext_of_isLE_of_isGE", "CategoryTheory.Triangulated.TStructure.exists_iso_triangleLEGE", "CategoryTheory.Triangulated.TStructure.truncLEFunctor", "CategoryTheory.Triangulated.TStructure.truncGEFunctor", "CategoryTheory.Triangulated.TStructure.truncLEAdjunction", "CategoryTheory.Triangulated.TStructure.truncGEAdjunction", "CategoryTheory.Triangulated.TStructure.heart\u2082", "CategoryTheory.Triangulated.TStructure.exists_isLimit_kernelFork_of_distTriang", "CategoryTheory.Triangulated.TStructure.exists_isColimit_cokernelCofork_of_distTriang", "CategoryTheory.Triangulated.TStructure.eq_of_distTriang_of_heart", "CategoryTheory.Triangulated.TStructure.shortExact_iff_exists_distTriang", "CategoryTheory.Triangulated.TStructure.homology\u2080", "CategoryTheory.Triangulated.TStructure.homology\u2080_exact", "CategoryTheory.Triangulated.TStructure.isHomological_homology\u2080", "AlgebraicGeometry.WeilSheaf.exact_map_higherLowerShriek"]
order = 2224
uses = ["def-weil-t-structure", "prop-weil-heart-abelian"]
+++
Let $(\mathcal T^{\le0},\mathcal T^{\ge0})$ be a t-structure on a
triangulated category $\mathcal T$ in the sense of [def-weil-t-structure]
(not necessarily bounded), and let $\mathcal A=\mathcal
T^{\le0}\cap\mathcal T^{\ge0}$ be its heart, which is abelian by
[prop-weil-heart-abelian].

1. (*Truncations.*) For every $K\in\mathcal T$ and $n\in\mathbf Z$ the
   triangle $\tau^{\le n}K\to K\to\tau^{\ge n+1}K\to\tau^{\le n}K[1]$ with
   $\tau^{\le n}K\in\mathcal T^{\le n}$ and $\tau^{\ge n+1}K\in\mathcal
   T^{\ge n+1}$ is unique up to unique isomorphism, and $\tau^{\le n}$,
   $\tau^{\ge n+1}$ are functors, right, respectively left, adjoint to the
   inclusions of $\mathcal T^{\le n}$ and $\mathcal T^{\ge n+1}$. There is
   a canonical isomorphism $\tau^{\ge0}\tau^{\le0}\cong\tau^{\le0}\tau^{\ge0}$,
   and $H^0:=\tau^{\ge0}\tau^{\le0}:\mathcal T\to\mathcal A$; put
   $H^i(K):=H^0(K[i])$.
2. (*Extensions.*) $\mathcal T^{\le n}$, $\mathcal T^{\ge n}$ and
   $\mathcal A$ are closed under extensions: if $X\to Y\to Z\to X[1]$ is
   distinguished and $X,Z$ lie in one of them, so does $Y$.
3. (*Kernels and cokernels.*) Let $f:X\to Y$ be a morphism of $\mathcal A$
   and complete it to a distinguished triangle $X\xrightarrow fY\to S\to
   X[1]$. Then $S\in\mathcal T^{\le0}\cap\mathcal T^{\ge-1}$,
   $$
   \ker f\cong H^{-1}(S)=(\tau^{\le-1}S)[-1],\qquad
   \operatorname{coker}f\cong H^0(S)=\tau^{\ge0}S,
   $$
   with the kernel map $(\tau^{\le-1}S)[-1]\to S[-1]\to X$ and the
   cokernel map $Y\to S\to\tau^{\ge0}S$.
4. (*Short exact sequences.*) A sequence $0\to X\xrightarrow fY
   \xrightarrow gZ\to0$ of $\mathcal A$ is short exact if and only if
   there is a morphism $\delta:Z\to X[1]$ such that $X\xrightarrow fY
   \xrightarrow gZ\xrightarrow\delta X[1]$ is distinguished, and then
   $\delta$ is unique. In particular a distinguished triangle whose three
   terms lie in $\mathcal A$ is a short exact sequence of $\mathcal A$.
5. (*Cohomological functor.*) $H^0$ is cohomological: a distinguished
   triangle $X\to Y\to Z\to X[1]$ gives a long exact sequence in
   $\mathcal A$
   $$
   \cdots\to H^{i}(X)\to H^{i}(Y)\to H^{i}(Z)\to H^{i+1}(X)\to\cdots .
   $$
