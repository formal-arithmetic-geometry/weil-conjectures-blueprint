+++
id = "lemma-sp-reduction"
kind = "lemma"
title = "Extension of scalars commutes with $Rf_!$ and $f^!$"
name_showing = false
order = 769
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-sp-scalar-extension", "definition-compactification-refinement"]
+++
For $M\in D^b_{\mathrm{ctf}}(X_{\mathrm{pro}\acute{e}t},A)$ and $K\in D^b_{\mathrm{ctf}}(Y_{\mathrm{pro}\acute{e}t},A)$ there are natural isomorphisms
$b(M):(Rf_{!,A}M)_B\xrightarrow{\sim}Rf_{!,B}(M_B)$ and
$c_{A,B}(K):(f_A^!K)_B\xrightarrow{\sim}f_B^!(K_B)$, where $c_{A,B}(K)$ is determined by

$$
\varepsilon_B(K_B)\circ Rf_{!,B}\bigl(c_{A,B}(K)\bigr)
=(\varepsilon_A(K))_B\circ b(f_A^!K)^{-1}.
\tag{9.16}
$$

For $A\to B\to C$, the comparisons for $A\to C$ are the composites of those for $A\to B$
and $B\to C$.
