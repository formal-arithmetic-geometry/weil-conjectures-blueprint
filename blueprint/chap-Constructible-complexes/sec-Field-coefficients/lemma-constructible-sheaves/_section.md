+++
id = "lemma-constructible-sheaves"
kind = "lemma"
title = "Abelian category of constructible sheaves"
order = 268
lean = ["AlgebraicGeometry.ProEtale.coefficientHeart"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "definition-lisse-sheaves", "proposition-sp-unique-adjoint", "lemma-schematic-closure-uniqueness"]
+++
Let $\Lambda=E$ or $\overline{\mathbf Q}_\ell$.

1. $\Cons(X,\Lambda)$ is closed under kernels, cokernels and
   extensions in $\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$. In particular it is an abelian
   category, and its inclusion into $\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is exact.
2. $\Cons(X,\Lambda)$ is essentially small.
3. Every $F\in\Cons(X,\Lambda)$ has a finite filtration
   $0=F_0\subset F_1\subset\cdots\subset F_m=F$ whose subquotients
   $F_k/F_{k-1}$ are of the form $a_!L$, with $a:S\hookrightarrow X$ a
   locally closed immersion and $L$ a lisse $\Lambda_S$-module.
