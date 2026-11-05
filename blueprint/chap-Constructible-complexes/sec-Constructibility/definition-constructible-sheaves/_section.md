+++
id = "definition-constructible-sheaves"
kind = "definition"
title = "Constructible sheaves"
order = 219
lean = ["AlgebraicGeometry.ProEtale.HasFiniteConstantLocalModel", "AlgebraicGeometry.ProEtale.finiteConstantLocalModel_iff_exists_cover", "AlgebraicGeometry.ProEtale.finiteConstantLocalModelOnCover_iff_scalarMatrix", "AlgebraicGeometry.ProEtale.IsFiniteConstantStratified", "AlgebraicGeometry.ProEtale.IsConstantModelConstructible", "AlgebraicGeometry.ProEtale.ConstantModelConstructible", "AlgebraicGeometry.ProEtale.constantModelBoundedConstructible", "AlgebraicGeometry.ProEtale.ConstantModelBoundedConstructible", "DerivedCategory.torAmplitudeIn", "DerivedCategory.finiteTorAmplitude", "AlgebraicGeometry.ProEtale.ConstantModelConstructibleFiniteTor"]
uses = ["definition-small-pro-etale-site", "proposition-topos-functoriality", "subsec-Coefficient-sheaves", "lemma-inverse-image-coefficient-sheaves", "sec-Derived-functors"]
+++
Let $\Lambda$ be a commutative condensed ring.

1. Consider the following condition on a $\Lambda_X$-module $M$:
   there is a pro-étale cover $\{U_i\to X\}$ and finitely presented
   modules $P_i$ over the ring $\Lambda(*)$ of sections over the point such that
   $$
   M|_{U_i}\simeq\Lambda_{U_i}\otimes_{\Lambda(*)}P_i.
   $$
   Here $\Lambda(*)$ and $P_i$ are constant sheaves on $U_i$, acting
   through $\Lambda(*)\to\Lambda_{U_i}$. Equivalently, on each $U_i$ the
   module $M$ has a presentation by a finite matrix with entries in
   $\Lambda(*)$.
2. For qcqs $X$, a $\Lambda_X$-module $M$ is *constructible* if
   there is a finite stratification of $X$ by constructible locally
   closed subschemes such that on each stratum $S$ the restriction
   $M|_S$ satisfies the condition of (1). On an arbitrary scheme this condition is
   imposed locally on affine opens.

We write $\Cons(X,\Lambda)\subset\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$ for the full
subcategory of constructible sheaves, and $\Dbc(X,\Lambda)\subset
D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ for the full subcategory of bounded complexes with
constructible cohomology sheaves. A complex $K$ has *Tor amplitude
in $[a,b]$* if $K\otimes^{\mathbf L}_{\Lambda_X}N$ has cohomology only
in $[a,b]$ for every sheaf $N$ of $\Lambda_X$-modules. We write
$D^b_{\mathrm{ctf}}(X,\Lambda)$ for the full subcategory of $\Dbc(X,\Lambda)$ of
complexes of finite Tor amplitude.
