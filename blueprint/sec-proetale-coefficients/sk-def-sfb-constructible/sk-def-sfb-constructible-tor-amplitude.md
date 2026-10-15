+++
id = "det-def-sfb-constructible-tor-amplitude"
kind = "definition"
title = "Tor amplitude and $D^b_{ctf}(X,\\Lambda)$"
uses = ["det-def-sfb-constructible-local-model", "def-sfb-constructible-module", "sk-def-sfb-bounded-constructible", "sk-def-sfb-derived-tensor-hom"]
+++
Let $\Lambda$ be a commutative condensed ring and $X$ a scheme.

1. $\Cons(X,\Lambda)\subset\Mod(X_{\mathrm{proét}},\Lambda)$ is the full subcategory of
   constructible $\Lambda_X$-modules (strata on which the module has a finite constant local
   model, [det-def-sfb-constructible-local-model]).
2. $\Dbc(X,\Lambda)\subset D(X_{\mathrm{proét}},\Lambda)$ is the full subcategory of complexes
   $K$ with $H^q(K)=0$ for all but finitely many $q$ and every $H^q(K)$ in $\Cons(X,\Lambda)$.
3. For integers $a\le b$, $K\in D(X_{\mathrm{proét}},\Lambda)$ has *Tor amplitude in $[a,b]$*
   if $H^q(K\otimes^{\mathbf L}_{\Lambda_X}N)=0$ for $q\notin[a,b]$ and every
   $\Lambda_X$-module $N$; it has *finite Tor amplitude* if this holds for some $a\le b$.
4. $\Dctf(X,\Lambda)\subset\Dbc(X,\Lambda)$ is the full subcategory of complexes of finite
   Tor amplitude.

**Well-definedness.** All four conditions are invariant under isomorphism in the respective
categories, so these are full replete subcategories. If $K$ has Tor amplitude in $[a,b]$ then
$K[1]$ has Tor amplitude in $[a-1,b-1]$. If $K'\to K\to K''\to K'[1]$ is a distinguished
triangle and $K',K''$ have Tor amplitude in $[a,b]$, so does $K$; and a direct summand of a
complex with Tor amplitude in $[a,b]$ has Tor amplitude in $[a,b]$. Hence the complexes of
finite Tor amplitude form a thick subcategory of $D(X_{\mathrm{proét}},\Lambda)$, and
$\Dctf(X,\Lambda)$ is the intersection of this thick subcategory with $\Dbc(X,\Lambda)$.
