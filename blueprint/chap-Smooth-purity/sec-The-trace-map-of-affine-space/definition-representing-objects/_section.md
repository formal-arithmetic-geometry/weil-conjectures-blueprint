+++
id = "definition-representing-objects"
kind = "definition"
title = "Representing objects"
order = 739
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-constructible-sheaves", "definition-compactification-refinement"]
+++
Let $f$ be smooth, and let us work in $D(Y,\mathbf Z/\ell^n\mathbf Z)$ and
$D(X,\mathbf Z/\ell^n\mathbf Z)$ on either the étale or the
[pro-étale sites](@definition-small-pro-etale-site). Let $K$ be an object on $Y$. We say that a pair
$(H,\varepsilon)$, where $H$ is an object on $X$ and
$\varepsilon:\href{@proposition-construction-independence-rf-shriek}{Rf_!H}\to K$ is a morphism, *represents*
$\operatorname{Hom}(\href{@proposition-construction-independence-rf-shriek}{Rf_!(-)},K)$ if $b\mapsto\varepsilon\circ \href{@proposition-construction-independence-rf-shriek}{Rf_!(b)}$ is a bijection
$\operatorname{Hom}(M,H)\to\operatorname{Hom}(\href{@proposition-construction-independence-rf-shriek}{Rf_!M},K)$ for all
$M\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,\mathbf Z/\ell^n\mathbf Z)}$.
