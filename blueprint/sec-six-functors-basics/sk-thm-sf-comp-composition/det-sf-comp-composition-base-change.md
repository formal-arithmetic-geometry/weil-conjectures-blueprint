+++
id = "det-sf-comp-composition-base-change"
kind = "lemma"
title = "Base change for $Rf_!$ on the localizing category"
order = 2269
uses = ["det-sf-comp-coherence-single", "det-sf-comp-coherence-cocycle", "sk-prop-proper-base-change-unbounded"]
+++
Let $\Lambda$ be admissible, let $f:X\to Y$ be separated of finite type, let
$v:Y'\to Y$ be a morphism with $Y'$ qcqs, and form the cartesian square with
$f':X'=X\times_YY'\to Y'$ and $u:X'\to X$. For a compactification $f=p\circ j$,
$j:X\to\overline X$, let $f'=p'\circ j'$ be its base change, with
$v':\overline X'=\overline X\times_YY'\to\overline X$. Then:

1. there is a canonical isomorphism $v'^*j_!\simeq j'_!u^*$ of functors
$D(X_{\mathrm{proét}},\Lambda)\to D(\overline X'_{\mathrm{proét}},\Lambda)$;
2. the composite
$\beta:v^*Rp_*j_!\xrightarrow{\ \sim\ }Rp'_*v'^*j_!\xrightarrow{\ \sim\ }Rp'_*j'_!u^*$
of proper base change and (1) is an isomorphism of functors
$\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y',\Lambda))$;
3. $\beta$ is compatible with the comparison isomorphisms between
compactifications of $f$ and of $f'$.
