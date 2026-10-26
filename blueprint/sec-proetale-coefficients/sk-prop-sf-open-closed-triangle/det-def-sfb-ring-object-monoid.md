+++
id = "det-def-sfb-ring-object-monoid"
kind = "definition"
title = "Ring objects of a monoidal category"
lean = ["CategoryTheory.MonObj", "CategoryTheory.IsMonHom", "CategoryTheory.Mon", "CategoryTheory.Mon.forget", "CategoryTheory.IsCommMonObj"]
order = 1094
+++
Let $(\mathcal C,\otimes,\mathbf 1)$ be a monoidal category with associator $\alpha$, left unitor
$\lambda$ and right unitor $\rho$.

1. A *ring object* (monoid object) of $\mathcal C$ is a triple $(R,\mu,\eta)$ of an object $R$, a
   *multiplication* $\mu\colon R\otimes R\to R$ and a *unit* $\eta\colon\mathbf 1\to R$ such that
   $$
   \mu\circ(\mu\otimes\mathrm{id}_R)=\mu\circ(\mathrm{id}_R\otimes\mu)\circ\alpha_{R,R,R},\qquad
   \mu\circ(\eta\otimes\mathrm{id}_R)=\lambda_R,\qquad
   \mu\circ(\mathrm{id}_R\otimes\eta)=\rho_R .
   $$
2. A *morphism of ring objects* $f\colon(R,\mu,\eta)\to(R',\mu',\eta')$ is a morphism
   $f\colon R\to R'$ of $\mathcal C$ with $f\circ\mu=\mu'\circ(f\otimes f)$ and $f\circ\eta=\eta'$.
   Ring objects and their morphisms, with the composition of $\mathcal C$, form a category
   $\mathrm{Mon}(\mathcal C)$, with a faithful forgetful functor to $\mathcal C$.
3. If $\mathcal C$ is braided with braiding $\beta$, a ring object is *commutative* if
   $\mu\circ\beta_{R,R}=\mu$.
