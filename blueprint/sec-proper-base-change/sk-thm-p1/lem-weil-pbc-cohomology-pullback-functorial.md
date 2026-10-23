+++
id = "lem-weil-pbc-cohomology-pullback-functorial"
kind = "lemma"
title = "The pullback on etale cohomology is natural and compatible with composition"
uses = ["def-pc-scheme", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-cohomology-pullback", "def-sp-kinjective-bridge", "def-weil-pbc-inverse-image", "def-weil-pbc-direct-image", "def-weil-pbc-etale-cohomology", "prop-weil-pbc-cohomology-resolution-independent", "lem-weil-pbc-inverse-image-composition"]
lean = ["AlgebraicGeometry.Etale.cohomologyPullbackFunctorial", "AlgebraicGeometry.Etale.cohomologyMap_map"]
order = 1846
tags = ["stacks-01F7"]
+++
For a morphism of schemes $u:Y\to X$ [def-pc-scheme] and an abelian sheaf $G$ on $X_{\Et}$ [def-weil-pbc-abelian-etale-sheaves], let $u^*:H^q(X_{\Et},G)\to H^q(Y_{\Et},u^{-1}G)$ be the pullback map of [def-weil-pbc-cohomology-pullback], built from a K-injective resolution $s:G\to I^\bullet$ and a K-injective resolution $r:u^{-1}I^\bullet\to J^\bullet$ [def-sp-kinjective-bridge], as $\mathcal H^q$ of $a\mapsto r(\eta_u(a))$, $\eta_u$ the unit of $u^{-1}\dashv u_*$ [def-weil-pbc-inverse-image], [def-weil-pbc-direct-image]. For a morphism $\varphi:G\to G'$ of abelian sheaves on a scheme $T$ and K-injective resolutions $G\to I^\bullet$, $G'\to I'^\bullet$, write $H^q(\varphi):H^q(T_{\Et},G)\to H^q(T_{\Et},G')$ [def-weil-pbc-etale-cohomology] for $\mathcal H^q(\Gamma(T,\tilde\varphi))$, where $\tilde\varphi:I^\bullet\to I'^\bullet$ is any morphism of complexes with $\tilde\varphi\circ(G\to I^\bullet)$ homotopic to $(G'\to I'^\bullet)\circ\varphi$; such $\tilde\varphi$ exist and $H^q(\varphi)$ does not depend on $\tilde\varphi$ (step 1 of the proof), and for $\varphi=\mathrm{id}_G$ these are the identifications of the groups computed from different resolutions [prop-weil-pbc-cohomology-resolution-independent]. Then:

1. (Naturality.) For a morphism $\varphi:G\to G'$ of abelian sheaves on $X_{\Et}$, $u^*\circ H^q(\varphi)=H^q(u^{-1}\varphi)\circ u^*$.
2. (Composition and identity.) For a morphism $v:Z\to Y$, let $c_{u,v}:v^{-1}u^{-1}\xrightarrow{\sim}(u\circ v)^{-1}$ be the isomorphism of [lem-weil-pbc-inverse-image-composition] (compatible with the units). Then $(u\circ v)^*=H^q(c_{u,v,G})\circ v^*\circ u^*:H^q(X_{\Et},G)\to H^q(Z_{\Et},(u\circ v)^{-1}G)$, and, with $e_X:\mathrm{id}_X^{-1}\xrightarrow{\sim}\mathrm{id}$ of the same lemma, $H^q(e_{X,G})\circ\mathrm{id}_X^*=\mathrm{id}$.

Both identities hold for any choice of the resolutions, the groups computed from different resolutions being identified as in [prop-weil-pbc-cohomology-resolution-independent].
