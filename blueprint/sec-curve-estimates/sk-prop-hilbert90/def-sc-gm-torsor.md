+++
id = "def-sc-gm-torsor"
kind = "definition"
title = "$\\mathbf G_m$-torsors"
order = 878
uses = ["def-sc-curves"]
lean = ["CategoryTheory.Sheaf.Torsor", "AlgebraicGeometry.Scheme.gmSheaf"]
+++
Let $X$ be a scheme (for instance a curve $C$ as in
[def-sc-curves]), and let $\mathbf G_m$ be the sheaf
$U\mapsto\Gamma(U,\mathcal O_U)^{\times}$ on the small etale site
$X_{\Et}$. A
$\mathbf G_m$-*torsor* on $X_{\Et}$ is an etale sheaf $T$
of sets on $X_{\Et}$ together with an action
$\mathbf G_m\times T\to T$ such that for every etale $U\to X$ the
group $\mathbf G_m(U)$ acts freely and transitively on $T(U)$, and
such that $T$ has sections locally: every etale $U\to X$ has an
etale covering $\{U_i\to U\}$ with $T(U_i)\neq\emptyset$.
Equivalently, $T$ is locally isomorphic to $\mathbf G_m$ with its
translation action. A torsor is *trivial* if
it is isomorphic to $\mathbf G_m$. More generally, for an abelian
sheaf $G$ on $X_{\Et}$ a $G$-*torsor* is defined in the same way
with $G$ in place of $\mathbf G_m$; replacing the etale site by the
Zariski site $X_{\mathrm{Zar}}$ and $\mathbf G_m$ by
$\mathcal O_X^{\times}$ gives the notion of a *Zariski*
$\mathcal O_X^{\times}$-torsor.
