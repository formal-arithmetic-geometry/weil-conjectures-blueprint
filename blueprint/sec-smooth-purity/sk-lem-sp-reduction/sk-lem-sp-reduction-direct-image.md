+++
id = "det-sp-reduction-direct-image"
kind = "lemma"
title = "Compactly supported direct image commutes with extension of coefficients"
order = 2955
uses = ["det-sp-scalar-extension-functor", "lem-sf-flat-model"]
+++
Let $f:X\to Y$ be a separated morphism of finite type with a compactification
$f=\bar f\circ j$ ($j$ an open immersion, $\bar f$ proper), and let $A\to B$ be
a map of finite commutative rings killed by a power of $\ell$. For
$M\in\Dctf(X_{\mathrm{proét}},A)$ there is an isomorphism in
$\Dctf(Y_{\mathrm{proét}},B)$, natural in $M$,

$$
b(M):(Rf_{!,A}M)_B=(R\bar f_{*}j_!M)\otimes^{\mathbf L}_{A_Y}B_Y
\xrightarrow{\ \sim\ }R\bar f_{*}j_!(M\otimes^{\mathbf L}_{A_X}B_X)=Rf_{!,B}(M_B),
$$

with no flatness or finite projective dimension hypothesis on $B$ over $A$.
For a further map $B\to C$, $b$ for $A\to C$ is the composite of $(b)_C$ for
$A\to B$, $b$ for $B\to C$ and the associativity isomorphisms of
[det-sp-scalar-extension-functor].
