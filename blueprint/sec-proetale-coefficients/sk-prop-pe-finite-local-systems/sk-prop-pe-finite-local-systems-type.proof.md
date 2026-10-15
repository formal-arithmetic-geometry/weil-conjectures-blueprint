+++
kind = "proof"
of = "det-pe-finite-local-systems-type"
+++
For $M\in R$ let $T_M=\mathcal Isom_{\Lambda_X}(\underline M,F)$, a sheaf of
sets on $X_{\Proet}$. Since $F$ is locally constant of finite presentation, the
map $\coprod_MT_M\to *$ is an epimorphism.

*Models are locally unique.* Let $V$ be a nonempty object with
$T_M(V)\neq\emptyset\neq T_{M'}(V)$. Then $\underline M|_V\cong\underline{M'}|_V$.
Choose a geometric point $\bar v\colon\Spec\Omega\to V$, with $\Omega$ separably
closed. Inverse image along $\bar v$ carries constant sheaves to constant sheaves,
and $\Gamma((\Spec\Omega)_{\Proet},\underline M)=\Gamma((\Spec\Omega)_{\Et},M)=M$
by [det-pe-classical-sheaves-unit] (every étale $\Omega$-scheme is a disjoint
union of copies of $\Spec\Omega$). Hence $M\cong M'$, so $M=M'$.

*The type map.* Let $\underline R$ be the constant sheaf of sets with value $R$.
Define $\tau\colon\coprod_MT_M\to\underline R$ to be the constant section $M$ on
$T_M$. The kernel pair of $\coprod_MT_M\to *$ is
$\coprod_{M,M'}T_M\times T_{M'}$; for $M\neq M'$ the sheaf $T_M\times T_{M'}$ has
sections only over the empty object, by the previous paragraph. So the two
composites of $\tau$ with the projections agree. In a topos an epimorphism is the
coequalizer of its kernel pair, so $\tau$ descends to a global section
$\sigma\in\Gamma(X_{\Proet},\underline R)$. By the unit isomorphism
$\Gamma(X_{\Proet},\underline R)=\Gamma(X_{\Et},R_{X,\Et})$, which is the set of
locally constant functions $X\to R$. Put $X_M=\sigma^{-1}(M)$; these are open,
closed, pairwise disjoint and cover $X$.

*Local models on $X_M$.* If $V\to X_M$ is nonempty and $T_{M'}(V)\neq\emptyset$,
then $\sigma|_V$ is the constant section $M'$ by construction of $\sigma$ and
also $M$ because $V$ maps to $X_M$; hence $M'=M$. Since the $T_{M'}$ jointly
cover, $T_M|_{X_M}\to *$ is an epimorphism, i.e. $F|_{X_M}$ is pro-étale locally
isomorphic to $\underline M$.
