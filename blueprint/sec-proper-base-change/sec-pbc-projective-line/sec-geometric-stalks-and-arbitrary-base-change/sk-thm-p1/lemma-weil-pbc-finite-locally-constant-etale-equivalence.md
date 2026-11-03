+++
id = "lemma-weil-pbc-finite-locally-constant-etale-equivalence"
kind = "lemma"
title = "Finite locally constant sheaves and finite-etale schemes"
lean = ["AlgebraicGeometry.Scheme.isFiniteLocallyConstant_yoneda_and_exists_iso", "AlgebraicGeometry.Scheme.EtaleTorsor.exists_toSheafTorsor_equiv"]
order = 1710
+++
Let $T$ be a scheme.

1. For every finite etale morphism $\pi:P\to T$, the functor of points
   $h_P:(U\to T)\mapsto\operatorname{Hom}_T(U,P)$ on $T_{\mathrm{et}}$ is a
   sheaf of sets, and it is finite locally constant.
2. Every finite locally constant sheaf of sets $E$ on $T_{\mathrm{et}}$ is
   isomorphic to $h_P$ for some finite etale $\pi:P\to T$.
3. Let $M$ be a finite abelian group. Every torsor under the constant sheaf
   $\underline M$ on $T_{\mathrm{et}}$ is isomorphic to the sheaf of sections
   of an etale $M$-torsor over $T$: a finite etale surjective $P\to T$ with an
   action of $M$ by $T$-automorphisms for which
   $\coprod_{m\in M}P\to P\times_TP$, $(m,x)\mapsto(mx,x)$, is an isomorphism.

Since $h$ is fully faithful (Yoneda), (1) and (2) say that finite locally
constant sheaves of sets on $T_{\mathrm{et}}$ are equivalent to finite etale
$T$-schemes.
