+++
id = "lem-weil-pbc-extension-by-zero-adjunction"
kind = "lemma"
title = "Extension by zero is left adjoint to restriction (étale site)"
uses = ["def-weil-pbc-extension-by-zero", "def-weil-pbc-inverse-image"]
lean = ["AlgebraicGeometry.Etale.openImmersionLowerShriekUpperStarAdjunction"]
order = 1857
+++
Let $\Lambda$ be a commutative ring ($\Lambda=\mathbf Z$ gives abelian sheaves), let $j:U\hookrightarrow X$ be an open immersion of schemes, and let $j_!:\Mod(U_{\Et},\Lambda)\to\Mod(X_{\Et},\Lambda)$ be extension by zero on sheaves of $\Lambda$-modules on the small etale sites [def-weil-pbc-extension-by-zero] and $j^{-1}:\Mod(X_{\Et},\Lambda)\to\Mod(U_{\Et},\Lambda)$ the inverse image [def-weil-pbc-inverse-image]. Then $j_!$ is left adjoint to $j^{-1}$: there are bijections
$$
\Hom_X(j_!F,G)\cong\Hom_U(F,j^{-1}G),
$$
natural in $F\in\Mod(U_{\Et},\Lambda)$ and $G\in\Mod(X_{\Et},\Lambda)$. Under this adjunction a morphism $\alpha:F\to j^{-1}G$ corresponds to the morphism $j_!F\to G$ induced, by the universal property of sheafification, by the presheaf map $(j_{p!}F)(V)=F(V\xrightarrow{\varphi}U)\to G(V)$, $s\mapsto\alpha(s)$ (and $0\to G(V)$ when $V\to X$ does not factor through $U$), where $j^{-1}G(V\xrightarrow{\varphi}U)$ is identified with $G(V\xrightarrow{j\varphi}X)$. In particular the counit $j_!j^{-1}G\to G$ is induced by the identity maps $G(V)\to G(V)$ for $V$ factoring through $U$.
