+++
id = "det-def-sfb-module-objects-definition"
kind = "definition"
title = "Module objects over a monoid object"
uses = ["det-def-sfb-ring-object-monoid"]
lean = ["CategoryTheory.ModObj", "CategoryTheory.IsModHom", "CategoryTheory.Mod", "CategoryTheory.Mod.Hom", "CategoryTheory.Mod.regular", "CategoryTheory.Mod.forget"]
order = 1095
+++
Let $(\mathcal C,\otimes,\mathbf 1)$ be a monoidal category with associator $\alpha$ and left
unitor $\lambda$, and let $(\mathcal R,\mu,\eta)$ be a monoid object of $\mathcal C$
([det-def-sfb-ring-object-monoid]).

1. A *(left) $\mathcal R$-module object* is a pair $(M,\gamma_M)$ of an object $M$ of $\mathcal C$ and
   an *action* $\gamma_M\colon\mathcal R\otimes M\to M$ such that
   $$
   \gamma_M\circ(\eta\otimes M)=\lambda_M\colon\mathbf 1\otimes M\to M,\qquad
   \gamma_M\circ(\mu\otimes M)=\gamma_M\circ(\mathcal R\otimes\gamma_M)\circ\alpha_{\mathcal R,\mathcal R,M}\colon(\mathcal R\otimes\mathcal R)\otimes M\to M .
   $$
2. A *morphism of $\mathcal R$-module objects* $f\colon(M,\gamma_M)\to(N,\gamma_N)$ is a morphism
   $f\colon M\to N$ of $\mathcal C$ with $f\circ\gamma_M=\gamma_N\circ(\mathcal R\otimes f)$.
3. The *regular module* is $(\mathcal R,\mu)$.
4. The category $\Mod_{\mathcal R}(\mathcal C)$ has the $\mathcal R$-module objects as objects, the
   morphisms of 2 as morphisms and the composition and identities of $\mathcal C$; the *forgetful
   functor* $\Mod_{\mathcal R}(\mathcal C)\to\mathcal C$ sends $(M,\gamma_M)\mapsto M$ and $f\mapsto f$.
