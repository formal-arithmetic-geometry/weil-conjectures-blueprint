+++
id = "lem-weil-pbc-finite-free-constant-map-etale-factorization"
kind = "lemma"
title = "Étale-local factorization of a finite free constant map"
uses = ["def-constructible-constant", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Scheme.exists_etale_factorization_of_finite_free_constant_map"]
order = 1881
+++
Let $X$ be a scheme [def-weil-pbc-scheme-conventions], $\Lambda$ a commutative ring, $F$ and $G$ sheaves of $\Lambda$-modules on the small etale site of $X$ [def-weil-pbc-etale-site], and $\varphi:F\to G$ any morphism. Let $n\ge0$, let $Q=\underline{\Lambda^{n}}_X$ be the constant sheaf with value $\Lambda^n$ [def-constructible-constant], and let $\alpha:Q\to G$ be a morphism. Let $x\in X$ and let $\bar x$ be the geometric point of $X$ at $x$ given by an algebraic closure of $\kappa(x)$ [def-weil-pbc-geometric-stalks]. Suppose a $\Lambda$-linear map $l:Q_{\bar x}\to F_{\bar x}$ satisfies $\varphi_{\bar x}\circ l=\alpha_{\bar x}$. Then there are an etale morphism $v:V\to X$ whose image contains $x$ and a morphism $\beta:v^{-1}Q\to v^{-1}F$ with $v^{-1}\varphi\circ\beta=v^{-1}\alpha$. No monomorphism hypothesis on $\varphi$ is required.
