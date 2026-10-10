+++
kind  = "proof"
of    = "prop-weil-pbc-gabber-affine-comparison"
+++
*The pair.* Degree zero is the etale henselian restriction lemma
[lemma-weil-pbc-etale-degree-zero]. Let $q>0$ and assume the comparison in
degrees $<q$ for all torsion sheaves.

Injectivity. Both sides commute with filtered colimits of sheaves on the
quasi-compact quasi-separated schemes $T$ and $T_0$, and $F$ is the filtered
union of its subsheaves $F[n]$, so we may assume $nF=0$ for some $n$. Embed
$F$ into an injective sheaf $J$ of $\mathbf Z/n$-modules; $J$ is torsion and
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

*Affine schemes over the pair.* Let $X=\operatorname{Spec}B$ over $A$, so
$X_0=\operatorname{Spec}(B/IB)$, and let $(B^h,IB^h)$ be the henselization of
the pair $(B,IB)$. It is a henselian pair with $B^h/IB^h=B/IB$, and
$B^h=\varinjlim B'$ over the etale $B$-algebras $B'$ with $B/IB\cong
B'/IB'$, i.e. over the affine etale neighbourhoods $U=\operatorname{Spec}B'$
of $X_0$. The first part applied to $(B^h,IB^h)$ gives
$H^q(\operatorname{Spec}B^h,F|)\cong H^q(X_0,F|_{X_0})$, and by continuity of
etale cohomology along the cofiltered limit of affine schemes
$\operatorname{Spec}B^h=\varprojlim U$,
$H^q(\operatorname{Spec}B^h,F|)=\varinjlim_UH^q(U,F|_U)$.
