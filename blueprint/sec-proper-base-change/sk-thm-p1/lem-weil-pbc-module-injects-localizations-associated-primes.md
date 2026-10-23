+++
id = "lem-weil-pbc-module-injects-localizations-associated-primes"
kind = "lemma"
title = "A module over a Noetherian ring embeds in the product of its localizations at its associated primes"
lean = ["Module.injective_pi_localization_associatedPrimes"]
order = 1893
+++
Let $R$ be a Noetherian ring and $M$ an $R$-module. Call a prime ideal $\mathfrak p\subset R$ an associated prime of $M$ if $\mathfrak p=\{a\in R:az=0\}$ for some $z\in M$, and write $\operatorname{Ass}(M)$ for the set of them. For a prime $\mathfrak p$ let $M_{\mathfrak p}$ be the localization of $M$ at $R\setminus\mathfrak p$. Then the $R$-linear map $M\to\prod_{\mathfrak p\in\operatorname{Ass}(M)}M_{\mathfrak p}$, $m\mapsto(m/1)_{\mathfrak p}$, is injective (the empty product being $0$). Equivalently: if $m\in M$ and for every $\mathfrak p\in\operatorname{Ass}(M)$ there is $s\in R\setminus\mathfrak p$ with $sm=0$, then $m=0$.
