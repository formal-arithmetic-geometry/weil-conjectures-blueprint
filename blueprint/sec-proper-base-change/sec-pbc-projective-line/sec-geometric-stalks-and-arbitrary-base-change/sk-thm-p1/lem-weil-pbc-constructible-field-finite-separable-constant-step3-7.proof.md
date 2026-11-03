+++
kind = "proof"
of = "lem-weil-pbc-constructible-field-finite-separable-constant-step3-7"
uses = ["lem-weil-pbc-inverse-image-composition", "lemma-constructible-pullback-constant", "lemma-constructible-pullback-locally-constant"]
+++
The covering is jointly surjective, so some member $f:U=U_i\to\operatorname{Spec}k$ has a point $y\in U$ over the unique point of $\operatorname{Spec}k$; $f$ is etale.

Let $K=\kappa(y)$ be the residue field of $U$ at $y$, a $k$-algebra through $f$. The map from $k$ to the residue field of $\operatorname{Spec}k$ at its point is an isomorphism, and the residue field map $\kappa(f(y))\to\kappa(y)$ of an etale morphism is etale; hence $k\to K$ is etale, i.e. $K/k$ is a finite separable field extension. Moreover $\operatorname{Spec}(K)\to\operatorname{Spec}(k)$ is the canonical morphism $g:\operatorname{Spec}\kappa(y)\to U$ followed by $f$.

By hypothesis there are a finite $\Lambda$-module $M$ and an isomorphism of the restriction of $G$ to $U_{\Et}$ with the constant sheaf with value $M$. Identifying the localized site $(\operatorname{Spec}k)_{\Et}/U$ with $U_{\Et}$, this is an isomorphism $f^{-1}G\cong\underline M_U$ [lemma-constructible-pullback-locally-constant].

Finally $\operatorname{Spec}(K)\to\operatorname{Spec}(k)$ equals $f\circ g$, so by the composition isomorphism of inverse images [lem-weil-pbc-inverse-image-composition], the inverse image under $g$ of the isomorphism above, and the canonical isomorphism $g^{-1}\underline M_U\cong\underline M_{\operatorname{Spec}K}$ [lemma-constructible-pullback-constant], the pullback of $G$ to $\operatorname{Spec}K$ is isomorphic to the constant sheaf with value $M$.
