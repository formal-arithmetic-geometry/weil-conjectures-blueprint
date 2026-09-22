+++
id = "def-sc-gm-torsor"
kind = "definition"
title = "G_m-torsors"
order = 3409
lean = ["AlgebraicGeometry.Etale.IsTorsor"]
uses = ["def-sc-curves"]
+++
Let $C$ be a curve [def-sc-curves]. A $\mathbf G_m$-*torsor* on $C_{\Et}$
is an etale sheaf $T$ on $C_{\Et}$ together with an action
$\mathbf G_m\times T\to T$ which is free and transitive, such that $T$ is
locally isomorphic to $\mathbf G_m$ with its translation action: there is
an etale covering $\{U_i\to C\}$ with
$T|_{U_i}\cong\mathbf G_m|_{U_i}$. A torsor is *trivial* if it is
isomorphic to $\mathbf G_m$.
