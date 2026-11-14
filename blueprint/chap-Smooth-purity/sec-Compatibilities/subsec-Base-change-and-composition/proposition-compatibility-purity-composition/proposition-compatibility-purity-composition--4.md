+++
id = "proposition-compatibility-purity-composition--4"
kind = "proposition"
title = "Algebraically closed coefficients"
order = 801008
aliases = ["bp-r240-4"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.smoothOrientation_comp_openImmersion", "AlgebraicGeometry.ProEtale.CondensedRing.smoothPurityIso_comp_openImmersion"]
uses = ["definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--3", "proposition-etale-implications--1", "lemma-stability--1", "lemma-stability--2", "lemma-stability--3", "lemma-stability--5", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "proposition-pro-etale-site-separably-closed--3", "corollary-finite-quotients-their-transition-maps--3", "definition-tate-twists--1", "definition-tate-twists--2", "definition-tate-twists--8", "definition-tate-twists--9", "definition-tate-twists--11", "definition-tate-twists--12", "lemma-inverse-image-coefficient-sheaves--1", "lemma-constructible-sheaves--8", "lemma-integral-models--3", "theorem-f-shriek-ell-adic-coefficients--5", "theorem-f-shriek-ell-adic-coefficients--6", "proposition-six-operations-dctf--14", "theorem-smooth-purity-all-admissible-coefficients--4", "corollary-dualizing-complex-smooth-scheme--1", "definition-compactification-refinement--1", "lemma-schematic-closure-uniqueness--1", "proposition-compactifying-union-two-opens--1", "lemma-affine-covers-dense-intersection--1", "lemma-affine-covers-dense-intersection--2", "definition-relative-picard-functor--2"]
+++
For $K\in D^b_{\mathrm{ctf}}(Z_{\mathrm{pro}\acute{e}t},\overline{\mathbf Q}_\ell)$,
the map $\gamma_{g\circ f}(K)$ of (9.2) is the composite

$$
\begin{aligned}
(g\circ f)^{*}K(d+e)[2d+2e]
&\simeq f^{*}\bigl(g^{*}K(e)[2e]\bigr)(d)[2d]\\
&\xrightarrow{\ f^{*}(\gamma_g(K))(d)[2d]\ }
f^{*}\bigl(g^!K\bigr)(d)[2d]\\
&\xrightarrow{\ \gamma_f(g^!K)\ }
f^!g^!K
\simeq(g\circ f)^!K
\end{aligned}
$$

in $D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},\overline{\mathbf Q}_\ell)$, where the coefficient $\overline{\mathbf Q}_\ell$ is omitted
from the displayed composite.
