+++
id = "lemma-weil-pbc-finite-direct-image-exact"
kind = "lemma"
title = "Exactness of finite direct image"
order = 998
lean = ["AlgebraicGeometry.Etale.preservesFiniteColimits_lowerStar_of_isFinite", "AlgebraicGeometry.Etale.rightDerivedFunctorLowerStarIsoMapDerivedCategory"]
uses = ["def-kun-separably-closed", "def-weil-pbc-direct-image", "def-weil-pbc-geometric-fibre", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions", "lemma-openclosed-point-ulift", "lemma-weil-pbc-finite-stalk-formula", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $f:X\to Y$ be a finite morphism of schemes and let $\mathcal A$ be a
Grothendieck abelian coefficient category for which presheaves on small etale
sites can be sheafified, which is concrete over sets with a forgetful functor
that reflects isomorphisms, preserves filtered colimits and is compatible with
the sheaf condition on $Y_{\Et}$ (for instance $\mathcal A=\Mod_\Lambda$).
Then the direct image $f_*:\shv{X_{\Et},\mathcal A}\to\shv{Y_{\Et},\mathcal A}$
is exact. Consequently, whenever the derived categories of $\mathcal A$-valued
etale sheaves on $X$ and $Y$ exist and every complex of sheaves on $X$ has a
K-injective resolution, the total right derived functor $Rf_*$ is isomorphic
to $f_*$ applied termwise to complexes; in particular $R^qf_*=0$ for $q>0$.

## Proof

*Left exactness.* By [def-weil-pbc-direct-image],
$(f_*G)(V)=G(X\times_YV)$ for $V\to Y$ etale. Kernels of sheaves in the
abelian category $\shv{X_{\Et},\mathcal A}$ (and in
$\shv{Y_{\Et},\mathcal A}$) are computed sectionwise, so $f_*$ preserves
kernels and finite products, i.e. finite limits.

*Epimorphisms.* Let $\varphi:G\to G'$ be an epimorphism of $\mathcal A$-valued
sheaves on $X_{\Et}$. For $s\in Y$ let $\bar s$ be the geometric point of $Y$ at
an algebraic closure of $\kappa(s)$. Geometric stalks are colimits, so they
preserve epimorphisms, and by [lemma-weil-pbc-finite-stalk-formula] (which
applies since $\overline{\kappa(s)}$ is algebraically closed) the map
$(f_*\varphi)_{\bar s}$ is identified, naturally in $\varphi$, with
$\prod_{\bar x}\varphi_{\bar x}:\prod_{\bar x}G_{\bar x}\to\prod_{\bar x}G'_{\bar x}$,
the product running over the finite geometric fibre [def-weil-pbc-geometric-fibre]
of $f$ over $\bar s$. A finite product of epimorphisms in the abelian category
$\mathcal A$ is an epimorphism, so $(f_*\varphi)_{\bar s}$ is an epimorphism for
every $s\in Y$. Let $c:f_*G'\to Q$ be the cokernel of $f_*\varphi$. Stalks
commute with cokernels, so $Q_{\bar s}=0$ for every $s$, and the map $0\to Q$
is an isomorphism on all these geometric stalks; by
[lemma-weil-pbc-geometric-stalk-conservative] (its hypotheses on $\mathcal A$
are among ours, and these geometric points are universe-raised as in
[lemma-openclosed-point-ulift]) it is an isomorphism, so $Q=0$ and
$f_*\varphi$ is an epimorphism.

A left exact functor between abelian categories which preserves epimorphisms
preserves homology, hence finite colimits; so $f_*$ is exact.

*Derived functor.* Let $K$ be a complex of $\mathcal A$-valued sheaves on $X$ and
$K\to I$ a K-injective resolution. Then $Rf_*K=f_*I$, and since $f_*$ is exact
it carries the quasi-isomorphism $K\to I$ to a quasi-isomorphism
$f_*K\to f_*I$. These quasi-isomorphisms are natural in $K$, so they give an
isomorphism between $Rf_*$ and $f_*$ applied termwise. For a sheaf $F$ placed
in degree $0$, $R^qf_*F=H^q(f_*F)=0$ for $q>0$.
