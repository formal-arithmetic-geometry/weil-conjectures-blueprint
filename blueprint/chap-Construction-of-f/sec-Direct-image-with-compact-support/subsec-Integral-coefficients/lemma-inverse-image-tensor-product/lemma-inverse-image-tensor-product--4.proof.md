+++
kind = "proof"
of = "lemma-inverse-image-tensor-product--4"
order = 494009
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--4", "lemma-stability--6", "lemma-stability--7", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "definition-w-local-w-strictly-local--2", "definition-w-local-w-strictly-local--3", "proposition-w-local-components--1", "proposition-pro-etale-affines-form-basis--2", "lemma-inverse-image-tensor-product--6", "proposition-sp-unique-adjoint--1"]
+++
Here $i_*$ sends $\Lambda_Z$-modules to $\Lambda_X$-modules through
$\Lambda_X\to i_*i^{-1}\Lambda_X=i_*\Lambda_Z$, where $i^{-1}\Lambda_X=\Lambda_Z$
because both are pulled back from the point (clause [corollary-finite-quotients-their-transition-maps--3]). On the
pro-étale sites $i_*$ is exact and $i^{-1}i_*=\mathrm{id}$
[Stacks, [09AA](https://stacks.math.columbia.edu/tag/09AA), [09AH](https://stacks.math.columbia.edu/tag/09AH), [09BM](https://stacks.math.columbia.edu/tag/09BM)]. Hence $\mathbf Ri_*$ is computed termwise,
$H^q(\mathbf Ri_*K)=i_*H^q(K)$, and $\mathbf Ri_*K$ is bounded when $K$ is. It
remains to show that $i_*N$ is constructible for a constructible
$\Lambda_Z$-module $N$.

Since the underlying space of $X$ is Noetherian, $X$ and its closed subscheme
$Z$ are quasi-compact and quasi-separated, and every locally closed subset of
$X$ is constructible (Remark [remark-constructible-sheaves-coefficient-rings--1](1)). Choose a finite
stratification $Z=\coprod_aS_a$ for $N$ as in Definition [definition-constructible-sheaves--2]. The
$S_a$, regarded as locally closed subschemes of $X$ via $i$, together with the
open complement $U$ of $Z$, form a finite stratification of $X$ by
constructible locally closed subschemes. On $S_a$ the restriction of $i_*N$ is
the restriction of $i^{-1}i_*N=N$, which satisfies condition (1) of
Definition [definition-constructible-sheaves--1] by the choice of the stratification. On $U$ the
restriction vanishes: for an object $V$ of $X_{\mathrm{pro}\acute{e}t}$ lying over $U$ one has
$V\times_XZ=\emptyset$, so $(i_*N)(V)=N(\emptyset)=0$. The zero module
satisfies condition (1) with $P=0$. Hence $i_*N$ is constructible, and
$\mathbf Ri_*K\in\Dbc(X,\Lambda)$.

*Source:* the proof of Lemma [lemma-inverse-image-tensor-product].
