+++
kind  = "proof"
of    = "lem-sf-proetale-constructible-origin"
+++
*(i).* The sheaf-level statement is Stacks Project, Pro-étale
Cohomology, Lemma 61.27.2,
[Tag 09AK](https://stacks.math.columbia.edu/tag/09AK), quoted here:
for a scheme $X$ and a Noetherian ring $\Lambda$, the functor
$\epsilon^{-1}$ defines an equivalence of categories between the
constructible sheaves of $\Lambda$-modules on $X_{\Et}$ and the
constructible sheaves of $\Lambda$-modules on
$X_{\mathrm{proet}}$, constructibility being the finite-partition notion
on both sides. The quoted statement applies with
$\epsilon^{-1}=\nu_T^*$, the comparison pullback of
[def-weil-pbc-site-comparison-morphism]; on the étale side the
finite-partition notion is the one of
[def-weil-pbc-constructible-complexes], and on the pro-étale side it
is the intrinsic one of the statement (that of
[def-weil-finite-torsion-constructibility] for $\Lambda=A_{E,n}$).
*(ii).* Let $K$ be a bounded complex of $\Lambda$-module sheaves on
$T_{\Proet}$ with constructible cohomology sheaves, say
$\mathcal H^q(K)=0$ for $q\notin[a,b]$, and argue by induction on
$b-a$. If $a=b$, then $K\cong\mathcal H^a(K)[-a]$, and by (i) the
sheaf $\mathcal H^a(K)$ is $\nu_T^*F'$ for a constructible étale
sheaf $F'$, so $K\cong\nu_T^*(F'[-a])$. If $a<b$, the truncation
triangle $\tau_{\leq b-1}K\to K\to\mathcal H^b(K)[-b]\to$ presents $K$ as
the cone of a morphism
$\mathcal H^b(K)[-b]\to(\tau_{\leq b-1}K)[1]$. Its first term is
$\nu_T^*(F'_b[-b])$ and its second is $\nu_T^*(L'[1])$ for a bounded
complex $L'$ with constructible cohomology on $T_{\Et}$, by (i) and the
induction hypothesis; by [thm-weil-pbc-site-comparison] the pullback
$\nu_T^*$ is fully faithful on bounded-below complexes, so that morphism
is $\nu_T^*(\varphi)$ for a unique
$\varphi:F'_b[-b]\to L'[1]$, and the cone $K'=\operatorname{Cone}(\varphi)$
is a bounded complex on $T_{\Et}$ with constructible cohomology satisfying
$\nu_T^*K'\cong K$, because $\nu_T^*$ is exact. Conversely (i) shows
that the pullback of a bounded complex with constructible cohomology on
$T_{\Et}$ is bounded with constructible cohomology, so the two categories
are equivalent. This is (ii).
