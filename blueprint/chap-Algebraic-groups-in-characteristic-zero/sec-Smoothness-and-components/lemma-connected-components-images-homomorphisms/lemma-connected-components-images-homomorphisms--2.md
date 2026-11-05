+++
id = "lemma-connected-components-images-homomorphisms--2"
kind = "lemma"
title = "Connected components and images of homomorphisms (2)"
name_showing = false
order = 1720003
aliases = ["bp-r534-2"]
lean = ["AlgebraicGeometry.exists_isMonHom_imageι", "AlgebraicGeometry.GeneralLinearGroup.mem_of_mem_closure_of_isConstructible"]
uses = []
+++
The general closed-image statement is bypassed by the Lean route,
which uses the following two forms.

Let $k$ be a field and $f:G\to G'$ a homomorphism of group schemes
over $k$, with $G$ proper and $G'$ separated and locally of finite
type. Its scheme-theoretic image $Z$ is locally of finite type over
$k$, the map $G\to Z$ is surjective, and $Z$ carries a group scheme
structure for which the closed immersion $Z\to G'$ is a homomorphism.

For the other form, let $k$ be algebraically closed, let
$S\subseteq\GL_n(k)$ be a subgroup, and write $T$ for its closure
in $\Spec k[\GL_n]$, viewing rational points as closed points of
this spectrum. Suppose $T$ is irreducible and there is a
constructible subset $Y\subseteq\Spec k[\GL_n]$ with
$\overline Y=T$ such that every $k$-point of $Y$ belongs to $S$.
Then every $k$-point of $T$ belongs to $S$.
