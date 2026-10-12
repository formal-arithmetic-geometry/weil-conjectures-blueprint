+++
id = "thm-sp-truncation-e2"
kind = "theorem"
title = "The truncation hypercohomology spectral sequence"
order = 1280
uses = ["def-sp-convergence", "def-sp-exact-couple", "def-sp-image-filtration", "def-sp-injective-resolutions", "def-sp-truncation-couple", "lem-sp-shift-identification", "lem-sp-truncation-couple-exact", "thm-sp-half-plane-convergence"]
+++
Let $K$ be as in [def-sp-truncation-couple]. The spectral sequence of the
truncation couple [def-sp-truncation-couple] has

$$
 E_2^{p,q}=R^pv\bigl(\mathcal H^q(K)\bigr)
 \Longrightarrow\mathcal H^{p+q}(RvK),
$$

the abutment $\mathcal H^n(RvK)$ carrying the image filtration
[def-sp-image-filtration] of the maps $\mathcal H^n(Rv\,\tau_{\leq q}K)\to
\mathcal H^n(RvK)$; in each degree $n$ only $a\leq q\leq n$ occurs, so the
couple is regular and complete and the convergence is unconditional
([def-sp-convergence]).
