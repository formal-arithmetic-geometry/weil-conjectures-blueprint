+++
id = "proposition-compatibility-purity-composition"
kind = "proposition"
title = "Compatibility of purity with composition"
order = 801
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-pro-etale-site-separably-closed", "corollary-finite-quotients-their-transition-maps", "definition-tate-twists", "lemma-inverse-image-coefficient-sheaves", "lemma-constructible-sheaves", "lemma-integral-models", "theorem-f-shriek-ell-adic-coefficients", "proposition-six-operations-dctf", "theorem-smooth-purity-all-admissible-coefficients", "corollary-dualizing-complex-smooth-scheme", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "definition-relative-picard-functor"]
+++
For every admissible $\Lambda$ and $K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Z,\Lambda)}$,
the map [$\gamma_{g\circ f}(K)$](@theorem-smooth-purity-all-admissible-coefficients) of (9.2) is the composite

$$
\begin{aligned}
(g\circ f)^{*}\href{@definition-tate-twists}{K(d+e)}[2d+2e]
&\simeq f^{*}\bigl(g^{*}\href{@definition-tate-twists}{K(e)}[2e]\bigr)\href{@definition-tate-twists}{(d)}[2d]\\
&\xrightarrow{\ f^{*}(\href{@theorem-smooth-purity-all-admissible-coefficients}{\gamma_g(K)})\href{@definition-tate-twists}{(d)}[2d]\ }
f^{*}\bigl(\href{@theorem-existence-exceptional-inverse-image}{g^!K}\bigr)\href{@definition-tate-twists}{(d)}[2d]\\
&\xrightarrow{\ \href{@theorem-smooth-purity-all-admissible-coefficients}{\gamma_f}(\href{@theorem-existence-exceptional-inverse-image}{g^!K})\ }
\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@theorem-existence-exceptional-inverse-image}{g^!K}
\simeq\href{@theorem-existence-exceptional-inverse-image}{(g\circ f)^!K}
\end{aligned}
$$

in [$D^b_{\mathrm{ctf}}(X,\Lambda)$](@definition-constructible-sheaves), where the coefficient $\Lambda$ is omitted
from the displayed composite.
