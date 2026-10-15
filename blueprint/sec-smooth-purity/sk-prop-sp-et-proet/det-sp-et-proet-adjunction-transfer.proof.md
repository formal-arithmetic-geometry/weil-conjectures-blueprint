+++
kind = "proof"
of = "det-sp-et-proet-adjunction-transfer"
uses = ["thm-weil-pbc-site-comparison", "thm-sf-ambient-adjoint-class"]
+++
Let $M'=\nu_X^*M\in\Dctf(X,A)$ and $N'=\nu_Y^*N\in\Dctf(Y,A)$, with
$M\in\Dctf(X_{\mathrm{ét}},A)$, $N\in\Dctf(Y_{\mathrm{ét}},A)$; every object is of this form
by the equivalence. Full faithfulness of $\nu^*$ on bounded-below complexes
([thm-weil-pbc-site-comparison]) and $c_f$ give natural bijections

$$
\Hom(M',G^{\mathrm{pro}}N')=\Hom(\nu_X^*M,\nu_X^*GN)\simeq\Hom(M,GN)
\simeq\Hom(Rf^{\mathrm{ét}}_!M,N)\simeq\Hom(\nu_Y^*Rf^{\mathrm{ét}}_!M,\nu_Y^*N)
\simeq\Hom(Rf_!M',N'),
$$

natural in $M'$ and $N'$ (naturality in $M'$ uses that $\nu_X^*$ is full, so
every morphism between objects $\nu_X^*M_1\to\nu_X^*M_2$ comes from the étale
site, and that $c_f$ is natural). Following the identity of $G^{\mathrm{pro}}N'$
through these bijections gives the stated counit. This is an adjunction $Rf_!\dashv G^{\mathrm{pro}}$ on the
pro-étale categories.

The Brown adjoint $f^!$ restricted to $\Dctf$ is also a right adjoint of
$Rf_!$ there (it preserves $\Dctf$ by the restriction theorem), so
$(f^!N',\varepsilon_{N'})$ and $(G^{\mathrm{pro}}N',\varepsilon_{\nu_Y^*N})$ both
represent $\Hom(Rf_!(-),N')$ on $\Dctf(X,A)$, and the Yoneda lemma gives a unique
isomorphism compatible with the counits. On bounded-below étale-origin
complexes this is the formula $Rf_n^\times=\nu_X^*f^\times R\nu_{Y,*}$ of
[thm-sf-ambient-adjoint-class], since $R\nu_{Y,*}\nu_Y^*N=N$.
