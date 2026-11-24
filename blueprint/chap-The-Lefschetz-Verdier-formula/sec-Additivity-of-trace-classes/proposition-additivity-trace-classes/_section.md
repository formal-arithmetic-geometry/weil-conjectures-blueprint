+++
id = "proposition-additivity-trace-classes"
kind = "proposition"
title = "Additivity of trace classes"
order = 943
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "corollary-finite-quotients-their-transition-maps", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "proposition-proper-direct-image-constructible-complexes", "lemma-inverse-image-tensor-product", "proposition-composition-base-change-rf-shriek", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "proposition-sp-unique-adjoint", "definition-verdier-dual-evaluation", "definition-correspondence", "definition-trace-class-local-terms", "definition-pushforward-correspondence", "definition-frobenius-correspondences-their-operators", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "lemma-passing-schematic-closure", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $c:C\to X\times X$ be a [correspondence](@definition-correspondence).

1. Let $\mathcal K$ be a finitely filtered complex on $X$ with
   underlying complex $K$ and graded pieces $K_a$ in [$D^b_{\mathrm{ctf}}(X,A)$](@definition-constructible-sheaves), and let
   $\tilde u:c_2^*\mathcal K\to \href{@theorem-existence-exceptional-inverse-image}{c_1^!\mathcal K}$ be a [cohomological
   correspondence](@definition-correspondence) in the filtered derived category, with underlying
   [correspondence](@definition-correspondence) $u$ on $K$ and graded pieces $u_a$ on $K_a$. Then
   $$
   \href{@definition-trace-class-local-terms}{\operatorname{Tr}_c(u)}=\sum_a\href{@definition-trace-class-local-terms}{\operatorname{Tr}_c(u_a)}
   \quad\text{in }H^0(\href{@definition-correspondence}{\Fix(c)},\href{@definition-verdier-dual-evaluation}{\omega_{\Fix(c)}}).
   $$
2. Let $i:Z\to X$ be a closed immersion with open complement $U$ such
   that $c_1^{-1}(Z)\subset c_2^{-1}(Z)$, let $K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,A)}$, and let
   $u$ be a [cohomological correspondence](@definition-correspondence) on $(X,K)$. Then
   $$
   \href{@definition-trace-class-local-terms}{\operatorname{Tr}_c(u)}=\href{@definition-trace-class-local-terms}{\operatorname{Tr}_c(u_U)}+\href{@definition-trace-class-local-terms}{\operatorname{Tr}_c(u_Z)},
   $$
   where $u_U$ and $u_Z$ are the graded pieces of the lift of
   Lemma [lemma-lift-correspondence-invariant-decomposition], and $u_Z$
   is the [pushforward](@definition-pushforward-correspondence) along $i$ and $C_Z\to C$ of the [correspondence](@definition-correspondence)
   $u_{|Z}$ on $(Z,i^*K)$ for $c_Z:C_Z=(c_1^{-1}(Z))_{\mathrm{red}}\to
Z\times Z$ (Lemma [lemma-closed-piece-pushforward]).
