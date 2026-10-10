+++
kind  = "proof"
of    = "prop-sf-comparison-bound-zero"
+++
The two inputs are Bhatt–Scholze, Lemma 5.1.1 and Corollary 5.1.6 of
[arXiv:1309.1198v2](https://arxiv.org/html/1309.1198v2), quoted verbatim in
Section 16.1 of the audit ledger; both are stated for an arbitrary scheme and
an arbitrary sheaf, respectively bounded-below complex, on the small étale
site, so a sheaf of $A$-modules on $X_{\Et}$ in the sense of
[def-weil-pbc-etale-sheaves] is covered verbatim. By Lemma 5.1.1, for
$G\in\Sh(X_{\Et})$ and an affine pro-étale $U=\lim_iU_i$ one has
$\nu_X^*G(U)=\colim_iG(U_i)$, the presheaf so defined being a sheaf; by
Lemma 5.1.2 the pullback $\nu_X^*$ is fully faithful, with essential image
exactly those sheaves $F$ on $X_{\Proet}$ whose values on $U=\lim_iU_i$
are the filtered colimits of their values on the $U_i$. The sheaf
$\nu_X^*G$ lies in that essential image, so
$\nu_X^*\nu_{X,*}\nu_X^*G\to\nu_X^*G$ is an isomorphism; applying the fully
faithful $\nu_X^*$ to the two maps $G\to\nu_{X,*}\nu_X^*G$ and
$\nu_{X,*}\nu_X^*G\to G$ that this isomorphism exhibits shows that the
adjunction map $G\to\nu_{X,*}\nu_X^*G$ is an isomorphism in
$\Sh(X_{\Et},A)$. Corollary 5.1.6 is the derived form of the same identity:
$K\to R\nu_{X,*}\nu_X^*K$ is an equivalence for every
$K\in D^+(X_{\Et})$. Taking $K=G$ concentrated in degree zero and passing
to cohomology sheaves gives
$R^q\nu_{X,*}\nu_X^*G=\mathcal H^q(R\nu_{X,*}\nu_X^*G)=0$ for every $q>0$,
which is the displayed vanishing. The identification of the class of étale
origin with the coefficient class [def-sf-fullcd-used-class] is
[lem-sf-proetale-constructible-origin], and the passage from this bound to
the bound $2d$ of [thm-sf-fullcd-etale-origin] in the form of
[def-weil-full-cohomological-dimension] is through the Leray spectral
sequence of [thm-sp-grothendieck], whose $p$-direction is bounded by
$2d$ on the étale site.
