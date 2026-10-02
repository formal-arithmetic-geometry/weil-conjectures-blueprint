+++
id = "rem-sf-typing"
kind = "remark"
title = "Typing table: ambient definition, small-category theorem"
order = 2045
+++
For each operation the second column is where it is *defined*, the third
where it is *proved* to descend, with the statement that proves it.
$\Dbc,\Dctf,D_c^{[a,b]}$ are as in [def-sf-categories]; ``ét'' and
``proét'' refer to the small étale and the small pro-étale site.

| operation | ambient definition | descent to small categories (theorem) |
| --- | --- | --- |
| $Lf^*$ | $D(Y,\Lambda)\to D(X,\Lambda)$ | $\Dbc(Y)\to\Dbc(X)$ ([thm-dg-finite-type-constructibility], ét); $\Dctf(Y)\to\Dctf(X)$ ([thm-sf-ctf-stability] (i)) |
| $-\otimes^L-$ | $D(Y)^2\to D(Y)$ | $\Dctf\times\Dbc\to\Dbc$ and $\Dctf\times\Dctf\to\Dctf$ on ét and proét, with $[a,b]+[c,d]\mapsto[a+c,b+d]$ ([thm-sf-ctf-stability] (ii)) |
| $\RHom(-,-)$ | $D(Y)^{\mathrm{op}}\times D(Y)\to D(Y)$ | $\Dctf\times\Dctf\to\Dctf$ on ét for two arbitrary objects, and on proét for pulled-back pairs, with $[a,b],[c,d]\mapsto[c-b-2m,d-a+2m]$ ($\dim Y\le m$), and $[c-b,d-a]$ for a site-perfect first argument ([thm-sf-hom-ctf], [thm-sf-ctf-stability] (ii)) |
| $Rf_*$ | $D^+(X)\to D^+(Y)$ | $\Dbc(X)\to\Dbc(Y)$ for every finite-type $f$ ([thm-dg-finite-type-constructibility]); $\Dctf(X)\to\Dctf(Y)$ on ét and proét, with $[a,b]\mapsto[a,b+2\dim X]$ for $f:X\to Y$ of finite-type $k$-schemes, $k=\overline{\mathbf F}_q$ ([thm-sf-direct-image-tor-amplitude], [cor-sf-direct-image-ctf-proetale], [thm-sf-ctf-stability] (iii)) |
| $Rf_!$ | ambient, via a compactification | $\Dbc(X)\to\Dbc(Y)$ ([thm-dg-finite-type-constructibility]) and $\Dctf(X)\to\Dctf(Y)$ ([thm-sf-ctf-stability] (iv)) |
| $Rf^{\times}$ | $D(Y)\to D(X)$, right adjoint of $Rf_!$; *assumed* to exist (ambient datum) | none: it is an ambient functor, and [thm-amb-etale-exceptional-adjoint] proves it exists on the étale sites unconditionally, and on the pro-étale sites from $\operatorname{FullCD}$, available on the étale-origin class by [thm-sf-fullcd-etale-origin] |
| $Rf^!$ | *defined* as $Rf^{\times}\|_{\Dctf(Y,\Lambda)}$ | $\Dctf(Y)\to\Dctf(X)$ — this is exactly the assertion that the restriction of the previous row to the small subcategories is a functor — for open immersions, finite étale morphisms, closed immersions, smooth $f$, and every $f$ carrying the ambient datum; shifts $-2d$, $2c$, $2d+1$ ([thm-exc-explicit-preservation], [thm-sf-ctf-stability] (v)) |
| $\mathbb D_X$ | $D(X)^{\mathrm{op}}\to D(X)$, $\RHom_X(-,\omega_X)$ | $\Dctf(X)\to\Dctf(X)$, a contravariant anti-equivalence ([thm-sf-biduality-class], [thm-sf-ctf-stability] (vi)) |

The table is an enumeration: every entry is a theorem of the blueprint, and
the conditional entries are listed in [rem-sf-ledger].
