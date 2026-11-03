+++
id = "lem-weil-pbc-derived-exchange-triangulated"
kind = "lemma"
title = "The derived exchange transformation commutes with shifts and maps triangles to morphisms of triangles"
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-exchange", "def-weil-pbc-derived-inverse-image", "def-weil-pbc-direct-image", "def-sp-kinjective-bridge", "def-weil-pbc-triangles-with-shift", "lem-weil-pbc-derived-direct-image-triangulated"]
lean = ["AlgebraicGeometry.Etale.commShift_derivedBaseChangeMapPlus", "CategoryTheory.NatTrans.mapTriangle"]
order = 2108
tags = ["stacks-0A8D"]
+++
Let $\square=(f,f',g,g',\alpha)$ be a cartesian square of schemes [def-weil-pbc-cartesian-square], with $f:X\to Y$, $g:Y'\to Y$, $f':X'\to Y'$, $g':X'\to X$, and let $\Ex_\square:\Phi:=g^{-1}Rf_*\to\Psi:=Rf'_*g'^{-1}$ be the derived exchange transformation of functors $\Dplus(X_{\Et})\to\Dplus(Y'_{\Et})$ [def-weil-pbc-derived-exchange]. Write $[1 ]$ for the shift of complexes, $(M[1 ])^r=M^{r+1}$, $d_{M[1 ]}=-d_M$. Give each of the four functors $u^{-1}$ [def-weil-pbc-derived-inverse-image] and $Ru_*$ [def-weil-pbc-direct-image] its shift-commutation isomorphism: for $u^{-1}$ the identity $u^{-1}(M[1 ])=(u^{-1}M)[1 ]$ of termwise shifted complexes; for $Ru_*$ the isomorphism $Ru_*(K[1 ])\cong u_*(I(K)[1 ])=(u_*I(K))[1 ]$ obtained by comparing the K-injective resolution $K[1 ]\to I(K[1 ])$ with the K-injective resolution $K[1 ]\to I(K)[1 ]$ [def-sp-kinjective-bridge], [lem-weil-pbc-derived-direct-image-triangulated]. Let $\xi_K:\Phi(K[1 ])\xrightarrow{\sim}\Phi(K)[1 ]$ and $\zeta_K:\Psi(K[1 ])\xrightarrow{\sim}\Psi(K)[1 ]$ be the composite shift-commutation isomorphisms, and $\xi^{(n)}_K:\Phi(K[n ])\xrightarrow{\sim}\Phi(K)[n ]$, $\zeta^{(n)}_K$ ($n\in\mathbf Z$) their iterates (for $n<0$ the inverses of the iterates at $K[n ]$). Then:

(1) for every $K\in\Dplus(X_{\Et})$, $\zeta_K\circ\Ex_{\square,K[1 ]}=\Ex_{\square,K}[1 ]\circ\xi_K$; hence $\zeta^{(n)}_K\circ\Ex_{\square,K[n ]}=\Ex_{\square,K}[n ]\circ\xi^{(n)}_K$ for every $n\in\mathbf Z$;

(2) for every triangle $X_1\xrightarrow{u}X_2\xrightarrow{v}X_3\xrightarrow{w}X_1[1 ]$ in $\Dplus(X_{\Et})$ [def-weil-pbc-triangles-with-shift], the triple $(\Ex_{\square,X_1},\Ex_{\square,X_2},\Ex_{\square,X_3})$ is a morphism of triangles from $(\Phi X_1,\Phi X_2,\Phi X_3,\Phi u,\Phi v,\xi_{X_1}\circ\Phi w)$ to $(\Psi X_1,\Psi X_2,\Psi X_3,\Psi u,\Psi v,\zeta_{X_1}\circ\Psi w)$.

(Part (2) follows from (1) and the naturality of $\Ex_\square$; part (1) says that $\Ex_\square$ is a morphism of triangulated functors.)
