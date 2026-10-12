+++
id = "sk-def-sfb-module-objects"
kind = "definition"
title = "Module objects and the category $\\Mod_{\\Lambda_X}$"
order = 1551
uses = ["def-weil-pbc-proetale-site", "sk-def-sfb-pulled-back-coefficients"]
lean = ["CategoryTheory.ModObj", "CategoryTheory.Mod", "CategoryTheory.Mod.forget", "CategoryTheory.Mod.regular"]
tags = ["sketch"]
+++
Let $(\mathcal C,\otimes,\mathbf 1)$ be a monoidal category with associator $\alpha$ and
left unitor $\lambda$. Let $\mathcal R$ be a monoid object of $\mathcal C$, with
multiplication $\mu\colon\mathcal R\otimes\mathcal R\to\mathcal R$ and unit
$\eta\colon\mathbf 1\to\mathcal R$. When $\mathcal C$ is a category of abelian sheaves with
its tensor product, these are the ring objects of [sk-def-sfb-ring-object].

1. A *(left) $\mathcal R$-module object* is an object $M$ of $\mathcal C$ with an
   *action* $\gamma_M\colon\mathcal R\otimes M\to M$ that is unital and associative:
   $$
   \gamma_M\circ(\eta\otimes M)=\lambda_M,\qquad
   \gamma_M\circ(\mu\otimes M)=\gamma_M\circ(\mathcal R\otimes\gamma_M)\circ\alpha_{\mathcal R,\mathcal R,M}.
   $$
2. A *morphism of $\mathcal R$-module objects* $f\colon M\to N$ is a morphism of
   $\mathcal C$ with $f\circ\gamma_M=\gamma_N\circ(\mathcal R\otimes f)$. With the
   composition of $\mathcal C$, the $\mathcal R$-module objects form a category
   $\Mod_{\mathcal R}(\mathcal C)$. It has a forgetful functor
   $\Mod_{\mathcal R}(\mathcal C)\to\mathcal C$, $(M,\gamma_M)\mapsto M$. The *regular
   module* is $\mathcal R$ itself with action $\mu$.
3. Let $X$ be a scheme with small pro-étale site $X_{\mathrm{proét}}$
   ([def-weil-pbc-proetale-site]). Give $\Sh(X_{\mathrm{proét}},\Ab)$ the tensor product of
   [sk-def-sfb-sheaf-tensor]. Let $\Lambda$ be a condensed ring and let
   $\Lambda_X=p_X^*\Lambda$ be its pullback, a ring object of $\Sh(X_{\mathrm{proét}},\Ab)$
   ([sk-def-sfb-pulled-back-coefficients]). The category of *sheaves of
   $\Lambda_X$-modules* is
   $$
   \Mod_{\Lambda_X}:=\Mod_{\Lambda_X}\bigl(\Sh(X_{\mathrm{proét}},\Ab)\bigr).
   $$
