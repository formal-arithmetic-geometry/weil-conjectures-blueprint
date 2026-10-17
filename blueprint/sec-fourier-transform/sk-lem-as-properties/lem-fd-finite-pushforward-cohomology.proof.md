+++
kind  = "proof"
of    = "lem-fd-finite-pushforward-cohomology"
uses = ["lemma-weil-pbc-finite-direct-image-exact", "lem-weil-pbc-grothendieck-spectral-sequence", "sk-def-sfb-module-derived-pushpull"]
+++
*(1).* By [lemma-weil-pbc-finite-direct-image-exact] the functor $\pi_*$ is exact and $R^q\pi_*=0$ for $q>0$, so the Grothendieck spectral sequence of [lem-weil-pbc-grothendieck-spectral-sequence] for the composite $\Gamma\circ\pi_*$ degenerates and computes the cohomology of $\pi_*\mathcal F$ as the cohomology of $\mathcal F$; explicitly $H^q(X_0,\pi_*\mathcal F)=H^q(\Gamma\circ\pi_*\mathcal F)=H^q(\Gamma_Y\mathcal F)=H^q(Y,\mathcal F)$.

*(2).* Since $\pi$ is finite étale, there is an étale cover $u:U\to X_0$ such that $Y_U=Y\times_{X_0}U$ is a finite disjoint union $\coprod_{i=1}^dU$ of copies of $U$. An étale cover is a pro-étale cover, and $u^*$ is the restriction of sheaves to the slice over $U$; restriction to a slice commutes with derived pushforward of module objects ([sk-def-sfb-module-derived-pushpull]), so
$$
u^*R\pi_*\mathcal F\simeq R\pi_{U,*}(\mathcal F|_{Y_U})\simeq\textstyle\prod_{i=1}^d\mathcal F|_{U_i},
$$
the pushforward along the identity of each copy $U_i\cong U$. This is concentrated in degree $0$, and $u^*$ is exact and conservative because $u$ is a cover; hence $R^q\pi_*\mathcal F=0$ for $q>0$ and $R\pi_*\mathcal F\simeq\pi_*\mathcal F$. Composing derived functors, $R\Gamma(X_{0,\mathrm{proét}},\pi_*\mathcal F)\simeq R\Gamma(X_{0,\mathrm{proét}},R\pi_*\mathcal F)\simeq R\Gamma(Y_{\mathrm{proét}},\mathcal F)$, and taking $H^q$ gives the isomorphism.
