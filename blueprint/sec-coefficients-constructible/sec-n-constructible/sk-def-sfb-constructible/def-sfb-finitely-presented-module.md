+++
id = "def-sfb-finitely-presented-module"
kind = "definition"
title = "Finitely presented module objects"
order = 1255
uses = ["det-def-sfb-module-objects", "det-prop-sfb-module-category"]
lean = ["CategoryTheory.Mod.IsFinitelyPresented"]
+++
Let $\mathcal C$ be an abelian monoidal category whose tensor product is additive, and let
$R$ be a ring object of $\mathcal C$ such that $R\otimes-$ is right exact, so that
$R$-modules [det-def-sfb-module-objects] form an abelian category
[det-prop-sfb-module-category]. Write $R^n=R\oplus\dots\oplus R$ for the free module of
rank $n$. An $R$-module $M$ is *finitely presented* if $M\cong\operatorname{coker}(f)$ for
some morphism $f\colon R^m\to R^n$ of $R$-modules.
