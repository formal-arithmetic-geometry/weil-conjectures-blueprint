+++
id = "proposition-comparison-etale-derived-category"
kind = "proposition"
title = "Comparison with the étale derived category"
order = 474
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image"]
+++
For a finite admissible ring $A$, the comparison functor
$\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*}:D(X_{\acute{e}t},A)\to D(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},A)$ identifies

$$
D(X_{\acute{e}t},A)=\Loc(D^b_{\mathrm{ctf}}(X_{\acute{e}t},A))
\simeq\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,A)}).
$$

It preserves arbitrary direct sums. For every morphism $g:X\to Y$ of
schemes of finite type over $k$ and every $K\in D(X_{\acute{e}t},A)$, the
comparison map (2.9)
$\href{@proposition-comparison-morphism-inverse-image}{\nu_Y^*}Rg_{\acute{e}t,*}K\to Rg_{\mathrm{pro}\acute{e}t,*}\href{@proposition-comparison-morphism-inverse-image}{\nu_X^*K}$ is an isomorphism, and
[$\nu^*$](@proposition-comparison-morphism-inverse-image) commutes with inverse images and, by
(2.10), with extension by zero along open
immersions.
