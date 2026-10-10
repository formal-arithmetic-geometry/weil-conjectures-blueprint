+++
kind  = "proof"
of    = "prop-weil-pbc-composition-stability"
+++
After an arbitrary base change $c:Z'\to Z$, write $Y'=Y\times_ZZ'$,
$X'=X\times_ZZ'$, with projections $b:Y'\to Y$ and $a:X'\to X$, and
base-changed maps $f'$, $h'$. Let $I$ be injective in $\mathbf F_r$-module
sheaves on $X$. By [lem-weil-pbc-direct-image-preserves-injectives] the sheaf
$f_*I$ is injective on $Y$. $\mathrm{IA}_r(f)$ gives $R^qf'_*a^{-1}I=0$ for
$q>0$, and the underived proper exchange identifies $f'_*a^{-1}I\cong
b^{-1}f_*I$; $\mathrm{IA}_r(h)$ applied to the injective $f_*I$ makes this
sheaf $h'_*$-acyclic. The Grothendieck spectral sequence of
[lem-weil-pbc-grothendieck-spectral-sequence] therefore vanishes in every
positive total degree, giving $\mathrm{IA}_r(hf)$, and $\mathrm{PBC}(hf)$ by
the equivalence between $\mathrm{PBC}$ and $\mathrm{IA}$ recorded with
[def-weil-pbc-property].
