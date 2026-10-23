+++
id = "det-lem-int-tensor-shriek"
kind = "lemma"
title = "Extension by zero and closed direct image preserve $\\Dbc(-,\\mathcal O_E)$"
order = 2459
uses = ["sk-prop-integral-criterion", "def-pe-derived-complete", "sk-prop-sf-open-closed-triangle", "sk-def-sfb-constructible", "sk-lem-int-integral-heart"]
+++
Let $X$ be a standing (Noetherian) scheme, $j\colon U\hookrightarrow X$ an open
immersion and $i\colon Z\hookrightarrow X$ a closed immersion.

1. $j_!\colon\D(U_{\mathrm{proét}},\mathcal O_E)\to\D(X_{\mathrm{proét}},\mathcal O_E)$ and
   $i_*\colon\D(Z_{\mathrm{proét}},\mathcal O_E)\to\D(X_{\mathrm{proét}},\mathcal O_E)$ map
   $\Dbc(U,\mathcal O_E)$ into $\Dbc(X,\mathcal O_E)$, respectively $\Dbc(Z,\mathcal O_E)$
   into $\Dbc(X,\mathcal O_E)$. Hence so does $a_!=i_*u_!$ for every locally
   closed immersion $a=i\circ u\colon S\hookrightarrow X$ ($u$ open, $i$ closed).
2. Every $K\in\Dbc(X,\mathcal O_E)$ lies in the smallest full subcategory of
   $\D(X_{\mathrm{proét}},\mathcal O_E)$ that is closed under isomorphisms and
   extensions (if two vertices of a distinguished triangle lie in it, so does
   the third) and contains the objects $a_!M$, where
   $a\colon S\hookrightarrow X$ is the inclusion of a stratum of a finite
   stratification and $M\in\Dbc(S,\mathcal O_E)$ is pro-étale locally on $S$ of the
   form $P\otimes_{\mathcal O_E}\mathcal O_{E,S}$ for a bounded complex $P$ of finite
   free $\mathcal O_E$-modules.
