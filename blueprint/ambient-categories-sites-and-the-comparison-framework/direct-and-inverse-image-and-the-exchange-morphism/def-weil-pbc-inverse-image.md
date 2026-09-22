+++
id = "def-weil-pbc-inverse-image"
kind = "definition"
title = "Inverse image and the derived adjunction"
order = 2030
lean = ["AlgebraicGeometry.Etale.upperStar", "AlgebraicGeometry.Etale.upperStarAdjunction"]
uses = ["def-weil-pbc-scheme-conventions", "def-weil-pbc-etale-site", "def-weil-pbc-etale-sheaves", "def-weil-pbc-derived-categories", "def-weil-pbc-direct-image"]
+++
For a morphism [def-weil-pbc-scheme-conventions] $u:U\to V$, inverse image

$$
 u^{-1}:\Ab(V_{\Et})\longrightarrow\Ab(U_{\Et})
$$

is the left adjoint of the direct image [def-weil-pbc-direct-image] $u_*$,
defined by sheafifying the presheaf inverse image along the functor
$U_{\Et}\to V_{\Et}$. Its unit and counit are denoted $\eta_u$ and
$\varepsilon_u$. With a fixed coefficient ring whose pullback is canonically
identified with itself, the same functors act on module sheaves.
