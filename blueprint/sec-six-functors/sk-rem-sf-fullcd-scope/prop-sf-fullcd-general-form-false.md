+++
id = "prop-sf-fullcd-general-form-false"
kind = "theorem"
title = "The all-sheaves, uniform-in-the-base-change form of the comparison bound is false"
order = 2143
tags = ["latex:proposition"]
uses = ["def-sf-fullcd-used-class", "def-weil-pbc-proetale-modules", "def-weil-pbc-proetale-site", "def-weil-pbc-site-comparison-morphism", "prop-sf-comparison-bound-zero", "rem-sf-fullcd-counterexample", "rem-sf-fullcd-general-form", "thm-sf-fullcd-used-class"]
+++
Fix an odd prime $\ell$, let $E/\Ql$ be a finite extension and put
$A=A_{E,1}$, a finite field of characteristic $\ell$. Then the following
statement is false.

1. **($\mathrm{G}$)** Let $X_0$ be a scheme. There is an integer $M$ such
that for *every* object $V\to X_0$ of the small pro-étale site
$X_{0,\Proet}$ of [def-weil-pbc-proetale-site] and *every* sheaf
$\mathcal F$ of $A$-modules on $V_{\Proet}$, in the sense of
[def-weil-pbc-proetale-modules], one has
$$
R^q\nu_{V,*}\mathcal F=0\qquad(q>M),
$$
where $\nu_V:V_{\Proet}\to V_{\Et}$ is the comparison morphism of
[def-weil-pbc-site-comparison-morphism].

More precisely, there exist a scheme $X_0$, an object $U\to X_0$ of
$X_{0,\Proet}$ and, for every integer $M$, a sheaf $\mathcal F$ of
$A$-modules on $U_{\Proet}$ and an integer $q>M$ with
$R^q\nu_{U,*}\mathcal F\neq0$; that is,
$\operatorname{cd}_A(\nu_{U,*})=\infty$. Consequently the general form of
$\operatorname{FullCD}(p,A;c)$ recorded in
[rem-sf-fullcd-general-form] — the form in which the bound is required
for *all* sheaves of $A$-modules and *uniformly over all
pro-étale base changes* — is false, and it is the quantifier over all
sheaves together with the uniformity over the base changes that fails: neither
the bound $M=0$ nor any other bound survives that quantification. The
restriction of the condition to the blueprint's coefficient class
[def-sf-fullcd-used-class] is unaffected and remains the theorem
[thm-sf-fullcd-used-class], with the sharp comparison bound $M=0$ of
[prop-sf-comparison-bound-zero].

## Proof

The construction of [rem-sf-fullcd-counterexample] starts from
$X_0=\Spec\mathbf C$, the set $I$ of cardinality $\aleph_\omega$, the
profinite space $S=\beta I\times\beta I$ and the scheme
$U=\Spec\mathcal C_{\mathrm{lc}}(S,\mathbf C)$, shows that $U\to X_0$ is an
object of $X_{0,\Proet}$, and produces for every integer $M$ a sheaf
$F_G$ of $A$-modules on $U_{\Proet}$ and an integer $q>M$ with
$R^q\nu_{U,*}F_G\neq0$. Taking $V=U$ in the statement
$(\mathrm{G})$ above, no integer $M$ can satisfy it: for each $M$ the
object $U\to X_0$ of $X_{0,\Proet}$ and the sheaf $F_G$ on $U_{\Proet}$
witness the failure in degree $q>M$. Since $U$ is one of the objects
quantified over, both the requirement that the bound be uniform over the base
changes and the requirement that it hold for all sheaves of $A$-modules are
used in the failure, and neither can be recovered by enlarging $M$. The
final clause is the content of [prop-sf-comparison-bound-zero]: the
vanishing on the sheaves of étale origin, which are the coefficient sheaves
of [def-sf-fullcd-used-class], holds with the bound $0$, so the
quantification over all sheaves and not the class form is what fails, exactly
as [rem-sf-fullcd-general-form] now records.
