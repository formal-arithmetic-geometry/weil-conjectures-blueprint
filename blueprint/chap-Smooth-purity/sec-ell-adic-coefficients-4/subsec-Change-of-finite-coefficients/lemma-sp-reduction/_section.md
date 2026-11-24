+++
id = "lemma-sp-reduction"
kind = "lemma"
title = "Extension of scalars commutes with $Rf_!$ and $f^!$"
name_showing = false
order = 769
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-sp-scalar-extension", "definition-compactification-refinement"]
+++
For $M\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},A)$ and $K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}}(\href{@definition-small-pro-etale-site}{Y_{\mathrm{pro}\acute{e}t}},A)$ there are natural isomorphisms
$b(M):(\href{@proposition-construction-independence-rf-shriek}{Rf_{!,A}M})_B\xrightarrow{\sim}\href{@proposition-construction-independence-rf-shriek}{Rf_{!,B}}(\href{@definition-sp-scalar-extension}{M_B})$ and
$c_{A,B}(K):(\href{@theorem-existence-exceptional-inverse-image}{f_A^!K})_B\xrightarrow{\sim}\href{@theorem-existence-exceptional-inverse-image}{f_B^!}(\href{@definition-sp-scalar-extension}{K_B})$, where $c_{A,B}(K)$ is determined by

$$
\varepsilon_B(\href{@definition-sp-scalar-extension}{K_B})\circ \href{@proposition-construction-independence-rf-shriek}{Rf_{!,B}}\bigl(c_{A,B}(K)\bigr)
=(\varepsilon_A(K))_B\circ b(\href{@theorem-existence-exceptional-inverse-image}{f_A^!K})^{-1}.
\tag{9.16}
$$

For $A\to B\to C$, the comparisons for $A\to C$ are the composites of those for $A\to B$
and $B\to C$.
