+++
id = "the-final-theorem-the-abelian-variety-estimate--remark-1"
kind = "remark"
order = 566
+++
*Where this feeds in.*

- **Smooth base change** ([sec-smooth-base-change],
the bad-prime computation of the eight curve assertions): clauses (a)
and (b) supply that the $p$-torsion group scheme of the Jacobian is
finite flat of order $p^{2g_{C_0}}$, so
that the Artin–Schreier kernel is finite; [lem-sc-lang-steinberg]
supplies the surjectivity of the Artin–Schreier map $\wp$ on
$H^1(C_0,\cO)$, and
[lem-sc-fixed-points-finite], [lem-sc-frobenius-fixed-invariance] supply the
$p$-linear fixed-point comparison in characteristic $p$.
- **Monodromy and the curve argument**
([sec-purity-real-sheaves], the Jacobian torsion data of
[def-sc-jacobian]): clause (c) gives
$A[\ell^n](k)\cong(\Z/\ell^n\Z)^{2g}$ and its base-change invariance; clause (d) gives the
divisibility used to see that the transition maps are surjective
and $T_\ell J\cong\Z_\ell^{2g}$.
The Kummer identification
$H^1(C,A_n(1))\cong J[\ell^n](\overline{k}_0)$ and the dual form
$\varprojlim H^1(C,A_n)\cong\Hom_{\Z_\ell}(T_\ell J,\Z_\ell)$ that the
whole real-purity argument runs on are not part of this section; they
belong to the real-purity section, built on [def-sc-jacobian], with the semilinear Galois
action coming from the functoriality of the Jacobian.
- **Jacobian**: the Jacobian itself is constructed later, in
[thm-sc-jacobian-representability] of [sec-picard-framework], resting on
[thm-pc-picard-representable], and over an arbitrary field in
[thm-pd-jacobian-general-field].

The largest external inputs of this section are the theorem of the
cube ([thm-sc-theorem-of-cube]), projectivity ([lem-sc-abelian-variety-projective]),
the rigidity lemma ([lem-sc-rigidity]), the quoted isogeny facts
([lem-sc-mult-n-finite-flat]), the $p$-power order of connected finite group
schemes ([lem-sc-connected-finite-order]), Cartier's theorem
([lem-sc-fg-order-prime-etale]).
