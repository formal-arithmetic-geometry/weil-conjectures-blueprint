+++
kind  = "proof"
of    = "prop-weil-pbc-gabber-affine-comparison"
+++
*The pair.* Degree zero is the étale henselian restriction lemma
[lemma-weil-pbc-etale-degree-zero]. Let $q>0$ and assume the comparison in
degrees $<q$ for all torsion sheaves.

Injectivity. Both sides commute with filtered colimits of sheaves on the
quasi-compact quasi-separated schemes $T$ and $T_0$, and $F$ is the filtered
union of its subsheaves $F[n]$, so we may assume $nF=0$ for some $n$. Embed
$F$ into an injective sheaf $J$ of $\Lambda/n\Lambda$-modules; $J$ is torsion and
$H^q(T,J)=0$. Put $Q=J/F$, again killed by $n$. Let $\xi\in H^q(T,F)$
restrict to $0$. Write $\xi=\delta(\zeta)$ with $\zeta\in H^{q-1}(T,Q)$. Its
restriction $\zeta_0$ satisfies $\delta_0(\zeta_0)=\xi_0=0$, so $\zeta_0$
comes from some $\theta_0\in H^{q-1}(T_0,J_0)$; by the induction hypothesis
$\theta_0$ is the restriction of some $\theta\in H^{q-1}(T,J)$. Then
$\zeta-\bar\theta$ (with $\bar\theta$ the image of $\theta$ in
$H^{q-1}(T,Q)$) restricts to $0$, hence is $0$ by injectivity in degree
$q-1$. So $\zeta=\bar\theta$ and $\xi=\delta(\bar\theta)=0$.

Surjectivity. Let $\eta\in H^q(T_0,F_0)$. By
[lemma-weil-pbc-gabber-effacement] there is a monomorphism $F\hookrightarrow
F'$ of torsion sheaves such that the image of $\eta$ in $H^q(T_0,F'_0)$ is
zero. Put $Q=F'/F$, a torsion sheaf. Then $\eta=\delta_0(\theta_0)$ for some
$\theta_0\in H^{q-1}(T_0,Q_0)$, which by the induction hypothesis is the
restriction of some $\theta\in H^{q-1}(T,Q)$; the boundary
$\delta(\theta)\in H^q(T,F)$ restricts to $\delta_0(\theta_0)=\eta$, by
naturality of the boundary maps under restriction.

*Closed subschemes of affine schemes.* Let $X=\operatorname{Spec}B$ and
$Z=\operatorname{Spec}(B/K)$, and let $(B^h,KB^h)$ be the henselization of the
pair $(B,K)$. It is a henselian pair with $B^h/KB^h=B/K$, and
$B^h=\varinjlim B'$ over the étale $B$-algebras $B'$ with $B/K\cong B'/KB'$, i.e.
over the affine étale neighbourhoods $U=\operatorname{Spec}B'$ of $Z$; these
form a directed system, and $Z\to\operatorname{Spec}B^h\to U$ are the
factorizations of $i$. The first part, applied to the henselian pair
$(B^h,KB^h)$ and the pullback of $F$ (which is again torsion), gives
$H^q(\operatorname{Spec}B^h,F|)\cong H^q(Z,i^{-1}F)$, and by continuity of étale
cohomology along the cofiltered limit of affine schemes
$\operatorname{Spec}B^h=\varprojlim U$,
$H^q(\operatorname{Spec}B^h,F|)=\varinjlim_UH^q(U,F|_U)$. All maps are pullback
maps, so the composite is the map induced by the $s_U^*$.
