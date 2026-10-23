+++
kind  = "proof"
of    = "lem-fd-finite-pushforward-cohomology"
uses = ["lemma-weil-pbc-finite-direct-image-exact", "lem-weil-pbc-grothendieck-spectral-sequence", "lem-fd-proetale-finite-pushforward-exact", "det-prop-sfb-module-pullback-exact-main", "sk-def-sfb-module-derived-pushpull"]
+++
*(1).* By [lemma-weil-pbc-finite-direct-image-exact] the functor $\pi_*$ is exact and $R^q\pi_*=0$ for $q>0$, so the Grothendieck spectral sequence of [lem-weil-pbc-grothendieck-spectral-sequence] for the composite $\Gamma\circ\pi_*$ degenerates and computes the cohomology of $\pi_*\mathcal F$ as the cohomology of $\mathcal F$; explicitly $H^q(X_0,\pi_*\mathcal F)=H^q(\Gamma\circ\pi_*\mathcal F)=H^q(\Gamma_Y\mathcal F)=H^q(Y,\mathcal F)$.

*(2).* A finite étale morphism is finite and of finite presentation, so $\pi_*$ is exact on $\Lambda_Y$-modules and $R\pi_*\mathcal F\simeq\pi_*\mathcal F$ by [lem-fd-proetale-finite-pushforward-exact] (2). Its left adjoint $\pi^*$ is exact ([det-prop-sfb-module-pullback-exact-main]), so $\pi_*$ carries K-injective complexes to K-injective complexes: $\operatorname{Hom}_{K}(C,\pi_*I)=\operatorname{Hom}_K(\pi^*C,I)=0$ for acyclic $C$, as $\pi^*C$ is acyclic. Let $\mathcal F\to I$ be a K-injective resolution in $\Mod_{\Lambda_Y}$ ([sk-def-sfb-module-derived-pushpull]). By exactness, $\pi_*\mathcal F\to\pi_*I$ is a K-injective resolution, and $\Gamma(X_0,\pi_*-)=\Gamma(Y,-)$ since $(\pi_*G)(X_0)=G(Y)$. Hence
$$
R\Gamma(X_{0,\mathrm{proét}},\pi_*\mathcal F)\simeq\Gamma(X_0,\pi_*I)=\Gamma(Y,I)\simeq R\Gamma(Y_{\mathrm{proét}},\mathcal F),
$$
and taking $H^q$ gives the isomorphism.
