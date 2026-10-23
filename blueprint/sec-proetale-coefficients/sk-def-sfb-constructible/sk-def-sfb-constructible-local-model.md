+++
id = "det-def-sfb-constructible-local-model"
kind = "definition"
title = "Finite constant local models"
order = 1243
uses = ["def-sfb-locally-finitely-presented", "def-sfb-finitely-presented-module", "det-def-sfb-pulled-back-coefficients", "def-weil-pbc-proetale-site"]
+++
Let $\Lambda$ be a commutative condensed ring with scalar ring $\Lambda(*)$, the ring of
sections over the one-point profinite set, and let $X$ be a scheme. For $U\in X_{\mathrm{proét}}$
there is a ring map from the constant sheaf $\Lambda(*)_U$ to $\Lambda_U$ (adjoint to
$\Lambda(*)\to\Gamma(U,\Lambda_U)$, the pullback along $U\to *$ of global sections). For a
$\Lambda(*)$-module $P$ put $\Lambda_U\otimes_{\Lambda(*)}P:=\Lambda_U\otimes_{\Lambda(*)_U}P_U$.

A $\Lambda_X$-module $M$ has a *finite constant local model* if there are a pro-étale cover
$\{U_i\to X\}$ and finitely presented $\Lambda(*)$-modules $P_i$ with
$M|_{U_i}\simeq\Lambda_{U_i}\otimes_{\Lambda(*)}P_i$.

**Lemma.** For a $\Lambda_X$-module $M$ and a cover $\{U_i\to X\}$ the following are
equivalent:

1. $M|_{U_i}\simeq\Lambda_{U_i}\otimes_{\Lambda(*)}P_i$ with $P_i$ finitely presented over
   $\Lambda(*)$;
2. $M|_{U_i}\simeq\operatorname{coker}\bigl(\Lambda_{U_i}^{m_i}\xrightarrow{\ A_i\ }\Lambda_{U_i}^{n_i}\bigr)$
   for a matrix $A_i$ with entries in $\Lambda(*)$, acting through $\Lambda(*)\to\Lambda_{U_i}$.

In particular a module with a finite constant local model is locally finitely presented
([def-sfb-locally-finitely-presented]); the converse fails in general, since a local
presentation over $\Lambda_{U}$ may have entries that are not constant.
