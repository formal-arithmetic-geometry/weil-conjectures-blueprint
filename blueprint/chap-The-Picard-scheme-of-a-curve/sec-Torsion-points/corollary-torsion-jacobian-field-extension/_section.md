+++
id = "corollary-torsion-jacobian-field-extension"
kind = "corollary"
title = "Torsion of the Jacobian and field extension"
order = 1561
lean = ["AlgebraicGeometry.Scheme.Hom.pic_proper_ntorsion", "AlgebraicGeometry.Scheme.surjective_pow_picardZero"]
uses = ["definition-abelian-variety", "lemma-abelian-variety-commutative", "theorem-picard-scheme-jacobian-over-separably"]
+++
Let $k$ be algebraically closed, let $C/k$ be a smooth proper
connected curve of genus $g$, and let $n>0$ be invertible in $k$.
Then there is a noncanonical isomorphism

$$
\href{@theorem-picard-scheme-jacobian-over-separably}{J(C)}\href{@definition-abelian-variety}{[n]}(k)\simeq(\mathbf Z/n\mathbf Z)^{2g}.
$$

For every algebraically closed
extension $k'/k$, the natural map

$$
\href{@theorem-picard-scheme-jacobian-over-separably}{J(C)}\href{@definition-abelian-variety}{[n]}(k)\longrightarrow \href{@theorem-picard-scheme-jacobian-over-separably}{J(C_{k'})}\href{@definition-abelian-variety}{[n]}(k')
$$

is an isomorphism. Multiplication by $n$ on [$J(C)(k)$](@theorem-picard-scheme-jacobian-over-separably) is
surjective, and consequently

$$
\operatorname{Pic}(C)[n]=\href{@theorem-picard-scheme-jacobian-over-separably}{J(C)}\href{@definition-abelian-variety}{[n]}(k),
\qquad
\operatorname{Pic}(C)/n\operatorname{Pic}(C)
\xrightarrow[\deg]{\ \sim\ }\mathbf Z/n\mathbf Z.
$$
