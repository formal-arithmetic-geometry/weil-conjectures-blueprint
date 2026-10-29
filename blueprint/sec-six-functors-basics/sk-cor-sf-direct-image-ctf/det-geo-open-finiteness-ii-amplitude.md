+++
id = "det-geo-open-finiteness-ii-amplitude"
kind = "lemma"
title = "Bounded amplitude of open direct image on classical torsion sheaves"
order = 2706
uses = ["def-kun-cd", "lem-kun-0f10", "def-weil-pbc-site-comparison-morphism", "prop-weil-pbc-site-comparison-finite-level", "prop-weil-pbc-comparison-direct-image"]
+++
Let $k$ be a field, let $\Lambda$ be a finite ring with $\ell^r\Lambda=0$ for
some $r\ge1$, and let $j:X\hookrightarrow Y$ be an open immersion of
finite-type $k$-schemes. Put $d=\operatorname{cd}(j)$ in the sense of
[def-kun-cd]. Then $d<\infty$, and:

1. for every sheaf $F$ of $\Lambda$-modules on $X_{\mathrm{ét}}$ and every
   $q>d$, $R^qj_{\mathrm{ét},*}F=0$;
2. for every such $F$ and every $q>d$,
   $\mathcal H^q\bigl(Rj_{\mathrm{proét},*}\nu_X^*F\bigr)=0$, where
   $\nu_X:X_{\mathrm{proét}}\to X_{\mathrm{ét}}$ is the comparison morphism;
3. consequently, if $M\in D^+(X_{\mathrm{ét}},\Lambda)$ has cohomology in
   degrees $[a,b]$, then $Rj_{\mathrm{proét},*}\nu_X^*M$ has cohomology in
   degrees $[a,b+d]$.
