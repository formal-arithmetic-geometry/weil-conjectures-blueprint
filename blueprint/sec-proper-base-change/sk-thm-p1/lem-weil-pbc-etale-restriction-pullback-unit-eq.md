+++
id = "lem-weil-pbc-etale-restriction-pullback-unit-eq"
kind = "lemma"
title = "Pullback of sections along an étale base change agrees with restriction"
uses = ["def-weil-pbc-etale-site", "def-weil-pbc-inverse-image", "def-weil-pbc-direct-image", "lem-weil-pbc-etale-inverse-image-restriction", "lem-weil-pbc-inverse-image-composition"]
lean = ["AlgebraicGeometry.etale_restriction_pullback_unit_eq"]
order = 1834
+++
Let
$$\begin{array}{ccc}W'&\xrightarrow{\;g'\;}&W\\ {\scriptstyle p'}\big\downarrow&&\big\downarrow{\scriptstyle p}\\ Y&\xrightarrow{\;g\;}&X\end{array}$$
be a commutative square of schemes with $p$ étale such that the induced morphism $\iota=(g',p'):W'\to W\times_XY$ is an isomorphism (so $p'$ is étale as well). Regard $(W,p)$ as an object of $X_{\Et}$ and $(W',p')$ as an object of $Y_{\Et}$ [def-weil-pbc-etale-site]. Let $F$ be an abelian sheaf on $X_{\Et}$, let $\rho_F:p^{-1}F\xrightarrow{\sim}F|_W$ and $\rho_{g^{-1}F}:p'^{-1}g^{-1}F\xrightarrow{\sim}(g^{-1}F)|_{W'}$ be the isomorphisms of [lem-weil-pbc-etale-inverse-image-restriction], let $\eta_g$ and $\eta_{g'}$ be the units of the adjunctions $g^{-1}\dashv g_*$ and $g'^{-1}\dashv g'_*$ [def-weil-pbc-inverse-image], [def-weil-pbc-direct-image], and let $\kappa:g'^{-1}p^{-1}F\cong(p g')^{-1}F=(g p')^{-1}F\cong p'^{-1}g^{-1}F$ be built from the composition isomorphisms of [lem-weil-pbc-inverse-image-composition]. Then the following two homomorphisms $\Gamma(W,p^{-1}F)\to(g^{-1}F)(W'\xrightarrow{p'}Y)$ are equal:

1. $\eta_{g',p^{-1}F}(W):\Gamma(W,p^{-1}F)\to(g'^{-1}p^{-1}F)(W\times_WW')$, followed by restriction along $\theta=(g',\mathrm{id}):W'\to W\times_WW'$, by $\kappa(W')$ and by $\rho_{g^{-1}F}(W')$;
2. $\rho_F(W):\Gamma(W,p^{-1}F)\to F(W\xrightarrow{p}X)$, followed by $\eta_{g,F}(W):F(W)\to(g^{-1}F)(W\times_XY)$ and by restriction along the $Y$-morphism $\iota:W'\to W\times_XY$.

In words: under the identifications $\rho$ of inverse images along étale maps with restrictions, pulling a section back along $g'$ agrees with pulling it back along $g$ and restricting along $\iota$.
