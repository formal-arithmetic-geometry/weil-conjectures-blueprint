+++
id = "det-sp-reduction-exceptional"
kind = "lemma"
title = "Exceptional inverse image of a smooth morphism commutes with extension of coefficients"
order = 2956
uses = ["det-sp-reduction-direct-image", "det-sp-scalar-extension-functor"]
+++
Let $f:X\to Y$ be smooth of pure relative dimension $d$ and $A\to B$ a map of
finite commutative rings killed by a power of $\ell$. For
$K\in\Dctf(Y_{\mathrm{proét}},A)$ let

$$
c_{A,B}(K):(f_A^!K)_B\longrightarrow f_B^!(K_B)\quad\text{in }\Dctf(X_{\mathrm{proét}},B)
$$

be the unique morphism (the transpose under $Rf_{!,B}\dashv f_B^!$) satisfying

$$
\varepsilon_B(K_B)\circ Rf_{!,B}\bigl(c_{A,B}(K)\bigr)
=(\varepsilon_A(K))_B\circ b(f_A^!K)^{-1}.
$$

Then $c_{A,B}(K)$ is natural in $K$ and is an isomorphism. On a coordinate
chart $f|_U=p_d\circ e$ (with $e:U\to\mathbf A^d_Y$ étale, where
$f_A^!=e^*p_d^*(-)(d)[2d]$) it is the canonical isomorphism
$(e^*p_d^*K(d)[2d])_B\simeq e^*p_d^*(K_B)(d)[2d]$.
