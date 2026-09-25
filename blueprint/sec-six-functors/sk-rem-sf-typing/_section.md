+++
id = "sk-rem-sf-typing"
kind = "section"
title = "Typing table: ambient definition, small-category theorem"
order = 2044
+++
*Remark (sketch).*

For each operation the second column is where it is *defined*, the third
where it is *proved* to descend, with the statement that proves it.
$\Dbc,\Dctf,D_c^{[a,b]}$ are as in [sk-def-sf-categories]; ``ét'' and
``proét'' refer to the small étale and the small pro-étale site.

| operation | ambient definition | descent to small categories (theorem) |
| --- | --- | --- |
| $Lf^*$ | $D(Y,\Lambda)\to D(X,\Lambda)$ | $\Dbc(Y)\to\Dbc(X)$ ([sk-prop-sf-finiteness], ét); $\Dctf(Y)\to\Dctf(X)$ ([sk-thm-sf-ctf-stability] (i)) |
| $-\otimes^L-$ | $D(Y)^2\to D(Y)$ | $\Dctf\times\Dbc\to\Dbc$ and $\Dctf\times\Dctf\to\Dctf$ on ét and proét, with $[a,b]+[c,d]\mapsto[a+c,b+d]$ ([sk-thm-sf-ctf-stability] (ii)) |
| $\RHom(-,-)$ | $D(Y)^{\mathrm{op}}\times D(Y)\to D(Y)$ | $\Dctf\times\Dctf\to\Dctf$ on ét for two arbitrary objects, and on proét for pulled-back pairs, with $[a,b],[c,d]\mapsto[c-b-2m,d-a+2m]$ ($\dim Y\le m$), and $[c-b,d-a]$ for a site-perfect first argument ([sk-thm-sf-hom-ctf], [sk-thm-sf-ctf-stability] (ii)) |
| $Rf_*$ | $D^+(X)\to D^+(Y)$ | $\Dbc(X)\to\Dbc(Y)$ for every finite-type $f$ ([sk-prop-sf-finiteness]); $\Dctf(X)\to\Dctf(Y)$ on ét and proét, with $[a,b]\mapsto[a,b+2\dim X]$ ([sk-thm-sf-direct-image-tor-amplitude], [sk-cor-sf-direct-image-ctf], [sk-thm-sf-ctf-stability] (iii)) |
| $Rf_!$ | ambient, via a compactification | $\Dbc(X)\to\Dbc(Y)$ ([sk-prop-sf-finiteness]) and $\Dctf(X)\to\Dctf(Y)$ ([sk-thm-sf-ctf-stability] (iv)) |
| $Rf^{\times}$ | $D(Y)\to D(X)$, right adjoint of $Rf_!$; *assumed* to exist (ambient datum) | none: it is an ambient functor, and [sk-prop-sf-existence] proves it exists on the étale sites unconditionally, and on the pro-étale sites from $\operatorname{FullCD}$, available on the étale-origin class by [sk-prop-sf-fullcd-etale-origin] |
| $Rf^!$ | *defined* as $Rf^{\times}\|_{\Dctf(Y,\Lambda)}$ | $\Dctf(Y)\to\Dctf(X)$ — this is exactly the assertion that the restriction of the previous row to the small subcategories is a functor — for open immersions, finite étale morphisms, closed immersions, smooth $f$, and every $f$ carrying the ambient datum; shifts $-2d$, $2c$, $2d+1$ ([sk-prop-sf-rf-shriek-preservation], [sk-thm-sf-ctf-stability] (v)) |
| $\mathbb D_X$ | $D(X)^{\mathrm{op}}\to D(X)$, $\RHom_X(-,\omega_X)$ | $\Dctf(X)\to\Dctf(X)$, a contravariant anti-equivalence ([sk-prop-sf-biduality-general], [sk-thm-sf-ctf-stability] (vi)) |

The table is an enumeration: every entry is a theorem of the blueprint, and
the conditional entries are listed in [sk-rem-sf-ledger].
