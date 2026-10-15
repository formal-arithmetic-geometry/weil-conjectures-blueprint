+++
kind = "proof"
of = "det-pe-constructible-comparison-classical"
+++
Since $\Lambda$ is Noetherian, a locally constant sheaf of finite type has
finitely presented models, so it is a local system of finite presentation. The
last sentence follows from the first by [det-pe-constructible-comparison-local],
applied to an open covering by quasi-compact opens on which a partition exists.

We prove the first statement by induction on $n$, for all quasi-compact
quasi-separated schemes simultaneously. If $n=0$ then $X=\emptyset$. If $n=1$,
$F$ is a local system of finite presentation and is classical by
[det-pe-finite-local-systems-twist].

Let $n\geq2$. By [det-pe-constructible-comparison-local] it suffices to show that
every $x\in X$ has an open neighbourhood on which $F$ is classical. Let
$x\in Z_k$. As $Z_k$ is locally closed, there is an affine open $W\ni x$ with
$Z:=Z_k\cap W$ closed in $W$. Let $i\colon Z\to W$ be the closed immersion and
$j\colon U=W\setminus Z\to W$ the open immersion. Since $Z_k$ is constructible,
$Z$ is a constructible closed subset of the affine scheme $W$, so $U$ is
quasi-compact; it is quasi-separated as an open of an affine scheme. By
[sk-prop-sf-open-closed-triangle] there is an exact sequence of
$\Lambda_W$-module sheaves

$$
0\to j_!j^*(F|_W)\to F|_W\to i_*i^*(F|_W)\to0 .
$$

*The open part.* The sets $Z_m\cap U$, $m\neq k$, form a partition of $U$ into at
most $n-1$ constructible locally closed subsets, and $F|_{Z_m\cap U}$ is the
restriction of the local system $F|_{Z_m}$ to an open, hence locally constant of
finite type. By induction $j^*(F|_W)\cong\nu_U^*G$ for an étale module sheaf $G$.
By [lem-cbc-proetale-extension-zero-comparison],
$j_!\nu_U^*G\cong\nu_W^*j_!G$, which is classical.

*The closed part.* $i^*(F|_W)=F|_{Z}$ is a local system of finite type on
$Z_{\Proet}$, hence $\cong\nu_Z^*H$ for an étale module sheaf $H$ by the case
$n=1$. The closed immersion $i$ is quasi-compact and quasi-separated, so
[prop-weil-pbc-comparison-direct-image] gives
$Ri_{\Proet,*}\nu_Z^*H\cong\nu_W^*Ri_{\Et,*}H$. Both direct images along a closed
immersion are exact (on the pro-étale side by
[sk-prop-sf-open-closed-triangle]), so in degree zero
$i_*\nu_Z^*H\cong\nu_W^*i_*H$, which is classical.

*The extension.* $F|_W$ is an extension of two classical module sheaves, hence
classical by [det-pe-classical-derived-weak-serre]. This proves the claim on
the neighbourhood $W$ of $x$.
