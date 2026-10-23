+++
id = "det-sp-unique-adjoint-coefficients"
kind = "lemma"
title = "Right adjoints inherit the coefficient comparisons"
order = 3028
uses = ["det-sp-unique-right-adjoint"]
+++
Let $\Lambda\to\Lambda'$ be a coefficient extension (subscripts denoting
extension of scalars), with an isomorphism
$b(M):(Rf_{!,\Lambda}M)_{\Lambda'}\xrightarrow{\sim}Rf_{!,\Lambda'}(M_{\Lambda'})$
natural in $M$. Let $J$ be a right adjoint of $Rf_{!,\Lambda}$ (counit
$\varepsilon^J$) and $J'$ a right adjoint of $Rf_{!,\Lambda'}$ (counit
$\varepsilon^{J'}$). Define $c_J(K):(JK)_{\Lambda'}\to J'(K_{\Lambda'})$ in
$\Dctf(X,\Lambda')$ as the $J'$-transpose of
$(\varepsilon^J(K))_{\Lambda'}\circ b(JK)^{-1}$, and let $c_f$ be the map defined
in this way for $f^!_\Lambda$ and $f^!_{\Lambda'}$. Let
$\gamma:f^!_\Lambda\xrightarrow{\sim}J$ and $\gamma':f^!_{\Lambda'}\xrightarrow{\sim}J'$ be
the isomorphisms of [det-sp-unique-right-adjoint]. Then

$$
c_J(K)=\gamma'(K_{\Lambda'})\circ c_f(K)\circ(\gamma(K)^{-1})_{\Lambda'},
$$

so $c_J$ is an isomorphism whenever $c_f$ is, and $c_J$ satisfies the
composition identity for $\Lambda\to\Lambda'\to\Lambda''$ whenever $c_f$ does.
