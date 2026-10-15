+++
kind = "proof"
of = "det-lem-int-ext-formula"
+++
(1) By [sk-lem-int-integral-heart](1) truncations stay in
$\Dbc(X,\mathcal O_E)$, so $C$ is a finite extension of shifts of its
cohomology sheaves, which are in $\Cons(X,\mathcal O_E)$. For
$C\in\Cons(X,\mathcal O_E)$ take the stratification of
[sk-lem-int-integral-heart](2), ordered so that each stratum $S$ is open in
the closed union $Z$ of itself and the later strata. The open–closed
localization sequences $0\to u_!u^*F\to F\to i'_*i'^*F\to0$ (exact functors)
filter $C$ by the sheaves $a_!(C|_S)$, and $L=C|_S$ has the stated local form.

(2) Since $i$ is a closed immersion, $a_!=i_*u_!$. The adjunction
$i_*\dashv R\underline\Gamma_Z$, which holds for $\mathcal O_{E,X}$-modules with
the proof of [sk-lem-formal-closed-support], and $u_!\dashv u^*$ give
$R\operatorname{Hom}_X(i_*u_!L,K)\simeq R\operatorname{Hom}_Z(u_!L,R\underline\Gamma_ZK)\simeq R\operatorname{Hom}_S(L,u^*R\underline\Gamma_ZK)$,
and $R\operatorname{Hom}_S(L,-)=R\Gamma(S,\cHom(L,-))$. By
[sk-lem-int-integral-heart](3), $L$ is dualizable on $S$, so tensor–Hom
adjunction identifies $\cHom(L,M)\simeq L^\vee\otimes^{\mathbf L}M$. The dual
$L^\vee$ has Tor amplitude $[0,1]$. Being dualizable, $L^\vee\otimes^{\mathbf L}-$
has adjoints on both sides ($L\otimes^{\mathbf L}-$), so it commutes with all
colimits and all limits, in particular with filtered colimits and derived
inverse limits.
